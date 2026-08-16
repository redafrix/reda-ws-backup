"""Exact promoted H10/TopK8 temporal risk-head architecture."""

from __future__ import annotations

import torch
import torch.nn as nn


class SeqRiskModel(nn.Module):
    def __init__(
        self,
        hist_dim: int = 21,
        action_dim: int = 7,
        static_dim: int = 51,
        width: int = 128,
        layers: int = 3,
        heads: int = 4,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        layer = nn.TransformerEncoderLayer(
            width,
            heads,
            width * 4,
            dropout=dropout,
            batch_first=True,
            activation="gelu",
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(layer, layers)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat(
            [self.hist_proj(batch["history"]), self.action_proj(batch["action"])],
            dim=1,
        )
        batch_size = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(batch_size, -1, -1), tokens], dim=1)
        sequence = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(batch["static"])
        return self.head(torch.cat([sequence, static], dim=-1)).squeeze(-1)
