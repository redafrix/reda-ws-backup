#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

WORKSPACE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKSPACE / "src"))

from risk_collection.manifests import build_seen_manifest, subset_manifest  # noqa: E402
from risk_collection.storage import write_json_atomic  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-manifest",
        type=Path,
        default=Path(
            "/media/redafrix/My Passport/reaching_pose_v1_4400/train/manifest.json"
        ),
    )
    parser.add_argument(
        "--collection-config",
        type=Path,
        default=Path(
            "/mnt/ai/projects/simvla_reproduction_workspace/"
            "franka_wrist_camera_isaaclab/configs/collect_reaching_pose_v1_4400.yaml"
        ),
    )
    parser.add_argument("--output-dir", type=Path, default=WORKSPACE / "manifests")
    args = parser.parse_args()

    master, assignments = build_seen_manifest(
        args.source_manifest, args.collection_config
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json_atomic(args.output_dir / "seen_4000_master.json", master)
    for split in ("train", "calibration", "test"):
        write_json_atomic(
            args.output_dir / f"seen_{split}.json",
            subset_manifest(master, split),
        )
    write_json_atomic(
        args.output_dir / "seen_split_assignments.json",
        {
            "schema_version": "simvla_risk_seen_split_v1",
            "master_manifest_fingerprint_sha256": master[
                "manifest_fingerprint_sha256"
            ],
            "assignments": {
                f"{episode_id:06d}": split
                for episode_id, split in sorted(assignments.items())
            },
            "counts": dict(Counter(assignments.values())),
        },
    )
    print(f"MASTER_EPISODES={len(master['episodes'])}")
    print(
        "SPLIT_COUNTS="
        + json.dumps(dict(Counter(assignments.values())), sort_keys=True)
    )
    print(
        "MASTER_MANIFEST_FINGERPRINT="
        + master["manifest_fingerprint_sha256"]
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
