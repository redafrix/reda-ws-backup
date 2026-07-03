import unittest
import subprocess
import tempfile
import shutil
import math
from pathlib import Path
from types import SimpleNamespace

from franka_wrist_camera_scene.tasks.layout_geometry import (
    FootprintCircle,
    planar_footprint_radius_from_bbox,
    footprints_overlap_xy,
    require_non_overlapping_footprints,
    validate_non_overlapping_layout,
    validate_pick_place_initial_layout,
    validate_reaching_initial_layout,
)


class TestLayoutGeometry(unittest.TestCase):
    def test_centered_bbox_radius_uses_root_corner_distance(self):
        radius = planar_footprint_radius_from_bbox(
            bbox_min=(-0.1, -0.2, 0.0),
            bbox_max=(0.1, 0.2, 0.1),
            margin_m=0.01,
        )

        self.assertAlmostEqual(radius, math.hypot(0.1, 0.2) + 0.01)

    def test_off_center_bbox_radius_uses_root_corner_distance(self):
        radius = planar_footprint_radius_from_bbox(
            bbox_min=(0.2, -0.1, 0.0),
            bbox_max=(0.4, 0.1, 0.1),
            margin_m=0.01,
        )

        self.assertAlmostEqual(radius, math.hypot(0.4, 0.1) + 0.01)

    def test_candidate_footprint_filter_uses_root_origin_radius(self):
        from franka_wrist_camera_scene.objects.candidates import (
            CandidatePool,
            CatalogCandidate,
            limit_clutter_footprint,
        )

        geometry = SimpleNamespace(
            local_bbox_min=(0.2, -0.1, 0.0),
            local_bbox_max=(0.4, 0.1, 0.1),
        )
        candidate = CatalogCandidate(
            category=SimpleNamespace(id="offset"),
            variant=SimpleNamespace(id="offset00"),
            geometry=geometry,
        )

        with self.assertRaisesRegex(ValueError, "footprint filtering"):
            limit_clutter_footprint(
                CandidatePool("offset_pool", (candidate,)),
                max_radius_m=0.25,
                margin_m=0.0,
            )

    def test_invalid_bbox_raises(self):
        with self.assertRaises(ValueError):
            # size_x <= 0
            planar_footprint_radius_from_bbox((0.5, 0.5, 0.0), (0.4, 0.6, 0.1), 0.01)

    def test_negative_margin_raises(self):
        with self.assertRaises(ValueError):
            planar_footprint_radius_from_bbox((0.0, 0.0, 0.0), (0.1, 0.1, 0.1), -0.01)

    def test_far_apart_passes(self):
        a = FootprintCircle(name="object", xy=(0.0, 0.0), radius_m=0.05)
        b = FootprintCircle(name="receptacle", xy=(0.5, 0.0), radius_m=0.1)
        self.assertFalse(footprints_overlap_xy(a, b))
        require_non_overlapping_footprints(a, b)

    def test_wide_receptacle_overlap_fails(self):
        # Centers are 0.3m apart, but sum of radii is 0.35m. They should overlap and raise.
        a = FootprintCircle(name="object", xy=(0.0, 0.0), radius_m=0.15)
        b = FootprintCircle(name="receptacle", xy=(0.3, 0.0), radius_m=0.2)
        self.assertTrue(footprints_overlap_xy(a, b))
        with self.assertRaises(ValueError):
            require_non_overlapping_footprints(a, b)

    def test_clutter_overlaps(self):
        target = FootprintCircle(name="target", xy=(0.0, 0.0), radius_m=0.05)
        receptacle = FootprintCircle(name="receptacle", xy=(0.5, 0.0), radius_m=0.1)

        # Clutter overlaps target
        clutter_overlapping_target = (
            FootprintCircle(name="clutter1", xy=(0.04, 0.0), radius_m=0.05),
        )
        with self.assertRaises(ValueError):
            validate_pick_place_initial_layout(
                target, receptacle, clutter_overlapping_target
            )

        # Clutter overlaps receptacle
        clutter_overlapping_receptacle = (
            FootprintCircle(name="clutter2", xy=(0.45, 0.0), radius_m=0.1),
        )
        with self.assertRaises(ValueError):
            validate_pick_place_initial_layout(
                target, receptacle, clutter_overlapping_receptacle
            )

        # Reaching: clutter overlaps target
        with self.assertRaises(ValueError):
            validate_reaching_initial_layout(target, clutter_overlapping_target)

    def test_preflight_rejects_missing_target_sources(self):
        from franka_wrist_camera_scene.collection.preflight import (
            validate_collection_config,
        )

        config = {
            "task": "reaching",
            "seed": 123,
            "visual_randomization": None,
            "target_object": {
                "catalog_config": "object_catalog.generated.yaml",
                "geometry_config": "object_geometry.generated.yaml",
                "category_id": "sample",
                "variant_id": "sample",
                "split": "train",
                "role": "target",
                "required_affordances": [],
                "required_grasp_strategy": "center_top",
            },
        }
        with self.assertRaises(ValueError) as ctx:
            validate_collection_config(config)
        self.assertIn("target_sources", str(ctx.exception))

    def test_preflight_rejects_zero_clutter_reaching(self):
        from franka_wrist_camera_scene.collection.preflight import (
            validate_collection_config,
        )

        config = {
            "task": "reaching",
            "seed": 123,
            "visual_randomization": None,
            "suite": {
                "name": "dummy",
                "split": "train",
                "difficulty": "core",
                "tags": [],
                "description": "",
            },
            "target_sources": [
                {
                    "name": "dummy_source",
                    "catalog_config": "object_catalog.generated.yaml",
                    "geometry_config": "object_geometry.generated.yaml",
                    "category_id": "sample",
                    "variant_id": "sample",
                    "split": "train",
                    "role": "target",
                    "required_affordances": [],
                    "required_grasp_strategy": "center_top",
                }
            ],
            "clutter": {
                "catalog_config": "object_catalog.generated.yaml",
                "geometry_config": "object_geometry.generated.yaml",
                "slot_count": 12,
                "unique_labels": True,
                "count": 0,
                "count_options": [0],
                "sources": [],
            },
        }
        with self.assertRaises(ValueError) as ctx:
            validate_collection_config(config)
        self.assertIn("minimum value must be >= 1", str(ctx.exception))

    def test_check_collection_success_script(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)

            # Scenario 1: One success episode -> check script exits 0
            ep0 = tmp_path / "000000"
            ep0.mkdir()
            (ep0 / "meta.json").write_text(
                '{"episode_id": 0, "success": true, "num_steps": 10}',
                encoding="utf-8",
            )

            res = subprocess.run(
                ["python", "scripts/check_collection_success.py", tmpdir],
                capture_output=True,
                text=True,
            )
            self.assertEqual(res.returncode, 0)

            # Scenario 2: Failed episode but missing failure.json -> exits nonzero
            ep1 = tmp_path / "000001"
            ep1.mkdir()
            (ep1 / "meta.json").write_text(
                '{"episode_id": 1, "success": false, "num_steps": 10}',
                encoding="utf-8",
            )

            res = subprocess.run(
                ["python", "scripts/check_collection_success.py", tmpdir],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("missing failure.json", res.stderr)

            # Scenario 3: Failed episode with failure.json, no --allow-failures -> exits nonzero
            (ep1 / "failure.json").write_text('{"episode_id": 1}', encoding="utf-8")
            res = subprocess.run(
                ["python", "scripts/check_collection_success.py", tmpdir],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Validation FAILED", res.stderr)

            # Scenario 4: Failed episode with failure.json, with --allow-failures -> exits 0
            res = subprocess.run(
                [
                    "python",
                    "scripts/check_collection_success.py",
                    tmpdir,
                    "--allow-failures",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(res.returncode, 0)
            self.assertIn("Validation PASSED", res.stdout)

            # Scenario 5: Malformed meta.json -> exits nonzero even with --allow-failures
            (ep1 / "meta.json").write_text("invalid json content", encoding="utf-8")
            res = subprocess.run(
                [
                    "python",
                    "scripts/check_collection_success.py",
                    tmpdir,
                    "--allow-failures",
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("ERROR parsing meta.json", res.stderr)

    def test_layout_boundary_validation(self):
        # Boundary: x=[0.0, 1.0], y=[0.0, 1.0]
        xy_range = (0.0, 1.0, 0.0, 1.0)

        # Valid layout: inside boundary
        target = FootprintCircle(name="target", xy=(0.5, 0.5), radius_m=0.05)
        receptacle = FootprintCircle(name="receptacle", xy=(0.8, 0.5), radius_m=0.1)
        clutter = (FootprintCircle(name="clutter", xy=(0.2, 0.5), radius_m=0.05),)

        # This should pass without raising
        validate_pick_place_initial_layout(target, receptacle, clutter, xy_range)
        validate_reaching_initial_layout(target, clutter, xy_range)

        # Target outside boundary -> fails
        target_outside = FootprintCircle(name="target", xy=(1.05, 0.5), radius_m=0.05)
        with self.assertRaises(ValueError) as ctx:
            validate_pick_place_initial_layout(target_outside, receptacle, clutter, xy_range)
        self.assertIn("Target object footprint 'target'", str(ctx.exception))
        self.assertIn("is not within", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            validate_reaching_initial_layout(target_outside, clutter, xy_range)
        self.assertIn("Target object footprint 'target'", str(ctx.exception))
        self.assertIn("is not within", str(ctx.exception))

        # Receptacle outside boundary -> fails
        receptacle_outside = FootprintCircle(name="receptacle", xy=(0.5, 1.05), radius_m=0.1)
        with self.assertRaises(ValueError) as ctx:
            validate_pick_place_initial_layout(target, receptacle_outside, clutter, xy_range)
        self.assertIn("Placement receptacle footprint 'receptacle'", str(ctx.exception))
        self.assertIn("is not within", str(ctx.exception))

        # Target center inside target_xy_range, but target footprint outside xy_range -> fails
        target_outside_footprint = FootprintCircle(name="target", xy=(0.98, 0.5), radius_m=0.05)
        target_xy_range = (0.0, 1.0, 0.0, 1.0)
        with self.assertRaises(ValueError) as ctx:
            validate_pick_place_initial_layout(target_outside_footprint, receptacle, clutter, xy_range, target_xy_range=target_xy_range)
        self.assertIn("Target object footprint 'target'", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            validate_reaching_initial_layout(target_outside_footprint, clutter, xy_range, target_xy_range=target_xy_range)
        self.assertIn("Target object footprint 'target'", str(ctx.exception))

        # Receptacle center inside receptacle_xy_range, but receptacle footprint outside xy_range -> fails
        receptacle_outside_footprint = FootprintCircle(name="receptacle", xy=(0.95, 0.5), radius_m=0.1)
        receptacle_xy_range = (0.0, 1.0, 0.0, 1.0)
        with self.assertRaises(ValueError) as ctx:
            validate_pick_place_initial_layout(target, receptacle_outside_footprint, clutter, xy_range, receptacle_xy_range=receptacle_xy_range)
        self.assertIn("Placement receptacle footprint 'receptacle'", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
