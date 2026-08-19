"""Stage 4 One-Time Held-Out Seen Evaluation Runner."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch

from .constants import (
    EXPERIMENT_NAME,
    SEEDS,
    TOTAL_ROWS,
    TEST_ROWS,
    TEST_EPISODES,
)
from .evaluate import run_held_out_test, sha256_file, score_split
from .dataset import IsaacMimicWindowDataset
from .model import MimicH10RiskMonitor


def run_stage4(
    derived_dir_path: str,
    model_root_path: str,
    val_root_path: str,
    heldout_root_path: str,
    snapshot_dir_path: str,
    device: torch.device,
) -> Dict[str, Any]:
    derived_dir = Path(derived_dir_path)
    model_root = Path(model_root_path)
    val_root = Path(val_root_path)
    heldout_root = Path(heldout_root_path)
    snapshot_dir = Path(snapshot_dir_path)

    heldout_root.mkdir(parents=True, exist_ok=True)
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    # 1. Cryptographic pretest gate
    manifest_v2_p = derived_dir / "dataset_manifest_v2.json"
    manifest_v2_sha = sha256_file(manifest_v2_p)
    assert manifest_v2_sha == "043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3", f"Manifest mismatch: {manifest_v2_sha}"

    norm_p = derived_dir / "normalization.json"
    norm_sha = sha256_file(norm_p)
    assert norm_sha == "40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a", f"Norm mismatch: {norm_sha}"

    tf_p = model_root / "TRAINING_FREEZE.json"
    tf_sha = sha256_file(tf_p)
    assert tf_sha == "8d84010c2989d605a910775e4a762e084f9b34de6855b323781356d3258876a0", f"Training freeze mismatch: {tf_sha}"

    vf_all_p = val_root / "VALIDATION_FREEZE_ALL_SEEDS.json"
    vf_all_sha = sha256_file(vf_all_p)
    assert vf_all_sha == "4235179f98634a1dce53f013b3dd06ecb37cf2a7ad7e12564b4027dc9889a50a", f"Validation freeze mismatch: {vf_all_sha}"

    expected_ckpts = {
        0: "4869526f636dc005b4cbcd85c8cfce1f307618fed9f81784f3fd3ee3c3180cf3",
        1: "9328a8102060bb46414b8f8bd3f71eedd61f4ce93949822dfe2138d4b9a40590",
        2: "199a17c2a34c56f4807869f2aa8cc556ba43a39c2bb000719612971ab1ccb693",
        3: "f745aa5392918b56135710e7cdb05e2a15c9bc19e9cd03284e5c9885fcfb20a8",
        4: "15825ca05155b6ba1248b5542454ae33bd210d77cf86522ceb28e28567d90cb7",
    }

    expected_val_freezes = {
        0: "5c087cbcbc0edee927e10d04b35b86059a4c186bdd27fff91b42bc7039883f84",
        1: "e4327ad5b7a3966550674ff24dc8bfd4741faf1d6f09d52db39ee4707f4d0cf8",
        2: "d791e83ecb90b9ec77142dfedcff1b3c5835422cb2f830b62e2ae85fde4ec10e",
        3: "cf888c2926043d8d967784d7d42ecd4942c5a401b9f713c87a3375277555b30c",
        4: "db6ede7faf10090fdaf49441a796788f257aeb3d4271cdcf2288eee3b9fc3b2a",
    }

    gate_seed_checks = {}
    for s in SEEDS:
        ckpt_p = model_root / f"seed_{s}" / "best_model.pt"
        ckpt_sha = sha256_file(ckpt_p)
        assert ckpt_sha == expected_ckpts[s], f"Seed {s} ckpt mismatch: {ckpt_sha} != {expected_ckpts[s]}"

        vf_p = val_root / f"seed_{s}" / "FROZEN_VALIDATION_SELECTION.json"
        vf_sha = sha256_file(vf_p)
        assert vf_sha == expected_val_freezes[s], f"Seed {s} val freeze mismatch: {vf_sha} != {expected_val_freezes[s]}"

        with open(vf_p) as f:
            vf_data = json.load(f)
        assert vf_data["model_checkpoint_sha256"] == ckpt_sha
        assert vf_data["normalization_sha256"] == norm_sha
        assert vf_data["dataset_manifest_v2_sha256"] == manifest_v2_sha

        gate_seed_checks[s] = {
            "checkpoint_sha256": ckpt_sha,
            "val_freeze_sha256": vf_sha,
            "val_thresholds": vf_data["calibrated_thresholds"],
            "checks_passed": True,
        }

    pretest_gate = {
        "gate_status": "PASSED",
        "dataset_manifest_sha256": manifest_v2_sha,
        "normalization_sha256": norm_sha,
        "training_freeze_sha256": tf_sha,
        "all_seed_validation_freeze_sha256": vf_all_sha,
        "seed_gate_checks": gate_seed_checks,
    }
    pretest_gate_p = heldout_root / "PRETEST_GATE.json"
    with open(pretest_gate_p, "w") as f:
        json.dump(pretest_gate, f, indent=2)
    pretest_gate_sha = sha256_file(pretest_gate_p)
    with open(snapshot_dir / "PRETEST_GATE.json", "w") as f:
        json.dump(pretest_gate, f, indent=2)

    print("Pre-test cryptographic gate PASSED!")

    # Load dataset arrays for raw score saving
    raw_scalars = np.load(derived_dir / "raw/scalar37.npy")
    raw_horizon = np.load(derived_dir / "raw/horizon10x6.npy")
    labels = np.load(derived_dir / "labels.npy")
    episode_indices = np.load(derived_dir / "episode_index.npy")
    decision_indices = np.load(derived_dir / "decision_index.npy")
    split_indices = np.load(derived_dir / "split_index.npy")

    with open(norm_p) as f:
        norm_params = json.load(f)

    test_row_idx = np.where(split_indices == 2)[0]
    test_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=test_row_idx
    )
    test_ep_arr = episode_indices[test_row_idx]
    test_dec_arr = decision_indices[test_row_idx]

    # 2. One-time scoring across all 5 seeds
    test_results: Dict[int, Dict[str, Any]] = {}

    for s in SEEDS:
        print(f"Scoring held-out test for Seed {s}...")
        ckpt_p = model_root / f"seed_{s}" / "best_model.pt"
        vf_p = val_root / f"seed_{s}" / "FROZEN_VALIDATION_SELECTION.json"
        seed_test_dir = heldout_root / f"seed_{s}"
        seed_test_dir.mkdir(parents=True, exist_ok=True)

        res = run_held_out_test(
            derived_dataset_dir=derived_dir,
            model_checkpoint_path=ckpt_p,
            validation_freeze_path=vf_p,
            output_dir=seed_test_dir,
            device=device,
        )

        test_res_p = seed_test_dir / "HELD_OUT_TEST_RESULTS.json"
        test_res_sha = sha256_file(test_res_p)

        # Save raw test scores npz outside git
        model = MimicH10RiskMonitor().to(device)
        ckpt = torch.load(ckpt_p, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])
        t_scores, t_targets = score_split(model, test_dataset, device)
        np.savez_compressed(
            seed_test_dir / "test_scores.npz",
            scores=t_scores,
            targets=t_targets,
            episode_index=test_ep_arr,
            decision_index=test_dec_arr,
        )

        test_results[s] = {
            "seed": s,
            "test_results_path": str(test_res_p),
            "test_results_sha256": test_res_sha,
            "row_metrics": res["test_row_metrics"],
            "threshold_evaluations": res["test_episode_evaluations"],
            "episode_count": TEST_EPISODES,
            "query_count": len(test_row_idx),
        }

        # Copy to snapshot directory
        with open(snapshot_dir / f"HELD_OUT_TEST_RESULTS_seed_{s}.json", "w") as f:
            json.dump(res, f, indent=2)

    # 3. TopK8 Comparison
    topk8_results_p = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_h10_topk8_temporal_v1/results.json")
    topk8_data = {}
    if topk8_results_p.exists():
        with open(topk8_results_p) as f:
            topk8_data = json.load(f)

    topk8_comparison = {
        "comparison_status": "NOT_DIRECTLY_COMPARABLE",
        "membership_exact_match": False,
        "membership_note": "TopK8 model isaac_h10_topk8_temporal_v1 used earlier dataset split in frozen_datasets/isaac_seen_h10_topk8_v1 with 133/600 episode overlap.",
        "topk8_source_path": str(topk8_results_p),
        "topk8_seen_test_results": topk8_data.get("seen_test", {}),
        "mimic_seed0_primary_results": test_results[0]["threshold_evaluations"]["conformal_alpha_0.10"],
        "mimic_seed0_row_metrics": test_results[0]["row_metrics"],
    }
    topk8_comp_p = heldout_root / "TOPK8_COMPARISON.json"
    with open(topk8_comp_p, "w") as f:
        json.dump(topk8_comparison, f, indent=2)
    with open(snapshot_dir / "TOPK8_COMPARISON.json", "w") as f:
        json.dump(topk8_comparison, f, indent=2)

    # 4. Freeze HELDOUT_SEEN_FREEZE.json
    s0_a10 = test_results[0]["threshold_evaluations"]["conformal_alpha_0.10"]

    aurocs = [test_results[s]["row_metrics"]["auroc"] for s in SEEDS]
    auprcs = [test_results[s]["row_metrics"]["auprc"] for s in SEEDS]
    fa_pcts = [test_results[s]["threshold_evaluations"]["conformal_alpha_0.10"]["fpr"] * 100 for s in SEEDS]
    rec_pcts = [test_results[s]["threshold_evaluations"]["conformal_alpha_0.10"]["recall"] * 100 for s in SEEDS]
    det10_pcts = [test_results[s]["threshold_evaluations"]["conformal_alpha_0.10"]["det_10_rate"] * 100 for s in SEEDS]
    det25_pcts = [test_results[s]["threshold_evaluations"]["conformal_alpha_0.10"]["det_25_rate"] * 100 for s in SEEDS]
    det50_pcts = [test_results[s]["threshold_evaluations"]["conformal_alpha_0.10"]["det_50_rate"] * 100 for s in SEEDS]

    heldout_freeze = {
        "experiment_name": EXPERIMENT_NAME,
        "pretest_gate_sha256": pretest_gate_sha,
        "dataset_manifest_sha256": manifest_v2_sha,
        "normalization_sha256": norm_sha,
        "training_freeze_sha256": tf_sha,
        "all_seed_validation_freeze_sha256": vf_all_sha,
        "checkpoint_sha256s": {str(s): expected_ckpts[s] for s in SEEDS},
        "validation_freeze_sha256s": {str(s): expected_val_freezes[s] for s in SEEDS},
        "held_out_result_sha256s": {str(s): test_results[s]["test_results_sha256"] for s in SEEDS},
        "primary_seed": 0,
        "primary_operating_point": "conformal_alpha_0.10",
        "primary_result": {
            "threshold": s0_a10["threshold"],
            "row_auroc": test_results[0]["row_metrics"]["auroc"],
            "row_auprc": test_results[0]["row_metrics"]["auprc"],
            "success_false_alarm_count": s0_a10["success_false_alarms"],
            "success_episodes": s0_a10["success_total"],
            "success_false_alarm_rate": s0_a10["fpr"],
            "failure_detection_count": s0_a10["failure_detected"],
            "failure_episodes": s0_a10["failure_total"],
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
        "robustness_aggregates": {
            "mean_row_auroc": float(np.mean(aurocs)),
            "std_row_auroc": float(np.std(aurocs)),
            "mean_row_auprc": float(np.mean(auprcs)),
            "std_row_auprc": float(np.std(auprcs)),
            "mean_fa_percent": float(np.mean(fa_pcts)),
            "std_fa_percent": float(np.std(fa_pcts)),
            "mean_failure_detection_percent": float(np.mean(rec_pcts)),
            "std_failure_detection_percent": float(np.std(rec_pcts)),
            "mean_det10_percent": float(np.mean(det10_pcts)),
            "std_det10_percent": float(np.std(det10_pcts)),
            "mean_det25_percent": float(np.mean(det25_pcts)),
            "std_det25_percent": float(np.std(det25_pcts)),
            "mean_det50_percent": float(np.mean(det50_pcts)),
            "std_det50_percent": float(np.std(det50_pcts)),
        },
        "test_used_for_selection": False,
        "ood_scored": False,
        "seed_test_results": test_results,
    }

    heldout_freeze_p = heldout_root / "HELDOUT_SEEN_FREEZE.json"
    with open(heldout_freeze_p, "w") as f:
        json.dump(heldout_freeze, f, indent=2)
    heldout_freeze_sha = sha256_file(heldout_freeze_p)
    with open(snapshot_dir / "HELDOUT_SEEN_FREEZE.json", "w") as f:
        json.dump(heldout_freeze, f, indent=2)

    # 5. Summary Markdown
    s_lines = [
        "# Stage 4 Summary — One-Time Held-Out Seen Evaluation",
        "",
        "## 1. Primary Predeclared Result (Seed 0, Conformal Alpha=0.10)",
        f"- Threshold: {s0_a10["threshold"]:.6f}",
        f"- Row AUROC: {test_results[0]["row_metrics"]["auroc"]:.6f}",
        f"- Row AUPRC: {test_results[0]["row_metrics"]["auprc"]:.6f}",
        f"- Success False Alarms: {s0_a10["success_false_alarms"]}/{s0_a10["success_total"]} ({s0_a10["fpr"]*100:.2f}%)",
        f"- Failure Detection: {s0_a10["failure_detected"]}/{s0_a10["failure_total"]} ({s0_a10["recall"]*100:.2f}%)",
        f"- Det@10: {s0_a10["det_10_count"]}/{s0_a10["failure_total"]} ({s0_a10["det_10_rate"]*100:.2f}%)",
        f"- Det@25: {s0_a10["det_25_count"]}/{s0_a10["failure_total"]} ({s0_a10["det_25_rate"]*100:.2f}%)",
        f"- Det@50: {s0_a10["det_50_count"]}/{s0_a10["failure_total"]} ({s0_a10["det_50_rate"]*100:.2f}%)",
        f"- Never Detected: {s0_a10["never_detected"]}/{s0_a10["failure_total"]}",
        f"- Mean Detection Fraction: {s0_a10["mean_first_alarm_fraction"]:.4f}",
        "",
        "## 2. Robustness Across All 5 Seeds (Conformal Alpha=0.10)",
        "| Seed | Row AUROC | Row AUPRC | Success FA | Failure Det | Det@25 | Det@50 |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in SEEDS:
        te = test_results[s]["threshold_evaluations"]["conformal_alpha_0.10"]
        s_lines.append(
            f"| Seed {s} | {test_results[s]["row_metrics"]["auroc"]:.4f} | {test_results[s]["row_metrics"]["auprc"]:.4f} | {te["success_false_alarms"]}/586 ({te["fpr"]*100:.2f}%) | {te["failure_detected"]}/14 ({te["recall"]*100:.2f}%) | {te["det_25_count"]}/14 ({te["det_25_rate"]*100:.2f}%) | {te["det_50_count"]}/14 ({te["det_50_rate"]*100:.2f}%) |"
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
        "## 3. Full Operating Point Table (Seed 0)",
        "| Operating Point | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 |",
        "|---|---|---|---|---|---|---|",
    ])
    for op_name, op_eval in test_results[0]["threshold_evaluations"].items():
        s_lines.append(
            f"| {op_name} | {op_eval["threshold"]:.4f} | {op_eval["success_false_alarms"]}/586 | {op_eval["failure_detected"]}/14 | {op_eval["det_10_count"]}/14 | {op_eval["det_25_count"]}/14 | {op_eval["det_50_count"]}/14 |"
        )

    with open(snapshot_dir / "STAGE4_SUMMARY.md", "w") as f:
        f.write("\n".join(s_lines) + "\n")

    print("Stage 4 evaluation complete and frozen successfully!")
    print(f"HELDOUT_SEEN_FREEZE SHA256: {heldout_freeze_sha}")
    return heldout_freeze


def main():
    parser = argparse.ArgumentParser(description="Stage 4 Held-out Seen Evaluation")
    parser.add_argument("--derived_dir", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_c0dyn_v1")
    parser.add_argument("--model_root", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_mimic_h10_c0dyn_v1")
    parser.add_argument("--val_root", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/evaluations/isaac_mimic_h10_c0dyn_v1/validation")
    parser.add_argument("--heldout_root", type=str, default="/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/evaluations/isaac_mimic_h10_c0dyn_v1/heldout_seen")
    parser.add_argument("--snapshot_dir", type=str, default="/home/redafrix/tests/internship/prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/heldout_snapshot")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    run_stage4(
        args.derived_dir,
        args.model_root,
        args.val_root,
        args.heldout_root,
        args.snapshot_dir,
        torch.device(args.device),
    )


if __name__ == "__main__":
    main()
