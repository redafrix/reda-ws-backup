from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

from .strict_label_utils import (
    LABEL_BAD,
    LABEL_GOOD_STRONG,
    STAGE9_ROOT,
    label_distribution,
    load_datasets,
    parent_context,
    parent_episode_id,
    parent_phase,
    sample_label,
    state_id,
    write_csv,
    write_json,
)


DEFAULT_DATASETS = [
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1",
    "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2",
]


def bool_known(value: Any) -> bool | None:
    if value is None:
        return None
    return bool(value)


def build_episode_rows(samples: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped = defaultdict(list)
    for sample in samples:
        grouped[(sample.get("_dataset_name"), parent_episode_id(sample))].append(sample)

    rows = []
    for (dataset, episode_id), group in grouped.items():
        labels = Counter(sample_label(s) for s in group)
        contexts = [parent_context(s) for s in group]
        success_values = [bool_known(c.get("parent_episode_success")) for c in contexts if bool_known(c.get("parent_episode_success")) is not None]
        failed_values = [bool_known(c.get("parent_failed_or_timeout")) for c in contexts if bool_known(c.get("parent_failed_or_timeout")) is not None]
        parent_steps = [c.get("parent_episode_steps") for c in contexts if c.get("parent_episode_steps") is not None]
        min_bad_distance = None
        bad_distances = [c.get("distance_to_failure_or_timeout_steps") for s, c in zip(group, contexts) if sample_label(s) == LABEL_BAD and c.get("distance_to_failure_or_timeout_steps") is not None]
        if bad_distances:
            min_bad_distance = min(bad_distances)
        rows.append({
            "dataset": dataset,
            "parent_episode_id": episode_id,
            "num_samples": len(group),
            "label_counts": dict(labels),
            "has_bad": labels.get(LABEL_BAD, 0) > 0,
            "has_good_strong": labels.get(LABEL_GOOD_STRONG, 0) > 0,
            "parent_episode_success": success_values[0] if success_values else None,
            "parent_failed_or_timeout": failed_values[0] if failed_values else None,
            "parent_episode_steps": parent_steps[0] if parent_steps else None,
            "min_bad_distance_to_failure_or_timeout_steps": min_bad_distance,
            "phases": dict(Counter(parent_phase(s) for s in group)),
        })
    return rows


def build_sample_rows(samples: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for sample in samples:
        c = parent_context(sample)
        rows.append({
            "dataset": sample.get("_dataset_name"),
            "sample_id": sample.get("sample_id"),
            "state_id": state_id(sample),
            "parent_episode_id": c.get("parent_episode_id"),
            "label": sample_label(sample),
            "parent_phase": c.get("parent_phase"),
            "parent_episode_success": c.get("parent_episode_success"),
            "parent_failed_or_timeout": c.get("parent_failed_or_timeout"),
            "parent_episode_steps": c.get("parent_episode_steps"),
            "parent_step_index": c.get("parent_step_index"),
            "distance_to_failure_or_timeout_steps": c.get("distance_to_failure_or_timeout_steps"),
            "history_reward_sum": c.get("history_reward_sum"),
        })
    return rows


def build_report(samples: list[dict[str, Any]], episode_rows: list[dict[str, Any]], sample_rows: list[dict[str, Any]], args: argparse.Namespace) -> str:
    parent_success_known = [r for r in episode_rows if r["parent_episode_success"] is not None]
    bad_eps = [r for r in episode_rows if r["has_bad"]]
    no_bad_eps = [r for r in episode_rows if not r["has_bad"]]
    gs_eps = [r for r in episode_rows if r["has_good_strong"]]
    no_gs_eps = [r for r in episode_rows if not r["has_good_strong"]]

    def success_rate(rows: list[dict[str, Any]]) -> float | None:
        vals = [bool(r["parent_episode_success"]) for r in rows if r["parent_episode_success"] is not None]
        if not vals:
            return None
        return sum(vals) / len(vals)

    bad_sample_rows = [r for r in sample_rows if r["label"] == LABEL_BAD]
    good_sample_rows = [r for r in sample_rows if r["label"] == LABEL_GOOD_STRONG]
    bad_before_failure = [
        r for r in bad_sample_rows
        if r["parent_failed_or_timeout"] is True and r["distance_to_failure_or_timeout_steps"] is not None and r["distance_to_failure_or_timeout_steps"] >= 0
    ]
    bad_parent_phases = Counter(r["parent_phase"] for r in bad_sample_rows)
    good_parent_phases = Counter(r["parent_phase"] for r in good_sample_rows)
    distances = [r["distance_to_failure_or_timeout_steps"] for r in bad_before_failure if r["distance_to_failure_or_timeout_steps"] is not None]

    summary = {
        "num_samples": len(samples),
        "num_parent_episodes": len(episode_rows),
        "parent_success_known_episodes": len(parent_success_known),
        "episodes_with_bad": len(bad_eps),
        "episodes_without_bad": len(no_bad_eps),
        "parent_success_rate_with_bad": success_rate(bad_eps),
        "parent_success_rate_without_bad": success_rate(no_bad_eps),
        "parent_success_rate_with_good_strong": success_rate(gs_eps),
        "parent_success_rate_without_good_strong": success_rate(no_gs_eps),
        "bad_samples_before_parent_failure_or_timeout": len(bad_before_failure),
        "bad_distance_to_failure_or_timeout_mean": mean(distances) if distances else None,
        "bad_parent_phases": dict(bad_parent_phases),
        "good_strong_parent_phases": dict(good_parent_phases),
    }

    contradiction = False
    if summary["parent_success_rate_with_bad"] is not None and summary["parent_success_rate_without_bad"] is not None:
        contradiction = summary["parent_success_rate_with_bad"] > summary["parent_success_rate_without_bad"] + 0.20

    lines = [
        "# Stage 9 Episode Outcome Alignment Report",
        "",
        "Generated: `2026-05-18`",
        "",
        "## Inputs",
        "",
        *[f"- `{d}`" for d in args.data_dirs],
        "",
        "## Parent Success/Failure Analysis",
        "",
        "```json",
        json.dumps(summary, indent=2, sort_keys=True),
        "```",
        "",
        "## Whether BAD Appears Before Failures",
        "",
        f"- BAD samples before recorded parent failure/timeout: `{len(bad_before_failure)}`",
        f"- BAD parent phases: `{dict(bad_parent_phases)}`",
        "",
        "## Whether GOOD_STRONG Appears More In Successful Episodes",
        "",
        f"- Parent success rate with GOOD_STRONG episodes: `{summary['parent_success_rate_with_good_strong']}`",
        f"- Parent success rate without GOOD_STRONG episodes: `{summary['parent_success_rate_without_good_strong']}`",
        "",
        "## Whether Current BAD Labels Make Sense With Full Episode Outcomes",
        "",
        f"Contradiction detected: `{'YES' if contradiction else 'NO'}`",
        "",
        "The episode fields are useful as an audit signal only. They are not sufficient label proof because a parent rollout can fail for reasons unrelated to a specific same-state candidate action.",
        "",
        "## Limitations",
        "",
        "- Parent outcome fields are missing or weak for older phase-balanced samples.",
        "- Parent reward windows around selected states are not fully stored; only history reward tails are available.",
        "- Distance to failure/timeout is only approximate because it uses saved parent step index and parent episode length.",
        "- This audit does not replace replay or same-state counterfactual comparison.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dirs", nargs="+", default=DEFAULT_DATASETS)
    parser.add_argument("--out-dir", default=str(STAGE9_ROOT / "validation/episode_outcome_alignment"))
    parser.add_argument("--report-path", default=str(STAGE9_ROOT / "reports/STAGE9_EPISODE_OUTCOME_ALIGNMENT_REPORT.md"))
    args = parser.parse_args()

    samples, _ = load_datasets(args.data_dirs)
    episode_rows = build_episode_rows(samples)
    sample_rows = build_sample_rows(samples)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "episode_outcome_alignment.json", {
        "input_data_dirs": args.data_dirs,
        "label_distribution": label_distribution(samples),
        "episodes": episode_rows,
        "samples": sample_rows,
    })
    write_csv(out_dir / "episode_outcome_alignment_samples.csv", sample_rows)
    write_csv(out_dir / "episode_outcome_alignment_episodes.csv", episode_rows)

    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(samples, episode_rows, sample_rows, args))
    print(json.dumps({
        "samples": len(samples),
        "episodes": len(episode_rows),
        "report_path": str(report_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
