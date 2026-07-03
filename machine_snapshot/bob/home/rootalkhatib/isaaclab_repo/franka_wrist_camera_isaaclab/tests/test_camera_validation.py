from unittest import TestCase

import numpy as np

from franka_wrist_camera_scene.episode.camera_validation import (
    rgb_frame_stats,
    validate_camera_recordings,
    validate_visible_rgb_frames,
)


class CameraValidationTest(TestCase):
    def test_rgb_frame_stats_summarizes_visible_frames(self) -> None:
        frames = [np.full((2, 2, 3), 32, dtype=np.uint8)]

        stats = rgb_frame_stats("agent_camera", frames)

        self.assertEqual(stats.frame_count, 1)
        self.assertEqual(stats.min_value, 32)
        self.assertEqual(stats.max_value, 32)
        self.assertEqual(stats.mean_value, 32.0)

    def test_validate_visible_rgb_frames_rejects_black_frames(self) -> None:
        stats = rgb_frame_stats("wrist_camera", [np.zeros((2, 2, 3), dtype=np.uint8)])

        with self.assertRaisesRegex(RuntimeError, "appear black"):
            validate_visible_rgb_frames(stats)

    def test_validate_visible_rgb_frames_rejects_white_frames(self) -> None:
        stats = rgb_frame_stats("wrist_camera", [np.full((2, 2, 3), 255, dtype=np.uint8)])

        with self.assertRaisesRegex(RuntimeError, "appear white"):
            validate_visible_rgb_frames(stats)

    def test_validate_camera_recordings_requires_both_cameras(self) -> None:
        visible = [np.full((2, 2, 3), 64, dtype=np.uint8)]
        black = [np.zeros((2, 2, 3), dtype=np.uint8)]

        with self.assertRaisesRegex(RuntimeError, "wrist_camera"):
            validate_camera_recordings(visible, black)
