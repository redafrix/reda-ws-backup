"""Geometry checks for target objects and physical receptacles."""

from __future__ import annotations

from franka_wrist_camera_scene.objects.geometry_registry import ObjectPlanarGeometry


def object_fits_gripper(geometry: ObjectPlanarGeometry, max_width_m: float) -> bool:
    return geometry.planar_extent_minor <= max_width_m


def object_fits_receptacle(
    object_geometry: ObjectPlanarGeometry,
    receptacle_geometry: ObjectPlanarGeometry,
    max_height_to_width: float,
) -> bool:
    object_height = object_geometry.local_bbox_max[2] - object_geometry.local_bbox_min[2]
    receptacle_width = min(
        receptacle_geometry.local_bbox_max[0] - receptacle_geometry.local_bbox_min[0],
        receptacle_geometry.local_bbox_max[1] - receptacle_geometry.local_bbox_min[1],
    )
    return receptacle_width > 0.0 and object_height <= max_height_to_width * receptacle_width
