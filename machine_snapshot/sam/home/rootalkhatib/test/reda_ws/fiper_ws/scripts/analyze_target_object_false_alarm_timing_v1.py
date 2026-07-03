#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Any


WORKSPACE = Path(__file__).resolve().parent.parent
EXPERIMENTS = WORKSPACE / "experiments"
REPORT = WORKSPACE / "reports/FIPER_TARGET_OBJECT_FALSE_ALARM_TIMING_AUDIT_20260527.md"

POLICIES = [
    "score_q95_K3",
    "score_q95_K5",
    "score_q99_K3",
    "or_q95_K3",
    "or_q99_K3",
    "and_q95_K3",
]


def parse_policy(policy: str) -> tuple[str, str, int]:
    mode, q, k = policy.split("_")
    return mode, q, int(k[1:])


def pct(x: float | None) -> str:
    return "NA" if x is None else f"{100.0 * x:.2f}%"


def num(x: float | None) -> str:
    return "NA" if x is None else f"{x:.3f}"


def summary(values: list[float]) -> dict[str, float | None]:
    if not values:
        return {"mean": None, "median": None, "min": None, "max": None}
    return {
        "mean": float(mean(values)),
        "median": float(median(values)),
        "min": float(min(values)),
        "max": float(max(values)),
    }


def eval_policy(ep_rows: dict[str, list[tuple[int, float, float]]], thresholds: dict[str, dict[str, float]], policy: str) -> dict[str, Any]:
    mode, q, k = parse_policy(policy)
    n_episodes = len(ep_rows)
    flagged = 0
    first_norms: list[float] = []
    first_steps: list[float] = []
    episode_lengths: list[float] = []
    alarm_steps_fp: list[float] = []
    alarm_steps_all: list[float] = []
    for rows in ep_rows.values():
        rows.sort(key=lambda x: x[0])
        raw: list[bool] = []
        for _, score, ace in rows:
            score_alarm = score > thresholds["score"][q]
            ace_alarm = ace > thresholds["ace"][q]
            if mode == "score":
                raw.append(score_alarm)
            elif mode == "ace":
                raw.append(ace_alarm)
            elif mode == "and":
                raw.append(score_alarm and ace_alarm)
            elif mode == "or":
                raw.append(score_alarm or ace_alarm)
            else:
                raise ValueError(policy)
        debounced = [False] * len(raw)
        for t in range(k - 1, len(raw)):
            if all(raw[t - j] for j in range(k)):
                debounced[t] = True
        alarm_count = sum(debounced)
        alarm_steps_all.append(float(alarm_count))
        first = next((i for i, val in enumerate(debounced) if val), None)
        if first is None:
            continue
        flagged += 1
        first_norms.append(float(first / max(1, len(raw))))
        first_steps.append(float(rows[first][0]))
        episode_lengths.append(float(len(raw)))
        alarm_steps_fp.append(float(alarm_count))
    return {
        "episodes": n_episodes,
        "fp_episodes": flagged,
        "fp_rate": flagged / max(1, n_episodes),
        "first_norm": summary(first_norms),
        "first_step": summary(first_steps),
        "fp_episode_length": summary(episode_lengths),
        "alarm_steps_per_fp_episode": summary(alarm_steps_fp),
        "alarm_steps_per_success_episode": summary(alarm_steps_all),
    }


def load_success_ood(job_dir: Path) -> dict[str, list[tuple[int, float, float]]]:
    by_ep: dict[str, list[tuple[int, float, float]]] = defaultdict(list)
    with (job_dir / "scores.jsonl").open() as f:
        for line in f:
            row = json.loads(line)
            if row.get("split") != "success_test_ood":
                continue
            by_ep[str(row["episode_key"])].append((int(row["timestep"]), float(row["score"]), float(row["ace_entropy"])))
    return by_ep


def combine_metric(items: list[dict[str, Any]], key: str) -> dict[str, float | None]:
    vals: list[float] = []
    for item in items:
        vals.extend(item.get("_raw", {}).get(key, []))
    return summary(vals)


