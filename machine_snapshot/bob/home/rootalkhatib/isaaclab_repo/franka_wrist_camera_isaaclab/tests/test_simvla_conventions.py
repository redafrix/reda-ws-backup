import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
from scipy.spatial.transform import Rotation as R

from franka_wrist_camera_scene.simvla.constants import (
    DEFAULT_SIMVLA_CONVENTION,
    IMAGE_ROTATION_180,
    IMAGE_ROTATION_NONE,
    validate_image_rotation,
)
from franka_wrist_camera_scene.simvla.geometry import (
    SimVLAProprioSource,
    decode_simvla_action,
    encode_simvla_proprio,
    euler_xyz_to_axis_angle,
    libero_euler_xyz_from_rotation,
    quat_xyzw_to_wxyz,
)
from franka_wrist_camera_scene.simvla.image_preprocessing import (
    preprocess_camera_views,
    preprocess_rgb_uint8,
)
from franka_wrist_camera_scene.simvla.replay_manifest import load_source_episode_refs


class SimVLAConventionTests(unittest.TestCase):
    def test_rotation_mode_validation(self) -> None:
        self.assertEqual(validate_image_rotation(IMAGE_ROTATION_NONE), IMAGE_ROTATION_NONE)
        self.assertEqual(validate_image_rotation(IMAGE_ROTATION_180), IMAGE_ROTATION_180)
        with self.assertRaises(ValueError):
            validate_image_rotation("flip")

    def test_preprocess_shapes_and_180_rotation(self) -> None:
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        frame[:, :, 0] = np.arange(640, dtype=np.uint8)[None, :]
        frame[:, :, 1] = np.arange(480, dtype=np.uint8)[:, None]

        unrotated = preprocess_rgb_uint8(frame, IMAGE_ROTATION_NONE)
        rotated = preprocess_rgb_uint8(frame, IMAGE_ROTATION_180)

        self.assertEqual(unrotated.shape, (384, 384, 3))
        self.assertEqual(unrotated.dtype, np.uint8)
        np.testing.assert_array_equal(rotated[0, 0], unrotated[-1, -1])
        np.testing.assert_array_equal(rotated[-1, -1], unrotated[0, 0])

    def test_camera_views_match_simvla_batch_shape(self) -> None:
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        batch = preprocess_camera_views(frame, frame, IMAGE_ROTATION_NONE)

        self.assertEqual(tuple(batch.image_input.shape), (1, 3, 3, 384, 384))
        self.assertEqual(tuple(batch.image_mask.shape), (1, 3))
        self.assertEqual(batch.image_mask.tolist(), [[True, True, False]])
        self.assertTrue(float(batch.image_input[:, 2].abs().sum()) == 0.0)

    def test_proprio_uses_libero_roll_branch_and_signed_gripper(self) -> None:
        rot = R.from_euler("xyz", (-2.9, 0.2, -0.1))
        source = SimVLAProprioSource(
            ee_pos_w=np.array([1.2, 0.4, 1.5]),
            ee_quat_wxyz=quat_xyzw_to_wxyz(rot.as_quat()),
            env_origin_w=np.array([0.5, -0.1, 0.0]),
            commanded_finger_opening_m=0.032,
        )

        proprio = encode_simvla_proprio(source)
        expected_euler = libero_euler_xyz_from_rotation(rot)
        expected_axis_angle = euler_xyz_to_axis_angle(expected_euler)

        self.assertEqual(proprio.shape, (8,))
        np.testing.assert_allclose(proprio[:3], [0.7, 0.5, 1.5], atol=1e-6)
        np.testing.assert_allclose(proprio[3:6], expected_axis_angle, atol=1e-6)
        np.testing.assert_allclose(proprio[6:], [0.032, -0.032], atol=1e-6)
        self.assertGreater(expected_euler[0], 0.0)

    def test_decode_action_reverses_conversion_scale(self) -> None:
        ee_pos = np.array([0.6, -0.2, 1.2])
        current = R.from_euler("xyz", (0.1, -0.2, 0.3))
        action = np.array([1.0, -2.0, 0.5, 0.2, -0.4, 0.6, 1.0], dtype=np.float32)

        decoded = decode_simvla_action(action, ee_pos, quat_xyzw_to_wxyz(current.as_quat()))
        target_rot = R.from_quat(decoded.target_quat_wxyz[[1, 2, 3, 0]])
        expected_rot = R.from_euler("xyz", action[3:6] * 0.5) * current

        np.testing.assert_allclose(decoded.target_pos_w, [0.65, -0.3, 1.225], atol=1e-6)
        np.testing.assert_allclose(target_rot.as_matrix(), expected_rot.as_matrix(), atol=1e-6)
        self.assertEqual(decoded.finger_opening_m, DEFAULT_SIMVLA_CONVENTION.closed_finger_m)

    def test_decode_action_opens_on_negative_gripper(self) -> None:
        decoded = decode_simvla_action(
            np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]),
            np.zeros(3),
            np.array([1.0, 0.0, 0.0, 0.0]),
        )
        self.assertEqual(decoded.finger_opening_m, DEFAULT_SIMVLA_CONVENTION.open_finger_m)

    def test_manifest_loader_preserves_hdf5_demo_and_source_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report_path = Path(tmp) / "raw_exact_verification_report.json"
            report_path.write_text(
                json.dumps(
                    {
                        "files": [
                            {
                                "path": "/tmp/shard.hdf5",
                                "verified_demos": [
                                    {
                                        "demo": "demo_3",
                                        "source_episode_path": "/tmp/raw/000003",
                                        "timesteps": 17,
                                    }
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            refs = load_source_episode_refs(report_path)

        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].demo, "demo_3")
        self.assertEqual(refs[0].hdf5_path, Path("/tmp/shard.hdf5"))
        self.assertEqual(refs[0].source_episode_path, Path("/tmp/raw/000003"))
        self.assertEqual(refs[0].timesteps, 17)

    def test_manifest_loader_rejects_duplicate_demo_refs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report_path = Path(tmp) / "raw_exact_verification_report.json"
            report_path.write_text(
                json.dumps(
                    {
                        "files": [
                            {
                                "path": "/tmp/shard.hdf5",
                                "verified_demos": [
                                    {"demo": "demo_3", "source_episode_path": "/tmp/raw/000003", "timesteps": 17},
                                    {"demo": "demo_3", "source_episode_path": "/tmp/raw/000004", "timesteps": 18},
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(ValueError):
                load_source_episode_refs(report_path)


if __name__ == "__main__":
    unittest.main()
