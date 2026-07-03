from math import isclose
from unittest import TestCase

from franka_wrist_camera_scene.tasks.placement_geometry import (
    object_root_pose_on_support,
    object_root_z_at_receptacle_rim,
    object_root_z_on_support,
)


class PlacementGeometryTest(TestCase):
    def test_object_root_z_on_support_places_bbox_bottom_above_surface(self) -> None:
        root_z = object_root_z_on_support(
            support_surface_z=1.05,
            object_bbox_min_z=-0.024,
            bottom_clearance_m=0.006,
        )

        self.assertTrue(isclose(root_z, 1.08))

    def test_object_root_pose_on_support_keeps_xy_and_derives_z(self) -> None:
        root_pose = object_root_pose_on_support(
            xy_pos=(0.58, -0.16),
            support_surface_z=1.05,
            object_bbox_min_z=-0.024,
            bottom_clearance_m=0.006,
        )

        self.assertEqual(root_pose[:2], (0.58, -0.16))
        self.assertTrue(isclose(root_pose[2], 1.08))

    def test_object_root_z_at_receptacle_rim_places_bbox_bottom_above_rim(self) -> None:
        object_bbox_min_z = -0.03
        receptacle_bbox_max_z = 0.12
        rim_clearance = 0.02
        receptacle_root_z = 1.05

        root_z = object_root_z_at_receptacle_rim(
            receptacle_root_z=receptacle_root_z,
            receptacle_bbox_max_z=receptacle_bbox_max_z,
            object_bbox_min_z=object_bbox_min_z,
            rim_clearance_m=rim_clearance,
        )

        # Expected: 1.05 + 0.12 - (-0.03) + 0.02 = 1.22
        self.assertTrue(isclose(root_z, 1.22))


