"""Pi0.5 action policy adapter for IsaacLab Cartesian control loops."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch

from franka_wrist_camera_scene.pi05.geometry import (
    Pi05ControlScales,
    Pi05ProprioSource,
    decode_pi05_libero_action,
    encode_pi05_libero_state,
)
from franka_wrist_camera_scene.pi05.image_tools import resize_with_pad_uint8
from franka_wrist_camera_scene.pi05.runtime import Pi05RemoteRuntime
from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand


@dataclass(frozen=True, slots=True)
class Pi05LiveObservation:
    language_instruction: str
    agent_rgb: np.ndarray
    wrist_rgb: np.ndarray
    ee_pos_w: np.ndarray
    ee_quat_wxyz: np.ndarray
    env_origin_w: np.ndarray
    commanded_finger_opening_m: float
    joint_position: np.ndarray | None = None
    gripper_position: np.ndarray | None = None


@dataclass(frozen=True, slots=True)
class Pi05DroidControlScales:
    joint_velocity_scale_rad_s: float = 1.0
    droid_control_fps: float = 15.0
    open_finger_m: float = 0.04
    closed_finger_m: float = 0.0
    gripper_open_threshold: float = 0.5


@dataclass(frozen=True, slots=True)
class Pi05DroidJointCommand:
    target_joint_pos: torch.Tensor
    recorder_command: PolicyCommand


class Pi05ActionPolicy:
    """Convert live Isaac observations into Pi0.5 LIBERO action chunks."""

    def __init__(
        self,
        runtime: Pi05RemoteRuntime,
        replan_steps: int = 10,
        command_device: torch.device | str = "cuda",
        control_scales: Pi05ControlScales = Pi05ControlScales(),
    ) -> None:
        if replan_steps <= 0:
            raise ValueError(f"replan_steps must be positive, got {replan_steps}.")
        self.runtime = runtime
        self.replan_steps = int(replan_steps)
        self.command_device = torch.device(command_device)
        self.control_scales = control_scales
        self._action_chunk: np.ndarray | None = None
        self._chunk_index = 0
        self._last_command: PolicyCommand | None = None
        self._last_camera_tick: int | None = None

    def reset(self) -> None:
        self._action_chunk = None
        self._chunk_index = 0
        self._last_command = None
        self._last_camera_tick = None
        self.runtime.reset()

    def step(self, observation: Pi05LiveObservation, camera_tick: int) -> PolicyCommand:
        self._validate_next_camera_tick(camera_tick)
        if self._needs_replan(camera_tick):
            self._action_chunk = self._infer_action_chunk(observation)
            self._chunk_index = 0

        if self._action_chunk is None:
            raise RuntimeError("Pi05ActionPolicy has no action chunk after replan.")

        action_index = min(self._chunk_index, self._action_chunk.shape[0] - 1)
        decoded = decode_pi05_libero_action(
            action=self._action_chunk[action_index],
            ee_pos_w=observation.ee_pos_w,
            ee_quat_wxyz=observation.ee_quat_wxyz,
            scales=self.control_scales,
        )
        self._chunk_index += 1
        command = PolicyCommand(
            target_pos_w=torch.as_tensor(decoded.target_pos_w, dtype=torch.float32, device=self.command_device).view(1, 3),
            target_quat_w=torch.as_tensor(decoded.target_quat_wxyz, dtype=torch.float32, device=self.command_device).view(1, 4),
            finger_opening_m=float(decoded.finger_opening_m),
        )
        self._last_command = command
        self._last_camera_tick = camera_tick
        return command

    def _validate_next_camera_tick(self, camera_tick: int) -> None:
        if camera_tick < 0:
            raise ValueError(f"camera_tick must be non-negative, got {camera_tick}.")
        if self._last_camera_tick is not None and camera_tick <= self._last_camera_tick:
            raise RuntimeError(
                "Pi05ActionPolicy.step() must be called once per new camera frame. "
                f"last_camera_tick={self._last_camera_tick}, got {camera_tick}."
            )

    def _needs_replan(self, camera_tick: int) -> bool:
        return self._action_chunk is None or camera_tick % self.replan_steps == 0

    def _infer_action_chunk(self, observation: Pi05LiveObservation) -> np.ndarray:
        state = encode_pi05_libero_state(
            Pi05ProprioSource(
                ee_pos_w=observation.ee_pos_w,
                ee_quat_wxyz=observation.ee_quat_wxyz,
                env_origin_w=observation.env_origin_w,
                commanded_finger_opening_m=observation.commanded_finger_opening_m,
            )
        )
        openpi_observation = {
            "observation/image": resize_with_pad_uint8(observation.agent_rgb, 224, 224),
            "observation/wrist_image": resize_with_pad_uint8(observation.wrist_rgb, 224, 224),
            "observation/state": state,
            "prompt": observation.language_instruction,
        }
        return self.runtime.infer(openpi_observation)


class Pi05DroidActionPolicy:
    """Convert live Isaac observations into OpenPI DROID joint-space commands."""

    def __init__(
        self,
        runtime: Pi05RemoteRuntime,
        replan_steps: int = 8,
        command_device: torch.device | str = "cpu",
        control_scales: Pi05DroidControlScales = Pi05DroidControlScales(),
    ) -> None:
        if replan_steps <= 0:
            raise ValueError(f"replan_steps must be positive, got {replan_steps}.")
        if control_scales.droid_control_fps <= 0:
            raise ValueError("droid_control_fps must be positive.")
        self.runtime = runtime
        self.replan_steps = int(replan_steps)
        self.command_device = torch.device(command_device)
        self.control_scales = control_scales
        self._action_chunk: np.ndarray | None = None
        self._chunk_index = 0
        self._last_camera_tick: int | None = None

    def reset(self) -> None:
        self._action_chunk = None
        self._chunk_index = 0
        self._last_camera_tick = None
        self.runtime.reset()

    def step(self, observation: Pi05LiveObservation, camera_tick: int) -> Pi05DroidJointCommand:
        self._validate_next_camera_tick(camera_tick)
        if self._needs_replan(camera_tick):
            self._action_chunk = self._infer_action_chunk(observation)
            self._chunk_index = 0

        if self._action_chunk is None:
            raise RuntimeError("Pi05DroidActionPolicy has no action chunk after replan.")
        if observation.joint_position is None:
            raise ValueError("DROID policy requires observation.joint_position.")

        action_index = min(self._chunk_index, self._action_chunk.shape[0] - 1)
        action = np.asarray(self._action_chunk[action_index], dtype=np.float32)
        self._chunk_index += 1

        joint_position = np.asarray(observation.joint_position, dtype=np.float32)
        if joint_position.shape != (7,):
            raise ValueError(f"DROID joint_position must have shape (7,), got {joint_position.shape}.")
        joint_velocity = np.clip(action[:7], -1.0, 1.0)
        command_dt_s = 1.0 / float(self.control_scales.droid_control_fps)
        target_joint_pos = joint_position + joint_velocity * float(self.control_scales.joint_velocity_scale_rad_s) * command_dt_s
        finger_opening = (
            self.control_scales.open_finger_m
            if float(action[7]) > float(self.control_scales.gripper_open_threshold)
            else self.control_scales.closed_finger_m
        )
        recorder_command = PolicyCommand(
            target_pos_w=torch.as_tensor(observation.ee_pos_w, dtype=torch.float32, device=self.command_device).view(1, 3),
            target_quat_w=torch.as_tensor(observation.ee_quat_wxyz, dtype=torch.float32, device=self.command_device).view(1, 4),
            finger_opening_m=float(finger_opening),
        )
        self._last_camera_tick = camera_tick
        return Pi05DroidJointCommand(
            target_joint_pos=torch.as_tensor(target_joint_pos, dtype=torch.float32, device=self.command_device).view(1, 7),
            recorder_command=recorder_command,
        )

    def _validate_next_camera_tick(self, camera_tick: int) -> None:
        if camera_tick < 0:
            raise ValueError(f"camera_tick must be non-negative, got {camera_tick}.")
        if self._last_camera_tick is not None and camera_tick <= self._last_camera_tick:
            raise RuntimeError(
                "Pi05DroidActionPolicy.step() must be called once per new camera frame. "
                f"last_camera_tick={self._last_camera_tick}, got {camera_tick}."
            )

    def _needs_replan(self, camera_tick: int) -> bool:
        return self._action_chunk is None or camera_tick % self.replan_steps == 0

    def _infer_action_chunk(self, observation: Pi05LiveObservation) -> np.ndarray:
        if observation.joint_position is None or observation.gripper_position is None:
            raise ValueError("DROID policy requires joint_position and gripper_position observations.")
        openpi_observation = {
            "observation/exterior_image_1_left": resize_with_pad_uint8(observation.agent_rgb, 224, 224),
            "observation/wrist_image_left": resize_with_pad_uint8(observation.wrist_rgb, 224, 224),
            "observation/joint_position": np.asarray(observation.joint_position, dtype=np.float32),
            "observation/gripper_position": np.asarray(observation.gripper_position, dtype=np.float32),
            "prompt": observation.language_instruction,
        }
        return self.runtime.infer(openpi_observation)
