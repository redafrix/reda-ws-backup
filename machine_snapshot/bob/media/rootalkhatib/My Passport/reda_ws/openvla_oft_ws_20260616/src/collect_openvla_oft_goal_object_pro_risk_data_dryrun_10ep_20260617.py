#!/usr/bin/env python3
"""
collect_openvla_oft_goal_object_pro_risk_data_dryrun_10ep_20260617.py

Large-scale risk-data collection round-robin script for OpenVLA-OFT on LIBERO libero_goal_object.
"""

import os
import sys
import time
import json
import hashlib
import numpy as np
import torch
from collections import deque

# Add workspace and LIBERO repo paths to sys.path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
sys.path.append("/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages")
sys.path.append("/usr/lib/python3/dist-packages")

# Set LIBERO_CONFIG_PATH before any imports from libero
os.environ["LIBERO_CONFIG_PATH"] = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"

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

# Apply Monkey Patch to fix Libero BDDL parsing / _load_sites_in_arena KeyError
def patch_libero_tabletop_manipulation():
    from libero.libero.envs.bddl_base_domain import TASK_MAPPING
    import libero.libero.envs.problems.libero_tabletop_manipulation
    from libero.libero.envs.objects import SiteObject, TargetZone
    from robosuite.utils.mjcf_utils import new_site, string_to_array
    import xml.etree.ElementTree as ET

    def patched_load_sites_in_arena(self, mujoco_arena):
        # Create site objects
        object_sites_dict = {}
        region_dict = self.parsed_problem["regions"]
        for object_region_name in list(region_dict.keys()):

            if "main_table" in object_region_name:
                ranges = region_dict[object_region_name]["ranges"][0]
                assert ranges[2] >= ranges[0] and ranges[3] >= ranges[1]
                zone_size = ((ranges[2] - ranges[0]) / 2, (ranges[3] - ranges[1]) / 2)
                zone_centroid_xy = (
                    (ranges[2] + ranges[0]) / 2,
                    (ranges[3] + ranges[1]) / 2,
                )
                target_zone = TargetZone(
                    name=object_region_name,
                    rgba=region_dict[object_region_name]["rgba"],
                    zone_size=zone_size,
                    zone_centroid_xy=zone_centroid_xy,
                )
                object_sites_dict[object_region_name] = target_zone

                mujoco_arena.table_body.append(
                    new_site(
                        name=target_zone.name,
                        pos=target_zone.pos,
                        quat=target_zone.quat,
                        rgba=target_zone.rgba,
                        size=target_zone.size,
                        type="box",
                    )
                )
                continue

            # Otherwise the processing is consistent
            for query_dict in [self.objects_dict, self.fixtures_dict]:
                for (name, body) in query_dict.items():
                    try:
                        if "worldbody" not in list(body.__dict__.keys()):
                            # This is a special case for CompositeObject, we skip this as this is very rare in our benchmark
                            continue
                    except:
                        continue
                    
                    top_body = body.worldbody.find("body")
                    if top_body is None:
                        continue
                    all_bodies = [top_body] + top_body.findall(".//body")
                    
                    # 1. Check if the site with the exact BDDL region name already exists
                    exact_site = None
                    matching_clean_site = None
                    matching_clean_part = None
                    
                    for part in all_bodies:
                        for site in part.findall("./site"):
                            site_name = site.get("name")
                            if site_name == object_region_name:
                                exact_site = site
                                break
                            
                            # Check clean name match
                            site_name_clean = site_name.replace("_site", "").replace("_region", "")
                            target_name_clean = object_region_name.replace("_site", "").replace("_region", "")
                            if site_name_clean == target_name_clean and site_name_clean != "":
                                matching_clean_site = site
                                matching_clean_part = part
                        if exact_site is not None:
                            break
                            
                    # If we found the exact site in the body, use it directly (no injection needed)
                    if exact_site is not None:
                        site_part = None
                        for part in all_bodies:
                            if exact_site in part.findall("./site"):
                                site_part = part
                                break
                        joints = site_part.findall("./joint") if site_part is not None else []
                        
                        # Process and pad size to at least 3 dimensions
                        size_arr = np.array([0.05, 0.05, 0.05])
                        size_val = exact_site.get("size")
                        if size_val is not None:
                            try:
                                raw_arr = string_to_array(size_val)
                                if isinstance(raw_arr, float) or isinstance(raw_arr, int):
                                    raw_arr = np.array([raw_arr])
                                for idx in range(min(3, len(raw_arr))):
                                    size_arr[idx] = max(0.05, raw_arr[idx])
                            except Exception as parse_err:
                                print(f"[Monkey Patch] Error parsing size '{size_val}': {parse_err}")
                        
                        object_sites_dict[object_region_name] = SiteObject(
                            name=object_region_name,
                            parent_name=body.name,
                            joints=[joint.get("name") for joint in joints],
                            size=size_arr,
                            rgba=exact_site.get("rgba"),
                            site_type=exact_site.get("type"),
                            site_pos=exact_site.get("pos"),
                            site_quat=exact_site.get("quat") if exact_site.get("quat") is not None else "1 0 0 0",
                            object_properties=body.object_properties,
                        )
                        continue
                        
                    # 2. If we didn't find the exact site, but found a matching clean site, inject it to body._obj
                    if matching_clean_site is not None:
                        # Check if a site with object_region_name was already injected in body._obj
                        already_injected = False
                        if body._obj is not None:
                            for site in body._obj.findall(".//site"):
                                if site.get("name") == object_region_name:
                                    already_injected = True
                                    exact_site = site
                                    break
                                    
                        if not already_injected:
                            print(f"[Monkey Patch] Injected missing XML site '{object_region_name}' to body._obj at pos={matching_clean_site.get('pos')} (based on '{matching_clean_site.get('name')}')")
                            new_site_el = new_site(
                                name=object_region_name,
                                pos=matching_clean_site.get("pos"),
                                quat=matching_clean_site.get("quat") if matching_clean_site.get("quat") is not None else "1 0 0 0",
                                rgba=matching_clean_site.get("rgba"),
                                size=matching_clean_site.get("size"),
                                type=matching_clean_site.get("type") if matching_clean_site.get("type") is not None else "sphere",
                            )
                            body._obj.append(new_site_el)
                            exact_site = new_site_el
                            
                        joints = matching_clean_part.findall("./joint") if matching_clean_part is not None else []
                        
                        # Process and pad size to at least 3 dimensions
                        size_arr = np.array([0.05, 0.05, 0.05])
                        size_val = exact_site.get("size")
                        if size_val is not None:
                            try:
                                raw_arr = string_to_array(size_val)
                                if isinstance(raw_arr, float) or isinstance(raw_arr, int):
                                    raw_arr = np.array([raw_arr])
                                for idx in range(min(3, len(raw_arr))):
                                    size_arr[idx] = max(0.05, raw_arr[idx])
                            except Exception as parse_err:
                                print(f"[Monkey Patch] Error parsing size '{size_val}': {parse_err}")

                        object_sites_dict[object_region_name] = SiteObject(
                            name=object_region_name,
                            parent_name=body.name,
                            joints=[joint.get("name") for joint in joints],
                            size=size_arr,
                            rgba=exact_site.get("rgba"),
                            site_type=exact_site.get("type"),
                            site_pos=exact_site.get("pos"),
                            site_quat=exact_site.get("quat") if exact_site.get("quat") is not None else "1 0 0 0",
                            object_properties=body.object_properties,
                        )
                                
        self.object_sites_dict = object_sites_dict

        # Keep track of visualization objects
        for query_dict in [self.fixtures_dict, self.objects_dict]:
            for name, body in query_dict.items():
                if body.object_properties["vis_site_names"] != {}:
                    self.visualization_sites_list.append(name)

    # Apply the monkey patch using the task mapping registry
    target_class = TASK_MAPPING.get("libero_tabletop_manipulation")
    if target_class is not None:
        target_class._load_sites_in_arena = patched_load_sites_in_arena
        print(f"[Monkey Patch] Successfully applied _load_sites_in_arena fix to {target_class.__name__}")
    else:
        print("[Monkey Patch] WARNING: Libero_Tabletop_Manipulation class not found in TASK_MAPPING!")

