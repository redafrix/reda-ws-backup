"""Unit tests for geometry-aware clutter sampling."""

from __future__ import annotations

import math
import random
import unittest
from types import SimpleNamespace

from franka_wrist_camera_scene.scene.clutter import (
    ClutterObjectSpec,
    FootprintDisk,
    XYRange,
    clutter_count_options,
    _sort_clutter_slots_by_descending_footprint,
    clutter_source_counts,
    footprints_overlap,
    footprint_for_context,
    layout_margin_for_context,
    planar_footprint_radius_m,
    place_clutter_contexts,
    place_reaching_clutter_contexts,
    sample_clutter_contexts,
    sample_reaching_clutter_xy,
    sample_non_overlapping_xy,
    validate_unique_active_labels,
    validate_unique_active_scene_labels,
)
import franka_wrist_camera_scene.scene.clutter as clutter_module


class ClutterSamplingTests(unittest.TestCase):
    def test_planar_footprint_radius_m_uses_bbox_diagonal_and_margin(self) -> None:
        radius = planar_footprint_radius_m(
            bbox_min=(-0.1, -0.2, 0.0),
            bbox_max=(0.1, 0.2, 0.1),
            margin_m=0.01,
        )
        expected = math.hypot(0.1, 0.2) + 0.01
        self.assertAlmostEqual(radius, expected)

    def test_container_context_gets_extra_layout_margin(self) -> None:
        cfg = {"container_exclusion_extra_margin_m": 0.05}
        bowl = SimpleNamespace(category_id="bowl", label="bowl", affordances=("container",))
        apple = SimpleNamespace(category_id="apple", label="apple", affordances=("pickable",))

        self.assertAlmostEqual(layout_margin_for_context(bowl, 0.02, cfg), 0.07)
        self.assertAlmostEqual(layout_margin_for_context(apple, 0.02, cfg), 0.02)

    def test_container_footprint_rejects_old_allowed_distance(self) -> None:
        cfg = {"container_exclusion_extra_margin_m": 0.05}
        geometry = SimpleNamespace(
            local_bbox_min=(-0.05, -0.05, 0.0),
            local_bbox_max=(0.05, 0.05, 0.1),
        )
        bowl = SimpleNamespace(
            category_id="bowl",
            label="bowl",
            affordances=("container",),
            geometry=geometry,
        )
        apple = SimpleNamespace(
            category_id="apple",
            label="apple",
            affordances=("pickable",),
            geometry=geometry,
        )
        apple_radius = footprint_for_context(apple, 0.02)
        bowl_base_radius = footprint_for_context(bowl, 0.02)
        bowl_extra_radius = footprint_for_context(
            bowl,
            layout_margin_for_context(bowl, 0.02, cfg),
        )
        old_allowed_distance = apple_radius + bowl_base_radius + 0.001

        apple_disk = FootprintDisk(xy=(0.0, 0.0), radius_m=apple_radius)
        bowl_disk = FootprintDisk(xy=(old_allowed_distance, 0.0), radius_m=bowl_extra_radius)

        self.assertTrue(footprints_overlap(apple_disk, bowl_disk))
        self.assertGreater(bowl_extra_radius, bowl_base_radius)

    def test_footprints_overlap_detects_overlap_and_separation(self) -> None:
        overlapping_a = FootprintDisk(xy=(0.0, 0.0), radius_m=0.2)
        overlapping_b = FootprintDisk(xy=(0.3, 0.0), radius_m=0.2)
        separated_a = FootprintDisk(xy=(0.0, 0.0), radius_m=0.1)
        separated_b = FootprintDisk(xy=(1.0, 0.0), radius_m=0.1)

        self.assertTrue(footprints_overlap(overlapping_a, overlapping_b))
        self.assertFalse(footprints_overlap(separated_a, separated_b))

    def test_sample_non_overlapping_xy_avoids_occupied_disks(self) -> None:
        rng = random.Random(7)
        xy_range = XYRange(x=(0.0, 1.0), y=(0.0, 1.0))
        occupied = (FootprintDisk(xy=(0.2, 0.2), radius_m=0.15),)
        candidate_radius_m = 0.1

        for _ in range(32):
            xy = sample_non_overlapping_xy(
                rng=rng,
                xy_range=xy_range,
                candidate_radius_m=candidate_radius_m,
                occupied=occupied,
                max_attempts=64,
                grid_step_m=0.015,
            )
            candidate = FootprintDisk(xy=xy, radius_m=candidate_radius_m)
            self.assertFalse(footprints_overlap(candidate, occupied[0]))

    def test_sample_non_overlapping_xy_fails_loudly_when_impossible(self) -> None:
        xy_range = XYRange(x=(0.0, 0.1), y=(0.0, 0.1))
        occupied = (FootprintDisk(xy=(0.05, 0.05), radius_m=1.0),)

        with self.assertRaises(RuntimeError):
            sample_non_overlapping_xy(
                rng=random.Random(0),
                xy_range=xy_range,
                candidate_radius_m=0.2,
                occupied=occupied,
                max_attempts=8,
                grid_step_m=0.015,
            )

    def test_clutter_slots_are_placed_largest_first(self) -> None:
        slots = [
            (0, object(), 0.10),
            (1, object(), 0.25),
            (2, object(), 0.15),
        ]

        ordered = _sort_clutter_slots_by_descending_footprint(slots)

        self.assertEqual([slot[0] for slot in ordered], [1, 2, 0])

    def test_place_clutter_contexts_uses_configured_layout_attempts(self) -> None:
        cfg = {
            "count": 1,
            "xy_range": {"x": [0.0, 1.0], "y": [0.0, 1.0]},
            "object_margin_m": 0.0,
            "placement_target_margin_m": 0.0,
            "clutter_margin_m": 0.0,
            "max_layout_sampling_attempts": 1,
            "grid_step_m": 0.5,
        }
        geometry = SimpleNamespace(
            local_bbox_min=(-0.05, -0.05, 0.0),
            local_bbox_max=(0.05, 0.05, 0.1),
        )
        context = SimpleNamespace(geometry=geometry)

        specs = place_clutter_contexts(
            clutter_cfg=cfg,
            rng=random.Random(0),
            support_surface_z_local=1.0,
            object_bottom_clearance_m=0.0,
            target_object_context=context,
            target_object_xy=(0.5, 0.5),
            placement_target_context=context,
            placement_target_xy=(0.8, 0.8),
            clutter_contexts=(context,),
        )

        self.assertEqual(len(specs), 1)

    def test_clutter_source_counts_allocates_extra_count_by_weight(self) -> None:
        cfg = {
            "catalog_config": "object_catalog.generated.yaml",
            "geometry_config": "object_geometry.generated.yaml",
            "slot_count": 12,
            "count_options": [6, 12],
            "sources": [
                {
                    "name": "objects",
                    "min_count": 3,
                    "weight": 3,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["pickable"],
                    "required_grasp_strategy": "center_top",
                },
                {
                    "name": "receptacles",
                    "min_count": 2,
                    "weight": 2,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["container", "physical_container"],
                    "required_grasp_strategy": "unsupported",
                },
                {
                    "name": "supports",
                    "min_count": 1,
                    "weight": 1,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "clutter",
                    "required_affordances": ["reachable", "support"],
                    "required_grasp_strategy": "unsupported",
                },
            ],
        }

        self.assertEqual(clutter_count_options(cfg), (6, 12))
        counts = {
            source_name: count
            for source_name, count, _ in clutter_source_counts(cfg, active_count=12)
        }

        self.assertEqual(counts, {"objects": 6, "receptacles": 4, "supports": 2})

    def test_clutter_source_counts_respects_max_count(self) -> None:
        cfg = {
            "catalog_config": "object_catalog.generated.yaml",
            "geometry_config": "object_geometry.generated.yaml",
            "slot_count": 12,
            "count_options": [12],
            "sources": [
                {
                    "name": "objects",
                    "min_count": 3,
                    "weight": 3,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["pickable"],
                    "required_grasp_strategy": "center_top",
                },
                {
                    "name": "receptacles",
                    "min_count": 1,
                    "max_count": 1,
                    "weight": 1,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["container", "physical_container"],
                    "required_grasp_strategy": "unsupported",
                },
                {
                    "name": "supports",
                    "min_count": 1,
                    "weight": 1,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "clutter",
                    "required_affordances": ["reachable", "support"],
                    "required_grasp_strategy": "unsupported",
                },
            ],
        }
        counts = {
            source_name: count
            for source_name, count, _ in clutter_source_counts(cfg, active_count=12)
        }
        self.assertEqual(counts["receptacles"], 1)
        self.assertEqual(counts["objects"] + counts["receptacles"] + counts["supports"], 12)

    def test_clutter_source_counts_invalid_constraints_raise(self) -> None:
        # max_count < min_count raises ValueError
        cfg = {
            "catalog_config": "object_catalog.generated.yaml",
            "geometry_config": "object_geometry.generated.yaml",
            "slot_count": 12,
            "sources": [
                {
                    "name": "objects",
                    "min_count": 3,
                    "max_count": 2,
                    "weight": 3,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["pickable"],
                    "required_grasp_strategy": "center_top",
                }
            ]
        }
        with self.assertRaises(ValueError):
            clutter_source_counts(cfg, active_count=12)

        # min_count total > active_count raises ValueError
        cfg_invalid_min = {
            "catalog_config": "object_catalog.generated.yaml",
            "geometry_config": "object_geometry.generated.yaml",
            "slot_count": 12,
            "sources": [
                {
                    "name": "objects",
                    "min_count": 15,
                    "weight": 3,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["pickable"],
                    "required_grasp_strategy": "center_top",
                }
            ]
        }
        with self.assertRaises(ValueError):
            clutter_source_counts(cfg_invalid_min, active_count=12)

        # No capacity for remaining extras raises ValueError
        cfg_no_capacity = {
            "catalog_config": "object_catalog.generated.yaml",
            "geometry_config": "object_geometry.generated.yaml",
            "slot_count": 12,
            "sources": [
                {
                    "name": "objects",
                    "min_count": 3,
                    "max_count": 3,
                    "weight": 3,
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": ["pickable"],
                    "required_grasp_strategy": "center_top",
                }
            ]
        }
        with self.assertRaises(ValueError):
            clutter_source_counts(cfg_no_capacity, active_count=12)

    def test_sample_clutter_contexts_can_enforce_unique_labels(self) -> None:
        geometry = SimpleNamespace(
            local_bbox_min=(-0.01, -0.01, 0.0),
            local_bbox_max=(0.01, 0.01, 0.02),
        )
        candidates = (
            SimpleNamespace(category_id="apple", variant_id="apple00", label="apple", geometry=geometry),
            SimpleNamespace(category_id="apple", variant_id="apple01", label="apple", geometry=geometry),
            SimpleNamespace(category_id="banana", variant_id="banana00", label="banana", geometry=geometry),
        )

        def fake_load_catalog_object_context(*, excluded_category_ids=(), excluded_labels=(), **_kwargs):
            for candidate in candidates:
                if candidate.category_id not in excluded_category_ids and candidate.label not in excluded_labels:
                    return candidate
            raise RuntimeError("No fake candidate available.")

        cfg = {
            "catalog_config": "unused",
            "geometry_config": "unused",
            "category_id": "sample",
            "variant_id": "sample",
            "split": "train",
            "role": "target",
            "required_affordances": ["reachable"],
            "required_grasp_strategy": "unsupported",
            "unique_labels": True,
            "max_asset_sampling_attempts": 8,
            "max_footprint_radius_m": 1.0,
            "clutter_margin_m": 0.0,
        }

        original_loader = clutter_module.load_catalog_object_context
        clutter_module.load_catalog_object_context = fake_load_catalog_object_context
        try:
            contexts = sample_clutter_contexts(cfg, rng=random.Random(0), count=2)
        finally:
            clutter_module.load_catalog_object_context = original_loader

        self.assertEqual([context.category_id for context in contexts], ["apple", "banana"])

    def test_sample_clutter_contexts_filters_asset_size_before_layout_extra_margin(self) -> None:
        geometry = SimpleNamespace(
            local_bbox_min=(-0.075, -0.075, 0.0),
            local_bbox_max=(0.075, 0.075, 0.02),
        )
        bowl = SimpleNamespace(
            category_id="bowl",
            variant_id="bowl00",
            label="bowl",
            affordances=("container", "physical_container"),
            geometry=geometry,
        )

        def fake_load_catalog_object_context(**_kwargs):
            return bowl

        cfg = {
            "catalog_config": "unused",
            "geometry_config": "unused",
            "category_id": "sample",
            "variant_id": "sample",
            "split": "train",
            "role": "target",
            "required_affordances": ["container"],
            "required_grasp_strategy": "unsupported",
            "unique_labels": True,
            "max_asset_sampling_attempts": 1,
            "max_footprint_radius_m": 0.14,
            "clutter_margin_m": 0.025,
            "container_exclusion_extra_margin_m": 0.05,
        }

        original_loader = clutter_module.load_catalog_object_context
        clutter_module.load_catalog_object_context = fake_load_catalog_object_context
        try:
            contexts = sample_clutter_contexts(cfg, rng=random.Random(0), count=1)
        finally:
            clutter_module.load_catalog_object_context = original_loader

        self.assertEqual(contexts, (bowl,))

    def test_reaching_clutter_sampling_uses_extra_margin_only_against_target(self) -> None:
        xy_range = XYRange(x=(0.0, 1.0), y=(0.0, 1.0))
        target = FootprintDisk(xy=(0.1, 0.1), radius_m=0.20)
        occupied_clutter = (FootprintDisk(xy=(0.5, 0.5), radius_m=0.17),)

        xy = sample_reaching_clutter_xy(
            rng=random.Random(1),
            xy_range=xy_range,
            target_disk=target,
            candidate_target_clearance_radius_m=0.22,
            candidate_clutter_radius_m=0.17,
            occupied_clutter=occupied_clutter,
            max_attempts=1,
            grid_step_m=0.01,
        )
        candidate_physical = FootprintDisk(xy=xy, radius_m=0.17)
        candidate_target_clearance = FootprintDisk(xy=xy, radius_m=0.22)

        self.assertFalse(footprints_overlap(candidate_physical, occupied_clutter[0]))
        self.assertFalse(footprints_overlap(candidate_target_clearance, target))

    def test_validate_unique_active_labels_rejects_duplicate_clutter_label(self) -> None:
        target = SimpleNamespace(label="apple")
        specs = (
            ClutterObjectSpec(
                prim_name="clutter_0",
                context=SimpleNamespace(label="bowl"),
                pos_local=(0.0, 0.0, 1.0),
                footprint_radius_m=0.1,
            ),
            ClutterObjectSpec(
                prim_name="clutter_1",
                context=SimpleNamespace(label="bowl"),
                pos_local=(0.4, 0.0, 1.0),
                footprint_radius_m=0.1,
            ),
        )

        with self.assertRaisesRegex(ValueError, "duplicate visual labels"):
            validate_unique_active_labels(target, specs)

    def test_validate_unique_active_labels_rejects_target_duplicate(self) -> None:
        target = SimpleNamespace(label="apple")
        specs = (
            ClutterObjectSpec(
                prim_name="clutter_0",
                context=SimpleNamespace(label="apple"),
                pos_local=(0.0, 0.0, 1.0),
                footprint_radius_m=0.1,
            ),
        )

        with self.assertRaisesRegex(ValueError, "apple"):
            validate_unique_active_labels(target, specs)

    def test_validate_unique_active_scene_labels_rejects_receptacle_duplicate(self) -> None:
        target = SimpleNamespace(category_id="apple", variant_id="apple00", label="apple")
        receptacle = SimpleNamespace(category_id="bowl", variant_id="bowl00", label="bowl")
        specs = (
            ClutterObjectSpec(
                prim_name="clutter_0",
                context=SimpleNamespace(category_id="bowl", variant_id="bowl01", label="bowl"),
                pos_local=(0.0, 0.0, 1.0),
                footprint_radius_m=0.1,
            ),
        )

        with self.assertRaisesRegex(ValueError, "bowl"):
            validate_unique_active_scene_labels(
                named_contexts=(("target", target), ("placement_target", receptacle)),
                clutter_specs=specs,
            )

    def test_validate_unique_active_scene_labels_rejects_duplicate_asset_key(self) -> None:
        target = SimpleNamespace(category_id="apple", variant_id="apple00", label="red apple")
        specs = (
            ClutterObjectSpec(
                prim_name="clutter_0",
                context=SimpleNamespace(category_id="apple", variant_id="apple00", label="green apple"),
                pos_local=(0.0, 0.0, 1.0),
                footprint_radius_m=0.1,
            ),
        )

        with self.assertRaisesRegex(ValueError, "duplicate object assets"):
            validate_unique_active_scene_labels(
                named_contexts=(("target", target),),
                clutter_specs=specs,
            )

    def test_validate_unique_active_labels_allows_unique_labels(self) -> None:
        target = SimpleNamespace(label="apple")
        specs = (
            ClutterObjectSpec(
                prim_name="clutter_0",
                context=SimpleNamespace(label="bowl"),
                pos_local=(0.0, 0.0, 1.0),
                footprint_radius_m=0.1,
            ),
        )

        validate_unique_active_labels(target, specs)

    def test_place_reaching_clutter_contexts_avoids_target_footprint(self) -> None:
        cfg = {
            "count": 2,
            "xy_range": {"x": [0.0, 0.7], "y": [0.0, 0.7]},
            "object_margin_m": 0.02,
            "clutter_margin_m": 0.02,
            "max_layout_sampling_attempts": 64,
            "grid_step_m": 0.02,
        }
        target_geometry = SimpleNamespace(
            local_bbox_min=(-0.06, -0.06, -0.02),
            local_bbox_max=(0.06, 0.06, 0.05),
        )
        clutter_geometry = SimpleNamespace(
            local_bbox_min=(-0.03, -0.03, -0.01),
            local_bbox_max=(0.03, 0.03, 0.04),
        )
        target_context = SimpleNamespace(geometry=target_geometry)
        clutter_context = SimpleNamespace(geometry=clutter_geometry)

        specs = place_reaching_clutter_contexts(
            clutter_cfg=cfg,
            rng=random.Random(4),
            support_surface_z_local=1.0,
            object_bottom_clearance_m=0.0,
            target_object_context=target_context,
            target_object_xy=(0.35, 0.35),
            clutter_contexts=(
                ("objects", clutter_context),
                ("receptacles", clutter_context),
            ),
        )

        target = FootprintDisk(
            xy=(0.35, 0.35),
            radius_m=planar_footprint_radius_m(
                target_geometry.local_bbox_min,
                target_geometry.local_bbox_max,
                margin_m=0.02,
            ),
        )
        self.assertEqual(len(specs), 2)
        for spec in specs:
            candidate = FootprintDisk(
                xy=(spec.pos_local[0], spec.pos_local[1]),
                radius_m=spec.footprint_radius_m,
            )
            self.assertFalse(footprints_overlap(candidate, target))


if __name__ == "__main__":
    unittest.main()
