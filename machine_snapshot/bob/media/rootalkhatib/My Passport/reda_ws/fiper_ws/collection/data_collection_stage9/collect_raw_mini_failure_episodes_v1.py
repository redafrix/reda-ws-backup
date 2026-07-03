from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

from libero.libero import benchmark

from .collect_outcome_advantage_dataset import git_hash
from .collect_raw_failure_episodes_v1 import append_jsonl, run_episode, write_json
from .libero_pro_env_utils import make_env, reset_to_init
from .outcome_metrics import object_body_positions
from .simvla_candidate_sampler import load_simvla
from .task_parser import parse_task_context


DEFAULT_REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
SUITE_PREFIXES = ("libero_object", "libero_spatial", "libero_goal", "libero_10")


def available_perturbed_suites() -> list[str]:
    """Return LIBERO-PRO perturbation suites, excluding normal base suites."""
    bd = benchmark.get_benchmark_dict()
    return sorted(
        name for name in bd
        if "_with_" in name and name.startswith(SUITE_PREFIXES)
    )


def task_ids_for_suite(suite: str, max_task_id: int | None) -> list[int]:
    bd = benchmark.get_benchmark_dict()
    bench = bd[suite]()
    n_tasks = getattr(bench, "n_tasks", None)
    if callable(n_tasks):
        n_tasks = n_tasks()
    if n_tasks is None:
        tasks = getattr(bench, "tasks", None)
        n_tasks = len(tasks) if tasks is not None else 10
    upper = int(n_tasks)
    if max_task_id is not None:
        upper = min(upper, int(max_task_id) + 1)
    return list(range(max(0, upper)))


def should_record(summary: dict[str, Any], mode: str) -> bool:
    if mode == "all":
        return True
    if mode == "failure":
        return not bool(summary.get("episode_success"))
    if mode == "success":
        return bool(summary.get("episode_success"))
    raise ValueError(f"unknown record_outcomes={mode}")


