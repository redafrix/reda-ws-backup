#!/usr/bin/env python3
import sys
import os
import pathlib
import collections
import json
import math
import time
import traceback
import argparse
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

# Set LIBERO_CONFIG_PATH before any imports from libero
os.environ["LIBERO_CONFIG_PATH"] = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"

# Add openpi src and LIBERO-PRO repository paths
sys.path.insert(0, "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi/src")



from openpi.policies import policy_config as _policy_config
from openpi.training import config as _config
from openpi.policies import libero_policy
from openpi_client import image_tools
from openpi.models import model as _model

import jax
import jax.numpy as jnp

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
                            # Parse size and pad to 3D if 1D
                            size_str = site.get("size", "0.005")
                            if len(size_str.split()) == 1:
                                size_str = f"{size_str} {size_str} {size_str}"
                                
                            # Dynamic XML injection to append/rename site in body._obj
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


def obs_to_proprio(obs):
    ee_pos = np.asarray(obs.get("robot0_eef_pos", np.zeros(3)), dtype=np.float32)
    ee_quat = np.asarray(obs.get("robot0_eef_quat", np.array([0, 0, 0, 1.0])), dtype=np.float32)
    grip = np.asarray(obs.get("robot0_gripper_qpos", np.zeros(2)), dtype=np.float32)
    state = np.concatenate([ee_pos, _quat2axisangle(ee_quat).astype(np.float32), grip])[:8]
    if state.size < 8:
        state = np.pad(state, (0, 8 - state.size))
    return state.astype(np.float32)


def check_success(env):
    for obj in [env, getattr(env, "env", None), getattr(env, "base_env", None)]:
        if obj is None:
            continue
        fn = getattr(obj, "_check_success", None) or getattr(obj, "check_success", None)
        if callable(fn):
            try:
                return bool(fn())
            except Exception:
                pass
    return False


def compute_ace_metrics(ace_chunks_normalized):
    chunks = np.asarray(ace_chunks_normalized, dtype=np.float32)
    if chunks.ndim != 3 or chunks.shape[0] < 2:
        return np.zeros(7, dtype=np.float32)
    n_seeds = chunks.shape[0]
    flat = chunks.reshape(n_seeds, -1)
    cov = np.cov(flat, rowvar=False)
    eps = 1e-6
    _sign, logdet = np.linalg.slogdet(cov + eps * np.eye(flat.shape[1]))
    entropy = 0.5 * (flat.shape[1] * (1.0 + np.log(2 * np.pi)) + logdet)
    diffs = flat[:, None, :] - flat[None, :, :]
    dists = np.sqrt(np.sum(diffs * diffs, axis=-1))
    mean_pairwise = np.sum(dists) / (n_seeds * (n_seeds - 1))
    per_step_std = float(np.mean(np.std(chunks, axis=0)))
    trans_std = float(np.mean(np.std(chunks[:, :, :3], axis=0)))
    rot_std = float(np.mean(np.std(chunks[:, :, 3:6], axis=0)))
    grip_std = float(np.mean(np.std(chunks[:, :, 6:], axis=0)))
    flat_std = float(np.mean(np.std(flat, axis=0)))
    return np.asarray([entropy, mean_pairwise, per_step_std, trans_std, rot_std, grip_std, flat_std], dtype=np.float32)


def history_array(history, history_steps=16):
    out = np.zeros((history_steps, 21), dtype=np.float32)
    src = list(history)[-history_steps:]
    offset = history_steps - len(src)
    for i, (prop, act, ace) in enumerate(src):
        out[offset + i, :] = np.concatenate([prop, act, ace[:6]]).astype(np.float32)
    return out


