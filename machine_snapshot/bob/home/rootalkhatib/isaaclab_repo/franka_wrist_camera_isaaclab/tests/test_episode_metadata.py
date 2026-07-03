import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from franka_wrist_camera_scene.episode.manifest import write_collection_manifest
from franka_wrist_camera_scene.episode.schema import EpisodeMetadata
from franka_wrist_camera_scene.episode.suite import suite_metadata_from_config


SUITE_CONFIG = {
    "name": "pick_place_train_core",
    "split": "train",
    "difficulty": "core",
    "tags": ["pick_place", "rgbd"],
    "description": "Core training suite.",
}


class TestEpisodeMetadata(TestCase):
    def test_missing_suite_is_serialized_as_none(self) -> None:
        suite = suite_metadata_from_config({"task": "pick_place"})

        self.assertIsNone(suite.name)
        self.assertIsNone(suite.tags)

    def test_manifest_records_suite_and_randomization_metadata(self) -> None:
        with TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            episode_dir = output_dir / "000000"
            episode_dir.mkdir()
            metadata = EpisodeMetadata(
                episode_id=0,
                task_name="pick_place",
                instruction="pick up the apple and place it in the bowl",
                success=True,
                num_steps=10,
                sim_dt=0.01,
                seed=1000,
                camera_width=320,
                camera_height=240,
                camera_fps=15,
                suite_name=SUITE_CONFIG["name"],
                suite_split=SUITE_CONFIG["split"],
                suite_difficulty=SUITE_CONFIG["difficulty"],
                suite_tags=SUITE_CONFIG["tags"],
                suite_description=SUITE_CONFIG["description"],
                object_xy_offset=(0.01, -0.02),
                object_reach_offset_local=(0.0, 0.0, 0.04),
                reach_success_threshold_m=0.02,
                place_xy_offset=(-0.03, 0.04),
                object_category_id="apple",
                object_variant_id="apple00",
                object_label="apple",
                placement_target_category_id="bowl",
                placement_target_variant_id="bowl00",
                placement_target_label="bowl",
                light_intensity=900.0,
                light_color=(1.0, 0.92, 0.84),
                table_color=(0.35, 0.35, 0.35),
                active_clutter_count=1,
                clutter_objects=[{"category_id": "plate", "variant_id": "plate00"}],
            )
            metadata.save(episode_dir / "meta.json")

            manifest_path = write_collection_manifest(
                output_dir,
                {
                    "task": "pick_place",
                    "suite": SUITE_CONFIG,
                    "camera_width": 320,
                    "camera_height": 240,
                    "camera_fps": 15,
                },
                [episode_dir],
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        self.assertEqual(manifest["suite_name"], "pick_place_train_core")
        self.assertEqual(manifest["suite_tags"], ["pick_place", "rgbd"])
        self.assertEqual(manifest["episodes"][0]["active_clutter_count"], 1)
        self.assertEqual(manifest["episodes"][0]["object_xy_offset"], [0.01, -0.02])
        self.assertEqual(manifest["episodes"][0]["object_reach_offset_local"], [0.0, 0.0, 0.04])
        self.assertEqual(manifest["episodes"][0]["reach_success_threshold_m"], 0.02)
        self.assertEqual(manifest["episodes"][0]["placement_target_category_id"], "bowl")
        self.assertEqual(manifest["camera_width"], 320)
        self.assertEqual(manifest["camera_height"], 240)
        self.assertEqual(manifest["camera_fps"], 15)
        self.assertEqual(manifest["episodes"][0]["camera_width"], 320)
        self.assertEqual(manifest["episodes"][0]["camera_height"], 240)
        self.assertEqual(manifest["episodes"][0]["camera_fps"], 15)
        self.assertEqual(manifest["episodes"][0]["table_color"], [0.35, 0.35, 0.35])

    def test_manifest_without_suite_keeps_none_fields(self) -> None:
        with TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            episode_dir = output_dir / "000000"
            episode_dir.mkdir()
            EpisodeMetadata(
                episode_id=0,
                task_name="reaching",
                instruction="reach the apple",
                success=False,
                num_steps=5,
                sim_dt=0.01,
            ).save(episode_dir / "meta.json")

            failure_json = {
                "task_name": "reaching",
                "final_tcp_distance_to_latched_target_m": 0.123
            }
            (episode_dir / "failure.json").write_text(json.dumps(failure_json), encoding="utf-8")

            manifest_path = write_collection_manifest(
                output_dir,
                {"task": "reaching", "camera_fps": 30},
                [episode_dir],
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        self.assertIsNone(manifest["suite_name"])
        self.assertIsNone(manifest["episodes"][0]["suite_name"])
