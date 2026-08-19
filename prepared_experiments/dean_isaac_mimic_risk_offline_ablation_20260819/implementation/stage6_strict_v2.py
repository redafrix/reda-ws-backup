"""Stage 6 Strict Mimic Fidelity Baseline V2: Build, Train, and Validate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
from torch.utils.data import DataLoader

from .constants import (
    SEEDS,
    BATCH_SIZE,
    EPOCHS,
    LR,
    WEIGHT_DECAY,
    GRAD_CLIP_NORM,
    HORIZON_STEPS,
    HORIZON_CHANNELS,
)
from .dataset import IsaacMimicWindowDataset
from .model import MimicH10RiskMonitor
from .evaluate import (
    compute_row_metrics,
    compute_successful_episode_maxima,
    compute_best_f1_threshold,
    compute_calibration_thresholds,
    compute_episode_evaluation,
    score_split,
    sha256_file,
)


STRICT_V2_EXP_NAME = "isaac_mimic_h10_strict_missingdyn_v2"


def build_strict_v2_dataset(
    v1_derived_dir: Path,
    v2_derived_dir: Path,
    snapshot_dir: Path,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    print("1. Building Strict V2 dataset arrays...")
    v2_derived_dir.mkdir(parents=True, exist_ok=True)
    raw_v2_dir = v2_derived_dir / "raw"
    raw_v2_dir.mkdir(parents=True, exist_ok=True)

    # Load V1 arrays
    v1_scalars = np.load(v1_derived_dir / "raw/scalar37.npy")
    v1_horizon = np.load(v1_derived_dir / "raw/horizon10x6.npy")
    labels = np.load(v1_derived_dir / "labels.npy")
    ep_idx = np.load(v1_derived_dir / "episode_index.npy")
    dec_idx = np.load(v1_derived_dir / "decision_index.npy")
    split_idx = np.load(v1_derived_dir / "split_index.npy")
    with open(v1_derived_dir / "episode_ids.json") as f:
        ep_ids = json.load(f)

    n_rows = len(labels)
    assert n_rows == 75603
    assert v1_scalars.shape == (75603, 37)
    assert v1_horizon.shape == (75603, 10, 6)

    # Construct V2 scalar37:
    # dims 0..8: copy from V1
    # dims 9..33: exact 0.0
    # dims 34..36: copy from V1
    v2_scalars = np.zeros((75603, 37), dtype=np.float32)
    v2_scalars[:, 0:9] = v1_scalars[:, 0:9]
    v2_scalars[:, 34:37] = v1_scalars[:, 34:37]

    v2_horizon = v1_horizon.copy().astype(np.float32)

    # Parity check
    s0_8_diff = float(np.max(np.abs(v2_scalars[:, 0:9] - v1_scalars[:, 0:9])))
    s34_36_diff = float(np.max(np.abs(v2_scalars[:, 34:37] - v1_scalars[:, 34:37])))
    h_diff = float(np.max(np.abs(v2_horizon - v1_horizon)))
    disabled_zeros = bool(np.all(v2_scalars[:, 9:34] == 0.0))

    assert s0_8_diff == 0.0, f"s0_8 diff: {s0_8_diff}"
    assert s34_36_diff == 0.0, f"s34_36 diff: {s34_36_diff}"
    assert h_diff == 0.0, f"h diff: {h_diff}"
    assert disabled_zeros, "Disabled channels are not all zero!"

    # Save arrays
    np.save(raw_v2_dir / "scalar37.npy", v2_scalars)
    np.save(raw_v2_dir / "horizon10x6.npy", v2_horizon)
    np.save(v2_derived_dir / "labels.npy", labels)
    np.save(v2_derived_dir / "episode_index.npy", ep_idx)
    np.save(v2_derived_dir / "decision_index.npy", dec_idx)
    np.save(v2_derived_dir / "split_index.npy", split_idx)
    with open(v2_derived_dir / "episode_ids.json", "w") as f:
        json.dump(ep_ids, f, indent=2)

    parity_audit = {
        "total_rows": n_rows,
        "scalar_0_to_8_exact_equal": bool(np.array_equal(v2_scalars[:, 0:9], v1_scalars[:, 0:9])),
        "scalar_0_to_8_max_diff": s0_8_diff,
        "scalar_34_to_36_exact_equal": bool(np.array_equal(v2_scalars[:, 34:37], v1_scalars[:, 34:37])),
        "scalar_34_to_36_max_diff": s34_36_diff,
        "horizon_exact_equal": bool(np.array_equal(v2_horizon, v1_horizon)),
        "horizon_max_diff": h_diff,
        "disabled_channels_9_to_33_all_zero": disabled_zeros,
        "labels_exact_equal": bool(np.array_equal(labels, np.load(v1_derived_dir / "labels.npy"))),
        "split_index_exact_equal": bool(np.array_equal(split_idx, np.load(v1_derived_dir / "split_index.npy"))),
        "episode_index_exact_equal": bool(np.array_equal(ep_idx, np.load(v1_derived_dir / "episode_index.npy"))),
        "decision_index_exact_equal": bool(np.array_equal(dec_idx, np.load(v1_derived_dir / "decision_index.npy"))),
        "episode_ids_exact_equal": ep_ids == json.load(open(v1_derived_dir / "episode_ids.json")),
        "parity_passed": True,
    }
    with open(snapshot_dir / "STRICT_V2_AVAILABLE_FEATURE_PARITY.json", "w") as f:
        json.dump(parity_audit, f, indent=2)

    print("2. Fitting Strict V2 Normalization from TRAIN rows...")
    train_mask = (split_idx == 0)
    train_scalars = v2_scalars[train_mask]
    train_horizon = v2_horizon[train_mask]

    scalar_mean = np.zeros(37, dtype=np.float32)
    scalar_std = np.ones(37, dtype=np.float32)

    # Active dims 0..8
    scalar_mean[0:9] = np.mean(train_scalars[:, 0:9], axis=0)
    s_std_0_8 = np.std(train_scalars[:, 0:9], axis=0)
    scalar_std[0:9] = np.maximum(s_std_0_8, 1e-6)

    # Disabled dims 9..33: mean 0.0, std 1.0 (already set)

    # Active dims 34..36
    scalar_mean[34:37] = np.mean(train_scalars[:, 34:37], axis=0)
    s_std_34_36 = np.std(train_scalars[:, 34:37], axis=0)
    scalar_std[34:37] = np.maximum(s_std_34_36, 1e-6)

    # Horizon per-channel mean/std
    horizon_mean = np.mean(train_horizon, axis=(0, 1))  # [6]
    horizon_std = np.maximum(np.std(train_horizon, axis=(0, 1)), 1e-6)  # [6]

    norm_dict = {
        "scalar_mean": scalar_mean.tolist(),
        "scalar_std": scalar_std.tolist(),
        "horizon_mean": horizon_mean.tolist(),
        "horizon_std": horizon_std.tolist(),
        "disabled_scalar_channel_indices": list(range(9, 34)),
        "disabled_scalar_channels_mean": 0.0,
        "disabled_scalar_channels_std": 1.0,
    }
    norm_p = v2_derived_dir / "normalization.json"
    with open(norm_p, "w") as f:
        json.dump(norm_dict, f, indent=2)
    norm_sha = sha256_file(norm_p)
    with open(snapshot_dir / "STRICT_V2_NORMALIZATION.json", "w") as f:
        json.dump(norm_dict, f, indent=2)

    print("3. Writing Strict V2 Dataset Manifest...")
    array_hashes = {
        "scalar37.npy": sha256_file(raw_v2_dir / "scalar37.npy"),
        "horizon10x6.npy": sha256_file(raw_v2_dir / "horizon10x6.npy"),
        "labels.npy": sha256_file(v2_derived_dir / "labels.npy"),
        "episode_index.npy": sha256_file(v2_derived_dir / "episode_index.npy"),
        "decision_index.npy": sha256_file(v2_derived_dir / "decision_index.npy"),
        "split_index.npy": sha256_file(v2_derived_dir / "split_index.npy"),
        "episode_ids.json": sha256_file(v2_derived_dir / "episode_ids.json"),
    }

    manifest = {
        "experiment_name": STRICT_V2_EXP_NAME,
        "parent_v1_dataset_manifest_sha256": "043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3",
        "spec_reference": "STRICT_MIMIC_FIDELITY_BASELINE_SPEC_V2.md",
        "disabled_channel_reason": "UNAVAILABLE_CROSS_CANDIDATE_DENOISING_INTERNALS_NOT_REPLACED",
        "disabled_channel_indices": list(range(9, 34)),
        "counts": {
            "total_episodes": 4000,
            "total_rows": 75603,
            "train_episodes": 2800,
            "val_episodes": 600,
            "test_episodes": 600,
            "train_rows": 52825,
            "val_rows": 11410,
            "test_rows": 11368,
            "train_failure_episodes": 64,
            "val_failure_episodes": 14,
            "test_failure_episodes": 14,
        },
        "heavy_array_hashes": array_hashes,
        "normalization_sha256": norm_sha,
    }
    manifest_p = v2_derived_dir / "dataset_manifest.json"
    with open(manifest_p, "w") as f:
        json.dump(manifest, f, indent=2)
    manifest_sha = sha256_file(manifest_p)
    with open(snapshot_dir / "STRICT_V2_DATASET_MANIFEST.json", "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Strict V2 dataset ready! Manifest SHA256: {manifest_sha}")
    return parity_audit, manifest


def train_strict_v2_seed(
    seed: int,
    v2_derived_dir: Path,
    model_dir: Path,
    device: torch.device,
) -> Dict[str, Any]:
    print(f"--- Training Strict V2 Seed {seed} ---")
    model_dir.mkdir(parents=True, exist_ok=True)

    # Set all random seeds
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)

    raw_scalars = np.load(v2_derived_dir / "raw/scalar37.npy")
    raw_horizon = np.load(v2_derived_dir / "raw/horizon10x6.npy")
    labels = np.load(v2_derived_dir / "labels.npy")
    episode_indices = np.load(v2_derived_dir / "episode_index.npy")
    decision_indices = np.load(v2_derived_dir / "decision_index.npy")
    split_indices = np.load(v2_derived_dir / "split_index.npy")

    with open(v2_derived_dir / "normalization.json") as f:
        norm_params = json.load(f)

    train_row_idx = np.where(split_indices == 0)[0]
    val_row_idx = np.where(split_indices == 1)[0]

    n_train_pos = int(np.sum(labels[train_row_idx] == 1))
    n_train_neg = int(np.sum(labels[train_row_idx] == 0))
    pos_weight_val = float(n_train_neg / max(1, n_train_pos))

    train_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=train_row_idx
    )
    val_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=val_row_idx
    )

    g = torch.Generator()
    g.manual_seed(seed)

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        generator=g,
        num_workers=0,
        pin_memory=True if device.type == "cuda" else False,
    )

    model = MimicH10RiskMonitor().to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=LR,
        weight_decay=WEIGHT_DECAY,
    )
    criterion = torch.nn.BCEWithLogitsLoss(pos_weight=torch.tensor([pos_weight_val], device=device))

    epoch_logs = []
    best_val_auprc = -1.0
    best_epoch = -1
    best_ckpt_path = model_dir / "best_model.pt"

    for epoch in range(EPOCHS):
        model.train()
        train_loss_sum = 0.0
        n_batches = 0

        for scalars_w, horizon_w, targets_b in train_loader:
            scalars_w = scalars_w.to(device, non_blocking=True)
            horizon_w = horizon_w.to(device, non_blocking=True)
            targets_b = targets_b.to(device, non_blocking=True)

            optimizer.zero_grad()
            logits = model(scalars_w, horizon_w)
            loss = criterion(logits, targets_b)
            loss.backward()

            torch.nn.utils.clip_grad_norm_(model.parameters(), GRAD_CLIP_NORM)
            optimizer.step()

            train_loss_sum += float(loss.item())
            n_batches += 1

        avg_train_loss = train_loss_sum / max(1, n_batches)

        # Validation scoring
        val_scores, val_targets = score_split(model, val_dataset, device)
        val_metrics = compute_row_metrics(val_targets, val_scores)
        val_auroc = val_metrics["auroc"]
        val_auprc = val_metrics["auprc"]

        # Checkpoint every epoch
        ep_ckpt_path = model_dir / f"checkpoint_epoch_{epoch:02d}.pt"
        torch.save(
            {
                "epoch": epoch,
                "seed": seed,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "val_auroc": val_auroc,
                "val_auprc": val_auprc,
            },
            ep_ckpt_path,
        )

        # Earliest tie selection on highest val AUPRC
        if val_auprc > best_val_auprc:
            best_val_auprc = val_auprc
            best_epoch = epoch
            torch.save(
                {
                    "epoch": epoch,
                    "seed": seed,
                    "model_state_dict": model.state_dict(),
                    "val_auroc": val_auroc,
                    "val_auprc": val_auprc,
                },
                best_ckpt_path,
            )

        epoch_logs.append({
            "epoch": epoch,
            "train_loss": avg_train_loss,
            "val_auroc": val_auroc,
            "val_auprc": val_auprc,
        })
        print(f"Seed {seed} | Ep {epoch:02d}/{EPOCHS-1:02d} | TrainLoss: {avg_train_loss:.4f} | Val AUROC: {val_auroc:.4f} | Val AUPRC: {val_auprc:.4f} | Best: Ep {best_epoch:02d} ({best_val_auprc:.4f})")

    best_ckpt_sha = sha256_file(best_ckpt_path)
    summary_data = {
        "experiment_name": STRICT_V2_EXP_NAME,
        "seed": seed,
        "total_epochs": EPOCHS,
        "best_epoch": best_epoch,
        "best_val_auprc": best_val_auprc,
        "best_model_checkpoint_path": str(best_ckpt_path),
        "best_model_checkpoint_sha256": best_ckpt_sha,
        "epoch_logs": epoch_logs,
    }
    summary_path = model_dir / "training_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary_data, f, indent=2)

    return summary_data


def calibrate_and_freeze_validation(
    seed: int,
    v2_derived_dir: Path,
    model_dir: Path,
    val_out_dir: Path,
    snapshot_dir: Path,
    device: torch.device,
) -> Dict[str, Any]:
    print(f"--- Calibrating and Freezing Validation for Seed {seed} ---")
    val_out_dir.mkdir(parents=True, exist_ok=True)

    raw_scalars = np.load(v2_derived_dir / "raw/scalar37.npy")
    raw_horizon = np.load(v2_derived_dir / "raw/horizon10x6.npy")
    labels = np.load(v2_derived_dir / "labels.npy")
    episode_indices = np.load(v2_derived_dir / "episode_index.npy")
    decision_indices = np.load(v2_derived_dir / "decision_index.npy")
    split_indices = np.load(v2_derived_dir / "split_index.npy")

    with open(v2_derived_dir / "normalization.json") as f:
        norm_params = json.load(f)

    val_row_idx = np.where(split_indices == 1)[0]
    val_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=val_row_idx
    )

    ckpt_path = model_dir / "best_model.pt"
    ckpt = torch.load(ckpt_path, map_location=device)
    model = MimicH10RiskMonitor().to(device)
    model.load_state_dict(ckpt["model_state_dict"])

    val_scores, val_targets = score_split(model, val_dataset, device)
    val_episodes = episode_indices[val_row_idx]

    row_metrics = compute_row_metrics(val_targets, val_scores)
    success_maxima = compute_successful_episode_maxima(val_scores, val_targets, val_episodes)
    f1_res = compute_best_f1_threshold(val_targets, val_scores)
    thresholds = compute_calibration_thresholds(success_maxima, val_targets, val_scores)

    episode_evals = {}
    for t_name, t_val in thresholds.items():
        episode_evals[t_name] = compute_episode_evaluation(val_scores, val_targets, val_episodes, t_val)

    val_package = {
        "experiment_name": STRICT_V2_EXP_NAME,
        "seed": seed,
        "selected_epoch": ckpt["epoch"],
        "model_checkpoint_path": str(ckpt_path),
        "model_checkpoint_sha256": sha256_file(ckpt_path),
        "dataset_manifest_sha256": sha256_file(v2_derived_dir / "dataset_manifest.json"),
        "normalization_sha256": sha256_file(v2_derived_dir / "normalization.json"),
        "validation_rows_count": len(val_row_idx),
        "validation_episodes_count": 600,
        "validation_failure_episodes_count": 14,
        "row_metrics": row_metrics,
        "row_best_f1_summary": f1_res,
        "calibrated_thresholds": thresholds,
        "episode_evaluations": episode_evals,
    }

    freeze_p = val_out_dir / "FROZEN_VALIDATION_SELECTION.json"
    with open(freeze_p, "w") as f:
        json.dump(val_package, f, indent=2)
    freeze_sha = sha256_file(freeze_p)
    with open(snapshot_dir / f"FROZEN_VALIDATION_SELECTION_seed_{seed}.json", "w") as f:
        json.dump(val_package, f, indent=2)

    print(f"Validation Freeze Seed {seed} saved! SHA256: {freeze_sha}")
    return val_package


def run_stage6(
    workspace_dir_path: str,
    snapshot_dir_path: str,
    device: torch.device,
) -> Dict[str, Any]:
    w_dir = Path(workspace_dir_path)
    snapshot_dir = Path(snapshot_dir_path)
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    v1_derived_dir = w_dir / "derived_datasets/isaac_mimic_h10_c0dyn_v1"
    v2_derived_dir = w_dir / "derived_datasets/isaac_mimic_h10_strict_missingdyn_v2"
    model_root = w_dir / "models/isaac_mimic_h10_strict_missingdyn_v2"
    val_root = w_dir / "evaluations/isaac_mimic_h10_strict_missingdyn_v2/validation"

    # Step 1: Build dataset & audit parity
    parity_audit, manifest = build_strict_v2_dataset(v1_derived_dir, v2_derived_dir, snapshot_dir)

    # Step 2: Train seeds 0..4 sequentially with validation calibration
    training_summaries = {}
    validation_freezes = {}

    for s in SEEDS:
        s_model_dir = model_root / f"seed_{s}"
        s_val_dir = val_root / f"seed_{s}"

        t_summary = train_strict_v2_seed(s, v2_derived_dir, s_model_dir, device)
        training_summaries[s] = t_summary

        v_freeze = calibrate_and_freeze_validation(s, v2_derived_dir, s_model_dir, s_val_dir, snapshot_dir, device)
        validation_freezes[s] = v_freeze

    # Save overall training freeze
    training_freeze_data = {
        "experiment_name": STRICT_V2_EXP_NAME,
        "dataset_manifest_sha256": sha256_file(v2_derived_dir / "dataset_manifest.json"),
        "normalization_sha256": sha256_file(v2_derived_dir / "normalization.json"),
        "primary_seed": 0,
        "primary_operating_point": "conformal_alpha_0.10",
        "held_out_test_observed_by_v2_training": False,
        "ood_observed_by_v2_training": False,
        "seeds": {
            str(s): {
                "checkpoint_path": training_summaries[s]["best_model_checkpoint_path"],
                "checkpoint_sha256": training_summaries[s]["best_model_checkpoint_sha256"],
                "best_epoch": training_summaries[s]["best_epoch"],
                "best_val_auprc": training_summaries[s]["best_val_auprc"],
                "validation_freeze_path": str(val_root / f"seed_{s}" / "FROZEN_VALIDATION_SELECTION.json"),
                "validation_freeze_sha256": sha256_file(val_root / f"seed_{s}" / "FROZEN_VALIDATION_SELECTION.json"),
            }
            for s in SEEDS
        }
    }
    tf_p = model_root / "TRAINING_FREEZE.json"
    with open(tf_p, "w") as f:
        json.dump(training_freeze_data, f, indent=2)
    tf_sha = sha256_file(tf_p)
    with open(snapshot_dir / "TRAINING_FREEZE.json", "w") as f:
        json.dump(training_freeze_data, f, indent=2)

    # Save all-seed validation freeze
    vf_all_data = {
        "experiment_name": STRICT_V2_EXP_NAME,
        "primary_seed": 0,
        "primary_operating_point": "conformal_alpha_0.10",
        "training_freeze_sha256": tf_sha,
        "validation_freezes": {str(s): validation_freezes[s] for s in SEEDS},
    }
    vf_all_p = val_root / "VALIDATION_FREEZE_ALL_SEEDS.json"
    with open(vf_all_p, "w") as f:
        json.dump(vf_all_data, f, indent=2)
    vf_all_sha = sha256_file(vf_all_p)
    with open(snapshot_dir / "VALIDATION_FREEZE_ALL_SEEDS.json", "w") as f:
        json.dump(vf_all_data, f, indent=2)

    # Markdown summary
    s0_vf = validation_freezes[0]
    s_lines = [
        "# Stage 6 Summary — Strict Mimic Fidelity Baseline V2",
        "",
        "## 1. Dataset & Parity Audit",
        f"- Dataset Root: `{v2_derived_dir}`",
        f"- Total Rows: {parity_audit['total_rows']}",
        f"- Parity Status: PASSED (scalar 0..8 max diff {parity_audit['scalar_0_to_8_max_diff']:.3e}, horizon max diff {parity_audit['horizon_max_diff']:.3e}, disabled dims 9..33 zero)",
        f"- Normalization SHA256: `{sha256_file(v2_derived_dir / 'normalization.json')}`",
        f"- Dataset Manifest SHA256: `{sha256_file(v2_derived_dir / 'dataset_manifest.json')}`",
        "",
        "## 2. Multi-Seed Training Results",
        "| Seed | Best Epoch | Val AUROC | Val AUPRC | Checkpoint SHA256 | Alpha 0.10 Threshold |",
        "|---|---|---|---|---|---|",
    ]
    for s in SEEDS:
        vf = validation_freezes[s]
        s_lines.append(
            f"| Seed {s} | Ep {vf['selected_epoch']:02d} | {vf['row_metrics']['auroc']:.4f} | {vf['row_metrics']['auprc']:.4f} | `{vf['model_checkpoint_sha256'][:16]}...` | {vf['calibrated_thresholds']['conformal_alpha_0.10']:.6f} |"
        )
    s_lines.extend([
        "",
        f"- Primary Seed 0 Validation AUROC: {s0_vf['row_metrics']['auroc']:.6f}",
        f"- Primary Seed 0 Validation AUPRC: {s0_vf['row_metrics']['auprc']:.6f}",
        f"- Primary Seed 0 Alpha 0.10 Threshold: {s0_vf['calibrated_thresholds']['conformal_alpha_0.10']:.6f}",
        "",
        "## 3. Pre-Scoring Safety Locks",
        "- Held-out seen test scored: NO",
        "- OOD scored: NO",
        "- Isaac Sim launched: NO",
        "- HARD1000 touched: NO",
    ])
    with open(snapshot_dir / "STAGE6_SUMMARY.md", "w") as f:
        f.write("\n".join(s_lines) + "\n")

    print(f"STAGE 6 COMPLETE! Training Freeze SHA256: {tf_sha}")
    return training_freeze_data


def main():
    parser = argparse.ArgumentParser(description="Stage 6 Strict Mimic V2 Build, Train, and Validate")
    parser.add_argument("--workspace", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
    parser.add_argument("--snapshot_dir", type=str, default="/home/redafrix/tests/internship/prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/strict_v2_snapshot")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    run_stage6(args.workspace, args.snapshot_dir, torch.device(args.device))


if __name__ == "__main__":
    main()