def collect(args: argparse.Namespace) -> None:
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "episodes").mkdir(exist_ok=True)
    (outdir / "scout").mkdir(exist_ok=True)

    suites = available_perturbed_suites() if args.all_perturbed_suites else list(args.suites)
    model, proc, device = load_simvla()
    code_version = git_hash()
    started = time.time()
    recorded = 0
    scouted = 0
    summaries: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    write_json(outdir / "collection_config.json", {
        "schema_version": "stage9_raw_mini_failure_collection_config_v1",
        "out_dir": str(outdir),
        "suites": suites,
        "all_perturbed_suites": bool(args.all_perturbed_suites),
        "task_ids": args.task_ids,
        "max_task_id": args.max_task_id,
        "rollouts_per_task": int(args.rollouts_per_task),
        "max_recorded_episodes": int(args.max_recorded_episodes),
        "max_parent_episodes": int(args.max_parent_episodes),
        "parent_max_steps": int(args.parent_max_steps),
        "parent_policy_chunk_steps": int(args.parent_policy_chunk_steps),
        "record_outcomes": args.record_outcomes,
        "history_k": int(args.history_k),
        "policy_seed_base": int(args.policy_seed_base),
        "env_seed": int(args.env_seed),
        "resolution": int(args.resolution),
        "code_version": code_version,
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    })

    stop = False
    for suite in suites:
        if stop:
            break
        if suite not in benchmark.get_benchmark_dict():
            err = {"suite": suite, "error": "suite_not_available"}
            errors.append(err)
            append_jsonl(outdir / "errors.jsonl", [err])
            continue
        task_ids = list(args.task_ids) if args.task_ids else task_ids_for_suite(suite, args.max_task_id)
        for task_id in task_ids:
            if stop:
                break
            try:
                env, bundle = make_env(suite, task_id, args.resolution, seed=args.env_seed)
            except Exception as exc:
                err = {"suite": suite, "task_id": int(task_id), "error": f"make_env_failed: {exc}"}
                errors.append(err)
                append_jsonl(outdir / "errors.jsonl", [err])
                continue
            try:
                init_states = bundle["init_states"]
                lang = bundle["task"].language
                obs0 = reset_to_init(env, init_states[0], warmup=args.warmup)
                task_context = parse_task_context(lang, obs0, all_bodies=list(object_body_positions(env).keys()))
                for rollout_idx in range(min(args.rollouts_per_task, len(init_states))):
                    if recorded >= args.max_recorded_episodes or scouted >= args.max_parent_episodes:
                        stop = True
                        break
                    if args.max_runtime_minutes > 0 and (time.time() - started) / 60.0 >= args.max_runtime_minutes:
                        stop = True
                        break
                    policy_seed = args.policy_seed_base + scouted
                    init_state = init_states[rollout_idx % len(init_states)]
                    scout = run_episode(
                        env=env,
                        model=model,
                        proc=proc,
                        lang=lang,
                        device=device,
                        init_state=init_state,
                        task_context=task_context,
                        suite=suite,
                        task_id=task_id,
                        rollout_idx=rollout_idx,
                        policy_seed=policy_seed,
                        args=args,
                        record_dir=None,
                    )
                    scouted += 1
                    scout["record_outcomes"] = args.record_outcomes
                    append_jsonl(outdir / "scout" / "episode_scout_summaries.jsonl", [scout])
                    print(
                        f"scout {scout['episode_id']} success={scout['episode_success']} "
                        f"steps={scout['episode_steps']} recorded={recorded}/{args.max_recorded_episodes}",
                        flush=True,
                    )
                    if not should_record(scout, args.record_outcomes):
                        continue
                    episode_dir = outdir / "episodes" / scout["episode_id"]
                    summary = run_episode(
                        env=env,
                        model=model,
                        proc=proc,
                        lang=lang,
                        device=device,
                        init_state=init_state,
                        task_context=task_context,
                        suite=suite,
                        task_id=task_id,
                        rollout_idx=rollout_idx,
                        policy_seed=policy_seed,
                        args=args,
                        record_dir=episode_dir,
                    )
                    summary["record_outcomes"] = args.record_outcomes
                    append_jsonl(outdir / "raw_episode_summaries.jsonl", [summary])
                    summaries.append(summary)
                    recorded += 1
                    print(
                        f"recorded {summary['episode_id']} success={summary['episode_success']} "
                        f"steps={summary['episode_steps']} recorded={recorded}/{args.max_recorded_episodes}",
                        flush=True,
                    )
            except Exception as exc:
                err = {"suite": suite, "task_id": int(task_id), "error": f"collection_failed: {type(exc).__name__}: {exc}"}
                errors.append(err)
                append_jsonl(outdir / "errors.jsonl", [err])
            finally:
                try:
                    env.close()
                except Exception:
                    pass

    by_suite: dict[str, dict[str, int]] = {}
    for row in summaries:
        suite = str(row.get("suite"))
        slot = by_suite.setdefault(suite, {"episodes": 0, "success": 0, "failure": 0})
        slot["episodes"] += 1
        if row.get("episode_success"):
            slot["success"] += 1
        else:
            slot["failure"] += 1
    final = {
        "schema_version": "stage9_raw_mini_failure_collection_v1",
        "out_dir": str(outdir),
        "episodes_scouted": int(scouted),
        "episodes_recorded": int(recorded),
        "record_outcomes": args.record_outcomes,
        "by_suite": by_suite,
        "episode_ids": [row["episode_id"] for row in summaries],
        "errors": errors,
        "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "runtime_minutes": (time.time() - started) / 60.0,
    }
    write_json(outdir / "summary.json", final)
    print(json.dumps(final, indent=2, sort_keys=True), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-perturbed-suites", action="store_true")
    parser.add_argument("--suites", nargs="+", default=[
        "libero_object_with_mug",
        "libero_object_with_red_box",
        "libero_object_with_blue_stick",
        "libero_spatial_with_mug",
        "libero_spatial_with_red_box",
        "libero_goal_with_mug",
        "libero_goal_with_red_box",
        "libero_10_with_mug",
    ])
    parser.add_argument("--task-ids", nargs="+", type=int, default=None)
    parser.add_argument("--max-task-id", type=int, default=9)
    parser.add_argument("--rollouts-per-task", type=int, default=2)
    parser.add_argument("--max-recorded-episodes", type=int, default=80)
    parser.add_argument("--max-parent-episodes", type=int, default=160)
    parser.add_argument("--max-runtime-minutes", type=float, default=0.0)
    parser.add_argument("--record-outcomes", choices=["all", "failure", "success"], default="all")
    parser.add_argument("--parent-max-steps", type=int, default=400)
    parser.add_argument("--parent-policy-chunk-steps", type=int, default=10)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--policy-seed-base", type=int, default=2026052200)
    parser.add_argument("--env-seed", type=int, default=20260522)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data/data/raw_mini_failure_broad/raw_mini_failure_broad_v1"),
    )
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
