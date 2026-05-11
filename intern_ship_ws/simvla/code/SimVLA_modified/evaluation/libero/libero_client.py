import argparse
import collections
import json
import math
import os
import sys
import time
from pathlib import Path
from typing import Deque, Dict, List, Optional, Tuple, Any

import imageio
import numpy as np
import torch
from tqdm import tqdm

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv
from models.modeling_smolvlm_vla import SmolVLMVLA
try:
    from openpi_client import image_tools
    from openpi_client import websocket_client_policy as ws_client
    HAS_WS_CLIENT = True
except ImportError:
    HAS_WS_CLIENT = False

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

LIBERO_ENV_RESOLUTION = 256
LIBERO_DUMMY_ACTION = [0, 0, 0, 0, 0, 0, -1]

MAX_STEPS = {
    "libero_spatial": 800,
    "libero_object": 800,
    "libero_goal": 800,
    "libero_10": 900,
    "libero_90": 900,
}

NUM_STEPS_WAIT = 10
benchmark_dict = benchmark.get_benchmark_dict()

def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
    if quat[3] > 1.0: quat[3] = 1.0
    elif quat[3] < -1.0: quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0): return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den

def get_libero_env(task, resolution: int, seed: int):
    task_description = task.language
    task_bddl_file = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    env_args = {"bddl_file_name": str(task_bddl_file), "camera_heights": resolution, "camera_widths": resolution}
    env = OffScreenRenderEnv(**env_args)
    env.seed(seed)
    return env, task_description

class WebSocketClient:
    def __init__(self, host: str, port: int, replan_steps: int = 5, resize_size: int = 224):
        if not HAS_WS_CLIENT:
            raise ImportError("openpi_client not installed. Run: pip install openpi-client")
        self.client = ws_client.WebsocketClientPolicy(host, port)
        self.replan_steps = replan_steps
        self.resize_size = resize_size
        self.reset()

    def reset(self) -> None:
        self.action_plan: Deque[np.ndarray] = collections.deque()
        self.uncertainty_plan: Deque[Dict] = collections.deque()

    def step(self, obs: Dict, goal: str) -> Tuple[np.ndarray, Optional[Dict]]:
        if not self.action_plan:
            img = image_tools.convert_to_uint8(image_tools.resize_with_pad(obs["image"], self.resize_size, self.resize_size))
            wrist_img = image_tools.convert_to_uint8(image_tools.resize_with_pad(obs["wrist_image"], self.resize_size, self.resize_size))
            element = {"observation/image": img, "observation/wrist_image": wrist_img, "observation/state": obs["state"], "prompt": goal}
            result = self.client.infer(element)
            action_chunk = result["actions"]
            path_variance = result.get("path_variance")
            last_step_variance = result.get("last_step_variance")
            if not isinstance(action_chunk, np.ndarray): action_chunk = np.array(action_chunk)
            for i in range(min(self.replan_steps, len(action_chunk))):
                self.action_plan.append(action_chunk[i])
                step_unc = {}
                if path_variance is not None: step_unc["path_variance"] = path_variance[i]
                if last_step_variance is not None: step_unc["last_step_variance"] = last_step_variance
                self.uncertainty_plan.append(step_unc)
        return self.action_plan.popleft(), self.uncertainty_plan.popleft()

def main():
    parser = argparse.ArgumentParser("LIBERO Evaluation Client")
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--task_suite", type=str, default="libero_spatial")
    parser.add_argument("--task_id", type=int, default=0)
    parser.add_argument("--num_trials", type=int, default=1)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--video_out", type=str, default="./eval_results")
    parser.add_argument("--no_video", action="store_true")
    parser.add_argument("--max_steps_override", type=int, default=None)
    args = parser.parse_args()

    client = WebSocketClient(args.host, args.port)
    task_suite = benchmark_dict[args.task_suite]()
    task = task_suite.get_task(args.task_id)
    initial_states = task_suite.get_task_init_states(args.task_id)
    env, task_description = get_libero_env(task, LIBERO_ENV_RESOLUTION, args.seed)
    
    max_steps = args.max_steps_override if args.max_steps_override else MAX_STEPS.get(args.task_suite, 400)
    
    Path(args.video_out).mkdir(parents=True, exist_ok=True)
    
    successes = 0
    for ep in range(args.num_trials):
        print(f"🚀 Starting Trial {ep} (Max Steps: {max_steps})...")
        env.reset()
        client.reset()
        obs = env.set_init_state(initial_states[ep % len(initial_states)])
        replay_images, uncertainties = [], []
        t, done = 0, False
        
        while t < max_steps + NUM_STEPS_WAIT:
            try:
                if t < NUM_STEPS_WAIT:
                    obs, reward, done, info = env.step(LIBERO_DUMMY_ACTION)
                    t += 1; continue
                img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
                wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
                if not args.no_video: replay_images.append(img)
                state = np.concatenate([obs["robot0_eef_pos"], _quat2axisangle(obs["robot0_eef_quat"]), obs["robot0_gripper_qpos"]])
                action, uncertainty = client.step({"image": img, "wrist_image": wrist_img, "state": state}, task_description)
                if uncertainty: uncertainties.append(uncertainty)
                obs, reward, done, info = env.step(action.tolist())
                if done: successes += 1; break
                t += 1
            except Exception as e: print(f"Error: {e}"); break

        suffix = "success" if done else "failure"
        task_name = task_description.replace(" ", "_")[:50]
        if replay_images: imageio.mimwrite(os.path.join(args.video_out, f"{task_name}_ep{ep}_{suffix}.mp4"), replay_images, fps=40)
        if uncertainties:
            with open(os.path.join(args.video_out, f"{task_name}_ep{ep}_{suffix}_uncertainty.json"), "w") as f:
                json.dump([{k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in u.items()} for u in uncertainties], f)
        print(f"  Result: {suffix.upper()} ({t} steps)")

    env.close()
    print(f"\nFinal Success Rate: {successes}/{args.num_trials}")

if __name__ == "__main__":
    main()
