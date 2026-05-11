#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import imageio
import numpy as np

ROOT = Path(__file__).parents[2] / "simvla/code/SimVLA"
sys.path.insert(0, str(ROOT))

from evaluation.libero.libero_client import (
    LIBERO_DUMMY_ACTION,
    LIBERO_ENV_RESOLUTION,
    MAX_STEPS,
    NUM_STEPS_WAIT,
    WebSocketClient,
    benchmark_dict,
    get_libero_env,
)


def quat2axisangle(quat: np.ndarray) -> np.ndarray:
    quat = quat.copy()
    if quat[3] > 1.0:
        quat[3] = 1.0
    elif quat[3] < -1.0:
        quat[3] = -1.0

    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0):
        return np.zeros(3)

    return (quat[:3] * 2.0 * math.acos(quat[3])) / den


def run_episode(
    *,
    host: str,
    port: int,
    task_suite_name: str,
    task_id: int,
    episode_index: int,
    seed: int,
    replan_steps: int,
    video_path: Path,
) -> dict:
    task_suite = benchmark_dict[task_suite_name]()
    task = task_suite.get_task(task_id)
    initial_states = task_suite.get_task_init_states(task_id)
    env, task_description = get_libero_env(task, LIBERO_ENV_RESOLUTION, seed)
    client = WebSocketClient(host, port, replan_steps=replan_steps)
    max_steps = MAX_STEPS[task_suite_name]

    env.reset()
    client.reset()
    obs = env.set_init_state(initial_states[episode_index % len(initial_states)])

    replay_images = []
    done = False
    t = 0
    error = None

    try:
        while t < max_steps + NUM_STEPS_WAIT:
            if t < NUM_STEPS_WAIT:
                obs, reward, done, info = env.step(LIBERO_DUMMY_ACTION)
                t += 1
                continue

            img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
            wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
            replay_images.append(img)

            state = np.concatenate(
                [
                    obs["robot0_eef_pos"],
                    quat2axisangle(obs["robot0_eef_quat"]),
                    obs["robot0_gripper_qpos"],
                ]
            )

            action = client.step(
                {
                    "image": img,
                    "wrist_image": wrist_img,
                    "state": state,
                },
                task_description,
            )
            obs, reward, done, info = env.step(action.tolist())
            t += 1
            if done:
                break
    except Exception as exc:
        error = repr(exc)
    finally:
        env.close()

    video_path.parent.mkdir(parents=True, exist_ok=True)
    if replay_images:
        imageio.mimwrite(str(video_path), replay_images, fps=40)

    return {
        "task_suite": task_suite_name,
        "task_id": task_id,
        "episode_index": episode_index,
        "task_description": task_description,
        "success": bool(done),
        "steps": t,
        "max_steps": max_steps,
        "video_path": str(video_path),
        "error": error,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one LIBERO task episode and save one video.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--task_suite", required=True, choices=["libero_spatial", "libero_object", "libero_goal", "libero_10", "libero_90"])
    parser.add_argument("--task_id", type=int, default=0)
    parser.add_argument("--episode_index", type=int, default=0)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--replan_steps", type=int, default=5)
    parser.add_argument("--video_path", required=True)
    parser.add_argument("--summary_path", required=True)
    args = parser.parse_args()

    result = run_episode(
        host=args.host,
        port=args.port,
        task_suite_name=args.task_suite,
        task_id=args.task_id,
        episode_index=args.episode_index,
        seed=args.seed,
        replan_steps=args.replan_steps,
        video_path=Path(args.video_path),
    )

    summary_path = Path(args.summary_path)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
