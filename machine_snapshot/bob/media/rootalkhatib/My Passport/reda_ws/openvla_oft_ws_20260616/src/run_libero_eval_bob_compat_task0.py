"""
run_libero_eval_bob_compat_task0.py

Runs isolated OpenVLA-OFT rollout on LIBERO libero_goal task 0 on Bob.
"""

import os
import sys
import time
import json
import pickle
import numpy as np
import torch
import argparse
from collections import deque
import tqdm

# Add paths to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
sys.path.append("/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages")
sys.path.append("/usr/lib/python3/dist-packages")

# Set HF Cache
os.environ["HF_HOME"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
os.environ["TRANSFORMERS_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"

# Mujoco GL & PyOpenGL Settings
os.environ["MUJOCO_GL"] = "egl"
os.environ["PYOPENGL_PLATFORM"] = "egl"

# Apply monkey patch
import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

# Imports from openvla-oft
from experiments.robot.openvla_utils import get_vla, get_processor, get_proprio_projector, get_action_head, get_vla_action
from experiments.robot.libero.libero_utils import get_libero_env, get_libero_image, get_libero_wrist_image, quat2axisangle, get_libero_dummy_action, save_rollout_video
from experiments.robot.openvla_utils import resize_image_for_policy
from experiments.robot.robot_utils import get_action, get_image_resize_size, normalize_gripper_action, invert_gripper_action, set_seed_everywhere
from libero.libero import benchmark
from prismatic.vla.constants import NUM_ACTIONS_CHUNK

class MockConfig:
    def __init__(self, load_in_8bit=True, load_in_4bit=False, num_trials=1, seed=7):
        self.model_family = "openvla"
        self.pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-goal"
        self.use_l1_regression = True
        self.use_diffusion = False
        self.use_film = False
        self.num_images_in_input = 2
        self.use_proprio = True
        self.center_crop = True
        self.lora_rank = 32
        self.load_in_8bit = load_in_8bit
        self.load_in_4bit = load_in_4bit
        self.unnorm_key = "libero_goal_no_noops"
        self.task_suite_name = "libero_goal"
        self.num_trials_per_task = num_trials
        self.initial_states_path = "DEFAULT"
        self.env_img_res = 256
        self.num_open_loop_steps = 8
        self.num_steps_wait = 10
        self.use_wandb = False
        self.seed = seed

def get_gpu_memory_str():
    if torch.cuda.is_available():
        free, total = torch.cuda.mem_get_info()
        return f"Free = {free / (1024**3):.2f} GB / Total = {total / (1024**3):.2f} GB"
    return "GPU not available"

def prepare_observation(obs, resize_size):
    img = get_libero_image(obs)
    wrist_img = get_libero_wrist_image(obs)

    img_resized = resize_image_for_policy(img, resize_size)
    wrist_img_resized = resize_image_for_policy(wrist_img, resize_size)

    observation = {
        "full_image": img_resized,
        "wrist_image": wrist_img_resized,
        "state": np.concatenate(
            (obs["robot0_eef_pos"], quat2axisangle(obs["robot0_eef_quat"]), obs["robot0_gripper_qpos"])
        ),
    }
    return observation, img

def process_action(action, model_family):
    action = normalize_gripper_action(action, binarize=True)
    if model_family == "openvla":
        action = invert_gripper_action(action)
    return action

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_trials", type=int, default=1)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--log_dir", type=str, required=True)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.log_dir, exist_ok=True)

    log_filepath = os.path.join(args.log_dir, f"rollout_trials_{args.num_trials}.log")
    log_file = open(log_filepath, "w")

    def log(msg):
        print(msg)
        log_file.write(msg + "\n")
        log_file.flush()

    log("=== OpenVLA-OFT LIBERO Rollout Test on Bob ===")
    gpu_before = get_gpu_memory_str()
    log(f"GPU Memory Before: {gpu_before}")

    cfg = MockConfig(num_trials=args.num_trials, seed=args.seed)
    set_seed_everywhere(cfg.seed)

    # 1. Load VLA Model
    log("Loading model...")
    t0_load = time.time()
    vla = get_vla(cfg)
    # Align devices
    openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    log(f"Model loaded in {time.time() - t0_load:.1f}s.")

    # 2. Initialize components
    processor = get_processor(cfg)
    llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
    proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = get_action_head(cfg, llm_dim=llm_dim)

    # 3. Load LIBERO task suite and task 0
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict[cfg.task_suite_name]()
    task_id = 0
    task = task_suite.get_task(task_id)
    initial_states = task_suite.get_task_init_states(task_id)

    log(f"Task ID: {task_id}")
    log(f"Task Instruction: {task.language}")

    env, task_description = get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
    resize_size = get_image_resize_size(cfg)

    max_steps = 300 # Hardcoded max steps for libero_goal in official config
    log(f"Max steps: {max_steps}")

    summaries = []
    summary_jsonl_path = os.path.join(args.output_dir, "episode_summaries.jsonl")

    # Clear/create the summaries file
    with open(summary_jsonl_path, "w") as f:
        pass

    for trial_idx in range(args.num_trials):
        log(f"\n--- Starting Trial {trial_idx + 1}/{args.num_trials} ---")
        trial_seed = cfg.seed + trial_idx
        set_seed_everywhere(trial_seed)

        # Reset environment with specific seed initial state
        env.reset()
        initial_state = initial_states[trial_idx]
        obs = env.set_init_state(initial_state)

        action_queue = deque(maxlen=cfg.num_open_loop_steps)
        t = 0
        success = False
        num_queries = 0
        query_times = []
        replay_images = []
        trial_exception = None

        t0_trial = time.time()
        first_action_chunk_shape = None

        try:
            while t < max_steps + cfg.num_steps_wait:
                if t < cfg.num_steps_wait:
                    obs, reward, done, info = env.step(get_libero_dummy_action(cfg.model_family))
                    t += 1
                    continue

                observation, img = prepare_observation(obs, resize_size)
                replay_images.append(img)

                if len(action_queue) == 0:
                    t_query_start = time.time()
                    # Query model
                    actions = get_action(
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
                    query_times.append(time.time() - t_query_start)
                    num_queries += 1
                    
                    if first_action_chunk_shape is None:
                        first_action_chunk_shape = list(np.array(actions).shape)

                    action_queue.extend(actions)

                action = action_queue.popleft()
                action = process_action(action, cfg.model_family)
                obs, reward, done, info = env.step(action.tolist())

                if done:
                    success = True
                    break
                t += 1

        except Exception as e:
            trial_exception = str(e)
            log(f"Trial failed with exception: {e}")
            import traceback
            traceback.print_exc()

        trial_duration = time.time() - t0_trial
        avg_inference_time = np.mean(query_times) if query_times else 0.0
        num_steps = t - cfg.num_steps_wait

        log(f"Trial {trial_idx + 1} finished in {trial_duration:.1f}s.")
        log(f"Success: {success}, Steps: {num_steps}, Queries: {num_queries}")
        log(f"Average Inference Time: {avg_inference_time:.3f}s")

        # Save video
        try:
            save_rollout_video(
                replay_images, trial_idx + 1, success=success, task_description=task_description, log_file=log_file
            )
        except Exception as video_err:
            log(f"Failed to save rollout video: {video_err}")

        # Record summary
        summary = {
            "task_id": task_id,
            "trial_index": trial_idx,
            "reset_seed": trial_seed,
            "success": success,
            "num_steps": num_steps,
            "num_queries": num_queries,
            "total_wall_time": trial_duration,
            "average_action_inference_time": avg_inference_time,
            "first_action_chunk_shape": first_action_chunk_shape,
            "failure_message": trial_exception
        }
        summaries.append(summary)

        # Append to JSONL
        with open(summary_jsonl_path, "a") as f:
            f.write(json.dumps(summary) + "\n")

    env.close()
    gpu_after = get_gpu_memory_str()
    log(f"GPU Memory After: {gpu_after}")

    # Package versions
    package_versions = {
        "torch": str(torch.__version__),
        "transformers": "4.40.1 (moojink fork)",
        "accelerate": "1.14.0",
        "bitsandbytes": "0.42.0"
    }

    # Save manifest
    manifest = {
        "model_id": cfg.pretrained_checkpoint,
        "repo_commit": "e4287e94541f459edc4feabc4e181f537cd569a8",
        "quantization": "8-bit",
        "unnorm_key": cfg.unnorm_key,
        "action_chunk_size": NUM_ACTIONS_CHUNK,
        "max_steps": max_steps,
        "suite": cfg.task_suite_name,
        "task_id": task_id,
        "exact_command": " ".join(sys.argv),
        "package_versions": package_versions,
        "compatibility_patch_used": True
    }

    manifest_path = os.path.join(args.output_dir, "run_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=4)

    log(f"Saved run manifest to {manifest_path}")
    log_file.close()

if __name__ == "__main__":
    main()
