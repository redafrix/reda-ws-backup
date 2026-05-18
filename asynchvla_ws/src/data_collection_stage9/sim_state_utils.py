from __future__ import annotations
import numpy as np

def get_sim(env):
    return getattr(env, "sim", None) or getattr(getattr(env, "env", None), "sim", None)

def get_state(env) -> dict:
    sim = get_sim(env)
    if sim is None: raise RuntimeError("env.sim unavailable")
    st = sim.get_state()
    try:
        flat = np.array(st.flatten(), dtype=np.float64)
        return {"kind": "mujoco_flat", "flat": flat}
    except Exception:
        return {"kind": "mujoco_state", "state": st}

def set_state(env, state: dict) -> None:
    sim = get_sim(env)
    if sim is None: raise RuntimeError("env.sim unavailable")
    if state.get("kind") == "mujoco_flat":
        sim.set_state_from_flattened(np.array(state["flat"], dtype=np.float64))
    else:
        sim.set_state(state["state"])
    sim.forward()

def state_distance(a: dict, b: dict) -> float:
    if a.get("kind") == b.get("kind") == "mujoco_flat":
        return float(np.max(np.abs(np.array(a["flat"]) - np.array(b["flat"]))))
    return float("nan")

def save_state_npz(path, state: dict) -> str:
    import numpy as np
    from pathlib import Path
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    if state.get("kind") == "mujoco_flat": np.savez_compressed(path, kind=state["kind"], flat=state["flat"])
    return str(path)
