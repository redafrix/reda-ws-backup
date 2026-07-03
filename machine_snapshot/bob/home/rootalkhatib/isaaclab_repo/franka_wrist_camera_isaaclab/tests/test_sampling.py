from pathlib import Path
from unittest import TestCase

import yaml

from franka_wrist_camera_scene.settings import TABLE_COLOR, TABLE_HEIGHT_M
from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
from franka_wrist_camera_scene.tasks.reaching import (
    REACH_MODE_NEAREST_TOP_SURFACE,
    REACH_MODE_TOP_CENTER,
    ReachingTaskSpec,
    object_reach_offset_from_geometry,
    make_reaching_episode_spec,
)
from franka_wrist_camera_scene.tasks.sampling import (
    LightingOptions,
    PickPlaceSamplingOptions,
    ReachingSamplingOptions,
    VisualRandomizationOptions,
    WorkspaceConstraint,
    XYRange,
    parse_visual_randomization,
    sample_pick_place,
    sample_reaching_offsets,
    sample_table_color,
)

TABLE_COLORS = (
    (0.55, 0.42, 0.30),
    (0.35, 0.35, 0.35),
    (0.62, 0.55, 0.45),
    (0.25, 0.30, 0.35),
)


class TestVisualRandomizationSampling(TestCase):
    def test_missing_visual_randomization_uses_default_table_color(self) -> None:
        options = parse_visual_randomization(None)

        self.assertEqual(options.table_color_options, (TABLE_COLOR,))

    def test_table_color_sampling_is_deterministic(self) -> None:
        options = VisualRandomizationOptions(TABLE_COLORS)

        first = sample_table_color(1000, 4, options)
        second = sample_table_color(1000, 4, options)

        self.assertEqual(first, second)

    def test_episode_id_changes_sampled_table_color(self) -> None:
        options = VisualRandomizationOptions(TABLE_COLORS)

        first = sample_table_color(1000, 0, options)
        second = sample_table_color(1000, 1, options)

        self.assertNotEqual(first, second)


