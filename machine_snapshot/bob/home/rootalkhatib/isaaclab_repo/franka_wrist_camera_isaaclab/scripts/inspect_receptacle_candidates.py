#!/usr/bin/env python3
"""Inspect object catalog for physical container receptacle candidates."""

from __future__ import annotations

from pathlib import Path
import sys
import yaml

REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

from franka_wrist_camera_scene.objects.catalog import load_object_catalog
from franka_wrist_camera_scene.objects.selection import variant_affordances, variant_grasp_strategy
from franka_wrist_camera_scene.utils.paths import REPO_ROOT


def main() -> None:
    collection_cfg_path = REPO_ROOT / "configs" / "collection.yaml"
    if not collection_cfg_path.exists():
        raise FileNotFoundError(f"Missing collection config: {collection_cfg_path}")

    collection_cfg = yaml.safe_load(collection_cfg_path.read_text())
    placement_cfg = collection_cfg.get("placement_target", {})
    catalog_config = placement_cfg.get("catalog_config", "object_catalog.generated.yaml")

    catalog = load_object_catalog(catalog_config)

    print("physical receptacle candidates:")
    print("Only variants tagged with physical_container are eligible for placement targets.")
    candidates_count = 0

    for category in catalog.categories:
        if category.role != "target":
            continue

        for variant in category.variants:
            affs = set(variant_affordances(category, variant))
            strategy = variant_grasp_strategy(category, variant)

            if "container" in affs and "physical_container" in affs and strategy == "unsupported":
                # Print relative path to objects directory
                rel_usd_path = variant.usd_path.relative_to(catalog.asset_root).as_posix()
                print(f"  {category.id}/{variant.id} -> objects/{rel_usd_path}")
                candidates_count += 1

    if candidates_count == 0:
        raise RuntimeError("No physical receptacle candidates found.")


if __name__ == "__main__":
    main()
