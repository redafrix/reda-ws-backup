#!/usr/bin/env python3
"""Collect deterministic pick-place episodes in the tabletop scene."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

# Import launcher before Isaac Lab modules so compatibility patches are registered.
from franka_wrist_camera_scene.app import launcher  # noqa: F401
from isaaclab.app import AppLauncher  # noqa: E402
from franka_wrist_camera_scene.collection.configs import collection_configs_from_config  # noqa: E402
from franka_wrist_camera_scene.collection.preflight import validate_collection_config  # noqa: E402
from franka_wrist_camera_scene.episode.manifest import write_collection_manifest  # noqa: E402
from franka_wrist_camera_scene.utils.paths import load_yaml_config  # noqa: E402


FABRIC_RENDER_TRANSFORM_SETTING = "/rtx/hydra/readTransformsFromFabricInRenderDelegate"
SKIP_COLLECTION_MANIFEST_KEY = "_skip_collection_manifest"
CHILD_INTERRUPT_TIMEOUT_S = 20.0
CHILD_TERMINATE_TIMEOUT_S = 10.0


def _append_kit_arg(existing: str, *tokens: str) -> str:
    parts = existing.split() if existing else []
    parts.extend(tokens)
    return " ".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect deterministic pick-and-place tabletop episodes.")
    parser.add_argument(
        "--collection_config",
        type=str,
        default="collection.yaml",
        help="Collection config file under configs/.",
    )
    parser.add_argument(
        "--allow_fabric_render_transforms",
        action="store_true",
        help=(
            "Allow RTX Hydra to read transforms directly from Fabric. By default this is disabled because Isaac "
            "Sim warns that this path can drop dynamic robot geometry when geometry streaming is active."
        ),
    )
    parser.add_argument(
        "--disable_collection_sharding",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    # Add app launcher arguments
    AppLauncher.add_app_launcher_args(parser)
    args = parser.parse_args()
    args.enable_cameras = True
    if not args.allow_fabric_render_transforms:
        args.kit_args = _append_kit_arg(args.kit_args, f"--{FABRIC_RENDER_TRANSFORM_SETTING}=false")
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

    if not collection_cfg.get(SKIP_COLLECTION_MANIFEST_KEY, False):
        manifest_path = output_dir / "manifest.json"
        if manifest_path.exists():
            raise FileExistsError(f"Collection manifest already exists: {manifest_path}")


def _configured_asset_bank_episode_batch_size(collection_cfg: dict) -> int:
    batch_size = int(collection_cfg.get("asset_bank_episode_batch_size", 8))
    if batch_size <= 0:
        raise ValueError(f"asset_bank_episode_batch_size must be positive, got {batch_size}.")
    return batch_size


def _requires_camera_process_sharding(collection_cfg: dict) -> bool:
    if not bool(collection_cfg.get("record_cameras", False)):
        return False
    return _configured_asset_bank_episode_batch_size(collection_cfg) < int(collection_cfg["num_episodes"])


def _child_passthrough_args(argv: list[str]) -> list[str]:
    passthrough: list[str] = []
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg == "--collection_config":
            index += 2
            continue
        if arg.startswith("--collection_config="):
            index += 1
            continue
        if arg == "--disable_collection_sharding":
            index += 1
            continue
        passthrough.append(arg)
        index += 1
    return passthrough


def _write_shard_config(path: Path, collection_cfg: dict, start_episode_id: int, num_episodes: int) -> None:
    shard_cfg = dict(collection_cfg)
    shard_cfg["start_episode_id"] = start_episode_id
    shard_cfg["num_episodes"] = num_episodes
    shard_cfg[SKIP_COLLECTION_MANIFEST_KEY] = True
    path.write_text(json.dumps(shard_cfg, indent=2), encoding="utf-8")


def _run_child_collection(config_path: Path, passthrough_args: list[str]) -> None:
    cmd = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--collection_config",
        str(config_path),
        "--disable_collection_sharding",
        *passthrough_args,
    ]
    child = subprocess.Popen(cmd, start_new_session=True)
    try:
        return_code = child.wait()
    except KeyboardInterrupt:
        _terminate_child_process_group(child)
        raise
    if return_code != 0:
        raise subprocess.CalledProcessError(return_code, cmd)


def _wait_for_child_exit(child: subprocess.Popen, timeout_s: float) -> bool:
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        if child.poll() is not None:
            return True
        time.sleep(0.1)
    return child.poll() is not None


def _terminate_child_process_group(child: subprocess.Popen) -> None:
    """Forward Ctrl-C to the active shard and escalate if Isaac/Kit keeps running."""
    if child.poll() is not None:
        return

    try:
        pgid = os.getpgid(child.pid)
    except ProcessLookupError:
        return

    print("[INFO] Ctrl-C received; stopping active collection shard...", flush=True)
    for sig, timeout_s, label in (
        (signal.SIGINT, CHILD_INTERRUPT_TIMEOUT_S, "SIGINT"),
        (signal.SIGTERM, CHILD_TERMINATE_TIMEOUT_S, "SIGTERM"),
    ):
        try:
            os.killpg(pgid, sig)
        except ProcessLookupError:
            return
        if _wait_for_child_exit(child, timeout_s):
            return
        print(f"[WARN] Child collection shard did not stop after {label}; escalating.", flush=True)

    try:
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        return
    child.wait()


def run_process_sharded_collections(collection_cfgs: list[dict], passthrough_args: list[str]) -> None:
    """Run camera collections in process shards to avoid renderer teardown and huge PhysX scenes."""
    with tempfile.TemporaryDirectory(prefix="franka_collection_shards_") as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        for config_index, collection_cfg in enumerate(collection_cfgs):
            output_dir = Path(collection_cfg["output_dir"])
            start_episode_id = int(collection_cfg["start_episode_id"])
            num_episodes = int(collection_cfg["num_episodes"])

            if not _requires_camera_process_sharding(collection_cfg):
                config_path = tmp_dir / f"collection_{config_index:02d}.json"
                config_path.write_text(json.dumps(collection_cfg, indent=2), encoding="utf-8")
                _run_child_collection(config_path, passthrough_args)
                continue

            batch_size = _configured_asset_bank_episode_batch_size(collection_cfg)
            shard_ranges = [
                (episode_id, min(batch_size, start_episode_id + num_episodes - episode_id))
                for episode_id in range(start_episode_id, start_episode_id + num_episodes, batch_size)
            ]
            print(
                "[INFO] Camera recording enabled; running collection in "
                f"{len(shard_ranges)} process shards of up to {batch_size} episodes. "
                "Each shard uses one Isaac scene, avoiding in-process RTX teardown and large all-episode asset banks.",
                flush=True,
            )
            for shard_index, (shard_start, shard_count) in enumerate(shard_ranges):
                config_path = tmp_dir / f"collection_{config_index:02d}_shard_{shard_index:04d}.json"
                _write_shard_config(config_path, collection_cfg, shard_start, shard_count)
                print(
                    f"[INFO] Starting process shard {shard_index + 1}/{len(shard_ranges)} "
                    f"episodes {shard_start}-{shard_start + shard_count - 1}",
                    flush=True,
                )
                _run_child_collection(config_path, passthrough_args)
                for episode_id in range(shard_start, shard_start + shard_count):
                    meta_path = output_dir / f"{episode_id:06d}" / "meta.json"
                    if not meta_path.exists():
                        raise RuntimeError(
                            "Collection shard finished without writing expected metadata: "
                            f"{meta_path}"
                        )

            episode_dirs = [
                output_dir / f"{episode_id:06d}"
                for episode_id in range(start_episode_id, start_episode_id + num_episodes)
            ]
            manifest_path = write_collection_manifest(
                output_dir=output_dir,
                collection_cfg=collection_cfg,
                episode_dirs=episode_dirs,
            )
            print(f"[INFO] Saved sharded collection manifest to: {manifest_path}", flush=True)


def main() -> None:
    args_cli = parse_args()
    collection_cfgs = collection_configs_from_config(load_yaml_config(args_cli.collection_config))
    for collection_cfg in collection_cfgs:
        preflight_collection_output(collection_cfg)
        validate_collection_config(collection_cfg)

    if not args_cli.disable_collection_sharding and any(
        _requires_camera_process_sharding(collection_cfg) for collection_cfg in collection_cfgs
    ):
        run_process_sharded_collections(
            collection_cfgs=collection_cfgs,
            passthrough_args=_child_passthrough_args(sys.argv[1:]),
        )
        return

    app_launcher = AppLauncher(args_cli)
    simulation_app = app_launcher.app
    launcher.patch_physx_schema()

    for collection_cfg in collection_cfgs:
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

    simulation_app.close()


if __name__ == "__main__":
    main()
