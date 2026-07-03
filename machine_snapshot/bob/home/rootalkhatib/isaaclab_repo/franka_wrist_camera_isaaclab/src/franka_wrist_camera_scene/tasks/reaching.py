"""Reaching task definitions."""

from __future__ import annotations

from dataclasses import dataclass

from franka_wrist_camera_scene.settings import TABLE_HEIGHT_M
from franka_wrist_camera_scene.tasks.placement_geometry import object_root_pose_on_support

from .base import TaskSpec

REACH_MODE_TOP_CENTER = "top_center"
REACH_MODE_NEAREST_TOP_SURFACE = "nearest_top_surface"
REACH_GEOMETRY_EPS = 1e-6

SURFACE_REACH_AFFORDANCES = frozenset(("container", "physical_container", "support"))
SURFACE_REACH_CATEGORY_IDS = frozenset(("basket", "bin", "bowl", "cup", "plate", "tray"))

REACHING_POSTURE_BIAS_JOINT_POS = (
    ("panda_joint1", 0.0),
    ("panda_joint2", -0.569),
    ("panda_joint3", 0.0),
    ("panda_joint4", -2.810),
    ("panda_joint5", 0.0),
    ("panda_joint6", 3.14159),
    ("panda_joint7", -2.2751),
)


@dataclass(frozen=True, slots=True)
class ReachingTaskSpec(TaskSpec):
    """Static single-object reaching task."""

    object_name: str = "target_cube"
    ee_body_name: str = "panda_hand"
    instruction: str = "reach the object"

    object_pos_local: tuple[float, float, float] = (0.58, -0.16, 1.08)
    object_reach_offset_local: tuple[float, float, float] = (0.0, 0.0, 0.0)
    object_local_bbox_min: tuple[float, float, float] | None = None
    object_local_bbox_max: tuple[float, float, float] | None = None

    tcp_offset_local: tuple[float, float, float] = (0.0, 0.0, 0.10)

    closed_finger_m: float = 0.0
    direct_reach_max_speed_m_s: float = 0.16
    reach_dwell_s: float = 1.0
    reach_surface_clearance_m: float = 0.01
    success_threshold_m: float = 0.01
    max_success_target_displacement_m: float = 0.02

    posture_bias_joint_pos: tuple[tuple[str, float], ...] = REACHING_POSTURE_BIAS_JOINT_POS
    posture_bias_gain: float = 0.5


def instruction_for_object(object_label: str) -> str:
    return f"reach the {object_label}"


def reach_mode_for_object(category_id: str | None, affordances: tuple[str, ...]) -> str:
    if category_id in SURFACE_REACH_CATEGORY_IDS:
        return REACH_MODE_NEAREST_TOP_SURFACE
    if SURFACE_REACH_AFFORDANCES.intersection(affordances):
        return REACH_MODE_NEAREST_TOP_SURFACE
    return REACH_MODE_TOP_CENTER


def object_reach_offset_from_geometry(
    object_xy: tuple[float, float],
    robot_base_xy: tuple[float, float] | None,
    bbox_min: tuple[float, float, float],
    bbox_max: tuple[float, float, float],
    reach_surface_clearance_m: float,
    reach_mode: str,
) -> tuple[float, float, float]:
    reach_z = bbox_max[2] + reach_surface_clearance_m
    if reach_mode == REACH_MODE_TOP_CENTER:
        return (0.0, 0.0, reach_z)
    if reach_mode != REACH_MODE_NEAREST_TOP_SURFACE:
        raise ValueError(f"Unsupported reaching mode: {reach_mode!r}")
    if robot_base_xy is None:
        raise ValueError("robot_base_xy is required for nearest-surface reaching targets.")

    dx = robot_base_xy[0] - object_xy[0]
    dy = robot_base_xy[1] - object_xy[1]
    distance = max((dx * dx + dy * dy) ** 0.5, REACH_GEOMETRY_EPS)
    ux = dx / distance
    uy = dy / distance

    half_x = max(abs(bbox_min[0]), abs(bbox_max[0]))
    half_y = max(abs(bbox_min[1]), abs(bbox_max[1]))
    scale_x = half_x / max(abs(ux), REACH_GEOMETRY_EPS)
    scale_y = half_y / max(abs(uy), REACH_GEOMETRY_EPS)
    scale = min(scale_x, scale_y)
    return (ux * scale, uy * scale, reach_z)


def make_reaching_episode_spec(
    base_spec: ReachingTaskSpec,
    object_xy_offset: tuple[float, float],
    object_label: str,
    object_local_bbox_min: tuple[float, float, float] | None = None,
    object_local_bbox_max: tuple[float, float, float] | None = None,
    object_category_id: str | None = None,
    object_affordances: tuple[str, ...] = (),
    robot_base_xy: tuple[float, float] | None = None,
) -> ReachingTaskSpec:
    object_xy = (
        base_spec.object_pos_local[0] + object_xy_offset[0],
        base_spec.object_pos_local[1] + object_xy_offset[1],
    )

    if object_local_bbox_min is None:
        object_pos = (*object_xy, base_spec.object_pos_local[2])
    else:
        object_pos = object_root_pose_on_support(
            xy_pos=object_xy,
            support_surface_z=TABLE_HEIGHT_M,
            object_bbox_min_z=object_local_bbox_min[2],
            bottom_clearance_m=0.003,
        )

    reach_offset = base_spec.object_reach_offset_local
    if object_local_bbox_min is not None and object_local_bbox_max is not None:
        reach_mode = reach_mode_for_object(object_category_id, object_affordances)
        reach_offset = object_reach_offset_from_geometry(
            object_xy=object_xy,
            robot_base_xy=robot_base_xy,
            bbox_min=object_local_bbox_min,
            bbox_max=object_local_bbox_max,
            reach_surface_clearance_m=base_spec.reach_surface_clearance_m,
            reach_mode=reach_mode,
        )

    return ReachingTaskSpec(
        instruction=instruction_for_object(object_label),
        object_name=base_spec.object_name,
        ee_body_name=base_spec.ee_body_name,
        object_pos_local=object_pos,
        object_reach_offset_local=reach_offset,
        object_local_bbox_min=object_local_bbox_min,
        object_local_bbox_max=object_local_bbox_max,
        tcp_offset_local=base_spec.tcp_offset_local,
        closed_finger_m=base_spec.closed_finger_m,
        direct_reach_max_speed_m_s=base_spec.direct_reach_max_speed_m_s,
        reach_dwell_s=base_spec.reach_dwell_s,
        reach_surface_clearance_m=base_spec.reach_surface_clearance_m,
        success_threshold_m=base_spec.success_threshold_m,
        max_success_target_displacement_m=base_spec.max_success_target_displacement_m,
        posture_bias_joint_pos=base_spec.posture_bias_joint_pos,
        posture_bias_gain=base_spec.posture_bias_gain,
    )
