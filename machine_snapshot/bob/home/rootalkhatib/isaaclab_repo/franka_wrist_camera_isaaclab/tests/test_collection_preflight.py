from copy import deepcopy
from pathlib import Path
from unittest import TestCase

import yaml

from franka_wrist_camera_scene.collection.preflight import validate_collection_config
from franka_wrist_camera_scene.collection.configs import collection_configs_from_config
from franka_wrist_camera_scene.objects.catalog import load_object_catalog
from franka_wrist_camera_scene.objects.selection import (
    matching_variants,
    variant_affordances,
)


SUITE_DIR = Path("configs/suites")


def load_config(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


class TestCollectionPreflight(TestCase):
    def test_collection_configs_from_config_returns_single_config(self) -> None:
        config = {"task": "reaching"}

        self.assertEqual(collection_configs_from_config(config), [config])

    def test_collection_configs_from_config_returns_combined_configs(self) -> None:
        configs = [{"task": "reaching"}, {"task": "pick_place"}]

        self.assertEqual(collection_configs_from_config({"collections": configs}), configs)

    def test_collection_configs_from_config_rejects_empty_combined_config(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-empty collections list"):
            collection_configs_from_config({"collections": []})

    def test_all_suite_configs_are_valid(self) -> None:
        suite_paths = sorted(SUITE_DIR.glob("*.yaml"))

        self.assertGreater(len(suite_paths), 0)
        for suite_path in suite_paths:
            with self.subTest(suite=suite_path.name):
                report = validate_collection_config(load_config(suite_path))
                self.assertEqual(report.suite.name, suite_path.stem)

    def test_train_receptacles_are_physical_and_exclude_cups(self) -> None:
        config = load_config(SUITE_DIR / "pick_place_train_core.yaml")

        report = validate_collection_config(config)
        receptacles = report.placement_targets

        self.assertIsNotNone(receptacles)
        self.assertNotIn("cup", receptacles.category_ids)
        for candidate in receptacles.candidates:
            self.assertIn(
                "physical_container",
                variant_affordances(candidate.category, candidate.variant),
            )

    def test_train_suite_includes_every_curated_physical_receptacle_category(self) -> None:
        config = load_config(SUITE_DIR / "pick_place_train_core.yaml")
        catalog = load_object_catalog("object_catalog.generated.yaml")
        expected_categories = {
            category.id
            for category in catalog.categories
            if category.split == "train"
            and category.role == "target"
            and matching_variants(
                category,
                ("container", "physical_container"),
                "unsupported",
            )
        }

        report = validate_collection_config(config)

        self.assertEqual(set(report.placement_targets.category_ids), expected_categories)

    def test_empty_unseen_receptacle_pool_fails(self) -> None:
        config = load_config(SUITE_DIR / "pick_place_train_core.yaml")
        config["placement_target"]["split"] = "unseen"

        with self.assertRaisesRegex(ValueError, "placement_target.*empty"):
            validate_collection_config(config)

    def test_pick_place_clutter_count_options_outside_dense_range_fails(self) -> None:
        config = deepcopy(load_config(SUITE_DIR / "pick_place_train_core.yaml"))
        config["clutter"]["count_options"] = [4]

        with self.assertRaisesRegex(ValueError, "pick-place clutter.count_options"):
            validate_collection_config(config)

    def test_visual_shift_suite_is_valid(self) -> None:
        config = load_config(SUITE_DIR / "pick_place_eval_visual_shift.yaml")

        report = validate_collection_config(config)

        self.assertEqual(report.suite.difficulty, "visual_shift")

    def test_reaching_config_remains_valid(self) -> None:
        config = load_config(Path("configs/collection_reaching.yaml"))

        report = validate_collection_config(config)

        self.assertIsNone(report.placement_targets)
        self.assertIsNotNone(report.clutter)
        self.assertGreater(len(report.clutter.candidates), 0)

    def test_reaching_support_distractors_can_use_support_receptacles(self) -> None:
        from franka_wrist_camera_scene.objects.candidates import load_candidate_pool, target_query
        from franka_wrist_camera_scene.scene.clutter import normalize_clutter_source_config

        config = load_config(Path("configs/collection_reaching.yaml"))
        support_source = next(
            source
            for source in config["clutter"]["sources"]
            if source["name"] == "support_distractors"
        )
        source_cfg = normalize_clutter_source_config(config["clutter"], support_source)

        pool = load_candidate_pool("support_distractors", target_query(source_cfg))

        self.assertGreaterEqual(set(pool.category_ids), {"placemat", "plate", "tray"})

    def test_reaching_episode_96_clutter_sources_do_not_exhaust_support_labels(self) -> None:
        import random

        from franka_wrist_camera_scene.scene.clutter import (
            sample_clutter_count,
            sample_clutter_contexts_from_sources,
        )
        from franka_wrist_camera_scene.scene.object_context import load_catalog_object_context

        config = load_config(Path("configs/collect_reaching_episodes.yaml"))
        episode_id = 96
        seed = int(config["seed"])
        rng = random.Random(seed + episode_id)
        sources = config["target_sources"]
        source_cfg = rng.choices(
            sources,
            weights=[float(source.get("weight", 1.0)) for source in sources],
            k=1,
        )[0]
        target = load_catalog_object_context(
            source_cfg["catalog_config"],
            source_cfg["geometry_config"],
            source_cfg["category_id"],
            source_cfg["variant_id"],
            source_cfg["split"],
            source_cfg["role"],
            tuple(source_cfg["required_affordances"]),
            source_cfg["required_grasp_strategy"],
            rng,
        )
        clutter_cfg = config["clutter"]
        active_count = sample_clutter_count(clutter_cfg, seed, episode_id)

        contexts = sample_clutter_contexts_from_sources(
            clutter_cfg=clutter_cfg,
            rng=random.Random(seed + 200_000 + episode_id),
            active_count=active_count,
            excluded_keys=((target.category_id, target.variant_id),),
            excluded_category_ids=(target.category_id,),
            excluded_labels=(target.label,),
        )
        labels = [target.label, *(context.label for _, context in contexts)]

        self.assertEqual(len(contexts), active_count)
        self.assertEqual(len(labels), len(set(labels)))

    def test_reaching_clutter_slot_count_must_match_scene_capacity(self) -> None:
        config = deepcopy(load_config(Path("configs/collection_reaching.yaml")))
        config["clutter"]["slot_count"] = 11

        with self.assertRaisesRegex(ValueError, "reaching clutter.slot_count must be 12"):
            validate_collection_config(config)

    def test_reaching_requires_unique_clutter_labels(self) -> None:
        config = deepcopy(load_config(Path("configs/collection_reaching.yaml")))
        config["clutter"]["unique_labels"] = False

        with self.assertRaisesRegex(ValueError, "clutter.unique_labels=true"):
            validate_collection_config(config)
