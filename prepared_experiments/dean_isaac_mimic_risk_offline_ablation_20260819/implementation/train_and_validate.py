"""Sequential multi-seed training and validation calibration runner with GPU headroom monitoring."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from typing import Any, Dict, List

import numpy as np
import torch

from .constants import (
    EXPERIMENT_NAME,
    SEEDS,
    TOTAL_ROWS,
    VAL_ROWS,
    VAL_EPISODES,
)
from .evaluate import run_validation_and_calibrate, sha256_file
from .train import train_single_seed


def get_gpu_status() -> Dict[str, Any]:
    try:
        out = subprocess.check_output([
            "nvidia-smi",
            "--query-gpu=memory.total,memory.used,memory.free,utilization.gpu",
            "--format=csv,noheader,nounits"
        ]).decode().strip()
        parts = [float(p.strip()) for p in out.split(",")]
        apps = subprocess.check_output([
            "nvidia-smi",
            "--query-compute-apps=pid,used_memory",
            "--format=csv,noheader,nounits"
        ]).decode().strip()
        app_dict = {}
        for l in apps.splitlines():
            if l.strip():
                p, m = l.split(",")
                app_dict[p.strip()] = float(m.strip())
        return {
            "total_mib": parts[0],
            "used_mib": parts[1],
            "free_mib": parts[2],
            "gpu_util_pct": parts[3],
            "apps": app_dict
        }
    except Exception as e:
        return {"error": str(e)}


def run_all(
    derived_dir_path: str,
    model_root_path: str,
    val_root_path: str,
    spec_path: str,
    snapshot_dir_path: str,
    device: torch.device,
) -> Dict[str, Any]:
    derived_dir = Path(derived_dir_path)
    model_root = Path(model_root_path)
    val_root = Path(val_root_path)
    s_path = Path(spec_path)
    snapshot_dir = Path(snapshot_dir_path)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    model_root.mkdir(parents=True, exist_ok=True)
    val_root.mkdir(parents=True, exist_ok=True)

    manifest_v2_p = derived_dir / "dataset_manifest_v2.json"
    manifest_v2_sha = sha256_file(manifest_v2_p)
    norm_p = derived_dir / "normalization.json"
    norm_sha = sha256_file(norm_p)
    spec_sha = sha256_file(s_path)

    training_results: Dict[int, Dict[str, Any]] = {}
    validation_results: Dict[int, Dict[str, Any]] = {}

    min_free_seen = 999999.0
    foreign_signaled = False

    t_all_start = time.time()

    for s in SEEDS:
        print(f"===================================================")
        print(f"Starting Seed {s} ({s+1}/{len(SEEDS)})...")
        print(f"===================================================")

        gpu_stat = get_gpu_status()
        if "free_mib" in gpu_stat:
            free_m = gpu_stat["free_mib"]
            used_m = gpu_stat["used_mib"]
            if free_m < min_free_seen:
                min_free_seen = free_m
            print(f"Pre-seed {s} GPU status: free={free_m:.1f} MiB, used={used_m:.1f} MiB")

        # Train seed
        t_seed_start = time.time()
        t_summary = train_single_seed(derived_dir, model_root, s, device)
        t_seed_end = time.time()
        print(f"Seed {s} Training finished in {t_seed_end - t_seed_start:.1f}s!")

        seed_model_dir = model_root / f"seed_{s}"
        best_model_p = seed_model_dir / "best_model.pt"
        summary_p = seed_model_dir / "training_summary.json"

        # Verify all 25 checkpoints
        for ep in range(1, 26):
            ckpt_ep_p = seed_model_dir / f"checkpoint_epoch_{ep:02d}.pt"
            if not ckpt_ep_p.exists():
                raise RuntimeError(f"Missing epoch checkpoint: {ckpt_ep_p}")

        if not best_model_p.exists():
            raise RuntimeError(f"Missing best model checkpoint: {best_model_p}")

        best_model_sha = sha256_file(best_model_p)
        summary_sha = sha256_file(summary_p)

        training_results[s] = {
            "seed": s,
            "best_epoch": t_summary["best_epoch"],
            "best_val_auprc": t_summary["best_val_auprc"],
            "best_model_path": str(best_model_p),
            "best_model_sha256": best_model_sha,
            "training_summary_path": str(summary_p),
            "training_summary_sha256": summary_sha,
            "epochs_completed": len(t_summary["epoch_logs"]),
        }

        # Run validation calibration
        seed_val_dir = val_root / f"seed_{s}"
        print(f"Running validation calibration for Seed {s}...")
        val_summary = run_validation_and_calibrate(
            derived_dataset_dir=derived_dir,
            model_checkpoint_path=best_model_p,
            training_summary_path=summary_p,
            spec_path=s_path,
            output_dir=seed_val_dir,
            device=device,
        )
        val_freeze_p = seed_val_dir / "FROZEN_VALIDATION_SELECTION.json"
        val_freeze_sha = sha256_file(val_freeze_p)

        validation_results[s] = {
            "seed": s,
            "freeze_path": str(val_freeze_p),
            "freeze_sha256": val_freeze_sha,
            "val_auroc": val_summary["row_metrics"]["auroc"],
            "val_auprc": val_summary["row_metrics"]["auprc"],
            "alpha010_threshold": val_summary["calibrated_thresholds"]["conformal_alpha_0.10"],
            "calibrated_thresholds": val_summary["calibrated_thresholds"],
            "episode_evaluations": val_summary["episode_evaluations"],
        }

        # Copy to snapshot directory
        with open(snapshot_dir / f"training_summary_seed_{s}.json", "w") as f:
            json.dump(t_summary, f, indent=2)
        with open(snapshot_dir / f"FROZEN_VALIDATION_SELECTION_seed_{s}.json", "w") as f:
            json.dump(val_summary, f, indent=2)

    # All seeds complete!
    # Create TRAINING_FREEZE.json
    training_freeze = {
        "experiment_name": EXPERIMENT_NAME,
        "training_code_commit": "1a09d4d350b1457cf4e2e99a6c66ed9a7fc233ac",
        "dataset_manifest_v2_sha256": manifest_v2_sha,
        "normalization_sha256": norm_sha,
        "spec_sha256": spec_sha,
        "seeds_trained": list(SEEDS),
        "primary_seed": 0,
        "primary_seed_rule": "primary_seed=0_predeclared_before_test",
        "all_seeds_25_epochs_complete": True,
        "no_test_scores_observed": True,
        "seed_results": training_results,
    }
    training_freeze_p = model_root / "TRAINING_FREEZE.json"
    with open(training_freeze_p, "w") as f:
        json.dump(training_freeze, f, indent=2)
    training_freeze_sha = sha256_file(training_freeze_p)
    with open(snapshot_dir / "TRAINING_FREEZE.json", "w") as f:
        json.dump(training_freeze, f, indent=2)

    # Create VALIDATION_FREEZE_ALL_SEEDS.json
    val_aurocs = [validation_results[s]["val_auroc"] for s in SEEDS]
    val_auprcs = [validation_results[s]["val_auprc"] for s in SEEDS]

    val_freeze_all = {
        "experiment_name": EXPERIMENT_NAME,
        "primary_seed": 0,
        "primary_operating_point": "conformal_alpha_0.10",
        "held_out_test_scored": False,
        "ood_scored": False,
        "aggregate_validation_metrics": {
            "mean_val_auroc": float(np.mean(val_aurocs)),
            "std_val_auroc": float(np.std(val_aurocs)),
            "mean_val_auprc": float(np.mean(val_auprcs)),
            "std_val_auprc": float(np.std(val_auprcs)),
        },
        "seed_validation_results": validation_results,
    }
    val_freeze_all_p = val_root / "VALIDATION_FREEZE_ALL_SEEDS.json"
    with open(val_freeze_all_p, "w") as f:
        json.dump(val_freeze_all, f, indent=2)
    val_freeze_all_sha = sha256_file(val_freeze_all_p)
    with open(snapshot_dir / "VALIDATION_FREEZE_ALL_SEEDS.json", "w") as f:
        json.dump(val_freeze_all, f, indent=2)

    # Write STAGE3_SUMMARY.md
    summary_lines = [
        "# Stage 3 Summary — Five-Seed Training & Validation Freeze",
        "",
        "## 1. Primary Predeclared Operating Point",
        "- Primary Seed: 0",
        "- Primary Operating Point: `conformal_alpha_0.10`",
        f"- Model Checkpoint: {training_results[0][best_model_path]}",
        f"- Checkpoint SHA256: {training_results[0][best_model_sha256]}",
        f"- Best Epoch: {training_results[0][best_epoch]}",
        f"- Validation Row AUROC: {validation_results[0][val_auroc]:.4f}",
        f"- Validation Row AUPRC: {validation_results[0][val_auprc]:.4f}",
        f"- Conformal alpha=0.10 Threshold: {validation_results[0][alpha010_threshold]:.6f}",
        "",
        "## 2. Robustness Repeats (Seeds 0..4)",
        "| Seed | Best Epoch | Val AUROC | Val AUPRC | Alpha 0.10 Thresh |",
        "|---|---|---|---|---|",
    ]
    for s in SEEDS:
        summary_lines.append(
            f"| Seed {s} | {training_results[s][best_epoch]} | {validation_results[s][val_auroc]:.4f} | {validation_results[s][val_auprc]:.4f} | {validation_results[s][alpha010_threshold]:.4f} |"
        )
    summary_lines.extend([
        "",
        f"- Mean Validation AUROC: {np.mean(val_aurocs):.4f} +/- {np.std(val_aurocs):.4f}",
        f"- Mean Validation AUPRC: {np.mean(val_auprcs):.4f} +/- {np.std(val_auprcs):.4f}",
        "",
        "## 3. Cryptographic Hashes",
        f"- Training Freeze SHA256: {training_freeze_sha}",
        f"- All-Seed Validation Freeze SHA256: {val_freeze_all_sha}",
        f"- Dataset Manifest V2 SHA256: {manifest_v2_sha}",
        f"- Normalization SHA256: {norm_sha}",
    ])

    with open(snapshot_dir / "STAGE3_SUMMARY.md", "w") as f:
        f.write("\n".join(summary_lines) + "\n")

    print("===================================================")
    print("ALL FIVE SEEDS SUCCESSFULLY TRAINED AND VALIDATED!")
    print("===================================================")
    return {
        "training_freeze_sha256": training_freeze_sha,
        "val_freeze_all_sha256": val_freeze_all_sha,
        "training_results": training_results,
        "validation_results": validation_results,
        "min_free_seen": min_free_seen,
        "foreign_signaled": foreign_signaled,
    }


def main():
    parser = argparse.ArgumentParser(description="Train and validate all 5 seeds")
    parser.add_argument("--derived_dir", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_c0dyn_v1")
    parser.add_argument("--model_root", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_mimic_h10_c0dyn_v1")
    parser.add_argument("--val_root", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/evaluations/isaac_mimic_h10_c0dyn_v1/validation")
    parser.add_argument("--spec", type=str, default="/home/redafrix/tests/internship/prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/FINAL_ADAPTATION_SPEC_V1.md")
    parser.add_argument("--snapshot_dir", type=str, default="/home/redafrix/tests/internship/prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/training_snapshot")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    run_all(args.derived_dir, args.model_root, args.val_root, args.spec, args.snapshot_dir, torch.device(args.device))


if __name__ == "__main__":
    main()
