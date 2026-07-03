#!/usr/bin/env python3
import argparse
import json
import sys
import time
import traceback
from collections import deque
from pathlib import Path

import numpy as np
import torch

WORKSPACE = Path("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616")
sys.path.append(str(WORKSPACE / "src"))

import run_openvla_ood_online_baseline_vs_risk_20260618 as runner


POLICY_NAME = "openvla_basic_h1"


def append_jsonl(path: Path, row: dict) -> None:
    with open(path, "a") as f:
        f.write(json.dumps(row, sort_keys=True) + "\n")


def run_episode_h1(task_id, reset_seed, episode_idx, episode_global_idx, task_suite, cfg, vla, processor, action_head, proprio_projector, args, paths, resize_size):
    task = task_suite.get_task(task_id)
    initial_states = task_suite.get_task_init_states(task_id)
    if args.suite == "libero_goal_object_ood" and getattr(task, "problem_folder", None) == "libero_goal_object_ood":
        if hasattr(task, "_replace"):
            task = task._replace(problem_folder="libero_goal_object_ood_temp")
        else:
            import copy

            task = copy.copy(task)
            object.__setattr__(task, "problem_folder", "libero_goal_object_ood_temp")

    runner.set_seed_everywhere(reset_seed)
    env, task_description = runner.get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
    success = False
    terminal_done = False
    error = ""
    num_queries = 0
    history_buffer = []
    action_queue = deque()
    executed_horizons = []
    t = 0
    start = time.time()

    try:
        env.reset()
        obs = env.set_init_state(initial_states[episode_idx % len(initial_states)])
        while t < args.max_steps + cfg.num_steps_wait:
            if t < cfg.num_steps_wait:
                obs, _reward, _done, _info = env.step(runner.get_libero_dummy_action(cfg.model_family))
                t += 1
                continue

            step_idx = t - cfg.num_steps_wait
            if len(action_queue) == 0:
                observation, _img = runner.prepare_observation(obs, resize_size)
                t0 = time.time()
                actions = runner.get_action(
                    cfg,
                    vla,
                    observation,
                    task_description,
                    processor=processor,
                    action_head=action_head,
                    proprio_projector=proprio_projector,
                    noisy_action_projector=None,
                    use_film=cfg.use_film,
                )
                inference_time = time.time() - t0
                actions_np = np.asarray(actions, dtype=np.float32)
                if actions_np.shape != (8, 7):
                    raise RuntimeError(f"action shape {actions_np.shape}, expected (8, 7)")
                if not np.isfinite(actions_np).all():
                    raise RuntimeError("non-finite action chunk")

                exec_h = 1
                selected = actions_np[:exec_h]
                action_queue.extend(selected)
                executed_horizons.append(exec_h)

                append_jsonl(
                    paths["query"],
                    {
                        "policy": POLICY_NAME,
                        "suite": args.suite,
                        "task_id": task_id,
                        "task_name": task.language,
                        "episode_index_global": episode_global_idx,
                        "episode_index_for_task": episode_idx,
                        "reset_seed": reset_seed,
                        "query_index": num_queries,
                        "env_timestep": step_idx,
                        "risk_score": None,
                        "risk_threshold": None,
                        "risk_triggered": False,
                        "executed_horizon": exec_h,
                        "native_prediction_horizon": 8,
                        "inference_time": inference_time,
                        "action_norm_statistics": {
                            "mean": float(np.mean(actions_np)),
                            "std": float(np.std(actions_np)),
                            "min": float(np.min(actions_np)),
                            "max": float(np.max(actions_np)),
                            "l1_norm": float(np.sum(np.abs(actions_np))),
                            "l2_norm": float(np.sqrt(np.sum(actions_np**2))),
                        },
                    },
                )
                num_queries += 1
                proprio = observation["state"]
                history_buffer.append((runner.pad_flat(proprio, 8), runner.pad_flat(selected[0], 7), np.zeros(7, dtype=np.float32)))

            action = action_queue.popleft()
            action_processed = runner.process_action(action, cfg.model_family)
            obs, _reward, done, _info = env.step(action_processed.tolist())
            if done:
                success = True
                terminal_done = True
                break
            t += 1
    except KeyboardInterrupt:
        raise
    except Exception as exc:
        error = repr(exc)
        traceback.print_exc()
    finally:
        try:
            env.close()
        except Exception:
            pass

    num_steps = max(0, t - cfg.num_steps_wait)
    return {
        "policy": POLICY_NAME,
        "suite": args.suite,
        "task_id": task_id,
        "task_name": task.language,
        "episode_index_for_task": episode_idx,
        "reset_seed": reset_seed,
        "success": bool(success),
        "terminal_done": bool(terminal_done),
        "timeout": bool(num_steps >= args.max_steps),
        "num_steps": int(num_steps),
        "max_steps": args.max_steps,
        "wall_time_seconds": time.time() - start,
        "model_id": cfg.pretrained_checkpoint,
        "quantization": "8-bit",
        "unnorm_key": cfg.unnorm_key,
        "native_prediction_horizon": 8,
        "fixed_execution_horizon": 1,
        "risk_threshold": None,
        "risk_horizon": None,
        "risk_trigger_count": 0,
        "num_queries": int(num_queries),
        "horizon1_query_count": int(sum(1 for h in executed_horizons if h == 1)),
        "horizon8_query_count": int(sum(1 for h in executed_horizons if h == 8)),
        "risk_score_min": None,
        "risk_score_max": None,
        "error_message": error,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="libero_goal_object_ood")
    ap.add_argument("--output-root", required=True)
    ap.add_argument("--episodes-per-task", type=int, default=100)
    ap.add_argument("--seed-start", type=int, default=10)
    ap.add_argument("--max-steps", type=int, default=800)
    ap.add_argument("--task-ids", default="all")
    args = ap.parse_args()

    out = Path(args.output_root)
    out.mkdir(parents=True, exist_ok=True)
    paths = {
        "summary": out / "episode_summaries.jsonl",
        "query": out / "query_records.jsonl",
        "manifest": out / "run_manifest.json",
    }

    cfg = runner.MockConfig(args.suite)
    runner.set_seed_everywhere(0)
    print("Loading OpenVLA...", flush=True)
    vla = runner.get_vla(cfg)
    runner.openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    processor = runner.get_processor(cfg)
    llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
    proprio_projector = runner.get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = runner.get_action_head(cfg, llm_dim=llm_dim)

    task_suite = runner.benchmark.get_benchmark_dict()[args.suite]()
    n_tasks = task_suite.get_num_tasks()
    if args.task_ids == "all":
        task_ids = list(range(n_tasks))
    else:
        task_ids = [int(x) for x in args.task_ids.split(",") if x.strip()]
    resize_size = runner.get_image_resize_size(cfg)

    manifest = {
        "suite": args.suite,
        "task_count": n_tasks,
        "task_ids": task_ids,
        "task_names": [task_suite.get_task(i).language for i in task_ids],
        "policy": POLICY_NAME,
        "episodes_per_task": args.episodes_per_task,
        "seed_start": args.seed_start,
        "seed_end": args.seed_start + args.episodes_per_task - 1,
        "max_steps": args.max_steps,
        "native_prediction_horizon": 8,
        "fixed_execution_horizon": 1,
        "model_id": cfg.pretrained_checkpoint,
        "quantization": "8-bit",
        "unnorm_key": cfg.unnorm_key,
        "comparison_target": "same suite/tasks/seeds/max_steps as libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618 openvla_basic H=8 baseline",
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    paths["manifest"].write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    completed = set()
    if paths["summary"].exists():
        with open(paths["summary"], "r") as f:
            for line in f:
                if line.strip():
                    row = json.loads(line)
                    completed.add((row["task_id"], row["reset_seed"]))

    total = len(task_ids) * args.episodes_per_task
    done_count = len(completed)
    print(f"[info] Starting/resuming {POLICY_NAME}: {done_count}/{total} already complete", flush=True)
    for task_id in task_ids:
        for episode_idx in range(args.episodes_per_task):
            seed = args.seed_start + episode_idx
            key = (task_id, seed)
            if key in completed:
                continue
            print(f"[{done_count + 1}/{total}] policy={POLICY_NAME} task={task_id} seed={seed}", flush=True)
            row = run_episode_h1(task_id, seed, episode_idx, done_count, task_suite, cfg, vla, processor, action_head, proprio_projector, args, paths, resize_size)
            row["episode_index_global"] = done_count
            append_jsonl(paths["summary"], row)
            completed.add(key)
            done_count += 1

    print("DONE", flush=True)


if __name__ == "__main__":
    main()
