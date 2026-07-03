"""Collection manifest writer."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

from franka_wrist_camera_scene.episode.suite import suite_metadata_from_config
from franka_wrist_camera_scene.settings import CAMERA_HEIGHT, CAMERA_WIDTH


@dataclass(frozen=True, slots=True)
class EpisodeManifestEntry:
    episode_id: int
    episode_dir: str
    success: bool
    success_mode: str | None
    num_steps: int
    num_camera_frames: int
    camera_width: int | None
    camera_height: int | None
    camera_fps: int | None
    suite_name: str | None
    suite_split: str | None
    suite_difficulty: str | None
    suite_tags: list[str] | None
    suite_description: str | None
    object_pos_local: tuple[float, float, float] | None
    object_reach_offset_local: tuple[float, float, float] | None
    reach_success_threshold_m: float | None
    max_success_target_displacement_m: float | None
    place_pos_local: tuple[float, float, float] | None
    seed: int | None
    object_xy_offset: tuple[float, float] | None
    place_xy_offset: tuple[float, float] | None
    object_category_id: str | None
    object_variant_id: str | None
    object_label: str | None
    object_usd_path: str | None
    object_grasp_strategy: str | None
    target_source_name: str | None
    object_affordances: list[str] | None
    object_yaw_relevant: bool | None
    object_planar_aspect_ratio: float | None
    object_planar_minor_axis_local: tuple[float, float] | None
    object_planar_major_axis_local: tuple[float, float] | None
    grasp_closing_axis_xy: tuple[float, float] | None
    placement_target_category_id: str | None
    placement_target_variant_id: str | None
    placement_target_label: str | None
    placement_target_usd_path: str | None
    placement_target_grasp_strategy: str | None
    placement_target_pos_local: tuple[float, float, float] | None
    placement_target_quat_wxyz: tuple[float, float, float, float] | None
    light_intensity: float | None
    light_color: tuple[float, float, float] | None
    table_color: tuple[float, float, float] | None
    active_clutter_count: int | None
    clutter_objects: list[dict] | None
    trajectory_file: str
    metadata_file: str


@dataclass(frozen=True, slots=True)
class CollectionManifest:
    format_version: int
    task_name: str
    suite_name: str | None
    suite_split: str | None
    suite_difficulty: str | None
    suite_tags: list[str] | None
    suite_description: str | None
    camera_width: int
    camera_height: int
    camera_fps: int
    num_episodes: int
    successes: int
    failures: int
    failed_episode_ids: list[int]
    episodes: list[EpisodeManifestEntry]
    failure_summary: dict | None = None

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")


def write_collection_manifest(
    output_dir: Path,
    collection_cfg: dict,
    episode_dirs: list[Path],
) -> Path:
    entries: list[EpisodeManifestEntry] = []

    for episode_dir in sorted(episode_dirs):
        meta_path = episode_dir / "meta.json"
        if not meta_path.exists():
            raise FileNotFoundError(meta_path)

        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        rel_dir = episode_dir.relative_to(output_dir)

        entries.append(
            EpisodeManifestEntry(
                episode_id=int(meta["episode_id"]),
                episode_dir=rel_dir.as_posix(),
                success=bool(meta["success"]),
                success_mode=meta.get("success_mode"),
                num_steps=int(meta["num_steps"]),
                num_camera_frames=int(meta.get("num_camera_frames", 0)),
                camera_width=meta.get("camera_width"),
                camera_height=meta.get("camera_height"),
                camera_fps=meta.get("camera_fps"),
                suite_name=meta.get("suite_name"),
                suite_split=meta.get("suite_split"),
                suite_difficulty=meta.get("suite_difficulty"),
                suite_tags=meta.get("suite_tags"),
                suite_description=meta.get("suite_description"),
                object_pos_local=tuple(meta["object_pos_local"]) if meta.get("object_pos_local") is not None else None,
                object_reach_offset_local=(
                    tuple(meta["object_reach_offset_local"])
                    if meta.get("object_reach_offset_local") is not None
                    else None
                ),
                reach_success_threshold_m=meta.get("reach_success_threshold_m"),
                max_success_target_displacement_m=meta.get("max_success_target_displacement_m"),
                place_pos_local=tuple(meta["place_pos_local"]) if meta.get("place_pos_local") is not None else None,
                seed=meta.get("seed"),
                object_xy_offset=tuple(meta["object_xy_offset"]) if meta.get("object_xy_offset") is not None else None,
                place_xy_offset=tuple(meta["place_xy_offset"]) if meta.get("place_xy_offset") is not None else None,
                object_category_id=meta.get("object_category_id"),
                object_variant_id=meta.get("object_variant_id"),
                object_label=meta.get("object_label"),
                object_usd_path=meta.get("object_usd_path"),
                object_grasp_strategy=meta.get("object_grasp_strategy"),
                target_source_name=meta.get("target_source_name"),
                object_affordances=meta.get("object_affordances"),
                object_yaw_relevant=meta.get("object_yaw_relevant"),
                object_planar_aspect_ratio=meta.get("object_planar_aspect_ratio"),
                object_planar_minor_axis_local=(
                    tuple(meta["object_planar_minor_axis_local"])
                    if meta.get("object_planar_minor_axis_local") is not None
                    else None
                ),
                object_planar_major_axis_local=(
                    tuple(meta["object_planar_major_axis_local"])
                    if meta.get("object_planar_major_axis_local") is not None
                    else None
                ),
                grasp_closing_axis_xy=(
                    tuple(meta["grasp_closing_axis_xy"])
                    if meta.get("grasp_closing_axis_xy") is not None
                    else None
                ),
                placement_target_category_id=meta.get("placement_target_category_id"),
                placement_target_variant_id=meta.get("placement_target_variant_id"),
                placement_target_label=meta.get("placement_target_label"),
                placement_target_usd_path=meta.get("placement_target_usd_path"),
                placement_target_grasp_strategy=meta.get("placement_target_grasp_strategy"),
                placement_target_pos_local=(
                    tuple(meta["placement_target_pos_local"])
                    if meta.get("placement_target_pos_local") is not None
                    else None
                ),
                placement_target_quat_wxyz=(
                    tuple(meta["placement_target_quat_wxyz"])
                    if meta.get("placement_target_quat_wxyz") is not None
                    else None
                ),
                light_intensity=meta.get("light_intensity"),
                light_color=tuple(meta["light_color"]) if meta.get("light_color") is not None else None,
                table_color=tuple(meta["table_color"]) if meta.get("table_color") is not None else None,
                active_clutter_count=meta.get("active_clutter_count"),
                clutter_objects=meta.get("clutter_objects"),
                trajectory_file=(rel_dir / "trajectory.npz").as_posix(),
                metadata_file=(rel_dir / "meta.json").as_posix(),
            )
        )

    successes = sum(entry.success for entry in entries)
    failed_episode_ids = [entry.episode_id for entry in entries if not entry.success]

    failure_summary = None
    if failed_episode_ids:
        by_task = {}
        by_object_category = {}
        by_receptacle_category = {}
        by_target_source = {}
        errors = []
        failure_json_files = []
        failure_summary_errors = []

        for ep_id in failed_episode_ids:
            fail_json_path = output_dir / f"{ep_id:06d}" / "failure.json"
            if not fail_json_path.exists():
                raise FileNotFoundError(f"Episode {ep_id:06d} is missing failure.json")

            try:
                fail_data = json.loads(fail_json_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError) as e:
                raise RuntimeError(f"Episode {ep_id:06d} failure.json is malformed or unreadable: {str(e)}") from e

            failure_json_files.append(f"{ep_id:06d}/failure.json")

            task = fail_data.get("task_name")
            if task:
                by_task[task] = by_task.get(task, 0) + 1

            obj_cat = fail_data.get("object_category_id")
            if obj_cat:
                by_object_category[obj_cat] = by_object_category.get(obj_cat, 0) + 1

            rec_cat = fail_data.get("placement_category_id")
            if rec_cat:
                by_receptacle_category[rec_cat] = by_receptacle_category.get(rec_cat, 0) + 1

            tgt_src = fail_data.get("target_source_name")
            if tgt_src:
                by_target_source[tgt_src] = by_target_source.get(tgt_src, 0) + 1

            if task == "pick_place":
                err = fail_data.get("object_to_receptacle_xy_error_m")
            else:  # reaching
                err = fail_data.get("final_tcp_distance_to_latched_target_m")

            if err is not None:
                try:
                    errors.append(float(err))
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Episode {ep_id:06d} failure.json has invalid error metric: {err!r}") from e

        import numpy as np
        mean_err = float(np.mean(errors)) if errors else None
        max_err = float(np.max(errors)) if errors else None

        failure_summary = {
            "by_task": by_task,
            "by_object_category": by_object_category,
            "by_receptacle_category": by_receptacle_category,
            "by_target_source": by_target_source,
            "mean_final_error_m": mean_err,
            "max_final_error_m": max_err,
            "failure_json_files": failure_json_files,
            "failure_summary_errors": failure_summary_errors,
        }

    suite = suite_metadata_from_config(collection_cfg)
    manifest = CollectionManifest(
        format_version=1,
        task_name=str(collection_cfg["task"]),
        suite_name=suite.name,
        suite_split=suite.split,
        suite_difficulty=suite.difficulty,
        suite_tags=suite.tags,
        suite_description=suite.description,
        camera_width=int(collection_cfg.get("camera_width", CAMERA_WIDTH)),
        camera_height=int(collection_cfg.get("camera_height", CAMERA_HEIGHT)),
        camera_fps=int(collection_cfg["camera_fps"]),
        num_episodes=len(entries),
        successes=successes,
        failures=len(entries) - successes,
        failed_episode_ids=failed_episode_ids,
        episodes=entries,
        failure_summary=failure_summary,
    )

    manifest_path = output_dir / "manifest.json"
    manifest.save(manifest_path)
    return manifest_path
