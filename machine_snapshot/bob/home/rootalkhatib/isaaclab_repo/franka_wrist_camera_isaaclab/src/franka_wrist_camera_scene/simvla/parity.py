"""Golden parity checks between raw IsaacLab episodes and converted SimVLA HDF5."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path

import h5py
import numpy as np
from scipy.spatial.transform import Rotation as R

from franka_wrist_camera_scene.simvla.constants import DEFAULT_SIMVLA_CONVENTION
from franka_wrist_camera_scene.simvla.geometry import (
    SimVLAProprioSource,
    decode_simvla_action,
    encode_simvla_proprio,
    euler_xyz_to_axis_angle,
    quat_wxyz_to_xyzw,
)
from franka_wrist_camera_scene.simvla.image_preprocessing import (
    normalize_rgb_uint8,
    preprocess_camera_views,
    preprocess_rgb_uint8,
    rotate_rgb_for_mode,
)
from franka_wrist_camera_scene.simvla.replay_manifest import SourceEpisodeRef


@dataclass(frozen=True, slots=True)
class SimVLAParityResult:
    source_episode_path: str
    hdf5_path: str
    demo: str
    frame_index: int
    state_index: int
    image_rotation: str
    hdf5_agent_rgb_max_abs_error: int
    hdf5_wrist_rgb_max_abs_error: int
    model_agent_tensor_max_abs_error: float
    model_wrist_tensor_max_abs_error: float
    image_mask_matches: bool
    proprio_max_abs_error: float
    decoded_target_pos_error_m: float
    decoded_target_rot_error_rad: float | None
    decoded_gripper_matches: bool

    def to_dict(self) -> dict:
        return asdict(self)

    def assert_within_tolerance(self) -> None:
        failures = []
        if self.hdf5_agent_rgb_max_abs_error != 0:
            failures.append(f"hdf5_agent_rgb_max_abs_error={self.hdf5_agent_rgb_max_abs_error}")
        if self.hdf5_wrist_rgb_max_abs_error != 0:
            failures.append(f"hdf5_wrist_rgb_max_abs_error={self.hdf5_wrist_rgb_max_abs_error}")
        if self.model_agent_tensor_max_abs_error > 1e-6:
            failures.append(f"model_agent_tensor_max_abs_error={self.model_agent_tensor_max_abs_error}")
        if self.model_wrist_tensor_max_abs_error > 1e-6:
            failures.append(f"model_wrist_tensor_max_abs_error={self.model_wrist_tensor_max_abs_error}")
        if not self.image_mask_matches:
            failures.append("image_mask_mismatch")
        if self.proprio_max_abs_error > 1e-5:
            failures.append(f"proprio_max_abs_error={self.proprio_max_abs_error}")
        if self.decoded_target_pos_error_m > 1e-5:
            failures.append(f"decoded_target_pos_error_m={self.decoded_target_pos_error_m}")
        if self.decoded_target_rot_error_rad is not None and self.decoded_target_rot_error_rad > 1e-5:
            failures.append(f"decoded_target_rot_error_rad={self.decoded_target_rot_error_rad}")
        if not self.decoded_gripper_matches:
            failures.append("decoded_gripper_mismatch")
        if failures:
            raise AssertionError("; ".join(failures))


def check_ref_parity(
    ref: SourceEpisodeRef,
    frame_index: int,
    image_rotation: str,
) -> SimVLAParityResult:
    meta = json.loads((ref.source_episode_path / "meta.json").read_text(encoding="utf-8"))
    with (
        np.load(ref.source_episode_path / "trajectory.npz", allow_pickle=False) as traj,
        np.load(ref.source_episode_path / "rgb.npz", allow_pickle=False) as rgb,
        h5py.File(ref.hdf5_path, "r") as h5_file,
    ):
        demo = h5_file["data"][ref.demo]
        state_index = int(np.asarray(traj["camera_step_indices"], dtype=np.int64)[frame_index])
        agent_h5 = np.asarray(demo["obs/agentview_rgb"][frame_index])
        wrist_h5 = np.asarray(demo["obs/eye_in_hand_rgb"][frame_index])
        agent_raw = np.asarray(rgb["agent_rgb"][frame_index])
        wrist_raw = np.asarray(rgb["wrist_rgb"][frame_index])

        ee_pos_w = _squeeze_env(np.asarray(traj["ee_pos_w"], dtype=np.float64), "ee_pos_w")
        ee_quat_w = _squeeze_env(np.asarray(traj["ee_quat_w"], dtype=np.float64), "ee_quat_w")
        object_pos_w = _squeeze_env(np.asarray(traj["object_pos_w"], dtype=np.float64), "object_pos_w")
        target_pos_w = _squeeze_env(np.asarray(traj["action_target_pos_w"], dtype=np.float64), "action_target_pos_w")
        target_quat_w = _squeeze_env(
            np.asarray(traj["action_target_quat_w"], dtype=np.float64),
            "action_target_quat_w",
        )
        finger_opening = np.asarray(traj["action_finger_opening_m"], dtype=np.float64)

        hdf5_agent_error = _max_uint8_error(preprocess_rgb_uint8(agent_raw, "none"), agent_h5)
        hdf5_wrist_error = _max_uint8_error(preprocess_rgb_uint8(wrist_raw, "none"), wrist_h5)
        image_batch = preprocess_camera_views(agent_raw, wrist_raw, image_rotation)
        expected_agent_tensor = normalize_rgb_uint8(rotate_rgb_for_mode(agent_h5, image_rotation))
        expected_wrist_tensor = normalize_rgb_uint8(rotate_rgb_for_mode(wrist_h5, image_rotation))

        origin = _episode_origin(meta, object_pos_w)
        proprio = encode_simvla_proprio(
            SimVLAProprioSource(
                ee_pos_w=ee_pos_w[state_index],
                ee_quat_wxyz=ee_quat_w[state_index],
                env_origin_w=origin,
                commanded_finger_opening_m=_scalar_at(finger_opening, state_index),
            )
        )
        expected_proprio = np.concatenate(
            (
                np.asarray(demo["obs/ee_pos"][frame_index], dtype=np.float32),
                euler_xyz_to_axis_angle(np.asarray(demo["obs/ee_ori"][frame_index], dtype=np.float32)),
                np.asarray(demo["obs/gripper_states"][frame_index], dtype=np.float32),
            ),
            axis=0,
        )

        decoded = decode_simvla_action(
            np.asarray(demo["actions"][frame_index], dtype=np.float32),
            ee_pos_w[state_index],
            ee_quat_w[state_index],
        )
        rot_error = _rotation_error_rad(decoded.target_quat_wxyz, target_quat_w[state_index])
        expected_opening = _expected_decoded_opening(_scalar_at(finger_opening, state_index))

    return SimVLAParityResult(
        source_episode_path=str(ref.source_episode_path),
        hdf5_path=str(ref.hdf5_path),
        demo=ref.demo,
        frame_index=frame_index,
        state_index=state_index,
        image_rotation=image_rotation,
        hdf5_agent_rgb_max_abs_error=hdf5_agent_error,
        hdf5_wrist_rgb_max_abs_error=hdf5_wrist_error,
        model_agent_tensor_max_abs_error=_max_float_error(image_batch.image_input[0, 0].numpy(), expected_agent_tensor.numpy()),
        model_wrist_tensor_max_abs_error=_max_float_error(image_batch.image_input[0, 1].numpy(), expected_wrist_tensor.numpy()),
        image_mask_matches=image_batch.image_mask.tolist() == [[True, True, False]],
        proprio_max_abs_error=_max_float_error(proprio, expected_proprio),
        decoded_target_pos_error_m=float(np.linalg.norm(decoded.target_pos_w - target_pos_w[state_index])),
        decoded_target_rot_error_rad=rot_error,
        decoded_gripper_matches=math.isclose(decoded.finger_opening_m, expected_opening, abs_tol=1e-7),
    )


def _squeeze_env(arr: np.ndarray, name: str) -> np.ndarray:
    if arr.ndim >= 3 and arr.shape[1] == 1:
        return arr[:, 0]
    if arr.ndim != 2:
        raise ValueError(f"{name} must have shape [T, D] or [T, 1, D], got {arr.shape}.")
    return arr


def _episode_origin(meta: dict, object_pos_w: np.ndarray) -> np.ndarray:
    object_pos_local = np.asarray(meta["object_pos_local"], dtype=np.float64)
    if object_pos_local.shape != (3,):
        raise ValueError(f"object_pos_local must have shape (3,), got {object_pos_local.shape}.")
    return object_pos_w[0] - object_pos_local


def _scalar_at(arr: np.ndarray, index: int) -> float:
    return float(np.asarray(arr[index]).reshape(-1)[0])


def _expected_decoded_opening(opening_m: float) -> float:
    convention = DEFAULT_SIMVLA_CONVENTION
    if opening_m <= convention.gripper_close_threshold_m:
        return convention.closed_finger_m
    return convention.open_finger_m


def _rotation_error_rad(decoded_quat_wxyz: np.ndarray, target_quat_wxyz: np.ndarray) -> float | None:
    if not np.all(np.isfinite(target_quat_wxyz)):
        return None
    decoded = R.from_quat(quat_wxyz_to_xyzw(decoded_quat_wxyz))
    target = R.from_quat(quat_wxyz_to_xyzw(target_quat_wxyz))
    return float((decoded.inv() * target).magnitude())


def _max_uint8_error(actual: np.ndarray, expected: np.ndarray) -> int:
    return int(np.max(np.abs(actual.astype(np.int16) - expected.astype(np.int16))))


def _max_float_error(actual: np.ndarray, expected: np.ndarray) -> float:
    return float(np.max(np.abs(np.asarray(actual, dtype=np.float64) - np.asarray(expected, dtype=np.float64))))
