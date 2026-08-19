"""Geometry and action conversion for mimic-video IsaacLab policies."""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.spatial.transform import Rotation as R

from franka_wrist_camera_scene.control.reaching_pose_actions import (
    PoseCommandAnchor,
    RobotBaseFrame,
    decode_command_increment,
)
from franka_wrist_camera_scene.mimic_video.constants import (
    DEFAULT_MIMIC_VIDEO_CONVENTION,
    MimicVideoConvention,
)


@dataclass(frozen=True, slots=True)
class MimicVideoProprioSource:
    ee_pos_w: np.ndarray
    ee_quat_wxyz: np.ndarray
    robot_base_pos_w: np.ndarray
    robot_base_quat_wxyz: np.ndarray
    finger_opening_m: float


@dataclass(frozen=True, slots=True)
class DecodedMimicVideoAction:
    target_pos_w: np.ndarray
    target_quat_xyzw: np.ndarray
    finger_opening_m: float


def encode_mimic_video_state(source: MimicVideoProprioSource) -> np.ndarray:
    ee_pos = require_finite_vector("ee_pos_w", source.ee_pos_w, (3,))
    base_pos = require_finite_vector("robot_base_pos_w", source.robot_base_pos_w, (3,))
    ee_quat = normalized_quaternion("ee_quat_wxyz", source.ee_quat_wxyz)
    base_quat = normalized_quaternion("robot_base_quat_wxyz", source.robot_base_quat_wxyz)
    opening = float(source.finger_opening_m)
    if not math.isfinite(opening) or not 0.0 <= opening <= 0.08:
        raise ValueError(f"finger_opening_m must be within [0, 0.08], got {opening}.")

    base_rotation = R.from_quat(quat_wxyz_to_xyzw(base_quat))
    ee_rotation = R.from_quat(quat_wxyz_to_xyzw(ee_quat))
    ee_position_base = base_rotation.inv().apply(ee_pos - base_pos)
    ee_rotation_base = base_rotation.inv() * ee_rotation
    rot6 = rotation_matrix_to_training_6d(ee_rotation_base.as_matrix())
    return np.concatenate(
        (ee_position_base.astype(np.float32), rot6, np.asarray((opening,), dtype=np.float32))
    )


@dataclass(slots=True)
class MimicVideoPersistentCommandIntegrator:
    convention: MimicVideoConvention = DEFAULT_MIMIC_VIDEO_CONVENTION
    _anchor: PoseCommandAnchor | None = None
    _base_frame: RobotBaseFrame | None = None

    def reset(self, source: MimicVideoProprioSource) -> None:
        ee_position = require_finite_vector("ee_pos_w", source.ee_pos_w, (3,)).copy()
        base_position = require_finite_vector(
            "robot_base_pos_w", source.robot_base_pos_w, (3,)
        ).copy()
        base_quaternion = normalized_quaternion(
            "robot_base_quat_wxyz", source.robot_base_quat_wxyz
        )
        canonical_quaternion_base = normalized_quaternion(
            "canonical_ee_quat_base_wxyz",
            np.asarray(self.convention.canonical_ee_quat_base_wxyz),
        )
        base_rotation_world = R.from_quat(quat_wxyz_to_xyzw(base_quaternion))
        canonical_rotation_base = R.from_quat(
            quat_wxyz_to_xyzw(canonical_quaternion_base)
        )
        canonical_quaternion_world_xyzw = (
            base_rotation_world * canonical_rotation_base
        ).as_quat()
        self._anchor = PoseCommandAnchor(
            position_w=ee_position,
            quaternion_xyzw=canonical_quaternion_world_xyzw,
        )
        self._base_frame = RobotBaseFrame(
            position_w=base_position,
            quaternion_wxyz=base_quaternion,
        )

    def decode(self, action: np.ndarray) -> DecodedMimicVideoAction:
        if self._anchor is None or self._base_frame is None:
            raise RuntimeError("MimicVideoPersistentCommandIntegrator.reset() must run first.")
        action_array = require_finite_vector(
            "mimic_video_action", action, (self.convention.action_dim,)
        )
        training_6d_to_rotation_matrix(action_array[3:9])
        action_seven = np.concatenate(
            (action_array[:3], np.zeros(3), action_array[9:10]), axis=0
        )
        decoded = decode_command_increment(action_seven, self._anchor, self._base_frame)
        self._anchor = decoded.anchor
        return DecodedMimicVideoAction(
            target_pos_w=decoded.anchor.position_w.astype(np.float32),
            target_quat_xyzw=decoded.anchor.quaternion_xyzw.astype(np.float32),
            finger_opening_m=float(decoded.finger_opening_m),
        )


def rotation_matrix_to_training_6d(rot: np.ndarray) -> np.ndarray:
    matrix = np.asarray(rot, dtype=np.float64)
    if matrix.shape != (3, 3):
        raise ValueError(f"rotation matrix must have shape (3,3), got {matrix.shape}.")
    return matrix[:2].reshape(6).astype(np.float32)


def training_6d_to_rotation_matrix(rot6: np.ndarray) -> np.ndarray:
    rows = require_finite_vector("rot6", rot6, (6,)).reshape(2, 3)
    first = normalize(rows[0], "rot6_row0")
    second_raw = rows[1] - first * float(np.dot(first, rows[1]))
    second = normalize(second_raw, "rot6_row1")
    third = np.cross(first, second)
    return np.stack((first, second, third), axis=0).astype(np.float64)


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


def normalized_quaternion(name: str, values: np.ndarray) -> np.ndarray:
    quaternion = require_finite_vector(name, values, (4,))
    norm = float(np.linalg.norm(quaternion))
    if norm <= 1e-8:
        raise ValueError(f"{name} has a near-zero norm.")
    return quaternion / norm


def normalize(values: np.ndarray, name: str) -> np.ndarray:
    norm = float(np.linalg.norm(values))
    if not math.isfinite(norm) or norm <= 1e-8:
        raise ValueError(f"{name} cannot be normalized; norm={norm}.")
    return np.asarray(values, dtype=np.float64) / norm
