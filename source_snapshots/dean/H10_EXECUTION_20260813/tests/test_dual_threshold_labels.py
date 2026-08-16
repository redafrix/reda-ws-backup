import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts/build_dual_threshold_labels.py"


def summary(episode_id: str, source_id: int, success: bool) -> dict:
    return {
        "episode_id": episode_id,
        "source_episode_id": source_id,
        "instruction": "reach the apple",
        "scene_fingerprint_sha256": f"scene-{source_id}",
        "minimum_tcp_distance_m": 0.019 if success else 0.021,
        "outcome": "success" if success else "failure_or_timeout",
        "risk_label": 0 if success else 1,
        "strict_success_threshold_m": 0.02,
        "settle_time_s": 0.2,
        "simulation_steps": 500 if success else 2400,
        "synthetic_smoke": False,
        "training_eligible": True,
    }


class DualThresholdLabelsTest(unittest.TestCase):
    def test_strict_success_and_operational_near_miss_are_distinct(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            round_root = root / "round"
            for episode_id, source_id, success in (
                ("r000_s000001", 1, True),
                ("r000_s000002", 2, False),
            ):
                path = round_root / "episodes" / episode_id / "summary.json"
                path.parent.mkdir(parents=True)
                path.write_text(json.dumps(summary(episode_id, source_id, success)))
            replay = root / "replay.json"
            replay.write_text(
                json.dumps(
                    {
                        "episodes": [
                            {
                                "source_episode_id": 2,
                                "exact_saved_executed_actions_used": True,
                                "policy_resampled": False,
                                "required_consecutive_physics_frames": 24,
                                "original_outcome": "failure_or_timeout",
                                "scene_fingerprint_sha256": "scene-2",
                                "simulation_steps": 2400,
                                "counterfactual_4cm_dwell_success": True,
                                "maximum_consecutive_counterfactual_4cm_frames": 25,
                            }
                        ]
                    }
                )
            )
            labels = root / "labels.jsonl"
            report = root / "report.json"
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(round_root),
                    "--failure-replay-report",
                    str(replay),
                    "--output-jsonl",
                    str(labels),
                    "--summary-json",
                    str(report),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            rows = [json.loads(line) for line in labels.read_text().splitlines()]
            self.assertEqual(rows[0]["classification"], "success_both_thresholds")
            self.assertEqual(rows[1]["strict_2cm_risk_label"], 1)
            self.assertEqual(rows[1]["operational_4cm_risk_label"], 0)
            self.assertIn("precision_near_miss", rows[1]["classification"])
            result = json.loads(report.read_text())
            self.assertEqual(result["strict_2cm_failures"], 1)
            self.assertEqual(result["operational_4cm_failures"], 0)


if __name__ == "__main__":
    unittest.main()
