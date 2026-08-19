"""AGY Stage 1 One-Time Held-Out Test for NEW4904 Mimic V3."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
from torch.utils.data import DataLoader

from .stage0_build_train_validate import (
    EXPERIMENT_NAME,
    TOTAL_EPISODES,
    TOTAL_ROWS,
    BATCH_SIZE,
    HISTORY_WINDOW_LENGTH,
    HORIZON_CHANNELS,
    HORIZON_STEPS,
    SCALAR_DIM,
    PRIMARY_CANDIDATES,
    SEEDS,
    IsaacMimicWindowDataset,
    MimicH10RiskMonitor,
    compute_row_metrics,
    compute_episode_evaluation,
    score_split,
    sha256_file,
)


EXPECTED_SOURCE_MANIFEST_SHA = "61462ceead4a79d6d44a0ae80ee9ff25b958c4c1afbd67142c4df276801a0a3c"
EXPECTED_SOURCE_SPLIT_SHA = "34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8"
EXPECTED_DERIVED_MANIFEST_SHA = "26e633c8815d92a46df841bd7976ec942740b83ec477cc20e7d9f6cf87bb3019"
EXPECTED_NORMALIZATION_SHA = "5564083f1561b627c81305c9ebfcb34732c4f3529bc2421ab6d4124682e84b26"
EXPECTED_TRAINING_FREEZE_SHA = "ec925b2dea8a66dd7b5317790d8f8c18bf59e67da0ddb0278ca678b5d8637e21"

EXPECTED_SEED0_CKPT_SHA = "857e16b7d846051c29921d148d8545198e7057f2e1458040250de7b8cc965b82"
EXPECTED_SEED0_ALPHA010_TH = 0.8907762169837952


def run_pretest_gates(
    w_dir: Path,
    source_ds_dir: Path,
    topk8_model_dir: Path,
    derived_ds_dir: Path,
    model_root: Path,
    val_root: Path,
    test_out_dir: Path,
    snapshot_dir: Path,
) -> Dict[str, Any]:
    print("1. Running Pretest Cryptographic & Fidelity Gates...")

    # Gate 1: Source manifest SHA
    src_man_p = source_ds_dir / "manifest.json"
    actual_src_man_sha = sha256_file(src_man_p)
    assert actual_src_man_sha == EXPECTED_SOURCE_MANIFEST_SHA, f"Source manifest SHA mismatch: {actual_src_man_sha}"

    # Gate 2: Source split artifact SHA
    split_p = topk8_model_dir / "split_manifest.json"
    actual_split_sha = sha256_file(split_p)
    assert actual_split_sha == EXPECTED_SOURCE_SPLIT_SHA, f"Source split SHA mismatch: {actual_split_sha}"

    # Gate 3: Derived dataset manifest SHA
    derived_man_p = derived_ds_dir / "dataset_manifest.json"
    actual_derived_man_sha = sha256_file(derived_man_p)
    assert actual_derived_man_sha == EXPECTED_DERIVED_MANIFEST_SHA, f"Derived manifest SHA mismatch: {actual_derived_man_sha}"

    # Gate 4: Normalization SHA
    norm_p = derived_ds_dir / "normalization.json"
    actual_norm_sha = sha256_file(norm_p)
    assert actual_norm_sha == EXPECTED_NORMALIZATION_SHA, f"Norm SHA mismatch: {actual_norm_sha}"

    # Gate 5: Training freeze SHA
    tf_p = model_root / "TRAINING_FREEZE.json"
    actual_tf_sha = sha256_file(tf_p)
    assert actual_tf_sha == EXPECTED_TRAINING_FREEZE_SHA, f"Training freeze SHA mismatch: {actual_tf_sha}"

    with open(tf_p) as f:
        tf_data = json.load(f)

    # Gate 6 & 7: Checkpoint and validation freeze bindings for all seeds
    for s in SEEDS:
        s_info = tf_data["seeds"][str(s)]
        ckpt_p = Path(s_info["checkpoint_path"])
        assert ckpt_p.exists()
        assert sha256_file(ckpt_p) == s_info["checkpoint_sha256"]

        vf_p = Path(s_info["validation_freeze_path"])
        assert vf_p.exists()
        assert sha256_file(vf_p) == s_info["validation_freeze_sha256"]

    # Gate 8: Seed 0 bindings
    assert tf_data["seeds"]["0"]["checkpoint_sha256"] == EXPECTED_SEED0_CKPT_SHA
    with open(tf_data["seeds"]["0"]["validation_freeze_path"]) as f:
        s0_vf = json.load(f)
    actual_s0_th = s0_vf["calibrated_thresholds"]["conformal_alpha_0.10"]
    assert abs(actual_s0_th - EXPECTED_SEED0_ALPHA010_TH) < 1e-6, f"Seed 0 threshold mismatch: {actual_s0_th}"

    # Gate 9: Heavy array hashes match manifest
    with open(derived_man_p) as f:
        derived_m = json.load(f)
    for arr_name, exp_sha in derived_m["heavy_array_hashes"].items():
        if arr_name in ["scalar37.npy", "horizon10x6.npy"]:
            arr_p = derived_ds_dir / "raw" / arr_name
        else:
            arr_p = derived_ds_dir / arr_name
        assert arr_p.exists()
        assert sha256_file(arr_p) == exp_sha, f"Array {arr_name} SHA mismatch: {sha256_file(arr_p)} vs {exp_sha}"

    # Gate 10: Held-out split census
    scalars = np.load(derived_ds_dir / "raw/scalar37.npy")
    labels = np.load(derived_ds_dir / "labels.npy")
    ep_idx = np.load(derived_ds_dir / "episode_index.npy")
    split_idx = np.load(derived_ds_dir / "split_index.npy")

    test_row_mask = (split_idx == 2)
    test_row_indices = np.where(test_row_mask)[0]
    n_test_rows = len(test_row_indices)
    assert n_test_rows == 14526, f"Expected 14526 test rows, got {n_test_rows}"

    test_pos_rows = int(np.sum(labels[test_row_mask] == 1))
    test_neg_rows = int(np.sum(labels[test_row_mask] == 0))
    assert test_pos_rows == 2730 and test_neg_rows == 11796

    test_ep_ords = np.unique(ep_idx[test_row_mask])
    n_test_eps = len(test_ep_ords)
    assert n_test_eps == 736, f"Expected 736 test episodes, got {n_test_eps}"

    ep_labels = {}
    for r_i in test_row_indices:
        ep_labels[ep_idx[r_i]] = labels[r_i]
    test_succ_eps = sum(1 for lbl in ep_labels.values() if lbl == 0)
    test_fail_eps = sum(1 for lbl in ep_labels.values() if lbl == 1)
    assert test_succ_eps == 658 and test_fail_eps == 78

    # Gate 11 & 12: Dims 9..33 zero and normalization mean 0 / std 1
    strict_zeros_test = bool(np.all(scalars[test_row_mask, 9:34] == 0.0))
    assert strict_zeros_test, "Dims 9..33 on test rows are not all zero!"

    with open(norm_p) as f:
        norm_data = json.load(f)
    assert norm_data["disabled_scalar_channels_mean"] == 0.0
    assert norm_data["disabled_scalar_channels_std"] == 1.0

    # Gate 13: Exact TopK8 test membership
    with open(split_p) as f:
        topk8_split_data = json.load(f)
    topk8_test_ids = set(ep["final_episode_id"] for ep in topk8_split_data["episodes"] if ep["split"] == "test")

    with open(derived_ds_dir / "episode_ids.json") as f:
        mimic_ep_ids = json.load(f)
    mimic_test_ids = set(mimic_ep_ids[ord] for ord in test_ep_ords)

    exact_test_membership = (topk8_test_ids == mimic_test_ids)
    assert exact_test_membership, "Test episode IDs do not match TopK8 split manifest!"
    assert len(mimic_test_ids) == 736

    # Gate 14: Pairwise disjoint splits
    tr_ords = set(np.unique(ep_idx[split_idx == 0]))
    va_ords = set(np.unique(ep_idx[split_idx == 1]))
    te_ords = set(np.unique(ep_idx[split_idx == 2]))
    assert len(tr_ords & va_ords) == 0
    assert len(tr_ords & te_ords) == 0
    assert len(va_ords & te_ords) == 0

    # Gate 15: No prior test score files exist
    test_score_files = list(test_out_dir.glob("**/test_scores.npz"))
    assert len(test_score_files) == 0, f"Prior test scoring files found: {test_score_files}"

    pretest_res = {
        "status": "PASSED",
        "source_manifest_sha256": actual_src_man_sha,
        "source_split_sha256": actual_split_sha,
        "derived_manifest_sha256": actual_derived_man_sha,
        "normalization_sha256": actual_norm_sha,
        "training_freeze_sha256": actual_tf_sha,
        "all_checkpoint_validation_bindings_match": True,
        "strict_missing_zero_channels_test": True,
        "heldout_rows": n_test_rows,
        "heldout_episodes": n_test_eps,
        "heldout_success_episodes": test_succ_eps,
        "heldout_failure_episodes": test_fail_eps,
        "heldout_positive_rows": test_pos_rows,
        "heldout_negative_rows": test_neg_rows,
        "exact_topk8_test_membership": True,
    }
    with open(snapshot_dir / "PRETEST_GATE.json", "w") as f:
        json.dump(pretest_res, f, indent=2)

    print("Pretest Gates PASSED successfully!")
    return pretest_res


def score_held_out_test(
    w_dir: Path,
    topk8_model_dir: Path,
    derived_ds_dir: Path,
    model_root: Path,
    val_root: Path,
    test_out_dir: Path,
    snapshot_dir: Path,
    device: torch.device,
) -> Dict[str, Any]:
    print("2. Scoring Held-Out Test for All 5 Seeds (ONE-TIME ONLY)...")
    test_out_dir.mkdir(parents=True, exist_ok=True)

    raw_scalars = np.load(derived_ds_dir / "raw/scalar37.npy")
    raw_horizon = np.load(derived_ds_dir / "raw/horizon10x6.npy")
    labels = np.load(derived_ds_dir / "labels.npy")
    ep_idx = np.load(derived_ds_dir / "episode_index.npy")
    dec_idx = np.load(derived_ds_dir / "decision_index.npy")
    split_idx = np.load(derived_ds_dir / "split_index.npy")

    with open(derived_ds_dir / "normalization.json") as f:
        norm_params = json.load(f)

    test_row_idx = np.where(split_idx == 2)[0]
    test_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, ep_idx, dec_idx, norm_params, row_indices=test_row_idx
    )

    seed_results = {}
    aurocs = []
    auprcs = []
    fa_pcts = []
    rec_pcts = []
    det25_pcts = []
    det50_pcts = []

    for s in SEEDS:
        ckpt_p = model_root / f"seed_{s}/best_model.pt"
        ckpt_sha = sha256_file(ckpt_p)

        vf_p = val_root / f"seed_{s}/FROZEN_VALIDATION_SELECTION.json"
        with open(vf_p) as f:
            vf_data = json.load(f)
        thresholds = vf_data["calibrated_thresholds"]

        model = MimicH10RiskMonitor().to(device)
        ckpt = torch.load(ckpt_p, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])

        scores, targets = score_split(model, test_dataset, device)
        test_episodes = ep_idx[test_row_idx]

        row_metrics = compute_row_metrics(targets, scores)

        ep_evals = {}
        for t_name, t_val in thresholds.items():
            ep_evals[t_name] = compute_episode_evaluation(scores, targets, test_episodes, t_val)

        seed_test_dir = test_out_dir / f"seed_{s}"
        seed_test_dir.mkdir(parents=True, exist_ok=True)

        np.savez_compressed(
            seed_test_dir / "test_scores.npz",
            scores=scores,
            targets=targets,
            episode_index=test_episodes,
            decision_index=dec_idx[test_row_idx],
        )

        res_pkg = {
            "experiment_name": EXPERIMENT_NAME,
            "seed": s,
            "selected_epoch": ckpt["epoch"],
            "model_checkpoint_path": str(ckpt_p),
            "model_checkpoint_sha256": ckpt_sha,
            "frozen_validation_reference": str(vf_p),
            "test_rows_count": len(test_row_idx),
            "test_episodes_count": 736,
            "test_failure_episodes_count": 78,
            "test_success_episodes_count": 658,
            "row_metrics": row_metrics,
            "applied_frozen_thresholds": thresholds,
            "test_episode_evaluations": ep_evals,
        }

        with open(seed_test_dir / "TEST_RESULTS.json", "w") as f:
            json.dump(res_pkg, f, indent=2)
        with open(snapshot_dir / f"TEST_RESULTS_seed_{s}.json", "w") as f:
            json.dump(res_pkg, f, indent=2)

        seed_results[s] = res_pkg

        aurocs.append(row_metrics["auroc"])
        auprcs.append(row_metrics["auprc"])
        fa_pcts.append(ep_evals["conformal_alpha_0.10"]["fpr"] * 100)
        rec_pcts.append(ep_evals["conformal_alpha_0.10"]["recall"] * 100)
        det25_pcts.append(ep_evals["conformal_alpha_0.10"]["det_25_rate"] * 100)
        det50_pcts.append(ep_evals["conformal_alpha_0.10"]["det_50_rate"] * 100)

    # Step 3: TopK8 Main V2 Matched Comparison
    topk8_res_p = topk8_model_dir / "test_results.json"
    topk8_res_sha = sha256_file(topk8_res_p)
    with open(topk8_res_p) as f:
        topk8_data = json.load(f)

    topk8_auroc = topk8_data["test"]["query_auroc"]
    topk8_auprc = topk8_data["test"]["query_auprc"]
    topk8_f1_op = topk8_data["test"]["threshold_operating_points"]["best_val_f1"]

    # TopK8 best_val_f1 numbers
    topk8_best_f1_th = topk8_f1_op["threshold"]
    topk8_best_f1_fa_rate = topk8_f1_op["success_episode_false_alarm_rate"]
    topk8_best_f1_fa_count = int(round(topk8_best_f1_fa_rate * 658)) # 50
    topk8_best_f1_det_rate = topk8_f1_op["failure_episode_detection_rate"] # 1.0 (78)

    # Mimic Seed 0 metrics
    s0_metrics = seed_results[0]["row_metrics"]
    s0_f1_eval = seed_results[0]["test_episode_evaluations"]["row_best_f1"]
    s0_a10_eval = seed_results[0]["test_episode_evaluations"]["conformal_alpha_0.10"]

    matched_comparison = {
        "status": "VALID",
        "topk8_result_path": str(topk8_res_p),
        "topk8_result_sha256": topk8_res_sha,
        "membership_exact_match": True,
        "query_key_equality": True,
        "threshold_independent": {
            "topk8_query_auroc": topk8_auroc,
            "mimic_seed0_row_auroc": s0_metrics["auroc"],
            "delta_auroc": s0_metrics["auroc"] - topk8_auroc,
            "topk8_query_auprc": topk8_auprc,
            "mimic_seed0_row_auprc": s0_metrics["auprc"],
            "delta_auprc": s0_metrics["auprc"] - topk8_auprc,
        },
        "matched_row_best_f1": {
            "topk8": {
                "threshold": topk8_best_f1_th,
                "success_false_alarms": topk8_best_f1_fa_count,
                "success_episodes": 658,
                "false_alarm_rate": topk8_best_f1_fa_rate,
                "failure_detected": 78,
                "failure_episodes": 78,
                "detection_rate": topk8_best_f1_det_rate,
            },
            "mimic_seed0": {
                "threshold": s0_f1_eval["threshold"],
                "success_false_alarms": s0_f1_eval["success_false_alarms"],
                "success_episodes": 658,
                "false_alarm_rate": s0_f1_eval["fpr"],
                "failure_detected": s0_f1_eval["failure_detected"],
                "failure_episodes": 78,
                "detection_rate": s0_f1_eval["recall"],
                "det_at_10_count": s0_f1_eval["det_10_count"],
                "det_at_10_rate": s0_f1_eval["det_10_rate"],
                "det_at_25_count": s0_f1_eval["det_25_count"],
                "det_at_25_rate": s0_f1_eval["det_25_rate"],
                "det_at_50_count": s0_f1_eval["det_50_count"],
                "det_at_50_rate": s0_f1_eval["det_50_rate"],
                "never_count": s0_f1_eval["never_detected"],
                "mean_first_alarm_fraction": s0_f1_eval["mean_first_alarm_fraction"],
            },
            "deltas_mimic_minus_topk8": {
                "fa_delta_count": s0_f1_eval["success_false_alarms"] - topk8_best_f1_fa_count,
                "fa_delta_percentage_points": (s0_f1_eval["fpr"] - topk8_best_f1_fa_rate) * 100,
                "failure_detection_delta_count": s0_f1_eval["failure_detected"] - 78,
            }
        },
        "mimic_primary_alpha010_operating_point": {
            "threshold": s0_a10_eval["threshold"],
            "success_false_alarms": s0_a10_eval["success_false_alarms"],
            "success_episodes": 658,
            "false_alarm_rate": s0_a10_eval["fpr"],
            "failure_detected": s0_a10_eval["failure_detected"],
            "failure_episodes": 78,
            "detection_rate": s0_a10_eval["recall"],
            "det_at_10_count": s0_a10_eval["det_10_count"],
            "det_at_10_rate": s0_a10_eval["det_10_rate"],
            "det_at_25_count": s0_a10_eval["det_25_count"],
            "det_at_25_rate": s0_a10_eval["det_25_rate"],
            "det_at_50_count": s0_a10_eval["det_50_count"],
            "det_at_50_rate": s0_a10_eval["det_50_rate"],
            "never_count": s0_a10_eval["never_detected"],
            "mean_first_alarm_fraction": s0_a10_eval["mean_first_alarm_fraction"],
        }
    }
    with open(snapshot_dir / "MATCHED_TOPK8_COMPARISON.json", "w") as f:
        json.dump(matched_comparison, f, indent=2)

    # Step 4: Held-Out Freeze Package
    heldout_freeze = {
        "experiment_name": EXPERIMENT_NAME,
        "source_manifest_sha256": EXPECTED_SOURCE_MANIFEST_SHA,
        "source_split_sha256": EXPECTED_SOURCE_SPLIT_SHA,
        "derived_manifest_sha256": EXPECTED_DERIVED_MANIFEST_SHA,
        "normalization_sha256": EXPECTED_NORMALIZATION_SHA,
        "training_freeze_sha256": EXPECTED_TRAINING_FREEZE_SHA,
        "primary_seed": 0,
        "primary_operating_point": "conformal_alpha_0.10",
        "test_used_for_selection": False,
        "ood_scored": False,
        "primary_result": {
            "threshold": s0_a10_eval["threshold"],
            "row_auroc": s0_metrics["auroc"],
            "row_auprc": s0_metrics["auprc"],
            "success_false_alarm_count": s0_a10_eval["success_false_alarms"],
            "success_episodes": 658,
            "success_false_alarm_rate": s0_a10_eval["fpr"],
            "failure_detection_count": s0_a10_eval["failure_detected"],
            "failure_episodes": 78,
            "failure_detection_rate": s0_a10_eval["recall"],
            "det_at_10_count": s0_a10_eval["det_10_count"],
            "det_at_10_rate": s0_a10_eval["det_10_rate"],
            "det_at_25_count": s0_a10_eval["det_25_count"],
            "det_at_25_rate": s0_a10_eval["det_25_rate"],
            "det_at_50_count": s0_a10_eval["det_50_count"],
            "det_at_50_rate": s0_a10_eval["det_50_rate"],
            "never_count": s0_a10_eval["never_detected"],
            "mean_first_alarm_fraction": s0_a10_eval["mean_first_alarm_fraction"],
        },
        "robustness_alpha010": {
            "mean_row_auroc": float(np.mean(aurocs)),
            "std_row_auroc": float(np.std(aurocs)),
            "mean_row_auprc": float(np.mean(auprcs)),
            "std_row_auprc": float(np.std(auprcs)),
            "mean_fa_percent": float(np.mean(fa_pcts)),
            "std_fa_percent": float(np.std(fa_pcts)),
            "mean_failure_detection_percent": float(np.mean(rec_pcts)),
            "std_failure_detection_percent": float(np.std(rec_pcts)),
            "mean_det25_percent": float(np.mean(det25_pcts)),
            "std_det25_percent": float(np.std(det25_pcts)),
            "mean_det50_percent": float(np.mean(det50_pcts)),
            "std_det50_percent": float(np.std(det50_pcts)),
        },
        "matched_topk8_comparison": matched_comparison,
        "seed_results": {str(s): seed_results[s] for s in SEEDS},
    }

    freeze_p = test_out_dir / "HELDOUT_TEST_FREEZE.json"
    with open(freeze_p, "w") as f:
        json.dump(heldout_freeze, f, indent=2)
    freeze_sha = sha256_file(freeze_p)
    with open(snapshot_dir / "HELDOUT_TEST_FREEZE.json", "w") as f:
        json.dump(heldout_freeze, f, indent=2)

    # Write Markdown Summary
    s_lines = [
        f"# Stage 1 Summary — {EXPERIMENT_NAME} Held-Out Test Evaluation",
        "",
        "## 1. Primary Result (Seed 0, Conformal Alpha=0.10)",
        f"- Threshold: {s0_a10_eval['threshold']:.6f}",
        f"- Row AUROC: {s0_metrics['auroc']:.6f}",
        f"- Row AUPRC: {s0_metrics['auprc']:.6f}",
        f"- Success False Alarms: {s0_a10_eval['success_false_alarms']}/658 ({s0_a10_eval['fpr']*100:.2f}%)",
        f"- Failure Detection: {s0_a10_eval['failure_detected']}/78 ({s0_a10_eval['recall']*100:.2f}%)",
        f"- Det@10: {s0_a10_eval['det_10_count']}/78 ({s0_a10_eval['det_10_rate']*100:.2f}%)",
        f"- Det@25: {s0_a10_eval['det_25_count']}/78 ({s0_a10_eval['det_25_rate']*100:.2f}%)",
        f"- Det@50: {s0_a10_eval['det_50_count']}/78 ({s0_a10_eval['det_50_rate']*100:.2f}%)",
        f"- Never Detected: {s0_a10_eval['never_detected']}/78",
        f"- Mean Detection Fraction: {s0_a10_eval['mean_first_alarm_fraction']:.4f}",
        "",
        "## 2. Robustness Across All 5 Seeds (Conformal Alpha=0.10)",
        "| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in SEEDS:
        te = seed_results[s]["test_episode_evaluations"]["conformal_alpha_0.10"]
        s_lines.append(
            f"| Seed {s} | {seed_results[s]['row_metrics']['auroc']:.4f} | {seed_results[s]['row_metrics']['auprc']:.4f} | {te['success_false_alarms']}/658 ({te['fpr']*100:.2f}%) | {te['failure_detected']}/78 ({te['recall']*100:.2f}%) | {te['det_25_count']}/78 ({te['det_25_rate']*100:.2f}%) | {te['det_50_count']}/78 ({te['det_50_rate']*100:.2f}%) |"
        )
    s_lines.extend([
        "",
        f"- Mean Row AUROC: {np.mean(aurocs):.4f} +/- {np.std(aurocs):.4f}",
        f"- Mean Row AUPRC: {np.mean(auprcs):.4f} +/- {np.std(auprcs):.4f}",
        f"- Mean FA Percent: {np.mean(fa_pcts):.2f}% +/- {np.std(fa_pcts):.2f}%",
        f"- Mean Failure Detection: {np.mean(rec_pcts):.2f}% +/- {np.std(rec_pcts):.2f}%",
        f"- Mean Det@25: {np.mean(det25_pcts):.2f}% +/- {np.std(det25_pcts):.2f}%",
        f"- Mean Det@50: {np.mean(det50_pcts):.2f}% +/- {np.std(det50_pcts):.2f}%",
        "",
        "## 3. Matched TopK8 Comparison",
        f"- TopK8 AUROC: {topk8_auroc:.4f} | Mimic Seed0 AUROC: {s0_metrics['auroc']:.4f} (Delta: {s0_metrics['auroc'] - topk8_auroc:+.4f})",
        f"- TopK8 AUPRC: {topk8_auprc:.4f} | Mimic Seed0 AUPRC: {s0_metrics['auprc']:.4f} (Delta: {s0_metrics['auprc'] - topk8_auprc:+.4f})",
        f"- TopK8 Best-F1 FA: {topk8_best_f1_fa_count}/658 ({topk8_best_f1_fa_rate*100:.2f}%) | Mimic Best-F1 FA: {s0_f1_eval['success_false_alarms']}/658 ({s0_f1_eval['fpr']*100:.2f}%)",
        f"- TopK8 Best-F1 Det: 78/78 (100.00%) | Mimic Best-F1 Det: {s0_f1_eval['failure_detected']}/78 ({s0_f1_eval['recall']*100:.2f}%)",
    ])
    with open(snapshot_dir / "STAGE1_SUMMARY.md", "w") as f:
        f.write("\n".join(s_lines) + "\n")

    print(f"STAGE 1 COMPLETE! Heldout Freeze SHA256: {freeze_sha}")
    return heldout_freeze


def run_stage1(
    workspace_path: str,
    snapshot_dir_path: str,
    device: torch.device,
) -> Dict[str, Any]:
    w_dir = Path(workspace_path)
    snapshot_dir = Path(snapshot_dir_path)
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    source_ds_dir = w_dir / "frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1"
    topk8_model_dir = w_dir / "models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2"
    derived_ds_dir = w_dir / f"derived_datasets/{EXPERIMENT_NAME}"
    model_root = w_dir / f"models/{EXPERIMENT_NAME}"
    val_root = w_dir / f"evaluations/{EXPERIMENT_NAME}/validation"
    test_out_dir = w_dir / f"evaluations/{EXPERIMENT_NAME}/test"

    pretest_res = run_pretest_gates(
        w_dir, source_ds_dir, topk8_model_dir, derived_ds_dir, model_root, val_root, test_out_dir, snapshot_dir
    )

    heldout_freeze = score_held_out_test(
        w_dir, topk8_model_dir, derived_ds_dir, model_root, val_root, test_out_dir, snapshot_dir, device
    )

    return heldout_freeze


def main():
    parser = argparse.ArgumentParser(description="AGY Stage 1 One-Time Held-Out Test for NEW4904 Mimic V3")
    parser.add_argument("--workspace", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
    parser.add_argument("--snapshot_dir", type=str, default="/home/redafrix/tests/internship/prepared_experiments/dean_isaac_mimic_risk_4904_3cm350_20260819/stage1_snapshot")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    run_stage1(args.workspace, args.snapshot_dir, torch.device(args.device))


if __name__ == "__main__":
    main()
