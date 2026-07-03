#!/usr/bin/env python3
"""Analyze fold00 ACE sampling ablation jobs with the current mass policy."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


EVAL_SPLITS = ["success_test_seen", "success_test_ood", "failure_eval_ood"]
LOAD_SPLITS = ["success_calib_seen", "success_val_seen", *EVAL_SPLITS]


def quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    idx = int(math.ceil(q * len(xs))) - 1
    return xs[max(0, min(idx, len(xs) - 1))]


def conformal_upper_threshold(values: list[float], alpha: float) -> float:
    if not values:
        return float("inf")
    xs = sorted(values)
    rank = int(math.ceil((len(xs) + 1) * (1.0 - alpha)))
    if rank > len(xs):
        return float("inf")
    return xs[max(0, rank - 1)]


def load_score_traces(job_dir: Path) -> dict[str, dict[str, list[tuple[int, float]]]]:
    scores_path = job_dir / "scores.jsonl"
    if not scores_path.exists():
        raise FileNotFoundError(scores_path)
    traces: dict[str, dict[str, list[tuple[int, float]]]] = defaultdict(lambda: defaultdict(list))
    with scores_path.open() as f:
        for line in f:
            row = json.loads(line)
            split = row.get("split")
            if split not in LOAD_SPLITS:
                continue
            score = row.get("score")
            if score is None:
                score = row.get("score_eventual")
            traces[split][str(row["episode_key"])].append((int(row["timestep"]), float(score)))
    for split_map in traces.values():
        for episode_key in list(split_map):
            split_map[episode_key].sort(key=lambda item: item[0])
    return traces


def scores_only(values: list[tuple[int, float]]) -> list[float]:
    return [score for _, score in values]


def total_mass(scores: list[float], row_threshold: float) -> float:
    return sum(max(0.0, score - row_threshold) for score in scores)


def trigger_mass(scores: list[float], row_threshold: float, mass_threshold: float) -> int | None:
    mass = 0.0
    for idx, score in enumerate(scores):
        mass += max(0.0, score - row_threshold)
        if mass >= mass_threshold:
            return idx
    return None


def evaluate_job(job_dir: Path, alpha: float) -> dict[str, Any]:
    traces = load_score_traces(job_dir)
    calib_scores = [
        score
        for values in traces.get("success_calib_seen", {}).values()
        for score in scores_only(values)
    ]
    q95 = quantile(calib_scores, 0.95)
    val_masses = [
        total_mass(scores_only(values), q95)
        for values in traces.get("success_val_seen", {}).values()
    ]
    mass_threshold = conformal_upper_threshold(val_masses, alpha)

    out: dict[str, Any] = {"q95": q95, "mass_threshold": mass_threshold}
    for split in EVAL_SPLITS:
        split_traces = traces.get(split, {})
        fired: list[tuple[int, int]] = []
        for values in split_traces.values():
            scores = scores_only(values)
            step = trigger_mass(scores, q95, mass_threshold)
            if step is not None:
                fired.append((step, len(scores)))
        n = len(split_traces)
        rate = len(fired) / n if n else 0.0
        out[f"{split}_episodes"] = n
        out[f"{split}_alarm_rate"] = rate
        if split == "failure_eval_ood":
            out["failure_det_rate"] = rate
            out["failure_never_rate"] = 1.0 - rate
            out["failure_det_at_10"] = sum(1 for step, length in fired if step / max(1, length) <= 0.10) / n if n else 0.0
            out["failure_det_at_25"] = sum(1 for step, length in fired if step / max(1, length) <= 0.25) / n if n else 0.0
            out["failure_det_at_50"] = sum(1 for step, length in fired if step / max(1, length) <= 0.50) / n if n else 0.0
            out["failure_mean_time_detected_only"] = (
                sum(step / max(1, length) for step, length in fired) / len(fired) if fired else 1.0
            )
    return out


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, default=Path("."))
    parser.add_argument("--experiment-dir", type=Path, required=True)
    parser.add_argument("--alpha", type=float, default=0.15)
    parser.add_argument("--output-report", type=Path, default=Path("reports/FIPER_ACE_SAMPLING_ABLATION_FOLD00_V1_REPORT.md"))
    parser.add_argument("--output-csv", type=Path, default=Path("reports/FIPER_ACE_SAMPLING_ABLATION_FOLD00_V1_RESULTS.csv"))
    args = parser.parse_args()

    base_dir = args.base_dir.resolve()
    exp_dir = base_dir / args.experiment_dir
    jobs: list[tuple[str, Path, str]] = [
        (
            "existing_real_v2_018",
            base_dir
            / "experiments/clean_temporal_nextgen_v2_full_all_20260527"
            / "fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16",
            "reference",
        )
    ]
    for job_dir in sorted((exp_dir / "jobs").iterdir()):
        if job_dir.is_dir():
            jobs.append((job_dir.name, job_dir, "ablation"))

    rows: list[dict[str, Any]] = []
    for name, job_dir, group in jobs:
        metrics = evaluate_job(job_dir, args.alpha)
        summary = load_json(job_dir / "summary.json")
        history = load_json(job_dir / "training_history.json")
        config = load_json(job_dir / "config.json")
        if isinstance(history, list) and history:
            epochs_run = len(history)
        else:
            epochs_run = None
        row = {
            "name": name,
            "group": group,
            "job_dir": str(job_dir.relative_to(base_dir)),
            "best_epoch": summary.get("best_epoch"),
            "epochs_run": epochs_run,
            "ace_candidate_limit": config.get("ace_candidate_limit", 8),
            "ace_temporal_stride": config.get("ace_temporal_stride", 1),
            **metrics,
        }
        rows.append(row)

    args.output_csv = base_dir / args.output_csv
    args.output_report = base_dir / args.output_report
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", newline="") as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# FIPER ACE Sampling Ablation Fold00 Report",
        "",
        "Policy: current score-only q95 row threshold from success_calib_seen plus conformal episode risk-mass threshold from success_val_seen, alpha=0.15.",
        "",
        "| Job | ACE Candidates | ACE Stride | Seen FA | OOD FA | OOD Failure Det | Det@25 | Det@50 | Mean Time | Never | Best Epoch |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['name']}` | {row['ace_candidate_limit']} | {row['ace_temporal_stride']} | "
            f"{pct(row['success_test_seen_alarm_rate'])} | {pct(row['success_test_ood_alarm_rate'])} | "
            f"{pct(row['failure_det_rate'])} | {pct(row['failure_det_at_25'])} | {pct(row['failure_det_at_50'])} | "
            f"{row['failure_mean_time_detected_only']:.3f} | {pct(row['failure_never_rate'])} | {row.get('best_epoch')} |"
        )

    best = min(
        [row for row in rows if row["group"] == "ablation"],
        key=lambda row: (
            row["success_test_ood_alarm_rate"],
            -row["failure_det_rate"],
            -row["failure_det_at_50"],
            -row["failure_det_at_25"],
        ),
    )
    lines += [
        "",
        "## Decision",
        "",
        f"Lowest OOD false-alarm ablation: `{best['name']}`.",
        "",
        "Final fields:",
        "",
        "```text",
        f"BEST_ABLATION_BY_OOD_FA = {best['name']}",
        f"BEST_ABLATION_OOD_FA = {best['success_test_ood_alarm_rate']:.6f}",
        f"BEST_ABLATION_FAILURE_DET = {best['failure_det_rate']:.6f}",
        f"BEST_ABLATION_DET_AT_25 = {best['failure_det_at_25']:.6f}",
        f"BEST_ABLATION_DET_AT_50 = {best['failure_det_at_50']:.6f}",
        "```",
        "",
    ]
    args.output_report.write_text("\n".join(lines))
    print(args.output_report)
    print(args.output_csv)


if __name__ == "__main__":
    main()
