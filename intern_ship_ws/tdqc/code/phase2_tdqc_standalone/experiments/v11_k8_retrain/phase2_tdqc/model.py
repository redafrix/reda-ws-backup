from __future__ import annotations

from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class TDQCCalibrator(nn.Module):
    """Small RNN-TDQC calibrator.

    Input:  sequence of Phase-1 uncertainty features, shape [B, T, F]
    Output: failure probability at every step, shape [B, T]

    We intentionally predict failure directly:
        q_t = P(final episode failure | uncertainty history up to t)
    This avoids switching signs later when using the predictor for early stopping.
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 128,
        num_layers: int = 2,
        dropout: float = 0.15,
        use_gru: bool = False,
        use_attention: bool = False,
        attention_heads: int = 4,
        attention_dropout: float | None = None,
        history_window: int = 0,
        input_proj_dim: int = 0,
        input_dropout: float = 0.0,
    ) -> None:
        super().__init__()
        if use_attention and hidden_dim % attention_heads != 0:
            raise ValueError("hidden_dim must be divisible by attention_heads when use_attention=True")
        if history_window < 0:
            raise ValueError("history_window must be >= 0")
        rnn_cls = nn.GRU if use_gru else nn.LSTM
        effective_dropout = dropout if num_layers > 1 else 0.0
        self.use_attention = use_attention
        self.history_window = history_window
        self.input_proj_dim = int(input_proj_dim)
        rnn_input_dim = input_dim
        self.input_dropout = nn.Dropout(input_dropout) if input_dropout > 0.0 else nn.Identity()
        if self.input_proj_dim > 0:
            self.input_encoder = nn.Sequential(
                nn.Linear(input_dim, self.input_proj_dim),
                nn.LayerNorm(self.input_proj_dim),
                nn.GELU(),
            )
            rnn_input_dim = self.input_proj_dim
        else:
            self.input_encoder = nn.Identity()
        self.rnn = rnn_cls(
            input_size=rnn_input_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=effective_dropout,
        )
        if use_attention:
            self.attention = nn.MultiheadAttention(
                embed_dim=hidden_dim,
                num_heads=attention_heads,
                dropout=dropout if attention_dropout is None else attention_dropout,
                batch_first=True,
            )
            self.attention_norm = nn.LayerNorm(hidden_dim)
        self.head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(inplace=False),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, features: torch.Tensor, valid_masks: torch.Tensor | None = None) -> torch.Tensor:
        features = self.input_dropout(self.input_encoder(features))
        h, _ = self.rnn(features)
        if self.use_attention:
            T = h.shape[1]
            causal_mask = torch.ones(T, T, dtype=torch.bool, device=h.device).triu(1)
            key_padding_mask = None if valid_masks is None else valid_masks <= 0
            attended, _ = self.attention(
                h,
                h,
                h,
                attn_mask=causal_mask,
                key_padding_mask=key_padding_mask,
                need_weights=False,
            )
            h = self.attention_norm(h + attended)
        logits = self.head(h).squeeze(-1)
        return torch.sigmoid(logits)


def predict_tdqc_sequence(
    model: TDQCCalibrator,
    features: torch.Tensor,
    valid_masks: torch.Tensor | None = None,
    history_window: int | None = None,
    window_batch_size: int | None = None,
) -> torch.Tensor:
    """Predict q_t from either full history or fixed windows ending at each t."""
    window = model.history_window if history_window is None else history_window
    if window <= 0:
        return model(features, valid_masks)

    B, T, F_dim = features.shape
    left_pad = window - 1
    padded_features = F.pad(features, (0, 0, left_pad, 0), mode="constant", value=0.0)
    feature_windows = padded_features.unfold(dimension=1, size=window, step=1).permute(0, 1, 3, 2)
    flat_features = feature_windows.reshape(B * T, window, F_dim)

    flat_masks = None
    if valid_masks is not None:
        padded_masks = F.pad(valid_masks, (left_pad, 0), mode="constant", value=0.0)
        mask_windows = padded_masks.unfold(dimension=1, size=window, step=1)
        flat_masks = mask_windows.reshape(B * T, window)

    if window_batch_size is None or window_batch_size <= 0 or flat_features.shape[0] <= window_batch_size:
        q_windows = model(flat_features, flat_masks)[:, -1]
    else:
        chunks = []
        for start in range(0, flat_features.shape[0], window_batch_size):
            end = start + window_batch_size
            mask_chunk = None if flat_masks is None else flat_masks[start:end]
            chunks.append(model(flat_features[start:end], mask_chunk)[:, -1])
        q_windows = torch.cat(chunks, dim=0)
    return q_windows.reshape(B, T)


@torch.no_grad()
def build_td0_targets(
    target_q: torch.Tensor,
    failure_labels: torch.Tensor,
    lengths: torch.Tensor,
) -> torch.Tensor:
    """Build TD(0) targets for failure-probability calibration.

    For every valid non-terminal step t:
        target_t = q_target(t+1)
    For the final valid step:
        target_T = Y_fail
    """
    targets = torch.zeros_like(target_q)
    B, T = target_q.shape
    for b in range(B):
        L = int(lengths[b].item())
        if L <= 0:
            continue
        if L > 1:
            targets[b, : L - 1] = target_q[b, 1:L]
        targets[b, L - 1] = failure_labels[b]
    return targets


def td0_brier_loss(
    online_q: torch.Tensor,
    target_q: torch.Tensor,
    failure_labels: torch.Tensor,
    valid_masks: torch.Tensor,
    lengths: torch.Tensor,
    *,
    failure_weight: float = 1.0,
    success_weight: float = 1.0,
    episode_balanced: bool = False,
) -> tuple[torch.Tensor, Dict[str, float]]:
    targets = build_td0_targets(target_q.detach(), failure_labels, lengths)
    episode_weights = torch.where(
        failure_labels[:, None] > 0.5,
        torch.as_tensor(failure_weight, dtype=online_q.dtype, device=online_q.device),
        torch.as_tensor(success_weight, dtype=online_q.dtype, device=online_q.device),
    )
    per_step = (online_q - targets).pow(2)
    if episode_balanced:
        step_denom = valid_masks.sum(dim=1).clamp_min(1.0)
        episode_losses = (per_step * valid_masks).sum(dim=1) / step_denom
        episode_weights = episode_weights.squeeze(1)
        loss = (episode_losses * episode_weights).sum() / episode_weights.sum().clamp_min(1.0)
        weighted_mask = valid_masks * episode_weights[:, None]
    else:
        weighted_mask = valid_masks * episode_weights
        denom = weighted_mask.sum().clamp_min(1.0)
        loss = (per_step * weighted_mask).sum() / denom

    terminal_preds = []
    terminal_targets = []
    for b in range(online_q.shape[0]):
        L = int(lengths[b].item())
        if L > 0:
            terminal_preds.append(online_q[b, L - 1])
            terminal_targets.append(failure_labels[b])
    if terminal_preds:
        term_q = torch.stack(terminal_preds)
        term_y = torch.stack(terminal_targets)
        terminal_brier = F.mse_loss(term_q, term_y).item()
    else:
        terminal_brier = float("nan")

    logs = {
        "td0_brier_loss": float(loss.detach().cpu()),
        "terminal_brier": terminal_brier,
        "mean_q": float((online_q * valid_masks).sum().detach().cpu() / valid_masks.sum().clamp_min(1.0).detach().cpu()),
    }
    return loss, logs


def mc_brier_loss(
    online_q: torch.Tensor,
    failure_labels: torch.Tensor,
    valid_masks: torch.Tensor,
    lengths: torch.Tensor,
    *,
    failure_weight: float = 1.0,
    success_weight: float = 1.0,
    episode_balanced: bool = False,
) -> tuple[torch.Tensor, Dict[str, float]]:
    """Monte Carlo Brier loss for failure-probability calibration.

    Every valid step t in the sequence is supervised to predict the final
    episode failure label:
        target_t = Y_fail
    """
    targets = failure_labels[:, None].expand_as(online_q)
    episode_weights = torch.where(
        failure_labels[:, None] > 0.5,
        torch.as_tensor(failure_weight, dtype=online_q.dtype, device=online_q.device),
        torch.as_tensor(success_weight, dtype=online_q.dtype, device=online_q.device),
    )
    per_step = (online_q - targets).pow(2)

    if episode_balanced:
        step_denom = valid_masks.sum(dim=1).clamp_min(1.0)
        episode_losses = (per_step * valid_masks).sum(dim=1) / step_denom
        episode_weights = episode_weights.squeeze(1)
        loss = (episode_losses * episode_weights).sum() / episode_weights.sum().clamp_min(1.0)
        weighted_mask = valid_masks * episode_weights[:, None]
    else:
        weighted_mask = valid_masks * episode_weights
        denom = weighted_mask.sum().clamp_min(1.0)
        loss = (per_step * weighted_mask).sum() / denom

    terminal_preds = []
    terminal_targets = []
    for b in range(online_q.shape[0]):
        L = int(lengths[b].item())
        if L > 0:
            terminal_preds.append(online_q[b, L - 1])
            terminal_targets.append(failure_labels[b])
    if terminal_preds:
        term_q = torch.stack(terminal_preds)
        term_y = torch.stack(terminal_targets)
        terminal_brier = F.mse_loss(term_q, term_y).item()
    else:
        terminal_brier = float("nan")

    logs = {
        "mc_brier_loss": float(loss.detach().cpu()),
        "terminal_brier": terminal_brier,
        "mean_q": float((online_q * valid_masks).sum().detach().cpu() / valid_masks.sum().clamp_min(1.0).detach().cpu()),
    }
    return loss, logs


@torch.no_grad()
def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())


@torch.no_grad()
def soft_update(target: nn.Module, source: nn.Module, tau: float) -> None:
    for target_param, source_param in zip(target.parameters(), source.parameters()):
        target_param.data.mul_(1.0 - tau).add_(source_param.data, alpha=tau)
