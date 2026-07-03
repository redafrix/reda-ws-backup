#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np
import torch

import run_dean_uncertainty_transformer_exploration_v2 as v2


POLICIES = [
    "base",
    "unc_raw",
    "avg_75base_25unc",
    "avg_50base_50unc",
    "max_base_unc",
    "soft_veto_base_times_unc",
    "mild_veto_unc_q95_or_base_q99",
    "hard_veto_unc_q95_or_base_q99",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def np_stats(obj: dict[str, dict[str, list[float]]]) -> dict[str, dict[str, np.ndarray]]:
    return {k: {kk: np.asarray(vv, dtype=np.float32) for kk, vv in v.items()} for k, v in obj.items()}


def load_model(job_dir: Path, variant: str, cfg: dict[str, Any], device: torch.device):
    stats = np_stats(load_json(job_dir / "normalization.json"))
    model = v2.SeqRiskModel(
        hist_dim=int(stats["history"]["mean"].shape[0]),
        action_dim=int(stats["action"]["mean"].shape[0]),
        static_dim=int(stats["static"]["mean"].shape[0]),
        width=int(cfg["width"]),
        layers=int(cfg["layers"]),
        heads=int(cfg["heads"]),
        dropout=float(cfg["dropout"]),
    ).to(device)
    state = torch.load(job_dir / "model.pt", map_location=device)
    model.load_state_dict(state)
    model.eval()
    thresholds = load_json(job_dir / "thresholds.json")
    return model, stats, thresholds


def combine(policy: str, b: np.ndarray, u: np.ndarray, bt: dict[str, float], ut: dict[str, float]) -> np.ndarray:
    if policy == "base":
        return b
    if policy == "unc_raw":
        return u
    if policy == "avg_75base_25unc":
        return (0.75 * b + 0.25 * u).astype(np.float32)
    if policy == "avg_50base_50unc":
        return (0.50 * b + 0.50 * u).astype(np.float32)
    if policy == "max_base_unc":
        return np.maximum(b, u).astype(np.float32)
    if policy == "soft_veto_base_times_unc":
        return (b * (0.25 + 0.75 * u)).astype(np.float32)
    if policy == "mild_veto_unc_q95_or_base_q99":
        keep = (u >= float(ut["q95"])) | (b >= float(bt["q99"]))
        return np.where(keep, b, 0.5 * b).astype(np.float32)
    if policy == "hard_veto_unc_q95_or_base_q99":
        keep = (u >= float(ut["q95"])) | (b >= float(bt["q99"]))
        return np.where(keep, b, 0.0).astype(np.float32)
    raise ValueError(policy)


def summarize_result(split: str, policy: str, thresholds: dict[str, float], metrics_by_bucket: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        "split": split,
        "policy": policy,
        "seen_success_fa": metrics_by_bucket["success_test_seen"].get("success_false_alarm_rate"),
        "seen_failure_detection": metrics_by_bucket["failure_test_seen"].get("failure_detection_rate"),
        "seen_failure_det_at_25": metrics_by_bucket["failure_test_seen"].get("det_at_25"),
        "seen_failure_det_at_50": metrics_by_bucket["failure_test_seen"].get("det_at_50"),
        "ood_success_fa": metrics_by_bucket["success_test_ood"].get("success_false_alarm_rate"),
        "ood_failure_detection": metrics_by_bucket["failure_eval_ood"].get("failure_detection_rate"),
        "ood_failure_det_at_25": metrics_by_bucket["failure_eval_ood"].get("det_at_25"),
        "ood_failure_det_at_50": metrics_by_bucket["failure_eval_ood"].get("det_at_50"),
        "q95": thresholds["q95"],
        "q99": thresholds["q99"],
        "conformal_mass": thresholds["conformal_mass"],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--trained-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_transformer_exploration_v2_20260601")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_fusion_policy_v1_20260601")
    p.add_argument("--splits", nargs="+", default=["all_tasks_random", "ood_suite_libero90", "ood_task_holdout"])
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--alpha", type=float, default=0.15)
    p.add_argument("--min-conformal-mass", type=float, default=0.15)
    args = p.parse_args()

    trained_dir = Path(args.trained_dir)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cfg = load_json(trained_dir / "run_config.json")
    episodes = v2.load_episode_meta(Path(args.run_root))
    all_results: list[dict[str, Any]] = []

    for split in args.splits:
        print(f"=== FUSION SPLIT {split} ===", flush=True)
        buckets = {k: set(v) for k, v in load_json(trained_dir / split / "episode_buckets.json").items()}
        rows_by_bucket = v2.build_rows_for_split(Path(args.run_root), episodes, buckets, int(cfg["history_steps"]))
        base_model, base_stats, base_thresholds = load_model(trained_dir / split / "base", "base", cfg, device)
        unc_model, unc_stats, unc_thresholds = load_model(trained_dir / split / "unc_raw", "unc_raw", cfg, device)

        base_scores: dict[str, np.ndarray] = {}
        unc_scores: dict[str, np.ndarray] = {}
        ids_by_bucket: dict[str, list[str]] = {}
        ts_by_bucket: dict[str, np.ndarray] = {}
        for bucket, rows in rows_by_bucket.items():
            bs, _labels, ids, ts = v2.score_rows(base_model, base_stats, rows, "base", args.batch_size, device)
            us, _labels2, ids2, ts2 = v2.score_rows(unc_model, unc_stats, rows, "unc_raw", args.batch_size, device)
            if ids != ids2 or not np.array_equal(ts, ts2):
                raise RuntimeError(f"score alignment mismatch for split={split} bucket={bucket}")
            base_scores[bucket] = bs
            unc_scores[bucket] = us
            ids_by_bucket[bucket] = ids
            ts_by_bucket[bucket] = ts

        for policy in POLICIES:
            combo_scores = {
                bucket: combine(policy, base_scores[bucket], unc_scores[bucket], base_thresholds, unc_thresholds)
                for bucket in rows_by_bucket
            }
            thresholds = v2.calibrate_thresholds(combo_scores, ids_by_bucket, args.alpha, args.min_conformal_mass)
            metrics_by_bucket = {
                bucket: v2.evaluate_bucket(bucket, rows_by_bucket[bucket], combo_scores[bucket], ids_by_bucket[bucket], ts_by_bucket[bucket], episodes, thresholds)
                for bucket in rows_by_bucket
            }
            result = summarize_result(split, policy, thresholds, metrics_by_bucket)
            all_results.append(result)
            print(json.dumps(result, sort_keys=True), flush=True)

    fields = [
        "split",
        "policy",
        "seen_success_fa",
        "seen_failure_detection",
        "seen_failure_det_at_25",
        "seen_failure_det_at_50",
        "ood_success_fa",
        "ood_failure_detection",
        "ood_failure_det_at_25",
        "ood_failure_det_at_50",
        "q95",
        "q99",
        "conformal_mass",
    ]
    csv_path = out_dir / "dean_uncertainty_fusion_policy_results.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_results)
    (out_dir / "run_config.json").write_text(json.dumps(vars(args) | {"device": str(device)}, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {csv_path}", flush=True)


if __name__ == "__main__":
    main()
