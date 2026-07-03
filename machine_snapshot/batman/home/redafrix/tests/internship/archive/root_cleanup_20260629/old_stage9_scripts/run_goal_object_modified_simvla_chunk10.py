#!/usr/bin/env python3
import os
import sys
import argparse
import json
import time
import hashlib
import csv
import random
import re
from pathlib import Path
import numpy as np
import torch
from tqdm import tqdm

# Constants
TRASH_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_modified_simvla_chunk10_100_20260605")
REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
FIPER_ROOT = REDA_WS / "fiper_ws"
SIMVLA_SRC = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
LIBERO_PRO_SRC = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"
ASYNCHVLA_SRC = REDA_WS / "asynchvla_ws/src"
CHECKPOINT_PATH = FIPER_ROOT / "checkpoints/simvla_libero_uncertainty/ckpt-60000"
NORM_STATS_PATH = SIMVLA_SRC / "norm_stats/libero_norm.json"
SMOLVLM_CACHE = FIPER_ROOT / "realtime_deployment/smolvlm_cache"
EXPECTED_CKPT_HASH = "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71"
GLOBAL_ACTION_SEED_BASE = "2026060503"

# Setup Paths for imports
for p in [SIMVLA_SRC, LIBERO_PRO_SRC, ASYNCHVLA_SRC]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

# Monkeypatch torch.load to avoid weights_only error in newer PyTorch
orig_load = torch.load
torch.load = lambda *args, **kwargs: orig_load(*args, **{**kwargs, "weights_only": False})

try:
    from data_collection_stage9.libero_pro_env_utils import obs_images, obs_to_proprio
    from data_collection_stage9.simvla_candidate_sampler import load_simvla, sample_candidate
    try:
        from libero.envs import OffScreenRenderEnv
    except ImportError:
        from libero.libero.envs import OffScreenRenderEnv
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_deterministic_action_seed(uid, policy_timestep, chunk_index):
    hash_input = f"{GLOBAL_ACTION_SEED_BASE}|{uid}|{policy_timestep}|{chunk_index}".encode()
    h = hashlib.sha256(hash_input).hexdigest()
    return int(h[:8], 16) % (2**31)

def parse_bddl_instruction(bddl_path):
    with open(bddl_path, "r") as f:
        content = f.read()
    match = re.search(r"\(:language\s+(.*?)\)", content, re.DOTALL)
    if match:
        raw = match.group(1).strip()
        # Handle quoted strings and potential newlines
        if raw.startswith('"') and raw.endswith('"'):
            return raw[1:-1].strip()
        return raw
    return ""

def make_exact_env(bddl_path):
    env = OffScreenRenderEnv(
        bddl_file_name=str(bddl_path),
        camera_heights=128,
        camera_widths=128
    )
    return env