class TestReachingTaskSampling(TestCase):
    def test_reaching_spec_uses_geometry_for_object_height_and_reach_point(self) -> None:
        spec = make_reaching_episode_spec(
            base_spec=ReachingTaskSpec(object_pos_local=(0.58, -0.16, 1.08)),
            object_xy_offset=(0.02, -0.03),
            object_label="apple",
            object_local_bbox_min=(-0.02, -0.02, -0.04),
            object_local_bbox_max=(0.02, 0.02, 0.05),
            object_category_id="apple",
            object_affordances=("pickable", "reachable"),
        )

        self.assertEqual(spec.instruction, "reach the apple")
        self.assertAlmostEqual(spec.object_pos_local[0], 0.60)
        self.assertAlmostEqual(spec.object_pos_local[1], -0.19)
        self.assertAlmostEqual(spec.object_pos_local[2], TABLE_HEIGHT_M + 0.04 + 0.003)
        self.assertEqual(spec.object_reach_offset_local, (0.0, 0.0, 0.060000000000000005))
        self.assertEqual(spec.success_threshold_m, 0.01)

    def test_compact_object_reach_offset_uses_top_center(self) -> None:
        offset = object_reach_offset_from_geometry(
            object_xy=(0.58, -0.16),
            robot_base_xy=(0.10, 0.0),
            bbox_min=(-0.02, -0.03, -0.04),
            bbox_max=(0.02, 0.03, 0.05),
            reach_surface_clearance_m=0.01,
            reach_mode=REACH_MODE_TOP_CENTER,
        )

        self.assertEqual(offset, (0.0, 0.0, 0.060000000000000005))

    def test_container_reach_offset_uses_nearest_rim_side(self) -> None:
        offset = object_reach_offset_from_geometry(
            object_xy=(0.50, 0.20),
            robot_base_xy=(0.10, 0.20),
            bbox_min=(-0.10, -0.05, -0.03),
            bbox_max=(0.10, 0.05, 0.06),
            reach_surface_clearance_m=0.01,
            reach_mode=REACH_MODE_NEAREST_TOP_SURFACE,
        )

        self.assertEqual(offset, (-0.10, 0.0, 0.06999999999999999))

    def test_nearest_reach_offset_stays_on_bbox_footprint(self) -> None:
        offset = object_reach_offset_from_geometry(
            object_xy=(0.50, 0.20),
            robot_base_xy=(0.10, -0.20),
            bbox_min=(-0.20, -0.10, -0.03),
            bbox_max=(0.20, 0.10, 0.06),
            reach_surface_clearance_m=0.01,
            reach_mode=REACH_MODE_NEAREST_TOP_SURFACE,
        )

        self.assertLessEqual(abs(offset[0]), 0.20)
        self.assertAlmostEqual(offset[1], -0.10)
        self.assertEqual(offset[2], 0.06999999999999999)

    def test_changing_robot_side_changes_nearest_rim_side(self) -> None:
        left_offset = object_reach_offset_from_geometry(
            object_xy=(0.50, 0.20),
            robot_base_xy=(0.10, 0.20),
            bbox_min=(-0.10, -0.05, -0.03),
            bbox_max=(0.10, 0.05, 0.06),
            reach_surface_clearance_m=0.01,
            reach_mode=REACH_MODE_NEAREST_TOP_SURFACE,
        )
        right_offset = object_reach_offset_from_geometry(
            object_xy=(0.50, 0.20),
            robot_base_xy=(0.90, 0.20),
            bbox_min=(-0.10, -0.05, -0.03),
            bbox_max=(0.10, 0.05, 0.06),
            reach_surface_clearance_m=0.01,
            reach_mode=REACH_MODE_NEAREST_TOP_SURFACE,
        )

        self.assertEqual(left_offset[0], -0.10)
        self.assertEqual(right_offset[0], 0.10)

    def test_reaching_spec_uses_rim_point_for_container_targets(self) -> None:
        spec = make_reaching_episode_spec(
            base_spec=ReachingTaskSpec(object_pos_local=(0.58, -0.16, 1.08)),
            object_xy_offset=(0.0, 0.0),
            object_label="bowl",
            object_local_bbox_min=(-0.10, -0.05, -0.03),
            object_local_bbox_max=(0.10, 0.05, 0.06),
            object_category_id="bowl",
            object_affordances=("reachable", "container", "physical_container"),
            robot_base_xy=(0.10, -0.16),
        )

        self.assertEqual(spec.object_reach_offset_local, (-0.10, 0.0, 0.06999999999999999))

    def test_container_reaching_requires_robot_base_position(self) -> None:
        with self.assertRaisesRegex(ValueError, "robot_base_xy is required"):
            make_reaching_episode_spec(
                base_spec=ReachingTaskSpec(object_pos_local=(0.58, -0.16, 1.08)),
                object_xy_offset=(0.0, 0.0),
                object_label="bowl",
                object_local_bbox_min=(-0.10, -0.05, -0.03),
                object_local_bbox_max=(0.10, 0.05, 0.06),
                object_category_id="bowl",
                object_affordances=("reachable", "container", "physical_container"),
            )

    def test_reaching_spec_has_no_pick_place_orientation_fields(self) -> None:
        spec = ReachingTaskSpec()

        self.assertFalse(hasattr(spec, "pregrasp_height_m"))
        self.assertFalse(hasattr(spec, "open_finger_m"))
        self.assertFalse(hasattr(spec, "free_space_max_speed_m_s"))
        self.assertFalse(hasattr(spec, "approach_max_speed_m_s"))
        self.assertFalse(hasattr(spec, "grasp_closing_axis_xy"))
        self.assertFalse(hasattr(spec, "object_yaw_relevant"))
        self.assertFalse(hasattr(spec, "object_planar_minor_axis_local"))

    def test_reaching_sampling_stays_inside_workspace_on_both_sides(self) -> None:
        base_spec = ReachingTaskSpec()
        workspace = WorkspaceConstraint((0.10, 0.0), 0.65, 128)
        options = ReachingSamplingOptions(
            object_xy_range=XYRange(x=(-0.23, 0.37), y=(-0.39, 0.71)),
            object_origin_xy=base_spec.object_pos_local[:2],
            workspace=workspace,
            lighting=LightingOptions((650.0, 1200.0), ((1.0, 1.0, 1.0),)),
        )
        sampled_y = []

        for episode_id in range(100):
            sample = sample_reaching_offsets(123, episode_id, options)
            position = tuple(
                origin + offset
                for origin, offset in zip(
                    options.object_origin_xy,
                    sample.object_xy_offset,
                )
            )
            distance_m = (
                sum(
                    (coordinate - base_coordinate) ** 2
                    for coordinate, base_coordinate in zip(position, workspace.robot_base_xy)
                )
                ** 0.5
            )
            sampled_y.append(position[1])

            self.assertLessEqual(distance_m, workspace.max_distance_m)

        self.assertLess(min(sampled_y), 0.0)
        self.assertGreater(max(sampled_y), 0.0)


