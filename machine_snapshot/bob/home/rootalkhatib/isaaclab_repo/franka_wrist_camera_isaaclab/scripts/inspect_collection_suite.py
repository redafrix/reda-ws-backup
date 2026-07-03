#!/usr/bin/env python3
"""Inspect a collection suite without importing or launching Isaac Lab."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

from franka_wrist_camera_scene.collection.configs import collection_configs_from_config
from franka_wrist_camera_scene.collection.preflight import validate_collection_config
from franka_wrist_camera_scene.objects.candidates import CandidatePool
from franka_wrist_camera_scene.utils.paths import load_yaml_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect and validate a collection suite.")
    parser.add_argument("collection_config")
    return parser.parse_args()


def _print_pool(pool: CandidatePool) -> None:
    print(
        f"{pool.name}: categories={len(pool.category_ids)} "
        f"variants={len(pool.candidates)}"
    )
    print(f"  category_ids: {', '.join(pool.category_ids)}")


def main() -> None:
    args = parse_args()
    collection_cfgs = collection_configs_from_config(load_yaml_config(args.collection_config))
    for idx, collection_cfg in enumerate(collection_cfgs):
        if idx:
            print()
        inspect_collection_config(args.collection_config, collection_cfg)


def inspect_collection_config(config_name: str, collection_cfg: dict) -> None:
    report = validate_collection_config(collection_cfg)
    suite = report.suite

    print(f"config: {config_name}")
    print(f"task: {collection_cfg['task']}")
    print(f"suite_name: {suite.name}")
    print(f"suite_split: {suite.split}")
    print(f"suite_difficulty: {suite.difficulty}")
    print(f"suite_tags: {', '.join(suite.tags or [])}")
    visual_randomization = collection_cfg.get("visual_randomization")
    if visual_randomization is not None:
        print("visual_randomization:")
        print(f"  table_color_options: {len(visual_randomization['table_color_options'])}")
    _print_pool(report.target_objects)
    if report.placement_targets is not None:
        _print_pool(report.placement_targets)
    if report.clutter is not None:
        _print_pool(report.clutter)
    if report.compatible_pairs:
        unique_pairs = len(set(report.compatible_pairs))
        print(
            f"compatible_pair_preflight: samples={len(report.compatible_pairs)} "
            f"unique_pairs={unique_pairs}"
        )
    print("status: valid")


if __name__ == "__main__":
    main()
