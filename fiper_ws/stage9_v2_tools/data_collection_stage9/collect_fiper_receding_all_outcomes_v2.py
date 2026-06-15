from __future__ import annotations

import os
import sys
from pathlib import Path

# SET UP ENVIRONMENT BEFORE ANY OTHER IMPORTS
REDA_WS = Path(os.environ.get("REDA_WS", "/home/rootalkhatib/test/reda_ws"))
os.environ["REDA_WS"] = str(REDA_WS)
# For Bob/Sam, we might need different config paths, but the collector should be agnostic if possible.
# We will pass the config path or rely on the system setup.

import argparse
import json
import random
import time
from collections import Counter, defaultdict
from typing import Any

import numpy as np

# We assume these are in the PYTHONPATH or the same directory
try:
    from .history_buffer import HistoryBuffer
    from .libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from .outcome_metrics import object_body_positions
    from .sim_state_utils import get_state, save_state_npz
    from .simvla_candidate_sampler import load_simvla, sample_candidate
    from .task_parser import parse_task_context
    from .collect_outcome_advantage_dataset import git_hash, save_png
except ImportError:
    # Fallback for local execution/testing if not in package mode
    from history_buffer import HistoryBuffer
    from libero_pro_env_utils import (
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
    )
    from outcome_metrics import object_body_positions
    from sim_state_utils import get_state, save_state_npz
    from simvla_candidate_sampler import load_simvla, sample_candidate
    from task_parser import parse_task_context
    from collect_outcome_advantage_dataset import git_hash, save_png


def generate_chunk(model, proc, lang, obs, seed: int, device, steps: int):
    """
    Sample a candidate action chunk from SimVLA without environment interaction.
    """
    img, wrist = obs_images(obs)
    prop = obs_to_proprio(obs)
    cand = sample_candidate(model, proc, lang, img, wrist, prop, seed=seed, device=device, steps=steps, flowtrace=False)
    chunk = cand['candidate_action_env'].numpy().astype(np.float32)
    norm = cand['candidate_action_normalized'].numpy().astype(np.float32)
    return chunk, norm


