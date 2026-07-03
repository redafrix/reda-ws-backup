#!/usr/bin/env python3
"""
run_openvla_goal_object_pro_10task_smoke_bob.py

Runs isolated 10-task smoke rollouts for OpenVLA-OFT on LIBERO libero_goal on Bob.
"""

import os
import sys
import time
import json
import numpy as np
import torch
from collections import deque

# Add workspace and LIBERO repo paths to sys.path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
sys.path.append("/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages")
sys.path.append("/usr/lib/python3/dist-packages")

# Set HF Cache and environment configurations
os.environ["HF_HOME"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
os.environ["TRANSFORMERS_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
os.environ["HF_HUB_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
os.environ["MUJOCO_GL"] = "egl"
os.environ["PYOPENGL_PLATFORM"] = "egl"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["USE_TF"] = "0"
os.environ["USE_FLAX"] = "0"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Import compatibility module and apply first patch before loading transformers/accelerate
import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

# Standard imports from openvla-oft and libero
from experiments.robot.openvla_utils import get_vla, get_processor, get_proprio_projector, get_action_head
from experiments.robot.libero.libero_utils import get_libero_env, get_libero_image, get_libero_wrist_image, quat2axisangle, get_libero_dummy_action
from experiments.robot.openvla_utils import resize_image_for_policy
from experiments.robot.robot_utils import get_action, get_image_resize_size, normalize_gripper_action, invert_gripper_action, set_seed_everywhere
from libero.libero import benchmark
from prismatic.vla.constants import NUM_ACTIONS_CHUNK

class Tee:
    def __init__(self, filename, mode="w"):
        self.file = open(filename, mode)
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
        self.file.flush()
        self.stdout.flush()

    def flush(self):
        self.file.flush()
        self.stdout.flush()

    def close(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        self.file.close()

class MockConfig:
    def __init__(self, load_in_8bit=True, load_in_4bit=False, num_trials=1, seed=0):
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

def save_rollout_video_custom(rollout_images, task_id, success, task_description, output_dir):
    """Saves an MP4 (or GIF fallback) replay of an episode directly to the output directory."""
    import imageio
    os.makedirs(output_dir, exist_ok=True)
    date_time = time.strftime("%Y_%m_%d-%H_%M_%S")
    processed_task_description = task_description.lower().replace(" ", "_").replace("\n", "_").replace(".", "_")[:50]
    
    try:
        mp4_path = os.path.join(output_dir, f"{date_time}--openvla_oft--task={task_id}--success={success}--name={processed_task_description}.mp4")
        video_writer = imageio.get_writer(mp4_path, fps=30)
        for img in rollout_images:
            video_writer.append_data(img)
        video_writer.close()
        print(f"Saved rollout MP4 at path {mp4_path}")
        return mp4_path
    except Exception as e:
        print(f"Failed to save as MP4 ({e}). Trying GIF fallback...")
        gif_path = os.path.join(output_dir, f"{date_time}--openvla_oft--task={task_id}--success={success}--name={processed_task_description}.gif")
        video_writer = imageio.get_writer(gif_path, fps=30)
        for img in rollout_images:
            video_writer.append_data(img)
        video_writer.close()
        print(f"Saved rollout GIF fallback at path {gif_path}")
        return gif_path

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
    output_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/goal_object_pro_10task_smoke_20260616"
    log_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/goal_object_pro_10task_smoke_20260616"
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)
    
    log_filepath = os.path.join(log_dir, "stdout_stderr.log")
    tee = Tee(log_filepath, "w")
    
    print("=== OpenVLA-OFT 10-Task Smoke Runner ===")
    print(f"GPU Memory Before Load: {get_gpu_memory_str()}")

    cfg = MockConfig(num_trials=1, seed=0)
    set_seed_everywhere(cfg.seed)

    # 1. Load VLA Model
    print("Loading VLA Model...")
    t0_load = time.time()
    vla = get_vla(cfg)
    
    # Apply second patch (align rotary device)
    openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    print(f"Model loaded in {time.time() - t0_load:.1f}s.")

    # 2. Initialize components
    processor = get_processor(cfg)
    llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
    proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = get_action_head(cfg, llm_dim=llm_dim)

    # 3. Load LIBERO task suite
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict[cfg.task_suite_name]()
    num_tasks = task_suite.get_num_tasks()
    
    # Verify exact suite/task source
    print(f"Resolved Suite Name: {cfg.task_suite_name}")
    print(f"Task Count: {num_tasks}")
    
    if num_tasks != 10:
        print(f"ERROR: Expected 10 tasks in the suite, but found {num_tasks}. Stopping.")
        sys.exit(1)

    print("Task IDs and Names:")
    for i in range(num_tasks):
        task = task_suite.get_task(i)
        print(f"  Task {i}: {task.language}")
        
    bddl_path_root = os.path.dirname(task_suite.get_task_bddl_file_path(0))
    init_state_path_root = os.path.dirname(os.path.join(
        benchmark.get_libero_path("init_states"),
        task_suite.tasks[0].problem_folder,
        task_suite.tasks[0].init_states_file,
    ))
    print(f"BDDL Path Root: {bddl_path_root}")
    print(f"Init-State Path Root: {init_state_path_root}")

    # Write suite info file
    suite_info_path = os.path.join(output_dir, "suite_info.json")
    with open(suite_info_path, "w") as f:
        json.dump({
            "suite_name": cfg.task_suite_name,
            "task_count": num_tasks,
            "task_ids": list(range(num_tasks)),
            "task_names": [task_suite.get_task(i).language for i in range(num_tasks)],
            "bddl_path_root": bddl_path_root,
            "init_state_path_root": init_state_path_root
        }, f, indent=4)

    max_steps = 800
    print(f"Max steps: {max_steps}")

    summaries = []
    summary_jsonl_path = os.path.join(output_dir, "episode_summaries.jsonl")

    # Clear/create the summaries file
    with open(summary_jsonl_path, "w") as f:
        pass

    all_passed = True

    for task_id in range(num_tasks):
        print(f"\n--- Starting Smoke Test for Task {task_id}/{num_tasks-1} ---")
        task = task_suite.get_task(task_id)
        initial_states = task_suite.get_task_init_states(task_id)
        
        print(f"Task Instruction: {task.language}")
        
        trial_seed = 0
        set_seed_everywhere(trial_seed)

        env, task_description = get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
        resize_size = get_image_resize_size(cfg)

        # Reset environment with specific seed initial state
        env.reset()
        initial_state = initial_states[0]
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

                    actions_np = np.array(actions)
                    
                    # Log prediction and execution horizons
                    # Since OpenVLA-OFT predicts chunk of 8 actions and we execute all 8 actions,
                    # predicted horizon is 8, and actual executed horizon is 8.
                    print(f"[Query {num_queries}] Predicted action chunk shape: {actions_np.shape}. Horizon prediction H=8, Executed H=8.")
                    
                    # Verify action shape and values are finite
                    assert actions_np.shape == (8, 7), f"Expected action shape (8, 7), got {actions_np.shape}"
                    assert np.isfinite(actions_np).all(), "Actions contain non-finite values (NaN/Inf)!"
                    
                    if first_action_chunk_shape is None:
                        first_action_chunk_shape = list(actions_np.shape)

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
            print(f"Task {task_id} failed with exception: {e}")
            import traceback
            traceback.print_exc()
            all_passed = False

        trial_duration = time.time() - t0_trial
        avg_inference_time = np.mean(query_times) if query_times else 0.0
        num_steps = t - cfg.num_steps_wait

        print(f"Task {task_id} finished in {trial_duration:.1f}s.")
        print(f"Success: {success}, Steps: {num_steps}, Queries: {num_queries}")

        # Close env
        env.close()

        # Save video
        try:
            save_rollout_video_custom(
                replay_images, task_id, success, task_description, output_dir
            )
        except Exception as video_err:
            print(f"Failed to save rollout video: {video_err}")

        # Record summary
        summary = {
            "task_id": task_id,
            "task_name": task.language,
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

    print(f"\nGPU Memory After Run: {get_gpu_memory_str()}")
    print(f"All Tasks Passed Smoke Test: {all_passed}")
    
    tee.close()
    
    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
