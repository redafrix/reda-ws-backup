#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import numpy as np


def clean(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    return value


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(clean(row), sort_keys=True) + "\n")


def read_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def load_metadata(meta_dir: Path) -> dict[str, dict[str, Any]]:
    by_stem: dict[str, dict[str, Any]] = {}
    if not meta_dir.exists():
        return by_stem
    for path in sorted(meta_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except Exception:
            continue
        npz_path = data.get("npz_path")
        if npz_path:
            by_stem[Path(npz_path).stem] = data
        by_stem.setdefault(path.stem, data)
    return by_stem


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--source-worker", required=True, help="Source worker dir containing episode_summaries.jsonl and episodes_npz/")
    p.add_argument("--dest-worker", required=True, help="Destination worker dir to write trainer JSONL files")
    p.add_argument("--suite", default="libero_goal_object")
    args = p.parse_args()

    src = Path(args.source_worker)
    dst = Path(args.dest_worker)
    npz_dir = src / "episodes_npz"
    meta_dir = src / "episode_metadata"
    summaries_path = src / "episode_summaries.jsonl"
    if not summaries_path.exists():
        raise FileNotFoundError(summaries_path)
    if not npz_dir.exists():
        raise FileNotFoundError(npz_dir)

    dst.mkdir(parents=True, exist_ok=True)
    for name in ["episode_summaries.jsonl", "query_samples.jsonl", "transitions.jsonl", "conversion_manifest.json"]:
        target = dst / name
        if target.exists():
            target.unlink()

    meta_by_stem = load_metadata(meta_dir)
    summary_rows = list(read_jsonl(summaries_path))
    converted = 0
    skipped = 0
    query_rows = 0
    transition_rows = 0

    for idx, row in enumerate(summary_rows):
        if row.get("error_message") or row.get("outcome") == "error":
            skipped += 1
            continue
        npz_value = row.get("npz_path")
        if npz_value:
            npz_path = src / "episodes_npz" / Path(npz_value).name
        else:
            uid = str(row.get("episode_uid") or row.get("episode_id") or f"episode_{idx:06d}")
            npz_path = npz_dir / f"{uid.split('::')[-1]}.npz"
        if not npz_path.exists():
            # Fallback: use the global episode index when the summary path was absolute.
            gei = int(row.get("global_episode_index", idx))
            matches = sorted(npz_dir.glob(f"*{gei:06d}.npz"))
            if matches:
                npz_path = matches[0]
        if not npz_path.exists():
            raise FileNotFoundError(f"missing NPZ for summary index {idx}: {npz_path}")

        episode_id = str(row.get("episode_uid") or row.get("episode_id") or npz_path.stem)
        task_id = int(row.get("task_id"))
        meta = meta_by_stem.get(npz_path.stem, {})
        episode_summary = dict(row)
        episode_summary["episode_id"] = episode_id
        episode_summary["episode_uid"] = episode_id
        episode_summary["suite"] = args.suite
        episode_summary["task_id"] = task_id
        episode_summary["num_steps"] = int(row.get("num_env_steps") or row.get("num_steps") or 0)
        episode_summary["outcome"] = row.get("outcome") or ("success" if row.get("success") else "failure_or_timeout")
        episode_summary["sweep_idx"] = int(row.get("global_episode_index") or idx)
        append_jsonl(dst / "episode_summaries.jsonl", episode_summary)

        z = np.load(npz_path, allow_pickle=True)
        query_timesteps = z["query_timesteps"]
        query_proprio = z["query_proprio"]
        main_chunks_normalized = z["main_chunks_normalized"]
        ace_chunks_normalized = z["ace_chunks_normalized"]
        uncertainty_49d = z["uncertainty_49d"]
        uncertainty_delta_49d = z["uncertainty_delta_49d"]
        transition_query_indices = z["transition_query_indices"]
        transition_action_indices = z["transition_action_indices"]
        transition_timesteps = z["transition_timesteps"]
        executed_actions = z["executed_actions"]
        rewards = z["rewards"] if "rewards" in z.files else np.zeros((len(transition_timesteps),), dtype=np.float32)
        dones = z["dones"] if "dones" in z.files else np.zeros((len(transition_timesteps),), dtype=bool)
        successes = z["successes"] if "successes" in z.files else np.zeros((len(transition_timesteps),), dtype=bool)
        pre_proprio = z["pre_proprio"] if "pre_proprio" in z.files else np.zeros((len(transition_timesteps), 8), dtype=np.float32)
        post_proprio = z["post_proprio"] if "post_proprio" in z.files else np.zeros((len(transition_timesteps), 8), dtype=np.float32)

        first_actions: dict[int, np.ndarray] = {}
        for j, qidx in enumerate(transition_query_indices):
            if int(transition_action_indices[j]) == 0:
                first_actions[int(qidx)] = executed_actions[j]

        task_context = meta.get("task_context") or {}
        instruction = meta.get("task_instruction") or task_context.get("task_instruction") or ""
        for qidx in range(len(query_timesteps)):
            executed = first_actions.get(qidx, main_chunks_normalized[qidx, 0])
            append_jsonl(
                dst / "query_samples.jsonl",
                {
                    "episode_id": episode_id,
                    "episode_uid": episode_id,
                    "suite": args.suite,
                    "task_id": task_id,
                    "query_index": qidx,
                    "timestep": int(query_timesteps[qidx]),
                    "current": {"proprio": query_proprio[qidx]},
                    "main_candidate_action_chunk_normalized": main_chunks_normalized[qidx],
                    "ace_candidate_chunks_normalized": ace_chunks_normalized[qidx],
                    "simvla_uncertainty_49d": uncertainty_49d[qidx],
                    "simvla_uncertainty_delta_49d": uncertainty_delta_49d[qidx],
                    "executed_action": executed,
                    "task_instruction": instruction,
                },
            )
            query_rows += 1

        for j, qidx in enumerate(transition_query_indices):
            append_jsonl(
                dst / "transitions.jsonl",
                {
                    "episode_id": episode_id,
                    "episode_uid": episode_id,
                    "suite": args.suite,
                    "task_id": task_id,
                    "query_index": int(qidx),
                    "action_index_in_chunk": int(transition_action_indices[j]),
                    "timestep": int(transition_timesteps[j]),
                    "executed_action": executed_actions[j],
                    "reward": float(rewards[j]),
                    "done": bool(dones[j]),
                    "success": bool(successes[j]),
                    "pre_proprio": pre_proprio[j],
                    "post_proprio": post_proprio[j],
                },
            )
            transition_rows += 1
        converted += 1

    manifest = {
        "source_worker": str(src),
        "dest_worker": str(dst),
        "episodes_seen": len(summary_rows),
        "episodes_converted": converted,
        "episodes_skipped": skipped,
        "query_rows": query_rows,
        "transition_rows": transition_rows,
    }
    (dst / "conversion_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
