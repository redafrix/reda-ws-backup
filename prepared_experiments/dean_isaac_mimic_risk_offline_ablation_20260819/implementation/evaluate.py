"""Evaluation module with strict held-out test leakage lock."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch
from torch.utils.data import DataLoader

from .calibration import (
    compute_calibration_thresholds,
    compute_conformal_threshold,
    compute_successful_episode_maxima,
)
from .constants import BATCH_SIZE
from .dataset import IsaacMimicWindowDataset
from .metrics import compute_episode_evaluation, compute_row_metrics
from .model import MimicH10RiskMonitor


def score_split(
    model: MimicH10RiskMonitor,
    dataset: IsaacMimicWindowDataset,
    device: torch.device,
) -> Tuple[np.ndarray, np.ndarray]:
    """Return raw predictions (probabilities) and targets for a dataset."""
    model.eval()
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False, drop_last=False)
    preds = []
    targets = []

    with torch.no_grad():
        for b_s, b_h, b_y in loader:
            b_s = b_s.to(device)
            b_h = b_h.to(device)
            logits = model(b_s, b_h)
            probs = torch.sigmoid(logits).cpu().numpy()
            preds.extend(probs)
            targets.extend(b_y.numpy())

    return np.asarray(preds, dtype=np.float64), np.asarray(targets, dtype=np.int64)


def run_validation_and_calibrate(
    derived_dataset_dir: Path | str,
    model_checkpoint_path: Path | str,
    output_dir: Path | str,
    device: torch.device,
) -> Dict[str, Any]:
    """Score validation split and freeze validation-derived thresholds."""
    derived_dir = Path(derived_dataset_dir)
    ckpt_path = Path(model_checkpoint_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_scalars = np.load(derived_dir / "raw/scalar37.npy")
    raw_horizon = np.load(derived_dir / "raw/horizon10x6.npy")
    labels = np.load(derived_dir / "labels.npy")
    episode_indices = np.load(derived_dir / "episode_index.npy")
    decision_indices = np.load(derived_dir / "decision_index.npy")
    split_indices = np.load(derived_dir / "split_index.npy")

    with open(derived_dir / "normalization.json") as f:
        norm_params = json.load(f)

    val_row_idx = np.where(split_indices == 1)[0]
    val_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=val_row_idx
    )

    model = MimicH10RiskMonitor().to(device)
    ckpt = torch.load(ckpt_path, map_location=device)
    model.load_state_dict(ckpt["model_state_dict"])

    val_scores, val_targets = score_split(model, val_dataset, device)
    val_episodes = episode_indices[val_row_idx]

    row_metrics = compute_row_metrics(val_targets, val_scores)
    success_maxima = compute_successful_episode_maxima(val_scores, val_targets, val_episodes)
    thresholds = compute_calibration_thresholds(success_maxima)

    episode_evals = {}
    for t_name, t_val in thresholds.items():
        episode_evals[t_name] = compute_episode_evaluation(val_scores, val_targets, val_episodes, t_val)

    val_package = {
        "checkpoint": str(ckpt_path),
        "row_metrics": row_metrics,
        "calibrated_thresholds": thresholds,
        "episode_evaluations": episode_evals,
        "success_episodes_count": len(success_maxima),
    }

    freeze_file = out_dir / "FROZEN_VALIDATION_SELECTION.json"
    with open(freeze_file, "w") as f:
        json.dump(val_package, f, indent=2)

    print(f"Validation calibration saved and frozen at: {freeze_file}")
    return val_package


def run_held_out_test(
    derived_dataset_dir: Path | str,
    model_checkpoint_path: Path | str,
    validation_freeze_path: Path | str,
    output_dir: Path | str,
    device: torch.device,
) -> Dict[str, Any]:
    """
    Score held-out test split using frozen validation thresholds.
    Strict Leakage Guard: Refuses execution if validation_freeze_path does not exist.
    """
    freeze_path = Path(validation_freeze_path)
    if not freeze_path.exists():
        raise RuntimeError(
            f"LEAKAGE GUARD ACTIVE: Held-out test evaluation refused because "
            f"FROZEN_VALIDATION_SELECTION.json was not found at {freeze_path}."
        )

    with open(freeze_path) as f:
        val_freeze = json.load(f)

    thresholds = val_freeze["calibrated_thresholds"]

    derived_dir = Path(derived_dataset_dir)
    ckpt_path = Path(model_checkpoint_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_scalars = np.load(derived_dir / "raw/scalar37.npy")
    raw_horizon = np.load(derived_dir / "raw/horizon10x6.npy")
    labels = np.load(derived_dir / "labels.npy")
    episode_indices = np.load(derived_dir / "episode_index.npy")
    decision_indices = np.load(derived_dir / "decision_index.npy")
    split_indices = np.load(derived_dir / "split_index.npy")

    with open(derived_dir / "normalization.json") as f:
        norm_params = json.load(f)

    test_row_idx = np.where(split_indices == 2)[0]
    test_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=test_row_idx
    )

    model = MimicH10RiskMonitor().to(device)
    ckpt = torch.load(ckpt_path, map_location=device)
    model.load_state_dict(ckpt["model_state_dict"])

    test_scores, test_targets = score_split(model, test_dataset, device)
    test_episodes = episode_indices[test_row_idx]

    row_metrics = compute_row_metrics(test_targets, test_scores)
    episode_evals = {}
    for t_name, t_val in thresholds.items():
        episode_evals[t_name] = compute_episode_evaluation(test_scores, test_targets, test_episodes, t_val)

    test_package = {
        "checkpoint": str(ckpt_path),
        "frozen_validation_reference": str(freeze_path),
        "test_row_metrics": row_metrics,
        "applied_thresholds": thresholds,
        "test_episode_evaluations": episode_evals,
    }

    with open(out_dir / "HELD_OUT_TEST_RESULTS.json", "w") as f:
        json.dump(test_package, f, indent=2)

    return test_package