# Automatically apply the patch upon import
patch_libero_tabletop_manipulation()

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
        self.task_suite_name = "libero_goal_object"
        self.num_trials_per_task = num_trials
        self.initial_states_path = "DEFAULT"
        self.env_img_res = 256
        self.num_open_loop_steps = 8
        self.num_steps_wait = 10
        self.use_wandb = False
        self.seed = seed

def save_rollout_video_custom(rollout_images, task_id, episode_idx, success, task_description, output_dir):
    """Saves an MP4 (or GIF fallback) replay of an episode directly to the output directory."""
    import imageio
    os.makedirs(output_dir, exist_ok=True)
    date_time = time.strftime("%Y_%m_%d-%H_%M_%S")
    processed_task_description = task_description.lower().replace(" ", "_").replace("\n", "_").replace(".", "_")[:50]
    
    mp4_path = os.path.join(output_dir, f"{date_time}--openvla_oft--task={task_id}--ep={episode_idx}--success={success}--name={processed_task_description}.mp4")
    gif_path = os.path.join(output_dir, f"{date_time}--openvla_oft--task={task_id}--ep={episode_idx}--success={success}--name={processed_task_description}.gif")
    
    try:
        video_writer = imageio.get_writer(mp4_path, fps=30)
        for img in rollout_images:
            video_writer.append_data(img)
        video_writer.close()
        print(f"Saved rollout MP4 at path {mp4_path}")
        # Remove empty or incomplete GIF if created by mistake
        if os.path.exists(gif_path):
            os.remove(gif_path)
        return mp4_path
    except Exception as e:
        print(f"Failed to save as MP4 ({e}). Trying GIF fallback...")
        if os.path.exists(mp4_path):
            try:
                os.remove(mp4_path)
            except:
                pass
        video_writer = imageio.get_writer(gif_path, fps=30)
        for img in rollout_images:
            video_writer.append_data(img)
        video_writer.close()
        print(f"Saved rollout GIF fallback at path {gif_path}")
        return gif_path

