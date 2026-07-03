"""Shared SimVLA data convention constants."""

from __future__ import annotations

from dataclasses import dataclass

IMAGE_ROTATION_NONE = "none"
IMAGE_ROTATION_180 = "rotate_180"
IMAGE_ROTATION_MODES = frozenset((IMAGE_ROTATION_NONE, IMAGE_ROTATION_180))


@dataclass(frozen=True, slots=True)
class SimVLADataConvention:
    source_width: int = 640
    source_height: int = 480
    crop_x0: int = 80
    crop_x1: int = 560
    crop_y0: int = 0
    crop_y1: int = 480
    image_size: int = 384
    num_views: int = 3
    camera_fps: float = 20.0
    sim_dt: float = 1.0 / 120.0
    camera_interval_steps: int = 6
    num_actions: int = 10
    translation_scale_m: float = 0.05
    rotation_scale_rad: float = 0.5
    gripper_close_threshold_m: float = 0.02
    open_finger_m: float = 0.04
    closed_finger_m: float = 0.0


DEFAULT_SIMVLA_CONVENTION = SimVLADataConvention()


def validate_image_rotation(image_rotation: str) -> str:
    if image_rotation not in IMAGE_ROTATION_MODES:
        modes = ", ".join(sorted(IMAGE_ROTATION_MODES))
        raise ValueError(f"image_rotation must be one of {modes}, got {image_rotation!r}.")
    return image_rotation
