import sys
from unittest.mock import MagicMock
from unittest import TestCase
import torch
import random
from pathlib import Path


class TestReachingUpgrade(TestCase):
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

    def test_target_source_sampling(self) -> None:
        from franka_wrist_camera_scene.objects.selection import sample_catalog_object
        from franka_wrist_camera_scene.objects.catalog import load_object_catalog

        catalog = load_object_catalog("object_catalog.generated.yaml")
        
        # Ensure we can sample a pickable object
        cat_pick, var_pick = sample_catalog_object(
            catalog=catalog,
            category_id="sample",
            variant_id="sample",
            split="train",
            role="target",
            required_affordances=("pickable", "reachable"),
            required_grasp_strategy="center_top",
            rng=random.Random(42),
        )
        affordances_pick = set(cat_pick.affordances)
        if var_pick.affordances is not None:
            affordances_pick.update(var_pick.affordances)
        self.assertIn("pickable", affordances_pick)
        
        # Ensure we can sample a physical container/receptacle
        cat_rec, var_rec = sample_catalog_object(
            catalog=catalog,
            category_id="sample",
            variant_id="sample",
            split="train",
            role="target",
            required_affordances=("container", "physical_container"),
            required_grasp_strategy="unsupported",
            rng=random.Random(42),
        )
        affordances_rec = set(cat_rec.affordances)
        if var_rec.affordances is not None:
            affordances_rec.update(var_rec.affordances)
        self.assertIn("physical_container", affordances_rec)
        self.assertNotEqual(cat_rec.label.lower(), "cup")
        self.assertNotEqual(cat_rec.id.lower(), "cup")

    def test_cups_are_not_sampled_as_physical_receptacle_targets(self) -> None:
        from franka_wrist_camera_scene.objects.selection import variant_matches
        from franka_wrist_camera_scene.objects.catalog import load_object_catalog

        catalog = load_object_catalog("object_catalog.generated.yaml")
        for category in catalog.categories:
            for variant in category.variants:
                if variant_matches(
                    category=category,
                    variant=variant,
                    required_affordances=("container", "physical_container"),
                    required_grasp_strategy="unsupported",
                ):
                    self.assertNotEqual(category.label.lower(), "cup")
                    self.assertNotEqual(category.id.lower(), "cup")

    def test_clutter_exclusions(self) -> None:
        from franka_wrist_camera_scene.objects.selection import sample_catalog_object
        from franka_wrist_camera_scene.objects.catalog import load_object_catalog

        catalog = load_object_catalog("object_catalog.generated.yaml")
        
        # Sample target object context
        cat, var = sample_catalog_object(
            catalog=catalog,
            category_id="sample",
            variant_id="sample",
            split="train",
            role="target",
            required_affordances=("pickable", "reachable"),
            required_grasp_strategy="center_top",
            rng=random.Random(42),
        )
        
        # Verify exclusions at catalog category level
        for i in range(50):
            sampled_cat, sampled_var = sample_catalog_object(
                catalog=catalog,
                category_id="sample",
                variant_id="sample",
                split="train",
                role="target",
                required_affordances=("pickable", "reachable"),
                required_grasp_strategy="center_top",
                rng=random.Random(i),
                excluded_category_ids=(cat.id,),
                excluded_labels=(cat.label,),
            )
            self.assertNotEqual(sampled_cat.id, cat.id)
            self.assertNotEqual(sampled_cat.label, cat.label)

    def test_box_receptacle_assets_are_labeled_as_baskets(self) -> None:
        from franka_wrist_camera_scene.objects.catalog import load_object_catalog
        from franka_wrist_camera_scene.objects.selection import (
            matching_variants,
            sample_catalog_object,
            variant_visual_label,
        )
        from franka_wrist_camera_scene.scene.object_context import load_catalog_object_context

        context = load_catalog_object_context(
            catalog_config="object_catalog.generated.yaml",
            geometry_config="object_geometry.generated.yaml",
            category_id="box",
            variant_id="box04",
            split="train",
            role="target",
            required_affordances=("container", "physical_container"),
            required_grasp_strategy="unsupported",
        )
        self.assertEqual(context.label, "basket")

        catalog = load_object_catalog("object_catalog.generated.yaml")
        categories = tuple(
            category
            for category in catalog.categories
            if category.split == "train" and category.role == "target"
        )
        receptacle_labels = {
            variant_visual_label(category, variant)
            for category in categories
            for variant in matching_variants(
                category=category,
                required_affordances=("container", "physical_container"),
                required_grasp_strategy="unsupported",
            )
        }
        self.assertGreaterEqual(receptacle_labels, {"basket", "bowl", "plate", "tray"})
        self.assertNotIn("box", receptacle_labels)

        with self.assertRaisesRegex(ValueError, "excluded by visual label"):
            sample_catalog_object(
                catalog=catalog,
                category_id="box",
                variant_id="box04",
                split="train",
                role="target",
                required_affordances=("container", "physical_container"),
                required_grasp_strategy="unsupported",
                excluded_labels=("basket",),
            )

    def test_reaching_policy_behavior(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.policies.reaching_scripted import ReachingScriptedPolicy

        mock_robot = MagicMock()
        mock_robot.device = torch.device("cpu")
        mock_robot.find_bodies.return_value = [[0]]
        
        mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))
        mock_robot.data.body_pose_w[0, 0, :3] = torch.tensor([0.0, 0.0, 1.0])
        mock_robot.data.body_pose_w[0, 0, 3:7] = torch.tensor([0.0, 0.0, 0.0, 1.0])
        
        mock_scene = MagicMock()
        mock_scene.num_envs = 1
        
        mock_target = MagicMock()
        mock_target.data.root_pos_w = torch.tensor([[0.5, 0.2, 1.0]])
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_cube": mock_target,
        }.__getitem__
        
        spec = ReachingTaskSpec(
            object_name="target_cube",
            object_pos_local=(0.5, 0.2, 1.0),
            closed_finger_m=0.0,
            direct_reach_max_speed_m_s=0.16,
            success_threshold_m=0.01,
        )
        
        policy = ReachingScriptedPolicy(spec)
        policy.bind(mock_scene, mock_robot)
        policy.reset()
        
        # Policy FSM state must be move_to_target directly (no pregrasp)
        self.assertEqual(policy.state, "move_to_target")
        
        # Gripper commanded to closed_finger_m from first step
        cmd = policy.step(None, 0.0)
        self.assertEqual(cmd.finger_opening_m, 0.0)
        
        # Target quaternion is latched at reset to prevent wrist spin while reaching.
        self.assertTrue(torch.allclose(cmd.target_quat_w, torch.tensor([[0.0, 0.0, 0.0, 1.0]])))
        
        mock_target.data.root_pos_w = torch.tensor([[0.2, 0.5, 1.0]])
        policy.reset()
        cmd2 = policy.step(None, 0.0)
        self.assertTrue(torch.allclose(cmd2.target_quat_w, torch.tensor([[0.0, 0.0, 0.0, 1.0]])))

    def test_reaching_success_thresholds(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.episode.success import reaching_success

        mock_robot = MagicMock()
        mock_robot.find_bodies.return_value = [[0]]
        
        mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))
        mock_robot.data.body_pose_w[0, 0, :3] = torch.tensor([0.0, 0.0, 0.0])
        mock_robot.data.body_pose_w[0, 0, 3:7] = torch.tensor([0.0, 0.0, 0.0, 1.0])
        
        mock_target = MagicMock()
        mock_scene = MagicMock()
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_cube": mock_target,
        }.__getitem__
        
        spec = ReachingTaskSpec(
            object_name="target_cube",
            tcp_offset_local=(0.0, 0.0, 0.10),
            object_reach_offset_local=(0.0, 0.0, 0.0),
            success_threshold_m=0.01,
        )
        
        # Case 1: TCP is exactly 0.009 m from reach point -> Succeeds
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.109]])
        self.assertTrue(reaching_success(mock_scene, spec)[0].item())
        
        # Case 2: TCP is exactly 0.011 m from reach point -> Fails
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.111]])
        self.assertFalse(reaching_success(mock_scene, spec)[0].item())
        
        # Case 3: Target is close to origin (hand), but far from TCP (TCP is at 0.10)
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.009]])
        self.assertFalse(reaching_success(mock_scene, spec)[0].item())

    def test_metadata_manifest_fields(self) -> None:
        from franka_wrist_camera_scene.episode.schema import EpisodeMetadata
        from franka_wrist_camera_scene.episode.manifest import EpisodeManifestEntry
        
        meta = EpisodeMetadata(
            episode_id=0,
            task_name="reaching",
            instruction="reach the apple",
            success=True,
            num_steps=100,
            sim_dt=0.01,
            target_source_name="pickable_targets",
            object_affordances=["pickable", "reachable"],
        )
        self.assertEqual(meta.target_source_name, "pickable_targets")
        self.assertEqual(meta.object_affordances, ["pickable", "reachable"])
        
        entry = EpisodeManifestEntry(
            episode_id=0,
            episode_dir="000000",
            success=True,
            success_mode=None,
            num_steps=100,
            num_camera_frames=0,
            camera_width=None,
            camera_height=None,
            camera_fps=None,
            suite_name=None,
            suite_split=None,
            suite_difficulty=None,
            suite_tags=None,
            suite_description=None,
            object_pos_local=None,
            object_reach_offset_local=None,
            reach_success_threshold_m=None,
            max_success_target_displacement_m=None,
            place_pos_local=None,
            seed=None,
            object_xy_offset=None,
            place_xy_offset=None,
            object_category_id=None,
            object_variant_id=None,
            object_label=None,
            object_usd_path=None,
            object_grasp_strategy=None,
            target_source_name="pickable_targets",
            object_affordances=["pickable", "reachable"],
            object_yaw_relevant=None,
            object_planar_aspect_ratio=None,
            object_planar_minor_axis_local=None,
            object_planar_major_axis_local=None,
            grasp_closing_axis_xy=None,
            placement_target_category_id=None,
            placement_target_variant_id=None,
            placement_target_label=None,
            placement_target_usd_path=None,
            placement_target_grasp_strategy=None,
            placement_target_pos_local=None,
            placement_target_quat_wxyz=None,
            light_intensity=None,
            light_color=None,
            table_color=None,
            active_clutter_count=None,
            clutter_objects=None,
            trajectory_file="trajectory.npz",
            metadata_file="meta.json",
        )
        self.assertEqual(entry.target_source_name, "pickable_targets")
        self.assertEqual(entry.object_affordances, ["pickable", "reachable"])

    def test_reaching_success_with_latched_reach_pos(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.episode.success import reaching_success

        mock_robot = MagicMock()
        mock_robot.find_bodies.return_value = [[0]]

        mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))
        mock_robot.data.body_pose_w[0, 0, :3] = torch.tensor([0.0, 0.0, 0.0])
        mock_robot.data.body_pose_w[0, 0, 3:7] = torch.tensor([0.0, 0.0, 0.0, 1.0])

        mock_target = MagicMock()
        mock_scene = MagicMock()
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_cube": mock_target,
        }.__getitem__

        spec = ReachingTaskSpec(
            object_name="target_cube",
            tcp_offset_local=(0.0, 0.0, 0.10),
            object_reach_offset_local=(0.0, 0.0, 0.0),
            success_threshold_m=0.01,
        )

        # Target has moved far away (0.150 m) from its initial pos
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.150]])
        # But we compare against the latched reach position (0.105 m)
        target_reach_pos_w = torch.tensor([[0.0, 0.0, 0.105]])

        self.assertTrue(reaching_success(mock_scene, spec, target_reach_pos_w=target_reach_pos_w)[0].item())

    def test_hybrid_reaching_success(self) -> None:
        from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
        from franka_wrist_camera_scene.episode.success import reaching_success_metrics, reaching_success

        mock_robot = MagicMock()
        mock_robot.find_bodies.return_value = [[0]]
        mock_robot.data.body_pose_w = torch.zeros((1, 1, 7))
        mock_robot.data.body_pose_w[0, 0, :3] = torch.tensor([0.0, 0.0, 0.0])
        mock_robot.data.body_pose_w[0, 0, 3:7] = torch.tensor([0.0, 0.0, 0.0, 1.0])

        mock_target = MagicMock()
        mock_scene = MagicMock()
        mock_scene.__getitem__.side_effect = {
            "robot": mock_robot,
            "target_cube": mock_target,
        }.__getitem__

        spec = ReachingTaskSpec(
            object_name="target_cube",
            tcp_offset_local=(0.0, 0.0, 0.10),
            object_reach_offset_local=(0.0, 0.0, 0.0),
            success_threshold_m=0.01,
            max_success_target_displacement_m=0.02,
        )

        # 1. latched distance <= threshold => success
        # TCP is at (0, 0, 0.10)
        # Latched pos is (0, 0, 0.105) -> distance = 0.005 <= 0.01
        # Live pos (target) is far away (0, 0, 0.20)
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.20]])
        target_reach_pos_w = torch.tensor([[0.0, 0.0, 0.105]])
        metrics = reaching_success_metrics(mock_scene, spec, target_reach_pos_w)
        self.assertTrue(metrics.success[0].item())
        self.assertTrue(metrics.reached_latched_target[0].item())

        # 2. live distance <= threshold and target displacement <= max displacement => success
        # Latched pos is (0, 0, 0.115) -> distance = 0.015 > 0.01 (latched fails)
        # Live pos (target) is (0, 0, 0.108) -> distance = 0.008 <= 0.01 (live reaches)
        # Displacement is |0.115 - 0.108| = 0.007 <= 0.02 (displacement OK)
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.108]])
        target_reach_pos_w = torch.tensor([[0.0, 0.0, 0.115]])
        metrics = reaching_success_metrics(mock_scene, spec, target_reach_pos_w)
        self.assertTrue(metrics.success[0].item())
        self.assertFalse(metrics.reached_latched_target[0].item())
        self.assertTrue(metrics.reached_live_target[0].item())
        self.assertTrue(metrics.target_displacement_ok[0].item())

        # 3. live distance <= threshold but target displacement > max displacement => failure
        # Latched pos is (0, 0, 0.20) -> distance = 0.10 > 0.01 (latched fails)
        # Live pos (target) is (0, 0, 0.108) -> distance = 0.008 <= 0.01 (live reaches)
        # Displacement is |0.20 - 0.108| = 0.092 > 0.02 (displacement fails)
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.108]])
        target_reach_pos_w = torch.tensor([[0.0, 0.0, 0.20]])
        metrics = reaching_success_metrics(mock_scene, spec, target_reach_pos_w)
        self.assertFalse(metrics.success[0].item())
        self.assertFalse(metrics.reached_latched_target[0].item())
        self.assertTrue(metrics.reached_live_target[0].item())
        self.assertFalse(metrics.target_displacement_ok[0].item())

        # 4. latched distance > threshold and live distance > threshold => failure
        # Latched pos is (0, 0, 0.12) -> distance = 0.02 > 0.01
        # Live pos is (0, 0, 0.13) -> distance = 0.03 > 0.01
        # Displacement is 0.01 <= 0.02
        mock_target.data.root_pos_w = torch.tensor([[0.0, 0.0, 0.13]])
        target_reach_pos_w = torch.tensor([[0.0, 0.0, 0.12]])
        metrics = reaching_success_metrics(mock_scene, spec, target_reach_pos_w)
        self.assertFalse(metrics.success[0].item())

        # 5. episode-16 numeric regression:
        # latched distance = 0.0124606, live distance = 0.0089640, displacement = 0.008317, threshold = 0.01, max_disp = 0.02
        mock_robot.data.body_pose_w[0, 0, :3] = torch.tensor([0.0, 0.0, 0.0])
        spec_episode16 = ReachingTaskSpec(
            object_name="target_cube",
            tcp_offset_local=(0.0, 0.0, 0.0),
            object_reach_offset_local=(0.0, 0.0, 0.0),
            success_threshold_m=0.01,
            max_success_target_displacement_m=0.02,
        )
        mock_target.data.root_pos_w = torch.tensor([[0.0066789, 0.0059787, 0.0]])
        target_reach_pos_w = torch.tensor([[0.0124606, 0.0, 0.0]])

        metrics = reaching_success_metrics(mock_scene, spec_episode16, target_reach_pos_w)
        self.assertTrue(metrics.success[0].item())
        self.assertFalse(metrics.reached_latched_target[0].item())
        self.assertTrue(metrics.reached_live_target[0].item())
        self.assertTrue(metrics.target_displacement_ok[0].item())

        # Also test the reaching_success wrapper
        self.assertTrue(reaching_success(mock_scene, spec_episode16, target_reach_pos_w=target_reach_pos_w)[0].item())

    def test_single_env_reaching_inactive_assets_are_all_non_active_bank_assets(self) -> None:
        from franka_wrist_camera_scene.collection.reaching import (
            ReachingAssetBank,
            ReachingAssetNames,
            _inactive_reaching_asset_names,
        )
        asset_bank = ReachingAssetBank(
            target_names={("apple", "apple00"): "target_cube", ("peach", "peach01"): "target_peach_peach01"},
            clutter_names={
                (0, "lemon", "lemon01"): "clutter_0",
                (1, "plate", "plate01"): "clutter_1",
            },
            target_usd_paths={
                "target_cube": "...",
                "target_peach_peach01": "...",
            },
            clutter_usd_paths={
                "clutter_0": "...",
                "clutter_1": "...",
            },
        )
        active = ReachingAssetNames(
            object_name="target_peach_peach01",
            clutter_names=("clutter_1",),
        )

        inactive_objects, inactive_clutter = _inactive_reaching_asset_names(asset_bank, active)

        self.assertEqual(inactive_objects, ("target_cube",))
        self.assertEqual(inactive_clutter, ("clutter_0",))
