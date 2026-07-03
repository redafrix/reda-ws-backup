#!/usr/bin/env python3
"""Stage 7 LIBERO rollout environment smoke check.

Reports import status for libero/robosuite/mujoco and tries to instantiate
OffScreenRenderEnv for the first task of a chosen suite to verify offscreen
rendering works on Bob.

Usage:
  python3 asynchvla_ws/src/eval_stage7/check_libero_rollout_env.py \
      --suite libero_spatial --task-id 0 --resolution 128

Returns non-zero on failure. Designed to run inside the
`activate_simvla_bob.sh` activation, with a Bob-local LIBERO config:

  export LIBERO_CONFIG_PATH=/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_bob
  export MUJOCO_GL=egl
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
import traceback
from pathlib import Path


PACKAGES = [
    "libero",
    "libero.libero",
    "robosuite",
    "mujoco",
    "bddl",
    "hydra",
    "einops",
    "easydict",
    "robomimic",
    "OpenGL",
    "imageio",
    "msgpack_numpy",
]

OPTIONAL = ["openpi_client"]


def import_status():
    out = {}
    for mod in PACKAGES + OPTIONAL:
        spec = importlib.util.find_spec(mod)
        if spec is None:
            out[mod] = {"ok": False, "version": "", "required": mod in PACKAGES}
            continue
        try:
            m = importlib.import_module(mod)
            out[mod] = {
                "ok": True,
                "version": getattr(m, "__version__", ""),
                "required": mod in PACKAGES,
            }
        except Exception as exc:  # pragma: no cover
            out[mod] = {
                "ok": False,
                "error": repr(exc),
                "required": mod in PACKAGES,
            }
    return out


def smoke_env(suite: str, task_id: int, resolution: int):
    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    bd = benchmark.get_benchmark_dict()
    if suite not in bd:
        return {"ok": False, "error": f"unknown suite {suite}", "available": list(bd.keys())}
    b = bd[suite]()
    if task_id >= b.n_tasks:
        return {"ok": False, "error": f"task_id {task_id} out of range {b.n_tasks}"}
    task = b.get_task(task_id)
    bddl_path = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    env_args = {
        "bddl_file_name": str(bddl_path),
        "camera_heights": resolution,
        "camera_widths": resolution,
    }
    t0 = time.time()
    env = OffScreenRenderEnv(**env_args)
    env.seed(0)
    obs = env.reset()
    instantiate_sec = time.time() - t0
    image_key = "agentview_image" if "agentview_image" in obs else next(iter(obs))
    image_shape = list(obs[image_key].shape)
    # try one stepped action to ensure the simulator+renderer round-trips
    import numpy as np
    action = np.zeros(7, dtype=np.float32)
    action[-1] = -1.0  # open gripper / dummy
    t1 = time.time()
    step_obs, reward, done, info = env.step(action)
    step_sec = time.time() - t1
    try:
        env.close()
    except Exception:
        pass
    return {
        "ok": True,
        "suite": suite,
        "task_id": task_id,
        "task_language": task.language,
        "bddl_path": str(bddl_path),
        "obs_keys_sample": sorted(list(obs.keys()))[:8],
        "image_shape": image_shape,
        "instantiate_sec": instantiate_sec,
        "step_sec": step_sec,
        "step_reward": float(reward),
        "step_done": bool(done),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="libero_spatial")
    ap.add_argument("--task-id", type=int, default=0)
    ap.add_argument("--resolution", type=int, default=128)
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    os.environ.setdefault("MUJOCO_GL", "egl")
    os.environ.setdefault("PYOPENGL_PLATFORM", "egl")

    status = import_status()
    blockers = [k for k, v in status.items() if v.get("required") and not v.get("ok")]

    smoke = None
    smoke_err = None
    if not blockers:
        try:
            smoke = smoke_env(args.suite, args.task_id, args.resolution)
        except Exception as exc:  # pragma: no cover
            smoke_err = traceback.format_exc()

    result = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "args": vars(args),
        "imports": status,
        "blockers": blockers,
        "smoke": smoke,
        "smoke_error": smoke_err,
    }
    out = json.dumps(result, indent=2, default=str)
    print(out)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out)
    if blockers or smoke_err or (smoke and not smoke["ok"]):
        sys.exit(2)


if __name__ == "__main__":
    main()
