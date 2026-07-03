#!/usr/bin/env python3
import os
import sys
import argparse
import json
import random
import time
import fcntl
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
    print(f"Import error: {e}. Trying local imports.")
    sys.path.append(str(Path(__file__).parent.parent.parent / "scripts"))
    from libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from simvla_candidate_sampler import load_simvla, sample_candidate

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
        
        # Read all entries from summaries file to compute overall totals
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

def append_episode_summary(summaries_path, summary_data):
    lock_file = open(summaries_path.parent / "summaries.lock", "w")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        with open(summaries_path, "a") as f:
            f.write(json.dumps(summary_data) + "\n")
    finally:
        fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()

def write_final_summary(out_dir):
    summaries_path = out_dir / "episode_summaries.jsonl"
    if not summaries_path.exists():
        return
    episodes = []
    with open(summaries_path, "r") as f:
        for line in f:
            if line.strip():
                try:
                    episodes.append(json.loads(line))
                except Exception:
                    pass
    successes = sum(1 for ep in episodes if ep.get("success", False))
    total = len(episodes)
    final_data = {
        "total_episodes": total,
        "successes": successes,
        "failures": total - successes,
        "success_rate": successes / total if total > 0 else 0.0,
        "episodes": episodes
    }
    (out_dir / "final_summary.json").write_text(json.dumps(final_data, indent=2) + "\n")

