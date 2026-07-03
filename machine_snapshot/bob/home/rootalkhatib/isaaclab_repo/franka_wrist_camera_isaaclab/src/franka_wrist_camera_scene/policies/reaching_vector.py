"""Vectorized scripted reaching policy."""

from __future__ import annotations

from dataclasses import dataclass

import torch
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene

from franka_wrist_camera_scene.control.motion_primitives import MinimumJerkPositionMotion
from franka_wrist_camera_scene.policies.reaching_targets import quat_apply_xyzw
from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
from franka_wrist_camera_scene.utils.tensors import as_torch

MOVE_TO_TARGET = 0
REACH_DWELL = 1
DONE = 2


@dataclass(slots=True)
class _EnvMotionState:
    motion: MinimumJerkPositionMotion | None = None
    state_start_time_s: float | None = None


class VectorReachingScriptedPolicy:
    """Per-env reaching FSM for one vectorized Isaac Lab scene."""

    def __init__(self, specs: tuple[ReachingTaskSpec, ...], active_env_count: int):
        if not specs:
            raise ValueError("VectorReachingScriptedPolicy requires at least one spec.")
        if active_env_count <= 0 or active_env_count > len(specs):
            raise ValueError(
                f"active_env_count must be in [1, {len(specs)}], got {active_env_count}."
            )
        self.specs = specs
        self.active_env_count = active_env_count
        self._scene: InteractiveScene | None = None
        self._device: torch.device | None = None
        self._ee_body_id: int | None = None
        self._phase: torch.Tensor | None = None
        self._motions: list[_EnvMotionState] = []
        self._latched_reach_pos_w: torch.Tensor | None = None
        self._latched_ee_quat_w: torch.Tensor | None = None
        self._tcp_offset_local: torch.Tensor | None = None
        self._closed_finger_m = float(specs[0].closed_finger_m)

    @property
    def latched_reach_pos_w(self) -> torch.Tensor:
        if self._latched_reach_pos_w is None:
            raise RuntimeError("Reaching targets were not latched.")
        return self._latched_reach_pos_w

    @property
    def latched_ee_quat_w(self) -> torch.Tensor:
        if self._latched_ee_quat_w is None:
            raise RuntimeError("Reaching end-effector orientations were not latched.")
        return self._latched_ee_quat_w

    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
        if len(self.specs) != scene.num_envs:
            raise ValueError(
                f"Vector policy expected {scene.num_envs} specs, got {len(self.specs)}."
            )
        first_spec = self.specs[0]
        if any(spec.ee_body_name != first_spec.ee_body_name for spec in self.specs):
            raise ValueError("Vector reaching requires a shared end-effector body across envs.")
        if any(spec.tcp_offset_local != first_spec.tcp_offset_local for spec in self.specs):
            raise ValueError("Vector reaching requires a shared TCP offset across envs.")
        if any(spec.closed_finger_m != first_spec.closed_finger_m for spec in self.specs):
            raise ValueError("Vector reaching requires a shared closed gripper width across envs.")

        self._scene = scene
        self._device = robot.device
        self._ee_body_id = robot.find_bodies(first_spec.ee_body_name)[0][0]
        self._tcp_offset_local = torch.tensor(
            first_spec.tcp_offset_local,
            device=self._device,
            dtype=torch.float32,
        ).view(1, 3)

    def reset(self) -> None:
        if self._scene is None or self._device is None:
            raise RuntimeError("VectorReachingScriptedPolicy was not bound before reset().")

        self._phase = torch.full((len(self.specs),), MOVE_TO_TARGET, device=self._device, dtype=torch.long)
        self._motions = [_EnvMotionState() for _ in self.specs]
        latched = torch.empty((len(self.specs), 3), device=self._device, dtype=torch.float32)
        for env_index, spec in enumerate(self.specs):
            obj_pos_w = as_torch(self._scene[spec.object_name].data.root_pos_w)[env_index, :3]
            reach_offset = torch.tensor(
                spec.object_reach_offset_local,
                device=self._device,
                dtype=obj_pos_w.dtype,
            )
            latched[env_index] = obj_pos_w + reach_offset
        self._latched_reach_pos_w = latched.detach().clone()
        robot = self._scene["robot"]
        self._latched_ee_quat_w = as_torch(robot.data.body_pose_w)[:, self._ee_body_id, 3:7].detach().clone()

    def _current_tcp_pos_w(self, ee_pos_w: torch.Tensor, ee_quat_w: torch.Tensor) -> torch.Tensor:
        if self._tcp_offset_local is None:
            raise RuntimeError("VectorReachingScriptedPolicy was not bound before step().")
        tcp_offset_w = quat_apply_xyzw(ee_quat_w, self._tcp_offset_local.expand(ee_pos_w.shape[0], -1))
        return ee_pos_w + tcp_offset_w

    def step(self, obs: dict | None, sim_time_s: float) -> PolicyCommand:
        if (
            self._scene is None
            or self._device is None
            or self._ee_body_id is None
            or self._phase is None
            or self._latched_reach_pos_w is None
            or self._latched_ee_quat_w is None
            or self._tcp_offset_local is None
        ):
            raise RuntimeError("VectorReachingScriptedPolicy was not fully initialized before step().")

        robot = self._scene["robot"]
        ee_pose_w = as_torch(robot.data.body_pose_w)[:, self._ee_body_id]
        ee_pos_w = ee_pose_w[:, :3]
        ee_quat_w = ee_pose_w[:, 3:7]
        current_tcp_pos_w = self._current_tcp_pos_w(ee_pos_w, ee_quat_w)
        desired_tcp_pos_w = self._latched_reach_pos_w.clone()

        done = self._phase == DONE
        for env_index, spec in enumerate(self.specs):
            phase = int(self._phase[env_index].item())
            motion_state = self._motions[env_index]

            if phase == MOVE_TO_TARGET:
                if motion_state.motion is None:
                    motion_state.motion = MinimumJerkPositionMotion.from_speed(
                        start_pos_w=current_tcp_pos_w[env_index : env_index + 1],
                        goal_pos_w=self._latched_reach_pos_w[env_index : env_index + 1],
                        start_time_s=sim_time_s,
                        max_speed_m_s=spec.direct_reach_max_speed_m_s,
                    )
                pos, finished = motion_state.motion.sample(sim_time_s)
                desired_tcp_pos_w[env_index] = pos[0]
                if finished:
                    self._phase[env_index] = REACH_DWELL
                    motion_state.motion = None
                    motion_state.state_start_time_s = sim_time_s

            elif phase == REACH_DWELL:
                desired_tcp_pos_w[env_index] = self._latched_reach_pos_w[env_index]
                if motion_state.state_start_time_s is None:
                    motion_state.state_start_time_s = sim_time_s
                if sim_time_s - motion_state.state_start_time_s >= spec.reach_dwell_s:
                    self._phase[env_index] = DONE
                    done[env_index] = True

            elif phase == DONE:
                desired_tcp_pos_w[env_index] = self._latched_reach_pos_w[env_index]
                done[env_index] = True
            else:
                raise RuntimeError(f"Unsupported reaching vector phase: {phase}.")

        tcp_offset_w_command = quat_apply_xyzw(
            self.latched_ee_quat_w,
            self._tcp_offset_local.expand(ee_pos_w.shape[0], -1),
        )
        target_hand_pos_w = desired_tcp_pos_w - tcp_offset_w_command

        return PolicyCommand(
            target_pos_w=target_hand_pos_w,
            target_quat_w=self.latched_ee_quat_w,
            finger_opening_m=self._closed_finger_m,
            done=done[: self.active_env_count].clone(),
        )
