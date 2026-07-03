"""Exporter for image-language-action datasets."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_rgb_video(path: Path) -> np.ndarray:
    import cv2

    reader = cv2.VideoCapture(str(path))
    if not reader.isOpened():
        raise RuntimeError(f"Failed to open video file: {path}")

    frames = []
    try:
        while True:
            ok, frame_bgr = reader.read()
            if not ok:
                break
            frames.append(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB))
    finally:
        reader.release()

    if not frames:
        raise RuntimeError(f"Video contains no readable frames: {path}")
    return np.asarray(frames, dtype=np.uint8)


def _state_indices_for_camera_steps(traj: np.lib.npyio.NpzFile, camera_step_indices: np.ndarray) -> np.ndarray:
    if "state_step_indices" not in traj.files:
        return camera_step_indices

    state_step_indices = traj["state_step_indices"].astype(np.int64)
    positions = np.searchsorted(state_step_indices, camera_step_indices)
    if np.any(positions >= state_step_indices.shape[0]):
        raise RuntimeError(
            "Export requires state samples at every camera frame. "
            "Set state_record_fps equal to camera_fps or use state_record_stride matching camera_interval_steps."
        )
    if np.any(state_step_indices[positions] != camera_step_indices):
        raise RuntimeError(
            "Export requires state samples at every camera frame. "
            "Set state_record_fps equal to camera_fps or use state_record_stride matching camera_interval_steps."
        )
    return positions


def _load_training_rgb(raw_episode_dir: Path, traj: np.lib.npyio.NpzFile) -> tuple[np.ndarray, np.ndarray]:
    rgb_path = raw_episode_dir / "rgb.npz"
    if rgb_path.exists():
        with np.load(rgb_path) as rgb:
            return rgb["agent_rgb"], rgb["wrist_rgb"]
    if "agent_rgb" in traj.files and "wrist_rgb" in traj.files:
        return traj["agent_rgb"], traj["wrist_rgb"]

    wrist_video_path = raw_episode_dir / "wrist_camera.mp4"
    if not wrist_video_path.exists():
        raise RuntimeError(
            f"Training RGB is missing for {raw_episode_dir}. Expected rgb.npz or legacy wrist_camera.mp4."
        )
    return (
        _read_rgb_video(raw_episode_dir / "agent_camera.mp4"),
        _read_rgb_video(wrist_video_path),
    )


def export_episode(
    raw_collection_dir: Path,
    export_dir: Path,
    episode_entry: dict,
) -> dict:
    episode_id = int(episode_entry["episode_id"])
    raw_meta_path = raw_collection_dir / episode_entry["metadata_file"]
    raw_traj_path = raw_collection_dir / episode_entry["trajectory_file"]

    meta = load_json(raw_meta_path)
    raw_episode_dir = raw_meta_path.parent

    with np.load(raw_traj_path) as traj:
        idx = traj["camera_step_indices"].astype(np.int64)
        state_idx = _state_indices_for_camera_steps(traj, idx)
        ee_pos_w = traj["ee_pos_w"][state_idx]
        action_target_pos_w = traj["action_target_pos_w"][state_idx]
        delta_target_pos_w = action_target_pos_w - ee_pos_w
        agent_rgb, wrist_rgb = _load_training_rgb(raw_episode_dir, traj)

        arrays = {
            "agent_rgb": agent_rgb,
            "wrist_rgb": wrist_rgb,
            "ee_pos_w": ee_pos_w,
            "object_pos_w": traj["object_pos_w"][state_idx],
            "action_target_pos_w": action_target_pos_w,
            "action_target_quat_w": traj["action_target_quat_w"][state_idx],
            "action_delta_target_pos_w": delta_target_pos_w,
            "action_finger_opening_m": traj["action_finger_opening_m"][state_idx],
            "timestamps_s": traj["camera_timestamps_s"],
            "source_control_step_indices": idx,
        }

        depth_path = raw_episode_dir / "depth.npz"
        if depth_path.exists():
            with np.load(depth_path) as depth:
                arrays["agent_depth"] = depth["agent_depth"]
                arrays["wrist_depth"] = depth["wrist_depth"]
        elif "agent_depth" in traj.files and "wrist_depth" in traj.files:
            arrays["agent_depth"] = traj["agent_depth"]
            arrays["wrist_depth"] = traj["wrist_depth"]

        episode_file = export_dir / "episodes" / f"{episode_id:06d}.npz"
        np.savez_compressed(episode_file, **arrays)

    return {
        "episode_id": episode_id,
        "episode_file": f"episodes/{episode_id:06d}.npz",
        "source_episode_dir": episode_entry["episode_dir"],
        "instruction": meta["instruction"],
        "success": bool(meta["success"]),
        "num_frames": int(arrays["timestamps_s"].shape[0]),
        "object_pos_local": meta["object_pos_local"],
        "place_pos_local": meta["place_pos_local"],
        "object_category_id": meta.get("object_category_id"),
        "object_variant_id": meta.get("object_variant_id"),
        "object_label": meta.get("object_label"),
        "object_usd_path": meta.get("object_usd_path"),
        "object_grasp_strategy": meta.get("object_grasp_strategy"),
        "object_yaw_relevant": meta["object_yaw_relevant"],
        "object_planar_aspect_ratio": meta["object_planar_aspect_ratio"],
        "object_planar_minor_axis_local": meta["object_planar_minor_axis_local"],
        "object_planar_major_axis_local": meta["object_planar_major_axis_local"],
        "grasp_closing_axis_xy": meta["grasp_closing_axis_xy"],
        "placement_target_category_id": meta.get("placement_target_category_id"),
        "placement_target_variant_id": meta.get("placement_target_variant_id"),
        "placement_target_label": meta.get("placement_target_label"),
        "placement_target_usd_path": meta.get("placement_target_usd_path"),
        "placement_target_grasp_strategy": meta.get("placement_target_grasp_strategy"),
        "placement_target_pos_local": meta.get("placement_target_pos_local"),
        "light_intensity": meta.get("light_intensity"),
        "light_color": meta.get("light_color"),
        "clutter_objects": meta.get("clutter_objects"),
    }


def export_collection_to_ila(
    raw_collection_dir: Path,
    export_dir: Path,
) -> Path:
    raw_manifest_path = raw_collection_dir / "manifest.json"
    raw_manifest = load_json(raw_manifest_path)

    episodes_dir = export_dir / "episodes"
    episodes_dir.mkdir(parents=True, exist_ok=False)

    exported_episodes = [
        export_episode(raw_collection_dir, export_dir, episode_entry)
        for episode_entry in raw_manifest["episodes"]
    ]

    manifest = {
        "format_version": 1,
        "dataset_type": "image_language_action",
        "source_collection": str(raw_collection_dir),
        "task_name": raw_manifest["task_name"],
        "num_episodes": len(exported_episodes),
        "camera_names": ["agent_rgb", "wrist_rgb"],
        "action_space": "relative_cartesian_target_plus_gripper",
        "action_keys": [
            "action_delta_target_pos_w",
            "action_target_quat_w",
            "action_finger_opening_m",
        ],
        "state_keys": [
            "ee_pos_w",
            "object_pos_w",
        ],
        "observation_keys": [
            "agent_rgb",
            "wrist_rgb",
        ],
        "episodes": exported_episodes,
    }

    manifest_path = export_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest_path
