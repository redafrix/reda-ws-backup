#!/usr/bin/env python3
"""Dynamic online policy sweep for v2_018_transformer_k16 score traces.

This is policy-only analysis: it does not train a model and it does not touch
datasets. It evaluates whether non-fixed thresholds or recovery-aware mass rules
improve target-object OOD false alarms while preserving failure detection.

Allowed online inputs:
  - current timestep
  - current/past model scores
  - thresholds calibrated from success-only calibration/validation splits
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict, deque
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

EVAL_SPLITS = ["success_test_seen", "success_test_ood", "failure_eval_ood"]
LOAD_SPLITS = ["success_calib_seen", "success_val_seen", *EVAL_SPLITS]
TIME_BINS = [(0, 25), (25, 50), (50, 75), (75, 100), (100, 150), (150, 225), (225, 10_000)]


@dataclass
class EpisodeTrace:
    fold: str
    split: str
    episode_key: str
    timesteps: list[int]
    scores: list[float]


@dataclass
class PolicySpec:
    name: str
    threshold_mode: str
    state_mode: str
    decay: float | None = None
    reset_steps: int | None = None
    window: int | None = None


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


def time_bin_name(timestep: int) -> str:
    for lo, hi in TIME_BINS:
        if lo <= timestep < hi:
            return f"t{lo}_{hi}"
    return "t225_plus"


def load_traces(root: Path, folds: list[str], job: str) -> list[EpisodeTrace]:
    traces: list[EpisodeTrace] = []
    for fold in folds:
        scores_path = root / fold / "jobs" / job / "scores.jsonl"
        if not scores_path.exists():
            raise FileNotFoundError(scores_path)
        grouped: dict[tuple[str, str], list[tuple[int, float]]] = defaultdict(list)
        with scores_path.open() as f:
            for line in f:
                row = json.loads(line)
                split = row.get("split")
                if split not in LOAD_SPLITS:
                    continue
                grouped[(split, row["episode_key"])].append((int(row["timestep"]), float(row["score"])))
        for (split, episode_key), values in grouped.items():
            values.sort(key=lambda item: item[0])
            traces.append(
                EpisodeTrace(
                    fold=fold,
                    split=split,
                    episode_key=episode_key,
                    timesteps=[t for t, _ in values],
                    scores=[s for _, s in values],
                )
            )
    return traces


def flatten_rows(traces: list[EpisodeTrace], split: str) -> dict[str, list[tuple[int, float]]]:
    by_fold: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for trace in traces:
        if trace.split != split:
            continue
        by_fold[trace.fold].extend(zip(trace.timesteps, trace.scores))
    return by_fold


def build_thresholds(traces: list[EpisodeTrace]) -> dict[str, dict[str, object]]:
    calib_rows = flatten_rows(traces, "success_calib_seen")
    thresholds: dict[str, dict[str, object]] = {}
    for fold, rows in calib_rows.items():
        scores = [score for _, score in rows]
        fixed_q50 = quantile(scores, 0.50)
        fixed_q90 = quantile(scores, 0.90)
        fixed_q95 = quantile(scores, 0.95)
        fixed_q99 = quantile(scores, 0.99)
        binned_q95: dict[str, float] = {}
        binned_q90: dict[str, float] = {}
        bin_counts: dict[str, int] = {}
        by_bin: dict[str, list[float]] = defaultdict(list)
        for timestep, score in rows:
            by_bin[time_bin_name(timestep)].append(score)
        for lo, hi in TIME_BINS:
            name = f"t{lo}_{hi}"
            vals = by_bin.get(name, [])
            bin_counts[name] = len(vals)
            # Avoid noisy thresholds from tiny bins.
            binned_q95[name] = quantile(vals, 0.95) if len(vals) >= 100 else fixed_q95
            binned_q90[name] = quantile(vals, 0.90) if len(vals) >= 100 else fixed_q90
        thresholds[fold] = {
            "fixed_q50": fixed_q50,
            "fixed_q90": fixed_q90,
            "fixed_q95": fixed_q95,
            "fixed_q99": fixed_q99,
            "binned_q90": binned_q90,
            "binned_q95": binned_q95,
            "bin_counts": bin_counts,
        }
    return thresholds


def get_high_threshold(trace: EpisodeTrace, idx: int, mode: str, thresholds: dict[str, dict[str, object]]) -> float:
    fold_thr = thresholds[trace.fold]
    if mode == "fixed_q95":
        return float(fold_thr["fixed_q95"])
    if mode == "fixed_q99":
        return float(fold_thr["fixed_q99"])
    if mode == "binned_q95":
        return float(fold_thr["binned_q95"][time_bin_name(trace.timesteps[idx])])
    raise ValueError(f"unknown threshold mode {mode}")


def get_low_threshold(trace: EpisodeTrace, idx: int, mode: str, thresholds: dict[str, dict[str, object]]) -> float:
    fold_thr = thresholds[trace.fold]
    if mode == "binned_q95":
        return float(fold_thr["binned_q90"][time_bin_name(trace.timesteps[idx])])
    return float(fold_thr["fixed_q90"])


def state_series(trace: EpisodeTrace, spec: PolicySpec, thresholds: dict[str, dict[str, object]]) -> list[float]:
    states: list[float] = []
    if spec.state_mode == "mass":
        mass = 0.0
        for idx, score in enumerate(trace.scores):
            high = get_high_threshold(trace, idx, spec.threshold_mode, thresholds)
            mass += max(0.0, score - high)
            states.append(mass)
        return states

    if spec.state_mode == "leaky":
        decay = float(spec.decay if spec.decay is not None else 0.98)
        mass = 0.0
        for idx, score in enumerate(trace.scores):
            high = get_high_threshold(trace, idx, spec.threshold_mode, thresholds)
            mass = decay * mass + max(0.0, score - high)
            states.append(mass)
        return states

    if spec.state_mode == "reset":
        reset_steps = int(spec.reset_steps if spec.reset_steps is not None else 5)
        mass = 0.0
        low_run = 0
        for idx, score in enumerate(trace.scores):
            high = get_high_threshold(trace, idx, spec.threshold_mode, thresholds)
            low = get_low_threshold(trace, idx, spec.threshold_mode, thresholds)
            if score > high:
                mass += score - high
                low_run = 0
            elif score < low:
                low_run += 1
                if low_run >= reset_steps:
                    mass = 0.0
            else:
                low_run = 0
            states.append(mass)
        return states

    if spec.state_mode == "sliding":
        window = int(spec.window if spec.window is not None else 20)
        values: deque[float] = deque()
        mass = 0.0
        for idx, score in enumerate(trace.scores):
            high = get_high_threshold(trace, idx, spec.threshold_mode, thresholds)
            excess = max(0.0, score - high)
            values.append(excess)
            mass += excess
            if len(values) > window:
                mass -= values.popleft()
            states.append(mass)
        return states

    raise ValueError(f"unknown state mode {spec.state_mode}")


def trigger_index(states: list[float], state_threshold: float) -> int | None:
    for idx, value in enumerate(states):
        if value >= state_threshold:
            return idx
    return None


def calibrate_policy(
    traces: list[EpisodeTrace],
    spec: PolicySpec,
    thresholds: dict[str, dict[str, object]],
    alpha: float,
) -> float:
    val_stats = []
    for trace in traces:
        if trace.split != "success_val_seen":
            continue
        states = state_series(trace, spec, thresholds)
        val_stats.append(max(states) if states else 0.0)
    return conformal_upper_threshold(val_stats, alpha)


def evaluate_policy(
    traces: list[EpisodeTrace],
    spec: PolicySpec,
    thresholds: dict[str, dict[str, object]],
    state_threshold: float,
) -> dict[str, float]:
    out: dict[str, float] = {}
    for split in EVAL_SPLITS:
        split_traces = [trace for trace in traces if trace.split == split]
        fired: list[tuple[int, int]] = []
        for trace in split_traces:
            states = state_series(trace, spec, thresholds)
            idx = trigger_index(states, state_threshold)
            if idx is not None:
                fired.append((idx, len(states)))
        episodes = len(split_traces)
        rate = len(fired) / episodes if episodes else 0.0
        out[f"{split}_episodes"] = float(episodes)
        out[f"{split}_alarm_rate"] = rate
        if split == "failure_eval_ood":
            out["failure_det_rate"] = rate
            out["failure_never_rate"] = 1.0 - rate
            out["failure_det_at_10"] = (
                sum(1 for step, n in fired if step / max(1, n) <= 0.10) / episodes if episodes else 0.0
            )
            out["failure_det_at_25"] = (
                sum(1 for step, n in fired if step / max(1, n) <= 0.25) / episodes if episodes else 0.0
            )
            out["failure_det_at_50"] = (
                sum(1 for step, n in fired if step / max(1, n) <= 0.50) / episodes if episodes else 0.0
            )
            out["failure_mean_time_detected_only"] = (
                sum(step / max(1, n) for step, n in fired) / len(fired) if fired else 1.0
            )
    return out


def build_policy_specs() -> list[PolicySpec]:
    specs = [
        PolicySpec("fixed_q95_mass_conformal_alpha0p15", "fixed_q95", "mass"),
        PolicySpec("binned_q95_mass_conformal_alpha0p15", "binned_q95", "mass"),
    ]
    for mode in ["fixed_q95", "binned_q95"]:
        for decay in [0.90, 0.95, 0.98, 0.99]:
            specs.append(PolicySpec(f"{mode}_leaky_decay{str(decay).replace('.', 'p')}_alpha0p15", mode, "leaky", decay=decay))
        for reset_steps in [3, 5, 10, 20]:
            specs.append(PolicySpec(f"{mode}_reset_lowq90_K{reset_steps}_alpha0p15", mode, "reset", reset_steps=reset_steps))
        for window in [10, 20, 40, 80]:
            specs.append(PolicySpec(f"{mode}_sliding_W{window}_alpha0p15", mode, "sliding", window=window))
    return specs


def score_policy(metrics: dict[str, float]) -> float:
    return (
        2.0 * metrics["failure_det_at_25"]
        + 1.5 * metrics["failure_det_at_50"]
        + 1.0 * metrics["failure_det_rate"]
        - 1.5 * metrics["success_test_ood_alarm_rate"]
        - 0.5 * metrics["success_test_seen_alarm_rate"]
        - 1.0 * metrics["failure_never_rate"]
    )


def format_pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("experiments/clean_temporal_nextgen_v2_full_all_20260527"))
    parser.add_argument("--job", default="v2_018_transformer_k16")
    parser.add_argument("--alpha", type=float, default=0.15)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528"),
    )
    args = parser.parse_args()

    traces = load_traces(args.root, OBJECT_FOLDS, args.job)
    thresholds = build_thresholds(traces)
    rows: list[dict[str, object]] = []

    for spec in build_policy_specs():
        state_threshold = calibrate_policy(traces, spec, thresholds, args.alpha)
        metrics = evaluate_policy(traces, spec, thresholds, state_threshold)
        rows.append(
            {
                "policy": spec.name,
                "state_threshold": state_threshold,
                "balanced_score": score_policy(metrics),
                **metrics,
            }
        )

    rows.sort(key=lambda row: float(row["balanced_score"]), reverse=True)

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "dynamic_threshold_policy_sweep.csv"
    fieldnames = [
        "policy",
        "balanced_score",
        "state_threshold",
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
    ]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / "dynamic_threshold_policy_sweep.json").write_text(json.dumps(rows, indent=2, sort_keys=True))
    (out_dir / "dynamic_threshold_policy_calibration.json").write_text(json.dumps(thresholds, indent=2, sort_keys=True))

    baseline = next(row for row in rows if row["policy"] == "fixed_q95_mass_conformal_alpha0p15")
    candidates = [
        row
        for row in rows
        if row["policy"] != baseline["policy"]
        and float(row["failure_det_rate"]) >= float(baseline["failure_det_rate"]) - 0.05
        and float(row["failure_det_at_50"]) >= float(baseline["failure_det_at_50"]) - 0.05
        and float(row["success_test_ood_alarm_rate"]) < float(baseline["success_test_ood_alarm_rate"])
    ]
    candidates.sort(key=lambda row: (float(row["success_test_ood_alarm_rate"]), -float(row["failure_det_at_25"])))

    report_lines = [
        "# Transformer K16 Dynamic Threshold Policy Sweep",
        "",
        "## Setup",
        "",
        f"- Score root: `{args.root}`",
        f"- Job: `{args.job}`",
        f"- Alpha: `{args.alpha}`",
        "- Trained model changed: NO",
        "- Calibration uses success_calib_seen for row thresholds and success_val_seen for conformal state thresholds.",
        "- Dynamic threshold inputs: timestep and past/current scores only.",
        "",
        "## Baseline",
        "",
        "| Policy | Seen FA | OOD FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
        "| "
        + " | ".join(
            [
                str(baseline["policy"]),
                format_pct(float(baseline["success_test_seen_alarm_rate"])),
                format_pct(float(baseline["success_test_ood_alarm_rate"])),
                format_pct(float(baseline["failure_det_rate"])),
                format_pct(float(baseline["failure_det_at_25"])),
                format_pct(float(baseline["failure_det_at_50"])),
                f"{float(baseline['failure_mean_time_detected_only']):.3f}",
                format_pct(float(baseline["failure_never_rate"])),
            ]
        )
        + " |",
        "",
        "## Best Balanced Policies",
        "",
        "| Rank | Policy | Seen FA | OOD FA | Failure Det | Det@25 | Det@50 | Mean Time | Never | Score |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(rows[:12], start=1):
        report_lines.append(
            "| "
            + " | ".join(
                [
                    str(idx),
                    str(row["policy"]),
                    format_pct(float(row["success_test_seen_alarm_rate"])),
                    format_pct(float(row["success_test_ood_alarm_rate"])),
                    format_pct(float(row["failure_det_rate"])),
                    format_pct(float(row["failure_det_at_25"])),
                    format_pct(float(row["failure_det_at_50"])),
                    f"{float(row['failure_mean_time_detected_only']):.3f}",
                    format_pct(float(row["failure_never_rate"])),
                    f"{float(row['balanced_score']):.3f}",
                ]
            )
            + " |"
        )

    report_lines.extend(
        [
            "",
            "## Candidates That Beat Baseline OOD FA Without Major Detection Loss",
            "",
            "| Rank | Policy | Seen FA | OOD FA | Failure Det | Det@25 | Det@50 | Mean Time | Never |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    if candidates:
        for idx, row in enumerate(candidates[:12], start=1):
            report_lines.append(
                "| "
                + " | ".join(
                    [
                        str(idx),
                        str(row["policy"]),
                        format_pct(float(row["success_test_seen_alarm_rate"])),
                        format_pct(float(row["success_test_ood_alarm_rate"])),
                        format_pct(float(row["failure_det_rate"])),
                        format_pct(float(row["failure_det_at_25"])),
                        format_pct(float(row["failure_det_at_50"])),
                        f"{float(row['failure_mean_time_detected_only']):.3f}",
                        format_pct(float(row["failure_never_rate"])),
                    ]
                )
                + " |"
            )
    else:
        report_lines.append("| 0 | NONE | - | - | - | - | - | - | - |")

    best_candidate = candidates[0] if candidates else None
    report_lines.extend(
        [
            "",
            "## Verdict",
            "",
            f"- `DYNAMIC_POLICY_SWEEP_PASS` = **YES**",
            f"- `ANY_POLICY_REDUCES_OOD_FA_WITHOUT_MAJOR_DET_LOSS` = **{'YES' if best_candidate else 'NO'}**",
            f"- `BEST_RECOMMENDED_POLICY` = **{best_candidate['policy'] if best_candidate else 'NONE'}**",
            "",
            "## Output Files",
            "",
            f"- `{csv_path}`",
            f"- `{out_dir / 'dynamic_threshold_policy_sweep.json'}`",
            f"- `{out_dir / 'dynamic_threshold_policy_calibration.json'}`",
        ]
    )
    report_path = out_dir / "TRANSFORMER_K16_DYNAMIC_THRESHOLD_POLICY_SWEEP_REPORT.md"
    report_path.write_text("\n".join(report_lines) + "\n")
    print(f"Wrote {report_path}")


if __name__ == "__main__":
    main()
