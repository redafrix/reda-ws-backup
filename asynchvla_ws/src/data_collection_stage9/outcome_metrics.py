from __future__ import annotations
import numpy as np
from typing import Any
from .libero_pro_env_utils import check_success, obs_to_proprio
from .sim_state_utils import get_sim

def obs_signal_summary(obs: dict) -> dict:
    keys = sorted(list(obs.keys()))
    out = {"obs_keys": keys}
    for k in ["robot0_eef_pos", "robot0_eef_quat", "robot0_gripper_qpos"]:
        if k in obs: out[k] = np.asarray(obs[k]).astype(float).tolist()
    return out

def eef_pos(obs: dict) -> np.ndarray | None:
    if "robot0_eef_pos" in obs: return np.asarray(obs["robot0_eef_pos"], dtype=float)
    return None

def gripper(obs: dict) -> np.ndarray | None:
    if "robot0_gripper_qpos" in obs: return np.asarray(obs["robot0_gripper_qpos"], dtype=float)
    return None

def object_body_positions(env) -> dict[str, list[float]]:
    sim = get_sim(env)
    if sim is None: return {}
    out = {}
    try:
        names = list(sim.model.body_names)
    except Exception:
        names = []
    ignore = ("world", "robot", "gripper", "eef", "mount", "base", "link", "wrist", "camera", "table", "floor")
    for name in names:
        low = str(name).lower()
        if any(x in low for x in ignore):
            continue
        try:
            bid = sim.model.body_name2id(name)
            pos = np.asarray(sim.data.body_xpos[bid], dtype=float)
            out[str(name)] = pos.tolist()
        except Exception:
            pass
    return out

def contact_summary(env) -> dict:
    sim = get_sim(env)
    if sim is None: return {"contact_available": False}
    try:
        ncon = int(sim.data.ncon)
    except Exception:
        return {"contact_available": False}
    names = []
    for i in range(ncon):
        try:
            c = sim.data.contact[i]
            g1 = sim.model.geom_id2name(c.geom1)
            g2 = sim.model.geom_id2name(c.geom2)
            names.append([str(g1), str(g2)])
        except Exception:
            pass
    suspicious = [x for pair in names for x in pair if x and any(t in x.lower() for t in ["table", "floor", "wall"])]
    return {"contact_available": True, "contact_count": ncon, "contacts": names[:20], "bad_contact_count": len(suspicious)}

def obs_pos(obs: dict, base: str | None) -> np.ndarray | None:
    if not base:
        return None
    key = f"{base}_pos"
    if key in obs:
        return np.asarray(obs[key], dtype=float)
    return None

def body_pos_by_prefix(objects: dict, prefix: str | None) -> np.ndarray | None:
    if not prefix:
        return None
    pref = str(prefix).lower()
    for k, v in objects.items():
        if str(k).lower().startswith(pref):
            return np.asarray(v, dtype=float)
    return None

def detect_phase(obs: dict, env: Any, task_context: dict | None, history_stats: dict | None = None) -> str:
    if check_success(env):
        return "PLACE_OR_GOAL"
    
    if not task_context or not task_context.get("target_base"):
        return "UNKNOWN"
    
    target = task_context.get("target_base")
    goal = task_context.get("goal_base")
    
    tb = obs_pos(obs, target)
    if tb is None:
        obj_pos_dict = object_body_positions(env)
        tb = body_pos_by_prefix(obj_pos_dict, task_context.get("target_body_prefix"))
    
    if tb is None:
        return "UNKNOWN"
    
    bp = eef_pos(obs)
    if bp is None:
        return "UNKNOWN"
    
    dist_eef_target = np.linalg.norm(tb - bp)
    target_height = tb[2]
    
    # Stuck detection if history_stats provided (last_N_steps_motion)
    if history_stats and history_stats.get("recent_motion", 1.0) < 0.005:
        return "STUCK_OR_NO_PROGRESS"

    # Goal distance
    gb = obs_pos(obs, goal)
    if gb is None:
        obj_pos_dict = object_body_positions(env)
        gb = body_pos_by_prefix(obj_pos_dict, task_context.get("goal_body_prefix"))
    
    if gb is not None:
        dist_target_goal = np.linalg.norm(tb - gb)
        if dist_target_goal < 0.12:
            return "PLACE_OR_GOAL"
    
    if target_height > 0.12:
        return "TRANSPORT"
    
    if dist_eef_target < 0.06:
        g = gripper(obs)
        if g is not None and np.mean(np.abs(g)) < 0.015:
            return "GRASP_OR_LIFT"
        if target_height > 0.07:
            return "GRASP_OR_LIFT"
        return "NEAR_GRASP"
    
    if dist_eef_target < 0.15:
        return "NEAR_GRASP"
    
    return "APPROACH"