def get_gpu_memory():
    if torch.cuda.is_available():
        try:
            free, total = torch.cuda.mem_get_info()
            return {
                "free_GB": float(free / (1024**3)),
                "total_GB": float(total / (1024**3))
            }
        except:
            pass
    return {"free_GB": 0.0, "total_GB": 0.0}

def prepare_observation(obs, resize_size):
    from experiments.robot.libero.libero_utils import get_libero_image, get_libero_wrist_image
    from experiments.robot.openvla_utils import resize_image_for_policy
    
    img = get_libero_image(obs)
    wrist = get_libero_wrist_image(obs)

    img_resized = resize_image_for_policy(img, resize_size)
    wrist_resized = resize_image_for_policy(wrist, resize_size)

    observation = {
        "full_image": img_resized,
        "wrist_image": wrist_resized,
        "state": obs_to_proprio(obs)
    }
    return observation, img

def obs_to_proprio(obs):
    ee_pos = obs.get("robot0_eef_pos", np.zeros(3))
    ee_quat = obs.get("robot0_eef_quat", np.array([0,0,0,1.0]))
    grip = obs.get("robot0_gripper_qpos", np.zeros(2))
    state = np.concatenate([ee_pos, quat2axisangle(ee_quat), grip])[:8]
    if state.size < 8:
        state = np.pad(state, (0, 8-state.size))
    return state

def process_action(action, model_family):
    action = normalize_gripper_action(action, binarize=True)
    if model_family == "openvla":
        action = invert_gripper_action(action)
    return action

