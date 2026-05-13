from __future__ import annotations

from pathlib import Path
from typing import Optional

import torch

from .model import TDQCCalibrator


class OnlineTDQCRisk:
    """Stateful online wrapper for the trained Phase-2 calibrator."""

    def __init__(self, checkpoint_path: str | Path, device: str | torch.device = "cpu") -> None:
        ckpt = torch.load(checkpoint_path, map_location=device)
        self.device = torch.device(device)
        self.model = TDQCCalibrator(
            input_dim=int(ckpt["input_dim"]),
            hidden_dim=int(ckpt["hidden_dim"]),
            num_layers=int(ckpt["num_layers"]),
            dropout=float(ckpt.get("dropout", 0.0)),
            use_gru=bool(ckpt.get("use_gru", False)),
            use_attention=bool(ckpt.get("use_attention", False)),
            attention_heads=int(ckpt.get("attention_heads", 4)),
            attention_dropout=ckpt.get("attention_dropout", None),
            history_window=int(ckpt.get("history_window", 0)),
            input_proj_dim=int(ckpt.get("input_proj_dim", 0)),
            input_dropout=float(ckpt.get("input_dropout", 0.0)),
        ).to(self.device)
        self.model.window_eval_batch_size = int(ckpt.get("window_eval_batch_size", 0))
        self.model.load_state_dict(ckpt["model_state_dict"])
        self.model.eval()
        self.feature_mean = ckpt["feature_mean"].to(self.device)
        self.feature_std = ckpt["feature_std"].to(self.device)
        self.feature_keys = ckpt.get("feature_keys")
        self.history_window = int(ckpt.get("history_window", 0))
        self.add_temporal_features = bool(ckpt.get("add_temporal_features", False))
        self.temporal_feature_source = ckpt.get("temporal_feature_source", "mean_last_var")
        self.base_feature_dim = (
            len(self.feature_keys) - 7
            if self.add_temporal_features and self.feature_keys is not None
            else len(self.feature_mean)
        )
        self.reset()

    def reset(self) -> None:
        self.history = []
        self.raw_history = []

    def _augment_current_phi(self, phi_t: torch.Tensor) -> torch.Tensor:
        self.raw_history.append(phi_t)
        if not self.add_temporal_features:
            return phi_t
        if self.feature_keys is None or self.temporal_feature_source not in self.feature_keys:
            raise ValueError("Temporal feature checkpoint is missing compatible feature_keys")
        source_idx = self.feature_keys.index(self.temporal_feature_source)
        values = torch.stack([phi[source_idx] for phi in self.raw_history]).to(self.device)
        current = values[-1]
        prev = values[-2] if len(values) > 1 else current
        delta = current - prev

        def recent(window: int) -> torch.Tensor:
            return values[-window:]

        roll5 = recent(5)
        roll10 = recent(10)
        if len(roll10) >= 2:
            x = torch.arange(len(roll10), dtype=roll10.dtype, device=self.device)
            x = x - x.mean()
            denom = (x * x).sum().clamp_min(1e-12)
            slope10 = (x * (roll10 - roll10.mean())).sum() / denom
        else:
            slope10 = torch.zeros((), dtype=phi_t.dtype, device=self.device)
        diffs = values.diff() if len(values) > 1 else values.new_zeros(1)
        max_spike10 = torch.clamp(diffs[-10:], min=0.0).max()
        extras = torch.stack(
            [
                delta,
                roll5.mean(),
                roll5.std(unbiased=False),
                roll10.mean(),
                roll10.std(unbiased=False),
                slope10,
                max_spike10,
            ]
        )
        return torch.cat([phi_t[: self.base_feature_dim], extras], dim=0)

    @torch.no_grad()
    def update(self, phi_t: torch.Tensor) -> float:
        """Append one feature vector and return current failure probability."""
        phi_t = phi_t.to(self.device, dtype=torch.float32)
        phi_t = self._augment_current_phi(phi_t)
        phi_t = (phi_t - self.feature_mean) / self.feature_std
        self.history.append(phi_t)
        if self.history_window > 0:
            self.history = self.history[-self.history_window :]
            real_len = len(self.history)
            if real_len < self.history_window:
                pad = [torch.zeros_like(phi_t) for _ in range(self.history_window - real_len)]
                items = pad + self.history
                mask = torch.tensor(
                    [0.0] * len(pad) + [1.0] * real_len,
                    dtype=torch.float32,
                    device=self.device,
                ).unsqueeze(0)
            else:
                items = self.history
                mask = torch.ones(1, self.history_window, dtype=torch.float32, device=self.device)
            x = torch.stack(items, dim=0).unsqueeze(0)
        else:
            x = torch.stack(self.history, dim=0).unsqueeze(0)
            mask = None
        q = self.model(x, mask)[0, -1]
        return float(q.cpu())