def task_progress(before_obs: dict, after_obs: dict, before_obj: dict, after_obj: dict, task_context: dict | None) -> dict:
    if not task_context:
        return {"task_context_available": False}
    target = task_context.get("target_base")
    goal = task_context.get("goal_base")
    tb = obs_pos(before_obs, target)
    ta = obs_pos(after_obs, target)
    gb = obs_pos(before_obs, goal)
    ga = obs_pos(after_obs, goal)
    if tb is None:
        tb = body_pos_by_prefix(before_obj, task_context.get("target_body_prefix"))
    if ta is None:
        ta = body_pos_by_prefix(after_obj, task_context.get("target_body_prefix"))
    if gb is None:
        gb = body_pos_by_prefix(before_obj, task_context.get("goal_body_prefix"))
    if ga is None:
        ga = body_pos_by_prefix(after_obj, task_context.get("goal_body_prefix"))
    out = {"task_context_available": True, "target_base": target, "goal_base": goal, "relation": task_context.get("relation"), "parse_confidence": task_context.get("parse_confidence")}
    bp, ap = eef_pos(before_obs), eef_pos(after_obs)
    if tb is not None and ta is not None:
        out["target_pos_available"] = True
        out["target_motion"] = float(np.linalg.norm(ta - tb))
        out["target_height_delta"] = float(ta[2] - tb[2])
        out["target_height_drop"] = float(tb[2] - ta[2])
        if bp is not None and ap is not None:
            out["target_to_eef_before"] = float(np.linalg.norm(tb - bp))
            out["target_to_eef_after"] = float(np.linalg.norm(ta - ap))
            out["target_to_eef_delta"] = out["target_to_eef_after"] - out["target_to_eef_before"]
    else:
        out["target_pos_available"] = False
    if tb is not None and ta is not None and gb is not None and ga is not None and target != goal:
        out["goal_pos_available"] = True
        out["target_to_goal_before"] = float(np.linalg.norm(tb - gb))
        out["target_to_goal_after"] = float(np.linalg.norm(ta - ga))
        out["target_to_goal_delta"] = out["target_to_goal_after"] - out["target_to_goal_before"]
    else:
        out["goal_pos_available"] = False
    return out

def relation_distance_changes(before_obs: dict, after_obs: dict) -> dict:
    changes = {}
    for key, bval in before_obs.items():
        if not key.endswith("_to_robot0_eef_pos") or key not in after_obs:
            continue
        try:
            b = float(np.linalg.norm(np.asarray(bval, dtype=float)))
            a = float(np.linalg.norm(np.asarray(after_obs[key], dtype=float)))
            changes[key] = {"before": b, "after": a, "delta_after_minus_before": a - b}
        except Exception:
            pass
    deltas = [v["delta_after_minus_before"] for v in changes.values()]
    return {
        "relation_distance_changes": changes,
        "best_approach_delta": min(deltas) if deltas else None,
        "worst_relation_worsen_delta": max(deltas) if deltas else None,
    }

def compute_delta(before_obs, after_obs, before_obj, after_obj, task_context: dict | None = None) -> dict:
    bp, ap = eef_pos(before_obs), eef_pos(after_obs)
    eef_delta = float(np.linalg.norm(ap-bp)) if bp is not None and ap is not None else None
    object_deltas = {}
    height_drops = {}
    for k,v in before_obj.items():
        if k in after_obj:
            b=np.asarray(v); a=np.asarray(after_obj[k]); object_deltas[k]=float(np.linalg.norm(a-b)); height_drops[k]=float(b[2]-a[2])
    rel = relation_distance_changes(before_obs, after_obs)
    task = task_progress(before_obs, after_obs, before_obj, after_obj, task_context)
    return {"eef_delta": eef_delta, "object_delta_max": max(object_deltas.values()) if object_deltas else None, "object_deltas": object_deltas, "height_drop_max": max(height_drops.values()) if height_drops else None, "height_drops": height_drops, **rel, "task_progress": task}

def execute_action_chunk(env, action_chunk, horizon: int, before_obs: dict, task_context: dict | None = None, return_after_obs: bool = False):
    rewards=[]; infos=[]; done=False; obs=before_obs
    before_success = check_success(env)
    before_obj = object_body_positions(env)
    before_contact = contact_summary(env)
    
    # Robustness against robosuite "executing action in terminated episode"
    terminated = False
    # Check common termination flag names in robosuite/libero
    for obj in [env, getattr(env, 'env', None)]:
        if obj and (getattr(obj, '_episode_terminated', False) or getattr(obj, 'done', False)):
            terminated = True; break

    if not terminated:
        for i,act in enumerate(action_chunk[:horizon]):
            try:
                obs, reward, done, info = env.step(np.asarray(act, dtype=np.float32))
                rewards.append(float(reward)); infos.append({k: str(v)[:200] for k,v in (info or {}).items()})
                if done: break
            except ValueError as e:
                if "terminated episode" in str(e):
                    done = True; break
                raise e
    
    after_success = check_success(env)
    after_obj = object_body_positions(env)
    after_contact = contact_summary(env)
    delta = compute_delta(before_obs, obs, before_obj, after_obj, task_context)
    result = {"H_used": int(min(horizon, len(action_chunk))), "steps_executed": len(rewards), "rewards": rewards, "reward_sum_H": float(sum(rewards)), "nonzero_reward_count_H": int(sum(abs(r)>1e-8 for r in rewards)), "success_before": before_success, "success_after": after_success, "success_within_H": bool(after_success and not before_success), "done_within_H": bool(done), "before_proprio": obs_to_proprio(before_obs).tolist(), "after_proprio": obs_to_proprio(obs).tolist(), "object_positions_before": before_obj, "object_positions_after": after_obj, "contact_before": before_contact, "contact_after": after_contact, "delta": delta, "info_keys": sorted(list(infos[-1].keys())) if infos else [], "last_info": infos[-1] if infos else {}}
    return (result, obs) if return_after_obs else result
