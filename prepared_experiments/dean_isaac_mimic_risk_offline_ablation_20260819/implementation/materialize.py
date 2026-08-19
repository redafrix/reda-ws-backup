"""Materialize the 75,603-row Isaac Mimic H10 dataset on Dean."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from typing import Any, Dict, List, Tuple

import numpy as np

from .action_adapter import isaac_7d_to_mimic_10d
from .c0_dynamics import compute_c0_dynamics_25, reconstruct_c0_trajectory
from .candidate_features import (
    assemble_scalar37,
    compute_disagreement_and_horizon_features,
    compute_temporal_scalars,
)
from .constants import (
    C0_PROXY_TRACE_NAMES,
    DISAGREEMENT_SCALAR_NAMES,
    EXPERIMENT_NAME,
    HORIZON_CHANNEL_NAMES,
    PRIMARY_CANDIDATES,
    RECONSTRUCTION_PARITY_TOLERANCE,
    SUMMARY_STAT_NAMES,
    TEMPORAL_SCALAR_NAMES,
    TOTAL_ROWS,
)
from .dataset import fit_normalization


def sha256_file(path: Path | str) -> str:
    p = Path(path)
    if not p.exists() or not p.is_file():
        return "N/A"
    hasher = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024 * 4), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def materialize_dataset(
    workspace_root: Path | str,
    output_derived_dir: Path | str,
) -> Dict[str, Any]:
    w_root = Path(workspace_root)
    out_dir = Path(output_derived_dir)
    raw_dir = out_dir / "raw"
    audit_dir = out_dir / "audit"
    raw_dir.mkdir(parents=True, exist_ok=True)
    audit_dir.mkdir(parents=True, exist_ok=True)

    outputs_dir = w_root / "outputs/final_seen_h10_round_000_seed20260730"
    episodes_dir = outputs_dir / "episodes"
    frozen_dir = w_root / "frozen_datasets/isaac_seen_h10_topk8_v1"

    # Load frozen split assignments
    with open(frozen_dir / "split_assignments.json") as f:
        splits_map = json.load(f)

    split_to_int = {"train": 0, "validation": 1, "test": 2}

    ep_list = sorted(os.listdir(episodes_dir))
    print(f"Starting materialization for {len(ep_list)} episodes...")

    all_scalars37 = []
    all_horizons10x6 = []
    all_labels = []
    all_episode_indices = []
    all_decision_indices = []
    all_split_indices = []
    unique_episode_ids = []

    parity_errors = []
    worst_parity_err = 0.0
    total_rows = 0

    t0 = time.time()

    for ep_idx, ep_id in enumerate(ep_list):
        if ep_idx % 500 == 0:
            print(f"  Processed {ep_idx}/{len(ep_list)} episodes ({total_rows} rows)...")

        zst_path = episodes_dir / ep_id / "risk_rows.jsonl.zst"
        if not zst_path.exists():
            continue

        unique_episode_ids.append(ep_id)
        ep_split_str = splits_map.get(ep_id, {}).get("split", "train")
        ep_split_int = split_to_int[ep_split_str]
        ep_label = splits_map.get(ep_id, {}).get("label", 0)

        prev_var_mean = None
        prev_spread_mean = None

        proc = subprocess.Popen(["zstd", "-dc", str(zst_path)], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        for line in proc.stdout:
            if not line.strip():
                continue
            row = json.loads(line)
            total_rows += 1

            dec_idx = int(row.get("decision_index", 0))

            # 1. Candidate selection: main + alternatives 1..7 (env action)
            main_env = np.asarray(row["main_candidate_action_chunk_env"], dtype=np.float32)[None, :, :]  # [1, 10, 7]
            ace_env = np.asarray(row["ace_candidate_chunks_env"], dtype=np.float32)[:7, :, :]            # [7, 10, 7]
            c8_env = np.concatenate([main_env, ace_env], axis=0)                                        # [8, 10, 7]

            # 2. Convert to 10D monitor representation
            c8_10d = isaac_7d_to_mimic_10d(c8_env)  # [8, 10, 10]

            # 3. Disagreement 9 scalars + Horizon 10x6
            disagree_9, horizon_10x6 = compute_disagreement_and_horizon_features(c8_10d)
            curr_var_mean = float(disagree_9[0])
            curr_spread_mean = float(disagree_9[4])

            # 4. Candidate0 Denoising Dynamics (25 scalars)
            raw_unc = row["simvla_uncertainty_raw"]
            init_n = np.asarray(raw_unc["initial_noise"], dtype=np.float32)
            upd_trace = np.asarray(raw_unc["update_vector_trace"], dtype=np.float32)
            final_norm = np.asarray(raw_unc["final_action_normalized"], dtype=np.float32)

            X, V, p_err = reconstruct_c0_trajectory(
                init_n, upd_trace, final_norm, tolerance=RECONSTRUCTION_PARITY_TOLERANCE
            )
            parity_errors.append(p_err)
            if p_err > worst_parity_err:
                worst_parity_err = p_err

            c0_dyn_25 = compute_c0_dynamics_25(X, V)

            # 5. Temporal changes (3 scalars)
            temp_3 = compute_temporal_scalars(
                dec_idx, curr_var_mean, curr_spread_mean, prev_var_mean, prev_spread_mean
            )
            prev_var_mean = curr_var_mean
            prev_spread_mean = curr_spread_mean

            # 6. Assemble 37 scalars
            scalar_37 = assemble_scalar37(disagree_9, c0_dyn_25, temp_3)

            # Finite check
            if not np.all(np.isfinite(scalar_37)) or not np.all(np.isfinite(horizon_10x6)):
                raise ValueError(f"Non-finite features in ep {ep_id} decision {dec_idx}")

            all_scalars37.append(scalar_37)
            all_horizons10x6.append(horizon_10x6)
            all_labels.append(ep_label)
            all_episode_indices.append(ep_idx)
            all_decision_indices.append(dec_idx)
            all_split_indices.append(ep_split_int)

        proc.wait()

    t1 = time.time()
    print(f"Materialized {total_rows} rows in {t1 - t0:.2f}s! Worst parity error: {worst_parity_err:.9e}")

    # Convert to arrays and save
    print("Saving numpy arrays...")
    scalars_arr = np.stack(all_scalars37).astype(np.float32)
    horizon_arr = np.stack(all_horizons10x6).astype(np.float32)
    labels_arr = np.asarray(all_labels, dtype=np.float32)
    ep_idx_arr = np.asarray(all_episode_indices, dtype=np.int64)
    dec_idx_arr = np.asarray(all_decision_indices, dtype=np.int64)
    split_idx_arr = np.asarray(all_split_indices, dtype=np.int64)

    np.save(raw_dir / "scalar37.npy", scalars_arr)
    np.save(raw_dir / "horizon10x6.npy", horizon_arr)
    np.save(out_dir / "labels.npy", labels_arr)
    np.save(out_dir / "episode_index.npy", ep_idx_arr)
    np.save(out_dir / "decision_index.npy", dec_idx_arr)
    np.save(out_dir / "split_index.npy", split_idx_arr)

    with open(out_dir / "episode_ids.json", "w") as f:
        json.dump(unique_episode_ids, f, indent=2)

    # Fit and save normalization on TRAIN rows only
    print("Fitting train normalization...")
    train_mask = (split_idx_arr == 0)
    val_mask = (split_idx_arr == 1)
    test_mask = (split_idx_arr == 2)

    norm_params = fit_normalization(scalars_arr[train_mask], horizon_arr[train_mask])
    norm_path = out_dir / "normalization.json"
    with open(norm_path, "w") as f:
        json.dump(norm_params, f, indent=2)
    norm_sha = sha256_file(norm_path)

    # Audit summaries
    parity_audit = {
        "total_rows_checked": total_rows,
        "tolerance": RECONSTRUCTION_PARITY_TOLERANCE,
        "max_parity_error": float(worst_parity_err),
        "mean_parity_error": float(np.mean(parity_errors)),
        "all_passed": bool(worst_parity_err <= RECONSTRUCTION_PARITY_TOLERANCE),
    }
    with open(audit_dir / "c0_reconstruction_parity.json", "w") as f:
        json.dump(parity_audit, f, indent=2)

    train_rows = int(np.sum(train_mask))
    val_rows = int(np.sum(val_mask))
    test_rows = int(np.sum(test_mask))

    n_train_pos = int(np.sum(labels_arr[train_mask] == 1))
    n_train_neg = int(np.sum(labels_arr[train_mask] == 0))
    pos_weight = float(n_train_neg / max(1, n_train_pos))

    manifest = {
        "experiment_name": EXPERIMENT_NAME,
        "source_root": str(outputs_dir),
        "source_frozen_root": str(frozen_dir),
        "total_rows": total_rows,
        "train_rows": train_rows,
        "val_rows": val_rows,
        "test_rows": test_rows,
        "train_positive_rows": n_train_pos,
        "train_negative_rows": n_train_neg,
        "pos_weight": pos_weight,
        "candidate_subset": "main_candidate + alternatives_1_through_7 (first 8 stored)",
        "action_conversion": "isaac_7d_to_mimic_10d (robot base axis-angle -> continuous 6D rotation matrix)",
        "features": {
            "disagreement_scalar_names": list(DISAGREEMENT_SCALAR_NAMES),
            "c0_proxy_trace_names": list(C0_PROXY_TRACE_NAMES),
            "summary_stat_names": list(SUMMARY_STAT_NAMES),
            "temporal_scalar_names": list(TEMPORAL_SCALAR_NAMES),
            "horizon_channel_names": list(HORIZON_CHANNEL_NAMES),
        },
        "normalization_sha256": norm_sha,
        "c0_reconstruction_parity": parity_audit,
    }

    manifest_path = out_dir / "dataset_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    manifest_sha = sha256_file(manifest_path)

    print(f"Materialization Complete! Manifest SHA256: {manifest_sha}")
    return {
        "root": str(out_dir),
        "rows": total_rows,
        "train_rows": train_rows,
        "val_rows": val_rows,
        "test_rows": test_rows,
        "train_positive_rows": n_train_pos,
        "train_negative_rows": n_train_neg,
        "pos_weight": pos_weight,
        "all_finite": True,
        "recurrence_parity_passed": parity_audit["all_passed"],
        "recurrence_worst_max_abs": float(worst_parity_err),
        "normalization_sha256": norm_sha,
        "dataset_manifest_sha256": manifest_sha,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize Isaac Mimic H10 dataset")
    parser.add_argument(
        "--workspace",
        type=str,
        default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813",
        help="Workspace root",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_c0dyn_v1",
        help="Output derived dataset directory",
    )
    args = parser.parse_args()
    materialize_dataset(args.workspace, args.output)


if __name__ == "__main__":
    main()
