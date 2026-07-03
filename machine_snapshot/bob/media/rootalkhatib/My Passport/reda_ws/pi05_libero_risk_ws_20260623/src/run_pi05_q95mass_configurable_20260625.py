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
import torch
import torch.nn as nn

# Monkeypatch torch.load to default weights_only=False for compatibility
original_load = torch.load
def patched_load(*args, **kwargs):
    if "weights_only" not in kwargs:
        kwargs["weights_only"] = False
    return original_load(*args, **kwargs)
torch.load = patched_load

# Set LIBERO_CONFIG_PATH before any imports from libero
os.environ["LIBERO_CONFIG_PATH"] = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"

# Add repository paths
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

# Monkeypatch Libero_Tabletop_Manipulation._load_sites_in_arena
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
            if body.object_properties.get("vis_site_names", {}) != {}:
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
    return np.array([mean_pairwise, per_step_std, entropy, 0.0, 0.0, 0.0, 0.0], dtype=np.float32)


def history_array(history, history_steps=16):
    out = np.zeros((history_steps, 21), dtype=np.float32)
    src = list(history)[-history_steps:]
    offset = history_steps - len(src)
    for i, (prop, act, ace) in enumerate(src):
        out[offset + i, :] = np.concatenate([prop, act, ace[:6]]).astype(np.float32)
    return out


def infer_actions(policy, obs, noise=None):
    inputs = jax.tree.map(lambda x: x, obs)
    inputs = policy._input_transform(inputs)
    
    if not policy._is_pytorch_model:
        inputs = jax.tree.map(lambda x: jnp.asarray(x)[np.newaxis, ...], inputs)
        policy._rng, sample_rng = jax.random.split(policy._rng)
        sample_device_or_rng = sample_rng
    else:
        inputs = jax.tree.map(lambda x: torch.from_numpy(np.array(x)).to(policy._pytorch_device)[None, ...], inputs)
        sample_device_or_rng = policy._pytorch_device

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
    return postprocessed_outputs["actions"], actions_raw_np[..., :7]


def append_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


# Normalization functions matching training
def apply_seq_standardizer(x, stats):
    mean = np.array(stats["mean"], dtype=np.float32)
    std = np.array(stats["std"], dtype=np.float32)
    return np.clip((x - mean) / std, -10.0, 10.0).astype(np.float32)

def apply_standardizer(x, stats):
    mean = np.array(stats["mean"], dtype=np.float32)
    std = np.array(stats["std"], dtype=np.float32)
    return np.clip((x - mean) / std, -10.0, 10.0).astype(np.float32)

# SeqRiskModel matching training exactly
class SeqRiskModel(nn.Module):
    def __init__(self, hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1):
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(
            width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu"
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)
        self.static_in_dropout = nn.Dropout(0.0)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch["static"]))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


def score_candidate(model, stats, h, a, st, device):
    h_std = apply_seq_standardizer(h, stats["history"])
    a_std = apply_seq_standardizer(a, stats["action"])
    st_std = apply_standardizer(st, stats["static"])
    
    batch = {
        "history": torch.tensor(h_std, dtype=torch.float32, device=device).unsqueeze(0),
        "action": torch.tensor(a_std, dtype=torch.float32, device=device).unsqueeze(0),
        "static": torch.tensor(st_std, dtype=torch.float32, device=device).unsqueeze(0),
    }
    with torch.no_grad():
        logits = model(batch)
        score = torch.sigmoid(logits).item()
    return score


def select_candidate(scores, main_threshold, min_margin, strong_margin, max_selected_score, q95, q99):
    main_score = float(scores[0])
    eligible = list(range(1, len(scores)))
    
    if len(eligible) == 0:
        return 0, "no_alternative_candidate"
        
    best_idx = min(eligible, key=lambda i: float(scores[i]))
    best_score = float(scores[best_idx])
    
    if main_score <= best_score:
        return 0, "main_is_lowest"
        
    diff = main_score - best_score
    
    if main_score < main_threshold:
        return 0, "main_below_required_threshold"
        
    if diff < min_margin:
        return 0, "insufficient_margin"
        
    if best_score > max_selected_score:
        return 0, "best_above_max_selected_score_cap"
        
    if best_score < q95:
        return best_idx, "best_below_q95"
        
    if main_score >= q99 and diff >= strong_margin:
        return best_idx, "main_q99_strong_margin"
        
    return 0, "strict_margin_reject"


