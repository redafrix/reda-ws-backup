from dataclasses import dataclass
import torch
from isaaclab.scene import InteractiveScene
from isaaclab.utils.math import quat_apply

from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
from franka_wrist_camera_scene.tasks.receptacle_pose import placement_target_root_pos_w
from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
from franka_wrist_camera_scene.utils.tensors import as_torch


@dataclass(frozen=True, slots=True)
class ReachingSuccessMetrics:
    success: torch.Tensor
    reached_latched_target: torch.Tensor
    reached_live_target: torch.Tensor
    target_displacement_ok: torch.Tensor
    latched_distance_m: torch.Tensor
    live_distance_m: torch.Tensor
    target_displacement_m: torch.Tensor


def receptacle_xy_radius_from_bbox(
    bbox_min: tuple[float, float, float],
    bbox_max: tuple[float, float, float],
    margin_m: float,
) -> float:
    size_x = float(bbox_max[0]) - float(bbox_min[0])
    size_y = float(bbox_max[1]) - float(bbox_min[1])
    return 0.5 * min(size_x, size_y) + margin_m


def pick_place_success(
    scene: InteractiveScene,
    spec: PickPlaceTaskSpec,
    xy_threshold_m: float = 0.08,
    z_threshold_m: float = 0.08,
) -> torch.Tensor:
    """Return per-env success for placing the object near the target area."""
    obj = scene[spec.object_name]
    obj_pos_w = as_torch(obj.data.root_pos_w)

    if spec.placement_target_pos_local is not None:
        if (
            spec.object_local_bbox_min is None
            or spec.placement_target_local_bbox_min is None
            or spec.placement_target_local_bbox_max is None
        ):
            raise RuntimeError("Receptacle placement success requires object and placement target geometry.")

        receptacle_pos_w = placement_target_root_pos_w(scene, spec).to(obj_pos_w.device)
        xy_error = torch.linalg.norm(obj_pos_w[:, :2] - receptacle_pos_w[:, :2], dim=-1)

        xy_threshold = receptacle_xy_radius_from_bbox(
            bbox_min=spec.placement_target_local_bbox_min,
            bbox_max=spec.placement_target_local_bbox_max,
            margin_m=0.025,
        )

        object_bottom_z = obj_pos_w[:, 2] + float(spec.object_local_bbox_min[2])
        receptacle_top_z = receptacle_pos_w[:, 2] + float(spec.placement_target_local_bbox_max[2])
        receptacle_bottom_z = receptacle_pos_w[:, 2] + float(spec.placement_target_local_bbox_min[2])
        vertical_ok = (
            (object_bottom_z >= receptacle_bottom_z - 0.03)
            & (object_bottom_z <= receptacle_top_z + 0.05)
        )
        return (xy_error <= xy_threshold) & vertical_ok

    target_pos_local = torch.tensor(spec.place_pos_local, device=obj_pos_w.device).view(1, 3)
    target_pos_w = scene.env_origins + target_pos_local

    xy_error = torch.linalg.norm(obj_pos_w[:, :2] - target_pos_w[:, :2], dim=-1)
    z_error = torch.abs(obj_pos_w[:, 2] - target_pos_w[:, 2])

    return (xy_error <= xy_threshold_m) & (z_error <= z_threshold_m)


def reaching_success_metrics(
    scene: InteractiveScene,
    spec: ReachingTaskSpec,
    target_reach_pos_w: torch.Tensor,
    threshold_m: float | None = None,
    max_target_displacement_m: float | None = None,
) -> ReachingSuccessMetrics:
    robot = scene["robot"]
    ee_body_id = robot.find_bodies(spec.ee_body_name)[0][0]
    ee_pose_w = as_torch(robot.data.body_pose_w)[:, ee_body_id]
    ee_pos_w = ee_pose_w[:, :3]
    ee_quat_w = ee_pose_w[:, 3:7]

    tcp_offset_local = torch.tensor(spec.tcp_offset_local, device=ee_pos_w.device).view(1, 3)
    tcp_offset_w = quat_apply(ee_quat_w, tcp_offset_local.expand(ee_pos_w.shape[0], -1))
    tcp_pos_w = ee_pos_w + tcp_offset_w

    latched_pos_w = target_reach_pos_w.to(device=tcp_pos_w.device, dtype=tcp_pos_w.dtype)
    if latched_pos_w.shape != tcp_pos_w.shape:
        raise ValueError(
            f"target_reach_pos_w shape must be {tuple(tcp_pos_w.shape)}, got {tuple(latched_pos_w.shape)}."
        )

    obj = scene[spec.object_name]
    obj_pos_w = as_torch(obj.data.root_pos_w)[:, :3].to(device=tcp_pos_w.device, dtype=tcp_pos_w.dtype)
    reach_offset = torch.tensor(spec.object_reach_offset_local, device=tcp_pos_w.device).view(1, 3)
    live_pos_w = obj_pos_w + reach_offset

    threshold = spec.success_threshold_m if threshold_m is None else threshold_m
    max_displacement = (
        spec.max_success_target_displacement_m
        if max_target_displacement_m is None
        else max_target_displacement_m
    )

    latched_distance = torch.linalg.norm(tcp_pos_w - latched_pos_w, dim=-1)
    live_distance = torch.linalg.norm(tcp_pos_w - live_pos_w, dim=-1)
    target_displacement = torch.linalg.norm(live_pos_w - latched_pos_w, dim=-1)

    reached_latched = latched_distance <= threshold
    reached_live = live_distance <= threshold
    displacement_ok = target_displacement <= max_displacement

    success = reached_latched | (reached_live & displacement_ok)

    return ReachingSuccessMetrics(
        success=success,
        reached_latched_target=reached_latched,
        reached_live_target=reached_live,
        target_displacement_ok=displacement_ok,
        latched_distance_m=latched_distance,
        live_distance_m=live_distance,
        target_displacement_m=target_displacement,
    )


def reaching_success(
    scene: InteractiveScene,
    spec: ReachingTaskSpec,
    threshold_m: float | None = None,
    target_reach_pos_w: torch.Tensor | None = None,
) -> torch.Tensor:
    """Return success if the TCP reaches the episode's target point.

    During collection, reaching success is evaluated against the target point
    latched at reset because dynamic target objects may be displaced by contact.
    If no target point is provided, this predicate uses the object's live pose
    for standalone checks.
    """
    if target_reach_pos_w is None:
        obj = scene[spec.object_name]
        obj_pos_w = as_torch(obj.data.root_pos_w)[:, :3]
        reach_offset = torch.tensor(spec.object_reach_offset_local, device=obj_pos_w.device).view(1, 3)
        target_reach_pos_w = obj_pos_w + reach_offset

    return reaching_success_metrics(
        scene=scene,
        spec=spec,
        target_reach_pos_w=target_reach_pos_w,
        threshold_m=threshold_m,
    ).success
