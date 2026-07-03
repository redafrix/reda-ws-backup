"""Scripted reaching policy using a simple finite-state machine."""

from __future__ import annotations

import torch
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene

from ..tasks.reaching import ReachingTaskSpec
from ..utils.tensors import as_torch
from .reaching_targets import compute_reaching_targets
from .scripted_base import PolicyCommand


def _reach_point_w(scene: InteractiveScene, spec: ReachingTaskSpec, device: torch.device) -> torch.Tensor:
    obj_pos_w = as_torch(scene[spec.object_name].data.root_pos_w)[:, :3]
    reach_offset = torch.tensor(spec.object_reach_offset_local, device=device).view(1, 3)
    return obj_pos_w + reach_offset


class ReachingScriptedPolicy:
    """Scripted finite-state machine policy for deterministic reaching."""

    def __init__(self, spec: ReachingTaskSpec):
        self.spec = spec
        self.state = "move_to_target"
        self._scene = None
        self._device = None
        self._motion = None
        self._state_start_time = None
        self._ee_body_id = None
        self._latched_reach_pos_w = None
        self._latched_ee_quat_w = None

    @property
    def latched_reach_pos_w(self) -> torch.Tensor:
        if self._latched_reach_pos_w is None:
            raise RuntimeError("Reaching target was not latched.")
        return self._latched_reach_pos_w

    @property
    def latched_ee_quat_w(self) -> torch.Tensor:
        if self._latched_ee_quat_w is None:
            raise RuntimeError("Reaching end-effector orientation was not latched.")
        return self._latched_ee_quat_w

    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
        """Bind simulation scene and get device reference."""
        if scene.num_envs != 1:
            raise RuntimeError("ReachingScriptedPolicy currently supports only num_envs=1.")
        self._scene = scene
        self._device = robot.device
        self._ee_body_id = robot.find_bodies(self.spec.ee_body_name)[0][0]

    def reset(self) -> None:
        """Reset the policy to the initial state."""
        if self._scene is None or self._device is None:
            raise RuntimeError("ReachingScriptedPolicy was not bound before reset().")
        self.state = "move_to_target"
        self._motion = None
        self._state_start_time = None
        self._latched_reach_pos_w = _reach_point_w(self._scene, self.spec, self._device).detach().clone()
        robot = self._scene["robot"]
        self._latched_ee_quat_w = as_torch(robot.data.body_pose_w)[:, self._ee_body_id, 3:7].detach().clone()

    def step(self, obs: dict | None, sim_time_s: float) -> PolicyCommand:
        """Compute the next command target according to the FSM state."""
        if self._scene is None or self._device is None or self._ee_body_id is None:
            raise RuntimeError("ReachingScriptedPolicy was not bound before step().")

        robot = self._scene["robot"]
        ee_pos_w = as_torch(robot.data.body_pose_w)[:, self._ee_body_id, :3]
        ee_quat_w = as_torch(robot.data.body_pose_w)[:, self._ee_body_id, 3:7]

        reach_pos_w = self.latched_reach_pos_w
        tcp_offset_local = torch.tensor(self.spec.tcp_offset_local, device=self._device).view(1, 3)

        target_hand_pos_w, self.state, self._state_start_time, self._motion, done = compute_reaching_targets(
            sim_time_s=sim_time_s,
            state=self.state,
            state_start_time=self._state_start_time,
            motion=self._motion,
            ee_pos_w=ee_pos_w,
            ee_quat_w=ee_quat_w,
            reach_pos_w=reach_pos_w,
            tcp_offset_local=tcp_offset_local,
            direct_reach_max_speed_m_s=self.spec.direct_reach_max_speed_m_s,
            reach_dwell_s=self.spec.reach_dwell_s,
            target_quat_w=self.latched_ee_quat_w,
        )

        finger_opening = self.spec.closed_finger_m

        return PolicyCommand(
            target_pos_w=target_hand_pos_w,
            target_quat_w=self.latched_ee_quat_w,
            finger_opening_m=finger_opening,
            done=done,
        )
