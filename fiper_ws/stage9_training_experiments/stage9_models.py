from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import torch
from torch import nn


@dataclass
class Stage9Dims:
    flat_dim: int
    context_action_dim: int
    action_flat_dim: int
    action_steps: int = 10
    action_dim: int = 7
    history_steps: int = 8
    history_dim: int = 17


class ModelOutput(dict):
    @property
    def risk_logits(self) -> torch.Tensor:
        return self["risk_logits"]


class ResidualBlock(nn.Module):
    def __init__(self, dim: int, dropout: float = 0.1) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.LayerNorm(dim), nn.Linear(dim, dim * 2), nn.GELU(), nn.Dropout(dropout), nn.Linear(dim * 2, dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.net(x)


class MLPModel(nn.Module):
    def __init__(self, input_key: str, input_dim: int, hidden: list[int], dropout: float = 0.1, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        self.input_key = input_key
        layers: list[nn.Module] = []
        dim = input_dim
        for width in hidden:
            layers.extend([nn.Linear(dim, width), nn.GELU(), nn.Dropout(dropout)])
            dim = width
        self.backbone = nn.Sequential(*layers)
        self.risk_head = nn.Linear(dim, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(dim, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        h = self.backbone(batch[self.input_key])
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class ResidualMLPLarge(nn.Module):
    def __init__(self, dims: Stage9Dims, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        width = 512
        self.inp = nn.Linear(dims.flat_dim, width)
        self.blocks = nn.Sequential(*[ResidualBlock(width, 0.12) for _ in range(5)])
        self.risk_head = nn.Linear(width, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(width, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        h = self.blocks(self.inp(batch["flat"]))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class GatedContextActionMLP(nn.Module):
    def __init__(self, dims: Stage9Dims, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        context_dim = dims.context_action_dim - dims.action_flat_dim
        self.context = nn.Sequential(nn.Linear(context_dim, 192), nn.GELU(), nn.Linear(192, 192), nn.GELU())
        self.action = nn.Sequential(nn.Linear(dims.action_flat_dim, 192), nn.GELU(), nn.Linear(192, 192), nn.GELU())
        self.gate = nn.Sequential(nn.Linear(384, 192), nn.Sigmoid())
        self.head = nn.Sequential(nn.Linear(192, 192), nn.GELU(), nn.Dropout(0.12))
        self.risk_head = nn.Linear(192, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(192, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        x = batch["context_action"]
        context_dim = x.shape[-1] - batch["action_flat"].shape[-1]
        c = self.context(x[:, :context_dim])
        a = self.action(batch["action_flat"])
        g = self.gate(torch.cat([c, a], dim=-1))
        h = self.head(g * a + (1.0 - g) * c)
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class HistoryRNN(nn.Module):
    def __init__(self, dims: Stage9Dims, kind: str = "gru", hidden: int = 128, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        rnn_cls = nn.GRU if kind == "gru" else nn.LSTM
        self.rnn = rnn_cls(dims.history_dim, hidden, num_layers=2, dropout=0.10, batch_first=True)
        self.head = nn.Sequential(nn.Linear(dims.context_action_dim + hidden, 256), nn.GELU(), nn.Dropout(0.12), nn.Linear(256, 160), nn.GELU())
        self.risk_head = nn.Linear(160, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(160, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        _, state = self.rnn(batch["history_seq"])
        if isinstance(state, tuple):
            state = state[0]
        h = self.head(torch.cat([batch["context_action"], state[-1]], dim=-1))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class HistoryTransformer(nn.Module):
    def __init__(self, dims: Stage9Dims, width: int, layers: int, heads: int, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        self.hist_proj = nn.Linear(dims.history_dim, width)
        self.action_proj = nn.Linear(dims.action_dim, width)
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 1 + dims.history_steps + dims.action_steps, width) * 0.02)
        enc_layer = nn.TransformerEncoderLayer(width, heads, dim_feedforward=width * 4, dropout=0.10, batch_first=True, activation="gelu")
        self.enc = nn.TransformerEncoder(enc_layer, layers)
        self.context_proj = nn.Linear(dims.context_action_dim, width)
        self.head = nn.Sequential(nn.LayerNorm(width * 2), nn.Linear(width * 2, width), nn.GELU(), nn.Dropout(0.12))
        self.risk_head = nn.Linear(width, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(width, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        bsz = batch["history_seq"].shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), self.hist_proj(batch["history_seq"]), self.action_proj(batch["action_seq"])], dim=1)
        tokens = tokens + self.pos[:, : tokens.shape[1]]
        encoded = self.enc(tokens)[:, 0]
        context = self.context_proj(batch["context_action"])
        h = self.head(torch.cat([encoded, context], dim=-1))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class ActionChunkTransformer(nn.Module):
    def __init__(self, dims: Stage9Dims, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        width = 160
        self.action_proj = nn.Linear(dims.action_dim, width)
        self.pos = nn.Parameter(torch.randn(1, dims.action_steps, width) * 0.02)
        layer = nn.TransformerEncoderLayer(width, 4, dim_feedforward=512, dropout=0.10, batch_first=True, activation="gelu")
        self.enc = nn.TransformerEncoder(layer, 4)
        self.context_proj = nn.Linear(dims.context_action_dim, width)
        self.head = nn.Sequential(nn.Linear(width * 2, 256), nn.GELU(), nn.Dropout(0.12))
        self.risk_head = nn.Linear(256, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(256, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        action = self.enc(self.action_proj(batch["action_seq"]) + self.pos).mean(dim=1)
        context = self.context_proj(batch["context_action"])
        h = self.head(torch.cat([action, context], dim=-1))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class CrossAttentionTransformer(nn.Module):
    def __init__(self, dims: Stage9Dims, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        width = 160
        self.hist_proj = nn.Linear(dims.history_dim, width)
        self.action_proj = nn.Linear(dims.action_dim, width)
        self.attn = nn.MultiheadAttention(width, 4, dropout=0.10, batch_first=True)
        self.hist_layer = nn.TransformerEncoderLayer(width, 4, dim_feedforward=512, dropout=0.10, batch_first=True, activation="gelu")
        self.hist_enc = nn.TransformerEncoder(self.hist_layer, 2)
        self.context_proj = nn.Linear(dims.context_action_dim, width)
        self.head = nn.Sequential(nn.Linear(width * 3, 256), nn.GELU(), nn.Dropout(0.12))
        self.risk_head = nn.Linear(256, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(256, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        hist = self.hist_enc(self.hist_proj(batch["history_seq"]))
        action = self.action_proj(batch["action_seq"])
        attended, _ = self.attn(hist, action, action, need_weights=False)
        h = self.head(torch.cat([hist.mean(dim=1), attended.mean(dim=1), self.context_proj(batch["context_action"])], dim=-1))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class TCNHistory(nn.Module):
    def __init__(self, dims: Stage9Dims, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv1d(dims.history_dim, 96, kernel_size=3, padding=1),
            nn.GELU(),
            nn.Conv1d(96, 128, kernel_size=3, padding=2, dilation=2),
            nn.GELU(),
            nn.AdaptiveAvgPool1d(1),
        )
        self.head = nn.Sequential(nn.Linear(dims.context_action_dim + 128, 256), nn.GELU(), nn.Dropout(0.12))
        self.risk_head = nn.Linear(256, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(256, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        hist = self.conv(batch["history_seq"].transpose(1, 2)).squeeze(-1)
        h = self.head(torch.cat([batch["context_action"], hist], dim=-1))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


class MambaHistory(nn.Module):
    def __init__(self, dims: Stage9Dims, width: int, layers: int, ordinal: bool = False, subtype: bool = False) -> None:
        super().__init__()
        try:
            from mamba_ssm import Mamba
        except Exception as exc:  # noqa: BLE001
            raise ImportError("mamba_ssm is required for Mamba_history models") from exc
        self.proj = nn.Linear(dims.history_dim + dims.action_dim, width)
        # The fused fast path is fragile across causal-conv1d wheel versions. The
        # non-fused path still uses mamba_ssm but avoids the missing cpp_functions
        # API seen on the available cu12/torch2.5 wheels.
        self.blocks = nn.ModuleList([Mamba(d_model=width, d_state=16, d_conv=4, expand=2, use_fast_path=False) for _ in range(layers)])
        self.norm = nn.LayerNorm(width)
        self.context_proj = nn.Linear(dims.context_action_dim, width)
        self.head = nn.Sequential(nn.Linear(width * 2, width), nn.GELU(), nn.Dropout(0.12))
        self.risk_head = nn.Linear(width, 4 if ordinal else 1)
        self.subtype_head = nn.Linear(width, 2) if subtype else None

    def forward(self, batch: dict[str, torch.Tensor]) -> ModelOutput:
        hist = batch["history_seq"]
        action_tail = batch["action_seq"][:, : hist.shape[1]]
        tokens = self.proj(torch.cat([hist, action_tail], dim=-1))
        for block in self.blocks:
            tokens = tokens + block(self.norm(tokens))
        seq = tokens.mean(dim=1)
        context = self.context_proj(batch["context_action"])
        h = self.head(torch.cat([seq, context], dim=-1))
        out = ModelOutput(risk_logits=self.risk_head(h))
        if self.subtype_head is not None:
            out["subtype_logits"] = self.subtype_head(h)
        return out


def create_model(model_name: str, dims: Stage9Dims, target_mode: str) -> nn.Module:
    ordinal = target_mode == "ordinal"
    subtype = target_mode == "subtype_multitask"
    if model_name == "action_only_mlp":
        return MLPModel("action_flat", dims.action_flat_dim, [192, 128], 0.10, ordinal, subtype)
    if model_name == "context_action_mlp":
        return MLPModel("context_action", dims.context_action_dim, [256, 160], 0.10, ordinal, subtype)
    if model_name == "residual_mlp_large":
        return ResidualMLPLarge(dims, ordinal, subtype)
    if model_name == "gated_context_action_mlp":
        return GatedContextActionMLP(dims, ordinal, subtype)
    if model_name == "history_gru_k8":
        return HistoryRNN(dims, "gru", 128, ordinal, subtype)
    if model_name == "history_lstm_k8":
        return HistoryRNN(dims, "lstm", 128, ordinal, subtype)
    if model_name == "small_history_transformer_k8":
        return HistoryTransformer(dims, 96, 2, 4, ordinal, subtype)
    if model_name == "medium_history_transformer_k8":
        return HistoryTransformer(dims, 160, 4, 4, ordinal, subtype)
    if model_name == "large_history_transformer_k8":
        return HistoryTransformer(dims, 256, 6, 8, ordinal, subtype)
    if model_name == "action_chunk_transformer":
        return ActionChunkTransformer(dims, ordinal, subtype)
    if model_name == "history_action_cross_attention_transformer":
        return CrossAttentionTransformer(dims, ordinal, subtype)
    if model_name == "TCN_history_k8":
        return TCNHistory(dims, ordinal, subtype)
    if model_name == "Mamba_history_k8":
        return MambaHistory(dims, 128, 2, ordinal, subtype)
    if model_name == "Mamba_medium_history_k8":
        return MambaHistory(dims, 192, 4, ordinal, subtype)
    raise ValueError(f"unknown model {model_name}")


def model_config(model_name: str, target_mode: str, dims: Stage9Dims) -> dict[str, Any]:
    return {
        "model_name": model_name,
        "target_mode": target_mode,
        "dims": dims.__dict__,
        "uses_forbidden_metadata_as_input": False,
        "input_fields": [
            "candidate_action.candidate_action_normalized or candidate_action_env",
            "current.proprio",
            "current.object_positions_before numeric positions only",
            "history[-8].proprio",
            "history[-8].executed_action",
            "history[-8].reward",
            "history[-8].success",
        ],
        "excluded_from_input": ["task_id", "suite_id", "task_name", "suite", "perturbation_type", "seed", "state_id", "sample_id"],
    }
