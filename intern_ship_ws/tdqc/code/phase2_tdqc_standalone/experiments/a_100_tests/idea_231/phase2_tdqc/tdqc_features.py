from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import torch


@dataclass
class TDQCFeatureConfig:
    horizon_decay: float = 0.8
    use_log1p: bool = True
    eps: float = 1e-8


def _log1p_if_needed(x: torch.Tensor, use_log1p: bool) -> torch.Tensor:
    return torch.log1p(torch.clamp_min(x, 0.0)) if use_log1p else x


def aggregate_uncertainty_features(
    path_variance: torch.Tensor,
    last_step_variance: torch.Tensor,
    cfg: TDQCFeatureConfig = TDQCFeatureConfig(),
) -> torch.Tensor:
    """
    Convert Phase 1 variance tensors into a compact TDQC feature vector.

    Inputs
    ------
    path_variance:
        Tensor with shape [H, D] or [B, H, D].
    last_step_variance:
        Tensor with shape [H, D] or [B, H, D].

    Returns
    -------
    Tensor:
        If input is [H, D], returns [F].
        If input is [B, H, D], returns [B, F].
    """
    if path_variance.shape != last_step_variance.shape:
        raise ValueError(
            f"Shape mismatch: path_variance={path_variance.shape}, "
            f"last_step_variance={last_step_variance.shape}"
        )

    squeeze_batch = False
    if path_variance.ndim == 2:
        path_variance = path_variance.unsqueeze(0)
        last_step_variance = last_step_variance.unsqueeze(0)
        squeeze_batch = True

    if path_variance.ndim != 3:
        raise ValueError(f"Expected [H,D] or [B,H,D], got {path_variance.shape}")

    B, H, D = path_variance.shape
    device = path_variance.device
    dtype = path_variance.dtype

    lam = float(cfg.horizon_decay)
    if not (0.0 < lam <= 1.0):
        raise ValueError(f"horizon_decay must be in (0,1], got {lam}")

    weights = lam ** torch.arange(H, device=device, dtype=dtype)
    weights = weights.view(1, H, 1)
    denom = weights.sum() * D + cfg.eps

    weighted_path_mean = (weights * path_variance).sum(dim=(1, 2)) / denom
    weighted_last_mean = (weights * last_step_variance).sum(dim=(1, 2)) / denom

    first_path_mean = path_variance[:, 0, :].mean(dim=-1)
    first_last_mean = last_step_variance[:, 0, :].mean(dim=-1)

    max_path = path_variance.amax(dim=(1, 2))
    max_last = last_step_variance.amax(dim=(1, 2))

    # Optional gripper-specific feature
    gripper_path = path_variance[:, :, -1].mean(dim=-1)
    gripper_last = last_step_variance[:, :, -1].mean(dim=-1)

    feats = torch.stack(
        [
            weighted_path_mean,
            weighted_last_mean,
            first_path_mean,
            first_last_mean,
            max_path,
            max_last,
            gripper_path,
            gripper_last,
        ],
        dim=-1,
    )

    feats = _log1p_if_needed(feats, cfg.use_log1p)

    if squeeze_batch:
        feats = feats.squeeze(0)

    return feats


@torch.no_grad()
def compute_feature_stats(features: torch.Tensor, mask: torch.Tensor | None = None) -> Dict[str, torch.Tensor]:
    """
    Compute train-set normalization statistics.
    """
    if mask is None:
        flat = features.reshape(-1, features.shape[-1])
    else:
        flat = features[mask.bool()]

    mean = flat.mean(dim=0)
    std = flat.std(dim=0).clamp_min(1e-6)
    return {"mean": mean, "std": std}


def normalize_features(features: torch.Tensor, mean: torch.Tensor, std: torch.Tensor) -> torch.Tensor:
    return (features - mean.to(features.device)) / std.to(features.device)
