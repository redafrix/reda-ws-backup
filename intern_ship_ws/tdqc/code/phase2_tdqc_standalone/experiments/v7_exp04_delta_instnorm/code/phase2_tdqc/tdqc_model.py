from __future__ import annotations

from typing import Optional, Tuple

import torch
import torch.nn as nn


class TDQCLSTMCalibrator(nn.Module):
    """
    LSTM TDQC calibrator.

    Input:
        uncertainty feature sequence, [B, T, F]

    Output:
        p_fail sequence, [B, T]
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 128,
        num_layers: int = 1,
        dropout: float = 0.0,
    ):
        super().__init__()
        self.input_dim = int(input_dim)
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

    def forward(self, x: torch.Tensor, lengths: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        x: [B, T, F]
        lengths: optional [B]

        Returns:
            p_fail: [B, T]
        """
        z = self.input_proj(x)

        # Simpler and robust: run padded sequence and mask loss later.
        out, _ = self.rnn(z)
        logits = self.head(out).squeeze(-1)
        p_fail = torch.sigmoid(logits)
        return p_fail

    @torch.no_grad()
    def step(
        self,
        phi_t: torch.Tensor,
        state: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
    ):
        """
        Stateful online inference for one control step.

        phi_t:
            [F] or [B, F]
        state:
            previous LSTM state or None

        Returns:
            p_fail_t, new_state
        """
        if phi_t.ndim == 1:
            phi_t = phi_t.unsqueeze(0)
        # phi_t: [B, F]
        
        x = phi_t.unsqueeze(1)  # [B, 1, F]

        z = self.input_proj(x)
        out, new_state = self.rnn(z, state)
        p_fail = torch.sigmoid(self.head(out).squeeze(-1)).squeeze(1)
        
        return p_fail, new_state


def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())


@torch.no_grad()
def soft_update(target: nn.Module, source: nn.Module, tau: float = 0.005) -> None:
    for p_targ, p_src in zip(target.parameters(), source.parameters()):
        p_targ.data.mul_(1.0 - tau)
        p_targ.data.add_(tau * p_src.data)
