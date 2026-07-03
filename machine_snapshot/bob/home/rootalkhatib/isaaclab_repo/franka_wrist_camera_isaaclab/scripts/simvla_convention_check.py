#!/usr/bin/env python3
"""Check converted IsaacLab SimVLA metadata and raw episode references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from franka_wrist_camera_scene.simvla.constants import DEFAULT_SIMVLA_CONVENTION, validate_image_rotation
from franka_wrist_camera_scene.simvla.replay_manifest import load_source_episode_refs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate local SimVLA/IsaacLab dataset conventions.")
    parser.add_argument("--converted-root", type=Path, default=Path("/home/utilisateur/isaac_dataset_lzf_parallel"))
    parser.add_argument("--image-rotation", default="rotate_180")
    parser.add_argument("--require-source-paths", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image_rotation = validate_image_rotation(args.image_rotation)
    convention = DEFAULT_SIMVLA_CONVENTION
    report_path = args.converted_root / "reports" / "raw_exact_verification_report.json"
    conversion_path = args.converted_root / "reports" / "conversion_report.json"
    refs = load_source_episode_refs(report_path)
    conversion = json.loads(conversion_path.read_text(encoding="utf-8"))
    if conversion.get("rgb_compression") != "lzf":
        raise RuntimeError(f"Expected lzf RGB compression, got {conversion.get('rgb_compression')!r}.")

    missing = [str(ref.source_episode_path) for ref in refs if not ref.source_episode_path.is_dir()]
    if missing and args.require_source_paths:
        raise FileNotFoundError(f"Missing {len(missing)} source episode directories. First: {missing[0]}")

    print(f"image_rotation: {image_rotation}")
    print(f"raw_rgb: {convention.source_height}x{convention.source_width}x3 uint8")
    print(f"crop: y={convention.crop_y0}:{convention.crop_y1}, x={convention.crop_x0}:{convention.crop_x1}")
    print(f"model_rgb: {convention.image_size}x{convention.image_size}x3")
    print(f"fps: {convention.camera_fps:g}, sim_dt: {convention.sim_dt}, camera_stride: {convention.camera_interval_steps}")
    print(f"num_actions: {convention.num_actions}, action_dim: 7, proprio_dim: 8")
    print(f"verified_demos: {len(refs)}")
    print(f"missing_source_episode_dirs: {len(missing)}")


if __name__ == "__main__":
    main()
