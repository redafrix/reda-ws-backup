#!/usr/bin/env python3
import argparse
import fcntl
import hashlib
import json
import os
import random
import sys
import time
from pathlib import Path

import numpy as np
import torch

REDA_WS = Path(os.environ.get("REDA_WS", "/home/rootalkhatib/test/reda_ws"))
os.environ["REDA_WS"] = str(REDA_WS)

asynchvla_src = REDA_WS / "asynchvla_ws/src"
simvla_code = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
libero_pro = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"

for p in [asynchvla_src, simvla_code, libero_pro]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

try:
    from data_collection_stage9.libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from data_collection_stage9.simvla_candidate_sampler import load_simvla, sample_candidate
except ImportError as exc:
    print(f"Import error: {exc}. Trying local imports.", flush=True)
    sys.path.append(str(Path(__file__).parent.parent.parent / "scripts"))
    from libero_pro_env_utils import make_env, obs_images, obs_to_proprio, reset_to_init
    from simvla_candidate_sampler import load_simvla, sample_candidate


def generate_chunk(model, proc, lang, obs, seed: int, device, steps: int = 10):
    img, wrist = obs_images(obs)
    prop = obs_to_proprio(obs)
    cand = sample_candidate(
        model, proc, lang, img, wrist, prop, seed=seed, device=device, steps=steps, flowtrace=False
    )
    return cand["candidate_action_env"].numpy().astype(np.float32)


def fallback_action_seed(reset_seed: int, episode_index: int, timestep: int) -> int:
    raw = f"baseline_fallback_{reset_seed}_{episode_index}_{timestep}".encode()
    return int(hashlib.sha256(raw).hexdigest()[:8], 16) % (2**31 - 1)


def load_main_seed_trace(path: Path) -> dict[int, list[int]]:
    trace: dict[int, list[int]] = {}
    bad_lines = 0
    with path.open() as f:
        for line in f:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except Exception:
                bad_lines += 1
                continue
            reset_seed = int(row["reset_seed"])
            timestep = int(row["timestep"])
            main_seed_raw = row.get("main_action_seed", row.get("main_seed"))
            if main_seed_raw is None:
                raise KeyError(f"seed trace row missing main_action_seed/main_seed: keys={sorted(row.keys())}")
            main_seed = int(main_seed_raw)
            bucket = trace.setdefault(reset_seed, [])
            if timestep == len(bucket):
                bucket.append(main_seed)
            elif timestep < len(bucket):
                if bucket[timestep] != main_seed:
                    raise ValueError(
                        f"Conflicting main seed for reset_seed={reset_seed} timestep={timestep}: "
                        f"{bucket[timestep]} vs {main_seed}"
                    )
            else:
                raise ValueError(
                    f"Non-contiguous seed trace for reset_seed={reset_seed}: got timestep={timestep}, "
                    f"expected={len(bucket)}"
                )
    if bad_lines:
        raise ValueError(f"Bad JSON lines in seed trace {path}: {bad_lines}")
    return trace