def append_jsonl(path, data):
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["smoke", "production"], required=True)
    args = parser.parse_args()

    # Metadata & Hash Verification
    ckpt_file = CHECKPOINT_PATH / "model.safetensors"
    actual_ckpt_hash = get_sha256(ckpt_file)
    print(f"Resolved checkpoint path: {CHECKPOINT_PATH}")
    print(f"Checkpoint SHA-256: {actual_ckpt_hash}")
    if actual_ckpt_hash != EXPECTED_CKPT_HASH:
        print(f"FATAL: Checkpoint hash mismatch! Expected {EXPECTED_CKPT_HASH}, got {actual_ckpt_hash}")
        sys.exit(1)

    # Output paths
    base_dir = TRASH_ROOT / args.mode
    base_dir.mkdir(parents=True, exist_ok=True)
    summaries_path = base_dir / "episode_summaries.jsonl"
    events_path = base_dir / "chunk_events.jsonl"
    
    # Load SimVLA
    print("Loading SimVLA...", flush=True)
    model, proc, device = load_simvla(
        ckpt=str(CHECKPOINT_PATH),
        norm_stats=str(NORM_STATS_PATH),
        smolvlm=str(SMOLVLM_CACHE)
    )
    
    # Print Metadata
    print(f"predict_uncertainty: {getattr(model, 'predict_uncertainty', 'N/A')}")
    print(f"action_horizon: {getattr(model, 'action_horizon', 'N/A')}")
    print(f"model dtype: {next(model.parameters()).dtype}")
    print(f"normalization path: {NORM_STATS_PATH}")
    print(f"SimVLA source path: {SIMVLA_SRC}")
    print(f"LIBERO-PRO source path: {LIBERO_PRO_SRC}")

    # Load Manifest
    manifest_path = TRASH_ROOT / "bundle/verification/episode_identity_table.csv"
    with open(manifest_path, "r") as f:
        reader = csv.DictReader(f)
        manifest = list(reader)

    if args.mode == "smoke":
        manifest = manifest[:1]
        max_steps = 13
        print("Running SMOKE test (1 episode, 13 steps max)")
    else:
        manifest = manifest[:100]
        max_steps = 250
        print(f"Running PRODUCTION test ({len(manifest)} episodes, 250 steps max)")

    # Resumability
    completed_uids = set()
    if summaries_path.exists():
        with open(summaries_path, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        completed_uids.add(json.loads(line)["episode_uid"])
                    except: pass

    all_action_seeds = set()

    for idx, row in enumerate(manifest):
        uid = f"{row['run_id']}_task{row['task_id']}_init{row['initial_state_index']}"
        if uid in completed_uids:
            print(f"Skipping completed episode: {uid}")
            continue

        print(f"\n--- Episode {idx} UID: {uid} ---", flush=True)
        
        # Verify hashes
        bddl_path = TRASH_ROOT / "bundle" / row['bddl_relative_path']
        init_path = TRASH_ROOT / "bundle" / row['init_state_file_relative_path']
        
        bddl_hash = get_sha256(bddl_path)
        init_hash = get_sha256(init_path)
        
        assert bddl_hash == row['bddl_sha256'], f"BDDL hash mismatch for {uid}"
        assert init_hash == row['init_state_file_sha256'], f"Init hash mismatch for {uid}"

        instruction = parse_bddl_instruction(bddl_path)
        print(f"Instruction: {instruction}")

        # Seed everything
        eval_seed = int(row['eval_seed'])
        random.seed(eval_seed)
        np.random.seed(eval_seed)
        torch.manual_seed(eval_seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(eval_seed)

        # Create Env
        env = make_exact_env(bddl_path)
        env.seed(eval_seed)
        
        # Load init states
        init_states = torch.load(init_path, map_location="cpu", weights_only=False)
        initial_state_index = int(row['initial_state_index'])
        
        # Reset and Warmup
        obs = env.reset()
        env.set_init_state(init_states[initial_state_index])
        # Warmup: 10 actions [0,0,0,0,0,0,-1]
        for _ in range(10):
            obs, _, _, _ = env.step(np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float32))

        success = False
        policy_step = 0
        chunk_idx = 0
        error_msg = ""
        start_time = time.time()
        done = False

        try:
            while policy_step < max_steps and not success and not done:
                action_seed = get_deterministic_action_seed(uid, policy_step, chunk_idx)
                if action_seed in all_action_seeds:
                    raise RuntimeError(f"Action seed collision: {action_seed}")
                all_action_seeds.add(action_seed)

                # Generate Chunk
                img, wrist = obs_images(obs)
                prop = obs_to_proprio(obs)
                
                # sample_candidate expects seed as int
                cand = sample_candidate(model, proc, instruction, img, wrist, prop, seed=int(action_seed), device=device, steps=10, flowtrace=False)
                
                chunk_env = cand['candidate_action_env'].numpy() # 10x7
                chunk_norm = cand['candidate_action_normalized'].numpy()
                
                assert chunk_env.shape == (10, 7), f"Expected (10,7) chunk, got {chunk_env.shape}"
                
                rewards = []
                chunk_dones = []
                chunk_successes = []
                actions_executed = 0
                
                policy_step_before = policy_step

                for i in range(10):
                    act = chunk_env[i].astype(np.float32)
                    obs, rew, done, info = env.step(act)
                    policy_step += 1
                    actions_executed += 1
                    
                    # Success semantics
                    is_success = bool(rew > 0)
                    if hasattr(env, "_check_success"):
                        is_success = is_success or env._check_success()
                    
                    rewards.append(float(rew))
                    chunk_dones.append(bool(done))
                    chunk_successes.append(is_success)
                    
                    if is_success or done:
                        success = is_success
                        break
                    
                    if policy_step >= max_steps:
                        break
                
                append_jsonl(events_path, {
                    "episode_uid": uid,
                    "task_id": int(row['task_id']),
                    "init_state_index": initial_state_index,
                    "chunk_index": chunk_idx,
                    "policy_timestep_before": policy_step_before,
                    "action_seed": int(action_seed),
                    "chunk_shape": list(chunk_env.shape),
                    "full_denormalized_chunk": chunk_env.tolist(),
                    "full_normalized_chunk": chunk_norm.tolist(),
                    "actions_executed": actions_executed,
                    "rewards": rewards,
                    "dones": chunk_dones,
                    "successes": chunk_successes,
                    "policy_timestep_after": policy_step
                })
                
                if success or done or policy_step >= max_steps:
                    break
                chunk_idx += 1

        except Exception as e:
            import traceback
            error_msg = str(e)
            print(f"Error in episode {uid}: {error_msg}")
            traceback.print_exc()

        wall_time = time.time() - start_time
        append_jsonl(summaries_path, {
            "manifest_row_index": idx,
            "episode_uid": uid,
            "run_id": row['run_id'],
            "task_id": int(row['task_id']),
            "initial_state_index": initial_state_index,
            "evaluation_seed": eval_seed,
            "bddl_path": str(row['bddl_relative_path']),
            "bddl_hash": bddl_hash,
            "init_state_path": str(row['init_state_file_relative_path']),
            "init_state_hash": init_hash,
            "instruction": instruction,
            "success": success,
            "outcome": "success" if success else "failure",
            "terminal_done": bool(done),
            "policy_environment_steps": policy_step,
            "num_chunk_queries": chunk_idx + 1 if not error_msg else chunk_idx,
            "wall_time": wall_time,
            "error_message": error_msg,
            "checkpoint_path": str(CHECKPOINT_PATH),
            "checkpoint_hash": actual_ckpt_hash
        })
        
        print(f"Finished episode {uid}. Success: {success}, Steps: {policy_step}, Time: {wall_time:.1f}s")
        env.close()
        if args.mode == "smoke" and idx == 0:
            break

if __name__ == "__main__":
    main()
