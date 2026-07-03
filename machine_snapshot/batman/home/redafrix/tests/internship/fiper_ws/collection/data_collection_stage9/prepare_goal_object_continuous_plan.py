#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np


FIELDS = [
    "episode_uid",
    "global_episode_index",
    "task_suite_name",
    "task_id",
    "initial_state_index",
    "eval_seed",
    "episode_seed",
    "bddl_relative_path",
    "bddl_sha256",
    "init_state_file_relative_path",
    "init_state_file_sha256",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-identity-csv", required=True)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--episodes", type=int, default=100_000)
    parser.add_argument("--plan-seed", type=int, default=2026060501)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = Path(args.exact_identity_csv)
    output = Path(args.output_csv)
    if args.episodes <= 0:
        raise ValueError("--episodes must be positive")

    with source.open(newline="", encoding="utf-8") as handle:
        exact_rows = list(csv.DictReader(handle))
    if len(exact_rows) != 200:
        raise ValueError(f"expected 200 exact rows, found {len(exact_rows)}")

    assets: dict[int, dict[str, str]] = {}
    for row in exact_rows:
        task_id = int(row["task_id"])
        current = {
            "bddl_relative_path": row["bddl_relative_path"],
            "bddl_sha256": row["bddl_sha256"],
            "init_state_file_relative_path": row["init_state_file_relative_path"],
            "init_state_file_sha256": row["init_state_file_sha256"],
        }
        if task_id in assets and assets[task_id] != current:
            raise ValueError(f"task {task_id} has inconsistent asset mapping")
        assets[task_id] = current
    if set(assets) != set(range(10)):
        raise ValueError(f"expected task IDs 0-9, found {sorted(assets)}")

    rng = np.random.default_rng(args.plan_seed)
    unique_seeds: set[int] = set()
    rows: list[dict[str, object]] = []
    task_order: list[int] = []
    while len(task_order) < args.episodes:
        task_order.extend(int(value) for value in rng.permutation(10))

    for index, task_id in enumerate(task_order[: args.episodes]):
        while True:
            episode_seed = int(rng.integers(1, 2**31 - 1, dtype=np.int64))
            if episode_seed not in unique_seeds:
                unique_seeds.add(episode_seed)
                break
        init_index = int(rng.integers(0, 50, dtype=np.int64))
        asset = assets[task_id]
        rows.append(
            {
                "episode_uid": f"libero_goal_object::continuous::{index:06d}",
                "global_episode_index": index,
                "task_suite_name": "libero_goal_object",
                "task_id": task_id,
                "initial_state_index": init_index,
                "eval_seed": episode_seed,
                "episode_seed": episode_seed,
                **asset,
            }
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    counts = {str(task_id): 0 for task_id in range(10)}
    for row in rows:
        counts[str(row["task_id"])] += 1
    manifest = {
        "schema_version": "goal_object_continuous_plan_v1",
        "episodes": len(rows),
        "plan_seed": args.plan_seed,
        "unique_episode_seeds": len(unique_seeds),
        "task_counts": counts,
        "initial_state_range": [0, 49],
        "csv_sha256": sha256_file(output),
        "source_exact_identity_csv": str(source),
        "source_exact_identity_sha256": sha256_file(source),
    }
    output.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
