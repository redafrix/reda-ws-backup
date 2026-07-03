#!/usr/bin/env python3
"""Create a side-by-side agent/wrist video from recorded episodes."""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("collection_dir", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--fps", type=float, default=5.0)
    return parser.parse_args()


def episode_dirs(collection_dir: Path) -> list[Path]:
    episodes = sorted(path for path in collection_dir.iterdir() if path.is_dir() and path.name.isdigit())
    if not episodes:
        raise FileNotFoundError(f"No episode directories found in {collection_dir}")
    return episodes


def load_rgb_arrays(episode_dir: Path) -> tuple[np.ndarray, np.ndarray]:
    trajectory_path = episode_dir / "trajectory.npz"
    if not trajectory_path.is_file():
        raise FileNotFoundError(f"Missing trajectory file: {trajectory_path}")

    trajectory = np.load(trajectory_path)
    if "agent_rgb" not in trajectory or "wrist_rgb" not in trajectory:
        raise KeyError(f"Missing agent_rgb or wrist_rgb in {trajectory_path}")

    agent_rgb = trajectory["agent_rgb"]
    wrist_rgb = trajectory["wrist_rgb"]
    if agent_rgb.shape != wrist_rgb.shape:
        raise ValueError(
            f"Camera arrays must have matching shapes in {trajectory_path}: "
            f"agent={agent_rgb.shape}, wrist={wrist_rgb.shape}"
        )
    return agent_rgb, wrist_rgb


def write_side_by_side_video(collection_dir: Path, output_path: Path, fps: float) -> None:
    episodes = episode_dirs(collection_dir)
    first_agent, first_wrist = load_rgb_arrays(episodes[0])
    height, width = first_agent.shape[1:3]
    frame_size = (width * 2, height)

    writer = cv2.VideoWriter(
        str(output_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        frame_size,
    )
    if not writer.isOpened():
        raise RuntimeError(f"Failed to open video writer: {output_path}")

    try:
        for episode_dir in episodes:
            agent_rgb, wrist_rgb = load_rgb_arrays(episode_dir)
            if agent_rgb.shape[1:3] != (height, width):
                raise ValueError(
                    f"Unexpected frame shape in {episode_dir}: "
                    f"expected {(height, width)}, got {agent_rgb.shape[1:3]}"
                )

            for agent_frame, wrist_frame in zip(agent_rgb, wrist_rgb, strict=True):
                side_by_side = np.concatenate((agent_frame, wrist_frame), axis=1)
                writer.write(cv2.cvtColor(side_by_side, cv2.COLOR_RGB2BGR))
    finally:
        writer.release()


def main() -> None:
    args = parse_args()
    output_path = args.output or args.collection_dir / "agent_wrist_side_by_side.mp4"
    write_side_by_side_video(args.collection_dir, output_path, args.fps)
    print(f"[INFO] Saved side-by-side video to: {output_path}")


if __name__ == "__main__":
    main()
