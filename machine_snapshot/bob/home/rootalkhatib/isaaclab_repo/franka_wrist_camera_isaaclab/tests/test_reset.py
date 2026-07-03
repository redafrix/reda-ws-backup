import sys
from unittest import TestCase
from unittest.mock import MagicMock
import torch


class FakeStaticExtra:
    def __init__(self, num_envs: int):
        self.local_translations = torch.zeros((num_envs, 3))
        self.local_orientations = torch.zeros((num_envs, 4))
        self.world_positions = torch.zeros((num_envs, 3))
        self.world_orientations = torch.zeros((num_envs, 4))
        self.set_local_call_count = 0
        self.set_world_call_count = 0

    def set_local_poses(self, *, translations, orientations):
        self.local_translations = translations.clone()
        self.local_orientations = orientations.clone()
        self.set_local_call_count += 1

    def set_world_poses(self, *, positions, orientations):
        self.world_positions = positions.clone()
        self.world_orientations = orientations.clone()
        self.set_world_call_count += 1

    def get_local_poses(self):
        return self.local_translations, self.local_orientations

    def get_world_poses(self):
        return self.world_positions, self.world_orientations


class TestResetPickPlaceEpisode(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._original_modules = {}
        for mod_name in [
            "isaaclab",
            "isaaclab.scene",
            "isaaclab.assets",
            "isaaclab.utils",
            "isaaclab.utils.math",
            "isaaclab.utils.configclass",
            "isaaclab.sim",
            "isaaclab.controllers",
            "isaaclab.sensors",
            "isaaclab.managers",
            "pxr",
            "isaaclab_assets",
        ]:
            if mod_name in sys.modules:
                cls._original_modules[mod_name] = sys.modules[mod_name]
            sys.modules[mod_name] = MagicMock()

        def mock_convert_quat(quat, to):
            if to == "xyzw":
                return torch.cat([quat[:, 1:], quat[:, :1]], dim=-1)
            elif to == "wxyz":
                return torch.cat([quat[:, 3:], quat[:, :3]], dim=-1)
            return quat

        sys.modules["isaaclab.utils.math"].convert_quat = mock_convert_quat
        import franka_wrist_camera_scene.episode.reset
        franka_wrist_camera_scene.episode.reset.convert_quat = mock_convert_quat

    @classmethod
    def tearDownClass(cls) -> None:
        for mod_name in [
            "isaaclab",
            "isaaclab.scene",
            "isaaclab.assets",
            "isaaclab.utils",
            "isaaclab.utils.math",
            "isaaclab.utils.configclass",
            "isaaclab.sim",
            "isaaclab.controllers",
            "isaaclab.sensors",
            "isaaclab.managers",
            "pxr",
            "isaaclab_assets",
        ]:
            if mod_name in cls._original_modules:
                sys.modules[mod_name] = cls._original_modules[mod_name]
            else:
                sys.modules.pop(mod_name, None)

    def test_receptacle_pose_is_reapplied_after_scene_reset(self) -> None:
        from franka_wrist_camera_scene.episode.reset import reset_pick_place_episode
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec

        events = []
        sim = MagicMock()
        sim.get_physics_dt.return_value = 0.01

        robot = MagicMock()
        robot.data.default_root_state = torch.zeros((1, 13))
        robot.data.default_joint_pos = torch.zeros((1, 9))
        robot.data.default_joint_vel = torch.zeros((1, 9))

        target_object = MagicMock()
        target_object.data.default_root_state = torch.zeros((1, 13))

        receptacle = MagicMock()
        receptacle.data.default_root_state = torch.zeros((1, 13))
        receptacle.data.root_pos_w = torch.tensor([[0.62, 0.18, 1.06]])
        receptacle.data.root_vel_w = torch.zeros((1, 6))

        receptacle.write_root_pose_to_sim.side_effect = (
            lambda *args, **kwargs: events.append("write_receptacle_pose")
        )

        scene = MagicMock()
        scene.env_origins = torch.zeros((1, 3))
        scene.reset.side_effect = lambda: events.append("scene_reset")
        scene.__getitem__.side_effect = {
            "robot": robot,
            "target_cube": target_object,
            "place_receptacle": receptacle,
        }.__getitem__

        spec = PickPlaceTaskSpec(
            object_name="target_cube",
            placement_target_name="place_receptacle",
            placement_target_pos_local=(0.62, 0.18, 1.06),
            placement_target_quat_wxyz=(1.0, 0.0, 0.0, 0.0),
        )

        reset_pick_place_episode(sim=sim, scene=scene, spec=spec)

        self.assertEqual(events, ["scene_reset", "write_receptacle_pose", "write_receptacle_pose"])
        scene.reset.assert_called_once_with()
        self.assertEqual(receptacle.write_root_pose_to_sim.call_count, 2)
        self.assertEqual(receptacle.write_root_velocity_to_sim.call_count, 2)
        sim.step.assert_called_once()
        self.assertEqual(scene.write_data_to_sim.call_count, 2)
        scene.update.assert_called_once_with(0.01)

        written_pose = receptacle.write_root_pose_to_sim.call_args[0][0]
        expected_pose = torch.tensor([[0.62, 0.18, 1.06, 0.0, 0.0, 0.0, 1.0]])
        torch.testing.assert_close(written_pose, expected_pose)


class TestResetReachingEpisode(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._original_modules = {}
        for mod_name in [
            "isaaclab",
            "isaaclab.scene",
            "isaaclab.assets",
            "isaaclab.utils",
            "isaaclab.utils.math",
            "isaaclab.utils.configclass",
            "isaaclab.sim",
            "isaaclab.controllers",
            "isaaclab.sensors",
            "isaaclab.managers",
            "pxr",
            "isaaclab_assets",
        ]:
            if mod_name in sys.modules:
                cls._original_modules[mod_name] = sys.modules[mod_name]
            sys.modules[mod_name] = MagicMock()

        def mock_convert_quat(quat, to):
            if to == "xyzw":
                return torch.cat([quat[:, 1:], quat[:, :1]], dim=-1)
            elif to == "wxyz":
                return torch.cat([quat[:, 3:], quat[:, :3]], dim=-1)
            return quat

        sys.modules["isaaclab.utils.math"].convert_quat = mock_convert_quat
        import franka_wrist_camera_scene.episode.reset
        franka_wrist_camera_scene.episode.reset.convert_quat = mock_convert_quat

    @classmethod
    def tearDownClass(cls) -> None:
        for mod_name in [
            "isaaclab",
            "isaaclab.scene",
            "isaaclab.assets",
            "isaaclab.utils",
            "isaaclab.utils.math",
            "isaaclab.utils.configclass",
            "isaaclab.sim",
            "isaaclab.controllers",
            "isaaclab.sensors",
            "isaaclab.managers",
            "pxr",
            "isaaclab_assets",
        ]:
            if mod_name in cls._original_modules:
                sys.modules[mod_name] = cls._original_modules[mod_name]
            else:
                sys.modules.pop(mod_name, None)

    def test_reaching_reset_matches_scene_reset_order_and_rigid_quaternion_convention(self) -> None:
        from franka_wrist_camera_scene.episode.reset import reset_reaching_episode
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec

        events = []
        sim = MagicMock()
        sim.get_physics_dt.return_value = 0.01

        robot = MagicMock()
        robot.data.default_root_state = torch.zeros((1, 13))
        robot.data.default_joint_pos = torch.zeros((1, 9))
        robot.data.default_joint_vel = torch.zeros((1, 9))

        target_object = MagicMock()
        target_object.data.default_root_state = torch.zeros((1, 13))
        target_object.data.root_pos_w = torch.tensor([[0.58, -0.16, 1.08]])
        target_object.data.root_vel_w = torch.zeros((1, 6))
        target_object.write_root_pose_to_sim.side_effect = (
            lambda *args, **kwargs: events.append("write_object_pose")
        )

        scene = MagicMock()
        scene.env_origins = torch.zeros((1, 3))
        scene.reset.side_effect = lambda: events.append("scene_reset")
        scene.__getitem__.side_effect = {
            "robot": robot,
            "target_cube": target_object,
        }.__getitem__

        spec = ReachingTaskSpec(
            object_name="target_cube",
            object_pos_local=(0.58, -0.16, 1.08),
        )

        reset_reaching_episode(sim=sim, scene=scene, spec=spec)

        self.assertEqual(events, ["scene_reset", "write_object_pose", "write_object_pose"])
        scene.reset.assert_called_once_with()
        sim.step.assert_called_once()
        self.assertEqual(scene.write_data_to_sim.call_count, 2)
        scene.update.assert_called_once_with(0.01)

        written_pose = target_object.write_root_pose_to_sim.call_args[0][0]
        expected_pose = torch.tensor([[0.58, -0.16, 1.08, 0.0, 0.0, 0.0, 1.0]])
        torch.testing.assert_close(written_pose, expected_pose)

    def test_reaching_target_reset_pose_rejects_position_drift(self) -> None:
        from franka_wrist_camera_scene.episode.reset import assert_reaching_target_reset_pose
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec

        target_object = MagicMock()
        target_object.data.root_pos_w = torch.tensor([[0.60, -0.16, 1.08]])
        target_object.data.root_vel_w = torch.zeros((1, 6))

        scene = MagicMock()
        scene.env_origins = torch.zeros((1, 3))
        scene.__getitem__.side_effect = {"target_cube": target_object}.__getitem__

        spec = ReachingTaskSpec(
            object_name="target_cube",
            object_pos_local=(0.58, -0.16, 1.08),
        )

        with self.assertRaisesRegex(RuntimeError, "not stable after reset"):
            assert_reaching_target_reset_pose(scene, spec)

    def test_reaching_target_reset_pose_rejects_velocity(self) -> None:
        from franka_wrist_camera_scene.episode.reset import assert_reaching_target_reset_pose
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec

        target_object = MagicMock()
        target_object.data.root_pos_w = torch.tensor([[0.58, -0.16, 1.08]])
        target_object.data.root_vel_w = torch.tensor([[0.02, 0.0, 0.0, 0.0, 0.0, 0.0]])

        scene = MagicMock()
        scene.env_origins = torch.zeros((1, 3))
        scene.__getitem__.side_effect = {"target_cube": target_object}.__getitem__

        spec = ReachingTaskSpec(
            object_name="target_cube",
            object_pos_local=(0.58, -0.16, 1.08),
        )

        with self.assertRaisesRegex(RuntimeError, "nonzero velocity"):
            assert_reaching_target_reset_pose(scene, spec)

    def test_vector_static_clutter_parks_inactive_base_slot_in_usd_and_world_pose(self) -> None:
        from franka_wrist_camera_scene.episode.reset import PARKED_ASSET_POS, _reset_vector_static_clutter
        from franka_wrist_camera_scene.scene.clutter import ClutterObjectSpec

        scene = MagicMock()
        scene.num_envs = 2
        scene.env_origins = torch.tensor([[0.0, 0.0, 0.0], [2.5, 0.0, 0.0]])

        base_bowl = FakeStaticExtra(num_envs=2)
        active_onion = FakeStaticExtra(num_envs=2)
        scene.__getitem__.side_effect = {
            "clutter_5": base_bowl,
            "clutter_5_onion_onion08": active_onion,
        }.__getitem__

        env0_bowl = ClutterObjectSpec(
            prim_name="clutter_5",
            context=MagicMock(),
            pos_local=(0.94, 0.35, 1.08),
            footprint_radius_m=0.05,
        )
        env1_onion = ClutterObjectSpec(
            prim_name="clutter_5_onion_onion08",
            context=MagicMock(),
            pos_local=(0.87, 0.34, 1.08),
            footprint_radius_m=0.04,
        )

        expected = _reset_vector_static_clutter(
            scene=scene,
            clutter_specs_by_env=((env0_bowl,), (env1_onion,)),
            all_clutter_names=("clutter_5", "clutter_5_onion_onion08"),
        )

        torch.testing.assert_close(
            base_bowl.local_translations,
            torch.tensor([[0.94, 0.35, 1.08], list(PARKED_ASSET_POS)]),
        )
        torch.testing.assert_close(
            base_bowl.world_positions,
            torch.tensor([[0.94, 0.35, 1.08], [102.5, 100.0, -10.0]]),
        )
        torch.testing.assert_close(base_bowl.local_translations, expected["clutter_5"])
        self.assertEqual(base_bowl.set_local_call_count, 1)
        self.assertEqual(base_bowl.set_world_call_count, 1)
