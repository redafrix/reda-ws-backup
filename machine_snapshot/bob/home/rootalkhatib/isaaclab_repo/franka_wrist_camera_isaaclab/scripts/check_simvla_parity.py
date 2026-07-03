#!/usr/bin/env python3
"""Golden parity check for raw IsaacLab episodes versus converted SimVLA HDF5."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from franka_wrist_camera_scene.simvla.constants import validate_image_rotation
from franka_wrist_camera_scene.simvla.parity import check_ref_parity
from franka_wrist_camera_scene.simvla.replay_manifest import load_source_episode_refs, validate_source_episode_refs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check SimVLA input/action parity on one verified converted demo.")
    parser.add_argument(
        "--raw-exact-report",
        type=Path,
        default=Path("/home/utilisateur/isaac_dataset_lzf_parallel/reports/raw_exact_verification_report.json"),
    )
    parser.add_argument("--ref-index", type=int, default=0)
    parser.add_argument("--frame-index", type=int, default=0)
    parser.add_argument("--image-rotation", default="rotate_180")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image_rotation = validate_image_rotation(args.image_rotation)
    refs = load_source_episode_refs(args.raw_exact_report)
    validate_source_episode_refs(refs, require_existing_paths=True)
    if args.ref_index < 0 or args.ref_index >= len(refs):
        raise IndexError(f"--ref-index must be in [0, {len(refs) - 1}], got {args.ref_index}.")
    result = check_ref_parity(refs[args.ref_index], args.frame_index, image_rotation)
    result.assert_within_tolerance()
    payload = result.to_dict()
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    for key, value in payload.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
