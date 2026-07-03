import sys
from unittest.mock import MagicMock
from unittest import TestCase
import torch
import numpy as np
from pathlib import Path


class TestReachingPolicy(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Define mock_quat_apply
        def mock_quat_apply(quat, vec):
            xyz = quat[:, :3]
            t = torch.cross(xyz, vec, dim=-1) * 2.0
            return vec + quat[:, 3:4] * t + torch.cross(xyz, t, dim=-1)

        modules = {
            "isaaclab": MagicMock(),
            "isaaclab.scene": MagicMock(),
            "isaaclab.assets": MagicMock(),
            "isaaclab.utils": MagicMock(),
            "isaaclab.utils.math": MagicMock(),
            "isaaclab.utils.configclass": MagicMock(),
            "isaaclab.sim": MagicMock(),
            "isaaclab.controllers": MagicMock(),
            "isaaclab.sensors": MagicMock(),
            "isaaclab.managers": MagicMock(),
            "pxr": MagicMock(),
            "isaaclab_assets": MagicMock(),
        }
        modules["isaaclab.utils.math"].quat_apply = mock_quat_apply

        from unittest.mock import patch
        cls.sys_modules_patcher = patch.dict(sys.modules, modules)
        cls.sys_modules_patcher.start()

        import franka_wrist_camera_scene.episode.success
        cls.original_quat_apply = getattr(franka_wrist_camera_scene.episode.success, "quat_apply", None)
        franka_wrist_camera_scene.episode.success.quat_apply = mock_quat_apply

    @classmethod
    def tearDownClass(cls) -> None:
        import franka_wrist_camera_scene.episode.success
        if hasattr(cls, "original_quat_apply") and cls.original_quat_apply is not None:
            franka_wrist_camera_scene.episode.success.quat_apply = cls.original_quat_apply
        cls.sys_modules_patcher.stop()

    def setUp(self) -> None:
        self.mock_robot = MagicMock()
        self.mock_robot.device = torch.device("cpu")
        self.mock_robot.find_bodies.return_value = [[0]]
        
        self.mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))
        self.mock_robot.data.body_pose_w[0, 0, :3] = torch.tensor([0.1, 0.2, 0.3])
        self.mock_robot.data.body_pose_w[0, 0, 3:7] = torch.tensor([0.0, 0.0, 0.0, 1.0])
        
        self.mock_scene = MagicMock()
        self.mock_scene.num_envs = 1
        
        self.mock_target = MagicMock()
        self.mock_target.data.root_pos_w = torch.tensor([[0.5, 0.2, 0.1]])
        
        self.mock_scene.__getitem__.side_effect = {
            "robot": self.mock_robot,
            "target_cube": self.mock_target,
        }.__getitem__

    def test_reaching_command_latches_orientation_and_closed_gripper(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.policies.reaching_scripted import ReachingScriptedPolicy

        spec = ReachingTaskSpec()
        policy = ReachingScriptedPolicy(spec)
        policy.bind(self.mock_scene, self.mock_robot)
        policy.reset()

        cmd = policy.step(None, 0.0)

        self.assertTrue(torch.allclose(cmd.target_quat_w, torch.tensor([[0.0, 0.0, 0.0, 1.0]])))
        self.assertEqual(cmd.finger_opening_m, spec.closed_finger_m)
        self.assertEqual(cmd.finger_opening_m, 0.0)

    def test_reset_latches_reach_point_as_detached_clone(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.policies.reaching_scripted import ReachingScriptedPolicy

        spec = ReachingTaskSpec(
            object_name="target_cube",
            object_reach_offset_local=(0.0, 0.0, 0.05),
        )
        policy = ReachingScriptedPolicy(spec)
        policy.bind(self.mock_scene, self.mock_robot)
        policy.reset()

        latched = policy.latched_reach_pos_w
        self.mock_target.data.root_pos_w[0, 2] += 1.0

        self.assertFalse(latched.requires_grad)
        self.assertTrue(torch.allclose(latched, torch.tensor([[0.5, 0.2, 0.15]])))
        self.assertTrue(torch.allclose(policy.latched_reach_pos_w, torch.tensor([[0.5, 0.2, 0.15]])))

    def test_tcp_desired_trajectory_reaches_target_point(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.policies.reaching_scripted import ReachingScriptedPolicy
        from franka_wrist_camera_scene.policies.reaching_targets import quat_apply_xyzw

        spec = ReachingTaskSpec(
            object_name="target_cube",
            object_pos_local=(0.5, 0.2, 0.1),
            tcp_offset_local=(0.02, -0.01, 0.15),
            object_reach_offset_local=(0.0, 0.0, 0.05),
            direct_reach_max_speed_m_s=0.16,
            reach_dwell_s=1.0,
        )
        
        orientations = [
            torch.tensor([0.0, 0.0, 0.0, 1.0]),
            torch.tensor([0.0, 0.7071, 0.0, 0.7071]),
        ]
        
        for ee_quat in orientations:
            self.mock_robot.data.body_pose_w[0, 0, 3:7] = ee_quat.clone()
            policy = ReachingScriptedPolicy(spec)
            policy.bind(self.mock_scene, self.mock_robot)
            policy.reset()
            
            # Step policy past time to complete minimum jerk motion
            policy.step(None, 0.0)
            cmd = policy.step(None, 10.0)
            
            # target_hand_pos_w + quat_apply(current_ee_quat_w, tcp_offset_local) == desired_tcp_pos_w
            tcp_offset_local = torch.tensor(spec.tcp_offset_local).view(1, 3)
            tcp_offset_w = quat_apply_xyzw(ee_quat.view(1, 4), tcp_offset_local)
            
            reconstructed_tcp = cmd.target_pos_w + tcp_offset_w
            
            object_root_pos = self.mock_target.data.root_pos_w
            object_reach_offset_local = torch.tensor(spec.object_reach_offset_local).view(1, 3)
            expected_reach_point = object_root_pos + object_reach_offset_local
            
            self.assertTrue(torch.allclose(reconstructed_tcp, expected_reach_point, atol=1e-4))

    def test_position_only_ik_mode_limits_api(self) -> None:
        from franka_wrist_camera_scene.control.ik import CartesianIKController
        ik_pos = CartesianIKController(command_type="position")
        with self.assertRaises(RuntimeError):
            ik_pos.set_target_pose(torch.zeros(1, 3), torch.zeros(1, 4))
            
        ik_pose = CartesianIKController(command_type="pose")
        with self.assertRaises(RuntimeError):
            ik_pose.set_target_position(torch.zeros(1, 3))

    def test_position_ik_posture_bias_projects_into_nullspace(self) -> None:
        from franka_wrist_camera_scene.control.ik import CartesianIKController, PostureBiasCfg
        ik = CartesianIKController(
            command_type="position",
            posture_bias=PostureBiasCfg(joint_pos={"panda_joint4": 1.0}, gain=0.5),
        )
        ik._posture_target_joint_pos = torch.ones(1, 7)
        ik._posture_joint_mask = torch.ones(1, 7, dtype=torch.bool)

        joint_pos = torch.zeros(1, 7)
        joint_pos_des = torch.zeros(1, 7)
        jacobian = torch.zeros(1, 6, 7)
        jacobian[0, 0, 0] = 1.0
        jacobian[0, 1, 1] = 1.0
        jacobian[0, 2, 2] = 1.0

        biased_joint_pos = ik._apply_posture_bias(joint_pos_des, joint_pos, jacobian)
        task_space_motion = jacobian[:, :3, :] @ (biased_joint_pos - joint_pos_des).unsqueeze(-1)

        self.assertLess(float(torch.linalg.norm(task_space_motion).item()), 1e-3)
        self.assertGreater(float(biased_joint_pos[0, 3].item()), 0.49)

    def test_pose_ik_posture_bias_projects_into_full_pose_nullspace(self) -> None:
        from franka_wrist_camera_scene.control.ik import CartesianIKController, PostureBiasCfg
        ik = CartesianIKController(
            command_type="pose",
            posture_bias=PostureBiasCfg(joint_pos={"panda_joint7": 1.0}, gain=0.5),
        )
        ik._posture_target_joint_pos = torch.ones(1, 7)
        ik._posture_joint_mask = torch.ones(1, 7, dtype=torch.bool)

        joint_pos = torch.zeros(1, 7)
        joint_pos_des = torch.zeros(1, 7)
        jacobian = torch.zeros(1, 6, 7)
        for axis in range(6):
            jacobian[0, axis, axis] = 1.0

        biased_joint_pos = ik._apply_posture_bias(joint_pos_des, joint_pos, jacobian)
        task_space_motion = jacobian @ (biased_joint_pos - joint_pos_des).unsqueeze(-1)

        self.assertLess(float(torch.linalg.norm(task_space_motion).item()), 1e-3)
        self.assertGreater(float(biased_joint_pos[0, 6].item()), 0.49)

    def test_position_ik_rejects_negative_posture_gain(self) -> None:
        from franka_wrist_camera_scene.control.ik import PostureBiasCfg
        with self.assertRaises(ValueError):
            PostureBiasCfg(joint_pos={"panda_joint1": 0.0}, gain=-0.1)

    def test_recorder_handles_null_target_quat(self) -> None:
        from franka_wrist_camera_scene.episode.recorder import EpisodeRecorder
        from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand

        recorder = EpisodeRecorder(
            output_dir=Path("/tmp"),
            episode_id=0,
            task_name="reaching",
            instruction="reach the object",
            sim_dt=0.01,
            ee_body_id=0,
            object_name="target_cube",
        )
        
        cmd = PolicyCommand(
            target_pos_w=torch.zeros(1, 3),
            target_quat_w=None,
            finger_opening_m=0.0,
        )
        
        # Mock recorder.record_step requirements
        mock_robot = MagicMock()
        mock_robot.data.joint_pos = torch.zeros(1, 7)
        mock_robot.data.joint_vel = torch.zeros(1, 7)
        mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))
        
        mock_obj = MagicMock()
        mock_obj.data.root_pos_w = torch.zeros(1, 3)
        
        mock_scene = MagicMock()
        mock_scene.num_envs = 1
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_cube": mock_obj,
        }.__getitem__
        
        recorder.record_step(mock_scene, cmd, 0, 0.0)
        
        logged_quat = recorder.action_target_quat_w[-1].cpu().numpy()
        self.assertTrue(np.isnan(logged_quat).all())
        self.assertEqual(logged_quat.shape, (1, 4))

    def test_recorder_state_stride_buffers_without_hot_loop_numpy(self) -> None:
        from tempfile import TemporaryDirectory

        from franka_wrist_camera_scene.episode.recorder import EpisodeRecorder
        from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand

        with TemporaryDirectory() as tmpdir:
            recorder = EpisodeRecorder(
                output_dir=Path(tmpdir),
                episode_id=3,
                task_name="reaching",
                instruction="reach the object",
                sim_dt=0.01,
                ee_body_id=0,
                object_name="target_cube",
                max_steps=6,
                state_record_stride=2,
            )

            cmd = PolicyCommand(
                target_pos_w=torch.ones(1, 3),
                target_quat_w=None,
                finger_opening_m=0.0,
            )

            mock_robot = MagicMock()
            mock_robot.data.joint_pos = torch.zeros(1, 7)
            mock_robot.data.joint_vel = torch.zeros(1, 7)
            mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))

            mock_obj = MagicMock()
            mock_obj.data.root_pos_w = torch.zeros(1, 3)

            mock_scene = MagicMock()
            mock_scene.num_envs = 1
            mock_scene.__getitem__.side_effect = {
                "robot": mock_robot,
                "target_cube": mock_obj,
            }.__getitem__

            for step in range(6):
                recorder.record_step(mock_scene, cmd, step, float(step) * 0.01)

            self.assertEqual(recorder.recorded_state_count, 3)
            self.assertEqual(len(recorder.joint_pos), 0)

            saved_dir = recorder.save(success=True)
            arrays = np.load(saved_dir / "trajectory.npz")
            self.assertEqual(arrays["joint_pos"].shape, (3, 1, 7))
            self.assertEqual(arrays["state_step_indices"].tolist(), [0, 2, 4])

    def test_recorder_camera_save_writes_agent_video_and_training_rgb(self) -> None:
        from tempfile import TemporaryDirectory
        from unittest.mock import patch

        from franka_wrist_camera_scene.episode.recorder import EpisodeRecorder, wait_for_pending_video_writes
        from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand

        with TemporaryDirectory() as tmpdir:
            recorder = EpisodeRecorder(
                output_dir=Path(tmpdir),
                episode_id=4,
                task_name="reaching",
                instruction="reach the object",
                sim_dt=0.01,
                ee_body_id=0,
                object_name="target_cube",
                max_steps=2,
                record_cameras=True,
                record_depth=True,
            )

            cmd = PolicyCommand(
                target_pos_w=torch.ones(1, 3),
                target_quat_w=None,
                finger_opening_m=0.0,
            )

            mock_robot = MagicMock()
            mock_robot.data.joint_pos = torch.zeros(1, 7)
            mock_robot.data.joint_vel = torch.zeros(1, 7)
            mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))

            mock_obj = MagicMock()
            mock_obj.data.root_pos_w = torch.zeros(1, 3)

            mock_scene = MagicMock()
            mock_scene.num_envs = 1
            mock_scene.__getitem__.side_effect = {
                "robot": mock_robot,
                "target_cube": mock_obj,
            }.__getitem__
            recorder.record_step(mock_scene, cmd, 0, 0.0)

            rgb = np.full((4, 4, 3), 80, dtype=np.uint8)
            recorder.camera_step_indices.append(0)
            recorder.camera_timestamps_s.append(0.0)
            recorder.agent_rgb.append(rgb)
            recorder.wrist_rgb.append(rgb)
            recorder.agent_depth.append(np.ones((4, 4), dtype=np.float32))
            recorder.wrist_depth.append(np.ones((4, 4), dtype=np.float32) * 2.0)

            with patch("franka_wrist_camera_scene.episode.recorder._write_rgb_video") as write_video:
                saved_dir = recorder.save(success=True)
                wait_for_pending_video_writes()

            self.assertEqual(write_video.call_count, 1)
            self.assertEqual(write_video.call_args.args[0].name, "agent_camera.mp4")
            trajectory = np.load(saved_dir / "trajectory.npz")
            self.assertNotIn("agent_rgb", trajectory.files)
            self.assertNotIn("wrist_rgb", trajectory.files)
            self.assertNotIn("agent_depth", trajectory.files)
            self.assertNotIn("wrist_depth", trajectory.files)
            rgb_arrays = np.load(saved_dir / "rgb.npz")
            self.assertEqual(rgb_arrays["agent_rgb"].shape, (1, 4, 4, 3))
            self.assertEqual(rgb_arrays["wrist_rgb"].shape, (1, 4, 4, 3))
            depth = np.load(saved_dir / "depth.npz")
            self.assertEqual(depth["agent_depth"].shape, (1, 4, 4))
            self.assertEqual(depth["wrist_depth"].shape, (1, 4, 4))

    def test_vector_reaching_policy_latches_per_env_targets(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.policies.reaching_vector import VectorReachingScriptedPolicy

        mock_robot = MagicMock()
        mock_robot.device = torch.device("cpu")
        mock_robot.find_bodies.return_value = [[0]]
        mock_robot.data.body_pose_w = torch.zeros((2, 1, 7))
        mock_robot.data.body_pose_w[:, 0, :3] = torch.tensor([[0.0, 0.0, 1.0], [0.1, 0.0, 1.0]])
        mock_robot.data.body_pose_w[:, 0, 3:7] = torch.tensor([[0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0]])

        target_a = MagicMock()
        target_a.data.root_pos_w = torch.tensor([[0.5, 0.1, 1.0], [100.0, 100.0, -10.0]])
        target_b = MagicMock()
        target_b.data.root_pos_w = torch.tensor([[100.0, 100.0, -10.0], [0.6, -0.1, 1.1]])

        mock_scene = MagicMock()
        mock_scene.num_envs = 2
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_a": target_a,
            "target_b": target_b,
        }.__getitem__

        specs = (
            ReachingTaskSpec(
                object_name="target_a",
                object_reach_offset_local=(0.0, 0.0, 0.05),
                direct_reach_max_speed_m_s=0.2,
            ),
            ReachingTaskSpec(
                object_name="target_b",
                object_reach_offset_local=(0.0, 0.0, 0.02),
                direct_reach_max_speed_m_s=0.2,
            ),
        )
        policy = VectorReachingScriptedPolicy(specs=specs, active_env_count=2)
        policy.bind(mock_scene, mock_robot)
        policy.reset()

        expected = torch.tensor([[0.5, 0.1, 1.05], [0.6, -0.1, 1.12]])
        self.assertTrue(torch.allclose(policy.latched_reach_pos_w, expected))

        cmd = policy.step(None, 0.0)
        self.assertTrue(torch.allclose(cmd.target_quat_w, torch.tensor([[0.0, 0.0, 0.0, 1.0]])))
        self.assertEqual(cmd.target_pos_w.shape, (2, 3))
        self.assertEqual(cmd.done.shape, (2,))

    def test_vector_reaching_policy_returns_done_mask_for_active_envs_only(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.policies.reaching_vector import VectorReachingScriptedPolicy

        mock_robot = MagicMock()
        mock_robot.device = torch.device("cpu")
        mock_robot.find_bodies.return_value = [[0]]
        mock_robot.data.body_pose_w = torch.zeros((2, 1, 7))
        mock_robot.data.body_pose_w[:, 0, :3] = torch.tensor([[0.0, 0.0, 1.0], [0.1, 0.0, 1.0]])
        mock_robot.data.body_pose_w[:, 0, 3:7] = torch.tensor([[0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0]])

        target_a = MagicMock()
        target_a.data.root_pos_w = torch.tensor([[0.5, 0.1, 1.0], [100.0, 100.0, -10.0]])
        target_b = MagicMock()
        target_b.data.root_pos_w = torch.tensor([[100.0, 100.0, -10.0], [0.6, -0.1, 1.1]])

        mock_scene = MagicMock()
        mock_scene.num_envs = 2
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_a": target_a,
            "target_b": target_b,
        }.__getitem__

        specs = (
            ReachingTaskSpec(object_name="target_a", direct_reach_max_speed_m_s=0.2),
            ReachingTaskSpec(object_name="target_b", direct_reach_max_speed_m_s=0.2),
        )
        policy = VectorReachingScriptedPolicy(specs=specs, active_env_count=1)
        policy.bind(mock_scene, mock_robot)
        policy.reset()

        cmd = policy.step(None, 0.0)

        self.assertEqual(cmd.target_pos_w.shape, (2, 3))
        self.assertEqual(cmd.done.shape, (1,))

    def test_vector_reaching_recorder_factory_sets_max_steps(self) -> None:
        from franka_wrist_camera_scene.collection.reaching import (
            ReachingEpisodePlan,
            ReachingSceneAssets,
            _make_reaching_recorder,
        )
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.tasks.sampling import ReachingSample

        context = MagicMock()
        context.category_id = "apple"
        context.variant_id = "apple00"
        context.label = "apple"
        context.usd_path = Path.cwd() / "objects/apple/apple00.usd"
        context.grasp_strategy = "center_top"
        context.affordances = ("pickable", "reachable")
        context.geometry.yaw_relevant = False
        context.geometry.planar_aspect_ratio = 1.0
        context.geometry.planar_minor_axis_local = (1.0, 0.0)
        context.geometry.planar_major_axis_local = (0.0, 1.0)

        plan = ReachingEpisodePlan(
            sample=ReachingSample(
                object_xy_offset=(0.0, 0.0),
                light_intensity=800.0,
                light_color=(1.0, 1.0, 1.0),
            ),
            spec=ReachingTaskSpec(object_name="target_apple"),
            clutter_specs=(),
            clutter_metadata=[],
        )
        scene_assets = ReachingSceneAssets(
            object_context=context,
            clutter_contexts=(),
            target_source_name="pickable_targets",
        )

        recorder = _make_reaching_recorder(
            output_dir=Path("/tmp/reaching-recorder-test"),
            episode_id=7,
            plan=plan,
            scene_assets=scene_assets,
            sim_dt=1.0 / 120.0,
            ee_body_id=0,
            max_steps=123,
            record_cameras=True,
            record_depth=False,
            camera_width=64,
            camera_height=48,
            state_record_stride=2,
            camera_fps=20,
            suite=MagicMock(),
            seed=42,
            env_index=1,
        )

        self.assertEqual(recorder.max_steps, 123)
        self.assertEqual(recorder.env_index, 1)
