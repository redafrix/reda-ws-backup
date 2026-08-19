"""Exact primary model architecture for Isaac Mimic H10 Single-Head monitor."""

from __future__ import annotations

import torch
import torch.nn as nn

from .constants import (
    DROPOUT,
    GRU_HIDDEN_DIM,
    GRU_NUM_LAYERS,
    HISTORY_WINDOW_LENGTH,
    HORIZON_BRANCH_WIDTH,
    HORIZON_CHANNELS,
    HORIZON_STEPS,
    QUERY_EMBED_DIM,
    SCALAR_BRANCH_WIDTH,
    SCALAR_DIM,
    TRANSFORMER_FFN_DIM,
    TRANSFORMER_HEADS,
    TRANSFORMER_LAYERS,
)


class CurrentQueryScalarBranch(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(SCALAR_DIM, SCALAR_BRANCH_WIDTH),
            nn.LayerNorm(SCALAR_BRANCH_WIDTH),
            nn.GELU(),
            nn.Dropout(DROPOUT),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [..., 37] -> [..., 128]
        return self.net(x)


class HorizonBranch(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.proj = nn.Linear(HORIZON_CHANNELS, HORIZON_BRANCH_WIDTH)
        self.pos_embed = nn.Parameter(torch.randn(1, HORIZON_STEPS, HORIZON_BRANCH_WIDTH) * 0.02)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=HORIZON_BRANCH_WIDTH,
            nhead=TRANSFORMER_HEADS,
            dim_feedforward=TRANSFORMER_FFN_DIM,
            dropout=DROPOUT,
            activation="gelu",
            batch_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=TRANSFORMER_LAYERS)

    def forward(self, h: torch.Tensor) -> torch.Tensor:
        # h: [B, 10, 6]
        tokens = self.proj(h) + self.pos_embed  # [B, 10, 128]
        out = self.transformer(tokens)           # [B, 10, 128]
        pooled = out.mean(dim=1)                # [B, 128]
        return pooled


class QueryEncoder(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.scalar_branch = CurrentQueryScalarBranch()
        self.horizon_branch = HorizonBranch()
        self.fusion = nn.Sequential(
            nn.Linear(SCALAR_BRANCH_WIDTH + HORIZON_BRANCH_WIDTH, 128),
            nn.GELU(),
            nn.Dropout(DROPOUT),
            nn.Linear(128, QUERY_EMBED_DIM),
            nn.GELU(),
        )

    def forward(self, scalars: torch.Tensor, horizon: torch.Tensor) -> torch.Tensor:
        # scalars: [B, 37], horizon: [B, 10, 6] -> [B, 64]
        s_feat = self.scalar_branch(scalars)
        h_feat = self.horizon_branch(horizon)
        fused = torch.cat([s_feat, h_feat], dim=-1)
        return self.fusion(fused)


class MimicH10RiskMonitor(nn.Module):
    """Primary 1-layer GRU risk monitor for 8-query temporal windows."""

    def __init__(self) -> None:
        super().__init__()
        self.query_encoder = QueryEncoder()
        self.gru = nn.GRU(
            input_size=QUERY_EMBED_DIM,
            hidden_size=GRU_HIDDEN_DIM,
            num_layers=GRU_NUM_LAYERS,
            batch_first=True,
        )
        self.head = nn.Linear(GRU_HIDDEN_DIM, 1)

    def forward(self, window_scalars: torch.Tensor, window_horizon: torch.Tensor) -> torch.Tensor:
        """
        Args:
            window_scalars: [B, 8, 37] float32 tensor
            window_horizon: [B, 8, 10, 6] float32 tensor
            
        Returns:
            risk_logits: [B] float32 tensor (unnormalized logits)
        """
        batch_size, seq_len, _ = window_scalars.shape
        if seq_len != HISTORY_WINDOW_LENGTH:
            raise ValueError(f"Expected sequence length {HISTORY_WINDOW_LENGTH}, got {seq_len}")

        # Flatten sequence into batch for query encoder
        flat_scalars = window_scalars.reshape(batch_size * seq_len, SCALAR_DIM)
        flat_horizon = window_horizon.reshape(batch_size * seq_len, HORIZON_STEPS, HORIZON_CHANNELS)

        query_embeds = self.query_encoder(flat_scalars, flat_horizon)  # [B * 8, 64]
        seq_embeds = query_embeds.reshape(batch_size, seq_len, QUERY_EMBED_DIM)  # [B, 8, 64]

        gru_out, _ = self.gru(seq_embeds)  # [B, 8, 128]
        final_state = gru_out[:, -1, :]     # [B, 128]

        logits = self.head(final_state).squeeze(-1)  # [B]
        return logits
