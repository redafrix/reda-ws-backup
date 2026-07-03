"""Pi0.5 LIBERO state and action conversions for IsaacLab control."""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.spatial.transform import Rotation as R

from franka_wrist_camera_scene.simvla.geometry import (
    quat_wxyz_to_xyzw,
    quat_xyzw_to_wxyz,
    require_finite_vector,
)


@dataclass(frozen=True, slots=True)
class Pi05ControlScales:
    translation_scale_m: float = 0.05
    rotation_scale_rad: float = 0.5
    open_finger_m: float = 0.04
    closed_finger_m: float = 0.0


@dataclass(frozen=True, slots=True)
class Pi05ProprioSource:
    ee_pos_w: np.ndarray
    ee_quat_wxyz: np.ndarray
    env_origin_w: np.ndarray
    commanded_finger_opening_m: float


@dataclass(frozen=True, slots=True)
class DecodedPi05Action:
    target_pos_w: np.ndarray
    target_quat_wxyz: np.ndarray
    finger_opening_m: float


def quat_xyzw_to_axis_angle(quat_xyzw: np.ndarray) -> np.ndarray:
    quat = require_finite_vector("quat_xyzw", quat_xyzw, (4,)).copy()
    quat[3] = min(1.0, max(-1.0, float(quat[3])))
    den = math.sqrt(max(0.0, 1.0 - float(quat[3]) * float(quat[3])))
    if math.isclose(den, 0.0):
        return np.zeros(3, dtype=np.float32)
    return ((quat[:3] * 2.0 * math.acos(float(quat[3]))) / den).astype(np.float32)


def encode_pi05_libero_state(source: Pi05ProprioSource) -> np.ndarray:
    """Build the official OpenPI LIBERO 8D state: xyz, axis-angle, two gripper joints."""
    ee_pos = require_finite_vector("ee_pos_w", source.ee_pos_w, (3,))
    env_origin = require_finite_vector("env_origin_w", source.env_origin_w, (3,))
    quat_wxyz = require_finite_vector("ee_quat_wxyz", source.ee_quat_wxyz, (4,))
    opening = float(source.commanded_finger_opening_m)
    if not math.isfinite(opening):
        raise ValueError(f"commanded_finger_opening_m must be finite, got {source.commanded_finger_opening_m}.")

    axis_angle = quat_xyzw_to_axis_angle(R.from_quat(quat_wxyz_to_xyzw(quat_wxyz)).as_quat())
    gripper = np.array((opening, -opening), dtype=np.float32)
    state = np.concatenate(((ee_pos - env_origin).astype(np.float32), axis_angle, gripper), axis=0)
    if state.shape != (8,):
        raise RuntimeError(f"Pi0.5 LIBERO state must have shape (8,), got {state.shape}.")
    return state


def decode_pi05_libero_action(
    action: np.ndarray,
    ee_pos_w: np.ndarray,
    ee_quat_wxyz: np.ndarray,
    scales: Pi05ControlScales = Pi05ControlScales(),
) -> DecodedPi05Action:
    """Convert Pi0.5 LIBERO env action to an IsaacLab Cartesian IK command."""
    action_arr = require_finite_vector("action", action, (7,))
    ee_pos = require_finite_vector("ee_pos_w", ee_pos_w, (3,))
    ee_quat = require_finite_vector("ee_quat_wxyz", ee_quat_wxyz, (4,))

    target_pos = ee_pos + action_arr[:3] * float(scales.translation_scale_m)
    current_rot = R.from_quat(quat_wxyz_to_xyzw(ee_quat))
    relative_rot = R.from_euler("xyz", action_arr[3:6] * float(scales.rotation_scale_rad))
    target_quat = quat_xyzw_to_wxyz((relative_rot * current_rot).as_quat()).astype(np.float32)
    finger_opening = scales.closed_finger_m if float(action_arr[6]) >= 0.0 else scales.open_finger_m
    return DecodedPi05Action(
        target_pos_w=target_pos.astype(np.float32),
        target_quat_wxyz=target_quat,
        finger_opening_m=float(finger_opening),
    )
