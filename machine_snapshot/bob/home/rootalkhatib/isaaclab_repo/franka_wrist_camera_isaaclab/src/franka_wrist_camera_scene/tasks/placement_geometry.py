"""Geometry helpers for object placement on support surfaces."""

from __future__ import annotations

import torch


def object_root_z_on_support(
    support_surface_z: float,
    object_bbox_min_z: float,
    bottom_clearance_m: float,
) -> float:
    return support_surface_z - object_bbox_min_z + bottom_clearance_m


def object_root_pose_on_support(
    xy_pos: tuple[float, float],
    support_surface_z: float,
    object_bbox_min_z: float,
    bottom_clearance_m: float,
) -> tuple[float, float, float]:
    return (
        xy_pos[0],
        xy_pos[1],
        object_root_z_on_support(
            support_surface_z=support_surface_z,
            object_bbox_min_z=object_bbox_min_z,
            bottom_clearance_m=bottom_clearance_m,
        ),
    )


def object_root_z_at_receptacle_rim(
    receptacle_root_z: float | torch.Tensor,
    receptacle_bbox_max_z: float,
    object_bbox_min_z: float,
    rim_clearance_m: float,
) -> float | torch.Tensor:
    """Compute the object root Z coordinate for releasing at the receptacle rim."""
    receptacle_top_z = receptacle_root_z + receptacle_bbox_max_z
    return receptacle_top_z - object_bbox_min_z + rim_clearance_m

