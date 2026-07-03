import sys
from math import isclose
from unittest import TestCase
from unittest.mock import MagicMock
import torch


class PickPlaceTaskTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._original_modules = {}
        for mod_name in [
            "isaaclab",
            "isaaclab.scene",
            "isaaclab.assets",
            "isaaclab.utils",
            "isaaclab.utils.math",
            "isaaclab.sim",
            "isaaclab.controllers",
            "isaaclab.sensors",
            "isaaclab.managers",
        ]:
            if mod_name in sys.modules:
                cls._original_modules[mod_name] = sys.modules[mod_name]
            sys.modules[mod_name] = MagicMock()

    @classmethod
    def tearDownClass(cls) -> None:
        for mod_name in [
            "isaaclab",
            "isaaclab.scene",
            "isaaclab.assets",
            "isaaclab.utils",
            "isaaclab.utils.math",
            "isaaclab.sim",
            "isaaclab.controllers",
            "isaaclab.sensors",
            "isaaclab.managers",
        ]:
            if mod_name in cls._original_modules:
                sys.modules[mod_name] = cls._original_modules[mod_name]
            else:
                sys.modules.pop(mod_name, None)

    def test_default_receptacle_release_has_one_centimeter_rim_clearance(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
        self.assertTrue(isclose(PickPlaceTaskSpec().receptacle_release_rim_clearance_m, 0.01))
        self.assertTrue(isclose(PickPlaceTaskSpec().release_dwell_s, 1.0))

    def test_receptacle_release_targets_rim_support_surface(self) -> None:
        from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec

        spec = PickPlaceTaskSpec(
            object_local_bbox_min=(-0.03, -0.03, -0.12),
            object_local_bbox_max=(0.03, 0.03, 0.12),
            placement_target_local_bbox_min=(-0.1, -0.1, -0.06),
            placement_target_local_bbox_max=(0.1, 0.1, 0.06),
            receptacle_release_rim_clearance_m=0.01,
        )
        policy = PickPlaceScriptedPolicy(spec)

        root_pos = policy._object_root_in_receptacle_w(torch.tensor([[0.5, 0.2, 1.116]]))

        self.assertTrue(isclose(float(root_pos[0, 2]), 1.306, abs_tol=1e-6))

    def test_release_finger_opening_ramps_over_release_dwell(self) -> None:
        from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec

        spec = PickPlaceTaskSpec(
            closed_finger_m=0.0,
            open_finger_m=0.04,
            release_dwell_s=2.0,
        )
        policy = PickPlaceScriptedPolicy(spec)
        policy._state_start_time = 10.0

        self.assertTrue(isclose(policy._release_finger_opening(10.0), 0.0))
        self.assertTrue(isclose(policy._release_finger_opening(11.0), 0.02))
        self.assertTrue(isclose(policy._release_finger_opening(12.0), 0.04))

    def test_top_grasp_depth_adapts_to_round_object_height(self) -> None:
        from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec

        spec = PickPlaceTaskSpec(
            object_local_bbox_min=(-0.042061, -0.0425, -0.042296),
            object_local_bbox_max=(0.042061, 0.0425, 0.042296),
            top_grasp_depth_m=0.025,
            top_grasp_depth_fraction=0.45,
            max_top_grasp_depth_m=0.04,
        )
        policy = PickPlaceScriptedPolicy(spec)

        grasp_tcp, _, _ = policy._object_top_tcp_targets_w(torch.tensor([[0.58, -0.12, 1.098296]]))

        expected_depth = 0.084592 * 0.45
        expected_z = 1.098296 + 0.042296 - expected_depth
        self.assertTrue(isclose(float(grasp_tcp[0, 2]), expected_z, abs_tol=1e-6))
        self.assertLess(float(grasp_tcp[0, 2]) - 1.098296, 0.01)

    def test_policy_latches_current_receptacle_pose_on_reset(self) -> None:
        from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec

        target = MagicMock()
        target.data.root_pos_w = torch.tensor([[0.58, -0.16, 1.08]])
        receptacle = MagicMock()
        receptacle.data.root_pos_w = torch.tensor([[0.64, 0.18, 1.06]])
        scene = MagicMock()
        scene.__getitem__.side_effect = {
            "target_cube": target,
            "place_receptacle": receptacle,
        }.__getitem__
        scene.env_origins = torch.zeros((1, 3))
        spec = PickPlaceTaskSpec(
            placement_target_pos_local=(0.55, 0.22, 1.05),
            placement_target_local_bbox_min=(-0.1, -0.1, -0.04),
            placement_target_local_bbox_max=(0.1, 0.1, 0.04),
        )
        policy = PickPlaceScriptedPolicy(spec)
        policy._scene = scene

        policy.reset()
        receptacle.data.root_pos_w = torch.tensor([[100.0, 100.0, -10.0]])

        torch.testing.assert_close(policy._episode_receptacle_root_pos_w(), torch.tensor([[0.64, 0.18, 1.06]]))

    def test_make_pick_place_episode_spec_requires_bbox_metadata(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
        with self.assertRaisesRegex(ValueError, "bbox metadata"):
            make_pick_place_episode_spec(
                base_spec=PickPlaceTaskSpec(),
                object_xy_offset=(0.0, 0.0),
                place_xy_offset=(0.0, 0.0),
                object_label="object",
            )

    def test_make_pick_place_episode_spec_uses_bbox_height_for_object_and_place(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
        spec = make_pick_place_episode_spec(
            base_spec=PickPlaceTaskSpec(),
            object_xy_offset=(0.01, -0.02),
            place_xy_offset=(-0.03, 0.04),
            object_label="box",
            object_quat_wxyz=(0.0, 1.0, 0.0, 0.0),
            object_local_bbox_min=(-0.02, -0.03, -0.024),
            object_local_bbox_max=(0.02, 0.03, 0.04),
        )

        self.assertEqual(spec.object_pos_local[:2], (0.59, -0.18))
        self.assertEqual(spec.object_quat_wxyz, (0.0, 1.0, 0.0, 0.0))
        self.assertTrue(isclose(spec.object_pos_local[2], 1.08))
        self.assertEqual(spec.place_pos_local[:2], (0.52, 0.26))
        self.assertTrue(isclose(spec.place_pos_local[2], 1.08))

    def test_make_pick_place_episode_spec_preserves_pregrasp_tolerances(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
        spec = make_pick_place_episode_spec(
            base_spec=PickPlaceTaskSpec(
                pregrasp_object_displacement_tolerance_m=0.06,
                pregrasp_object_fall_tolerance_m=0.05,
            ),
            object_xy_offset=(0.0, 0.0),
            place_xy_offset=(0.0, 0.0),
            object_label="box",
            object_local_bbox_min=(-0.02, -0.03, -0.024),
            object_local_bbox_max=(0.02, 0.03, 0.04),
        )

        self.assertTrue(isclose(spec.pregrasp_object_displacement_tolerance_m, 0.06))
        self.assertTrue(isclose(spec.pregrasp_object_fall_tolerance_m, 0.05))

    def test_make_pick_place_episode_spec_uses_receptacle_center_and_instruction(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
        spec = make_pick_place_episode_spec(
            base_spec=PickPlaceTaskSpec(),
            object_xy_offset=(0.0, 0.0),
            place_xy_offset=(0.2, 0.2),
            object_label="box",
            object_local_bbox_min=(-0.02, -0.03, -0.024),
            object_local_bbox_max=(0.02, 0.03, 0.04),
            placement_target_pos_local=(0.60, 0.25, 1.07),
            placement_target_quat_wxyz=(0.0, 1.0, 0.0, 0.0),
            placement_target_local_bbox_min=(-0.07, -0.07, -0.02),
            placement_target_local_bbox_max=(0.07, 0.07, 0.06),
            placement_label="bowl",
        )

        self.assertEqual(spec.instruction, "pick up the box and place it in the bowl")
        self.assertEqual(spec.place_pos_local[:2], (0.60, 0.25))
        self.assertTrue(isclose(spec.place_pos_local[2], 1.08))
        self.assertEqual(spec.placement_target_pos_local, (0.60, 0.25, 1.07))
        self.assertEqual(spec.placement_target_quat_wxyz, (0.0, 1.0, 0.0, 0.0))

    def test_make_pick_place_episode_spec_requires_complete_receptacle_metadata(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
        with self.assertRaisesRegex(ValueError, "Receptacle pick-place"):
            make_pick_place_episode_spec(
                base_spec=PickPlaceTaskSpec(),
                object_xy_offset=(0.0, 0.0),
                place_xy_offset=(0.0, 0.0),
                object_label="box",
                object_local_bbox_min=(-0.02, -0.03, -0.024),
                object_local_bbox_max=(0.02, 0.03, 0.04),
                placement_target_pos_local=(0.60, 0.25, 1.07),
            )
