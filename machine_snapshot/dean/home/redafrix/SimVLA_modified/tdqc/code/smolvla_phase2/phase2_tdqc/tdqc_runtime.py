from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

import torch

from phase2_tdqc.tdqc_features import TDQCFeatureConfig, aggregate_uncertainty_features, normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator


class TDQCRiskRuntime:
    def __init__(self, ckpt_path: str | Path, device: str = "cuda"):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        ckpt = torch.load(ckpt_path, map_location="cpu")
        cfg = ckpt["config"]

        self.model = TDQCLSTMCalibrator(
            input_dim=cfg["input_dim"],
            hidden_dim=cfg["hidden_dim"],
            num_layers=cfg["num_layers"],
            dropout=cfg["dropout"],
        ).to(self.device)
        self.model.load_state_dict(ckpt["model"])
        self.model.eval()

        self.mean = ckpt["mean"].to(self.device)
        self.std = ckpt["std"].to(self.device)
        self.feature_cfg = TDQCFeatureConfig()
        self.state: Optional[Tuple[torch.Tensor, torch.Tensor]] = None

    def reset(self):
        self.state = None

    @torch.no_grad()
    def update(self, path_variance: torch.Tensor, last_step_variance: torch.Tensor) -> torch.Tensor:
        phi = aggregate_uncertainty_features(
            path_variance.to(self.device),
            last_step_variance.to(self.device),
            self.feature_cfg,
        )
        phi = normalize_features(phi, self.mean, self.std)
        p_fail, self.state = self.model.step(phi, self.state)
        return p_fail
