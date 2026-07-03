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

# Monkeypatch Libero_Tabletop_Manipulation._load_sites_in_arena to fix break-vs-continue bug in wine_rack_stand_1_top_region
from libero.libero.envs import TASK_MAPPING
Libero_Tabletop_Manipulation = TASK_MAPPING["libero_tabletop_manipulation"]
from libero.libero.envs.problems.libero_tabletop_manipulation import TargetZone, SiteObject, new_site

def patched_load_sites_in_arena(self, mujoco_arena):
    import xml.etree.ElementTree as ET
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
        for query_dict in [self.objects_dict, self.fixtures_dict]:
            for (name, body) in query_dict.items():
                try:
                    if "worldbody" not in list(body.__dict__.keys()):
                        continue
                except:
                    continue
                
                root_body = body.worldbody.find("body")
                all_parts = [root_body] + (root_body.findall(".//body") if root_body is not None else [])
                for part in all_parts:
                    if part is None:
                        continue
                    sites = part.findall("./site")
                    joints = part.findall("./joint")
                    for site in sites:
                        site_name = site.get("name")
                        is_match = (site_name == object_region_name)
                        if not is_match:
                            if object_region_name.endswith("_region") and site_name.endswith("_site"):
                                is_match = (object_region_name[:-7] == site_name[:-5])
                            elif object_region_name.endswith("_site") and site_name.endswith("_region"):
                                is_match = (object_region_name[:-5] == site_name[:-7])
                        
                        if is_match:
                            size_str = site.get("size", "0.005")
                            if len(size_str.split()) == 1:
                                size_str = f"{size_str} {size_str} {size_str}"
                                
                            existing_site = body._obj.find(f".//site[@name='{object_region_name}']")
                            if existing_site is None:
                                existing_site = body._obj.find(f".//site[@name='{site_name}']")
                                
                            if existing_site is not None:
                                if existing_site.get("name") != object_region_name:
                                    existing_site.set("name", object_region_name)
                            else:
                                new_site_el = ET.Element("site", attrib={
                                    "name": object_region_name,
                                    "pos": site.get("pos", "0 0 0"),
                                    "quat": site.get("quat", "1 0 0 0"),
                                    "size": size_str,
                                    "rgba": site.get("rgba", "0 0 0 0"),
                                    "type": site.get("type", "box"),
                                })
                                body._obj.append(new_site_el)
                            
                            object_sites_dict[object_region_name] = SiteObject(
                                name=object_region_name,
                                parent_name=body.name,
                                joints=[joint.get("name") for joint in joints],
                                size=size_str,
                                rgba=site.get("rgba"),
                                site_type=site.get("type", "box"),
                                site_pos=site.get("pos", "0 0 0"),
                                site_quat=site.get("quat", "1 0 0 0"),
                                object_properties=body.object_properties,
                            )
    self.object_sites_dict = object_sites_dict

    for query_dict in [self.fixtures_dict, self.objects_dict]:
        for name, body in query_dict.items():
            if body.object_properties["vis_site_names"] != {}:
                self.visualization_sites_list.append(name)

Libero_Tabletop_Manipulation._load_sites_in_arena = patched_load_sites_in_arena


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
            
    steps_executed = t - num_steps_wait
    print(f"Rollout {mode_name} finished. Success: {success}. Steps: {steps_executed}")
    
    video_path = output_dir / f"smoke_{mode_name}_rollout.mp4"
    imageio.mimwrite(
        video_path,
        [np.asarray(x) for x in replay_images],
        fps=10,
    )
    
    summary = {
        "mode": mode_name,
        "success": bool(success),
        "steps": int(steps_executed),
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

def main():
    checkpoint_dir = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/pi05_libero"
    config_name = "pi05_libero"
    output_dir = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/outputs")
    
    print("Loading policy...")
    policy = _policy_config.create_trained_policy(
        _config.get_config(config_name), 
        checkpoint_dir
    )
    
    print("Initializing task suite...")
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict["libero_goal_object"]()
    
    results = {}
    
    for task_id in range(10):
        print(f"\n================ Task {task_id} / 10 ================")
        task = task_suite.get_task(task_id)
        initial_states = task_suite.get_task_init_states(task_id)
        task_description = task.language
        print(f"Task instruction: {task_description}")
        
        task_bddl_file = pathlib.Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
        env_args = {"bddl_file_name": task_bddl_file, "camera_heights": 256, "camera_widths": 256}
        env = OffScreenRenderEnv(**env_args)
        
        try:
            summary = run_rollout(
                policy=policy,
                env=env,
                task_description=task_description,
                initial_states=initial_states,
                episode_idx=0,
                seed=10,
                mode_name=f"one_camera_task{task_id}",
                mask_left_wrist_false=True,
                zero_wrist=True,
                max_steps=800,
                output_dir=output_dir
            )
            results[task_id] = summary
        except Exception as e:
            print(f"Failed task {task_id} rollout: {e}")
            results[task_id] = {"success": False, "steps": -1, "error": str(e)}
        finally:
            env.close()
            
    print("\n================ All tasks completed ================")
    for task_id, res in results.items():
        print(f"Task {task_id}: Success={res.get('success')}, Steps={res.get('steps')}")
        
    summary_file = output_dir / "smoke_10tasks_one_camera_summary.json"
    with open(summary_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nFull summary written to {summary_file}")

if __name__ == "__main__":
    main()
