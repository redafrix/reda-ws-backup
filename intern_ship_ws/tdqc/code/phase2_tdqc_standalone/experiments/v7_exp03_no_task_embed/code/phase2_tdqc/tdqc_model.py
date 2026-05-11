from __future__ import annotations

from typing import Optional, Tuple

import torch
import torch.nn as nn


class TDQCLSTMCalibrator(nn.Module):
    """LSTM TDQC calibrator — no task embedding (ablation of idea 3)."""

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 256,
        num_layers: int = 2,
        dropout: float = 0.0,
    ):
        super().__init__()
        self.input_dim  = int(input_dim)
        self.hidden_dim = int(hidden_dim)
        self.num_layers = int(num_layers)

        self.input_proj = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=False),
        )

        self.rnn = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )

        self.head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(inplace=False),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )

    def forward(
        self,
        x: torch.Tensor,
        lengths: Optional[torch.Tensor] = None,
        task_ids: Optional[torch.Tensor] = None,  # accepted but ignored
    ) -> torch.Tensor:
        z = self.input_proj(x)
        out, _ = self.rnn(z)
        logits = self.head(out).squeeze(-1)
        return torch.sigmoid(logits)

    @torch.no_grad()
    def step(
        self,
        phi_t: torch.Tensor,
        state: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
        task_id: Optional[torch.Tensor] = None,
    ):
        if phi_t.ndim == 1:
            phi_t = phi_t.unsqueeze(0)
        x = phi_t.unsqueeze(1)
        z = self.input_proj(x)
        out, new_state = self.rnn(z, state)
        p_fail = torch.sigmoid(self.head(out).squeeze(-1)).squeeze(1)
        return p_fail, new_state


def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())