def infer_actions(policy, obs, noise=None):
    # Make a copy since transformations may modify the inputs in place.
    inputs = jax.tree.map(lambda x: x, obs)
    inputs = policy._input_transform(inputs)
    
    if not policy._is_pytorch_model:
        # Make a batch and convert to jax.Array.
        inputs = jax.tree.map(lambda x: jnp.asarray(x)[np.newaxis, ...], inputs)
        policy._rng, sample_rng = jax.random.split(policy._rng)
        sample_device_or_rng = sample_rng
    else:
        inputs = jax.tree.map(lambda x: torch.from_numpy(np.array(x)).to(policy._pytorch_device)[None, ...], inputs)
        sample_device_or_rng = policy._pytorch_device

    # Prepare kwargs for sample_actions
    sample_kwargs = dict(policy._sample_kwargs)
    if noise is not None:
        if policy._is_pytorch_model:
            noise_t = torch.from_numpy(noise).to(policy._pytorch_device)
        else:
            noise_t = jnp.asarray(noise)

        if noise_t.ndim == 2:
            noise_t = noise_t[None, ...]
        sample_kwargs["noise"] = noise_t

    observation = _model.Observation.from_dict(inputs)
    actions_raw = policy._sample_actions(sample_device_or_rng, observation, **sample_kwargs)
    
    if policy._is_pytorch_model:
        actions_raw_np = np.asarray(actions_raw[0, ...].detach().cpu())
    else:
        actions_raw_np = np.asarray(actions_raw[0, ...])
        
    outputs = {
        "state": inputs["state"],
        "actions": actions_raw,
    }
    if policy._is_pytorch_model:
        outputs = jax.tree.map(lambda x: np.asarray(x[0, ...].detach().cpu()), outputs)
    else:
        outputs = jax.tree.map(lambda x: np.asarray(x[0, ...]), outputs)

    postprocessed_outputs = policy._output_transform(outputs)
    
    # We index [..., :7] because the policy actions have dimension 7 (rest is padding)
    return postprocessed_outputs["actions"], actions_raw_np[..., :7]


