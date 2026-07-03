#!/usr/bin/env python3
"""Validate RGB tensors in a recorded collection."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


RGB_KEYS = ("agent_rgb", "wrist_rgb")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate recorded RGB tensors.")
    parser.add_argument("collection_dir", type=Path)
    parser.add_argument("--episode", default="000000")
    parser.add_argument("--min-mean", type=float, default=1.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    episode_path = args.collection_dir / args.episode / "rgb.npz"
    if not episode_path.is_file():
        raise FileNotFoundError(f"Missing trajectory file: {episode_path}")

    data = np.load(episode_path)

    for key in RGB_KEYS:
        if key not in data:
            raise RuntimeError(f"Missing RGB key in trajectory: {key}")

        arr = data[key]
        min_value = int(arr.min())
        max_value = int(arr.max())
        mean_value = float(arr.mean())

        print(
            f"{key}: shape={arr.shape} "
            f"min={min_value} max={max_value} mean={mean_value:.3f}"
        )

        if max_value == 0 or mean_value < args.min_mean:
            raise RuntimeError(
                f"{key} appears invalid: "
                f"shape={arr.shape} min={min_value} max={max_value} mean={mean_value:.3f}"
            )


if __name__ == "__main__":
    main()
