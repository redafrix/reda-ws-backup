#!/usr/bin/env python3
"""Policy-only sweep for the v2_018_transformer_k16 score traces.

This script does not retrain a model. It reads per-timestep score traces from
completed nextgen jobs and evaluates online alarm rules that only depend on
current/past scores and thresholds calibrated from success validation episodes.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


OBJECT_FOLDS = [
    "fold_00_holdout_alphabet_soup_bbq_sauce",
    "fold_01_holdout_butter_chocolate_pudding",
    "fold_02_holdout_cream_cheese_ketchup",
    "fold_03_holdout_milk_orange_juice",
    "fold_04_holdout_salad_dressing_tomato_sauce",
]


@dataclass
class EpisodeTrace:
    split: str
    fold: str
    episode_key: str
    scores: list[float]
    q90: float
    q95: float
    q99: float


def quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    idx = int(math.ceil(q * len(xs))) - 1
    return xs[max(0, min(idx, len(xs) - 1))]


def conformal_upper_threshold(values: list[float], alpha: float) -> float:
    """Split-conformal upper threshold for one-sided nonconformity scores.

    The finite-sample index is ceil((n + 1) * (1 - alpha)). If that index is
    larger than n, the conformal threshold is infinite, meaning the requested
    false-alarm level is not attainable with the calibration set size.
    """

    if not values:
        return float("inf")
    xs = sorted(values)
    rank_1indexed = int(math.ceil((len(xs) + 1) * (1.0 - alpha)))
    if rank_1indexed > len(xs):
        return float("inf")
    return xs[max(0, rank_1indexed - 1)]


def trigger_consecutive(scores: list[float], threshold: float, k: int) -> int | None:
    run = 0
    for idx, score in enumerate(scores):
        if score > threshold:
            run += 1
        else:
            run = 0
        if run >= k:
            return idx
    return None


def trigger_count(scores: list[float], threshold: float, count_threshold: int) -> int | None:
    count = 0
    for idx, score in enumerate(scores):
        if score > threshold:
            count += 1
        if count >= count_threshold:
            return idx
    return None


def trigger_mass(scores: list[float], threshold: float, mass_threshold: float) -> int | None:
    mass = 0.0
    for idx, score in enumerate(scores):
        mass += max(0.0, score - threshold)
        if mass >= mass_threshold:
            return idx
    return None


def trigger_count_reset(
    scores: list[float],
    high_threshold: float,
    low_threshold: float,
    count_threshold: int,
    reset_steps: int,
) -> int | None:
    count = 0
    low_run = 0
    for idx, score in enumerate(scores):
        if score > high_threshold:
            count += 1
            low_run = 0
        elif score < low_threshold:
            low_run += 1
            if low_run >= reset_steps:
                count = 0
        else:
            low_run = 0
        if count >= count_threshold:
            return idx
    return None


def trigger_mass_reset(
    scores: list[float],
    high_threshold: float,
    low_threshold: float,
    mass_threshold: float,
    reset_steps: int,
) -> int | None:
    mass = 0.0
    low_run = 0
    for idx, score in enumerate(scores):
        if score > high_threshold:
            mass += score - high_threshold
            low_run = 0
        elif score < low_threshold:
            low_run += 1
            if low_run >= reset_steps:
                mass = 0.0
        else:
            low_run = 0
        if mass >= mass_threshold:
            return idx
    return None


def max_run_above(scores: list[float], threshold: float) -> int:
    best = 0
    run = 0
    for score in scores:
        if score > threshold:
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


def total_count_above(scores: list[float], threshold: float) -> int:
    return sum(1 for score in scores if score > threshold)


def total_mass_above(scores: list[float], threshold: float) -> float:
    return sum(max(0.0, score - threshold) for score in scores)


def load_traces(root: Path, folds: list[str], job: str) -> list[EpisodeTrace]:
    traces: list[EpisodeTrace] = []
    for fold in folds:
        job_dir = root / fold / "jobs" / job
        scores_path = job_dir / "scores.jsonl"
        thresholds_path = job_dir / "thresholds.json"
        if not scores_path.exists():
            raise FileNotFoundError(scores_path)
        thresholds = json.loads(thresholds_path.read_text())["score"]["eventual"]
        grouped: dict[tuple[str, str], list[tuple[int, float]]] = defaultdict(list)
        with scores_path.open() as f:
            for line in f:
                row = json.loads(line)
                split = row.get("split")
                if split not in {
                    "success_val_seen",
                    "success_test_seen",
                    "success_test_ood",
                    "failure_eval_ood",
                }:
                    continue
                grouped[(split, row["episode_key"])].append(
                    (int(row["timestep"]), float(row["score"]))
                )
        for (split, episode_key), values in grouped.items():
            values.sort()
            traces.append(
                EpisodeTrace(
                    split=split,
                    fold=fold,
                    episode_key=episode_key,
                    scores=[score for _, score in values],
                    q90=float(thresholds["q90"]),
                    q95=float(thresholds["q95"]),
                    q99=float(thresholds["q99"]),
                )
            )
    return traces


def evaluate_policy(
    traces: list[EpisodeTrace],
    trigger_fn: Callable[[EpisodeTrace], int | None],
) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for split in ["success_test_seen", "success_test_ood", "failure_eval_ood"]:
        split_traces = [trace for trace in traces if trace.split == split]
        fired: list[tuple[int, int]] = []
        for trace in split_traces:
            step = trigger_fn(trace)
            if step is not None:
                fired.append((step, len(trace.scores)))
        episodes = len(split_traces)
        alarm_rate = len(fired) / episodes if episodes else 0.0
        det10 = sum(1 for step, n in fired if step / n <= 0.10) / episodes if episodes else 0.0
        det25 = sum(1 for step, n in fired if step / n <= 0.25) / episodes if episodes else 0.0
        det50 = sum(1 for step, n in fired if step / n <= 0.50) / episodes if episodes else 0.0
        mean_time = (
            sum(step / n for step, n in fired) / len(fired)
            if fired
            else None
        )
        out[split] = {
            "episodes": episodes,
            "alarm_rate": alarm_rate,
            "det_at_10": det10,
            "det_at_25": det25,
            "det_at_50": det50,
            "mean_time_detected": mean_time,
            "never_rate": 1.0 - alarm_rate,
        }
    return out


def build_policies(traces: list[EpisodeTrace]) -> tuple[list[dict], dict[str, float]]:
    val = [trace for trace in traces if trace.split == "success_val_seen"]
    if not val:
        raise RuntimeError("No success_val_seen episodes found for policy calibration.")

    # Episode-level thresholds calibrated only from success validation traces.
    calibration: dict[str, float] = {}
    for q_name, threshold_getter in {
        "q95": lambda t: t.q95,
        "q99": lambda t: t.q99,
    }.items():
        calibration[f"{q_name}_count_epq90"] = quantile(
            [total_count_above(t.scores, threshold_getter(t)) for t in val], 0.90
        )
        calibration[f"{q_name}_count_epq95"] = quantile(
            [total_count_above(t.scores, threshold_getter(t)) for t in val], 0.95
        )
        calibration[f"{q_name}_mass_epq90"] = quantile(
            [total_mass_above(t.scores, threshold_getter(t)) for t in val], 0.90
        )
        calibration[f"{q_name}_mass_epq95"] = quantile(
            [total_mass_above(t.scores, threshold_getter(t)) for t in val], 0.95
        )
        calibration[f"{q_name}_maxrun_epq90"] = quantile(
            [max_run_above(t.scores, threshold_getter(t)) for t in val], 0.90
        )
        calibration[f"{q_name}_maxrun_epq95"] = quantile(
            [max_run_above(t.scores, threshold_getter(t)) for t in val], 0.95
        )
        for alpha in [0.20, 0.15, 0.10, 0.05]:
            suffix = str(alpha).replace(".", "p")
            calibration[f"{q_name}_count_conformal_alpha{suffix}"] = conformal_upper_threshold(
                [total_count_above(t.scores, threshold_getter(t)) for t in val],
                alpha,
            )
            calibration[f"{q_name}_mass_conformal_alpha{suffix}"] = conformal_upper_threshold(
                [total_mass_above(t.scores, threshold_getter(t)) for t in val],
                alpha,
            )
            calibration[f"{q_name}_maxrun_conformal_alpha{suffix}"] = conformal_upper_threshold(
                [max_run_above(t.scores, threshold_getter(t)) for t in val],
                alpha,
            )

    policies: list[dict] = []

    def add(name: str, trigger: Callable[[EpisodeTrace], int | None], family: str) -> None:
        policies.append({"name": name, "family": family, "trigger": trigger})

    for q_name, threshold_getter in {
        "q95": lambda t: t.q95,
        "q99": lambda t: t.q99,
    }.items():
        for k in [1, 2, 3, 5, 10, 15, 20, 30]:
            add(
                f"{q_name}_consec_K{k}",
                lambda t, getter=threshold_getter, k=k: trigger_consecutive(
                    t.scores, getter(t), k
                ),
                "baseline_consecutive",
            )
        for count in [5, 10, 15, 20, 30, 40, 60, 80]:
            add(
                f"{q_name}_count_{count}",
                lambda t, getter=threshold_getter, count=count: trigger_count(
                    t.scores, getter(t), count
                ),
                "manual_count",
            )
        for mass in [1, 2, 3, 5, 8, 10, 15, 20, 30, 40]:
            add(
                f"{q_name}_mass_{mass}",
                lambda t, getter=threshold_getter, mass=mass: trigger_mass(
                    t.scores, getter(t), mass
                ),
                "manual_mass",
            )

    for key, value in sorted(calibration.items()):
        q_name = key.split("_")[0]
        if not math.isfinite(value):
            continue
        if "_count_" in key:
            count_threshold = max(1, int(math.ceil(value)))
            add(
                key,
                lambda t, q_name=q_name, count_threshold=count_threshold: trigger_count(
                    t.scores, getattr(t, q_name), count_threshold
                ),
                (
                    "episode_calibrated_count"
                    if "conformal" not in key
                    else "split_conformal_count"
                ),
            )
        elif "_mass_" in key:
            mass_threshold = max(1e-9, float(value))
            add(
                key,
                lambda t, q_name=q_name, mass_threshold=mass_threshold: trigger_mass(
                    t.scores, getattr(t, q_name), mass_threshold
                ),
                "episode_calibrated_mass"
                if "conformal" not in key
                else "split_conformal_mass",
            )
        elif "_maxrun_" in key:
            run_threshold = max(1, int(math.ceil(value)))
            add(
                key,
                lambda t, q_name=q_name, run_threshold=run_threshold: trigger_consecutive(
                    t.scores, getattr(t, q_name), run_threshold
                ),
                "episode_calibrated_maxrun"
                if "conformal" not in key
                else "split_conformal_maxrun",
            )

    for reset in [3, 5, 10]:
        for count in [5, 10, 15, 20, 30]:
            add(
                f"q95_count_{count}_reset_q90_R{reset}",
                lambda t, count=count, reset=reset: trigger_count_reset(
                    t.scores, t.q95, t.q90, count, reset
                ),
                "recovery_reset_count",
            )
        for mass in [1, 2, 3, 5, 8, 10, 15]:
            add(
                f"q95_mass_{mass}_reset_q90_R{reset}",
                lambda t, mass=mass, reset=reset: trigger_mass_reset(
                    t.scores, t.q95, t.q90, mass, reset
                ),
                "recovery_reset_mass",
            )

    for count in [10, 20, 30, 40, 60]:
        add(
            f"q99K1_or_q95_count_{count}",
            lambda t, count=count: min(
                [
                    step
                    for step in [
                        trigger_consecutive(t.scores, t.q99, 1),
                        trigger_count(t.scores, t.q95, count),
                    ]
                    if step is not None
                ],
                default=None,
            ),
            "two_stage",
        )
    for mass in [2, 5, 10, 20, 30]:
        add(
            f"q99K1_or_q95_mass_{mass}",
            lambda t, mass=mass: min(
                [
                    step
                    for step in [
                        trigger_consecutive(t.scores, t.q99, 1),
                        trigger_mass(t.scores, t.q95, mass),
                    ]
                    if step is not None
                ],
                default=None,
            ),
            "two_stage",
        )

    return policies, calibration


def objective(row: dict[str, float]) -> float:
    return (
        2.0 * row["failure_detection"]
        + 1.5 * row["failure_det_at_50"]
        + 1.25 * row["failure_det_at_25"]
        - 2.0 * row["success_ood_fa"]
        - 0.25 * (row["failure_mean_time"] if row["failure_mean_time"] is not None else 1.0)
    )


def write_report(rows: list[dict], calibration: dict[str, float], out_dir: Path) -> None:
    def pct(value: float | None) -> str:
        if value is None:
            return "NA"
        return f"{100 * value:.1f}%"

    def num(value: float | None) -> str:
        if value is None:
            return "NA"
        return f"{value:.3f}"

    rows_by_obj = sorted(rows, key=lambda row: row["objective"], reverse=True)
    low_fa = {
        limit: sorted(
            [row for row in rows if row["success_ood_fa"] <= limit],
            key=lambda row: (
                row["failure_detection"],
                row["failure_det_at_50"],
                row["failure_det_at_25"],
                -row["success_ood_fa"],
            ),
            reverse=True,
        )[:10]
        for limit in [0.20, 0.30, 0.35, 0.40, 0.45]
    }
    lines = [
        "# Transformer K16 Online Policy Sweep",
        "",
        "Model: `v2_018_transformer_k16`.",
        "",
        "This is a policy-only analysis over existing score traces. No model was retrained.",
        "All new episode-level thresholds are calibrated only from `success_val_seen` episodes.",
        "",
        "## Calibration Values",
        "",
        "```json",
        json.dumps(calibration, indent=2, sort_keys=True),
        "```",
        "",
        "## Top Policies By Objective",
        "",
        "| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(rows_by_obj[:25], 1):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(idx),
                    f"`{row['policy']}`",
                    row["family"],
                    pct(row["success_ood_fa"]),
                    pct(row["success_seen_fa"]),
                    pct(row["failure_detection"]),
                    pct(row["failure_det_at_25"]),
                    pct(row["failure_det_at_50"]),
                    num(row["failure_mean_time"]),
                    pct(row["failure_never"]),
                ]
            )
            + " |"
        )
    for limit, subset in low_fa.items():
        lines.extend(
            [
                "",
                f"## Best Policies With OOD Success FA <= {pct(limit)}",
                "",
                "| Rank | Policy | Family | OOD FA | Seen FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |",
                "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for idx, row in enumerate(subset, 1):
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(idx),
                        f"`{row['policy']}`",
                        row["family"],
                        pct(row["success_ood_fa"]),
                        pct(row["success_seen_fa"]),
                        pct(row["failure_detection"]),
                        pct(row["failure_det_at_25"]),
                        pct(row["failure_det_at_50"]),
                        num(row["failure_mean_time"]),
                        pct(row["failure_never"]),
                    ]
                )
                + " |"
            )
    lines.extend(
        [
            "",
            "## Decision Notes",
            "",
            "- `q95_consec_K3` is the original score-only reference.",
            "- Count/mass policies are online accumulators over past score evidence.",
            "- Recovery-reset policies reset accumulated evidence after sustained recovery below q90.",
            "- Episode-calibrated policies use success validation episodes to target episode-level behavior instead of row-level behavior.",
        ]
    )
    (out_dir / "TRANSFORMER_K16_ONLINE_POLICY_SWEEP_REPORT.md").write_text(
        "\n".join(lines) + "\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="experiments/clean_temporal_nextgen_v2_full_all_20260527",
    )
    parser.add_argument("--job", default="v2_018_transformer_k16")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--folds", nargs="*", default=OBJECT_FOLDS)
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    traces = load_traces(Path(args.root), args.folds, args.job)
    policies, calibration = build_policies(traces)

    rows: list[dict] = []
    for policy in policies:
        metrics = evaluate_policy(traces, policy["trigger"])
        success_seen = metrics["success_test_seen"]
        success_ood = metrics["success_test_ood"]
        failure = metrics["failure_eval_ood"]
        row = {
            "policy": policy["name"],
            "family": policy["family"],
            "success_seen_episodes": success_seen["episodes"],
            "success_ood_episodes": success_ood["episodes"],
            "failure_ood_episodes": failure["episodes"],
            "success_seen_fa": success_seen["alarm_rate"],
            "success_ood_fa": success_ood["alarm_rate"],
            "failure_detection": failure["alarm_rate"],
            "failure_det_at_10": failure["det_at_10"],
            "failure_det_at_25": failure["det_at_25"],
            "failure_det_at_50": failure["det_at_50"],
            "failure_mean_time": failure["mean_time_detected"],
            "failure_never": failure["never_rate"],
        }
        row["objective"] = objective(row)
        rows.append(row)

    with (out_dir / "policy_sweep_results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / "policy_sweep_results.json").write_text(
        json.dumps(rows, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "policy_calibration.json").write_text(
        json.dumps(calibration, indent=2, sort_keys=True) + "\n"
    )
    write_report(rows, calibration, out_dir)
    print(f"Wrote {len(rows)} policy rows to {out_dir}")


if __name__ == "__main__":
    main()
