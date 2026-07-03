#!/usr/bin/env python3
"""Collect deterministic pick-place episodes in the tabletop scene."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

# Import launcher to apply Isaac Sim 6.0 and pxr compatibility patches before importing isaaclab
from franka_wrist_camera_scene.app import launcher  # noqa: F401
from isaaclab.app import AppLauncher  # noqa: E402
from franka_wrist_camera_scene.utils.paths import load_yaml_config  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect deterministic pick-and-place tabletop episodes.")
    parser.add_argument(
        "--collection_config",
        type=str,
        default="collection.yaml",
        help="Collection config file under configs/.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=None,
        help="Override output directory.",
    )
    # Add app launcher arguments
    AppLauncher.add_app_launcher_args(parser)
    args = parser.parse_args()
    args.enable_cameras = True
    args.kit_args = f"{args.kit_args} --/rtx/hydra/readTransformsFromFabricInRenderDelegate=false".strip()
    return args


def preflight_collection_output(collection_cfg: dict) -> None:
    """Preflight check on output paths before launching simulator."""
    output_dir = Path(collection_cfg["output_dir"])
    start_episode_id = int(collection_cfg["start_episode_id"])
    num_episodes = int(collection_cfg["num_episodes"])

    for episode_id in range(start_episode_id, start_episode_id + num_episodes):
        episode_dir = output_dir / f"{episode_id:06d}"
        if episode_dir.exists():
            raise FileExistsError(f"Episode directory already exists: {episode_dir}")

    manifest_path = output_dir / "manifest.json"
    if manifest_path.exists():
        raise FileExistsError(f"Collection manifest already exists: {manifest_path}")


def preflight_feasibility_check(collection_cfg: dict) -> None:
    """Preflight check on geometry and physical feasibility before launching simulator."""
    target_object_cfg = collection_cfg.get("target_object")
    placement_target_cfg = collection_cfg.get("placement_target")
    
    if target_object_cfg is None:
        return
        
    obj_cat = target_object_cfg.get("category_id")
    obj_var = target_object_cfg.get("variant_id")
    
    rec_cat = None
    rec_var = None
    if placement_target_cfg is not None:
        rec_cat = placement_target_cfg.get("category_id")
        rec_var = placement_target_cfg.get("variant_id")

    # If they are explicit (not sample), check feasibility
    if obj_cat != "sample" and obj_var != "sample":
        if rec_cat != "sample" and rec_var != "sample":
            from franka_wrist_camera_scene.validation.pick_place_preflight import validate_pick_place_pair
            res = validate_pick_place_pair(
                object_category_id=obj_cat,
                object_variant_id=obj_var,
                receptacle_category_id=rec_cat,
                receptacle_variant_id=rec_var,
                collection_policy=collection_cfg.get("collection_policy"),
                preflight_cfg=collection_cfg.get("preflight"),
            )
            if not res.accepted:
                raise ValueError(f"PREFLIGHT_REJECTED: {res.code} - {res.reason}")


def main() -> None:
    args_cli = parse_args()
    collection_cfg = load_yaml_config(args_cli.collection_config)
    if args_cli.output_dir is not None:
        collection_cfg["output_dir"] = args_cli.output_dir
    preflight_collection_output(collection_cfg)
    preflight_feasibility_check(collection_cfg)

    app_launcher = AppLauncher(args_cli)
    simulation_app = app_launcher.app
    launcher.patch_physx_schema()

    task = collection_cfg["task"]
    if task == "reaching":
        from franka_wrist_camera_scene.collection.reaching import collect_reaching_dataset
        collect_reaching_dataset(
            collection_cfg=collection_cfg,
            device=args_cli.device,
            simulation_app=simulation_app,
        )
    elif task == "pick_place":
        from franka_wrist_camera_scene.collection.pick_place import collect_pick_place_dataset
        collect_pick_place_dataset(
            collection_cfg=collection_cfg,
            device=args_cli.device,
            simulation_app=simulation_app,
        )
    else:
        raise ValueError(f"Unsupported collection task: {task!r}")

    # Spawn a daemon thread to force exit if closing simulation app hangs.
    import os
    import threading
    import time

    def force_exit():
        time.sleep(2.0)
        os._exit(0)

    t = threading.Thread(target=force_exit, daemon=True)
    t.start()

    simulation_app.close()
    os._exit(0)


if __name__ == "__main__":
    main()