def append_jsonl_locked(path: Path, obj: dict):
    lock_path = path.with_suffix(path.suffix + ".lock")
    lock_file = open(lock_path, "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        with path.open("a") as f:
            f.write(json.dumps(obj) + "\n")
    finally:
        fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()


def write_live_status(path: Path, worker_id: str, attempted: int, successes: int, last_episode_idx: int):
    status = {
        "worker_id": worker_id,
        "total_episodes_attempted": attempted,
        "total_successes": successes,
        "total_failures": attempted - successes,
        "success_rate": successes / attempted if attempted else 0.0,
        "last_episode_idx": last_episode_idx,
        "last_updated": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    path.write_text(json.dumps(status, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--worker-id", required=True)
    parser.add_argument("--episode-start", type=int, required=True)
    parser.add_argument("--episode-end", type=int, required=True)
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text())
    suite = config["suite"]
    task_id = int(config["task_id"])
    max_steps = int(config.get("max_steps", 300))
    seeds = [int(x) for x in config["seeds"]]
    out_dir = Path(config["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "logs").mkdir(parents=True, exist_ok=True)

    suffix = args.worker_id.replace("/", "_")
    summary_path = out_dir / f"episode_summary_w{suffix}.jsonl"
    seed_log_path = out_dir / f"action_seed_trace_w{suffix}.jsonl"
    live_path = out_dir / "live_status.json"

    for p in [summary_path, seed_log_path, live_path]:
        if p.exists():
            p.unlink()

    trace_path = Path(config["riskaware_step_scores_path"])
    print(f"[{args.worker_id}] Loading risk-aware main-action seed trace: {trace_path}", flush=True)
    seed_trace = load_main_seed_trace(trace_path)

    ckpt_override = config.get("simvla_checkpoint") or config.get("checkpoint")
    smolvlm_override = config.get("smolvlm_path") or config.get("smolvlm")
    norm_stats_override = config.get("norm_stats")
    print(f"[{args.worker_id}] Loading SimVLA model...", flush=True)
    print(f"[{args.worker_id}] simvla_checkpoint={ckpt_override or 'LOAD_SIMVLA_DEFAULT'}", flush=True)
    load_kwargs = {}
    if ckpt_override:
        load_kwargs["ckpt"] = Path(ckpt_override)
    if smolvlm_override:
        load_kwargs["smolvlm"] = Path(smolvlm_override)
    if norm_stats_override:
        load_kwargs["norm_stats"] = Path(norm_stats_override)
    model, proc, device = load_simvla(**load_kwargs)
    print(f"[{args.worker_id}] SimVLA model loaded on {device}.", flush=True)

    print(f"[{args.worker_id}] Creating environment for {suite}_t{task_id}...", flush=True)
    env, bundle = make_env(suite, task_id, resolution=128, seed=7)
    init_states = bundle["init_states"]
    lang = bundle["task"].language
    print(f"[{args.worker_id}] BDDL task prompt: '{lang}'", flush=True)
    print(
        f"[{args.worker_id}] Running baseline episodes [{args.episode_start}, {args.episode_end}) "
        f"with risk-aware main seeds reused where available.",
        flush=True,
    )

    attempted = 0
    successes = 0

    try:
        for ep_idx in range(args.episode_start, args.episode_end):
            reset_seed = int(seeds[ep_idx % len(seeds)])
            random.seed(reset_seed)
            np.random.seed(reset_seed)
            torch.manual_seed(reset_seed)

            print(f"[{args.worker_id}] --- Starting Episode {ep_idx} (Reset Seed {reset_seed}) ---", flush=True)
            start = time.time()
            obs = reset_to_init(env, init_states[ep_idx % len(init_states)], warmup=10)

            success = False
            step_count = 0
            error_msg = ""
            fallback_count = 0
            trace_available = len(seed_trace.get(reset_seed, []))

            try:
                for t in range(max_steps):
                    step_count += 1
                    trace_for_episode = seed_trace.get(reset_seed, [])
                    if t < len(trace_for_episode):
                        chunk_seed = int(trace_for_episode[t])
                        seed_source = "riskaware_main_action_seed"
                    else:
                        chunk_seed = fallback_action_seed(reset_seed, ep_idx, t)
                        seed_source = "deterministic_fallback_after_trace_end"
                        fallback_count += 1

                    chunk = generate_chunk(model, proc, lang, obs, seed=chunk_seed, device=device, steps=10)
                    act = chunk[0].astype(np.float32)
                    obs, rew, done, _info = env.step(act)

                    append_jsonl_locked(
                        seed_log_path,
                        {
                            "episode_index": ep_idx,
                            "reset_seed": reset_seed,
                            "timestep": t,
                            "main_action_seed": chunk_seed,
                            "seed_source": seed_source,
                        },
                    )

                    success = success or bool(rew > 0)
                    if done or success:
                        break
            except Exception as exc:
                error_msg = repr(exc)
                print(f"[{args.worker_id}] Error in episode {ep_idx}: {error_msg}", flush=True)

            wall = time.time() - start
            outcome = "success" if success else "failure_or_timeout"
            attempted += 1
            successes += int(success)
            summary = {
                "episode_index": ep_idx,
                "worker_id": args.worker_id,
                "suite": suite,
                "task_id": task_id,
                "reset_seed": reset_seed,
                "outcome": outcome,
                "success": success,
                "num_steps": step_count,
                "wall_time_seconds": wall,
                "error_message": error_msg,
                "riskaware_seed_trace_rows_available": trace_available,
                "fallback_main_action_seed_count": fallback_count,
                "baseline_policy": "simvla_first_action_only_reuse_riskaware_main_seed_v2",
                "simvla_checkpoint": str(ckpt_override or "LOAD_SIMVLA_DEFAULT"),
                "ace_used": False,
                "risk_model_used": False,
                "actions_modified": False,
            }
            append_jsonl_locked(summary_path, summary)
            write_live_status(live_path, args.worker_id, attempted, successes, ep_idx)
            print(
                f"[{args.worker_id}] Episode {ep_idx} finished. Steps: {step_count}. "
                f"Outcome: {outcome}. Fallback seeds: {fallback_count}. Time: {wall:.1f}s",
                flush=True,
            )
    finally:
        env.close()

    print(f"[{args.worker_id}] Baseline same-seed worker completed.", flush=True)


if __name__ == "__main__":
    main()
