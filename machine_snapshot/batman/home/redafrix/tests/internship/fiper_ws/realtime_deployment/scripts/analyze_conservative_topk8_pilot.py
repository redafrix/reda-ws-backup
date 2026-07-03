#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter
from pathlib import Path


STAGES = [
    ("modified_simvla", "01_modified_simvla", "simvla_only"),
    ("topk8_protective", "02_topk8_protective", "risk_unc_topk8"),
    ("topk8_balanced", "03_topk8_balanced", "risk_unc_topk8"),
]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def summarize(rows: list[dict]) -> dict:
    wall = [float(row["wall_time_seconds"]) for row in rows]
    steps = [int(row["num_steps"]) for row in rows]
    return {
        "episodes": len(rows),
        "successes": sum(bool(row["success"]) for row in rows),
        "failures": sum(not bool(row["success"]) for row in rows),
        "success_rate": sum(bool(row["success"]) for row in rows) / len(rows) if rows else None,
        "mean_steps": statistics.mean(steps) if steps else None,
        "mean_wall_seconds": statistics.mean(wall) if wall else None,
        "total_modifications": sum(int(row.get("action_modifications_count", 0)) for row in rows),
        "modified_episodes": sum(int(row.get("action_modifications_count", 0)) > 0 for row in rows),
        "errors": sum(bool(row.get("error_message")) for row in rows),
        "seed_collisions": sum(int(row.get("seed_collisions", 0)) for row in rows),
        "main_ace_collisions": sum(int(row.get("main_seed_collisions_with_ace", 0)) for row in rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()

    episode_rows: dict[str, list[dict]] = {}
    payload: dict = {"run_dir": str(args.run_dir), "stages": {}, "paired": {}}
    for name, stage, policy in STAGES:
        policy_dir = args.run_dir / stage / policy
        rows = read_jsonl(policy_dir / "episode_summaries.jsonl")
        episode_rows[name] = rows
        summary = summarize(rows)
        step_path = policy_dir / f"step_scores_{policy}.jsonl"
        step_rows = read_jsonl(step_path)
        reasons = Counter(row.get("selection_reason") for row in step_rows if row.get("selection_reason"))
        selected_distances = []
        for row in step_rows:
            idx = int(row.get("selected_candidate_index", 0))
            distances = row.get("candidate_first_action_l2")
            if idx and distances:
                selected_distances.append(float(distances[idx]))
        summary.update(
            {
                "selection_reasons": dict(reasons),
                "selected_action_l2_mean": statistics.mean(selected_distances) if selected_distances else None,
                "selected_action_l2_max": max(selected_distances) if selected_distances else None,
            }
        )
        payload["stages"][name] = summary

    baseline = {row["reset_seed"]: row for row in episode_rows["modified_simvla"]}
    for variant in ["topk8_protective", "topk8_balanced"]:
        current = {row["reset_seed"]: row for row in episode_rows[variant]}
        seeds = sorted(set(baseline) & set(current))
        recoveries = [seed for seed in seeds if not baseline[seed]["success"] and current[seed]["success"]]
        regressions = [seed for seed in seeds if baseline[seed]["success"] and not current[seed]["success"]]
        payload["paired"][variant] = {
            "paired_episodes": len(seeds),
            "recoveries": len(recoveries),
            "regressions": len(regressions),
            "net_success_change": len(recoveries) - len(regressions),
            "recovery_seeds": recoveries,
            "regression_seeds": regressions,
        }

    seed_lists = [
        [row["reset_seed"] for row in episode_rows[name]]
        for name, _stage, _policy in STAGES
        if episode_rows[name]
    ]
    payload["seed_sequences_identical"] = bool(seed_lists) and all(values == seed_lists[0] for values in seed_lists[1:])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
