#!/usr/bin/env python3
import json
from pathlib import Path
from collections import defaultdict, Counter

SRC = Path("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260617")
DST = Path("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618")

KEEP_SEEDS = set(range(100000, 100189))
TASKS = list(range(10))


def read_jsonl(path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path, rows):
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\n")


def main():
    DST.mkdir(parents=True, exist_ok=True)

    episodes_all = list(read_jsonl(SRC / "episode_summaries.jsonl"))
    episodes_all.sort(key=lambda r: int(r["episode_index_global"]))
    keep_eps_old = [
        ep for ep in episodes_all
        if ep["reset_seed"] in KEEP_SEEDS and ep["task_id"] in TASKS
    ]

    # Require exactly complete paired rounds: 189 seeds x 10 tasks.
    by_seed = defaultdict(list)
    for ep in keep_eps_old:
        by_seed[ep["reset_seed"]].append(ep["task_id"])
    bad = {seed: sorted(tasks) for seed, tasks in by_seed.items() if sorted(tasks) != TASKS}
    if len(by_seed) != 189 or bad:
        raise RuntimeError(f"Complete-round check failed: seeds={len(by_seed)} bad={bad}")

    # Re-index globally but keep original ids for traceability.
    old_to_new = {}
    key_to_ep = {}
    clean_eps = []
    per_task_index = Counter()
    for new_gid, ep in enumerate(keep_eps_old):
        old_gid = int(ep["episode_index_global"])
        ep = dict(ep)
        ep["original_episode_index_global"] = old_gid
        ep["episode_index_global"] = new_gid
        ep["episode_index_for_task"] = per_task_index[ep["task_id"]]
        ep["final_dataset_included"] = True
        old_to_new[old_gid] = new_gid
        key_to_ep[(ep["task_id"], ep["reset_seed"])] = ep
        per_task_index[ep["task_id"]] += 1
        clean_eps.append(ep)

    write_jsonl(DST / "episode_summaries.jsonl", clean_eps)

    # Query records can be joined by unique (task_id, reset_seed).
    clean_query_count = 0
    with (DST / "query_records.jsonl").open("w") as out:
        for q in read_jsonl(SRC / "query_records.jsonl"):
            ep = key_to_ep.get((q["task_id"], q["reset_seed"]))
            if ep is None:
                continue
            q = dict(q)
            q["suite"] = ep["suite"]
            q["task_name"] = ep["task_name"]
            q["episode_index_global"] = ep["episode_index_global"]
            q["original_episode_index_global"] = ep["original_episode_index_global"]
            q["round_index"] = ep["round_index"]
            q["episode_index_for_task"] = ep["episode_index_for_task"]
            out.write(json.dumps(q, sort_keys=True) + "\n")
            clean_query_count += 1

    # Step records lack ids in the raw file. Reconstruct by episode order and num_steps.
    clean_step_count = 0
    src_steps = (SRC / "step_records.jsonl").open()
    with (DST / "step_records.jsonl").open("w") as out:
        for raw_ep in episodes_all:
            n = int(raw_ep["num_steps"])
            clean_ep = key_to_ep.get((raw_ep["task_id"], raw_ep["reset_seed"]))
            for step_idx in range(n):
                line = src_steps.readline()
                if not line:
                    raise RuntimeError("step_records ended before episode_summaries total steps")
                if clean_ep is None:
                    continue
                row = json.loads(line)
                row["suite"] = clean_ep["suite"]
                row["task_id"] = clean_ep["task_id"]
                row["task_name"] = clean_ep["task_name"]
                row["reset_seed"] = clean_ep["reset_seed"]
                row["round_index"] = clean_ep["round_index"]
                row["episode_index_global"] = clean_ep["episode_index_global"]
                row["original_episode_index_global"] = clean_ep["original_episode_index_global"]
                row["episode_index_for_task"] = clean_ep["episode_index_for_task"]
                row["step_index_in_episode"] = step_idx
                out.write(json.dumps(row, sort_keys=True) + "\n")
                clean_step_count += 1
        orphan_step_rows = 0
        for extra in src_steps:
            if extra.strip():
                orphan_step_rows += 1
    src_steps.close()

    # Copy/enrich schema and create manifest/seed plan.
    schema = json.loads((SRC / "dataset_schema.json").read_text())
    schema.update({
        "dataset_name": "openvla_goal_object_final_1890_complete_rounds_20260618",
        "source_dataset": str(SRC),
        "cleaning_policy": "kept complete paired rounds only, reset_seed 100000..100188; dropped partial seed 100189 tasks 0..3",
        "episode_count": len(clean_eps),
        "task_count": 10,
        "round_count": 189,
        "query_records_have_episode_ids": True,
        "step_records_have_episode_ids": True,
        "ACE_AVAILABLE": "NO",
        "SIMVLA_UNCERTAINTY_FEATURES_AVAILABLE": "NO",
    })
    (DST / "dataset_schema.json").write_text(json.dumps(schema, indent=2, sort_keys=True) + "\n")

    seed_plan = {
        "seed_rule": "reset_seed = 100000 + round_index",
        "included_reset_seeds": [100000, 100188],
        "included_round_indices": [0, 188],
        "excluded_partial_reset_seed": 100189,
        "tasks_per_complete_round": TASKS,
        "episodes": len(clean_eps),
    }
    (DST / "seed_plan.json").write_text(json.dumps(seed_plan, indent=2, sort_keys=True) + "\n")

    succ = sum(bool(ep["success"]) for ep in clean_eps)
    per_task = {}
    for tid in TASKS:
        eps = [ep for ep in clean_eps if ep["task_id"] == tid]
        s = sum(bool(ep["success"]) for ep in eps)
        per_task[str(tid)] = {
            "episodes": len(eps),
            "success": s,
            "failure": len(eps) - s,
            "success_rate": s / len(eps),
            "task_name": eps[0]["task_name"],
        }

    manifest = {
        "dataset_name": "openvla_goal_object_final_1890_complete_rounds_20260618",
        "created_by": "Codex cleanup on 2026-06-18",
        "source_dataset": str(SRC),
        "output_dataset": str(DST),
        "suite": "libero_goal_object",
        "episode_count": len(clean_eps),
        "success_count": succ,
        "failure_count": len(clean_eps) - succ,
        "success_rate": succ / len(clean_eps),
        "query_record_count": clean_query_count,
        "step_record_count": clean_step_count,
        "complete_rounds": 189,
        "reset_seed_min": 100000,
        "reset_seed_max": 100188,
        "dropped_episode_count": len(episodes_all) - len(clean_eps),
        "dropped_reason": "partial round reset_seed=100189 had only tasks 0..3",
        "orphan_step_rows_dropped": orphan_step_rows,
        "orphan_step_rows_reason": "collector was interrupted during reset_seed=100189 task 4 before an episode summary was written",
        "model_id": clean_eps[0]["model_id"],
        "quantization": clean_eps[0]["quantization"],
        "unnorm_key": clean_eps[0]["unnorm_key"],
        "native_prediction_horizon": clean_eps[0]["native_prediction_horizon"],
        "actual_execution_horizon": clean_eps[0]["actual_execution_horizon"],
        "per_task": per_task,
        "known_limitations": [
            "Some tasks are label-imbalanced in this partial OpenVLA collection: tasks 2 and 9 have no successes; tasks 5 and 7 have no failures.",
            "ACE and SimVLA uncertainty features are unavailable by design.",
            "Raw source collector was interrupted before 10000 episodes; this final dataset intentionally freezes the complete 189-round subset."
        ],
    }
    (DST / "run_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    readme = f"""# OpenVLA Goal-Object Final Dataset

Final cleaned dataset for the OpenVLA-OFT risk model experiment.

- Source: `{SRC}`
- Kept: complete paired rounds only, reset seeds `100000..100188`
- Dropped: partial seed `100189` tasks 0..3
- Episodes: `{len(clean_eps)}`
- Success/failure: `{succ}` / `{len(clean_eps) - succ}`
- Suite: `libero_goal_object`
- Query and step rows now include episode/task/reset identifiers.

This is the frozen dataset for the current OpenVLA risk-model training run.
"""
    (DST / "README.md").write_text(readme)

    print(json.dumps({
        "output": str(DST),
        "episodes": len(clean_eps),
        "success": succ,
        "failure": len(clean_eps) - succ,
        "queries": clean_query_count,
        "steps": clean_step_count,
        "dropped": len(episodes_all) - len(clean_eps),
        "orphan_step_rows_dropped": orphan_step_rows,
    }, indent=2))


if __name__ == "__main__":
    main()
