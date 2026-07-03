"""Offline diagnostics for reaching success scoring."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

import numpy as np
from scipy.spatial.transform import Rotation as R

from franka_wrist_camera_scene.simvla.geometry import quat_wxyz_to_xyzw


@dataclass(frozen=True, slots=True)
class ReachingEpisodeDiagnostic:
    episode_dir: str
    instruction: str
    success_in_meta: bool
    success_mode_in_meta: str | None
    final_tcp_pos_w: list[float]
    latched_target_reach_pos_w: list[float]
    live_target_reach_pos_w: list[float]
    latched_distance_m: float
    live_distance_m: float
    target_displacement_m: float
    success_threshold_m: float
    max_success_target_displacement_m: float
    reached_latched_target: bool
    reached_live_target: bool
    target_displacement_ok: bool
    recomputed_success: bool

    def to_dict(self) -> dict:
        return asdict(self)


def diagnose_reaching_episode(episode_dir: Path) -> ReachingEpisodeDiagnostic:
    meta_path = episode_dir / "meta.json"
    traj_path = episode_dir / "trajectory.npz"
    if not meta_path.is_file():
        raise FileNotFoundError(meta_path)
    if not traj_path.is_file():
        raise FileNotFoundError(traj_path)

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    with np.load(traj_path, allow_pickle=False) as traj:
        ee_pos_w = _squeeze_env(np.asarray(traj["ee_pos_w"], dtype=np.float64), "ee_pos_w")
        ee_quat_w = _squeeze_env(np.asarray(traj["ee_quat_w"], dtype=np.float64), "ee_quat_w")
        object_pos_w = _squeeze_env(np.asarray(traj["object_pos_w"], dtype=np.float64), "object_pos_w")

    tcp_offset = _meta_vector(meta, "tcp_offset_local", (0.0, 0.0, 0.10))
    reach_offset = _meta_vector(meta, "object_reach_offset_local", (0.0, 0.0, 0.0))
    tcp_final = ee_pos_w[-1] + R.from_quat(quat_wxyz_to_xyzw(ee_quat_w[-1])).apply(tcp_offset)
    latched_target = _latched_target(meta, object_pos_w, reach_offset)
    live_target = object_pos_w[-1] + reach_offset

    threshold = float(meta.get("reach_success_threshold_m", 0.01))
    max_displacement = float(meta.get("max_success_target_displacement_m", 0.02))
    latched_distance = float(np.linalg.norm(tcp_final - latched_target))
    live_distance = float(np.linalg.norm(tcp_final - live_target))
    displacement = float(np.linalg.norm(live_target - latched_target))
    reached_latched = latched_distance <= threshold
    reached_live = live_distance <= threshold
    displacement_ok = displacement <= max_displacement

    return ReachingEpisodeDiagnostic(
        episode_dir=str(episode_dir),
        instruction=str(meta.get("instruction", "")),
        success_in_meta=bool(meta.get("success", False)),
        success_mode_in_meta=meta.get("success_mode"),
        final_tcp_pos_w=tcp_final.astype(float).tolist(),
        latched_target_reach_pos_w=latched_target.astype(float).tolist(),
        live_target_reach_pos_w=live_target.astype(float).tolist(),
        latched_distance_m=latched_distance,
        live_distance_m=live_distance,
        target_displacement_m=displacement,
        success_threshold_m=threshold,
        max_success_target_displacement_m=max_displacement,
        reached_latched_target=reached_latched,
        reached_live_target=reached_live,
        target_displacement_ok=displacement_ok,
        recomputed_success=bool(reached_latched or (reached_live and displacement_ok)),
    )


def _squeeze_env(arr: np.ndarray, name: str) -> np.ndarray:
    if arr.ndim >= 3 and arr.shape[1] == 1:
        return arr[:, 0]
    if arr.ndim != 2:
        raise ValueError(f"{name} must have shape [T, D] or [T, 1, D], got {arr.shape}.")
    return arr


def _meta_vector(meta: dict, key: str, default: tuple[float, ...]) -> np.ndarray:
    value = np.asarray(meta.get(key, default), dtype=np.float64)
    if value.shape != (3,):
        raise ValueError(f"{key} must have shape (3,), got {value.shape}.")
    return value


def _latched_target(meta: dict, object_pos_w: np.ndarray, reach_offset: np.ndarray) -> np.ndarray:
    stored = meta.get("latched_target_reach_pos_w")
    if stored is not None:
        value = np.asarray(stored, dtype=np.float64)
        if value.shape == (3,):
            return value
    return object_pos_w[0] + reach_offset
