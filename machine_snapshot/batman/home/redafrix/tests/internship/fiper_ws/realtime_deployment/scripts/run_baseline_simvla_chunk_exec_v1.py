#!/usr/bin/env python3
import os
import sys
import argparse
import json
import random
import time
import fcntl
import hashlib
from pathlib import Path
import numpy as np
import torch

# Set up paths for imports
REDA_WS = Path(os.environ.get("REDA_WS", "/home/rootalkhatib/test/reda_ws"))
os.environ["REDA_WS"] = str(REDA_WS)

# Include directories needed in PYTHONPATH
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
except ImportError as e:
    sys.path.append(str(Path(__file__).parent.parent.parent / "scripts"))
    from libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from simvla_candidate_sampler import load_simvla, sample_candidate

def get_action_seed(global_action_seed: int, reset_seed: int, episode_index: int, chunk_index: int, sample_index: int) -> int:
    hash_input = f"{global_action_seed}_{reset_seed}_{episode_index}_{chunk_index}_{sample_index}".encode()
    h = hashlib.sha256(hash_input).hexdigest()
    return int(h[:8], 16) % (2**31)

def generate_chunk(model, proc, lang, obs, seed: int, device, steps: int = 10):
    img, wrist = obs_images(obs)
    prop = obs_to_proprio(obs)
    cand = sample_candidate(model, proc, lang, img, wrist, prop, seed=seed, device=device, steps=steps, flowtrace=False)
    chunk = cand['candidate_action_env'].numpy().astype(np.float32)
    norm = cand['candidate_action_normalized'].numpy().astype(np.float32)
    return chunk, norm

def update_live_status(status_path, worker_id, episode_idx, success):
    lock_file = open(status_path.parent / "live_status.lock", "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        status = {}
        if status_path.exists():
            try:
                status = json.loads(status_path.read_text())
            except Exception:
                status = {}
        if "workers" not in status:
            status["workers"] = {}
        status["workers"][worker_id] = {
            "last_episode_idx": episode_idx,
            "success": success,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        summaries_path = status_path.parent / "episode_summaries.jsonl"
        successes = 0
        total = 0
        if summaries_path.exists():
            with open(summaries_path, "r") as f:
                for line in f:
                    if line.strip():
                        try:
                            data = json.loads(line)
                            total += 1
                            if data.get("success", False):
                                successes += 1
                        except Exception:
                            pass
        status["total_episodes_attempted"] = total
        status["total_successes"] = successes
        status["total_failures"] = total - successes
        status["success_rate"] = successes / total if total > 0 else 0.0
        status["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        status_path.write_text(json.dumps(status, indent=2) + "\n")
    finally:
        fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()

def append_jsonl(path, data):
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--num-episodes", type=int)
    parser.add_argument("--worker-id", required=True)
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text())
    suite = config["suite"]
    task_id = config["task_id"]
    max_steps = config.get("max_steps", 300)
    seeds = config["seeds"]
    global_action_seed = config.get("global_action_seed", 424242)
    
    out_dir = Path(config["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    status_path = out_dir / "live_status.json"
    summaries_path = out_dir / "episode_summaries.jsonl"
    events_path = out_dir / "chunk_events.jsonl"
    
    print(f"[{args.worker_id}] Loading SimVLA model...", flush=True)
    model, proc, device = load_simvla()
    print(f"[{args.worker_id}] Creating environment...", flush=True)
    env, bundle = make_env(suite, task_id, resolution=128, seed=7)
    init_states = bundle["init_states"]
    lang = bundle["task"].language
    
    num_episodes = args.num_episodes if args.num_episodes is not None else len(seeds)
    
    for ep_idx in range(num_episodes):
        reset_seed = seeds[ep_idx % len(seeds)]
        print(f"[{args.worker_id}] --- Episode {ep_idx} (Seed {reset_seed}) ---", flush=True)
        
        random.seed(reset_seed)
        np.random.seed(reset_seed)
        torch.manual_seed(reset_seed)
        
        init_state = init_states[ep_idx % len(init_states)]
        obs = reset_to_init(env, init_state, warmup=10)
        
        start_time = time.time()
        success = False
        step_count = 0
        num_chunk_queries = 0
        error_msg = ""
        
        try:
            while step_count < max_steps and not success:
                num_chunk_queries += 1
                env_step_start = step_count
                chunk_index = num_chunk_queries - 1
                
                chunk_seed = get_action_seed(global_action_seed, reset_seed, ep_idx, chunk_index, 0)
                main_chunk, _ = generate_chunk(model, proc, lang, obs, seed=chunk_seed, device=device, steps=10)
                
                actions_executed = 0
                for i in range(len(main_chunk)):
                    step_count += 1
                    actions_executed += 1
                    act = main_chunk[i].astype(np.float32)
                    obs, rew, done, info = env.step(act)
                    success = success or bool(rew > 0)
                    if done or success:
                        break
                
                append_jsonl(events_path, {
                    "episode_index": ep_idx,
                    "reset_seed": reset_seed,
                    "chunk_index": chunk_index,
                    "env_step_start": env_step_start,
                    "main_action_seed": int(chunk_seed),
                    "actions_executed_from_chunk": actions_executed,
                    "success_after_chunk": bool(success),
                    "done_after_chunk": bool(done)
                })
                if done or success:
                    break
        except Exception as exc:
            error_msg = repr(exc)
            print(f"[{args.worker_id}] Error: {error_msg}")
            
        wall_time = time.time() - start_time
        append_jsonl(summaries_path, {
            "episode_index": ep_idx,
            "reset_seed": reset_seed,
            "outcome": "success" if success else "failure",
            "success": bool(success),
            "num_steps": step_count,
            "num_chunk_queries": num_chunk_queries,
            "wall_time_seconds": wall_time,
            "error_message": error_msg
        })
        update_live_status(status_path, args.worker_id, ep_idx, success)
        print(f"[{args.worker_id}] Result: {'Success' if success else 'Failure'}, Steps: {step_count}, Time: {wall_time:.1f}s")

    env.close()

if __name__ == "__main__":
    main()
