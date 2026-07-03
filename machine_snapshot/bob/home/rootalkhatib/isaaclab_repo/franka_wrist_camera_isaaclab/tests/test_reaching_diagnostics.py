import json
import tempfile
import unittest
from pathlib import Path

import numpy as np

from franka_wrist_camera_scene.simvla.reaching_diagnostics import diagnose_reaching_episode


class ReachingDiagnosticsTests(unittest.TestCase):
    def test_recompute_success_from_saved_reaching_episode(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "000016"
            episode_dir.mkdir()
            (episode_dir / "meta.json").write_text(
                json.dumps(
                    {
                        "instruction": "reach the avocado",
                        "success": False,
                        "success_mode": None,
                        "tcp_offset_local": [0.0, 0.0, 0.1],
                        "object_reach_offset_local": [0.0, 0.0, 0.02],
                        "reach_success_threshold_m": 0.01,
                        "max_success_target_displacement_m": 0.02,
                    }
                ),
                encoding="utf-8",
            )
            np.savez(
                episode_dir / "trajectory.npz",
                ee_pos_w=np.array([[[0.5, 0.0, 1.0]], [[0.6, 0.0, 1.0]]], dtype=np.float32),
                ee_quat_w=np.array([[[1.0, 0.0, 0.0, 0.0]], [[1.0, 0.0, 0.0, 0.0]]], dtype=np.float32),
                object_pos_w=np.array([[[0.6, 0.0, 1.08]], [[0.6, 0.0, 1.08]]], dtype=np.float32),
            )

            diagnostic = diagnose_reaching_episode(episode_dir)

        self.assertEqual(diagnostic.instruction, "reach the avocado")
        self.assertTrue(diagnostic.recomputed_success)
        self.assertTrue(diagnostic.reached_latched_target)
        self.assertAlmostEqual(diagnostic.latched_distance_m, 0.0, places=6)


if __name__ == "__main__":
    unittest.main()
