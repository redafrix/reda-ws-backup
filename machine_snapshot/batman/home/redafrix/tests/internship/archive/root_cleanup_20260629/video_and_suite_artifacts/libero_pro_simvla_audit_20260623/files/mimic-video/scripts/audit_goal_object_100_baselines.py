#!/usr/bin/env python3
"""Audit the goal-object 100-episode WM/SimVLA baseline comparison."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def read_jsonl(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def read_manifest(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise RuntimeError(f"Manifest is empty: {path}")
    return rows


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_manifest(rows: list[dict[str, str]]) -> None:
    identities = [
        (
            row["task_suite_name"],
            int(row["task_id"]),
            int(row["initial_state_index"]),
            int(row["eval_seed"]),
        )
        for row in rows
    ]
    if len(rows) != 100:
        raise RuntimeError(f"Expected 100 manifest rows, got {len(rows)}.")
    if len(set(identities)) != len(identities):
        raise RuntimeError("Manifest contains duplicate episode identities.")
    if {row["task_suite_name"] for row in rows} != {"libero_goal_object"}:
        raise RuntimeError("Manifest must contain only libero_goal_object rows.")
    if {int(row["eval_seed"]) for row in rows} != {0}:
        raise RuntimeError("Manifest eval_seed must be exactly 0 for all rows.")
    expected_pairs = {(task_id, state_idx) for task_id in range(10) for state_idx in range(10)}
    actual_pairs = {(int(row["task_id"]), int(row["initial_state_index"])) for row in rows}
    if actual_pairs != expected_pairs:
        missing = sorted(expected_pairs - actual_pairs)
        extra = sorted(actual_pairs - expected_pairs)
        raise RuntimeError(f"Manifest task/state grid mismatch. missing={missing[:5]}, extra={extra[:5]}")
    for row in rows:
        if int(row["trial_index"]) != int(row["initial_state_index"]):
            raise RuntimeError(f"trial_index mismatch in row: {row}")


def validate_world_model(rows: list[dict[str, object]], manifest_rows: list[dict[str, str]], result_dir: Path) -> None:
    expected_pairs = [(int(row["task_id"]), int(row["initial_state_index"])) for row in manifest_rows]
    actual_pairs = [(int(row["task_id"]), int(row["episode_index"])) for row in rows]
    if actual_pairs != expected_pairs:
        raise RuntimeError("World-model task/trial order does not match manifest.")
    if len(rows) != 100:
        raise RuntimeError(f"Expected 100 world-model outcomes, got {len(rows)}.")
    runtime_rows = read_jsonl(result_dir / "policy_query_runtime.jsonl")
    horizons = {int(row["selected_execute_horizon"]) for row in runtime_rows}
    if horizons != {56}:
        raise RuntimeError(f"World-model baseline must execute h56 only, got {sorted(horizons)}.")
    forbidden = ["action_candidate_uncertainty.jsonl", "v2w_uncertainty.jsonl"]
    present = [name for name in forbidden if (result_dir / name).exists()]
    if present:
        raise RuntimeError(f"World-model no-UQ baseline unexpectedly wrote UQ logs: {present}")


def validate_simvla(rows: list[dict[str, object]], manifest_rows: list[dict[str, str]], result_dir: Path) -> None:
    expected_uids = [row["episode_uid"] for row in manifest_rows]
    actual_uids = [str(row["episode_uid"]) for row in rows]
    if actual_uids != expected_uids:
        raise RuntimeError("SimVLA episode UID order does not match manifest.")
    if len(rows) != 100:
        raise RuntimeError(f"Expected 100 SimVLA outcomes, got {len(rows)}.")
    step_rows = read_jsonl(result_dir / "arbiter_step_scores.jsonl")
    if {str(row["branch"]) for row in step_rows} != {"simvla"}:
        raise RuntimeError("HF SimVLA baseline used a non-SimVLA branch.")
    if {int(row["simvla_selected_candidate_index"]) for row in step_rows} != {0}:
        raise RuntimeError("HF SimVLA baseline selected non-main candidates.")
    if {int(row["selected_execute_horizon"]) for row in step_rows} != {10}:
        raise RuntimeError("HF SimVLA baseline did not execute h10 only.")
    if any(row["simvla_candidate_scores"] is not None for row in step_rows):
        raise RuntimeError("HF SimVLA baseline unexpectedly computed risk scores.")
    run_manifest = json.loads((result_dir / "run_manifest.json").read_text(encoding="utf-8"))
    if run_manifest["uses_world_model"]:
        raise RuntimeError("HF SimVLA baseline run_manifest says uses_world_model=true.")


def summarize(name: str, rows: list[dict[str, object]], step_key: str, query_key: str) -> dict[str, object]:
    successes = sum(bool(row["success"]) for row in rows)
    per_task: dict[int, dict[str, object]] = {}
    buckets: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[int(row["task_id"])].append(row)
    for task_id, task_rows in sorted(buckets.items()):
        task_successes = sum(bool(row["success"]) for row in task_rows)
        per_task[task_id] = {
            "episodes": len(task_rows),
            "successes": task_successes,
            "rate": task_successes / len(task_rows),
        }
    return {
        "policy": name,
        "episodes": len(rows),
        "successes": successes,
        "failures": len(rows) - successes,
        "success_rate": successes / len(rows),
        "env_steps_or_frames": sum(int(row[step_key]) for row in rows),
        "policy_queries": sum(int(row[query_key]) for row in rows),
        "wall_time_seconds": sum(float(row["wall_time_seconds"]) for row in rows),
        "per_task": per_task,
    }


def agreement(
    wm_rows: list[dict[str, object]],
    sim_rows: list[dict[str, object]],
    manifest_rows: list[dict[str, str]],
) -> dict[str, object]:
    wm_by_pair = {(int(row["task_id"]), int(row["episode_index"])): row for row in wm_rows}
    sim_by_uid = {str(row["episode_uid"]): row for row in sim_rows}
    counts: Counter[tuple[bool, bool]] = Counter()
    per_task: dict[int, Counter[tuple[bool, bool]]] = defaultdict(Counter)
    for row in manifest_rows:
        pair = (int(row["task_id"]), int(row["initial_state_index"]))
        uid = row["episode_uid"]
        outcomes = (bool(wm_by_pair[pair]["success"]), bool(sim_by_uid[uid]["success"]))
        counts[outcomes] += 1
        per_task[pair[0]][outcomes] += 1
    return {
        "both_success": counts[(True, True)],
        "world_model_only_success": counts[(True, False)],
        "simvla_only_success": counts[(False, True)],
        "both_failure": counts[(False, False)],
        "same_outcome": counts[(True, True)] + counts[(False, False)],
        "per_task": {
            task_id: {
                "both_success": task_counts[(True, True)],
                "world_model_only_success": task_counts[(True, False)],
                "simvla_only_success": task_counts[(False, True)],
                "both_failure": task_counts[(False, False)],
            }
            for task_id, task_counts in sorted(per_task.items())
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("/home/utilisateur/worldmodel/mimic-video"),
    )
    parser.add_argument("--write-json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root
    manifest_path = root / "configs/uq_benchmarks/libero_goal_object_task0to9_trials0to9_eval_seed0_tasklang_20260623.csv"
    result_root = root / "results/libero_goal_object_100_official_tasklang_20260623"
    wm_dir = result_root / "wm_h56_k1/libero_goal_object"
    sim_dir = result_root / "hf_simvla"
    manifest_rows = read_manifest(manifest_path)
    wm_rows = read_jsonl(wm_dir / "episode_outcomes.jsonl")
    sim_rows = read_jsonl(sim_dir / "episode_summaries.jsonl")

    validate_manifest(manifest_rows)
    validate_world_model(wm_rows, manifest_rows, wm_dir)
    validate_simvla(sim_rows, manifest_rows, sim_dir)

    report = {
        "manifest": str(manifest_path),
        "manifest_sha256": sha256(manifest_path),
        "world_model": summarize("WM h56 no-UQ", wm_rows, "replay_frames", "policy_queries"),
        "simvla": summarize("HF/base SimVLA", sim_rows, "num_steps", "num_queries"),
        "agreement": agreement(wm_rows, sim_rows, manifest_rows),
    }
    if args.write_json is not None:
        args.write_json.parent.mkdir(parents=True, exist_ok=True)
        args.write_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
