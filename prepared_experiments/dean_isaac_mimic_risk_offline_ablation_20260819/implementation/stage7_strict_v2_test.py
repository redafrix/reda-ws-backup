"""Stage 7 Strict Mimic Fidelity V2: One-Time Held-Out Seen Evaluation."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import torch

from .constants import SEEDS
from .dataset import IsaacMimicWindowDataset
from .model import MimicH10RiskMonitor
from .evaluate import compute_row_metrics, compute_episode_evaluation, score_split, sha256_file


STRICT_V2_EXP_NAME = "isaac_mimic_h10_strict_missingdyn_v2"

EXPECTED_DATASET_MANIFEST_SHA = "852ad05e6208caba23c630174eb6784793304281169e5e24a25da22d030b57a1"
EXPECTED_NORMALIZATION_SHA = "d055a71bc2e531264f35d8bdd91e545d3f3b39cbba1cc543699ec1b987107830"
EXPECTED_TRAINING_FREEZE_SHA = "ecf7fa8e2b8b755663f81dfd1e2b63c2bd578a1da03ee38ea1a94bc24128d6fd"

EXPECTED_SEED0_CKPT_SHA = "78b801c9071561108dded63d4e4b43fcf3b423932864f6817f808d6268e17fe6"
EXPECTED_SEED0_ALPHA010_TH = 0.6284286379814148


def run_pretest_gates(
    w_dir: Path,
    v2_derived_dir: Path,
    v1_derived_dir: Path,
    model_root: Path,
    val_root: Path,
    snapshot_dir: Path,
) -> Dict[str, Any]:
    print("1. Running Pretest Cryptographic & Fidelity Gates...")

    # Gate 1: Dataset Manifest & Normalization hashes
    manifest_p = v2_derived_dir / "dataset_manifest.json"
    manifest_sha = sha256_file(manifest_p)
    assert manifest_sha == EXPECTED_DATASET_MANIFEST_SHA, f"Manifest SHA mismatch: {manifest_sha}"

    norm_p = v2_derived_dir / "normalization.json"
    norm_sha = sha256_file(norm_p)
    assert norm_sha == EXPECTED_NORMALIZATION_SHA, f"Norm SHA mismatch: {norm_sha}"

    # Gate 2: Training Freeze hash & Seed bindings
    tf_p = model_root / "TRAINING_FREEZE.json"
    tf_sha = sha256_file(tf_p)
    assert tf_sha == EXPECTED_TRAINING_FREEZE_SHA, f"Training Freeze SHA mismatch: {tf_sha}"

    with open(tf_p) as f:
        tf_data = json.load(f)

    assert tf_data["primary_seed"] == 0
    assert tf_data["primary_operating_point"] == "conformal_alpha_0.10"

    for s in SEEDS:
        s_data = tf_data["seeds"][str(s)]
        ckpt_p = Path(s_data["checkpoint_path"])
        assert ckpt_p.exists(), f"Missing ckpt: {ckpt_p}"
        actual_ckpt_sha = sha256_file(ckpt_p)
        assert actual_ckpt_sha == s_data["checkpoint_sha256"], f"Seed {s} ckpt SHA mismatch: {actual_ckpt_sha}"

        vf_p = Path(s_data["validation_freeze_path"])
        assert vf_p.exists(), f"Missing val freeze: {vf_p}"
        actual_vf_sha = sha256_file(vf_p)
        assert actual_vf_sha == s_data["validation_freeze_sha256"], f"Seed {s} val freeze SHA mismatch: {actual_vf_sha}"

    # Verify seed 0 primary values
    assert tf_data["seeds"]["0"]["checkpoint_sha256"] == EXPECTED_SEED0_CKPT_SHA
    with open(tf_data["seeds"]["0"]["validation_freeze_path"]) as f:
        s0_vf = json.load(f)
    s0_th = s0_vf["calibrated_thresholds"]["conformal_alpha_0.10"]
    assert abs(s0_th - EXPECTED_SEED0_ALPHA010_TH) < 1e-6, f"Seed 0 Alpha0.10 threshold mismatch: {s0_th}"

    # Gate 3: Dataset fidelity on frozen arrays
    v2_scalars = np.load(v2_derived_dir / "raw/scalar37.npy")
    v2_horizon = np.load(v2_derived_dir / "raw/horizon10x6.npy")
    labels = np.load(v2_derived_dir / "labels.npy")
    split_idx = np.load(v2_derived_dir / "split_index.npy")
    ep_idx = np.load(v2_derived_dir / "episode_index.npy")

    v1_scalars = np.load(v1_derived_dir / "raw/scalar37.npy")
    v1_horizon = np.load(v1_derived_dir / "raw/horizon10x6.npy")

    n_total = len(labels)
    assert n_total == 75603

    test_row_mask = (split_idx == 2)
    test_row_idx = np.where(test_row_mask)[0]
    n_test_rows = len(test_row_idx)
    assert n_test_rows == 11368, f"Expected 11368 test rows, got {n_test_rows}"

    test_episodes = np.unique(ep_idx[test_row_mask])
    n_test_eps = len(test_episodes)
    assert n_test_eps == 600, f"Expected 600 test episodes, got {n_test_eps}"

    # Count success/failure episodes in test
    ep_labels = {}
    for r_i in test_row_idx:
        ep = ep_idx[r_i]
        ep_labels[ep] = labels[r_i]

    test_successes = sum(1 for lbl in ep_labels.values() if lbl == 0)
    test_failures = sum(1 for lbl in ep_labels.values() if lbl == 1)
    assert test_successes == 586, f"Expected 586 test successes, got {test_successes}"
    assert test_failures == 14, f"Expected 14 test failures, got {test_failures}"

    # Check zero channels on test rows
    strict_zeros_test = bool(np.all(v2_scalars[test_row_mask, 9:34] == 0.0))
    assert strict_zeros_test, "Disabled channels on test rows are not all zero!"

    # Check available channel equality to V1 on test rows
    s0_8_match = bool(np.array_equal(v2_scalars[test_row_mask, 0:9], v1_scalars[test_row_mask, 0:9]))
    s34_36_match = bool(np.array_equal(v2_scalars[test_row_mask, 34:37], v1_scalars[test_row_mask, 34:37]))
    h_match = bool(np.array_equal(v2_horizon[test_row_mask], v1_horizon[test_row_mask]))
    assert s0_8_match, "Scalar 0..8 does not match V1 on test rows!"
    assert s34_36_match, "Scalar 34..36 does not match V1 on test rows!"
    assert h_match, "Horizon does not match V1 on test rows!"

    # Gate 4: TopK8 Test Membership Proof
    split_assign_p = w_dir / "frozen_datasets/isaac_seen_h10_topk8_v1/split_assignments.json"
    with open(split_assign_p) as f:
        split_assign = json.load(f)

    with open(v2_derived_dir / "episode_ids.json") as f:
        v2_ep_ids = json.load(f)

    v2_test_ep_ids = set(v2_ep_ids[ep_ord] for ep_ord in test_episodes)
    source_test_ep_ids = set(k for k, v in split_assign.items() if v.get("split") == "test")

    exact_topk8_membership = (v2_test_ep_ids == source_test_ep_ids)
    assert exact_topk8_membership, "Test episode IDs do not match source split assignments!"
    assert len(v2_test_ep_ids) == 600

    pretest_res = {
        "status": "PASSED",
        "dataset_manifest_sha256": manifest_sha,
        "normalization_sha256": norm_sha,
        "training_freeze_sha256": tf_sha,
        "checkpoint_and_validation_bindings_all_match": True,
        "strict_zero_channels_test_rows": True,
        "exact_topk8_test_membership": True,
        "test_rows": n_test_rows,
        "test_episodes": n_test_eps,
        "test_successes": test_successes,
        "test_failures": test_failures,
    }
    with open(snapshot_dir / "PRETEST_GATE.json", "w") as f:
        json.dump(pretest_res, f, indent=2)

    print("Pretest Gates PASSED successfully!")
    return pretest_res


def score_held_out_seen_test(
    w_dir: Path,
    v2_derived_dir: Path,
    model_root: Path,
    val_root: Path,
    test_out_dir: Path,
    snapshot_dir: Path,
    device: torch.device,
) -> Dict[str, Any]:
    print("2. Scoring Held-Out Seen Test for All 5 Seeds...")
    test_out_dir.mkdir(parents=True, exist_ok=True)

    raw_scalars = np.load(v2_derived_dir / "raw/scalar37.npy")
    raw_horizon = np.load(v2_derived_dir / "raw/horizon10x6.npy")
    labels = np.load(v2_derived_dir / "labels.npy")
    ep_idx = np.load(v2_derived_dir / "episode_index.npy")
    dec_idx = np.load(v2_derived_dir / "decision_index.npy")
    split_idx = np.load(v2_derived_dir / "split_index.npy")

    with open(v2_derived_dir / "normalization.json") as f:
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
        ckpt_p = model_root / f"seed_{s}" / "best_model.pt"
        ckpt_sha = sha256_file(ckpt_p)

        vf_p = val_root / f"seed_{s}" / "FROZEN_VALIDATION_SELECTION.json"
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
            "experiment_name": STRICT_V2_EXP_NAME,
            "seed": s,
            "selected_epoch": ckpt["epoch"],
            "model_checkpoint_path": str(ckpt_p),
            "model_checkpoint_sha256": ckpt_sha,
            "frozen_validation_reference": str(vf_p),
            "test_rows_count": len(test_row_idx),
            "test_episodes_count": 600,
            "test_failure_episodes_count": 14,
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

    # TopK8 matched comparison
    topk8_seen_p = w_dir / "models/isaac_h10_topk8_temporal_v1/results.json"
    topk8_data = {}
    if topk8_seen_p.exists():
        with open(topk8_seen_p) as f:
            topk8_data = json.load(f)

    # TopK8 best_val_f1 stats on seen 600
    topk8_auroc = 0.9310794796642061
    topk8_auprc = 0.818629985131437
    topk8_f1_fa = 12
    topk8_f1_rec = 14
    topk8_f1_d10 = 2
    topk8_f1_d25 = 5
    topk8_f1_d50 = 14

    s0_f1 = seed_results[0]["test_episode_evaluations"]["row_best_f1"]
    s0_a10 = seed_results[0]["test_episode_evaluations"]["conformal_alpha_0.10"]

    matched_topk8 = {
        "provenance_reference": "PRETEST_GATE.json",
        "topk8_source": {
            "results_path": str(topk8_seen_p),
            "model_type": "SeqRiskModel (TopK8)",
            "dataset_manifest_sha256": "8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859",
        },
        "strict_v2_source": {
            "experiment_name": STRICT_V2_EXP_NAME,
            "primary_seed": 0,
            "model_type": "MimicH10RiskMonitor (Strict Missing Dynamics V2)",
        },
        "threshold_independent": {
            "topk8_auroc": topk8_auroc,
            "strict_v2_seed0_auroc": seed_results[0]["row_metrics"]["auroc"],
            "delta_auroc": seed_results[0]["row_metrics"]["auroc"] - topk8_auroc,
            "topk8_auprc": topk8_auprc,
            "strict_v2_seed0_auprc": seed_results[0]["row_metrics"]["auprc"],
            "delta_auprc": seed_results[0]["row_metrics"]["auprc"] - topk8_auprc,
        },
        "row_best_f1_matched_calibration": {
            "topk8": {
                "threshold": 0.7990124225616455,
                "success_false_alarms": topk8_f1_fa,
                "success_episodes": 586,
                "false_alarm_rate": topk8_f1_fa / 586,
                "failure_detected": topk8_f1_rec,
                "failure_episodes": 14,
                "detection_rate": topk8_f1_rec / 14,
                "det_at_10_count": topk8_f1_d10,
                "det_at_10_rate": topk8_f1_d10 / 14,
                "det_at_25_count": topk8_f1_d25,
                "det_at_25_rate": topk8_f1_d25 / 14,
                "det_at_50_count": topk8_f1_d50,
                "det_at_50_rate": topk8_f1_d50 / 14,
            },
            "strict_v2": {
                "threshold": s0_f1["threshold"],
                "success_false_alarms": s0_f1["success_false_alarms"],
                "success_episodes": 586,
                "false_alarm_rate": s0_f1["fpr"],
                "failure_detected": s0_f1["failure_detected"],
                "failure_episodes": 14,
                "detection_rate": s0_f1["recall"],
                "det_at_10_count": s0_f1["det_10_count"],
                "det_at_10_rate": s0_f1["det_10_rate"],
                "det_at_25_count": s0_f1["det_25_count"],
                "det_at_25_rate": s0_f1["det_25_rate"],
                "det_at_50_count": s0_f1["det_50_count"],
                "det_at_50_rate": s0_f1["det_50_rate"],
            },
            "deltas_strict_v2_minus_topk8": {
                "fa_delta_percentage_points": (s0_f1["fpr"] - (topk8_f1_fa / 586)) * 100,
                "fa_delta_count": s0_f1["success_false_alarms"] - topk8_f1_fa,
                "failure_detection_delta_count": s0_f1["failure_detected"] - topk8_f1_rec,
                "det_at_10_delta_count": s0_f1["det_10_count"] - topk8_f1_d10,
                "det_at_25_delta_count": s0_f1["det_25_count"] - topk8_f1_d25,
                "det_at_50_delta_count": s0_f1["det_50_count"] - topk8_f1_d50,
            }
        },
        "strict_v2_primary_conformal_alpha010": {
            "threshold": s0_a10["threshold"],
            "success_false_alarms": s0_a10["success_false_alarms"],
            "success_episodes": 586,
            "false_alarm_rate": s0_a10["fpr"],
            "failure_detected": s0_a10["failure_detected"],
            "failure_episodes": 14,
            "detection_rate": s0_a10["recall"],
            "det_at_10_count": s0_a10["det_10_count"],
            "det_at_10_rate": s0_a10["det_10_rate"],
            "det_at_25_count": s0_a10["det_25_count"],
            "det_at_25_rate": s0_a10["det_25_rate"],
            "det_at_50_count": s0_a10["det_50_count"],
            "det_at_50_rate": s0_a10["det_50_rate"],
        }
    }
    with open(snapshot_dir / "TOPK8_MATCHED_COMPARISON_V2.json", "w") as f:
        json.dump(matched_topk8, f, indent=2)

    heldout_freeze = {
        "experiment_name": STRICT_V2_EXP_NAME,
        "dataset_manifest_sha256": EXPECTED_DATASET_MANIFEST_SHA,
        "normalization_sha256": EXPECTED_NORMALIZATION_SHA,
        "training_freeze_sha256": EXPECTED_TRAINING_FREEZE_SHA,
        "primary_seed": 0,
        "primary_operating_point": "conformal_alpha_0.10",
        "test_used_for_selection": False,
        "ood_scored": False,
        "primary_result": {
            "threshold": s0_a10["threshold"],
            "row_auroc": seed_results[0]["row_metrics"]["auroc"],
            "row_auprc": seed_results[0]["row_metrics"]["auprc"],
            "success_false_alarm_count": s0_a10["success_false_alarms"],
            "success_episodes": 586,
            "success_false_alarm_rate": s0_a10["fpr"],
            "failure_detection_count": s0_a10["failure_detected"],
            "failure_episodes": 14,
            "failure_detection_rate": s0_a10["recall"],
            "det_at_10_count": s0_a10["det_10_count"],
            "det_at_10_rate": s0_a10["det_10_rate"],
            "det_at_25_count": s0_a10["det_25_count"],
            "det_at_25_rate": s0_a10["det_25_rate"],
            "det_at_50_count": s0_a10["det_50_count"],
            "det_at_50_rate": s0_a10["det_50_rate"],
            "never_count": s0_a10["never_detected"],
            "mean_detection_fraction": s0_a10["mean_first_alarm_fraction"],
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
        "matched_topk8_comparison": matched_topk8,
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
        "# Stage 7 Summary — Strict Mimic Fidelity V2 Held-Out Seen Evaluation",
        "",
        "## 1. Primary Result (Seed 0, Conformal Alpha=0.10)",
        f"- Threshold: {s0_a10['threshold']:.6f}",
        f"- Row AUROC: {seed_results[0]['row_metrics']['auroc']:.6f}",
        f"- Row AUPRC: {seed_results[0]['row_metrics']['auprc']:.6f}",
        f"- Success False Alarms: {s0_a10['success_false_alarms']}/586 ({s0_a10['fpr']*100:.2f}%)",
        f"- Failure Detection: {s0_a10['failure_detected']}/14 ({s0_a10['recall']*100:.2f}%)",
        f"- Det@10: {s0_a10['det_10_count']}/14 ({s0_a10['det_10_rate']*100:.2f}%)",
        f"- Det@25: {s0_a10['det_25_count']}/14 ({s0_a10['det_25_rate']*100:.2f}%)",
        f"- Det@50: {s0_a10['det_50_count']}/14 ({s0_a10['det_50_rate']*100:.2f}%)",
        f"- Never Detected: {s0_a10['never_detected']}/14",
        f"- Mean Detection Fraction: {s0_a10['mean_first_alarm_fraction']:.4f}",
        "",
        "## 2. Robustness Across All 5 Seeds (Conformal Alpha=0.10)",
        "| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in SEEDS:
        te = seed_results[s]["test_episode_evaluations"]["conformal_alpha_0.10"]
        s_lines.append(
            f"| Seed {s} | {seed_results[s]['row_metrics']['auroc']:.4f} | {seed_results[s]['row_metrics']['auprc']:.4f} | {te['success_false_alarms']}/586 ({te['fpr']*100:.2f}%) | {te['failure_detected']}/14 ({te['recall']*100:.2f}%) | {te['det_25_count']}/14 ({te['det_25_rate']*100:.2f}%) | {te['det_50_count']}/14 ({te['det_50_rate']*100:.2f}%) |"
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
        "## 3. Matched TopK8 Comparison (Row Best-F1)",
        f"- TopK8 AUROC: {topk8_auroc:.4f} | Strict V2 Seed0 AUROC: {seed_results[0]['row_metrics']['auroc']:.4f} (Delta: {seed_results[0]['row_metrics']['auroc'] - topk8_auroc:+.4f})",
        f"- TopK8 AUPRC: {topk8_auprc:.4f} | Strict V2 Seed0 AUPRC: {seed_results[0]['row_metrics']['auprc']:.4f} (Delta: {seed_results[0]['row_metrics']['auprc'] - topk8_auprc:+.4f})",
        f"- TopK8 Best-F1 FA: {topk8_f1_fa}/586 ({topk8_f1_fa/586*100:.2f}%) | Strict V2 Best-F1 FA: {s0_f1['success_false_alarms']}/586 ({s0_f1['fpr']*100:.2f}%)",
        f"- TopK8 Best-F1 Det@25: {topk8_f1_d25}/14 ({topk8_f1_d25/14*100:.2f}%) | Strict V2 Best-F1 Det@25: {s0_f1['det_25_count']}/14 ({s0_f1['det_25_rate']*100:.2f}%)",
    ])
    with open(snapshot_dir / "STAGE7_SUMMARY.md", "w") as f:
        f.write("\n".join(s_lines) + "\n")

    print(f"STAGE 7 COMPLETE! Heldout Freeze SHA256: {freeze_sha}")
    return heldout_freeze


def run_stage7(
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
    test_out_dir = w_dir / "evaluations/isaac_mimic_h10_strict_missingdyn_v2/test"

    # Step 1: Pretest Gate
    pretest_res = run_pretest_gates(w_dir, v2_derived_dir, v1_derived_dir, model_root, val_root, snapshot_dir)

    # Step 2: One-time held-out evaluation
    heldout_freeze = score_held_out_seen_test(w_dir, v2_derived_dir, model_root, val_root, test_out_dir, snapshot_dir, device)

    return heldout_freeze


def main():
    parser = argparse.ArgumentParser(description="Stage 7 Strict Mimic V2 Held-Out Seen Evaluation")
    parser.add_argument("--workspace", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
    parser.add_argument("--snapshot_dir", type=str, default="/home/redafrix/tests/internship/prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/strict_v2_snapshot")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    run_stage7(args.workspace, args.snapshot_dir, torch.device(args.device))


if __name__ == "__main__":
    main()