def run_episode(policy_name, task_id, reset_seed, rollout_idx, task_suite, policy, risk_model, stats, thresholds, args, paths, device):
    task = task_suite.get_task(task_id)
    initial_states = task_suite.get_task_init_states(task_id)
    task_description = task.language
    episode_id = f"pi05_ood_t{task_id}_s{reset_seed}_{policy_name}"
    
    # Adjust problem folder name to libero_goal_object_ood_temp
    if hasattr(task, 'problem_folder') and task.problem_folder == 'libero_goal_object_ood':
        if hasattr(task, '_replace'):
            task = task._replace(problem_folder='libero_goal_object_ood_temp')
        else:
            import copy
            task = copy.copy(task)
            object.__setattr__(task, 'problem_folder', 'libero_goal_object_ood_temp')
            
    print(f"\n[episode-start] {episode_id} task={task_id} seed={reset_seed} instruction={task_description}", flush=True)
    
    env = None
    episode_rows = []
    query_records = []
    replay_images = []
    
    success = False
    error_message = ""
    start = time.time()
    
    q95 = thresholds["q95"]
    q99 = thresholds["q99"]
    
    q95_mass = 0.0
    q95_mass_alarm = False
    modification_count = 0
    
    try:
        task_bddl_file = pathlib.Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
        env_args = {"bddl_file_name": task_bddl_file, "camera_heights": 256, "camera_widths": 256}
        env = OffScreenRenderEnv(**env_args)
        
        env.seed(reset_seed)
        env.reset()
        
        init_state_idx = rollout_idx % len(initial_states)
        obs = env.set_init_state(initial_states[init_state_idx])
        
        history = collections.deque(maxlen=16)
        
        t = 0
        num_steps_wait = 10
        action_plan = collections.deque()
        action_plan_norm = collections.deque()
        
        query_idx = 0
        max_steps = args.max_steps
        
        while t < max_steps + num_steps_wait:
            if t < num_steps_wait:
                obs, reward, done, info = env.step([0.0] * 6 + [-1.0])
                t += 1
                continue
                
            step_idx = t - num_steps_wait
            
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
                hist_16x21 = history_array(history, 16)
                
                # Score all chunks with risk model
                all_chunks = [main_chunk] + list(candidates_env)
                cand_scores = []
                for chunk in all_chunks:
                    action_stats = np.concatenate([chunk[0], chunk.mean(axis=0), chunk.std(axis=0), chunk[-1] - chunk[0]]).astype(np.float32)
                    static = np.concatenate([action_stats, ace, proprio_np, [0.0]*8]).astype(np.float32)
                    
                    score = score_candidate(risk_model, stats, hist_16x21, chunk, static, device)
                    cand_scores.append(score)
                    
                main_score = cand_scores[0]
                
                # Conformal mass accumulator update
                excess = max(0.0, main_score - q95)
                q95_mass += excess
                if q95_mass >= args.mass_threshold:
                    q95_mass_alarm = True
                    
                # Selected-cap candidate selection logic
                selected_idx = 0
                selection_reason = "pi05_risk_selected_cap_topk8_h10_q95mass1_loose"
                if policy_name == "pi05_risk_selected_cap_topk8_h10":
                    if not q95_mass_alarm:
                        selected_idx, selection_reason = 0, f"q95_mass_below_{args.mass_threshold:g}"
                    elif args.selection_mode == "always_select_lowest_after_alarm":
                        best_idx = min(range(len(cand_scores)), key=lambda i: float(cand_scores[i]))
                        if best_idx == 0:
                            selected_idx, selection_reason = 0, "alarm_main_is_lowest"
                        else:
                            selected_idx = int(best_idx)
                            selection_reason = "always_select_lowest_after_alarm"
                    else:
                        selected_idx, selection_reason = select_candidate(
                            scores=cand_scores,
                            main_threshold=args.selection_main_threshold,
                            min_margin=args.selection_min_margin,
                            strong_margin=args.selection_strong_margin,
                            max_selected_score=args.selection_max_selected_score,
                            q95=q95,
                            q99=q99
                        )
                    
                # Execute selected chunk
                if selected_idx == 0:
                    executed_chunk = main_chunk
                    executed_chunk_norm = main_chunk_norm
                else:
                    executed_chunk = candidates_env[selected_idx - 1]
                    executed_chunk_norm = candidates_norm[selected_idx - 1]
                    modification_count += 1
                    
                action_plan.extend(executed_chunk[:10])
                action_plan_norm.extend(executed_chunk_norm[:10])
                
                # Construct query logging record
                exec_action_stats = np.concatenate([executed_chunk[0], executed_chunk.mean(axis=0), executed_chunk.std(axis=0), executed_chunk[-1] - executed_chunk[0]]).astype(np.float32)
                exec_static = np.concatenate([exec_action_stats, ace, proprio_np, [0.0]*8]).astype(np.float32)
                
                qrec = {
                    "suite": "libero_goal_object_ood",
                    "task_id": task_id,
                    "task_language": task_description,
                    "reset_seed": reset_seed,
                    "episode_id": episode_id,
                    "policy_name": policy_name,
                    "env_step": step_idx,
                    "query_index": query_idx,
                    "proprio": proprio_np.tolist(),
                    "main_action_chunk": main_chunk.tolist(),
                    "candidate_action_chunks": candidates_env.tolist(),
                    "ace": ace.tolist(),
                    "uncertainty_topk8": [0.0]*8,
                    "static_features": exec_static.tolist(),
                    "history_16x21": hist_16x21.tolist(),
                    "risk_score_main": main_score,
                    "risk_scores_candidates": cand_scores,
                    "selected_candidate_index": int(selected_idx),
                    "proposed_candidate_index": int(selected_idx),
                    "selection_reason": selection_reason,
                    "replaced_by_selected_cap": bool(selected_idx != 0),
                    "raw_score_threshold_status": bool(main_score >= args.selection_main_threshold),
                    "q95_mass_value": q95_mass,
                    "q95_alarm_fired": q95_mass_alarm,
                    "executed_chunk": executed_chunk.tolist(),
                    "executed_horizon": 10,
                    "success": False,
                    "final_episode_length": 0
                }
                query_records.append(qrec)
                query_idx += 1
                
            # Execute step action
            act = action_plan.popleft()
            act_norm = action_plan_norm.popleft()
            
            # Step environment
            obs, reward, done, info = env.step(act.tolist())
            done = bool(done)
            success = bool(reward > 0.0) or check_success(env)
            success = bool(success)
            
            # Construct step record
            step_rec = {
                "episode_id": episode_id,
                "policy_name": policy_name,
                "task_id": task_id,
                "reset_seed": reset_seed,
                "env_step": step_idx,
                "proprio": proprio_np.tolist(),
                "executed_action": act.tolist(),
                "executed_action_normalized": act_norm.tolist(),
                "ace_step": ace.tolist(),
                "success": success,
                "done": done
            }
            episode_rows.append(step_rec)
            
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
                
    # Complete episode stats updates
    outcome_str = "success" if success else "failure_or_timeout"
    if error_message:
        outcome_str = "error"
        
    final_len = len(episode_rows)
    for r in episode_rows:
        r["success"] = success
        r["outcome"] = outcome_str
        
    for q in query_records:
        q["success"] = success
        q["final_episode_length"] = final_len
        
    if episode_rows:
        append_jsonl(paths["step_records"], episode_rows)
    if query_records:
        append_jsonl(paths["query_records"], query_records)
        
    # Save video
    video_path = paths["video_dir"] / f"{episode_id}.mp4"
    imageio.mimwrite(
        video_path,
        [np.asarray(x) for x in replay_images],
        fps=10,
    )
    
    episode_seconds = time.time() - start
    summary = {
        "episode_id": episode_id,
        "policy": policy_name,
        "suite": "libero_goal_object_ood",
        "task_id": task_id,
        "reset_seed": reset_seed,
        "success": success,
        "outcome": outcome_str,
        "steps": final_len,
        "wall_time_seconds": episode_seconds,
        "error_message": error_message,
        "video_path": str(video_path),
        "action_modifications_count": modification_count,
        "q95_mass_alarm_fired": q95_mass_alarm,
        "q95_mass_final_value": q95_mass
    }
    
    print(f"[episode-finished] {episode_id} outcome={outcome_str} steps={final_len} time={episode_seconds:.1f}s mass={q95_mass:.4f} alarm={q95_mass_alarm}", flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=str, required=True)
    parser.add_argument("--seed-start", type=int, default=200)
    parser.add_argument("--episodes-per-task", type=int, default=10)
    parser.add_argument("--max-steps", type=int, default=800)
    parser.add_argument("--task-ids", type=str, default="9,12")
    parser.add_argument("--policies", type=str, default="pi05_risk_selected_cap_topk8_h10")
    parser.add_argument("--rollout-start", type=int, default=0)
    parser.add_argument("--mass-threshold", type=float, default=1.0)
    parser.add_argument("--selection-mode", type=str, default="selected_cap", choices=["selected_cap", "always_select_lowest_after_alarm"])
    parser.add_argument("--selection-main-threshold", type=float, default=0.7218163013458249)
    parser.add_argument("--selection-min-margin", type=float, default=0.005)
    parser.add_argument("--selection-strong-margin", type=float, default=0.02)
    parser.add_argument("--selection-max-selected-score", type=float, default=0.95)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    
    output_root = pathlib.Path(args.output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    
    checkpoint_dir = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/pi05_libero"
    config_name = "pi05_libero"
    
    model_path = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_20260625/models/model.pt"
    thresholds_path = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_20260625/models/thresholds.json"
    norm_path = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_20260625/models/normalization.json"
    
    print("Loading Policy...", flush=True)
    policy = _policy_config.create_trained_policy(
        _config.get_config(config_name), 
        checkpoint_dir
    )
    
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Loading Risk Model on {device}...", flush=True)
    risk_model = SeqRiskModel(hist_dim=21, action_dim=7, static_dim=51)
    risk_model.load_state_dict(torch.load(model_path, map_location=device))
    risk_model.to(device)
    risk_model.eval()
    
    with open(thresholds_path) as f:
        thresholds = json.load(f)
    with open(norm_path) as f:
        stats = json.load(f)
        
    print("Initializing task suite libero_goal_object_ood...", flush=True)
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict["libero_goal_object_ood"]()
    n_tasks = task_suite.get_num_tasks()
    
    policies = [x.strip() for x in args.policies.split(",") if x.strip()]
    task_ids = [int(x.strip()) for x in args.task_ids.split(",") if x.strip()]
    for task_id in task_ids:
        if task_id < 0 or task_id >= n_tasks:
            raise ValueError(f"task_id {task_id} out of range for suite with {n_tasks} tasks")
    
    if args.smoke:
        print("\n*** RUNNING IN SMOKE MODE ***", flush=True)
        task_ids = [0, 8]
        args.episodes_per_task = 1
        args.max_steps = 100
        
    policy_paths = {}
    for p in policies:
        pdir = output_root / f"policy_{p}"
        pdir.mkdir(parents=True, exist_ok=True)
        vdir = pdir / "videos"
        vdir.mkdir(parents=True, exist_ok=True)
        
        policy_paths[p] = {
            "dir": pdir,
            "video_dir": vdir,
            "summaries": pdir / "episode_summaries.jsonl",
            "query_records": pdir / "query_records.jsonl",
            "step_records": pdir / "step_records.jsonl",
        }
        
    manifest = {
        "suite": "libero_goal_object_ood",
        "task_count": len(task_ids),
        "task_ids": task_ids,
        "policies": policies,
        "episodes_per_task": args.episodes_per_task,
        "seed_start": args.seed_start,
        "max_steps": args.max_steps,
        "risk_model_path": model_path,
        "risk_thresholds": thresholds,
        "selected_cap_controls": {
            "policy": "q95_mass_then_configurable_selection",
            "mass_threshold": args.mass_threshold,
            "selection_main_threshold": args.selection_main_threshold,
            "selection_min_margin": args.selection_min_margin,
            "selection_strong_margin": args.selection_strong_margin,
            "selection_max_selected_score": args.selection_max_selected_score,
            "selection_mode": args.selection_mode,
            "rollout_start": args.rollout_start
        },
        "created_at": time.strftime('%Y-%m-%d %H:%M:%S'),
        "smoke": args.smoke
    }
    for p in policies:
        with open(policy_paths[p]["dir"] / "run_manifest.json", "w") as f:
            json.dump(manifest, f, indent=2)
            
    completed = set()
    for p in policies:
        sum_file = policy_paths[p]["summaries"]
        if sum_file.exists():
            with open(sum_file) as f:
                for line in f:
                    if line.strip():
                        r = json.loads(line)
                        completed.add((p, r["task_id"], r["reset_seed"]))
                        
    total = len(policies) * len(task_ids) * args.episodes_per_task
    done_count = len(completed)
    
    print(f"Start execution: {done_count} / {total} episodes completed.", flush=True)
    
    for ep in range(args.episodes_per_task):
        seed = args.seed_start + ep
        for task_id in task_ids:
            for p in policies:
                key = (p, task_id, seed)
                if key in completed:
                    continue
                    
                print(f"\n--- Episode [{done_count+1}/{total}] policy={p} task={task_id} seed={seed} ---", flush=True)
                summary = run_episode(
                    policy_name=p,
                    task_id=task_id,
                    reset_seed=seed,
                    rollout_idx=args.rollout_start + ep,
                    task_suite=task_suite,
                    policy=policy,
                    risk_model=risk_model,
                    stats=stats,
                    thresholds=thresholds,
                    args=args,
                    paths=policy_paths[p],
                    device=device
                )
                
                append_jsonl(policy_paths[p]["summaries"], [summary])
                completed.add(key)
                done_count += 1
                
                status = {
                    "updated_at": time.strftime('%Y-%m-%d %H:%M:%S'),
                    "completed": done_count,
                    "target_total": total,
                    "last_episode_summary": summary,
                    "smoke": args.smoke
                }
                with open(output_root / "live_status.json", "w") as f:
                    json.dump(status, f, indent=2)
                    
    print("\nRUN COMPLETED successfully.", flush=True)

if __name__ == "__main__":
    main()