class TestPoseRandomizationConfigs(TestCase):
    def test_collection_configs_sample_target_on_both_sides_of_robot(self) -> None:
        config_paths = [
            Path("configs/collection.yaml"),
            Path("configs/collection_pick_place_headless_smoke.yaml"),
            Path("configs/collection_reaching.yaml"),
            Path("configs/collection_reaching_smoke.yaml"),
            *sorted(Path("configs/suites").glob("pick_place_*.yaml")),
        ]

        for config_path in config_paths:
            with self.subTest(config=config_path.as_posix()):
                config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
                base_y = (
                    ReachingTaskSpec().object_pos_local[1]
                    if config["task"] == "reaching"
                    else PickPlaceTaskSpec().object_pos_local[1]
                )
                y_range = config["pose_randomization"]["object_xy_range"]["y"]
                min_y = base_y + float(y_range[0])
                max_y = base_y + float(y_range[1])

                self.assertLess(min_y, 0.0)
                self.assertGreater(max_y, 0.0)

    def test_pick_place_configs_sample_receptacle_on_both_sides_of_robot(self) -> None:
        config_paths = [
            Path("configs/collection.yaml"),
            Path("configs/collection_pick_place_headless_smoke.yaml"),
            *sorted(Path("configs/suites").glob("pick_place_*.yaml")),
        ]

        for config_path in config_paths:
            with self.subTest(config=config_path.as_posix()):
                config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
                y_range = config["pose_randomization"]["place_xy_range"]["y"]
                min_y = PickPlaceTaskSpec().place_pos_local[1] + float(y_range[0])
                max_y = PickPlaceTaskSpec().place_pos_local[1] + float(y_range[1])

                self.assertLess(min_y, 0.0)
                self.assertGreater(max_y, 0.0)

    def test_pick_place_sampling_keeps_object_and_receptacle_separated(self) -> None:
        minimum_distance_m = 0.30
        base_spec = PickPlaceTaskSpec()
        options = PickPlaceSamplingOptions(
            object_origin_xy=base_spec.object_pos_local[:2],
            place_origin_xy=base_spec.place_pos_local[:2],
            object_xy_range=XYRange(x=(-0.23, 0.37), y=(-0.39, 0.71)),
            place_xy_range=XYRange(x=(-0.20, 0.40), y=(-0.77, 0.33)),
            minimum_object_place_distance_m=minimum_distance_m,
            workspace=WorkspaceConstraint((0.10, 0.0), 0.65, 128),
            lighting=LightingOptions(
                intensity_range=(650.0, 1200.0),
                color_options=((1.0, 1.0, 1.0),),
            ),
            visual=VisualRandomizationOptions(table_color_options=(TABLE_COLOR,)),
        )

        for episode_id in range(100):
            sample = sample_pick_place(seed=123, episode_id=episode_id, options=options)
            distance_m = (
                sum(
                    (object_origin + object_offset - place_origin - place_offset) ** 2
                    for object_origin, object_offset, place_origin, place_offset in zip(
                        options.object_origin_xy,
                        sample.object_xy_offset,
                        options.place_origin_xy,
                        sample.place_xy_offset,
                    )
                )
                ** 0.5
            )

            self.assertGreaterEqual(distance_m, minimum_distance_m)
            for origin_xy, offset in (
                (options.object_origin_xy, sample.object_xy_offset),
                (options.place_origin_xy, sample.place_xy_offset),
            ):
                radial_distance_m = (
                    sum(
                        (origin + delta - base) ** 2
                        for origin, delta, base in zip(
                            origin_xy,
                            offset,
                            options.workspace.robot_base_xy,
                        )
                    )
                    ** 0.5
                )
                self.assertLessEqual(
                    radial_distance_m,
                    options.workspace.max_distance_m,
                )
