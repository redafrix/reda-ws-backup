import sys
import os
import pathlib
import collections
import json
import math
import numpy as np
import imageio
import tqdm

import torch
# Monkeypatch torch.load to default weights_only=False for PyTorch 2.6+ compatibility with old LIBERO files
original_load = torch.load
def patched_load(*args, **kwargs):
    if "weights_only" not in kwargs:
        kwargs["weights_only"] = False
    return original_load(*args, **kwargs)
torch.load = patched_load

# Add openpi src and libero to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi/src")

from openpi.policies import policy_config as _policy_config
from openpi.training import config as _config
from openpi.policies import libero_policy
from openpi_client import image_tools

from libero.libero import benchmark
from libero.libero import get_libero_path
from libero.libero.envs import OffScreenRenderEnv

def _quat2axisangle(quat):
    if quat[3] > 1.0:
        quat[3] = 1.0
    elif quat[3] < -1.0:
        quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0):
        return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den

def run_rollout(policy, env, task_description, initial_states, episode_idx, seed, mode_name, mask_left_wrist_false, zero_wrist, max_steps, output_dir):
    env.seed(seed)
    env.reset()
    obs = env.set_init_state(initial_states[episode_idx])
    
    t = 0
    num_steps_wait = 10
    action_plan = collections.deque()
    replay_images = []
    
    success = False
    
    print(f"Running rollout for {mode_name}...")
    while t < max_steps + num_steps_wait:
        try:
            if t < num_steps_wait:
                obs, reward, done, info = env.step([0.0] * 6 + [-1.0])
                t += 1
                continue
                
            img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
            if zero_wrist:
                wrist_img = np.zeros_like(img)
            else:
                wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
                
            img = image_tools.convert_to_uint8(
                image_tools.resize_with_pad(img, 224, 224)
            )
            wrist_img = image_tools.convert_to_uint8(
                image_tools.resize_with_pad(wrist_img, 224, 224)
            )
            
            replay_images.append(img)
            
            if not action_plan:
                element = {
                    "observation/image": img,
                    "observation/wrist_image": wrist_img,
                    "observation/state": np.concatenate(
                        (
                            obs["robot0_eef_pos"],
                            _quat2axisangle(obs["robot0_eef_quat"]),
                            obs["robot0_gripper_qpos"],
                        )
                    ),
                    "prompt": str(task_description),
                }
                if mask_left_wrist_false:
                    element["mask_left_wrist_false"] = True
                    
                outputs = policy.infer(element)
                action_chunk = outputs["actions"]
                action_plan.extend(action_chunk[:10])
                
            action = action_plan.popleft()
            obs, reward, done, info = env.step(action.tolist())
            if done:
                success = True
                break
            t += 1
        except Exception as e:
            print(f"Exception during rollout: {e}")
            break
            
    print(f"Rollout {mode_name} finished. Success: {success}. Steps: {t - num_steps_wait}")
    
    video_path = output_dir / f"smoke_{mode_name}_rollout.mp4"
    imageio.mimwrite(
        video_path,
        [np.asarray(x) for x in replay_images],
        fps=10,
    )
    
    summary = {
        "mode": mode_name,
        "success": bool(success),
        "steps": int(t - num_steps_wait),
        "max_steps": max_steps,
        "seed": seed,
        "video_path": str(video_path),
        "zero_wrist": zero_wrist,
        "mask_left_wrist_false": mask_left_wrist_false,
    }
    summary_path = output_dir / f"smoke_{mode_name}_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
        
    return summary

def run_candidate_generation_smoke(policy, output_dir):
    print("Running Candidate Generation Smoke...")
    obs = libero_policy.make_libero_example()
    element = {
        "observation/image": obs["observation/image"],
        "observation/wrist_image": obs["observation/wrist_image"],
        "observation/state": obs["observation/state"],
        "prompt": obs["prompt"],
    }
    
    outputs = policy.infer(element)
    main_chunk = outputs["actions"]
    
    candidates = []
    for i in range(8):
        rng = np.random.default_rng(seed=i)
        noise = rng.normal(size=(10, 32)) # Padding to 32 action dim of the model
        outputs = policy.infer(element, noise=noise)
        candidates.append(outputs["actions"])
        
    candidates = np.stack(candidates)
    
    are_identical = True
    for i in range(8):
        for j in range(i+1, 8):
            if np.allclose(candidates[i], candidates[j]):
                print(f"Candidates {i} and {j} are identical!")
            else:
                are_identical = False
                
    print(f"Candidates generated: shape={candidates.shape}")
    print(f"Are candidates identical: {are_identical}")
    
    summary = {
        "main_chunk_shape": list(main_chunk.shape),
        "candidates_shape": list(candidates.shape),
        "are_candidates_identical": are_identical,
        "main_chunk": main_chunk.tolist(),
        "candidates": candidates.tolist(),
    }
    summary_path = output_dir / "smoke_candidate_generation_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    return summary

def main():
    checkpoint_dir = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/pi05_libero"
    config_name = "pi05_libero"
    output_dir = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/outputs")
    
    print("Loading policy...")
    policy = _policy_config.create_trained_policy(
        _config.get_config(config_name), 
        checkpoint_dir
    )
    
    print("Initializing environment...")
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict["libero_goal_object"]()
    task = task_suite.get_task(0)
    initial_states = task_suite.get_task_init_states(0)
    
    task_description = task.language
    task_bddl_file = pathlib.Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    env_args = {"bddl_file_name": task_bddl_file, "camera_heights": 256, "camera_widths": 256}
    env = OffScreenRenderEnv(**env_args)
    
    # 1. Smoke Test A: Two Camera
    run_rollout(
        policy=policy,
        env=env,
        task_description=task_description,
        initial_states=initial_states,
        episode_idx=0,
        seed=10,
        mode_name="two_camera",
        mask_left_wrist_false=False,
        zero_wrist=False,
        max_steps=300,
        output_dir=output_dir
    )
    
    # 2. Smoke Test B1: One Camera (zeros_like, mask=True)
    run_rollout(
        policy=policy,
        env=env,
        task_description=task_description,
        initial_states=initial_states,
        episode_idx=0,
        seed=10,
        mode_name="one_camera_mask_true",
        mask_left_wrist_false=False,
        zero_wrist=True,
        max_steps=300,
        output_dir=output_dir
    )
    
    # 3. Smoke Test B2: One Camera (zeros_like, mask=False)
    run_rollout(
        policy=policy,
        env=env,
        task_description=task_description,
        initial_states=initial_states,
        episode_idx=0,
        seed=10,
        mode_name="one_camera_mask_false",
        mask_left_wrist_false=True,
        zero_wrist=True,
        max_steps=300,
        output_dir=output_dir
    )
    
    # 4. Candidate Generation
    run_candidate_generation_smoke(policy, output_dir)
    
    print("All smoke tests executed successfully!")

if __name__ == "__main__":
    main()
