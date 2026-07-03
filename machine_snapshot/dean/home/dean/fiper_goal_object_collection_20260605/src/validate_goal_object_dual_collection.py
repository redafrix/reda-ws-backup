#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

import numpy as np


TOPK8_INDICES = [6, 21, 25, 27, 23, 2, 26, 24]


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except Exception as exc:
                raise ValueError(f"invalid JSON at {path}:{line_number}: {exc}") from exc
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    parser.add_argument("--run-root", required=True)
    parser.add_argument("--execution-mode", choices=["receding", "chunk10"], required=True)
    parser.add_argument("--expected-episodes", type=int, required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    plan_path = Path(args.plan)
    run_root = Path(args.run_root)
    with plan_path.open(newline="", encoding="utf-8") as handle:
        plan_rows = list(csv.DictReader(handle))
    expected_uids = {row["episode_uid"] for row in plan_rows[: args.expected_episodes]}
    plan_by_uid = {row["episode_uid"]: row for row in plan_rows[: args.expected_episodes]}

    summary_files = sorted(run_root.glob("worker_*/episode_summaries.jsonl"))
    if not summary_files and (run_root / "episode_summaries.jsonl").exists():
        summary_files = [run_root / "episode_summaries.jsonl"]
    summaries = [row for path in summary_files for row in read_jsonl(path)]
    by_uid: dict[str, dict] = {}
    duplicate_uids: list[str] = []
    errors: list[str] = []
    shape_failures: list[str] = []
    seed_collisions = 0

    for summary in summaries:
        uid = str(summary.get("episode_uid"))
        if uid in by_uid:
            duplicate_uids.append(uid)
        by_uid[uid] = summary

    actual_uids = set(by_uid)
    missing = sorted(expected_uids - actual_uids)
    unexpected = sorted(actual_uids - expected_uids)
    outcome_counts: Counter[str] = Counter()
    total_queries = 0
    total_transitions = 0

    for uid in sorted(expected_uids & actual_uids):
        summary = by_uid[uid]
        outcome_counts[str(summary.get("outcome"))] += 1
        if summary.get("execution_mode") != args.execution_mode:
            errors.append(f"{uid}: execution_mode={summary.get('execution_mode')}")
        if summary.get("error_message"):
            errors.append(f"{uid}: {summary['error_message']}")
        if not summary.get("episode_complete"):
            errors.append(f"{uid}: incomplete summary")
        plan_row = plan_by_uid[uid]
        for key in ["task_id", "initial_state_index", "eval_seed", "episode_seed"]:
            if int(summary.get(key, -1)) != int(plan_row[key]):
                errors.append(f"{uid}: summary {key}={summary.get(key)} does not match plan={plan_row[key]}")
        metadata_path = Path(summary["metadata_path"])
        if not metadata_path.is_file():
            errors.append(f"{uid}: missing metadata {metadata_path}")
        else:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata.get("episode", {}).get("episode_uid") != uid:
                errors.append(f"{uid}: metadata episode UID mismatch")
            if not metadata.get("task_instruction"):
                errors.append(f"{uid}: empty BDDL task instruction")
            if len(metadata.get("warmup_transitions", [])) != 10:
                errors.append(f"{uid}: expected 10 warmup transitions")
        npz_path = Path(summary["npz_path"])
        if not npz_path.is_file():
            errors.append(f"{uid}: missing NPZ {npz_path}")
            continue
        with np.load(npz_path) as data:
            query_timesteps = data["query_timesteps"]
            transition_timesteps = data["transition_timesteps"]
            query_indices = data["transition_query_indices"]
            action_indices = data["transition_action_indices"]
            q = len(query_timesteps)
            t = len(transition_timesteps)
            total_queries += q
            total_transitions += t
            expected_shapes = {
                "query_proprio": (q, 8),
                "ace_seeds": (q, 8),
                "main_chunks_env": (q, 10, 7),
                "main_chunks_normalized": (q, 10, 7),
                "ace_chunks_env": (q, 8, 10, 7),
                "ace_chunks_normalized": (q, 8, 10, 7),
                "uncertainty_49d": (q, 49),
                "uncertainty_delta_49d": (q, 49),
                "uncertainty_topk8": (q, 8),
                "uncertainty_delta_topk8": (q, 8),
                "executed_actions": (t, 7),
                "pre_proprio": (t, 8),
                "post_proprio": (t, 8),
            }
            for key, expected_shape in expected_shapes.items():
                if data[key].shape != expected_shape:
                    shape_failures.append(f"{uid}: {key}={data[key].shape}, expected={expected_shape}")
            if not np.array_equal(transition_timesteps, np.arange(t, dtype=np.int32)):
                errors.append(f"{uid}: transition timesteps are not contiguous 0..{t - 1}")
            if q and int(query_timesteps[0]) != 0:
                errors.append(f"{uid}: first query timestep is not zero")
            if args.execution_mode == "receding":
                if q != t:
                    errors.append(f"{uid}: receding query/transition mismatch q={q}, t={t}")
                if np.any(action_indices != 0):
                    errors.append(f"{uid}: receding action index is not always zero")
                if not np.array_equal(query_timesteps, np.arange(q, dtype=query_timesteps.dtype)):
                    errors.append(f"{uid}: receding query timesteps are not contiguous")
            else:
                expected_q = (t + 9) // 10
                if q != expected_q:
                    errors.append(f"{uid}: chunk10 query count q={q}, expected={expected_q} for t={t}")
                if not np.array_equal(query_timesteps, np.arange(0, t, 10, dtype=query_timesteps.dtype)):
                    errors.append(f"{uid}: chunk10 query timesteps are not 0,10,20,...")
                for query_index in range(q):
                    indices = action_indices[query_indices == query_index]
                    if not np.array_equal(indices, np.arange(len(indices), dtype=indices.dtype)):
                        errors.append(f"{uid}: bad action indices in query {query_index}")
            if q and not np.allclose(data["uncertainty_delta_49d"][0], 0.0):
                errors.append(f"{uid}: first uncertainty delta is not zero")
            if not np.array_equal(data["uncertainty_topk8"], data["uncertainty_49d"][:, TOPK8_INDICES]):
                errors.append(f"{uid}: top-8 uncertainty extraction mismatch")
            if not np.array_equal(
                data["uncertainty_delta_topk8"], data["uncertainty_delta_49d"][:, TOPK8_INDICES]
            ):
                errors.append(f"{uid}: top-8 uncertainty delta extraction mismatch")
            numeric_keys = [
                "main_chunks_env",
                "main_chunks_normalized",
                "ace_chunks_env",
                "ace_chunks_normalized",
                "uncertainty_49d",
                "uncertainty_delta_49d",
                "executed_actions",
                "pre_proprio",
                "post_proprio",
            ]
            for key in numeric_keys:
                if not np.all(np.isfinite(data[key])):
                    errors.append(f"{uid}: non-finite values in {key}")
            if t:
                expected_actions = data["main_chunks_env"][query_indices, action_indices]
                if not np.array_equal(data["executed_actions"], expected_actions):
                    errors.append(f"{uid}: executed actions do not match the selected main chunk")
            main_seeds = data["main_seeds"].tolist()
            ace_seeds = data["ace_seeds"].tolist()
            for main_seed, ace in zip(main_seeds, ace_seeds):
                all_seeds = [int(main_seed), *[int(value) for value in ace]]
                if len(set(all_seeds)) != 9:
                    seed_collisions += 1

    report = {
        "schema_version": "goal_object_dual_collection_validation_v1",
        "plan": str(plan_path),
        "run_root": str(run_root),
        "execution_mode": args.execution_mode,
        "expected_episodes": args.expected_episodes,
        "summary_files": [str(path) for path in summary_files],
        "actual_unique_episodes": len(actual_uids),
        "missing_episode_uids": missing,
        "unexpected_episode_uids": unexpected,
        "duplicate_episode_uids": duplicate_uids,
        "outcome_counts": dict(outcome_counts),
        "total_queries": total_queries,
        "total_transitions": total_transitions,
        "seed_collision_timesteps": seed_collisions,
        "errors": errors,
        "shape_failures": shape_failures,
    }
    report["pass"] = not any([missing, unexpected, duplicate_uids, errors, shape_failures, seed_collisions])
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
