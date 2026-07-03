"""Geometry and action conversions matching the SimVLA IsaacLab dataset."""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.spatial.transform import Rotation as R

from franka_wrist_camera_scene.simvla.constants import DEFAULT_SIMVLA_CONVENTION, SimVLADataConvention


@dataclass(frozen=True, slots=True)
class SimVLAProprioSource:
    ee_pos_w: np.ndarray
    ee_quat_wxyz: np.ndarray
    env_origin_w: np.ndarray
    commanded_finger_opening_m: float


@dataclass(frozen=True, slots=True)
class DecodedSimVLAAction:
    target_pos_w: np.ndarray
    target_quat_wxyz: np.ndarray
    finger_opening_m: float


def quat_wxyz_to_xyzw(quat_wxyz: np.ndarray) -> np.ndarray:
    quat = np.asarray(quat_wxyz, dtype=np.float64)
    if quat.shape[-1] != 4:
        raise ValueError(f"Quaternion last dimension must be 4, got {quat.shape}.")
    return np.concatenate((quat[..., 1:4], quat[..., 0:1]), axis=-1)


def quat_xyzw_to_wxyz(quat_xyzw: np.ndarray) -> np.ndarray:
    quat = np.asarray(quat_xyzw, dtype=np.float64)
    if quat.shape[-1] != 4:
        raise ValueError(f"Quaternion last dimension must be 4, got {quat.shape}.")
    return np.concatenate((quat[..., 3:4], quat[..., 0:3]), axis=-1)


def require_finite_vector(name: str, values: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
    arr = np.asarray(values, dtype=np.float64)
    if arr.shape != shape:
        raise ValueError(f"{name} must have shape {shape}, got {arr.shape}.")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} contains non-finite values: {arr}.")
    return arr


def libero_euler_xyz_from_rotation(rot: R) -> np.ndarray:
    euler = rot.as_euler("xyz").astype(np.float32)
    if float(euler[0]) < -math.pi / 2.0:
        euler[0] += 2.0 * math.pi
    return euler


def euler_xyz_to_axis_angle(euler_xyz: np.ndarray) -> np.ndarray:
    quat_xyzw = R.from_euler("xyz", euler_xyz).as_quat()
    return quat_xyzw_to_axis_angle(quat_xyzw)


def quat_xyzw_to_axis_angle(quat_xyzw: np.ndarray) -> np.ndarray:
    quat = require_finite_vector("quat_xyzw", quat_xyzw, (4,)).copy()
    quat[3] = min(1.0, max(-1.0, float(quat[3])))
    den = math.sqrt(max(0.0, 1.0 - float(quat[3]) * float(quat[3])))
    if math.isclose(den, 0.0):
        return np.zeros(3, dtype=np.float32)
    return ((quat[:3] * 2.0 * math.acos(float(quat[3]))) / den).astype(np.float32)


def encode_simvla_proprio(source: SimVLAProprioSource) -> np.ndarray:
    ee_pos = require_finite_vector("ee_pos_w", source.ee_pos_w, (3,))
    env_origin = require_finite_vector("env_origin_w", source.env_origin_w, (3,))
    quat_wxyz = require_finite_vector("ee_quat_wxyz", source.ee_quat_wxyz, (4,))
    if not math.isfinite(float(source.commanded_finger_opening_m)):
        raise ValueError(f"commanded_finger_opening_m must be finite, got {source.commanded_finger_opening_m}.")

    rot = R.from_quat(quat_wxyz_to_xyzw(quat_wxyz))
    ee_ori = libero_euler_xyz_from_rotation(rot)
    axis_angle = euler_xyz_to_axis_angle(ee_ori)
    opening = float(source.commanded_finger_opening_m)
    gripper = np.array((opening, -opening), dtype=np.float32)
    return np.concatenate(((ee_pos - env_origin).astype(np.float32), axis_angle, gripper), axis=0)


def decode_simvla_action(
    action: np.ndarray,
    ee_pos_w: np.ndarray,
    ee_quat_wxyz: np.ndarray,
    convention: SimVLADataConvention = DEFAULT_SIMVLA_CONVENTION,
) -> DecodedSimVLAAction:
    action_arr = require_finite_vector("action", action, (7,))
    ee_pos = require_finite_vector("ee_pos_w", ee_pos_w, (3,))
    ee_quat = require_finite_vector("ee_quat_wxyz", ee_quat_wxyz, (4,))

    target_pos = ee_pos + action_arr[:3] * convention.translation_scale_m
    current_rot = R.from_quat(quat_wxyz_to_xyzw(ee_quat))
    relative_rot = R.from_euler("xyz", action_arr[3:6] * convention.rotation_scale_rad)
    target_quat = quat_xyzw_to_wxyz((relative_rot * current_rot).as_quat()).astype(np.float32)
    finger_opening = convention.closed_finger_m if float(action_arr[6]) >= 0.0 else convention.open_finger_m
    return DecodedSimVLAAction(
        target_pos_w=target_pos.astype(np.float32),
        target_quat_wxyz=target_quat,
        finger_opening_m=float(finger_opening),
    )
