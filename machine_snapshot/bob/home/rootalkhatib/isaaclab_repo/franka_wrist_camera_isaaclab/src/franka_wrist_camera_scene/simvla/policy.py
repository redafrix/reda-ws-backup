"""SimVLA policy adapter for IsaacLab Cartesian control loops."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch

from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
from franka_wrist_camera_scene.simvla.geometry import (
    SimVLAProprioSource,
    decode_simvla_action,
    encode_simvla_proprio,
)
from franka_wrist_camera_scene.simvla.image_preprocessing import preprocess_camera_views
from franka_wrist_camera_scene.simvla.runtime import SimVLARuntime


@dataclass(frozen=True, slots=True)
class SimVLALiveObservation:
    language_instruction: str
    agent_rgb: np.ndarray
    wrist_rgb: np.ndarray
    ee_pos_w: np.ndarray
    ee_quat_wxyz: np.ndarray
    env_origin_w: np.ndarray
    commanded_finger_opening_m: float


class SimVLAActionPolicy:
    """Converts live camera/proprio observations into held Cartesian commands."""

    def __init__(
        self,
        runtime: SimVLARuntime,
        image_rotation: str,
        replan_steps: int = 5,
        command_device: torch.device | str | None = None,
    ) -> None:
        if replan_steps <= 0:
            raise ValueError(f"replan_steps must be positive, got {replan_steps}.")
        self.runtime = runtime
        self.image_rotation = image_rotation
        self.replan_steps = int(replan_steps)
        self.command_device = torch.device(command_device) if command_device is not None else runtime.device
        self._action_chunk: np.ndarray | None = None
        self._chunk_index = 0
        self._last_command: PolicyCommand | None = None
        self._last_camera_tick: int | None = None
        self._last_uncertainty: dict[str, np.ndarray] = {}

    def reset(self) -> None:
        self._action_chunk = None
        self._chunk_index = 0
        self._last_command = None
        self._last_camera_tick = None
        self._last_uncertainty = {}

    @property
    def last_command(self) -> PolicyCommand:
        if self._last_command is None:
            raise RuntimeError("No SimVLA command has been produced yet.")
        return self._last_command

    @property
    def last_uncertainty(self) -> dict[str, np.ndarray]:
        return self._last_uncertainty

    def step(self, observation: SimVLALiveObservation, camera_tick: int) -> PolicyCommand:
        self._validate_next_camera_tick(camera_tick)
        if self._needs_replan(camera_tick):
            self._action_chunk = self._infer_action_chunk(observation)
            self._chunk_index = 0

        if self._action_chunk is None:
            raise RuntimeError("SimVLAActionPolicy has no action chunk after replan.")

        action_index = min(self._chunk_index, self._action_chunk.shape[0] - 1)
        decoded = decode_simvla_action(
            action=self._action_chunk[action_index],
            ee_pos_w=observation.ee_pos_w,
            ee_quat_wxyz=observation.ee_quat_wxyz,
        )
        self._chunk_index += 1
        command = PolicyCommand(
            target_pos_w=torch.as_tensor(decoded.target_pos_w, dtype=torch.float32, device=self.command_device).view(1, 3),
            target_quat_w=torch.as_tensor(
                decoded.target_quat_wxyz,
                dtype=torch.float32,
                device=self.command_device,
            ).view(1, 4),
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
                "SimVLAActionPolicy.step() must be called once per new camera frame. "
                f"last_camera_tick={self._last_camera_tick}, got {camera_tick}."
            )

    def _needs_replan(self, camera_tick: int) -> bool:
        return self._action_chunk is None or camera_tick % self.replan_steps == 0

    def _infer_action_chunk(self, observation: SimVLALiveObservation) -> np.ndarray:
        images = preprocess_camera_views(
            observation.agent_rgb,
            observation.wrist_rgb,
            self.image_rotation,
            device=self.runtime.device,
        )
        proprio = encode_simvla_proprio(
            SimVLAProprioSource(
                ee_pos_w=observation.ee_pos_w,
                ee_quat_wxyz=observation.ee_quat_wxyz,
                env_origin_w=observation.env_origin_w,
                commanded_finger_opening_m=observation.commanded_finger_opening_m,
            )
        )
        output = self.runtime.infer(
            language_instruction=observation.language_instruction,
            image_input=images.image_input,
            image_mask=images.image_mask,
            proprio=proprio,
        )
        self._last_uncertainty = output.uncertainty
        return output.actions
