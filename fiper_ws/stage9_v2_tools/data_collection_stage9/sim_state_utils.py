from __future__ import annotations
import json
import numpy as np

_WRAPPER_ATTRS = ("env", "base_env", "wrapped_env", "_env")
_RUNTIME_COUNTER_ATTRS = (
    "timestep",
    "_timestep",
    "cur_time",
    "_cur_time",
    "cur_step",
    "_cur_step",
    "step_count",
    "_step_count",
    "_elapsed_steps",
    "elapsed_steps",
    "_episode_timestep",
    "episode_timestep",
    "_episode_step",
    "episode_step",
    "_current_step",
    "current_step",
    "_steps",
    "steps",
    "_n_steps",
    "n_steps",
    "_num_steps",
    "num_steps",
)
_TERMINATION_FLAG_ATTRS = ("_episode_terminated", "done", "_done", "terminated", "_terminated")
_MUJOCO_DATA_ARRAY_ATTRS = (
    "ctrl",
    "qacc_warmstart",
    "qfrc_applied",
    "xfrc_applied",
    "mocap_pos",
    "mocap_quat",
    "userdata",
)


def get_sim(env):
    return getattr(env, "sim", None) or getattr(getattr(env, "env", None), "sim", None)


def _iter_env_objects(env):
    """Yield env wrappers in stable traversal order without recursing forever."""
    seen = set()
    stack = [env]
    while stack:
        obj = stack.pop(0)
        if obj is None or id(obj) in seen:
            continue
        seen.add(id(obj))
        yield obj
        for attr in _WRAPPER_ATTRS:
            child = getattr(obj, attr, None)
            if child is not None and id(child) not in seen:
                stack.append(child)


def _json_scalar(value):
    if isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, np.generic):
        return value.item()
    return None


def _capture_env_runtime(env) -> dict:
    objects = []
    for index, obj in enumerate(_iter_env_objects(env)):
        attrs = {}
        for attr in _RUNTIME_COUNTER_ATTRS:
            if not hasattr(obj, attr):
                continue
            try:
                value = _json_scalar(getattr(obj, attr))
            except Exception:
                value = None
            if isinstance(value, (bool, int, float)):
                attrs[attr] = value
        if attrs:
            objects.append({
                "index": index,
                "class": obj.__class__.__name__,
                "attrs": attrs,
            })
    return {"schema_version": "stage9_env_runtime_v1", "objects": objects}


def _restore_env_runtime(env, runtime: dict | None) -> None:
    if not runtime:
        return
    objects = list(_iter_env_objects(env))
    saved = runtime.get("objects") or []
    for item in saved:
        index = item.get("index")
        if not isinstance(index, int) or index < 0 or index >= len(objects):
            continue
        obj = objects[index]
        for attr, value in (item.get("attrs") or {}).items():
            if not hasattr(obj, attr):
                continue
            try:
                setattr(obj, attr, value)
            except Exception:
                pass


def _capture_sim_runtime(sim) -> dict[str, np.ndarray]:
    data = getattr(sim, "data", None)
    out: dict[str, np.ndarray] = {}
    if data is None:
        return out
    for attr in _MUJOCO_DATA_ARRAY_ATTRS:
        if not hasattr(data, attr):
            continue
        try:
            out[attr] = np.array(getattr(data, attr), dtype=np.float64, copy=True)
        except Exception:
            pass
    return out


def _restore_sim_runtime(sim, runtime: dict | None) -> None:
    if not runtime:
        return
    data = getattr(sim, "data", None)
    if data is None:
        return
    for attr, value in runtime.items():
        if not hasattr(data, attr):
            continue
        try:
            target = getattr(data, attr)
            arr = np.asarray(value, dtype=target.dtype)
            if target.shape == arr.shape:
                target[...] = arr
        except Exception:
            pass


def get_state(env) -> dict:
    sim = get_sim(env)
    if sim is None: raise RuntimeError("env.sim unavailable")
    st = sim.get_state()
    runtime = _capture_env_runtime(env)
    sim_runtime = _capture_sim_runtime(sim)
    try:
        flat = np.array(st.flatten(), dtype=np.float64)
        return {"kind": "mujoco_flat", "flat": flat, "env_runtime": runtime, "sim_runtime": sim_runtime}
    except Exception:
        return {"kind": "mujoco_state", "state": st, "env_runtime": runtime, "sim_runtime": sim_runtime}

def _hard_reset_before_restore(env) -> None:
    """Clear wrapper/task episode state before restoring a saved MuJoCo state.

    MuJoCo qpos/qvel alone is not enough in LIBERO/robosuite after prior
    candidates have reached success/done. A reset followed by set_state is
    slower, but it prevents hidden wrapper state from leaking across
    same-state counterfactual replays.
    """
    try:
        env.reset()
    except Exception:
        pass


def set_state(env, state: dict, hard_reset: bool = True) -> None:
    if hard_reset:
        _hard_reset_before_restore(env)
    sim = get_sim(env)
    if sim is None: raise RuntimeError("env.sim unavailable")
    if state.get("kind") == "mujoco_flat":
        sim.set_state_from_flattened(np.array(state["flat"], dtype=np.float64))
    else:
        sim.set_state(state["state"])
    _restore_sim_runtime(sim, state.get("sim_runtime"))
    sim.forward()
    # MuJoCo forward recomputes derived quantities and can overwrite warm-start
    # solver fields. Restore again so contact-rich grasp states replay exactly.
    _restore_sim_runtime(sim, state.get("sim_runtime"))
    _restore_env_runtime(env, state.get("env_runtime"))
    clear_episode_termination(env)


def clear_episode_termination(env) -> None:
    """Reset robosuite/LIBERO termination flags after restoring a raw MuJoCo state."""
    for obj in _iter_env_objects(env):
        for flag in _TERMINATION_FLAG_ATTRS:
            if hasattr(obj, flag):
                try:
                    setattr(obj, flag, False)
                except Exception:
                    pass

def state_distance(a: dict, b: dict) -> float:
    if a.get("kind") == b.get("kind") == "mujoco_flat":
        return float(np.max(np.abs(np.array(a["flat"]) - np.array(b["flat"]))))
    return float("nan")

def save_state_npz(path, state: dict) -> str:
    import numpy as np
    from pathlib import Path
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    if state.get("kind") == "mujoco_flat":
        payload = {
            "kind": state["kind"],
            "flat": state["flat"],
            "env_runtime_json": json.dumps(state.get("env_runtime") or {}, sort_keys=True),
        }
        for key, value in (state.get("sim_runtime") or {}).items():
            payload[f"sim_runtime__{key}"] = np.asarray(value)
        np.savez_compressed(path, **payload)
    return str(path)