def append_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--num-episodes-per-task", type=int, default=10)
    parser.add_argument("--max-steps", type=int, default=800)
    parser.add_argument("--seed-start", type=int, default=10)
    args = parser.parse_args()

    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_dir = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/pi05_libero"
    config_name = "pi05_libero"
    
    print("Loading policy...", flush=True)
    policy = _policy_config.create_trained_policy(
        _config.get_config(config_name), 
        checkpoint_dir
    )
    
    print("Initializing task suite...", flush=True)
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict["libero_goal_object"]()
    
    manifest = {
        "schema_version": "pi05_libero_goal_object_v1_manifest",
        "created_at": now_iso(),
        "checkpoint": checkpoint_dir,
        "num_episodes_per_task": args.num_episodes_per_task,
        "max_steps": args.max_steps,
        "seed_start": args.seed_start,
    }
    with open(output_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    total_episodes = 0
    start_time = time.time()
    
    # Sequential round-robin by task
    # task0 ep0, task1 ep0, ..., task9 ep0, task0 ep1, ...
    for rollout_idx in range(args.num_episodes_per_task):
        for task_id in range(10):
            episode_id = f"pi05_t{task_id}_r{rollout_idx}"
            video_path = output_dir / f"{episode_id}.mp4"
            if video_path.exists():
                total_episodes += 1
                print(f"[episode-skip] {episode_id} already exists, skipping.", flush=True)
                continue
                
            episode_start = time.time()
            print(f"\n[episode-start] {episode_id} (Task {task_id}, Episode index {rollout_idx})", flush=True)
            
            task = task_suite.get_task(task_id)
            initial_states = task_suite.get_task_init_states(task_id)
            task_description = task.language
            print(f"Task instruction: {task_description}", flush=True)
            
            env = None
            episode_rows = []
            success = False
            error_message = ""
            
            try:
                task_bddl_file = pathlib.Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
                env_args = {"bddl_file_name": task_bddl_file, "camera_heights": 256, "camera_widths": 256}
                env = OffScreenRenderEnv(**env_args)
                
                env_seed = args.seed_start + task_id + 1000 * rollout_idx
                env.seed(env_seed)
                env.reset()
                
                init_state_idx = rollout_idx % len(initial_states)
                obs = env.set_init_state(initial_states[init_state_idx])
                
                # Reset history deque
                history = collections.deque(maxlen=16)
                
                t = 0
                num_steps_wait = 10
                action_plan = collections.deque()
                action_plan_norm = collections.deque()
                replay_images = []
                
                while t < args.max_steps + num_steps_wait:
                    # Let the robot settle first
                    if t < num_steps_wait:
                        obs, reward, done, info = env.step([0.0] * 6 + [-1.0])
                        t += 1
                        continue
                        
                    img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
                    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
                    
                    img_resized = image_tools.convert_to_uint8(
                        image_tools.resize_with_pad(img, 224, 224)
                    )
                    wrist_img_resized = image_tools.convert_to_uint8(
                        image_tools.resize_with_pad(wrist_img, 224, 224)
                    )
                    
                    replay_images.append(img_resized)
                    
                    proprio_np = obs_to_proprio(obs)
                    
                    # Policy queries occur every 10 steps (horizon chunk size = 10)
                    if not action_plan:
                        element = {
                            "observation/image": img_resized,
                            "observation/wrist_image": wrist_img_resized,
                            "observation/state": proprio_np,
                            "prompt": str(task_description),
                        }
                        
                        # 1. Main action chunk inference (both unnormalized and normalized)
                        main_chunk, main_chunk_norm = infer_actions(policy, element)
                        
                        # 2. Candidate action chunks inference (8 flow noise seeds)
                        candidates_norm = []
                        candidates_env = []
                        for i in range(8):
                            rng = np.random.default_rng(seed=i)
                            noise = rng.normal(size=(10, 32))  # Model action dim is 32
                            cand_env, cand_norm = infer_actions(policy, element, noise=noise)
                            candidates_norm.append(cand_norm)
                            candidates_env.append(cand_env)
                            
                        candidates_norm = np.stack(candidates_norm)  # (8, 10, 7)
                        candidates_env = np.stack(candidates_env)    # (8, 10, 7)
                        
                        # Compute ACE metrics
                        ace = compute_ace_metrics(candidates_norm)
                        
                        action_plan.extend(main_chunk[:10])
                        action_plan_norm.extend(main_chunk_norm[:10])
                        
                    # Execute policy action
                    act = action_plan.popleft()
                    act_norm = action_plan_norm.popleft()
                    
                    # Generate history array for the current timestep
                    hist_16x21 = history_array(history, 16)
                    
                    # Construct data row
                    row = {
                        "episode_id": episode_id,
                        "suite": "libero_goal_object",
                        "task_id": task_id,
                        "task_language": task_description,
                        "timestep": t - num_steps_wait,
                        "env_seed": env_seed,
                        "init_state_idx": init_state_idx,
                        "proprio": proprio_np.tolist(),
                        "executed_action": act.tolist(),
                        "main_action_chunk": main_chunk.tolist(),
                        "main_action_chunk_normalized": main_chunk_norm.tolist(),
                        "candidate_action_chunks": candidates_env.tolist(),
                        "candidate_action_chunks_normalized": candidates_norm.tolist(),
                        "ace": ace.tolist(),
                        "history_16x21": hist_16x21.tolist(),
                        "uncertainty_topk8": [0.0] * 8,  # Masked as zeros for Pi0.5
                    }
                    episode_rows.append(row)
                    
                    # Step environment
                    obs, reward, done, info = env.step(act.tolist())
                    success = bool(reward > 0.0) or check_success(env)
                    
                    # Append (proprio_np, act_norm, ace) to history deque
                    history.append((proprio_np, act_norm, ace))
                    
                    if done or success:
                        break
                    t += 1
                    
            except Exception as e:
                error_message = "".join(traceback.format_exception_only(type(e), e)).strip()
                print(f"[episode-error] {episode_id}: {error_message}", flush=True)
                traceback.print_exc()
            finally:
                if env is not None:
                    try:
                        env.close()
                    except Exception:
                        pass
                
            # Add outcome to all rows and save them
            outcome_str = "success" if success else "failure_or_timeout"
            if error_message:
                outcome_str = "error"
                
            for r in episode_rows:
                r["success"] = success
                r["outcome"] = outcome_str
                
            if episode_rows:
                append_jsonl(output_dir / "episode_rows.jsonl", episode_rows)
                
            # Save video of rollout
            video_path = output_dir / f"{episode_id}.mp4"
            imageio.mimwrite(
                video_path,
                [np.asarray(x) for x in replay_images],
                fps=10,
            )
            
            episode_seconds = time.time() - episode_start
            summary = {
                "episode_id": episode_id,
                "suite": "libero_goal_object",
                "task_id": task_id,
                "rollout_idx": rollout_idx,
                "outcome": outcome_str,
                "success": success,
                "steps": len(episode_rows),
                "wall_time_seconds": episode_seconds,
                "error_message": error_message,
                "video_path": str(video_path),
            }
            append_jsonl(output_dir / "episode_summaries.jsonl", [summary])
            total_episodes += 1
            
            print(f"[episode-finished] {episode_id} outcome={outcome_str} steps={len(episode_rows)} time={episode_seconds:.1f}s total={total_episodes}", flush=True)
            
    total_seconds = time.time() - start_time
    print(f"\n[collection-finished] Total episodes: {total_episodes}. Total time: {total_seconds/3600:.2f} hours.", flush=True)

if __name__ == "__main__":
    main()
