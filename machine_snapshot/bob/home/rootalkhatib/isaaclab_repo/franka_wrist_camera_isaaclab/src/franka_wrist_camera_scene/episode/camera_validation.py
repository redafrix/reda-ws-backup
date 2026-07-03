"""Validation helpers for recorded RGB camera frames."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

MIN_VISIBLE_RGB_MEAN = 5.0
MAX_VISIBLE_RGB_MEAN = 250.0


@dataclass(frozen=True, slots=True)
class CameraFrameStats:
    camera_name: str
    frame_count: int
    min_value: int
    max_value: int
    mean_value: float


def rgb_frame_stats(camera_name: str, frames: list[np.ndarray]) -> CameraFrameStats:
    frame_array = np.asarray(frames, dtype=np.uint8)
    if frame_array.ndim != 4 or frame_array.shape[-1] != 3:
        raise RuntimeError(f"{camera_name} RGB frames must have shape (frames, height, width, 3).")

    return CameraFrameStats(
        camera_name=camera_name,
        frame_count=int(frame_array.shape[0]),
        min_value=int(frame_array.min()),
        max_value=int(frame_array.max()),
        mean_value=float(frame_array.mean()),
    )


def validate_visible_rgb_frames(stats: CameraFrameStats) -> None:
    if stats.frame_count == 0:
        raise RuntimeError(f"{stats.camera_name} recorded no RGB frames.")
    if stats.max_value == 0 or stats.mean_value <= MIN_VISIBLE_RGB_MEAN:
        raise RuntimeError(
            f"{stats.camera_name} RGB frames appear black: "
            f"frames={stats.frame_count} min={stats.min_value} "
            f"max={stats.max_value} mean={stats.mean_value:.3f}"
        )
    if stats.min_value == 255 or stats.mean_value >= MAX_VISIBLE_RGB_MEAN:
        raise RuntimeError(
            f"{stats.camera_name} RGB frames appear white: "
            f"frames={stats.frame_count} min={stats.min_value} "
            f"max={stats.max_value} mean={stats.mean_value:.3f}"
        )


def validate_camera_recordings(agent_rgb: list[np.ndarray], wrist_rgb: list[np.ndarray]) -> None:
    for stats in (
        rgb_frame_stats("agent_camera", agent_rgb),
        rgb_frame_stats("wrist_camera", wrist_rgb),
    ):
        validate_visible_rgb_frames(stats)