def collect(args: argparse.Namespace) -> None:
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "states").mkdir(exist_ok=True)
    (outdir / "images").mkdir(exist_ok=True)
    
    model, proc, device = load_simvla()
    code_version = git_hash()
    
    total_samples = 0
    outcome_counts = Counter()
    episodes_per_task = defaultdict(int)
    
    # BROAD SWEEP STRATEGY: 
    # Iterate over sweeps first, then suites, then tasks.
    # This ensures high diversity across the entire dataset from the start.
    
    print(f"FIPER Sweep Collector v2 started. Sweeps: {args.num_sweeps}, ACE: {args.ace_candidates}, MaxSteps: {args.max_timesteps}", flush=True)

    for sweep_idx in range(args.num_sweeps):
        print(f"\n--- Starting Sweep {sweep_idx} ---", flush=True)
        for suite in args.suites:
            for task_id in args.task_ids:
                try:
                    # Instantiate env for each task to ensure clean state and avoid registration issues
                    env, bundle = make_env(suite, task_id, args.resolution, seed=args.env_seed)
                except Exception as exc:
                    print(f"Skipping unavailable {suite}_t{task_id}: {exc}", flush=True)
                    continue

                init_states = bundle["init_states"]
                lang = bundle["task"].language
                all_bodies = list(object_body_positions(env).keys())
                
                rollout_idx = episodes_per_task[(suite, task_id)]
                print(f"  {suite}_t{task_id} Episode {rollout_idx} (Sweep {sweep_idx})...", flush=True)

                # Reset to next available init state
                obs = reset_to_init(env, init_states[rollout_idx % len(init_states)], warmup=args.warmup)
                task_context = parse_task_context(lang, obs, all_bodies=all_bodies)
                hist = HistoryBuffer(args.history_k)
                
                episode_rows = []
                success = False
                
                for t in range(args.max_timesteps):
                    # 1. Capture current state
                    state = get_state(env)
                    prop = obs_to_proprio(obs)
                    before_obj = object_body_positions(env)
                    
                    state_id = f"{suite}_t{task_id}_r{rollout_idx}_s{t}_state"
                    state_path = save_state_npz(outdir / "states" / f"{state_id}.npz", state)
                    
                    before_img, before_wrist = obs_images(obs)
                    before_agent_path = save_png(outdir / "images" / f"{state_id}_before_agent.png", before_img) if args.save_images else None
                    before_wrist_path = save_png(outdir / "images" / f"{state_id}_before_wrist.png", before_wrist) if args.save_images and before_wrist is not None else None
                    
                    # 2. Sample ONE main action chunk
                    main_seed = random.randint(0, 2**31 - 1)
                    main_chunk, main_norm = generate_chunk(model, proc, lang, obs, seed=main_seed, device=device, steps=10)
                    
                    # 3. NO-REPLAY ACE DESIGN (Reduced to 8 candidates per user request)
                    ace_seeds = [random.randint(0, 2**31 - 1) for _ in range(args.ace_candidates)]
                    ace_chunks_env = []
                    ace_chunks_norm = []
                    for s in ace_seeds:
                        c, n = generate_chunk(model, proc, lang, obs, seed=s, device=device, steps=10)
                        ace_chunks_env.append(c.tolist())
                        ace_chunks_norm.append(n.tolist())
                    
                    row = {
                        "episode_id": f"{suite}_t{task_id}_r{rollout_idx}",
                        "timestep": t,
                        "suite": suite,
                        "task_id": task_id,
                        "task_instruction": lang,
                        "current": {
                            "proprio": prop.tolist(),
                            "object_positions_before": before_obj,
                            "sim_state_path": state_path,
                            "before_image_path": before_agent_path,
                            "before_wrist_image_path": before_wrist_path,
                            "task_context": task_context,
                        },
                        "history": hist.to_list(),
                        "main_seed": int(main_seed),
                        "main_candidate_action_chunk_normalized": main_norm.tolist(),
                        "main_candidate_action_chunk_env": main_chunk.tolist(),
                        "executed_action": main_chunk[0].tolist(), 
                        "ace_candidate_seeds": ace_seeds,
                        "ace_candidate_chunks_normalized": ace_chunks_norm,
                        "ace_candidate_chunks_env": ace_chunks_env,
                        "metadata": {
                            "collection_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
                            "code_version": code_version,
                            "source": "libero_pro_receding_all_outcomes_v2_sweep",
                            "ace_replay_used": False,
                            "sweep_idx": sweep_idx,
                        },
                        "deployability_flags": {
                            "proprio_deployable": True,
                            "history_deployable": True,
                            "candidate_action_deployable": True,
                            "object_positions_deployable": True,
                            "sim_state_deployable": False,
                            "before_image_deployable": True,
                        }
                    }
                    episode_rows.append(row)
                    
                    # 4. EXECUTE ONLY THE FIRST ACTION
                    act = main_chunk[0].astype(np.float32)
                    obs, rew, done, info = env.step(act)
                    
                    # Update history
                    hist.append({
                        "reward": float(rew),
                        "success": bool(rew > 0),
                        "proprio": obs_to_proprio(obs).tolist(),
                        "executed_action": act.tolist()
                    })
                    
                    success = success or bool(rew > 0)
                    if done or success:
                        break
                
                # Episode outcome backfill
                outcome_str = "success" if success else "failure_or_timeout"
                outcome_counts[outcome_str] += 1
                for r in episode_rows:
                    r["episode_outcome"] = outcome_str
                    r["parent_episode_success"] = success
                    r["parent_failed_or_timeout"] = not success
                    r["allowed_use"] = "train_calib_eval_success" if success else "eval_only_failure"
                
                # Save to JSONL
                with (outdir / "fiper_receding_samples.jsonl").open("a") as f:
                    for r in episode_rows:
                        f.write(json.dumps(r) + "\n")
                
                total_samples += len(episode_rows)
                episodes_per_task[(suite, task_id)] += 1
                print(f"    Episode finished. Steps: {len(episode_rows)}. Success: {success}", flush=True)
                
                env.close()

    summary = {
        "schema_version": "stage9_fiper_receding_all_outcomes_v2_summary",
        "num_samples": total_samples,
        "outcome_counts": dict(outcome_counts),
        "out_dir": str(outdir),
        "suites": args.suites,
        "task_ids": args.task_ids,
        "num_sweeps": args.num_sweeps,
        "ace_candidates": args.ace_candidates,
    }
    (outdir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=list(range(10)))
    parser.add_argument("--num-sweeps", type=int, default=100)
    parser.add_argument("--max-timesteps", type=int, default=300)
    parser.add_argument("--ace-candidates", type=int, default=8)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--env-seed", type=int, default=7)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
