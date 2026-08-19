"""Evaluation module with strict held-out test leakage lock and cryptographic binding."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
from torch.utils.data import DataLoader

from .calibration import (
    compute_best_f1_threshold,
    compute_calibration_thresholds,
    compute_conformal_threshold,
    compute_successful_episode_maxima,
)
from .constants import BATCH_SIZE
from .dataset import IsaacMimicWindowDataset
from .metrics import compute_episode_evaluation, compute_row_metrics
from .model import MimicH10RiskMonitor


def sha256_file(path: Path | str) -> str:
    p = Path(path)
    if not p.exists() or not p.is_file():
        return 'N/A'
    hasher = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024 * 4), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


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
    training_summary_path: Path | str,
    spec_path: Path | str,
    output_dir: Path | str,
    device: torch.device,
) -> Dict[str, Any]:
    """Score validation split and freeze validation-derived thresholds with full provenance hashes."""
    derived_dir = Path(derived_dataset_dir)
    ckpt_path = Path(model_checkpoint_path)
    summary_path = Path(training_summary_path)
    s_path = Path(spec_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_scalars = np.load(derived_dir / 'raw/scalar37.npy')
    raw_horizon = np.load(derived_dir / 'raw/horizon10x6.npy')
    labels = np.load(derived_dir / 'labels.npy')
    episode_indices = np.load(derived_dir / 'episode_index.npy')
    decision_indices = np.load(derived_dir / 'decision_index.npy')
    split_indices = np.load(derived_dir / 'split_index.npy')

    norm_file = derived_dir / 'normalization.json'
    manifest_file = derived_dir / 'dataset_manifest_v2.json'
    if not manifest_file.exists():
        manifest_file = derived_dir / 'dataset_manifest.json'

    with open(norm_file) as f:
        norm_params = json.load(f)

    val_row_idx = np.where(split_indices == 1)[0]
    val_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=val_row_idx
    )

    model = MimicH10RiskMonitor().to(device)
    ckpt = torch.load(ckpt_path, map_location=device)
    model.load_state_dict(ckpt['model_state_dict'])
    seed = ckpt.get('seed', 0)
    selected_epoch = ckpt.get('epoch', -1)

    val_scores, val_targets = score_split(model, val_dataset, device)
    val_episodes = episode_indices[val_row_idx]

    row_metrics = compute_row_metrics(val_targets, val_scores)
    success_maxima = compute_successful_episode_maxima(val_scores, val_targets, val_episodes)
    f1_res = compute_best_f1_threshold(val_targets, val_scores)
    thresholds = compute_calibration_thresholds(success_maxima, val_targets, val_scores)

    episode_evals = {}
    for t_name, t_val in thresholds.items():
        episode_evals[t_name] = compute_episode_evaluation(val_scores, val_targets, val_episodes, t_val)

    val_unique_eps = np.unique(val_episodes)
    val_fail_eps = [ep for ep in val_unique_eps if labels[np.where(episode_indices == ep)[0][0]] == 1]

    val_package = {
        'model_checkpoint_path': str(ckpt_path.resolve()),
        'model_checkpoint_sha256': sha256_file(ckpt_path),
        'seed': seed,
        'selected_epoch': selected_epoch,
        'training_summary_sha256': sha256_file(summary_path),
        'dataset_manifest_v2_sha256': sha256_file(manifest_file),
        'normalization_sha256': sha256_file(norm_file),
        'spec_sha256': sha256_file(s_path),
        'validation_rows_count': len(val_row_idx),
        'validation_episodes_count': len(val_unique_eps),
        'validation_failure_episodes_count': len(val_fail_eps),
        'row_metrics': row_metrics,
        'row_best_f1_summary': f1_res,
        'calibrated_thresholds': thresholds,
        'episode_evaluations': episode_evals,
    }

    freeze_file = out_dir / 'FROZEN_VALIDATION_SELECTION.json'
    with open(freeze_file, 'w') as f:
        json.dump(val_package, f, indent=2)

    print(f'Validation calibration saved and frozen at: {freeze_file}')
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
    Strict Leakage Guard: Refuses execution if validation_freeze_path does not exist
    or if checkpoint / dataset / normalization SHA256 hashes do not match frozen values.
    """
    freeze_path = Path(validation_freeze_path)
    if not freeze_path.exists():
        raise RuntimeError(
            f'LEAKAGE GUARD ACTIVE: Held-out test evaluation refused because '
            f'FROZEN_VALIDATION_SELECTION.json was not found at {freeze_path}.'
        )

    with open(freeze_path) as f:
        val_freeze = json.load(f)

    derived_dir = Path(derived_dataset_dir)
    ckpt_path = Path(model_checkpoint_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Verify cryptographic binding
    current_ckpt_sha = sha256_file(ckpt_path)
    if current_ckpt_sha != val_freeze['model_checkpoint_sha256']:
        raise RuntimeError(
            f'LEAKAGE GUARD ACTIVE: Checkpoint SHA256 mismatch! '
            f'Current: {current_ckpt_sha}, Frozen: {val_freeze["model_checkpoint_sha256"]}'
        )

    norm_file = derived_dir / 'normalization.json'
    current_norm_sha = sha256_file(norm_file)
    if current_norm_sha != val_freeze['normalization_sha256']:
        raise RuntimeError(
            f'LEAKAGE GUARD ACTIVE: Normalization SHA256 mismatch! '
            f'Current: {current_norm_sha}, Frozen: {val_freeze["normalization_sha256"]}'
        )

    manifest_file = derived_dir / 'dataset_manifest_v2.json'
    if not manifest_file.exists():
        manifest_file = derived_dir / 'dataset_manifest.json'
    current_manifest_sha = sha256_file(manifest_file)
    if current_manifest_sha != val_freeze['dataset_manifest_v2_sha256']:
        raise RuntimeError(
            f'LEAKAGE GUARD ACTIVE: Dataset Manifest SHA256 mismatch! '
            f'Current: {current_manifest_sha}, Frozen: {val_freeze["dataset_manifest_v2_sha256"]}'
        )

    thresholds = val_freeze['calibrated_thresholds']

    raw_scalars = np.load(derived_dir / 'raw/scalar37.npy')
    raw_horizon = np.load(derived_dir / 'raw/horizon10x6.npy')
    labels = np.load(derived_dir / 'labels.npy')
    episode_indices = np.load(derived_dir / 'episode_index.npy')
    decision_indices = np.load(derived_dir / 'decision_index.npy')
    split_indices = np.load(derived_dir / 'split_index.npy')

    with open(norm_file) as f:
        norm_params = json.load(f)

    test_row_idx = np.where(split_indices == 2)[0]
    test_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=test_row_idx
    )

    model = MimicH10RiskMonitor().to(device)
    ckpt = torch.load(ckpt_path, map_location=device)
    model.load_state_dict(ckpt['model_state_dict'])

    test_scores, test_targets = score_split(model, test_dataset, device)
    test_episodes = episode_indices[test_row_idx]

    row_metrics = compute_row_metrics(test_targets, test_scores)
    episode_evals = {}
    for t_name, t_val in thresholds.items():
        episode_evals[t_name] = compute_episode_evaluation(test_scores, test_targets, test_episodes, t_val)

    test_package = {
        'checkpoint': str(ckpt_path.resolve()),
        'frozen_validation_reference': str(freeze_path.resolve()),
        'test_row_metrics': row_metrics,
        'applied_thresholds': thresholds,
        'test_episode_evaluations': episode_evals,
    }

    with open(out_dir / 'HELD_OUT_TEST_RESULTS.json', 'w') as f:
        json.dump(test_package, f, indent=2)

    return test_package
