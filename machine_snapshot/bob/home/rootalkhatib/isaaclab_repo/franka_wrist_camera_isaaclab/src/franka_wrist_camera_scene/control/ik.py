"""Inverse Kinematics solver using Isaac Lab differential IK."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

import torch

from isaaclab.assets import Articulation
from isaaclab.controllers import DifferentialIKController, DifferentialIKControllerCfg
from isaaclab.managers import SceneEntityCfg
from isaaclab.scene import InteractiveScene
from isaaclab.utils.math import compute_pose_error, subtract_frame_transforms

from franka_wrist_camera_scene.utils.tensors import as_torch


@dataclass(frozen=True, slots=True)
class PostureBiasCfg:
    """Joint-space posture preference for redundant position IK."""

    joint_pos: Mapping[str, float]
    gain: float
    damping: float = 0.01

    def __post_init__(self) -> None:
        if self.gain < 0.0:
            raise ValueError("posture bias gain must be non-negative.")
        if self.damping <= 0.0:
            raise ValueError("posture bias damping must be positive.")


class CartesianIKController:
    """Robot arm end-effector IK controller using differential IK."""

    def __init__(
        self,
        arm_joint_expr: str = "panda_joint.*",
        end_effector_body: str = "panda_hand",
        command_type: str = "pose",
        posture_bias: PostureBiasCfg | None = None,
        pose_error_weights: tuple[float, float, float, float, float, float] | None = None,
    ):
        if command_type not in {"pose", "position"}:
            raise ValueError(f"Invalid command_type: {command_type}")
        if pose_error_weights is not None and command_type != "pose":
            raise ValueError("pose_error_weights can only be used with pose command mode.")
        if pose_error_weights is not None and any(weight <= 0.0 for weight in pose_error_weights):
            raise ValueError("pose_error_weights must all be positive.")
        self.command_type = command_type
        self.arm_joint_expr = arm_joint_expr
        self.end_effector_body = end_effector_body
        self._posture_bias = posture_bias
        self._pose_error_weights = pose_error_weights

        self._entity = None
        self._ik = None
        self._robot = None
        self._ee_jacobian_index = None
        self._target_pos_w = None
        self._target_quat_w = None
        self._posture_target_joint_pos = None
        self._posture_joint_mask = None

    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
        """Resolve scene references and initialize differential IK."""
        self._entity = SceneEntityCfg(
            "robot",
            joint_names=[self.arm_joint_expr],
            body_names=[self.end_effector_body],
        )
        self._entity.resolve(scene)
        self._robot = robot

        self._ee_jacobian_index = self._entity.body_ids[0] - int(robot.is_fixed_base)

        self._ik = DifferentialIKController(
            DifferentialIKControllerCfg(
                command_type=self.command_type,
                use_relative_mode=False,
                ik_method="dls",
                ik_params={"lambda_val": 0.01},
            ),
            num_envs=scene.num_envs,
            device=robot.device,
        )
        self._resolve_posture_target(robot)

    def reset(self) -> None:
        """Reset the differential IK solver state."""
        self._ik.reset()
        self._target_pos_w = None
        self._target_quat_w = None

    def set_posture_bias(self, posture_bias: PostureBiasCfg | None) -> None:
        """Set the optional joint posture bias projected into the IK nullspace."""
        self._posture_bias = posture_bias
        self._posture_target_joint_pos = None
        self._posture_joint_mask = None
        if self._entity is not None and self._robot is not None:
            self._resolve_posture_target(self._robot)

    def _robot_joint_names(self, robot: Articulation) -> list[str]:
        joint_names = getattr(robot, "joint_names", None)
        if joint_names is None:
            joint_names = getattr(robot.data, "joint_names", None)
        if joint_names is None:
            raise RuntimeError("Robot joint names are required for posture bias.")
        return list(joint_names)

    def _resolve_posture_target(self, robot: Articulation) -> None:
        if self._posture_bias is None or not self._posture_bias.joint_pos or self._posture_bias.gain == 0.0:
            self._posture_target_joint_pos = None
            self._posture_joint_mask = None
            return

        joint_names = self._robot_joint_names(robot)
        unknown_names = set(self._posture_bias.joint_pos) - set(joint_names)
        if unknown_names:
            raise ValueError(f"Unknown posture bias joint names: {sorted(unknown_names)}")

        controlled_joint_ids = self._entity.joint_ids
        target = torch.zeros(len(controlled_joint_ids), device=robot.device, dtype=torch.float32)
        mask = torch.zeros(len(controlled_joint_ids), device=robot.device, dtype=torch.bool)
        for local_index, joint_id in enumerate(controlled_joint_ids):
            joint_name = joint_names[joint_id]
            if joint_name in self._posture_bias.joint_pos:
                target[local_index] = float(self._posture_bias.joint_pos[joint_name])
                mask[local_index] = True

        self._posture_target_joint_pos = target.view(1, -1)
        self._posture_joint_mask = mask.view(1, -1)

    @property
    def end_effector_body_id(self) -> int:
        if self._entity is None:
            raise RuntimeError("CartesianIKController was not bound.")
        return self._entity.body_ids[0]

    def set_target_pose(self, target_pos_w: torch.Tensor, target_quat_w: torch.Tensor) -> None:
        """Set the target end-effector pose in world coordinates."""
        if self.command_type != "pose":
            raise RuntimeError("Cannot call set_target_pose in position mode.")
        self._target_pos_w = target_pos_w
        self._target_quat_w = target_quat_w

    def set_target_position(self, target_pos_w: torch.Tensor) -> None:
        """Set the target end-effector position in world coordinates."""
        if self.command_type != "position":
            raise RuntimeError("Cannot call set_target_position in pose mode.")
        self._target_pos_w = target_pos_w

    def apply(self, scene: InteractiveScene, robot: Articulation) -> None:
        """Compute and apply joint command targets for the arm."""
        root_pose_w = as_torch(robot.data.root_pose_w)
        ee_pose_w = as_torch(robot.data.body_pose_w)[:, self._entity.body_ids[0]]

        ee_pos_b, ee_quat_b = subtract_frame_transforms(
            root_pose_w[:, :3],
            root_pose_w[:, 3:7],
            ee_pose_w[:, :3],
            ee_pose_w[:, 3:7],
        )

        joint_pos = as_torch(robot.data.joint_pos)[:, self._entity.joint_ids]

        if self.command_type == "pose":
            if self._target_pos_w is None or self._target_quat_w is None:
                raise RuntimeError("CartesianIKController target pose was not set before apply().")

            # Transform target pose from world to robot base frame
            target_pos_b, target_quat_b = subtract_frame_transforms(
                root_pose_w[:, :3],
                root_pose_w[:, 3:7],
                self._target_pos_w,
                self._target_quat_w,
            )
            self._ik.set_command(torch.cat((target_pos_b, target_quat_b), dim=-1))
        else:
            if self._target_pos_w is None:
                raise RuntimeError("CartesianIKController target position was not set before apply().")

            # Transform target position from world to robot base frame
            target_pos_b, _ = subtract_frame_transforms(
                root_pose_w[:, :3],
                root_pose_w[:, 3:7],
                self._target_pos_w,
            )
            self._ik.set_command(target_pos_b, ee_quat=ee_quat_b)

        # Compute joint velocities/positions from Jacobian and current joint states
        jacobian_joint_ids = [joint_id + robot.num_base_dofs for joint_id in self._entity.joint_ids]
        jacobian = as_torch(robot.data.body_link_jacobian_w)[:, self._ee_jacobian_index, :, jacobian_joint_ids]

        if self.command_type == "pose" and self._pose_error_weights is not None:
            joint_pos_des = self._compute_weighted_pose_target(
                ee_pos=ee_pos_b,
                ee_quat=ee_quat_b,
                target_pos=target_pos_b,
                target_quat=target_quat_b,
                jacobian=jacobian,
                joint_pos=joint_pos,
            )
        else:
            joint_pos_des = self._ik.compute(ee_pos_b, ee_quat_b, jacobian, joint_pos)
        if self._posture_bias is not None:
            joint_pos_des = self._apply_posture_bias(joint_pos_des, joint_pos, jacobian)

        robot.set_joint_position_target_index(target=joint_pos_des, joint_ids=self._entity.joint_ids)

    def _compute_weighted_pose_target(
        self,
        *,
        ee_pos: torch.Tensor,
        ee_quat: torch.Tensor,
        target_pos: torch.Tensor,
        target_quat: torch.Tensor,
        jacobian: torch.Tensor,
        joint_pos: torch.Tensor,
    ) -> torch.Tensor:
        position_error, axis_angle_error = compute_pose_error(
            ee_pos,
            ee_quat,
            target_pos,
            target_quat,
            rot_error_type="axis_angle",
        )
        pose_error = torch.cat((position_error, axis_angle_error), dim=1)
        weights = torch.tensor(
            self._pose_error_weights,
            device=jacobian.device,
            dtype=jacobian.dtype,
        ).view(1, 6)
        weighted_jacobian = jacobian * weights.unsqueeze(-1)
        weighted_error = pose_error * weights

        jacobian_t = weighted_jacobian.transpose(1, 2)
        lambda_val = self._ik.cfg.ik_params["lambda_val"]
        lambda_matrix = (lambda_val**2) * torch.eye(n=weighted_jacobian.shape[1], device=jacobian.device)
        delta_joint_pos = (
            jacobian_t
            @ torch.inverse(weighted_jacobian @ jacobian_t + lambda_matrix)
            @ weighted_error.unsqueeze(-1)
        ).squeeze(-1)
        return joint_pos + delta_joint_pos

    def _apply_posture_bias(
        self,
        joint_pos_des: torch.Tensor,
        joint_pos: torch.Tensor,
        jacobian: torch.Tensor,
    ) -> torch.Tensor:
        if self._posture_target_joint_pos is None or self._posture_joint_mask is None:
            return joint_pos_des
        if self._posture_bias is None or self._posture_bias.gain == 0.0:
            return joint_pos_des

        posture_error = self._posture_target_joint_pos.to(joint_pos) - joint_pos
        posture_error = torch.where(
            self._posture_joint_mask.to(joint_pos.device),
            posture_error,
            torch.zeros_like(posture_error),
        )

        task_jacobian = jacobian[:, :3, :] if self.command_type == "position" else jacobian
        jacobian_transpose = task_jacobian.transpose(1, 2)
        task_space_matrix = task_jacobian @ jacobian_transpose
        task_dim = task_jacobian.shape[1]
        eye_task = torch.eye(task_dim, device=jacobian.device, dtype=jacobian.dtype).expand(
            jacobian.shape[0],
            -1,
            -1,
        )
        damped_inverse = torch.linalg.inv(
            task_space_matrix + (self._posture_bias.damping**2) * eye_task
        )
        jacobian_pinv = jacobian_transpose @ damped_inverse

        num_joints = joint_pos.shape[1]
        eye_joint = torch.eye(num_joints, device=jacobian.device, dtype=jacobian.dtype).expand(
            jacobian.shape[0],
            -1,
            -1,
        )
        nullspace = eye_joint - jacobian_pinv @ task_jacobian
        posture_step = (nullspace @ posture_error.unsqueeze(-1)).squeeze(-1)
        return joint_pos_des + self._posture_bias.gain * posture_step
