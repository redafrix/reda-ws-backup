import sys
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import MagicMock
import yaml


class TestPickPlaceAssetBank(TestCase):
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

        class DummyMeta(type):
            def __getattr__(cls, name):
                return cls

        class DummyCfg(metaclass=DummyMeta):
            def __init__(self, *args, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
            def __getattr__(self, name):
                val = DummyCfg()
                setattr(self, name, val)
                return val

        sys.modules["isaaclab.scene"].InteractiveSceneCfg = DummyCfg
        sys.modules["isaaclab.sensors"].CameraCfg = DummyCfg
        sys.modules["isaaclab.assets"].ArticulationCfg = DummyCfg
        sys.modules["isaaclab.assets"].AssetBaseCfg = DummyCfg
        sys.modules["isaaclab.assets"].RigidObjectCfg = DummyCfg

        def mock_configclass(c):
            return c

        sys.modules["isaaclab.utils.configclass"].configclass = mock_configclass
        import franka_wrist_camera_scene.scene.tabletop
        franka_wrist_camera_scene.scene.tabletop.configclass = mock_configclass

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

    def test_tabletop_scene_preserves_camera_visual_context(self) -> None:
        from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg
        scene_cfg = TabletopFrankaSceneCfg(num_envs=1, env_spacing=2.5)

        self.assertNotIn("warehouse", scene_cfg.__dict__)
        self.assertEqual(scene_cfg.agent_camera.offset.pos, (1.4186131747, 0.0, 1.7603500240))
        self.assertEqual(scene_cfg.agent_camera.offset.rot, (-0.33316794, 0.0, 0.94286750, 0.0))
        self.assertEqual(scene_cfg.wrist_camera.offset.pos, (-0.042, 0.0, 0.020))
        self.assertEqual(scene_cfg.wrist_camera.offset.rot, (-0.0493, 0.0493, -0.7054, 0.7054))
        self.assertEqual(scene_cfg.robot.init_state.joint_pos["panda_joint1"], 0.0)
        self.assertEqual(scene_cfg.robot.init_state.joint_pos["panda_joint6"], 2.35619)
        self.assertEqual(scene_cfg.robot.init_state.joint_pos["panda_joint7"], -2.395)

    def test_reaching_scene_uses_centered_wrist_reset(self) -> None:
        from franka_wrist_camera_scene.scene.tabletop import make_reaching_tabletop_scene_cfg

        context = SimpleNamespace(usd_path="/tmp/object.usd")
        clutter = (SimpleNamespace(context=context, pos_local=(0.0, 0.0, 0.0)),)
        scene_cfg = make_reaching_tabletop_scene_cfg(
            object_context=context,
            clutter_specs=clutter,
            num_envs=1,
            env_spacing=2.5,
        )

        self.assertEqual(scene_cfg.robot.init_state.joint_pos["panda_joint6"], 2.35619)
        self.assertEqual(scene_cfg.robot.init_state.joint_pos["panda_joint7"], -2.2751)

    def test_collection_camera_resolution_applies_to_both_views(self) -> None:
        from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg
        from franka_wrist_camera_scene.collection.pick_place import _apply_camera_resolution

        scene_cfg = TabletopFrankaSceneCfg(num_envs=1, env_spacing=2.5)

        _apply_camera_resolution(scene_cfg, width=400, height=400, record_depth=False, camera_fps=20)

        self.assertEqual(scene_cfg.agent_camera.width, 400)
        self.assertEqual(scene_cfg.agent_camera.height, 400)
        self.assertEqual(scene_cfg.wrist_camera.width, 400)
        self.assertEqual(scene_cfg.wrist_camera.height, 400)
        self.assertEqual(scene_cfg.agent_camera.data_types, ["rgb"])
        self.assertEqual(scene_cfg.wrist_camera.data_types, ["rgb"])
        self.assertAlmostEqual(scene_cfg.agent_camera.update_period, 1.0 / 20.0)
        self.assertAlmostEqual(scene_cfg.wrist_camera.update_period, 1.0 / 20.0)

    def test_basket_prompt_uses_basket_label(self) -> None:
        from franka_wrist_camera_scene.tasks.pick_place import instruction_for_object_and_receptacle

        self.assertEqual(
            instruction_for_object_and_receptacle("apple", "basket"),
            "pick up the apple and place it in the basket",
        )

    def test_collection_camera_config_keeps_depth_only_when_requested(self) -> None:
        from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg
        from franka_wrist_camera_scene.scene.tabletop import configure_scene_cameras

        scene_cfg = TabletopFrankaSceneCfg(num_envs=1, env_spacing=2.5)
        configure_scene_cameras(
            scene_cfg,
            width=320,
            height=240,
            record_depth=True,
            camera_fps=10,
        )

        self.assertEqual(scene_cfg.agent_camera.data_types, ["rgb", "distance_to_image_plane"])
        self.assertEqual(scene_cfg.wrist_camera.data_types, ["rgb", "distance_to_image_plane"])
        self.assertAlmostEqual(scene_cfg.agent_camera.update_period, 0.1)
        self.assertAlmostEqual(scene_cfg.wrist_camera.update_period, 0.1)

    def test_vector_pick_place_policy_batches_env_commands(self) -> None:
        import torch

        def mock_quat_apply(quat, vec):
            xyz = quat[:, :3]
            t = torch.cross(xyz, vec, dim=-1) * 2.0
            return vec + quat[:, 3:4] * t + torch.cross(xyz, t, dim=-1)

        sys.modules["isaaclab.utils.math"].quat_apply = mock_quat_apply

        import franka_wrist_camera_scene.policies.pick_place_scripted as pick_place_scripted
        pick_place_scripted.quat_apply = mock_quat_apply
        from franka_wrist_camera_scene.policies.pick_place_vector import VectorPickPlaceScriptedPolicy
        from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec

        robot = MagicMock()
        robot.device = torch.device("cpu")
        robot.find_bodies.return_value = [[0]]
        robot.data.body_pose_w = torch.zeros((2, 1, 7))
        robot.data.body_pose_w[:, 0, 3:7] = torch.tensor([[1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0]])

        object_a = MagicMock()
        object_a.data.root_pos_w = torch.tensor([[0.50, 0.05, 1.00], [100.0, 100.0, -10.0]])
        object_b = MagicMock()
        object_b.data.root_pos_w = torch.tensor([[100.0, 100.0, -10.0], [0.55, -0.05, 1.00]])
        receptacle_a = MagicMock()
        receptacle_a.data.root_pos_w = torch.tensor([[0.60, 0.20, 1.00], [100.0, 100.0, -10.0]])
        receptacle_b = MagicMock()
        receptacle_b.data.root_pos_w = torch.tensor([[100.0, 100.0, -10.0], [0.65, -0.20, 1.00]])

        scene = MagicMock()
        scene.num_envs = 2
        scene.env_origins = torch.zeros((2, 3))
        scene.__getitem__.side_effect = {
            "robot": robot,
            "object_a": object_a,
            "object_b": object_b,
            "receptacle_a": receptacle_a,
            "receptacle_b": receptacle_b,
        }.__getitem__

        common_kwargs = dict(
            object_local_bbox_min=(-0.02, -0.02, -0.02),
            object_local_bbox_max=(0.02, 0.02, 0.04),
            placement_target_local_bbox_min=(-0.10, -0.10, -0.02),
            placement_target_local_bbox_max=(0.10, 0.10, 0.04),
            free_space_max_speed_m_s=0.5,
            approach_max_speed_m_s=0.5,
        )
        specs = (
            PickPlaceTaskSpec(
                object_name="object_a",
                placement_target_name="receptacle_a",
                placement_target_pos_local=(0.60, 0.20, 1.00),
                **common_kwargs,
            ),
            PickPlaceTaskSpec(
                object_name="object_b",
                placement_target_name="receptacle_b",
                placement_target_pos_local=(0.65, -0.20, 1.00),
                **common_kwargs,
            ),
        )

        policy = VectorPickPlaceScriptedPolicy(specs=specs, active_env_count=2)
        policy.bind(scene, robot)
        policy.reset()
        cmd = policy.step(None, 0.0)

        self.assertEqual(cmd.target_pos_w.shape, (2, 3))
        self.assertEqual(cmd.target_quat_w.shape, (2, 4))
        self.assertEqual(cmd.finger_opening_m.shape, (2, 1))
        self.assertEqual(cmd.done.shape, (2,))

    def test_pick_place_clutter_excludes_named_object_and_receptacle_labels(self) -> None:
        import franka_wrist_camera_scene.collection.pick_place as pick_place_collection

        object_geometry = SimpleNamespace(
            planar_extent_minor=0.04,
            local_bbox_min=(-0.02, -0.02, -0.02),
            local_bbox_max=(0.02, 0.02, 0.04),
        )
        receptacle_geometry = SimpleNamespace(
            planar_extent_minor=0.20,
            local_bbox_min=(-0.10, -0.10, -0.02),
            local_bbox_max=(0.10, 0.10, 0.04),
        )
        target_context = SimpleNamespace(
            category_id="apple",
            variant_id="apple00",
            label="apple",
            geometry=object_geometry,
        )
        receptacle_context = SimpleNamespace(
            category_id="bowl",
            variant_id="bowl00",
            label="bowl",
            geometry=receptacle_geometry,
        )
        clutter_context = SimpleNamespace(
            category_id="tray",
            variant_id="tray00",
            label="tray",
            geometry=receptacle_geometry,
        )
        captured: dict[str, tuple[str, ...]] = {}

        def fake_load_collection_object_context(*_args, **_kwargs):
            if not hasattr(fake_load_collection_object_context, "calls"):
                fake_load_collection_object_context.calls = 0
            fake_load_collection_object_context.calls += 1
            return target_context if fake_load_collection_object_context.calls == 1 else receptacle_context

        def fake_sample_clutter_contexts_from_sources(*, excluded_category_ids=(), excluded_labels=(), excluded_keys=(), **_kwargs):
            captured["category_ids"] = tuple(excluded_category_ids)
            captured["labels"] = tuple(excluded_labels)
            captured["keys"] = tuple(excluded_keys)
            return (("pickable_distractors", clutter_context),)

        collection_cfg = {
            "object_receptacle_compatibility": {
                "max_height_to_receptacle_width": 1.1,
                "max_sampling_attempts": 1,
            },
            "clutter": {"count": 1},
        }
        target_cfg = {"max_planar_minor_extent_m": 0.075}

        original_loader = pick_place_collection._load_collection_object_context
        original_sampler = pick_place_collection.sample_clutter_contexts_from_sources
        pick_place_collection._load_collection_object_context = fake_load_collection_object_context
        pick_place_collection.sample_clutter_contexts_from_sources = fake_sample_clutter_contexts_from_sources
        try:
            pick_place_collection._sample_scene_assets(
                collection_cfg=collection_cfg,
                target_object_cfg=target_cfg,
                placement_target_cfg={},
                seed=123,
                episode_id=0,
            )
        finally:
            pick_place_collection._load_collection_object_context = original_loader
            pick_place_collection.sample_clutter_contexts_from_sources = original_sampler

        self.assertEqual(set(captured["category_ids"]), {"apple", "bowl"})
        self.assertEqual(set(captured["labels"]), {"apple", "bowl"})
        self.assertEqual(set(captured["keys"]), {("apple", "apple00"), ("bowl", "bowl00")})

    def test_pick_place_resamples_visual_duplicate_object_and_receptacle(self) -> None:
        import franka_wrist_camera_scene.collection.pick_place as pick_place_collection

        object_geometry = SimpleNamespace(
            planar_extent_minor=0.04,
            local_bbox_min=(-0.02, -0.02, -0.02),
            local_bbox_max=(0.02, 0.02, 0.04),
        )
        receptacle_geometry = SimpleNamespace(
            planar_extent_minor=0.20,
            local_bbox_min=(-0.10, -0.10, -0.02),
            local_bbox_max=(0.10, 0.10, 0.04),
        )
        duplicate_object = SimpleNamespace(
            category_id="bowl",
            variant_id="bowl_pickable",
            label="bowl",
            geometry=object_geometry,
        )
        duplicate_receptacle = SimpleNamespace(
            category_id="bowl",
            variant_id="bowl_receptacle",
            label="bowl",
            geometry=receptacle_geometry,
        )
        final_object = SimpleNamespace(
            category_id="apple",
            variant_id="apple00",
            label="apple",
            geometry=object_geometry,
        )
        final_receptacle = SimpleNamespace(
            category_id="plate",
            variant_id="plate00",
            label="plate",
            geometry=receptacle_geometry,
        )
        clutter_context = SimpleNamespace(
            category_id="tray",
            variant_id="tray00",
            label="tray",
            geometry=receptacle_geometry,
        )
        contexts = [duplicate_object, duplicate_receptacle, final_object, final_receptacle]

        def fake_load_collection_object_context(*_args, **_kwargs):
            return contexts.pop(0)

        def fake_sample_clutter_contexts_from_sources(**_kwargs):
            return (("pickable_distractors", clutter_context),)

        collection_cfg = {
            "object_receptacle_compatibility": {
                "max_height_to_receptacle_width": 1.1,
                "max_sampling_attempts": 2,
            },
            "clutter": {"count": 1},
        }
        target_cfg = {"max_planar_minor_extent_m": 0.075}

        original_loader = pick_place_collection._load_collection_object_context
        original_sampler = pick_place_collection.sample_clutter_contexts_from_sources
        pick_place_collection._load_collection_object_context = fake_load_collection_object_context
        pick_place_collection.sample_clutter_contexts_from_sources = fake_sample_clutter_contexts_from_sources
        try:
            scene_assets = pick_place_collection._sample_scene_assets(
                collection_cfg=collection_cfg,
                target_object_cfg=target_cfg,
                placement_target_cfg={},
                seed=123,
                episode_id=0,
            )
        finally:
            pick_place_collection._load_collection_object_context = original_loader
            pick_place_collection.sample_clutter_contexts_from_sources = original_sampler

        self.assertEqual(scene_assets.object_context.label, "apple")
        self.assertEqual(scene_assets.placement_context.label, "plate")

    def test_asset_bank_contains_sampled_episode_targets(self) -> None:
        from franka_wrist_camera_scene.collection.pick_place import _sample_all_scene_assets, _build_asset_bank
        config_path = Path("configs/collection.yaml")
        collection_cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        episode_ids = range(
            int(collection_cfg["start_episode_id"]),
            int(collection_cfg["start_episode_id"]) + int(collection_cfg["num_episodes"]),
        )

        scene_assets_by_episode = _sample_all_scene_assets(
            collection_cfg=collection_cfg,
            target_object_cfg=collection_cfg["target_object"],
            placement_target_cfg=collection_cfg["placement_target"],
            seed=int(collection_cfg["seed"]),
            episode_ids=episode_ids,
        )
        asset_bank = _build_asset_bank(scene_assets_by_episode)

        sampled_target_ids = {
            (assets.object_context.category_id, assets.object_context.variant_id)
            for assets in scene_assets_by_episode.values()
        }
        sampled_receptacle_ids = {
            (assets.placement_context.category_id, assets.placement_context.variant_id)
            for assets in scene_assets_by_episode.values()
        }

        self.assertGreater(len(sampled_target_ids), 1)
        self.assertEqual(set(asset_bank.target_names), sampled_target_ids)
        self.assertEqual(set(asset_bank.receptacle_names), sampled_receptacle_ids)

    def test_beer_bottle_spawn_orientation_is_upright(self) -> None:
        from franka_wrist_camera_scene.objects.geometry_registry import get_object_geometry, load_object_geometry_registry
        registry = load_object_geometry_registry("object_geometry.generated.yaml")
        geometry = get_object_geometry(registry, "beer", "beer05")

        self.assertEqual(geometry.spawn_quat_wxyz, (0.0, 1.0, 0.0, 0.0))

    def test_bowl_receptacles_keep_default_orientation(self) -> None:
        from franka_wrist_camera_scene.objects.geometry_registry import get_object_geometry, load_object_geometry_registry
        registry = load_object_geometry_registry("object_geometry.generated.yaml")
        bowl_variants = [
            key
            for key in registry.records
            if key[0] == "bowl"
        ]

        self.assertGreater(len(bowl_variants), 0)
        for category_id, variant_id in bowl_variants:
            geometry = get_object_geometry(registry, category_id, variant_id)
            self.assertEqual(geometry.spawn_quat_wxyz, (1.0, 0.0, 0.0, 0.0))

    def test_placement_target_sampling_uses_physical_receptacles(self) -> None:
        from franka_wrist_camera_scene.objects.catalog import load_object_catalog
        from franka_wrist_camera_scene.objects.selection import (
            filtered_categories,
            matching_variants,
            variant_visual_label,
        )

        catalog = load_object_catalog("object_catalog.generated.yaml")
        categories = filtered_categories(catalog, split="train", role="target")
        placement_candidates = {
            category.id
            for category in categories
            if matching_variants(
                category=category,
                required_affordances=("container", "physical_container"),
                required_grasp_strategy="unsupported",
            )
        }
        placement_labels = {
            variant_visual_label(category, variant)
            for category in categories
            for variant in matching_variants(
                category=category,
                required_affordances=("container", "physical_container"),
                required_grasp_strategy="unsupported",
            )
        }

        self.assertIn("bowl", placement_candidates)
        self.assertIn("box", placement_candidates)
        self.assertIn("plate", placement_candidates)
        self.assertIn("tray", placement_candidates)
        self.assertIn("basket", placement_labels)
        self.assertNotIn("box", placement_labels)
        self.assertNotIn("cup", placement_candidates)

    def test_tall_object_is_incompatible_with_shallow_receptacle(self) -> None:
        from franka_wrist_camera_scene.objects.geometry_registry import get_object_geometry, load_object_geometry_registry
        from franka_wrist_camera_scene.collection.pick_place import _object_receptacle_pair_is_compatible

        registry = load_object_geometry_registry("object_geometry.generated.yaml")
        beer = get_object_geometry(registry, "beer", "beer05")
        bowl = get_object_geometry(registry, "bowl", "bowl18")

        class Context:
            def __init__(self, geometry):
                self.geometry = geometry

        self.assertFalse(
            _object_receptacle_pair_is_compatible(
                object_context=Context(beer),
                placement_context=Context(bowl),
                compatibility_cfg={"max_height_to_receptacle_width": 1.1},
            )
        )

    def test_gripper_filter_rejects_wide_target_object(self) -> None:
        from franka_wrist_camera_scene.objects.geometry_registry import get_object_geometry, load_object_geometry_registry
        from franka_wrist_camera_scene.collection.pick_place import _object_fits_gripper

        registry = load_object_geometry_registry("object_geometry.generated.yaml")
        tomato = get_object_geometry(registry, "tomato", "tomato03")

        self.assertFalse(
            _object_fits_gripper(
                context=SimpleNamespace(geometry=tomato),
                sampling_cfg={"max_planar_minor_extent_m": 0.08},
            )
        )

    def test_gripper_filter_rejects_borderline_target_object(self) -> None:
        from franka_wrist_camera_scene.objects.geometry_registry import get_object_geometry, load_object_geometry_registry
        from franka_wrist_camera_scene.collection.pick_place import _object_fits_gripper

        registry = load_object_geometry_registry("object_geometry.generated.yaml")
        tomato = get_object_geometry(registry, "tomato", "tomato02")

        self.assertFalse(
            _object_fits_gripper(
                context=SimpleNamespace(geometry=tomato),
                sampling_cfg={"max_planar_minor_extent_m": 0.075},
            )
        )

    def test_gripper_filter_accepts_narrow_target_object(self) -> None:
        from franka_wrist_camera_scene.objects.geometry_registry import get_object_geometry, load_object_geometry_registry
        from franka_wrist_camera_scene.collection.pick_place import _object_fits_gripper

        registry = load_object_geometry_registry("object_geometry.generated.yaml")
        tomato = get_object_geometry(registry, "tomato", "tomato07")

        self.assertTrue(
            _object_fits_gripper(
                context=SimpleNamespace(geometry=tomato),
                sampling_cfg={"max_planar_minor_extent_m": 0.075},
            )
        )

    def test_single_env_inactive_assets_are_all_non_active_bank_assets(self) -> None:
        from franka_wrist_camera_scene.collection.pick_place import (
            PickPlaceAssetBank,
            PickPlaceAssetNames,
            _inactive_asset_names,
        )
        asset_bank = PickPlaceAssetBank(
            target_names={("apple", "apple00"): "target_cube", ("peach", "peach01"): "target_peach_peach01"},
            receptacle_names={("bowl", "bowl00"): "place_receptacle", ("box", "box01"): "receptacle_box_box01"},
            clutter_names={
                (0, "lemon", "lemon01"): "clutter_0",
                (1, "plate", "plate01"): "clutter_1",
                (2, "kiwi", "kiwi07"): "clutter_2",
                (0, "tomato", "tomato02"): "clutter_0_tomato_tomato02",
            },
            target_usd_paths={
                "target_cube": "...",
                "target_peach_peach01": "...",
            },
            receptacle_usd_paths={
                "place_receptacle": "...",
                "receptacle_box_box01": "...",
            },
            clutter_usd_paths={
                "clutter_0": "...",
                "clutter_1": "...",
                "clutter_2": "...",
                "clutter_0_tomato_tomato02": "...",
            },
        )
        active = PickPlaceAssetNames(
            object_name="target_peach_peach01",
            placement_target_name="receptacle_box_box01",
            clutter_names=("clutter_0_tomato_tomato02", "clutter_1", "clutter_2"),
        )

        inactive_objects, inactive_receptacles, inactive_clutter = _inactive_asset_names(asset_bank, active)

        self.assertEqual(inactive_objects, ("target_cube",))
        self.assertEqual(inactive_receptacles, ("place_receptacle",))
        self.assertEqual(inactive_clutter, ("clutter_0",))
