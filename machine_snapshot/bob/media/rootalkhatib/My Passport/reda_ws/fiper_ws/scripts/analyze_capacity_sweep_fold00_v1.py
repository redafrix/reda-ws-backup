#!/usr/bin/env python3
"""Analyze fold_00 transformer capacity/history sweeps.

Reads completed score traces and evaluates every job with the same deployable
policy: score q95 row threshold from success_calib_seen plus split-conformal
episode risk-mass threshold from success_val_seen.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


BASELINE_JOB = (
    "existing_real_v2_018",
    Path(
        "experiments/clean_temporal_nextgen_v2_full_all_20260527/"
        "fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16"
    ),
)

BIG_ROOT = Path("experiments/transformer_capacity_history_sweep_fold00_v1_20260528/jobs")
SMALL_ROOT = Path("experiments/transformer_capacity_history_small_sweep_fold00_v1_20260528/jobs")
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
    rank_1indexed = int(math.ceil((len(xs) + 1) * (1.0 - alpha)))
    if rank_1indexed > len(xs):
        return float("inf")
    return xs[max(0, rank_1indexed - 1)]


def load_score_traces(job_dir: Path) -> dict[str, dict[str, list[tuple[int, float]]]]:
    traces: dict[str, dict[str, list[tuple[int, float]]]] = defaultdict(lambda: defaultdict(list))
    scores_path = job_dir / "scores.jsonl"
    if not scores_path.exists():
        raise FileNotFoundError(scores_path)
    with scores_path.open() as f:
        for line in f:
            row = json.loads(line)
            split = row.get("split")
            if split not in LOAD_SPLITS:
                continue
            traces[split][str(row["episode_key"])].append((int(row["timestep"]), float(row["score"])))
    for split_map in traces.values():
        for episode_key in list(split_map):
            split_map[episode_key].sort(key=lambda item: item[0])
    return traces


def trace_scores(values: list[tuple[int, float]]) -> list[float]:
    return [score for _, score in values]


def total_mass(scores: list[float], threshold: float) -> float:
    return sum(max(0.0, score - threshold) for score in scores)


def trigger_mass(scores: list[float], threshold: float, mass_threshold: float) -> int | None:
    mass = 0.0
    for idx, score in enumerate(scores):
        mass += max(0.0, score - threshold)
        if mass >= mass_threshold:
            return idx
    return None


def evaluate_job(job_dir: Path, alpha: float) -> dict[str, Any]:
    traces = load_score_traces(job_dir)
    calib_scores = [
        score
        for values in traces.get("success_calib_seen", {}).values()
        for score in trace_scores(values)
    ]
    q95 = quantile(calib_scores, 0.95)
    val_masses = [
        total_mass(trace_scores(values), q95)
        for values in traces.get("success_val_seen", {}).values()
    ]
    mass_threshold = conformal_upper_threshold(val_masses, alpha)

    metrics: dict[str, Any] = {
        "q95": q95,
        "mass_threshold": mass_threshold,
    }
    for split in EVAL_SPLITS:
        split_traces = traces.get(split, {})
        fired: list[tuple[int, int]] = []
        for values in split_traces.values():
            scores = trace_scores(values)
            step = trigger_mass(scores, q95, mass_threshold)
            if step is not None:
                fired.append((step, len(scores)))
        n = len(split_traces)
        rate = len(fired) / n if n else 0.0
        metrics[f"{split}_episodes"] = n
        metrics[f"{split}_alarm_rate"] = rate
        if split == "failure_eval_ood":
            metrics["failure_det_rate"] = rate
            metrics["failure_never_rate"] = 1.0 - rate
            metrics["failure_det_at_10"] = (
                sum(1 for step, length in fired if step / max(1, length) <= 0.10) / n if n else 0.0
            )
            metrics["failure_det_at_25"] = (
                sum(1 for step, length in fired if step / max(1, length) <= 0.25) / n if n else 0.0
            )
            metrics["failure_det_at_50"] = (
                sum(1 for step, length in fired if step / max(1, length) <= 0.50) / n if n else 0.0
            )
            metrics["failure_mean_time_detected_only"] = (
                sum(step / max(1, length) for step, length in fired) / len(fired) if fired else 1.0
            )
    return metrics


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def training_summary(job_dir: Path) -> dict[str, Any]:
    history_path = job_dir / "training_history.json"
    summary = load_json(job_dir / "summary.json")
    if not history_path.exists():
        return {
            "best_epoch": summary.get("best_epoch"),
            "epochs_run": None,
            "train_loss_best": None,
            "train_loss_final": None,
            "val_auroc_best": None,
            "degraded_after_best": None,
            "peaked_by_5": None,
            "peaked_by_10": None,
        }
    history = json.loads(history_path.read_text())
    if not history:
        return {}
    scored = []
    for row in history:
        score = row.get("early_stop_score", row.get("val_score", row.get("objective")))
        if score is not None:
            scored.append((float(score), row))
    best_row = max(scored, key=lambda item: item[0])[1] if scored else history[0]
    best_epoch = int(best_row.get("epoch", summary.get("best_epoch", 0)))
    final_row = history[-1]
    final_score = final_row.get("early_stop_score", final_row.get("val_score", final_row.get("objective")))
    best_score = best_row.get("early_stop_score", best_row.get("val_score", best_row.get("objective")))
    return {
        "best_epoch": best_epoch,
        "epochs_run": len(history),
        "train_loss_best": best_row.get("train_loss"),
        "train_loss_final": final_row.get("train_loss"),
        "val_auroc_best": best_row.get("val_auroc", best_row.get("val_auc")),
        "val_score_best": best_score,
        "val_score_final": final_score,
        "degraded_after_best": bool(final_score is not None and best_score is not None and float(final_score) < float(best_score) - 1e-6),
        "peaked_by_5": best_epoch <= 5,
        "peaked_by_10": best_epoch <= 10,
    }


def feature_hygiene(job_dir: Path) -> dict[str, Any]:
    audit = load_json(job_dir / "FEATURE_AUDIT.json")
    bad_flags = []
    for key in [
        "uses_reward",
        "uses_success",
        "uses_object_positions_before",
        "uses_task_metadata_as_input",
        "uses_ood_rows_for_train",
        "uses_future_timestep",
    ]:
        if audit.get(key):
            bad_flags.append(key)
    fields = audit.get("input_fields", [])
    forbidden_field_hits = [
        field
        for field in fields
        if any(token in str(field).lower() for token in ["reward", "success", "object_position", "task_language", "instruction"])
    ]
    return {
        "feature_hygiene_pass": not bad_flags and not forbidden_field_hits,
        "bad_flags": bad_flags,
        "forbidden_field_hits": forbidden_field_hits,
        "input_fields": fields,
    }


def balanced_score(row: dict[str, Any]) -> float:
    return (
        2.0 * row["failure_det_at_25"]
        + 1.5 * row["failure_det_at_50"]
        + row["failure_det_rate"]
        - 1.5 * row["success_test_ood_alarm_rate"]
        - 0.5 * row["success_test_seen_alarm_rate"]
        - row["failure_never_rate"]
    )


def pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, default=Path("."))
    parser.add_argument("--alpha", type=float, default=0.15)
    parser.add_argument("--output-report", type=Path, default=Path("reports/TRANSFORMER_CAPACITY_HISTORY_BIG_SMALL_SWEEP_FOLD00_V1_REPORT.md"))
    parser.add_argument("--output-csv", type=Path, default=Path("reports/TRANSFORMER_CAPACITY_HISTORY_BIG_SMALL_SWEEP_FOLD00_V1_RESULTS.csv"))
    args = parser.parse_args()

    base_dir = args.base_dir.resolve()
    jobs: list[tuple[str, Path, str]] = [(BASELINE_JOB[0], base_dir / BASELINE_JOB[1], "existing")]
    for root, group in [(BIG_ROOT, "big"), (SMALL_ROOT, "small")]:
        root_path = base_dir / root
        for job_dir in sorted(root_path.iterdir()):
            if job_dir.is_dir():
                jobs.append((job_dir.name, job_dir, group))

    rows: list[dict[str, Any]] = []
    for name, job_dir, group in jobs:
        metrics = evaluate_job(job_dir, args.alpha)
        train = training_summary(job_dir)
        hygiene = feature_hygiene(job_dir)
        config = load_json(job_dir / "config.json")
        row = {
            "name": name,
            "group": group,
            "job_dir": str(job_dir.relative_to(base_dir)),
            "width": config.get("width"),
            "layers": config.get("layers"),
            "heads": config.get("heads"),
            "history_steps": config.get("history_steps"),
            "dropout": config.get("dropout", 0.1),
            **train,
            **metrics,
            **hygiene,
        }
        row["balanced_score"] = balanced_score(row)
        rows.append(row)

    baseline = next(row for row in rows if row["name"] == "existing_real_v2_018")
    for row in rows:
        row["beats_ood_fa"] = row["success_test_ood_alarm_rate"] < baseline["success_test_ood_alarm_rate"]
        row["keeps_det_within_5pct"] = row["failure_det_rate"] >= baseline["failure_det_rate"] - 0.05
        row["keeps_det50_within_5pct"] = row["failure_det_at_50"] >= baseline["failure_det_at_50"] - 0.05
        row["improves_det25"] = row["failure_det_at_25"] > baseline["failure_det_at_25"]
        row["scale_candidate"] = (
            row["name"] != baseline["name"]
            and row["beats_ood_fa"]
            and row["keeps_det_within_5pct"]
            and row["keeps_det50_within_5pct"]
        )

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "name",
        "group",
        "width",
        "layers",
        "heads",
        "history_steps",
        "dropout",
        "best_epoch",
        "epochs_run",
        "train_loss_best",
        "train_loss_final",
        "val_auroc_best",
        "val_score_best",
        "val_score_final",
        "degraded_after_best",
        "peaked_by_5",
        "peaked_by_10",
        "q95",
        "mass_threshold",
        "success_test_seen_episodes",
        "success_test_seen_alarm_rate",
        "success_test_ood_episodes",
        "success_test_ood_alarm_rate",
        "failure_eval_ood_episodes",
        "failure_det_rate",
        "failure_det_at_10",
        "failure_det_at_25",
        "failure_det_at_50",
        "failure_mean_time_detected_only",
        "failure_never_rate",
        "balanced_score",
        "feature_hygiene_pass",
        "beats_ood_fa",
        "keeps_det_within_5pct",
        "keeps_det50_within_5pct",
        "improves_det25",
        "scale_candidate",
        "job_dir",
    ]
    with args.output_csv.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    sorted_by_balanced = sorted(rows, key=lambda row: row["balanced_score"], reverse=True)
    preserving = [
        row for row in rows
        if row["name"] != baseline["name"]
        and row["keeps_det_within_5pct"]
        and row["keeps_det50_within_5pct"]
    ]
    sorted_by_low_fa = sorted(preserving, key=lambda row: (row["success_test_ood_alarm_rate"], -row["failure_det_at_25"]))
    scale_candidates = [row for row in sorted_by_low_fa if row["scale_candidate"]]
    best_scale = scale_candidates[0] if scale_candidates else None

    def table(rows_for_table: list[dict[str, Any]]) -> list[str]:
        lines = [
            "| Job | Group | W/L/H/k | Best Ep | Seen FA | OOD FA | Det | Det@25 | Det@50 | Mean | Hygiene |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for row in rows_for_table:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["name"]),
                        str(row["group"]),
                        f"{row.get('width')}/{row.get('layers')}/{row.get('heads')}/{row.get('history_steps')}",
                        str(row.get("best_epoch")),
                        pct(row["success_test_seen_alarm_rate"]),
                        pct(row["success_test_ood_alarm_rate"]),
                        pct(row["failure_det_rate"]),
                        pct(row["failure_det_at_25"]),
                        pct(row["failure_det_at_50"]),
                        f"{row['failure_mean_time_detected_only']:.3f}",
                        "YES" if row["feature_hygiene_pass"] else "NO",
                    ]
                )
                + " |"
            )
        return lines

    big_complete = all((base_dir / BIG_ROOT / name / "summary.json").exists() for name in [
        "cap_00_current_reproduce", "cap_01_medium_k16", "cap_02_large_k16",
        "cap_03_medium_k32", "cap_04_large_k32", "cap_05_wide_lowdrop_k16",
    ])
    small_complete = all((base_dir / SMALL_ROOT / name / "summary.json").exists() for name in [
        "cap_06_tiny_k16", "cap_07_small_k16", "cap_08_shallow_k16",
        "cap_09_tiny_k32", "cap_10_small_k32", "cap_11_shallow_k32",
    ])
    hygiene_pass = all(row["feature_hygiene_pass"] for row in rows)
    early_pattern = sum(1 for row in rows if row.get("peaked_by_5")) >= int(0.5 * len(rows))

    report_lines = [
        "# Transformer Capacity/History Big+Small Sweep Fold00",
        "",
        "## Baseline",
        "",
        *table([baseline]),
        "",
        "## All Jobs By Balanced Score",
        "",
        *table(sorted_by_balanced),
        "",
        "## Lowest OOD FA While Preserving Det/Det@50",
        "",
        *table(sorted_by_low_fa),
        "",
        "## Verdict",
        "",
        f"- `BIG_SWEEP_COMPLETE` = **{'YES' if big_complete else 'NO'}**",
        f"- `SMALL_SWEEP_COMPLETE` = **{'YES' if small_complete else 'NO'}**",
        f"- `FEATURE_HYGIENE_PASS` = **{'YES' if hygiene_pass else 'NO'}**",
        f"- `OLD_EARLY_OVERFITTING_PATTERN_CONFIRMED` = **{'YES' if early_pattern else 'NO'}**",
        f"- `ANY_SMALL_MODEL_BEATS_REAL_V2_018` = **{'YES' if any(row['group']=='small' and row['scale_candidate'] for row in rows) else 'NO'}**",
        f"- `ANY_BIG_MODEL_BEATS_REAL_V2_018` = **{'YES' if any(row['group']=='big' and row['scale_candidate'] for row in rows) else 'NO'}**",
        f"- `BEST_MODEL_TO_SCALE_ALL_FOLDS` = **{best_scale['name'] if best_scale else 'NONE'}**",
        f"- `SHOULD_SCALE_TO_ALL_FOLDS` = **{'YES' if best_scale else 'NO'}**",
        "",
        "## Notes",
        "",
        "- Policy used for every row: score q95 mass-conformal alpha=0.15.",
        "- The two sweep folders contain `failed_jobs.jsonl` BrokenPipeError entries, but every expected job has summary and score artifacts and was included here.",
        f"- CSV: `{args.output_csv}`",
    ]
    args.output_report.write_text("\n".join(report_lines) + "\n")
    print(f"Wrote {args.output_report}")


if __name__ == "__main__":
    main()
