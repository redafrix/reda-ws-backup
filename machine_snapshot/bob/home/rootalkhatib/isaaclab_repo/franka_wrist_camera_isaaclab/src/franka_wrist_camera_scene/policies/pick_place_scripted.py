"""Scripted pick-and-place policy using a simple finite-state machine."""

from __future__ import annotations

import torch
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene
from isaaclab.utils.math import quat_apply

from ..control.grasp_orientation import downward_gripper_quat_for_closing_axis
from ..control.motion_primitives import MinimumJerkWaypointMotion
from ..tasks.placement_geometry import object_root_z_at_receptacle_rim, object_root_z_on_support
from ..tasks.pick_place import PickPlaceTaskSpec
from ..tasks.receptacle_pose import placement_target_root_pos_w
from ..utils.tensors import as_torch
from .scripted_base import PolicyCommand


class PickPlaceScriptedPolicy:
    """Scripted finite-state machine policy for deterministic pick-and-place."""

    def __init__(self, spec: PickPlaceTaskSpec):
        self.spec = spec
        self.state = "approach_object"
        self._scene = None
        self._device = None
        self._motion = None
        self._state_start_time = None
        self._ee_body_id = None
        self._grasp_tcp_offset_from_root_w = None
        self._lift_pos_w = None
        self._placement_target_root_pos_w = None
        self._object_reset_pos_w = None

        self.quat_wxyz = torch.tensor([0.0, 1.0, 0.0, 0.0])

    def _actual_tcp_pos_w(self, ee_pos_w: torch.Tensor, tcp_offset_w: torch.Tensor) -> torch.Tensor:
        return ee_pos_w + tcp_offset_w.view(1, 3)

    def _require_finite_tensor(self, name: str, value: torch.Tensor) -> None:
        if not bool(torch.isfinite(value).all().item()):
            raise RuntimeError(
                f"Pick-place policy produced non-finite {name} in state={self.state}: "
                f"{value.detach().cpu().tolist()}"
            )

    def _object_displacement_from_reset_m(self, obj_pos_w: torch.Tensor) -> torch.Tensor:
        if self._object_reset_pos_w is None:
            raise RuntimeError("Object reset pose was not latched before disturbance check.")
        reset_pos = self._object_reset_pos_w.to(device=obj_pos_w.device, dtype=obj_pos_w.dtype)
        return torch.linalg.norm(obj_pos_w[:, :3] - reset_pos[:, :3], dim=-1)

    def _check_object_pregrasp_stability(
        self,
        obj_pos_w: torch.Tensor,
        *,
        sim_time_s: float,
        stage: str,
    ) -> None:
        if self._object_reset_pos_w is None:
            return

        displacement_m = self._object_displacement_from_reset_m(obj_pos_w)
        reset_pos = self._object_reset_pos_w.to(device=obj_pos_w.device, dtype=obj_pos_w.dtype)
        z_drop_m = reset_pos[:, 2] - obj_pos_w[:, 2]

        object_entity = self._scene[self.spec.object_name]
        root_vel_w = as_torch(object_entity.data.root_vel_w)
        speed_m_s = torch.linalg.norm(root_vel_w[:, :3], dim=-1)

        self._require_finite_tensor("object_pregrasp_position", obj_pos_w)
        self._require_finite_tensor("object_pregrasp_velocity", root_vel_w)
        self._require_finite_tensor("object_pregrasp_displacement_m", displacement_m)
        self._require_finite_tensor("object_pregrasp_z_drop_m", z_drop_m)
        self._require_finite_tensor("object_pregrasp_speed_m_s", speed_m_s)

        if self.spec.pregrasp_object_displacement_tolerance_m > 0.0:
            moved = displacement_m > self.spec.pregrasp_object_displacement_tolerance_m
        else:
            moved = torch.zeros_like(displacement_m, dtype=torch.bool)
        fell = z_drop_m > self.spec.pregrasp_object_fall_tolerance_m
        if bool((moved | fell).any().item()):
            raise RuntimeError(
                "Active pick-place object was disturbed before grasp; refusing to latch a fallen/moved object. "
                f"stage={stage}, state={self.state}, sim_time_s={sim_time_s:.4f}, "
                f"object={self.spec.object_name!r}, "
                f"reset_pos_w={reset_pos.detach().cpu().tolist()}, "
                f"current_pos_w={obj_pos_w.detach().cpu().tolist()}, "
                f"root_vel_w={root_vel_w.detach().cpu().tolist()}, "
                f"displacement_m={displacement_m.detach().cpu().tolist()}, "
                f"z_drop_m={z_drop_m.detach().cpu().tolist()}, "
                f"speed_m_s={speed_m_s.detach().cpu().tolist()}, "
                f"displacement_tolerance_m={self.spec.pregrasp_object_displacement_tolerance_m}, "
                f"fall_tolerance_m={self.spec.pregrasp_object_fall_tolerance_m}"
            )

    def _initial_lift_waypoint_w(
        self,
        ee_pos_w: torch.Tensor,
        object_transit_pos: torch.Tensor,
    ) -> torch.Tensor:
        """Lift from home before lateral object approach to avoid low arm-link sweeps."""
        lift_pos = ee_pos_w.clone()
        min_z = torch.maximum(ee_pos_w[:, 2], object_transit_pos[:, 2])
        lift_pos[:, 2] = min_z + float(self.spec.initial_lift_clearance_m)
        return lift_pos

    def _release_finger_opening(self, sim_time_s: float) -> float:
        if self._state_start_time is None:
            raise RuntimeError("Release opening requested before the release state started.")

        elapsed_s = sim_time_s - self._state_start_time
        if self.spec.release_dwell_s <= 0.0:
            return self.spec.open_finger_m

        release_fraction = min(max(elapsed_s / self.spec.release_dwell_s, 0.0), 1.0)
        opening_range_m = self.spec.open_finger_m - self.spec.closed_finger_m
        return self.spec.closed_finger_m + release_fraction * opening_range_m

    def _object_root_on_support_w(self, xy_pos_w: torch.Tensor) -> torch.Tensor:
        if self.spec.object_local_bbox_min is None:
            raise RuntimeError("Pick-place requires object bbox metadata for placement height.")

        root_pos = xy_pos_w.clone()
        root_pos[:, 2] = object_root_z_on_support(
            support_surface_z=self.spec.support_surface_z_local,
            object_bbox_min_z=float(self.spec.object_local_bbox_min[2]),
            bottom_clearance_m=self.spec.object_bottom_clearance_m,
        )
        return root_pos

    def _object_root_in_receptacle_w(self, receptacle_root_w: torch.Tensor) -> torch.Tensor:
        if (
            self.spec.object_local_bbox_min is None
            or self.spec.placement_target_local_bbox_min is None
            or self.spec.placement_target_local_bbox_max is None
        ):
            raise RuntimeError("Receptacle placement requires object and placement target geometry.")

        root_pos = receptacle_root_w.clone()
        root_pos[:, 2] = object_root_z_at_receptacle_rim(
            receptacle_root_z=receptacle_root_w[:, 2],
            receptacle_bbox_max_z=float(self.spec.placement_target_local_bbox_max[2]),
            object_bbox_min_z=float(self.spec.object_local_bbox_min[2]),
            rim_clearance_m=self.spec.receptacle_release_rim_clearance_m,
        )
        return root_pos

    def _episode_receptacle_root_pos_w(self) -> torch.Tensor:
        if self._placement_target_root_pos_w is None:
            raise RuntimeError("Receptacle target requested before policy reset latched the receptacle pose.")
        return self._placement_target_root_pos_w

    def _object_top_tcp_targets_w(self, obj_pos_w: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        if self.spec.object_local_bbox_min is None or self.spec.object_local_bbox_max is None:
            raise RuntimeError("Pick-place requires object bbox metadata for top grasp targeting.")

        bbox_min_z = float(self.spec.object_local_bbox_min[2])
        bbox_max_z = float(self.spec.object_local_bbox_max[2])
        bbox_height_m = bbox_max_z - bbox_min_z
        top_grasp_depth_m = min(
            self.spec.max_top_grasp_depth_m,
            max(self.spec.top_grasp_depth_m, bbox_height_m * self.spec.top_grasp_depth_fraction),
        )

        grasp_tcp = obj_pos_w.clone()
        grasp_tcp[:, 2] = obj_pos_w[:, 2] + bbox_max_z - top_grasp_depth_m

        pregrasp_tcp = grasp_tcp.clone()
        pregrasp_tcp[:, 2] += self.spec.pregrasp_clearance_m

        transit_tcp = grasp_tcp.clone()
        transit_tcp[:, 2] += self.spec.object_transit_clearance_m

        return grasp_tcp, pregrasp_tcp, transit_tcp

    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
        """Bind simulation scene and get device reference."""
        if scene.num_envs != 1:
            raise RuntimeError("PickPlaceScriptedPolicy currently supports only num_envs=1.")
        self._scene = scene
        self._device = robot.device
        if self.spec.grasp_closing_axis_xy is None:
            self.quat_wxyz = self.quat_wxyz.to(self._device)
        else:
            self.quat_wxyz = downward_gripper_quat_for_closing_axis(
                closing_axis_xy=self.spec.grasp_closing_axis_xy,
                device=self._device,
            )
        self._ee_body_id = robot.find_bodies(self.spec.ee_body_name)[0][0]

    def reset(self) -> None:
        """Reset the policy to the initial state."""
        self.state = "approach_object"
        self._motion = None
        self._state_start_time = None
        self._grasp_tcp_offset_from_root_w = None
        self._lift_pos_w = None
        self._placement_target_root_pos_w = None
        self._object_reset_pos_w = None
        if self._scene is not None:
            obj_pos_w = as_torch(self._scene[self.spec.object_name].data.root_pos_w)[:, :3].clone()
            self._require_finite_tensor("object_reset_pos_w", obj_pos_w)
            self._object_reset_pos_w = obj_pos_w
        if self._scene is not None and self.spec.placement_target_pos_local is not None:
            self._placement_target_root_pos_w = placement_target_root_pos_w(self._scene, self.spec).clone()
            self._require_finite_tensor("placement_target_root_pos_w", self._placement_target_root_pos_w)

    def step(self, obs: dict | None, sim_time_s: float) -> PolicyCommand:
        """Compute the next command target according to the FSM state."""
        if self._scene is None or self._device is None or self._ee_body_id is None:
            raise RuntimeError("PickPlaceScriptedPolicy was not bound before step().")

        robot = self._scene["robot"]
        ee_pos_w = as_torch(robot.data.body_pose_w)[:, self._ee_body_id, :3]
        self._require_finite_tensor("ee_pos_w", ee_pos_w)
        num_envs = self._scene.num_envs

        # Target definitions (TCP targets)
        # Dynamic object position from the simulated RigidObject (allows randomization)
        obj_pos = as_torch(self._scene[self.spec.object_name].data.root_pos_w)
        self._require_finite_tensor("object_root_pos_w", obj_pos)

        place_local = torch.tensor(self.spec.place_pos_local, device=self._device)
        # Convert env-local coordinates to world coordinates using env origins
        place_pos = self._scene.env_origins + place_local.view(1, 3)

        tcp_offset_local = torch.tensor(self.spec.tcp_offset_local, device=self._device).view(1, 3)
        tcp_offset_w = quat_apply(self.quat_wxyz.view(1, 4), tcp_offset_local).view(3)

        obj_grasp_tcp, obj_pregrasp_tcp, obj_transit_tcp = self._object_top_tcp_targets_w(obj_pos)

        obj_hand_pos = obj_grasp_tcp - tcp_offset_w.view(1, 3)
        pregrasp_pos = obj_pregrasp_tcp - tcp_offset_w.view(1, 3)
        object_transit_pos = obj_transit_tcp - tcp_offset_w.view(1, 3)

        lift_pos = None
        if self._lift_pos_w is not None:
            lift_pos = self._lift_pos_w
        else:
            lift_pos = obj_hand_pos.clone()
            lift_pos[:, 2] += self.spec.lift_height_m

        place_hand_pos = None
        place_pre_pos = None
        place_transit_pos = None

        if self._grasp_tcp_offset_from_root_w is not None:
            if self.spec.placement_target_pos_local is None:
                place_root_pos = self._object_root_on_support_w(place_pos)
            else:
                receptacle_root_w = self._episode_receptacle_root_pos_w()
                place_root_pos = self._object_root_in_receptacle_w(receptacle_root_w)
            place_release_tcp = place_root_pos + self._grasp_tcp_offset_from_root_w

            place_pre_tcp = place_release_tcp.clone()
            place_pre_tcp[:, 2] += self.spec.place_pregrasp_clearance_m

            place_hand_pos = place_release_tcp - tcp_offset_w.view(1, 3)
            place_pre_pos = place_pre_tcp - tcp_offset_w.view(1, 3)

            place_transit_pos = place_pre_pos.clone()
            place_transit_pos[:, 2] = lift_pos[:, 2]

        if self.state in ["carry_to_place", "open", "retreat", "done"]:
            if place_hand_pos is None or place_pre_pos is None or place_transit_pos is None or lift_pos is None:
                raise RuntimeError("Placement targets requested before grasp offset was latched.")

        target_pos_w = ee_pos_w.clone()
        target_quat_w = self.quat_wxyz.repeat(num_envs, 1)
        finger_opening = self.spec.open_finger_m
        done = False

        if self.state == "approach_object":
            self._check_object_pregrasp_stability(
                obj_pos,
                sim_time_s=sim_time_s,
                stage="approach_object",
            )
            if self._motion is None:
                initial_lift_pos = self._initial_lift_waypoint_w(ee_pos_w, object_transit_pos)
                self._require_finite_tensor("initial_lift_pos", initial_lift_pos)
                self._motion = MinimumJerkWaypointMotion.from_segment_speeds(
                    waypoints_w=(ee_pos_w, initial_lift_pos, object_transit_pos, pregrasp_pos, obj_hand_pos),
                    quat_w=target_quat_w,
                    start_time_s=sim_time_s,
                    max_speed_m_s=(
                        self.spec.lift_max_speed_m_s,
                        self.spec.free_space_max_speed_m_s,
                        self.spec.approach_max_speed_m_s,
                        self.spec.approach_max_speed_m_s,
                    ),
                )
            pos, quat, finished = self._motion.sample(sim_time_s)
            target_pos_w = pos
            target_quat_w = quat
            if finished:
                self.state = "close"
                self._state_start_time = sim_time_s
                self._motion = None

        elif self.state == "close":
            self._check_object_pregrasp_stability(
                obj_pos,
                sim_time_s=sim_time_s,
                stage="close",
            )
            target_pos_w = obj_hand_pos
            finger_opening = self.spec.closed_finger_m
            if sim_time_s - self._state_start_time >= self.spec.grasp_dwell_s:
                self._check_object_pregrasp_stability(
                    obj_pos,
                    sim_time_s=sim_time_s,
                    stage="close_to_carry_latch",
                )
                actual_tcp_pos_w = self._actual_tcp_pos_w(ee_pos_w, tcp_offset_w)
                self._require_finite_tensor("actual_tcp_pos_w", actual_tcp_pos_w)
                self._grasp_tcp_offset_from_root_w = (actual_tcp_pos_w - obj_pos).clone()
                self._require_finite_tensor("grasp_tcp_offset_from_root_w", self._grasp_tcp_offset_from_root_w)
                self._lift_pos_w = obj_hand_pos.clone()
                self._lift_pos_w[:, 2] += self.spec.lift_height_m
                self.state = "carry_to_place"
                self._state_start_time = None

        elif self.state == "carry_to_place":
            finger_opening = self.spec.closed_finger_m
            if self._motion is None:
                self._motion = MinimumJerkWaypointMotion.from_segment_speeds(
                    waypoints_w=(ee_pos_w, lift_pos, place_transit_pos, place_pre_pos, place_hand_pos),
                    quat_w=target_quat_w,
                    start_time_s=sim_time_s,
                    max_speed_m_s=(
                        self.spec.lift_max_speed_m_s,
                        self.spec.free_space_max_speed_m_s,
                        self.spec.approach_max_speed_m_s,
                        self.spec.approach_max_speed_m_s,
                    ),
                )
            pos, quat, finished = self._motion.sample(sim_time_s)
            target_pos_w = pos
            target_quat_w = quat
            if finished:
                self.state = "open"
                self._state_start_time = sim_time_s
                self._motion = None

        elif self.state == "open":
            target_pos_w = place_hand_pos
            finger_opening = self._release_finger_opening(sim_time_s)
            if sim_time_s - self._state_start_time >= self.spec.release_dwell_s:
                self.state = "retreat"
                self._state_start_time = None

        elif self.state == "retreat":
            finger_opening = self.spec.open_finger_m
            if self._motion is None:
                self._motion = MinimumJerkWaypointMotion.from_speed(
                    waypoints_w=(ee_pos_w, place_transit_pos),
                    quat_w=target_quat_w,
                    start_time_s=sim_time_s,
                    max_speed_m_s=self.spec.retreat_max_speed_m_s,
                )
            pos, quat, finished = self._motion.sample(sim_time_s)
            target_pos_w = pos
            target_quat_w = quat
            if finished:
                self.state = "done"
                self._motion = None

        elif self.state == "done":
            target_pos_w = place_transit_pos
            finger_opening = self.spec.open_finger_m
            done = True

        self._require_finite_tensor("target_pos_w", target_pos_w)
        self._require_finite_tensor("target_quat_w", target_quat_w)

        return PolicyCommand(
            target_pos_w=target_pos_w,
            target_quat_w=target_quat_w,
            finger_opening_m=finger_opening,
            done=done,
        )
