#!/usr/bin/env python3
"""
run_openvla_goal_object_pro_correct_smoke_bob.py

Runs isolated 10-task smoke rollouts for OpenVLA-OFT on LIBERO libero_goal_object on Bob.
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
    from robosuite.utils.mjcf_utils import new_site

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
                    for part in all_bodies:
                        sites = part.findall("./site")
                        joints = part.findall("./joint")
                        # Do not break if no sites, just continue searching other parts
                        for site in sites:
                            site_name = site.get("name")
                            
                            # Flexible matcher to handle naming mismatches like top_site vs top_region
                            site_name_clean = site_name.replace("_site", "").replace("_region", "")
                            target_name_clean = object_region_name.replace("_site", "").replace("_region", "")
                            
                            if site_name == object_region_name or (site_name_clean == target_name_clean and site_name_clean != ""):
                                actual_site_name = site_name
                                if site_name != object_region_name:
                                    # Create and append the missing site with the expected BDDL name
                                    # to the XML part so MuJoCo compiles it
                                    new_site_el = new_site(
                                        name=object_region_name,
                                        pos=site.get("pos"),
                                        quat=site.get("quat") if site.get("quat") is not None else "1 0 0 0",
                                        rgba=site.get("rgba"),
                                        size=site.get("size"),
                                        type=site.get("type") if site.get("type") is not None else "sphere",
                                    )
                                    part.append(new_site_el)
                                    actual_site_name = object_region_name
                                    
                                object_sites_dict[object_region_name] = SiteObject(
                                    name=actual_site_name,
                                    parent_name=body.name,
                                    joints=[joint.get("name") for joint in joints],
                                    size=site.get("size"),
                                    rgba=site.get("rgba"),
                                    site_type=site.get("type"),
                                    site_pos=site.get("pos"),
                                    site_quat=site.get("quat") if site.get("quat") is not None else "1 0 0 0",
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

def save_rollout_video_custom(rollout_images, task_id, success, task_description, output_dir):
    """Saves an MP4 (or GIF fallback) replay of an episode directly to the output directory."""
    import imageio
    os.makedirs(output_dir, exist_ok=True)
    date_time = time.strftime("%Y_%m_%d-%H_%M_%S")
    processed_task_description = task_description.lower().replace(" ", "_").replace("\n", "_").replace(".", "_")[:50]
    
    mp4_path = os.path.join(output_dir, f"{date_time}--openvla_oft--task={task_id}--success={success}--name={processed_task_description}.mp4")
    gif_path = os.path.join(output_dir, f"{date_time}--openvla_oft--task={task_id}--success={success}--name={processed_task_description}.gif")
    
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
        free, total = torch.cuda.mem_get_info()
        return {
            "free_GB": float(free / (1024**3)),
            "total_GB": float(total / (1024**3))
        }
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
    output_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/goal_object_pro_correct_smoke_20260617"
    log_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/goal_object_pro_correct_smoke_20260617"
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)
    
    log_filepath = os.path.join(log_dir, "stdout_stderr.log")
    tee = Tee(log_filepath, "w")
    
    print("\n=======================================================")
    print("=== OpenVLA-OFT 10-Task Corrected Smoke Runner ===")
    print("=======================================================")
    
    mem = get_gpu_memory()
    print(f"GPU Memory Before Load: {mem['free_GB']:.2f} GB free / {mem['total_GB']:.2f} GB total")

    cfg = MockConfig(num_trials=1, seed=0)
    set_seed_everywhere(cfg.seed)

    # 1. Load VLA Model
    print("Loading VLA Model...")
    t0_load = time.time()
    vla = get_vla(cfg)
    openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    print(f"Model loaded in {time.time() - t0_load:.1f}s.")

    processor = get_processor(cfg)
    llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
    proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = get_action_head(cfg, llm_dim=llm_dim)

    # 2. Load LIBERO task suite
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict[cfg.task_suite_name]()
    num_tasks = task_suite.get_num_tasks()
    
    print(f"[info] Using default task order for benchmark '{cfg.task_suite_name}' ({num_tasks} tasks).")
    print(f"Resolved Suite Name: {cfg.task_suite_name}")
    print(f"Task Count: {num_tasks}")
    print("Task IDs and Names:")
    for task_id in range(num_tasks):
        print(f"  Task {task_id}: {task_suite.get_task(task_id).language}")
    
    bddl_path_root = os.path.dirname(task_suite.get_task_bddl_file_path(0))
    init_state_path_root = os.path.dirname(os.path.join(
        benchmark.get_libero_path("init_states"),
        task_suite.tasks[0].problem_folder,
        task_suite.tasks[0].init_states_file,
    ))
    print(f"BDDL Path Root: {bddl_path_root}")
    print(f"Init-State Path Root: {init_state_path_root}")

    suite_info = {
        "suite_name": cfg.task_suite_name,
        "task_count": num_tasks,
        "bddl_path_root": bddl_path_root,
        "init_state_path_root": init_state_path_root,
        "tasks": [{"task_id": i, "task_name": task_suite.get_task(i).language} for i in range(num_tasks)]
    }
    with open(os.path.join(output_dir, "suite_info.json"), "w") as f:
        json.dump(suite_info, f, indent=4)

    max_steps = 800
    print(f"Max steps: {max_steps}")

    resize_size = get_image_resize_size(cfg)
    episode_summaries_path = os.path.join(output_dir, "episode_summaries.jsonl")

    # Run smoke test for each task
    for task_id in range(num_tasks):
        task = task_suite.get_task(task_id)
        initial_states = task_suite.get_task_init_states(task_id)
        
        print(f"\n--- Starting Smoke Test for Task {task_id}/{num_tasks - 1} ---")
        print(f"Task Instruction: {task.language}")

        # Seed and initialize env
        set_seed_everywhere(0)
        env, task_description = get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
        
        env.reset()
        # Seed 0, trial index 0 selects the first init state
        obs = env.set_init_state(initial_states[0])

        action_queue = deque(maxlen=cfg.num_open_loop_steps)
        t = 0
        success = False
        num_queries = 0
        replay_images = []
        action_inference_times = []
        first_action_chunk_shape = None
        trial_exception = None

        t0_rollout = time.time()
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
                    action_inference_times.append(time.time() - t_query_start)
                    num_queries += 1
                    
                    actions_np = np.array(actions)
                    if first_action_chunk_shape is None:
                        first_action_chunk_shape = list(actions_np.shape)

                    print(f"[Query {num_queries}] Predicted action chunk shape: {actions_np.shape}. Horizon prediction H={actions_np.shape[0]}, Executed H={actions_np.shape[0]}.")
                    action_queue.extend(actions)

                # Get and execute action
                action = action_queue.popleft()
                action_processed = process_action(action, cfg.model_family)
                
                obs, reward, done, info = env.step(action_processed.tolist())

                if done:
                    success = True
                    break
                t += 1

        except Exception as e:
            trial_exception = str(e)
            print(f"Task {task_id} failed with exception: {e}")
            import traceback
            traceback.print_exc()

        env.close()
        total_time = time.time() - t0_rollout
        num_steps = t - cfg.num_steps_wait
        avg_inference_time = np.mean(action_inference_times) if action_inference_times else 0.0

        print(f"Task {task_id} finished in {total_time:.1f}s.")
        print(f"Success: {success}, Steps: {num_steps}, Queries: {num_queries}")

        # Save rollout video
        if len(replay_images) > 0:
            try:
                save_rollout_video_custom(replay_images, task_id, success, task.language, output_dir)
            except Exception as video_err:
                print(f"Failed to save video: {video_err}")

        # Save summary record
        summary_record = {
            "task_id": task_id,
            "task_name": task.language,
            "success": success,
            "num_steps": num_steps,
            "num_queries": num_queries,
            "total_wall_time": total_time,
            "average_action_inference_time": avg_inference_time,
            "first_action_chunk_shape": first_action_chunk_shape,
            "failure_message": trial_exception
        }
        with open(episode_summaries_path, "a") as f:
            f.write(json.dumps(summary_record) + "\n")

    print("\n=======================================================")
    print("=== Smoke Test Suite Completed successfully! ===")
    print("=======================================================")
    tee.close()

if __name__ == "__main__":
    main()