def generate_markdown_report(report_path, out_dir, suite, task_id):
    final_summary_path = out_dir / "final_summary.json"
    if not final_summary_path.exists():
        return
    final_data = json.loads(final_summary_path.read_text())
    total = final_data["total_episodes"]
    successes = final_data["successes"]
    failures = final_data["failures"]
    rate = final_data["success_rate"]
    
    steps = [ep["num_steps"] for ep in final_data["episodes"] if "num_steps" in ep]
    avg_steps = np.mean(steps) if steps else 0.0
    max_steps = np.max(steps) if steps else 0
    min_steps = np.min(steps) if steps else 0
    
    times = [ep["wall_time_seconds"] for ep in final_data["episodes"] if "wall_time_seconds" in ep]
    avg_time = np.mean(times) if times else 0.0
    
    lines = [
        f"# Baseline SimVLA Rollout Report - {suite} Task {task_id}",
        "",
        "This report summarizes the performance of the baseline SimVLA-only policy on the specified task.",
        "",
        "## 1. Metrics Summary",
        "",
        f"- **Suite:** `{suite}`",
        f"- **Task ID:** `{task_id}`",
        f"- **Total Episodes Run:** {total}",
        f"- **Successes:** {successes}",
        f"- **Failures/Timeouts:** {failures}",
        f"- **Success Rate:** {rate:.2%}",
        f"- **Average Steps per Episode:** {avg_steps:.2f} (min: {min_steps}, max: {max_steps})",
        f"- **Average Wall Time per Episode:** {avg_time:.2f} seconds",
        "",
        "## 2. Config & System Information",
        "",
        "- **Policy:** `receding_horizon_execute_first_action_only` (SimVLA baseline only, no FIPER, no ACE)",
        "- **Device:** `cuda`",
        "- **Max Steps limit:** 300",
        "",
        "## 3. Detailed Episode Log",
        "",
        "| Episode Index | Reset Seed | Success | Steps | Wall Time (s) |",
        "|---|---|---|---|---|",
    ]
    for ep in sorted(final_data["episodes"], key=lambda x: x.get("episode_index", 0)):
        lines.append(
            f"| {ep.get('episode_index')} | {ep.get('reset_seed')} | {ep.get('success')} | {ep.get('num_steps')} | {ep.get('wall_time_seconds'):.1f} |"
        )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote report to {report_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to config file")
    parser.add_argument("--num-episodes", type=int, help="Override target episode count")
    parser.add_argument("--worker-id", required=True, help="Unique worker name")
    parser.add_argument("--episode-start", type=int, required=True, help="Starting episode index (inclusive)")
    parser.add_argument("--episode-end", type=int, required=True, help="Ending episode index (exclusive)")
    args = parser.parse_args()

    # Load config
    config = json.loads(Path(args.config).read_text())
    suite = config["suite"]
    task_id = config["task_id"]
    max_steps = config.get("max_steps", 300)
    seeds = config["seeds"]
    
    out_dir = Path(config["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "logs").mkdir(parents=True, exist_ok=True)
    
    status_path = out_dir / "live_status.json"
    summaries_path = out_dir / "episode_summaries.jsonl"
    
    # Load SimVLA
    print(f"[{args.worker_id}] Loading SimVLA model...", flush=True)
    model, proc, device = load_simvla()
    print(f"[{args.worker_id}] SimVLA model loaded on {device}.", flush=True)
    
    # Create environment
    print(f"[{args.worker_id}] Creating environment for {suite}_t{task_id}...", flush=True)
    env, bundle = make_env(suite, task_id, resolution=128, seed=7)
    init_states = bundle["init_states"]
    lang = bundle["task"].language
    print(f"[{args.worker_id}] BDDL task prompt: '{lang}'", flush=True)
    
    episode_indices = list(range(args.episode_start, args.episode_end))
    if args.num_episodes is not None:
        episode_indices = episode_indices[:args.num_episodes]
        
    print(f"[{args.worker_id}] Worker running episodes {episode_indices} (total {len(episode_indices)})", flush=True)
    
    for ep_idx in episode_indices:
        reset_seed = seeds[ep_idx % len(seeds)]
        print(f"[{args.worker_id}] --- Starting Episode {ep_idx} (Reset Seed {reset_seed}) ---", flush=True)
        
        # Set seeds
        random.seed(reset_seed)
        np.random.seed(reset_seed)
        torch.manual_seed(reset_seed)
        
        start_time = time.time()
        
        # Reset env
        init_state_to_use = init_states[ep_idx % len(init_states)]
        obs = reset_to_init(env, init_state_to_use, warmup=10)
        
        success = False
        step_count = 0
        error_msg = ""
        
        try:
            for t in range(max_steps):
                step_count += 1
                
                # Sample chunk
                chunk_seed = random.randint(0, 2**31 - 1)
                main_chunk, _ = generate_chunk(model, proc, lang, obs, seed=chunk_seed, device=device, steps=10)
                
                # Execute only the first action
                act = main_chunk[0].astype(np.float32)
                obs, rew, done, info = env.step(act)
                
                success = success or bool(rew > 0)
                if done or success:
                    break
        except Exception as exc:
            error_msg = repr(exc)
            print(f"[{args.worker_id}] Error in episode {ep_idx}: {error_msg}", flush=True)
            
        wall_time = time.time() - start_time
        outcome = "success" if success else "failure_or_timeout"
        
        # Log episode info
        ep_summary = {
            "episode_index": ep_idx,
            "suite": suite,
            "task_id": task_id,
            "reset_seed": reset_seed,
            "outcome": outcome,
            "success": success,
            "num_steps": step_count,
            "wall_time_seconds": wall_time,
            "error_message": error_msg
        }
        
        append_episode_summary(summaries_path, ep_summary)
        update_live_status(status_path, args.worker_id, ep_idx, success)
        
        print(f"[{args.worker_id}] Episode {ep_idx} finished. Steps: {step_count}. Outcome: {outcome}. Time: {wall_time:.1f}s", flush=True)

    env.close()
    print(f"[{args.worker_id}] Worker completed.", flush=True)
    
    # Write final summaries
    write_final_summary(out_dir)
    report_path = Path("realtime_deployment/reports/BASELINE_SIMVLA_LIBERO10_MILK_TASK7_SAM_V1_REPORT.md")
    generate_markdown_report(report_path, out_dir, suite, task_id)

if __name__ == "__main__":
    main()
