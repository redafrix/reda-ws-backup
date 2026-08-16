from __future__ import annotations

from collections import Counter
import json
import math
from pathlib import Path
import unittest

from risk_collection.manifests import build_seen_manifest
from risk_collection.rounds import (
    ROUND_SCHEDULE_VERSION,
    balanced_round_robin_order,
    global_episode_id,
    scene_family_id,
    schedule_sha256,
)


class ManifestsCpuTest(unittest.TestCase):
    def test_seen_manifest_is_deterministic_and_disjoint(self) -> None:
        source = Path(
            "/media/redafrix/My Passport/reaching_pose_v1_4400/train/manifest.json"
        )
        config = Path(
            "/mnt/ai/projects/simvla_reproduction_workspace/"
            "franka_wrist_camera_isaaclab/configs/collect_reaching_pose_v1_4400.yaml"
        )
        first, assignments_a = build_seen_manifest(source, config)
        second, assignments_b = build_seen_manifest(source, config)
        self.assertEqual(
            first["manifest_fingerprint_sha256"],
            second["manifest_fingerprint_sha256"],
        )
        self.assertEqual(assignments_a, assignments_b)
        self.assertEqual(len(first["episodes"]), 4000)
        self.assertEqual(len(assignments_a), 4000)
        self.assertEqual(len(set(assignments_a)), 4000)
        counts = Counter(assignments_a.values())
        self.assertEqual(sum(counts.values()), 4000)
        self.assertEqual(set(counts), {"train", "calibration", "test"})
        self.assertGreater(counts["train"], counts["calibration"])
        self.assertGreater(counts["train"], counts["test"])
        self.assertEqual(
            first["provenance"]["source_manifest_sha256"],
            "32261a82df8e015b13931afaf3b9f8de2f59b30980fc5e57833166fad0a3ffd6",
        )
        order_a = balanced_round_robin_order(first["episodes"])
        order_b = balanced_round_robin_order(second["episodes"])
        self.assertEqual(order_a, order_b)
        self.assertEqual(len(order_a), 4000)
        self.assertEqual(set(order_a), set(range(4000)))
        self.assertEqual(
            schedule_sha256(order_a),
            schedule_sha256(order_b, version=ROUND_SCHEDULE_VERSION),
        )
        entries_by_id = {
            int(item["benchmark_episode_id"]): item for item in first["episodes"]
        }
        first_hundred = [entries_by_id[value] for value in order_a[:100]]
        distance_bins = {
            min(
                7,
                int(
                    math.hypot(*item["scene"]["object_xy_offset"])
                    / 0.05
                ),
            )
            for item in first_hundred
        }
        self.assertEqual(distance_bins, set(range(8)))
        self.assertEqual(
            {
                item["scene"]["target"]["source_name"]
                for item in first_hundred
            },
            {"pickable_targets", "receptacle_targets"},
        )
        self.assertEqual(
            {len(item["scene"]["clutter"]) for item in first_hundred},
            {4, 5, 6},
        )
        self.assertEqual(global_episode_id(0, 4196), "r000_s004196")
        fingerprint = first["episodes"][0]["scene_fingerprint_sha256"]
        self.assertEqual(scene_family_id(fingerprint), f"scene_sha256:{fingerprint}")
        json.dumps(first)


if __name__ == "__main__":
    unittest.main()