def main():
    output_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_dryrun_10ep_20260617"
    log_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/openvla_goal_object_pro_risk_data_dryrun_10ep_20260617"
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)
    
    log_filepath = os.path.join(log_dir, "collector_supervisor.log")
    tee = Tee(log_filepath, "a")
    
    print("\n=======================================================")
    print("=== OpenVLA-OFT Risk Data Collection Supervisor ===")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=======================================================")

    cfg = MockConfig(num_trials=1, seed=0)
    set_seed_everywhere(cfg.seed)

    # 1. Load VLA Model
    print("Loading VLA Model...")
    t0_load = time.time()
    vla = get_vla(cfg)
    openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    print(f"Model loaded successfully in {time.time() - t0_load:.1f}s.")

    processor = get_processor(cfg)
    llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
    proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = get_action_head(cfg, llm_dim=llm_dim)

    # 2. Load LIBERO task suite
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict[cfg.task_suite_name]()
    num_tasks = task_suite.get_num_tasks()
    
    bddl_path_root = os.path.dirname(task_suite.get_task_bddl_file_path(0))
    init_state_path_root = os.path.dirname(os.path.join(
        benchmark.get_libero_path("init_states"),
        task_suite.tasks[0].problem_folder,
        task_suite.tasks[0].init_states_file,
    ))

    # 3. Create schema, seed plan, and status files if missing
    schema_path = os.path.join(output_dir, "dataset_schema.json")
    if not os.path.exists(schema_path):
        schema = {
            "dataset_name": "openvla_goal_object_pro_risk_data_dryrun_10ep_20260617",
            "ACE_AVAILABLE": "NO",
            "OPENVLA_ACTION_STAT_FEATURES_AVAILABLE": "YES",
            "history_window_size": 8,
            "episode_level_fields": [
                "suite", "task_id", "task_name", "episode_index_global", "episode_index_for_task", 
                "round_index", "reset_seed", "success", "terminal_done", "timeout", "num_steps", 
                "max_steps", "wall_time_seconds", "model_id", "quantization", "unnorm_key", 
                "native_prediction_horizon", "actual_execution_horizon"
            ],
            "query_level_fields": [
                "query_index", "env_timestep", "task_id", "reset_seed", "observation_image_path", 
                "proprio_vector", "predicted_action_chunk_shape", "full_predicted_action_chunk", 
                "executed_prefix_length", "actual_executed_actions", "action_finite_check", 
                "action_norm_statistics", "model_inference_time", "GPU_memory", "native_horizon_H", 
                "any_available_logits", "OPENVLA_ACTION_STAT_FEATURES"
            ],
            "step_level_fields": [
                "env_timestep", "action_executed", "proprio_before", "proprio_after", "reward", 
                "done", "info", "success_check", "query_index_that_produced_action", "step_in_chunk", "history"
            ],
            "note": "This dataset supports an OpenVLA-specific risk model, not the old SimVLA ACE feature schema."
        }
        with open(schema_path, "w") as f:
            json.dump(schema, f, indent=4)
        print(f"Created schema file at: {schema_path}")

    seed_plan_path = os.path.join(output_dir, "seed_plan.json")
    if not os.path.exists(seed_plan_path):
        seed_plan = {
            "note": "For round r and task t, reset_seed = 100000 + r. All tasks in same round share the same reset_seed.",
            "plan": [{"round": r, "task": t, "reset_seed": 100000 + r} for r in range(1000) for t in range(10)]
        }
        with open(seed_plan_path, "w") as f:
            json.dump(seed_plan, f, indent=4)
        print(f"Created seed plan file at: {seed_plan_path}")

    # Resume-safe status file
    status_path = os.path.join(output_dir, "collection_status.json")
    if os.path.exists(status_path):
        with open(status_path, "r") as f:
            status = json.load(f)
        print(f"Resuming collection from status. Completed episodes: {status['total_episodes_completed']}")
    else:
        status = {
            "total_episodes_completed": 0,
            "next_round": 0,
            "next_task": 0,
            "completed_episodes_list": []
        }
        with open(status_path, "w") as f:
            json.dump(status, f, indent=4)
        print("Created new collection status file.")

    total_target_episodes = 10
    max_steps = 800
    resize_size = get_image_resize_size(cfg)

    # File paths for dataset records
    episode_summaries_path = os.path.join(output_dir, "episode_summaries.jsonl")
    query_records_path = os.path.join(output_dir, "query_records.jsonl")
    step_records_path = os.path.join(output_dir, "step_records.jsonl")

    # Round robin loop
    # 1000 rounds * 10 tasks = 10,000 episodes
    for round_idx in range(status["next_round"], 1000):
        # Action chunk lists to save in round .npz file
        round_action_chunks = []
        round_query_metadata = []

        for task_id in range(10):
            # If we are resuming, skip tasks in the next_round until we reach next_task
            if round_idx == status["next_round"] and task_id < status["next_task"]:
                continue

            if status["total_episodes_completed"] >= total_target_episodes:
                break

            task = task_suite.get_task(task_id)
            initial_states = task_suite.get_task_init_states(task_id)
            
            reset_seed = 100000 + round_idx
            print(f"\n--- Round {round_idx}, Task {task_id} (Global Ep {status['total_episodes_completed'] + 1}/{total_target_episodes}) ---")
            print(f"Task Name: {task.language}")
            print(f"Reset Seed: {reset_seed}")

            set_seed_everywhere(reset_seed)
            env, task_description = get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
            
            # Reset environment
            env.reset()
            initial_state = initial_states[round_idx % len(initial_states)]
            obs = env.set_init_state(initial_state)

            action_queue = deque(maxlen=cfg.num_open_loop_steps)
            t = 0
            success = False
            num_queries = 0
            replay_images = []
            
            # Trajectory histories for rolling windows
            traj_proprios = []
            traj_actions = []
            traj_query_stats = []

            # Lists to hold query and step records for this episode until it finishes (to write atomically)
            ep_query_records = []
            ep_step_records = []

            t0_episode = time.time()
            trial_exception = None

            try:
                while t < max_steps + cfg.num_steps_wait:
                    if t < cfg.num_steps_wait:
                        obs, reward, done, info = env.step(get_libero_dummy_action(cfg.model_family))
                        t += 1
                        continue

                    # Current active policy step
                    step_idx = t - cfg.num_steps_wait
                    observation, img = prepare_observation(obs, resize_size)
                    
                    # Video saving policy: save first 3 rounds (0, 1, 2) or save failures that ran past step 300
                    replay_images.append(img)

                    # Proprio before execution
                    proprio_before = observation["state"]
                    traj_proprios.append(proprio_before)

                    # Determine if query is needed
                    if len(action_queue) == 0:
                        t_query_start = time.time()
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
                        inference_time = time.time() - t_query_start
                        num_queries += 1

                        actions_np = np.array(actions)
                        assert actions_np.shape == (8, 7), f"Expected action shape (8, 7), got {actions_np.shape}"
                        assert np.isfinite(actions_np).all(), "Actions contain non-finite values (NaN/Inf)!"

                        # Calculate Action Statistics
                        action_norm_stats = {
                            "mean": float(np.mean(actions_np)),
                            "std": float(np.std(actions_np)),
                            "min": float(np.min(actions_np)),
                            "max": float(np.max(actions_np)),
                            "l1_norm": float(np.sum(np.abs(actions_np))),
                            "l2_norm": float(np.sqrt(np.sum(actions_np**2)))
                        }

                        # Compute image hash
                        img_hash = hashlib.md5(img.tobytes()).hexdigest()

                        # GPU Memory Info
                        gpu_mem = get_gpu_memory()

                        # Save query record
                        query_record = {
                            "query_index": num_queries - 1,
                            "env_timestep": step_idx,
                            "task_id": task_id,
                            "reset_seed": reset_seed,
                            "observation_image_path": img_hash,  # image hash used as requested
                            "proprio_vector": proprio_before.tolist(),
                            "predicted_action_chunk_shape": [8, 7],
                            "full_predicted_action_chunk": actions_np.tolist(),
                            "executed_prefix_length": 8,
                            "actual_executed_actions": actions_np.tolist(),
                            "action_finite_check": True,
                            "action_norm_statistics": action_norm_stats,
                            "model_inference_time": inference_time,
                            "GPU_memory": gpu_mem,
                            "native_horizon_H": 8,
                            "any_available_logits": None,
                            "OPENVLA_ACTION_STAT_FEATURES": action_norm_stats
                        }
                        ep_query_records.append(query_record)

                        # Append to round chunks for .npz file
                        round_action_chunks.append(actions_np)
                        round_query_metadata.append({
                            "round": round_idx,
                            "task": task_id,
                            "step": step_idx,
                            "query": num_queries - 1
                        })

                        action_queue.extend(actions)

                    # Get and execute action
                    action = action_queue.popleft()
                    action_processed = process_action(action, cfg.model_family)
                    
                    obs, reward, done, info = env.step(action_processed.tolist())
                    
                    proprio_after = obs_to_proprio(obs)
                    traj_actions.append(action_processed)

                    # Query stats associated with this action's query
                    # In our case, the query is the last one in ep_query_records
                    current_query_stats = ep_query_records[-1]["action_norm_statistics"]
                    traj_query_stats.append(current_query_stats)

                    # Build rolling history window (size K=8)
                    K = 8
                    prev_proprio_window = []
                    prev_action_window = []
                    prev_stats_window = []

                    for h_idx in range(max(0, step_idx - K), step_idx):
                        prev_proprio_window.append(traj_proprios[h_idx].tolist())
                        prev_action_window.append(traj_actions[h_idx].tolist())
                        prev_stats_window.append(traj_query_stats[h_idx])

                    valid_history_count = len(prev_proprio_window)
                    padding_count = K - valid_history_count

                    # Pad windows if necessary
                    if padding_count > 0:
                        prev_proprio_window = [[0.0] * 8] * padding_count + prev_proprio_window
                        prev_action_window = [[0.0] * 7] * padding_count + prev_action_window
                        # Empty statistics pad
                        pad_stat = {"mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0, "l1_norm": 0.0, "l2_norm": 0.0}
                        prev_stats_window = [pad_stat] * padding_count + prev_stats_window

                    step_record = {
                        "env_timestep": step_idx,
                        "action_executed": action_processed.tolist(),
                        "proprio_before": proprio_before.tolist(),
                        "proprio_after": proprio_after.tolist(),
                        "reward": float(reward),
                        "done": bool(done),
                        "info": str(info),
                        "success_check": bool(done),
                        "query_index_that_produced_action": num_queries - 1,
                        "step_in_chunk": (step_idx % 8),
                        "history": {
                            "prev_proprio_states": prev_proprio_window,
                            "prev_executed_actions": prev_action_window,
                            "prev_query_action_statistics": prev_stats_window,
                            "valid_history_count": valid_history_count,
                            "padding_count": padding_count,
                            "history_stride": 1
                        }
                    }
                    ep_step_records.append(step_record)

                    if done:
                        success = True
                        break
                    t += 1

            except Exception as e:
                trial_exception = str(e)
                print(f"Episode failed with exception: {e}")
                import traceback
                traceback.print_exc()

            env.close()

            episode_duration = time.time() - t0_episode
            num_steps = t - cfg.num_steps_wait

            print(f"Finished episode. Success: {success}, Steps: {num_steps}, Duration: {episode_duration:.1f}s")

            # Save video if first 3 rounds OR (failed and steps > 300)
            should_save_video = (round_idx < 3) or (not success and num_steps > 300)
            if should_save_video and len(replay_images) > 0:
                try:
                    save_rollout_video_custom(
                        replay_images, task_id, round_idx, success, task.language, output_dir
                    )
                except Exception as video_err:
                    print(f"Failed to save video: {video_err}")

            # Episode summary
            summary = {
                "suite": cfg.task_suite_name,
                "task_id": task_id,
                "task_name": task.language,
                "episode_index_global": status["total_episodes_completed"],
                "episode_index_for_task": round_idx,
                "round_index": round_idx,
                "reset_seed": reset_seed,
                "success": success,
                "terminal_done": success,  # matches success in LIBERO
                "timeout": (num_steps >= max_steps),
                "num_steps": num_steps,
                "max_steps": max_steps,
                "wall_time_seconds": episode_duration,
                "model_id": cfg.pretrained_checkpoint,
                "quantization": "8-bit",
                "unnorm_key": cfg.unnorm_key,
                "native_prediction_horizon": 8,
                "actual_execution_horizon": 8
            }

            # Write data atomically to files
            with open(episode_summaries_path, "a") as f:
                f.write(json.dumps(summary) + "\n")

            with open(query_records_path, "a") as f:
                for qr in ep_query_records:
                    f.write(json.dumps(qr) + "\n")

            with open(step_records_path, "a") as f:
                for sr in ep_step_records:
                    f.write(json.dumps(sr) + "\n")

            # Update status atomically
            status["total_episodes_completed"] += 1
            if task_id == 9:
                status["next_round"] = round_idx + 1
                status["next_task"] = 0
            else:
                status["next_round"] = round_idx
                status["next_task"] = task_id + 1

            status["completed_episodes_list"].append({
                "round": round_idx,
                "task": task_id,
                "success": success,
                "num_steps": num_steps
            })

            temp_status_path = status_path + ".tmp"
            with open(temp_status_path, "w") as f:
                json.dump(status, f, indent=4)
            os.replace(temp_status_path, status_path)

        # Save round action chunks as .npz at the end of each round
        if round_action_chunks:
            npz_filename = os.path.join(output_dir, f"round_{round_idx}_action_chunks.npz")
            np.savez_compressed(
                npz_filename,
                action_chunks=np.array(round_action_chunks),
                metadata=np.array(round_query_metadata, dtype=object)
            )
            print(f"Saved action chunks for round {round_idx} to: {npz_filename}")

    # Write final run manifest
    package_versions = {
        "torch": str(torch.__version__),
        "transformers": "4.40.1 (moojink fork)",
        "accelerate": "1.14.0",
        "bitsandbytes": "0.42.0"
    }
    manifest = {
        "model_id": cfg.pretrained_checkpoint,
        "quantization": "8-bit",
        "unnorm_key": cfg.unnorm_key,
        "action_chunk_size": NUM_ACTIONS_CHUNK,
        "max_steps": max_steps,
        "suite": cfg.task_suite_name,
        "package_versions": package_versions,
        "compatibility_patch_used": True,
        "ACE_AVAILABLE": "NO",
        "OPENVLA_ACTION_FEATURES_SAVED": "YES",
        "HISTORY_SAVED": "YES",
        "total_episodes_collected": status["total_episodes_completed"]
    }
    manifest_path = os.path.join(output_dir, "run_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=4)
    print(f"Saved run manifest to {manifest_path}")

    print("\n=======================================================")
    print("=== Collection Completed successfully! ===")
    print("=======================================================")
    tee.close()

if __name__ == "__main__":
    main()
