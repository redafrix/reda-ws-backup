from __future__ import annotations
import os, sys, math, json, random
from pathlib import Path
from typing import Any
import numpy as np

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
SIM = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
LIBERO_PRO = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"
for p in [REDA_WS / "asynchvla_ws/src", SIM, LIBERO_PRO]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from libero.libero import benchmark, get_libero_path  # noqa
from libero.libero.envs import OffScreenRenderEnv  # noqa

DEFAULT_SUITES = [
    "libero_object_with_mug", "libero_object_with_red_box", "libero_object_with_blue_stick",
    "libero_object_temp_x0.1", "libero_object_temp_x0.3", "libero_spatial_with_mug",
    "libero_spatial_with_red_box", "libero_goal_with_mug", "libero_goal_with_red_box",
    "libero_10_with_mug",
]

PERTURBATION_HINTS = {
    "object": ["object_with", "object_temp"],
    "initial_position": ["spatial_with"],
    "instruction_or_goal": ["goal_with", "libero_10"],
    "environment": ["temp"],
}

def setup_env_vars() -> None:
    os.environ.setdefault("LIBERO_CONFIG_PATH", str(REDA_WS / "asynchvla_ws/configs/libero_pro_bob"))
    os.environ.setdefault("MUJOCO_GL", "egl")
    os.environ.setdefault("PYOPENGL_PLATFORM", "egl")
    os.environ.setdefault("PYTHONPATH", str(LIBERO_PRO) + ":" + os.environ.get("PYTHONPATH", ""))

def suite_perturbation_type(suite: str) -> str:
    for k, vals in PERTURBATION_HINTS.items():
        if any(v in suite for v in vals):
            return k
    return "unknown"

def available_suites() -> list[str]:
    bd = benchmark.get_benchmark_dict()
    return sorted([s for s in DEFAULT_SUITES if s in bd])

def task_bundle(suite: str, task_id: int, resolution: int = 128) -> dict[str, Any]:
    setup_env_vars()
    bd = benchmark.get_benchmark_dict()
    if suite not in bd:
        raise KeyError(f"suite {suite} not available; examples={list(bd)[:20]}")
    bench = bd[suite]()
    task = bench.get_task(task_id)
    init_states = bench.get_task_init_states(task_id)
    bddl_path = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    env_args = {"bddl_file_name": str(bddl_path), "camera_heights": resolution, "camera_widths": resolution}
    return {"benchmark": bench, "task": task, "init_states": init_states, "bddl_path": str(bddl_path), "env_args": env_args, "suite": suite, "task_id": task_id}

def make_env(suite: str, task_id: int, resolution: int = 128, seed: int | None = None):
    b = task_bundle(suite, task_id, resolution)
    env = OffScreenRenderEnv(**b["env_args"])
    if seed is not None and hasattr(env, "seed"):
        env.seed(int(seed))
    return env, b

def reset_to_init(env, init_state=None, warmup: int = 10):
    obs = env.reset()
    if init_state is not None:
        obs = env.set_init_state(init_state)
    zero = np.array([0,0,0,0,0,0,-1], dtype=np.float32)
    for _ in range(warmup):
        obs, reward, done, info = env.step(zero)
    return obs

def check_success(env) -> bool | None:
    for obj in [env, getattr(env, "env", None), getattr(env, "base_env", None)]:
        if obj is None: continue
        fn = getattr(obj, "_check_success", None) or getattr(obj, "check_success", None)
        if callable(fn):
            try: return bool(fn())
            except Exception: pass
    return None

def obs_images(obs: dict) -> tuple[np.ndarray, np.ndarray]:
    img = obs.get("agentview_image")
    wrist = obs.get("robot0_eye_in_hand_image")
    if img is None:
        img = np.zeros((128,128,3), dtype=np.uint8)
    if wrist is None:
        wrist = np.zeros_like(img)
    return np.ascontiguousarray(img[::-1, ::-1]), np.ascontiguousarray(wrist[::-1, ::-1])

def quat2axisangle(quat: np.ndarray) -> np.ndarray:
    quat = quat.copy().astype(np.float64)
    quat[3] = np.clip(quat[3], -1.0, 1.0)
    den = np.sqrt(max(0.0, 1.0 - quat[3] * quat[3]))
    if math.isclose(den, 0.0): return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den

def obs_to_proprio(obs: dict) -> np.ndarray:
    ee_pos = obs.get("robot0_eef_pos", np.zeros(3))
    ee_quat = obs.get("robot0_eef_quat", np.array([0,0,0,1.0]))
    grip = obs.get("robot0_gripper_qpos", np.zeros(2))
    state = np.concatenate([ee_pos, quat2axisangle(ee_quat), grip])[:8]
    if state.size < 8: state = np.pad(state, (0, 8-state.size))
    return state.astype(np.float32)