def main() -> None:
    per_result: list[dict[str, Any]] = []
    raw_lists: dict[tuple[str, str], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for campaign_dir in sorted(EXPERIMENTS.glob("clean_temporal_41_44_target_object_fold0*_20260527")):
        fold = campaign_dir.name.replace("clean_temporal_41_44_target_object_", "").replace("_20260527", "")
        for job_dir in sorted((campaign_dir / "jobs").glob("*")):
            if not (job_dir / "scores.jsonl").exists() or not (job_dir / "thresholds.json").exists():
                continue
            thresholds = json.loads((job_dir / "thresholds.json").read_text())
            ep_rows = load_success_ood(job_dir)
            for policy in POLICIES:
                metrics = eval_policy(ep_rows, thresholds, policy)
                per_result.append({"fold": fold, "job": job_dir.name, "policy": policy, **metrics})
                # Keep raw-ish values by re-evaluating compactly for weighted aggregate.
                mode, q, k = parse_policy(policy)
                for rows in ep_rows.values():
                    rows.sort(key=lambda x: x[0])
                    raw = []
                    for _, score, ace in rows:
                        s = score > thresholds["score"][q]
                        a = ace > thresholds["ace"][q]
                        raw.append(s if mode == "score" else a if mode == "ace" else (s and a) if mode == "and" else (s or a))
                    debounced = [False] * len(raw)
                    for t in range(k - 1, len(raw)):
                        if all(raw[t - j] for j in range(k)):
                            debounced[t] = True
                    raw_lists[(job_dir.name, policy)]["all_alarm_steps"].append(float(sum(debounced)))
                    first = next((i for i, val in enumerate(debounced) if val), None)
                    if first is not None:
                        raw_lists[(job_dir.name, policy)]["first_norm"].append(float(first / max(1, len(raw))))
                        raw_lists[(job_dir.name, policy)]["first_step"].append(float(rows[first][0]))
                        raw_lists[(job_dir.name, policy)]["fp_episode_length"].append(float(len(raw)))
                        raw_lists[(job_dir.name, policy)]["alarm_steps_fp"].append(float(sum(debounced)))

    lines: list[str] = []
    lines.append("# Target-Object OOD False-Alarm Timing Audit")
    lines.append("")
    lines.append("Split analyzed: `success_test_ood` for completed target-object folds `fold00` through `fold04`.")
    lines.append("")
    lines.append("A false alarm is an OOD-success episode where the policy fires at least once. For K-step debounce, first false alarm time is the actual trigger step after K consecutive high-risk steps.")
    lines.append("")

    lines.append("## Weighted Across All Target-Object Folds")
    lines.append("")
    lines.append("| Job | Policy | FP Episodes | Total Episodes | FP Rate | Mean First Norm | Median First Norm | Mean First Step | Median First Step | Mean Alarm Steps per FP | Mean Alarm Steps per Success Ep |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for job in sorted({r["job"] for r in per_result}):
        for policy in POLICIES:
            rows = [r for r in per_result if r["job"] == job and r["policy"] == policy]
            if not rows:
                continue
            total_eps = sum(int(r["episodes"]) for r in rows)
            fp_eps = sum(int(r["fp_episodes"]) for r in rows)
            raw = raw_lists[(job, policy)]
            first_norm = summary(raw["first_norm"])
            first_step = summary(raw["first_step"])
            alarm_fp = summary(raw["alarm_steps_fp"])
            alarm_all = summary(raw["all_alarm_steps"])
            lines.append(
                f"| `{job}` | `{policy}` | {fp_eps} | {total_eps} | {pct(fp_eps / max(1, total_eps))} | "
                f"{num(first_norm['mean'])} | {num(first_norm['median'])} | {num(first_step['mean'])} | {num(first_step['median'])} | "
                f"{num(alarm_fp['mean'])} | {num(alarm_all['mean'])} |"
            )
    lines.append("")

    lines.append("## Fold-Level Score q95 K3")
    lines.append("")
    lines.append("This is the policy family that produced roughly 45-60% OOD-success episode false alarms in the previous fold averages.")
    lines.append("")
    lines.append("| Fold | Job | FP Rate | Mean First Norm | Median First Norm | Mean First Step | Median First Step | Mean Alarm Steps per FP |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for r in sorted([r for r in per_result if r["policy"] == "score_q95_K3"], key=lambda x: (x["fold"], x["job"])):
        lines.append(
            f"| `{r['fold']}` | `{r['job']}` | {pct(r['fp_rate'])} | {num(r['first_norm']['mean'])} | "
            f"{num(r['first_norm']['median'])} | {num(r['first_step']['mean'])} | {num(r['first_step']['median'])} | "
            f"{num(r['alarm_steps_per_fp_episode']['mean'])} |"
        )
    lines.append("")

    lines.append("## Practical Reading")
    lines.append("")
    lines.append("- Mean first norm near `0.50` means false alarms usually happen halfway through successful OOD episodes, not immediately at the start.")
    lines.append("- Mean alarm steps per FP episode measures burden after an episode has already false-alarmed; mean alarm steps per success episode measures overall burden including clean episodes.")
    lines.append("- If a policy has acceptable failure detection but first false alarms occur late, it may still be usable as a warning signal; if first false alarms are early and frequent, it is much worse operationally.")
    lines.append("")
    lines.append("## Final Fields")
    lines.append("")
    lines.append("```text")
    lines.append(f"TARGET_OBJECT_FALSE_ALARM_TIMING_ROWS = {len(per_result)}")
    lines.append(f"TARGET_OBJECT_FALSE_ALARM_TIMING_REPORT = {REPORT.relative_to(WORKSPACE)}")
    lines.append("```")
    lines.append("")

    REPORT.write_text("\n".join(lines))
    print(REPORT)


if __name__ == "__main__":
    main()
