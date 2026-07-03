#!/usr/bin/env python3
"""
SimVLA TDQC Data Collection Client

Connects to serve_tdqc_collection.py, runs LIBERO rollouts, 
and saves TDQC-ready datasets (phi sequence + success label).
"""

import argparse
import collections
import json
import math
import os
import sys
import time
from pathlib import Path
from typing import Deque, Dict, List, Optional

import imageio
import numpy as np
import torch
from tqdm import tqdm
import websockets

try:
    import msgpack
    import msgpack_numpy
    HAS_MSGPACK = True
except ImportError:
    HAS_MSGPACK = False

# Add project root to path
ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from phase2_tdqc.tdqc_features import TDQCFeatureConfig, aggregate_uncertainty_features
from phase2_tdqc.tdqc_dataset import TDQCEpisode

from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
LIBERO_ENV_RESOLUTION = 256
NUM_STEPS_WAIT = 10

MAX_STEPS = {
    "libero_spatial": 800,
    "libero_object": 800,
    "libero_goal": 800,
    "libero_10": 900,
    "libero_90": 900,
}

benchmark_dict = benchmark.get_benchmark_dict()

def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
    if quat[3] > 1.0: quat[3] = 1.0
    elif quat[3] < -1.0: quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0): return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den

# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------

class TDQCWebSocketClient:
    def __init__(self, host: str, port: int, replan_steps: int = 5):
        self.uri = f"ws://{host}:{port}"
        self.replan_steps = replan_steps
        self.ws = None
        self.action_plan: Deque[np.ndarray] = collections.deque()
        self.feature_plan: Deque[torch.Tensor] = collections.deque()

    async def connect(self):
        self.ws = await websockets.connect(self.uri, max_size=None)
        # Read metadata
        msg = await self.ws.recv()
        if HAS_MSGPACK:
            meta = msgpack_numpy.unpackb(msg, raw=False)
        else:
            meta = json.loads(msg)
        print(f"Connected to server: {meta}")

    def reset(self):
        self.action_plan.clear()
        self.feature_plan.clear()

    async def step(self, obs: Dict, goal: str, feature_cfg: TDQCFeatureConfig):
        if not self.action_plan:
            element = {
                "observation/image": obs["image"],
                "observation/wrist_image": obs["wrist_image"],
                "observation/state": obs["state"],
                "prompt": goal,
            }
            
            if HAS_MSGPACK:
                await self.ws.send(msgpack_numpy.packb(element, use_bin_type=True))
                resp = await self.ws.recv()
                result = msgpack_numpy.unpackb(resp, raw=False)
            else:
                await self.ws.send(json.dumps(element))
                resp = await self.ws.recv()
                result = json.loads(resp)
            
            actions = np.array(result["actions"])
            path_var = torch.tensor(result["path_variance"])
            last_var = torch.tensor(result["last_step_variance"])
            
            # Aggregate features for the whole chunk (B=1, H, D)
            phi = aggregate_uncertainty_features(path_var, last_var, feature_cfg)
            
            for i in range(min(self.replan_steps, len(actions))):
                self.action_plan.append(actions[i])
                # In TDQC collection, we assign the SAME uncertainty feature to every
                # step of the replan block. This matches deployment logic where
                # uncertainty is computed every replan_steps.
                self.feature_plan.append(phi)

        return self.action_plan.popleft(), self.feature_plan.popleft()

# -----------------------------------------------------------------------------
# Collection Loop
# -----------------------------------------------------------------------------

async def run_collection(args):
    feature_cfg = TDQCFeatureConfig(horizon_decay=args.horizon_decay)
    client = TDQCWebSocketClient(args.host, args.port, replan_steps=args.replan_steps)
    await client.connect()
    
    task_suite = benchmark_dict[args.task_suite]()
    max_steps = MAX_STEPS.get(args.task_suite, 800)
    
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    episodes: List[Dict] = []
    if output_path.exists():
        print(f"Loading existing episodes from {output_path}")
        try:
            checkpoint = torch.load(output_path, map_location="cpu")
            episodes = checkpoint.get("episodes", [])
            print(f"Resuming from {len(episodes)} episodes.")
        except Exception as e:
            print(f"Failed to load checkpoint: {e}. Starting from scratch.")

    total_success = sum(e["success"] for e in episodes)
    
    # Selection of tasks
    task_ids = [args.task_id] if args.task_id != -1 else range(task_suite.n_tasks)
    
    for tid in task_ids:
        # Skip tasks already completed (if tid matches previously saved ones)
        # For now, simplest resume: check if we already have num_rollouts for this tid
        done_for_this_task = [e for e in episodes if e["task_id"] == tid]
        start_idx = len(done_for_this_task)
        
        if start_idx >= args.num_rollouts:
            print(f"Task {tid} already finished ({start_idx} rollouts). Skipping.")
            continue

        task = task_suite.get_task(tid)
        init_states = task_suite.get_task_init_states(tid)
        task_desc = task.language
        
        bddl = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
        env = OffScreenRenderEnv(bddl_file_name=str(bddl), camera_heights=LIBERO_ENV_RESOLUTION, camera_widths=LIBERO_ENV_RESOLUTION)
        env.seed(args.seed)
        
        print(f"\nCollecting Task {tid}: {task_desc}")
        
        for ep_idx in tqdm(range(start_idx, args.num_rollouts), desc=f"Task {tid}"):
            env.reset()
            client.reset()
            obs = env.set_init_state(init_states[ep_idx % len(init_states)])
            
            features_history = []
            t = 0
            done = False
            
            while t < max_steps + NUM_STEPS_WAIT:
                if t < NUM_STEPS_WAIT:
                    obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
                    t += 1
                    continue
                
                img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
                wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
                state = np.concatenate([
                    obs["robot0_eef_pos"],
                    _quat2axisangle(obs["robot0_eef_quat"]),
                    obs["robot0_gripper_qpos"],
                ])
                
                action, phi = await client.step({"image": img, "wrist_image": wrist_img, "state": state}, task_desc, feature_cfg)
                
                features_history.append(phi)
                obs, reward, done, info = env.step(action.tolist())
                
                if done:
                    total_success += 1
                    break
                t += 1
            
            episodes.append({
                "features": torch.stack(features_history),
                "success": int(done),
                "task_id": tid,
                "episode_idx": ep_idx,
                "instruction": task_desc,
            })
            
            # Atomic save to prevent corruption
            tmp_path = str(output_path) + ".tmp"
            torch.save({"episodes": episodes}, tmp_path)
            os.replace(tmp_path, output_path)
            
            print(f" [SAVE] Episode {ep_idx} (Task {tid}) saved. Success: {done}. Total: {len(episodes)}")
        
        env.close()
    
    torch.save({"episodes": episodes}, output_path)
    print(f"\nCollection Finished. Saved {len(episodes)} rollouts to {output_path}")
    print(f"Total success rate: {total_success}/{len(episodes)} ({total_success/len(episodes)*100:.1f}%)")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8001)
    parser.add_argument("--task_suite", default="libero_spatial")
    parser.add_argument("--task_id", type=int, default=5) # Default to Task 5
    parser.add_argument("--num_rollouts", type=int, default=100)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--replan_steps", type=int, default=5)
    parser.add_argument("--horizon_decay", type=float, default=0.8)
    parser.add_argument("--output_path", required=True)
    args = parser.parse_args()
    
    import asyncio
    asyncio.run(run_collection(args))

if __name__ == "__main__":
    main()
