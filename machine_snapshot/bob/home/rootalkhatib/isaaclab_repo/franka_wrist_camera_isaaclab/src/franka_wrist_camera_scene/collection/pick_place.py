"""Pick-and-place data collection orchestration pipeline."""

from __future__ import annotations

import gc
from dataclasses import dataclass, replace
import json
import math
from pathlib import Path
import random
import re

import isaaclab.sim as sim_utils
import torch
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene
from isaaclab.utils.math import quat_apply

from franka_wrist_camera_scene.app.simulation_config import make_simulation_cfg
from franka_wrist_camera_scene.app.stage_lifecycle import clear_simulation_context
from franka_wrist_camera_scene.collection.batching import effective_asset_bank_episode_batch_size
from franka_wrist_camera_scene.episode.suite import (
    EMPTY_SUITE_METADATA,
    SuiteMetadata,
    suite_metadata_from_config,
)
from franka_wrist_camera_scene.control.gripper import GripperController
from franka_wrist_camera_scene.control.ik import CartesianIKController
from franka_wrist_camera_scene.episode.manifest import write_collection_manifest
from franka_wrist_camera_scene.episode.recorder import EpisodeRecorder, wait_for_pending_episode_writes
from franka_wrist_camera_scene.episode.reset import reset_pick_place_episode, reset_pick_place_vector_episode
from franka_wrist_camera_scene.episode.success import pick_place_success, receptacle_xy_radius_from_bbox
from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
from franka_wrist_camera_scene.policies.pick_place_vector import VectorPickPlaceScriptedPolicy
from franka_wrist_camera_scene.scene.appearance import set_table_color
from franka_wrist_camera_scene.scene.clutter import (
    ClutterObjectSpec,
    clutter_count_options,
    layout_margin_for_context,
    place_clutter_contexts,
    sample_clutter_count,
    sample_clutter_contexts_from_sources,
    validate_unique_active_scene_labels,
)
from franka_wrist_camera_scene.scene.lighting import set_dome_light
from franka_wrist_camera_scene.scene.object_context import CatalogObjectContext, load_catalog_object_context
from franka_wrist_camera_scene.scene.tabletop import configure_scene_cameras, make_pick_place_asset_bank_scene_cfg
from franka_wrist_camera_scene.tasks.placement_geometry import object_root_pose_on_support
from franka_wrist_camera_scene.tasks.placement_compatibility import (
    object_fits_gripper,
    object_fits_receptacle,
)
from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
from franka_wrist_camera_scene.tasks.receptacle_pose import placement_target_root_pos_w
from franka_wrist_camera_scene.tasks.sampling import (
    PickPlaceSample,
    PickPlaceSamplingOptions,
    WorkspaceConstraint,
    parse_lighting_options,
    parse_visual_randomization,
    parse_xy_range,
    sample_pick_place,
)
from franka_wrist_camera_scene.settings import CAMERA_HEIGHT, CAMERA_WIDTH
from franka_wrist_camera_scene.utils.paths import REPO_ROOT
from franka_wrist_camera_scene.utils.tensors import as_torch


DEFAULT_ASSET_BANK_EPISODE_BATCH_SIZE = 8


@dataclass(frozen=True, slots=True)
class PickPlaceSceneAssets:
    object_context: CatalogObjectContext
    placement_context: CatalogObjectContext
    clutter_contexts: tuple[CatalogObjectContext, ...]


@dataclass(frozen=True, slots=True)
class PickPlaceEpisodePlan:
    sample: PickPlaceSample
    spec: PickPlaceTaskSpec
    placement_receptacle_pos_local: tuple[float, float, float]
    clutter_specs: tuple[ClutterObjectSpec, ...]
    clutter_metadata: list[dict[str, object]]
    initial_object_receptacle_footprint_margin_m: float = 0.0


@dataclass(frozen=True, slots=True)
class PickPlaceAssetNames:
    object_name: str
    placement_target_name: str
    clutter_names: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PickPlaceAssetBank:
    target_names: dict[tuple[str, str], str]
    receptacle_names: dict[tuple[str, str], str]
    clutter_names: dict[tuple[int, str, str], str]
    target_usd_paths: dict[str, str]
    receptacle_usd_paths: dict[str, str]
    clutter_usd_paths: dict[str, str]


def _load_collection_object_context(sampling_cfg: dict, rng: random.Random) -> CatalogObjectContext:
    return load_catalog_object_context(
        catalog_config=sampling_cfg["catalog_config"],
        geometry_config=sampling_cfg["geometry_config"],
        category_id=sampling_cfg["category_id"],
        variant_id=sampling_cfg["variant_id"],
        split=sampling_cfg["split"],
        role=sampling_cfg["role"],
        required_affordances=tuple(sampling_cfg["required_affordances"]),
        required_grasp_strategy=sampling_cfg["required_grasp_strategy"],
        rng=rng,
    )


def _repo_relative_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _asset_key(context: CatalogObjectContext) -> tuple[str, str]:
    return (context.category_id, context.variant_id)


def _object_fits_gripper(context: CatalogObjectContext, sampling_cfg: dict) -> bool:
    return object_fits_gripper(
        context.geometry,
        float(sampling_cfg["max_planar_minor_extent_m"]),
    )


def _object_receptacle_pair_is_compatible(
    object_context: CatalogObjectContext,
    placement_context: CatalogObjectContext,
    compatibility_cfg: dict,
) -> bool:
    return object_fits_receptacle(
        object_context.geometry,
        placement_context.geometry,
        float(compatibility_cfg["max_height_to_receptacle_width"]),
    )


def _configured_camera_resolution(collection_cfg: dict) -> tuple[int, int]:
    width = int(collection_cfg.get("camera_width", CAMERA_WIDTH))
    height = int(collection_cfg.get("camera_height", CAMERA_HEIGHT))
    if width <= 0 or height <= 0:
        raise ValueError(f"Camera resolution must be positive, got width={width}, height={height}.")
    return width, height


def _configured_state_record_stride(collection_cfg: dict, sim_dt: float) -> int:
    if "state_record_stride" in collection_cfg and "state_record_fps" in collection_cfg:
        raise ValueError("Configure only one of state_record_stride or state_record_fps.")
    if "state_record_fps" in collection_cfg:
        state_record_fps = float(collection_cfg["state_record_fps"])
        if state_record_fps <= 0.0:
            raise ValueError(f"state_record_fps must be positive, got {state_record_fps}.")
        return max(1, round(1.0 / (state_record_fps * sim_dt)))
    return max(1, int(collection_cfg.get("state_record_stride", 1)))


def _apply_camera_resolution(
    scene_cfg,
    width: int,
    height: int,
    record_depth: bool = True,
    camera_fps: int = 30,
) -> None:
    configure_scene_cameras(
        scene_cfg,
        width=width,
        height=height,
        record_depth=record_depth,
        camera_fps=camera_fps,
    )


def _safe_entity_suffix(context: CatalogObjectContext) -> str:
    raw_name = f"{context.category_id}_{context.variant_id}"
    return re.sub(r"[^0-9A-Za-z_]+", "_", raw_name)


def _sample_scene_assets(
    collection_cfg: dict,
    target_object_cfg: dict,
    placement_target_cfg: dict,
    seed: int,
    episode_id: int,
) -> PickPlaceSceneAssets:
    compatibility_cfg = collection_cfg.get("object_receptacle_compatibility", {})
    max_attempts = int(compatibility_cfg.get("max_sampling_attempts", 32))
    target_rng = random.Random(seed + episode_id)
    placement_rng = random.Random(seed + 100_000 + episode_id)
    object_context = None
    placement_context = None
    for _ in range(max_attempts):
        candidate_object_context = _load_collection_object_context(target_object_cfg, target_rng)
        if not _object_fits_gripper(candidate_object_context, target_object_cfg):
            continue

        candidate_placement_context = _load_collection_object_context(placement_target_cfg, placement_rng)
        if (
            candidate_placement_context.category_id == candidate_object_context.category_id
            or candidate_placement_context.label == candidate_object_context.label
        ):
            continue
        if _object_receptacle_pair_is_compatible(
            object_context=candidate_object_context,
            placement_context=candidate_placement_context,
            compatibility_cfg=compatibility_cfg,
        ):
            object_context = candidate_object_context
            placement_context = candidate_placement_context
            break
    if object_context is None or placement_context is None:
        raise RuntimeError(
            "Failed to sample a compatible pick-place object/receptacle pair "
            f"after {max_attempts} attempts. "
            f"target_object={target_object_cfg!r}, "
            f"object_receptacle_compatibility={compatibility_cfg!r}"
        )

    clutter_cfg = collection_cfg["clutter"]
    excluded_clutter_keys = (
        _asset_key(object_context),
        _asset_key(placement_context),
    )
    excluded_clutter_category_ids = (
        object_context.category_id,
        placement_context.category_id,
    )
    excluded_clutter_labels = (
        object_context.label,
        placement_context.label,
    )
    clutter_count = sample_clutter_count(clutter_cfg, seed, episode_id)
    clutter_contexts_with_sources = sample_clutter_contexts_from_sources(
        clutter_cfg=clutter_cfg,
        rng=random.Random(seed + 200_000 + episode_id),
        active_count=clutter_count,
        excluded_keys=excluded_clutter_keys,
        excluded_category_ids=excluded_clutter_category_ids,
        excluded_labels=excluded_clutter_labels,
    )
    clutter_contexts = tuple(context for _, context in clutter_contexts_with_sources)

    return PickPlaceSceneAssets(
        object_context=object_context,
        placement_context=placement_context,
        clutter_contexts=clutter_contexts,
    )


def _sample_all_scene_assets(
    collection_cfg: dict,
    target_object_cfg: dict,
    placement_target_cfg: dict,
    seed: int,
    episode_ids: range,
) -> dict[int, PickPlaceSceneAssets]:
    return {
        episode_id: _sample_scene_assets(
            collection_cfg=collection_cfg,
            target_object_cfg=target_object_cfg,
            placement_target_cfg=placement_target_cfg,
            seed=seed,
            episode_id=episode_id,
        )
        for episode_id in episode_ids
    }


def _episode_batches(episode_ids: list[int], batch_size: int) -> list[list[int]]:
    if batch_size <= 0:
        raise ValueError(f"asset_bank_episode_batch_size must be positive, got {batch_size}.")
    return [episode_ids[index : index + batch_size] for index in range(0, len(episode_ids), batch_size)]


def _episode_waves(episode_ids: list[int], wave_size: int) -> list[list[int]]:
    if wave_size <= 0:
        raise ValueError(f"num_envs must be positive, got {wave_size}.")
    return [episode_ids[index : index + wave_size] for index in range(0, len(episode_ids), wave_size)]


def _register_asset_name(
    names: dict,
    usd_paths: dict[str, str],
    key,
    entity_name: str,
    usd_path: Path,
) -> None:
    if key in names:
        return
    names[key] = entity_name
    usd_paths[entity_name] = str(usd_path)


def _build_asset_bank(scene_assets_by_episode: dict[int, PickPlaceSceneAssets]) -> PickPlaceAssetBank:
    if not scene_assets_by_episode:
        raise ValueError("Cannot build a pick-place asset bank with no episodes.")

    first_assets = scene_assets_by_episode[min(scene_assets_by_episode)]
    target_names: dict[tuple[str, str], str] = {}
    receptacle_names: dict[tuple[str, str], str] = {}
    clutter_names: dict[tuple[int, str, str], str] = {}
    target_usd_paths: dict[str, str] = {}
    receptacle_usd_paths: dict[str, str] = {}
    clutter_usd_paths: dict[str, str] = {}

    _register_asset_name(
        names=target_names,
        usd_paths=target_usd_paths,
        key=_asset_key(first_assets.object_context),
        entity_name="target_cube",
        usd_path=first_assets.object_context.usd_path,
    )
    _register_asset_name(
        names=receptacle_names,
        usd_paths=receptacle_usd_paths,
        key=_asset_key(first_assets.placement_context),
        entity_name="place_receptacle",
        usd_path=first_assets.placement_context.usd_path,
    )
    for slot_index, context in enumerate(first_assets.clutter_contexts):
        _register_asset_name(
            names=clutter_names,
            usd_paths=clutter_usd_paths,
            key=(slot_index, context.category_id, context.variant_id),
            entity_name=f"clutter_{slot_index}",
            usd_path=context.usd_path,
        )

    for scene_assets in scene_assets_by_episode.values():
        target_key = _asset_key(scene_assets.object_context)
        _register_asset_name(
            names=target_names,
            usd_paths=target_usd_paths,
            key=target_key,
            entity_name=f"target_{_safe_entity_suffix(scene_assets.object_context)}",
            usd_path=scene_assets.object_context.usd_path,
        )

        receptacle_key = _asset_key(scene_assets.placement_context)
        _register_asset_name(
            names=receptacle_names,
            usd_paths=receptacle_usd_paths,
            key=receptacle_key,
            entity_name=f"receptacle_{_safe_entity_suffix(scene_assets.placement_context)}",
            usd_path=scene_assets.placement_context.usd_path,
        )

        for slot_index, context in enumerate(scene_assets.clutter_contexts):
            clutter_key = (slot_index, context.category_id, context.variant_id)
            _register_asset_name(
                names=clutter_names,
                usd_paths=clutter_usd_paths,
                key=clutter_key,
                entity_name=f"clutter_{slot_index}_{_safe_entity_suffix(context)}",
                usd_path=context.usd_path,
            )

    return PickPlaceAssetBank(
        target_names=target_names,
        receptacle_names=receptacle_names,
        clutter_names=clutter_names,
        target_usd_paths=target_usd_paths,
        receptacle_usd_paths=receptacle_usd_paths,
        clutter_usd_paths=clutter_usd_paths,
    )


def _episode_asset_names(
    asset_bank: PickPlaceAssetBank,
    scene_assets: PickPlaceSceneAssets,
) -> PickPlaceAssetNames:
    return PickPlaceAssetNames(
        object_name=asset_bank.target_names[_asset_key(scene_assets.object_context)],
        placement_target_name=asset_bank.receptacle_names[_asset_key(scene_assets.placement_context)],
        clutter_names=tuple(
            asset_bank.clutter_names[(slot_index, context.category_id, context.variant_id)]
            for slot_index, context in enumerate(scene_assets.clutter_contexts)
        ),
    )


def _inactive_asset_names(
    asset_bank: PickPlaceAssetBank,
    active_names: PickPlaceAssetNames,
) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    active_clutter_names = set(active_names.clutter_names)

    inactive_object_names = tuple(
        name
        for name in asset_bank.target_usd_paths
        if name != active_names.object_name
    )

    inactive_receptacle_names = tuple(
        name
        for name in asset_bank.receptacle_usd_paths
        if name != active_names.placement_target_name
    )

    inactive_clutter_names = tuple(
        name
        for name in asset_bank.clutter_usd_paths
        if name not in active_clutter_names
    )

    return inactive_object_names, inactive_receptacle_names, inactive_clutter_names



def _clutter_metadata(clutter_specs: tuple[ClutterObjectSpec, ...]) -> list[dict[str, object]]:
    return [
        {
            "prim_name": clutter_spec.prim_name,
            "category_id": clutter_spec.context.category_id,
            "variant_id": clutter_spec.context.variant_id,
            "label": clutter_spec.context.label,
            "usd_path": _repo_relative_path(clutter_spec.context.usd_path),
            "grasp_strategy": clutter_spec.context.grasp_strategy,
            "pos_local": list(clutter_spec.pos_local),
            "local_bbox_min": list(clutter_spec.context.geometry.local_bbox_min),
            "local_bbox_max": list(clutter_spec.context.geometry.local_bbox_max),
            "footprint_radius_m": clutter_spec.footprint_radius_m,
        }
        for clutter_spec in clutter_specs
    ]


def _pick_place_task_spec_from_collection_config(collection_cfg: dict) -> PickPlaceTaskSpec:
    spec_kwargs = {}
    if "pregrasp_object_displacement_tolerance_m" in collection_cfg:
        spec_kwargs["pregrasp_object_displacement_tolerance_m"] = float(
            collection_cfg["pregrasp_object_displacement_tolerance_m"]
        )
    if "pregrasp_object_fall_tolerance_m" in collection_cfg:
        spec_kwargs["pregrasp_object_fall_tolerance_m"] = float(
            collection_cfg["pregrasp_object_fall_tolerance_m"]
        )
    return PickPlaceTaskSpec(**spec_kwargs)


def _make_episode_plan(
    collection_cfg: dict,
    scene_assets: PickPlaceSceneAssets,
    seed: int,
    episode_id: int,
    sampling_options: PickPlaceSamplingOptions,
    asset_names: PickPlaceAssetNames,
) -> PickPlaceEpisodePlan:
    from franka_wrist_camera_scene.tasks.layout_geometry import (
        FootprintCircle,
        footprints_overlap_xy,
        planar_footprint_radius_from_bbox,
    )

    spec = _pick_place_task_spec_from_collection_config(collection_cfg)
    max_attempts = sampling_options.workspace.max_sampling_attempts
    clutter_cfg = collection_cfg["clutter"]
    object_margin = layout_margin_for_context(
        scene_assets.object_context,
        float(clutter_cfg["object_margin_m"]),
        clutter_cfg,
    )
    receptacle_margin = layout_margin_for_context(
        scene_assets.placement_context,
        float(clutter_cfg["placement_target_margin_m"]),
        clutter_cfg,
    )

    # Compute target and receptacle footprint radii from bboxes
    object_r = planar_footprint_radius_from_bbox(
        scene_assets.object_context.geometry.local_bbox_min,
        scene_assets.object_context.geometry.local_bbox_max,
        margin_m=object_margin,
    )
    receptacle_r = planar_footprint_radius_from_bbox(
        scene_assets.placement_context.geometry.local_bbox_min,
        scene_assets.placement_context.geometry.local_bbox_max,
        margin_m=receptacle_margin,
    )

    xy_range = None
    if "clutter" in collection_cfg and "xy_range" in collection_cfg["clutter"]:
        raw_range = collection_cfg["clutter"]["xy_range"]
        xy_range = (
            float(raw_range["x"][0]),
            float(raw_range["x"][1]),
            float(raw_range["y"][0]),
            float(raw_range["y"][1]),
        )

    sample = None
    for attempt in range(max_attempts):
        attempt_seed = seed + attempt * 100000
        candidate_sample = sample_pick_place(
            seed=attempt_seed,
            episode_id=episode_id,
            options=sampling_options,
        )
        object_xy = (
            sampling_options.object_origin_xy[0] + candidate_sample.object_xy_offset[0],
            sampling_options.object_origin_xy[1] + candidate_sample.object_xy_offset[1],
        )
        place_xy = (
            sampling_options.place_origin_xy[0] + candidate_sample.place_xy_offset[0],
            sampling_options.place_origin_xy[1] + candidate_sample.place_xy_offset[1],
        )
        a = FootprintCircle(name="object", xy=object_xy, radius_m=object_r)
        b = FootprintCircle(name="receptacle", xy=place_xy, radius_m=receptacle_r)

        if xy_range is not None:
            min_x, max_x, min_y, max_y = xy_range
            if not (
                a.xy[0] - a.radius_m >= min_x
                and a.xy[0] + a.radius_m <= max_x
                and a.xy[1] - a.radius_m >= min_y
                and a.xy[1] + a.radius_m <= max_y
            ):
                continue
            if not (
                b.xy[0] - b.radius_m >= min_x
                and b.xy[0] + b.radius_m <= max_x
                and b.xy[1] - b.radius_m >= min_y
                and b.xy[1] + b.radius_m <= max_y
            ):
                continue

        if not footprints_overlap_xy(a, b):
            sample = candidate_sample
            break
    else:
        raise RuntimeError(
            "Failed to sample a non-overlapping object/receptacle layout within "
            f"{max_attempts} attempts or layout bounds.\n"
            f"Object metadata: category={scene_assets.object_context.category_id}, "
            f"variant={scene_assets.object_context.variant_id}, label={scene_assets.object_context.label}, "
            f"bbox_min={scene_assets.object_context.geometry.local_bbox_min}, "
            f"bbox_max={scene_assets.object_context.geometry.local_bbox_max}, radius={object_r:.4f}m.\n"
            f"Receptacle metadata: category={scene_assets.placement_context.category_id}, "
            f"variant={scene_assets.placement_context.variant_id}, label={scene_assets.placement_context.label}, "
            f"bbox_min={scene_assets.placement_context.geometry.local_bbox_min}, "
            f"bbox_max={scene_assets.placement_context.geometry.local_bbox_max}, radius={receptacle_r:.4f}m."
        )

    placement_xy = (
        spec.place_pos_local[0] + sample.place_xy_offset[0],
        spec.place_pos_local[1] + sample.place_xy_offset[1],
    )
    placement_pos_local = object_root_pose_on_support(
        xy_pos=placement_xy,
        support_surface_z=spec.support_surface_z_local,
        object_bbox_min_z=scene_assets.placement_context.geometry.local_bbox_min[2],
        bottom_clearance_m=spec.object_bottom_clearance_m,
    )

    # Compute actual footprint margin at initial layout
    center_dist = math.hypot(
        (sampling_options.object_origin_xy[0] + sample.object_xy_offset[0]) - placement_pos_local[0],
        (sampling_options.object_origin_xy[1] + sample.object_xy_offset[1]) - placement_pos_local[1],
    )
    initial_object_receptacle_footprint_margin_m = center_dist - (object_r + receptacle_r)

    grasp_closing_axis_xy = (
        scene_assets.object_context.geometry.planar_minor_axis_local
        if scene_assets.object_context.geometry.yaw_relevant
        else None
    )
    episode_spec = make_pick_place_episode_spec(
        base_spec=spec,
        object_xy_offset=sample.object_xy_offset,
        place_xy_offset=sample.place_xy_offset,
        object_label=scene_assets.object_context.label,
        grasp_closing_axis_xy=grasp_closing_axis_xy,
        object_local_bbox_min=scene_assets.object_context.geometry.local_bbox_min,
        object_local_bbox_max=scene_assets.object_context.geometry.local_bbox_max,
        object_quat_wxyz=scene_assets.object_context.geometry.spawn_quat_wxyz,
        placement_target_pos_local=placement_pos_local,
        placement_target_quat_wxyz=scene_assets.placement_context.geometry.spawn_quat_wxyz,
        placement_target_local_bbox_min=scene_assets.placement_context.geometry.local_bbox_min,
        placement_target_local_bbox_max=scene_assets.placement_context.geometry.local_bbox_max,
        placement_label=scene_assets.placement_context.label,
    )
    episode_spec = replace(
        episode_spec,
        object_name=asset_names.object_name,
        placement_target_name=asset_names.placement_target_name,
    )

    clutter_specs = place_clutter_contexts(
        clutter_cfg=collection_cfg["clutter"],
        rng=random.Random(seed + 200_000 + episode_id),
        support_surface_z_local=episode_spec.support_surface_z_local,
        object_bottom_clearance_m=episode_spec.object_bottom_clearance_m,
        target_object_context=scene_assets.object_context,
        target_object_xy=(
            episode_spec.object_pos_local[0],
            episode_spec.object_pos_local[1],
        ),
        placement_target_context=scene_assets.placement_context,
        placement_target_xy=(
            placement_pos_local[0],
            placement_pos_local[1],
        ),
        clutter_contexts=scene_assets.clutter_contexts,
    )
    active_clutter_count = len(clutter_specs)
    if active_clutter_count not in clutter_count_options(collection_cfg["clutter"]):
        raise ValueError(f"Unexpected active pick-place clutter count: {active_clutter_count}.")
    clutter_specs = tuple(
        ClutterObjectSpec(
            prim_name=clutter_name,
            context=clutter_spec.context,
            pos_local=clutter_spec.pos_local,
            footprint_radius_m=clutter_spec.footprint_radius_m,
        )
        for clutter_name, clutter_spec in zip(asset_names.clutter_names, clutter_specs, strict=True)
    )
    validate_unique_active_scene_labels(
        named_contexts=(
            ("target", scene_assets.object_context),
            ("placement_target", scene_assets.placement_context),
        ),
        clutter_specs=clutter_specs,
    )

    return PickPlaceEpisodePlan(
        sample=sample,
        spec=episode_spec,
        placement_receptacle_pos_local=placement_pos_local,
        clutter_specs=clutter_specs,
        clutter_metadata=_clutter_metadata(clutter_specs),
        initial_object_receptacle_footprint_margin_m=initial_object_receptacle_footprint_margin_m,
    )


def validate_pick_place_plan(
    collection_cfg: dict,
    scene_assets: PickPlaceSceneAssets,
    episode_plan: PickPlaceEpisodePlan,
) -> None:
    from franka_wrist_camera_scene.tasks.layout_geometry import (
        FootprintCircle,
        validate_pick_place_initial_layout,
        planar_footprint_radius_from_bbox,
    )
    clutter_cfg = collection_cfg["clutter"]
    validate_unique_active_scene_labels(
        named_contexts=(
            ("target", scene_assets.object_context),
            ("placement_target", scene_assets.placement_context),
        ),
        clutter_specs=episode_plan.clutter_specs,
    )
    object_margin = layout_margin_for_context(
        scene_assets.object_context,
        float(clutter_cfg["object_margin_m"]),
        clutter_cfg,
    )
    receptacle_margin = layout_margin_for_context(
        scene_assets.placement_context,
        float(clutter_cfg["placement_target_margin_m"]),
        clutter_cfg,
    )

    # 1. Target object footprint
    target_radius = planar_footprint_radius_from_bbox(
        scene_assets.object_context.geometry.local_bbox_min,
        scene_assets.object_context.geometry.local_bbox_max,
        margin_m=object_margin,
    )
    target_circle = FootprintCircle(
        name=episode_plan.spec.object_name,
        xy=episode_plan.spec.object_pos_local[:2],
        radius_m=target_radius,
    )

    # 2. Receptacle footprint
    receptacle_radius = planar_footprint_radius_from_bbox(
        scene_assets.placement_context.geometry.local_bbox_min,
        scene_assets.placement_context.geometry.local_bbox_max,
        margin_m=receptacle_margin,
    )
    receptacle_circle = FootprintCircle(
        name=episode_plan.spec.placement_target_name,
        xy=episode_plan.placement_receptacle_pos_local[:2],
        radius_m=receptacle_radius,
    )

    # 3. Clutter footprints
    clutter_circles = tuple(
        FootprintCircle(
            name=spec.prim_name,
            xy=spec.pos_local[:2],
            radius_m=spec.footprint_radius_m,
        )
        for spec in episode_plan.clutter_specs
    )

    # 4. Configured xy_ranges
    xy_range = None
    if "clutter" in collection_cfg and "xy_range" in collection_cfg["clutter"]:
        raw_range = collection_cfg["clutter"]["xy_range"]
        xy_range = (
            float(raw_range["x"][0]),
            float(raw_range["x"][1]),
            float(raw_range["y"][0]),
            float(raw_range["y"][1]),
        )

    target_xy_range = None
    if "pose_randomization" in collection_cfg and "object_xy_range" in collection_cfg["pose_randomization"]:
        raw_range = collection_cfg["pose_randomization"]["object_xy_range"]
        origin_x = float(episode_plan.spec.object_pos_local[0]) - float(episode_plan.sample.object_xy_offset[0])
        origin_y = float(episode_plan.spec.object_pos_local[1]) - float(episode_plan.sample.object_xy_offset[1])
        target_xy_range = (
            origin_x + float(raw_range["x"][0]),
            origin_x + float(raw_range["x"][1]),
            origin_y + float(raw_range["y"][0]),
            origin_y + float(raw_range["y"][1]),
        )

    receptacle_xy_range = None
    if "pose_randomization" in collection_cfg and "place_xy_range" in collection_cfg["pose_randomization"]:
        raw_range = collection_cfg["pose_randomization"]["place_xy_range"]
        origin_x = float(episode_plan.placement_receptacle_pos_local[0]) - float(episode_plan.sample.place_xy_offset[0])
        origin_y = float(episode_plan.placement_receptacle_pos_local[1]) - float(episode_plan.sample.place_xy_offset[1])
        receptacle_xy_range = (
            origin_x + float(raw_range["x"][0]),
            origin_x + float(raw_range["x"][1]),
            origin_y + float(raw_range["y"][0]),
            origin_y + float(raw_range["y"][1]),
        )

    validate_pick_place_initial_layout(
        target_object=target_circle,
        placement_receptacle=receptacle_circle,
        clutter=clutter_circles,
        xy_range=xy_range,
        target_xy_range=target_xy_range,
        receptacle_xy_range=receptacle_xy_range,
    )


def _print_pick_place_timeout_diagnostics(
    scene: InteractiveScene,
    policy: PickPlaceScriptedPolicy,
    ik: CartesianIKController,
) -> None:
    """Print detailed state diagnostics when pick-and-place times out."""
    from franka_wrist_camera_scene.utils.tensors import as_torch
    robot = scene["robot"]
    ee_body_id = ik.end_effector_body_id
    ee_pose_w = as_torch(robot.data.body_pose_w)[:, ee_body_id]
    ee_pos_w = ee_pose_w[:, :3].tolist()
    ee_quat_w = ee_pose_w[:, 3:7].tolist()

    place_pos_local = policy.spec.place_pos_local
    placement_target_pos_local = policy.spec.placement_target_pos_local

    active_object = policy.spec.object_name
    active_receptacle = policy.spec.placement_target_name

    rigid_root_states = {}
    for name, r_obj in scene.rigid_objects.items():
        pos = as_torch(r_obj.data.root_pos_w)[0].tolist() if hasattr(r_obj.data, "root_pos_w") else None
        quat = as_torch(r_obj.data.root_quat_w)[0].tolist() if hasattr(r_obj.data, "root_quat_w") else None
        vel = as_torch(r_obj.data.root_vel_w)[0].tolist() if hasattr(r_obj.data, "root_vel_w") else None
        state_w = as_torch(r_obj.data.root_state_w)[0].tolist() if hasattr(r_obj.data, "root_state_w") else None
        rigid_root_states[name] = {"pos": pos, "quat": quat, "vel": vel, "state_w": state_w}

    print(
        f"[DIAGNOSTIC] Max steps exceeded!\n"
        f"  policy.state: {policy.state}\n"
        f"  current EE pose: pos={ee_pos_w}, quat={ee_quat_w}\n"
        f"  final target pose (place_pos_local): {place_pos_local}\n"
        f"  placement_target_pos_local: {placement_target_pos_local}\n"
        f"  active object/receptacle names: object={active_object}, receptacle={active_receptacle}\n"
        f"  rigid object root states: {rigid_root_states}",
        flush=True,
    )


def _motion_debug_state(policy: PickPlaceScriptedPolicy) -> dict[str, object]:
    motion = getattr(policy, "_motion", None)
    if motion is None:
        return {"active": False}
    profile = getattr(motion, "profile", None)
    segment_lengths = getattr(motion, "segment_lengths", None)
    cumulative_scaled_lengths = getattr(motion, "cumulative_scaled_lengths", None)
    return {
        "active": True,
        "duration_s": getattr(profile, "duration_s", None),
        "segment_lengths": (
            segment_lengths.detach().cpu().tolist()
            if isinstance(segment_lengths, torch.Tensor)
            else None
        ),
        "cumulative_scaled_lengths": (
            cumulative_scaled_lengths.detach().cpu().tolist()
            if isinstance(cumulative_scaled_lengths, torch.Tensor)
            else None
        ),
    }


def _print_vector_pick_place_timeout_diagnostics(
    scene: InteractiveScene,
    policy: VectorPickPlaceScriptedPolicy,
    ik: CartesianIKController,
    episode_ids: list[int],
    completed: list[bool],
    last_cmd,
    sim_time_s: float,
    step: int,
) -> None:
    """Print per-env diagnostics for vector pick-place timeouts."""
    from franka_wrist_camera_scene.utils.tensors import as_torch

    robot = scene["robot"]
    ee_body_id = ik.end_effector_body_id
    ee_pose_w = as_torch(robot.data.body_pose_w)[:, ee_body_id]
    child_policies = list(getattr(policy, "_policies", []))

    diagnostics: list[dict[str, object]] = []
    for env_index, (episode_id, is_completed) in enumerate(zip(episode_ids, completed, strict=True)):
        if is_completed:
            continue

        child_policy = child_policies[env_index] if env_index < len(child_policies) else None
        spec = child_policy.spec if child_policy is not None else None
        record: dict[str, object] = {
            "episode_id": episode_id,
            "env_index": env_index,
            "step": step,
            "sim_time_s": sim_time_s,
            "policy_state": getattr(child_policy, "state", None),
            "motion": _motion_debug_state(child_policy) if child_policy is not None else None,
            "ee_pos_w": ee_pose_w[env_index, :3].detach().cpu().tolist(),
            "ee_quat_w": ee_pose_w[env_index, 3:7].detach().cpu().tolist(),
        }

        if spec is not None:
            obj = scene[spec.object_name]
            receptacle = scene[spec.placement_target_name]
            record.update(
                {
                    "object_name": spec.object_name,
                    "receptacle_name": spec.placement_target_name,
                    "object_pos_w": as_torch(obj.data.root_pos_w)[env_index].detach().cpu().tolist(),
                    "object_quat_w": as_torch(obj.data.root_quat_w)[env_index].detach().cpu().tolist(),
                    "object_vel_w": as_torch(obj.data.root_vel_w)[env_index].detach().cpu().tolist(),
                    "receptacle_pos_w": as_torch(receptacle.data.root_pos_w)[env_index].detach().cpu().tolist(),
                    "receptacle_quat_w": as_torch(receptacle.data.root_quat_w)[env_index].detach().cpu().tolist(),
                    "receptacle_vel_w": as_torch(receptacle.data.root_vel_w)[env_index].detach().cpu().tolist(),
                    "object_pos_local": spec.object_pos_local,
                    "place_pos_local": spec.place_pos_local,
                    "placement_target_pos_local": spec.placement_target_pos_local,
                }
            )

        if last_cmd is not None:
            record["last_target_pos_w"] = last_cmd.target_pos_w[env_index].detach().cpu().tolist()
            if last_cmd.target_quat_w is not None:
                record["last_target_quat_w"] = last_cmd.target_quat_w[env_index].detach().cpu().tolist()
            if isinstance(last_cmd.finger_opening_m, torch.Tensor):
                record["last_finger_opening_m"] = (
                    last_cmd.finger_opening_m[env_index].detach().cpu().tolist()
                )

        diagnostics.append(record)

    print(f"[DIAGNOSTIC] Vector pick-place timeout diagnostics: {diagnostics}", flush=True)


def run_episode(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    policy: PickPlaceScriptedPolicy,
    ik: CartesianIKController,
    gripper: GripperController,
    output_dir: Path,
    episode_id: int,
    max_steps: int,
    settle_time_s: float,
    record_cameras: bool,
    record_depth: bool,
    camera_fps: int,
    camera_width: int,
    camera_height: int,
    state_record_stride: int,
    simulation_app,
    suite: SuiteMetadata = EMPTY_SUITE_METADATA,
    seed: int | None = None,
    object_xy_offset: tuple[float, float] | None = None,
    place_xy_offset: tuple[float, float] | None = None,
    object_category_id: str | None = None,
    object_variant_id: str | None = None,
    object_label: str | None = None,
    object_usd_path: str | None = None,
    object_grasp_strategy: str | None = None,
    object_yaw_relevant: bool | None = None,
    object_planar_aspect_ratio: float | None = None,
    object_planar_minor_axis_local: tuple[float, float] | None = None,
    object_planar_major_axis_local: tuple[float, float] | None = None,
    grasp_closing_axis_xy: tuple[float, float] | None = None,
    placement_target_category_id: str | None = None,
    placement_target_variant_id: str | None = None,
    placement_target_label: str | None = None,
    placement_target_usd_path: str | None = None,
    placement_target_grasp_strategy: str | None = None,
    placement_target_pos_local: tuple[float, float, float] | None = None,
    placement_target_quat_wxyz: tuple[float, float, float, float] | None = None,
    light_intensity: float | None = None,
    light_color: tuple[float, float, float] | None = None,
    table_color: tuple[float, float, float] | None = None,
    clutter_objects: list[dict] | None = None,
    initial_object_receptacle_footprint_margin_m: float | None = None,
) -> Path:
    """Run one episode, record data, check success, and save."""
    robot: Articulation = scene["robot"]
    sim_dt = sim.get_physics_dt()
    sim_time_s = 0.0
    step = 0
    camera_interval_steps = max(1, round(1.0 / (camera_fps * sim_dt)))

    # Initialize EpisodeRecorder
    recorder = EpisodeRecorder(
        output_dir=output_dir,
        episode_id=episode_id,
        task_name="pick_place",
        instruction=policy.spec.instruction,
        sim_dt=sim_dt,
        ee_body_id=ik.end_effector_body_id,
        object_name=policy.spec.object_name,
        max_steps=max_steps,
        state_record_stride=state_record_stride,
        record_cameras=record_cameras,
        record_depth=record_depth,
        camera_width=camera_width,
        camera_height=camera_height,
        camera_fps=camera_fps,
        suite=suite,
        object_pos_local=policy.spec.object_pos_local,
        object_quat_wxyz=policy.spec.object_quat_wxyz,
        place_pos_local=policy.spec.place_pos_local,
        seed=seed,
        object_xy_offset=object_xy_offset,
        place_xy_offset=place_xy_offset,
        object_category_id=object_category_id,
        object_variant_id=object_variant_id,
        object_label=object_label,
        object_usd_path=object_usd_path,
        object_grasp_strategy=object_grasp_strategy,
        object_yaw_relevant=object_yaw_relevant,
        object_planar_aspect_ratio=object_planar_aspect_ratio,
        object_planar_minor_axis_local=object_planar_minor_axis_local,
        object_planar_major_axis_local=object_planar_major_axis_local,
        grasp_closing_axis_xy=grasp_closing_axis_xy,
        placement_target_category_id=placement_target_category_id,
        placement_target_variant_id=placement_target_variant_id,
        placement_target_label=placement_target_label,
        placement_target_usd_path=placement_target_usd_path,
        placement_target_grasp_strategy=placement_target_grasp_strategy,
        placement_target_pos_local=placement_target_pos_local,
        placement_target_quat_wxyz=placement_target_quat_wxyz,
        light_intensity=light_intensity,
        light_color=light_color,
        table_color=table_color,
        active_clutter_count=len(clutter_objects) if clutter_objects is not None else None,
        clutter_objects=clutter_objects,
    )
    recorder.validate_output_path()

    from franka_wrist_camera_scene.utils.tensors import as_torch
    receptacle_initial = scene[policy.spec.placement_target_name]
    receptacle_initial_pos_w = as_torch(receptacle_initial.data.root_pos_w)[0].tolist()

    settling = False
    settle_steps = 0
    max_settle_steps = int(settle_time_s / sim_dt)
    completed = False

    while simulation_app.is_running() and step < max_steps:
        # 1. Step the policy to get reference actions
        cmd = policy.step(None, sim_time_s)

        # 2. Update and apply Cartesian IK command
        ik.set_target_pose(cmd.target_pos_w, cmd.target_quat_w)
        ik.apply(scene, robot)

        # 3. Update and apply gripper command
        gripper.set_width(cmd.finger_opening_m)
        gripper.apply(robot)

        scene.write_data_to_sim()

        # Dataset convention: record state_t and command_t before advancing to state_{t+1}.
        recorder.record_step(scene, cmd, step, sim_time_s)

        if record_cameras and step % camera_interval_steps == 0:
            recorder.record_cameras_step(scene, step, sim_time_s)

        sim.step()
        sim_time_s += sim_dt
        step += 1
        scene.update(sim_dt)

        if cmd.done:
            if not settling:
                print(
                    "[INFO] Scripted policy completed execution. "
                    f"Settling for {settle_time_s}s ({max_settle_steps} steps)...",
                    flush=True,
                )
                settling = True
            settle_steps += 1
            if settle_steps >= max_settle_steps:
                completed = True
                break

    if not completed:
        if step >= max_steps:
            _print_pick_place_timeout_diagnostics(scene, policy, ik)
            raise RuntimeError(f"Episode exceeded max_steps={max_steps} before policy completion.")
        raise RuntimeError("Simulation stopped before episode completion.")

    # Check success
    success = bool(pick_place_success(scene, policy.spec)[0].item())
    print(f"[INFO] Episode {episode_id} success: {success}", flush=True)

    # Save episode data
    saved_dir = recorder.save(success)
    print(f"[INFO] Saved episode data to: {saved_dir}", flush=True)

    if not success:
        import json
        import torch
        from isaaclab.utils.math import quat_apply
        from franka_wrist_camera_scene.utils.tensors import as_torch
        from franka_wrist_camera_scene.tasks.receptacle_pose import placement_target_root_pos_w
        from franka_wrist_camera_scene.episode.success import receptacle_xy_radius_from_bbox

        obj = scene[policy.spec.object_name]
        obj_pos_w = as_torch(obj.data.root_pos_w)

        ee_body_id = ik.end_effector_body_id
        ee_pose_w = as_torch(robot.data.body_pose_w)[:, ee_body_id]
        ee_pos_w = ee_pose_w[:, :3]
        ee_quat_w = ee_pose_w[:, 3:7]
        tcp_offset_local = torch.tensor(policy.spec.tcp_offset_local, device=ee_pos_w.device).view(1, 3)
        tcp_offset_w = quat_apply(ee_quat_w, tcp_offset_local.expand(ee_pos_w.shape[0], -1))
        tcp_pos_w = ee_pos_w + tcp_offset_w

        receptacle = scene[policy.spec.placement_target_name]
        receptacle_pos_w = as_torch(receptacle.data.root_pos_w)

        receptacle_pos_w_val = placement_target_root_pos_w(scene, policy.spec).to(obj_pos_w.device)
        xy_err = torch.linalg.norm(obj_pos_w[:, :2] - receptacle_pos_w_val[:, :2], dim=-1).item()

        obj_bottom_z_val = obj_pos_w[0, 2].item() + float(policy.spec.object_local_bbox_min[2])
        rec_top_z_val = receptacle_pos_w_val[0, 2].item() + float(policy.spec.placement_target_local_bbox_max[2])
        rec_bottom_z_val = receptacle_pos_w_val[0, 2].item() + float(policy.spec.placement_target_local_bbox_min[2])

        xy_threshold = receptacle_xy_radius_from_bbox(
            bbox_min=policy.spec.placement_target_local_bbox_min,
            bbox_max=policy.spec.placement_target_local_bbox_max,
            margin_m=0.025,
        )

        failure_data = {
            "episode_id": episode_id,
            "task_name": "pick_place",
            "instruction": policy.spec.instruction,
            "success": False,
            "seed": seed,
            "object_category_id": object_category_id,
            "object_variant_id": object_variant_id,
            "object_label": object_label,
            "object_initial_pos_w": recorder.first_object_pos_w()[0].tolist(),
            "object_final_pos_w": obj_pos_w[0].tolist(),
            "tcp_final_pos_w": tcp_pos_w[0].tolist(),
            "active_clutter_count": len(clutter_objects) if clutter_objects is not None else 0,
            "clutter_objects": clutter_objects if clutter_objects is not None else [],
            "placement_category_id": placement_target_category_id,
            "placement_variant_id": placement_target_variant_id,
            "placement_label": placement_target_label,
            "placement_initial_pos_w": receptacle_initial_pos_w,
            "placement_final_pos_w": receptacle_pos_w[0].tolist(),
            "object_to_receptacle_xy_error_m": xy_err,
            "object_bottom_z": obj_bottom_z_val,
            "receptacle_bottom_z": rec_bottom_z_val,
            "receptacle_top_z": rec_top_z_val,
            "xy_success_threshold_m": xy_threshold,
            "z_success_threshold_m": 0.08,
            "initial_object_receptacle_footprint_margin_m": initial_object_receptacle_footprint_margin_m if initial_object_receptacle_footprint_margin_m is not None else 0.0,
        }

        fail_file = saved_dir / "failure.json"
        fail_file.write_text(json.dumps(failure_data, indent=2), encoding="utf-8")
        print(f"[INFO] Saved failure diagnostics to: {fail_file}", flush=True)

    return saved_dir


def _make_pick_place_recorder(
    *,
    output_dir: Path,
    episode_id: int,
    plan: PickPlaceEpisodePlan,
    scene_assets: PickPlaceSceneAssets,
    sim_dt: float,
    ee_body_id: int,
    max_steps: int,
    state_record_stride: int,
    record_cameras: bool,
    record_depth: bool,
    camera_width: int,
    camera_height: int,
    camera_fps: int,
    suite: SuiteMetadata,
    seed: int | None,
    env_index: int | None,
) -> EpisodeRecorder:
    return EpisodeRecorder(
        output_dir=output_dir,
        episode_id=episode_id,
        task_name="pick_place",
        instruction=plan.spec.instruction,
        sim_dt=sim_dt,
        ee_body_id=ee_body_id,
        object_name=plan.spec.object_name,
        env_index=env_index,
        max_steps=max_steps,
        state_record_stride=state_record_stride,
        record_cameras=record_cameras,
        record_depth=record_depth,
        camera_width=camera_width,
        camera_height=camera_height,
        camera_fps=camera_fps,
        suite=suite,
        object_pos_local=plan.spec.object_pos_local,
        object_quat_wxyz=plan.spec.object_quat_wxyz,
        place_pos_local=plan.spec.place_pos_local,
        seed=seed,
        object_xy_offset=plan.sample.object_xy_offset,
        place_xy_offset=plan.sample.place_xy_offset,
        object_category_id=scene_assets.object_context.category_id,
        object_variant_id=scene_assets.object_context.variant_id,
        object_label=scene_assets.object_context.label,
        object_usd_path=_repo_relative_path(scene_assets.object_context.usd_path),
        object_grasp_strategy=scene_assets.object_context.grasp_strategy,
        object_yaw_relevant=scene_assets.object_context.geometry.yaw_relevant,
        object_planar_aspect_ratio=scene_assets.object_context.geometry.planar_aspect_ratio,
        object_planar_minor_axis_local=scene_assets.object_context.geometry.planar_minor_axis_local,
        object_planar_major_axis_local=scene_assets.object_context.geometry.planar_major_axis_local,
        grasp_closing_axis_xy=plan.spec.grasp_closing_axis_xy,
        placement_target_category_id=scene_assets.placement_context.category_id,
        placement_target_variant_id=scene_assets.placement_context.variant_id,
        placement_target_label=scene_assets.placement_context.label,
        placement_target_usd_path=_repo_relative_path(scene_assets.placement_context.usd_path),
        placement_target_grasp_strategy=scene_assets.placement_context.grasp_strategy,
        placement_target_pos_local=plan.placement_receptacle_pos_local,
        placement_target_quat_wxyz=plan.spec.placement_target_quat_wxyz,
        light_intensity=plan.sample.light_intensity,
        light_color=plan.sample.light_color,
        table_color=plan.sample.table_color,
        active_clutter_count=len(plan.clutter_metadata),
        clutter_objects=plan.clutter_metadata,
    )


def _pick_place_success_for_env(scene: InteractiveScene, spec: PickPlaceTaskSpec, env_index: int) -> bool:
    return bool(pick_place_success(scene, spec)[env_index].item())


def _write_vector_pick_place_failure_diagnostics(
    *,
    scene: InteractiveScene,
    robot: Articulation,
    ik: CartesianIKController,
    recorder: EpisodeRecorder,
    saved_dir: Path,
    episode_id: int,
    plan: PickPlaceEpisodePlan,
    scene_assets: PickPlaceSceneAssets,
    seed: int,
    env_index: int,
    reason: str,
) -> None:
    spec = plan.spec
    obj_pos_w = as_torch(scene[spec.object_name].data.root_pos_w)
    obj_pos = obj_pos_w[env_index]

    ee_body_id = ik.end_effector_body_id
    ee_pose_w = as_torch(robot.data.body_pose_w)[env_index, ee_body_id]
    ee_pos_w = ee_pose_w[:3]
    ee_quat_w = ee_pose_w[3:7]
    tcp_offset_local = torch.tensor(spec.tcp_offset_local, device=ee_pos_w.device).view(1, 3)
    tcp_offset_w = quat_apply(ee_quat_w.view(1, 4), tcp_offset_local).view(3)
    tcp_pos_w = ee_pos_w + tcp_offset_w

    receptacle_pos_w = as_torch(scene[spec.placement_target_name].data.root_pos_w)
    receptacle_pos = receptacle_pos_w[env_index]
    receptacle_target_pos_w = placement_target_root_pos_w(scene, spec).to(obj_pos.device)[env_index]
    xy_err = torch.linalg.norm(obj_pos[:2] - receptacle_target_pos_w[:2]).item()

    obj_bottom_z = obj_pos[2].item() + float(spec.object_local_bbox_min[2])
    rec_top_z = receptacle_target_pos_w[2].item() + float(spec.placement_target_local_bbox_max[2])
    rec_bottom_z = receptacle_target_pos_w[2].item() + float(spec.placement_target_local_bbox_min[2])
    xy_threshold = receptacle_xy_radius_from_bbox(
        bbox_min=spec.placement_target_local_bbox_min,
        bbox_max=spec.placement_target_local_bbox_max,
        margin_m=0.025,
    )

    placement_initial_pos_w = scene.env_origins[env_index] + torch.tensor(
        plan.placement_receptacle_pos_local,
        device=scene.env_origins.device,
        dtype=scene.env_origins.dtype,
    )

    failure_data = {
        "episode_id": episode_id,
        "task_name": "pick_place",
        "instruction": spec.instruction,
        "success": False,
        "failure_reason": reason,
        "seed": seed,
        "object_category_id": scene_assets.object_context.category_id,
        "object_variant_id": scene_assets.object_context.variant_id,
        "object_label": scene_assets.object_context.label,
        "object_initial_pos_w": recorder.first_object_pos_w()[0].tolist(),
        "object_final_pos_w": obj_pos.tolist(),
        "tcp_final_pos_w": tcp_pos_w.tolist(),
        "active_clutter_count": len(plan.clutter_metadata),
        "clutter_objects": plan.clutter_metadata,
        "placement_category_id": scene_assets.placement_context.category_id,
        "placement_variant_id": scene_assets.placement_context.variant_id,
        "placement_label": scene_assets.placement_context.label,
        "placement_initial_pos_w": placement_initial_pos_w.detach().cpu().tolist(),
        "placement_final_pos_w": receptacle_pos.tolist(),
        "object_to_receptacle_xy_error_m": xy_err,
        "object_bottom_z": obj_bottom_z,
        "receptacle_bottom_z": rec_bottom_z,
        "receptacle_top_z": rec_top_z,
        "xy_success_threshold_m": xy_threshold,
        "z_success_threshold_m": 0.08,
        "initial_object_receptacle_footprint_margin_m": plan.initial_object_receptacle_footprint_margin_m,
    }

    fail_file = saved_dir / "failure.json"
    fail_file.write_text(json.dumps(failure_data, indent=2), encoding="utf-8")
    print(f"[INFO] Saved failure diagnostics to: {fail_file}", flush=True)


def run_vector_pick_place_episodes(
    *,
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    robot: Articulation,
    ik: CartesianIKController,
    gripper: GripperController,
    output_dir: Path,
    episode_ids: list[int],
    episode_plans: list[PickPlaceEpisodePlan],
    scene_assets_by_episode: dict[int, PickPlaceSceneAssets],
    asset_bank: PickPlaceAssetBank,
    max_steps: int,
    settle_time_s: float,
    record_cameras: bool,
    record_depth: bool,
    camera_fps: int,
    camera_width: int,
    camera_height: int,
    state_record_stride: int,
    simulation_app,
    suite: SuiteMetadata,
    seed: int,
) -> list[Path]:
    """Run a wave of pick-place episodes in parallel across scene envs."""
    if len(episode_ids) != len(episode_plans):
        raise ValueError("episode_ids and episode_plans must have the same length.")
    if not episode_ids:
        return []
    if len(episode_ids) > scene.num_envs:
        raise ValueError(f"Wave has {len(episode_ids)} episodes but scene has {scene.num_envs} envs.")

    active_env_count = len(episode_ids)
    padded_plans = list(episode_plans)
    while len(padded_plans) < scene.num_envs:
        padded_plans.append(episode_plans[-1])

    reset_pick_place_vector_episode(
        sim=sim,
        scene=scene,
        specs=tuple(plan.spec for plan in padded_plans),
        clutter_specs_by_env=tuple(plan.clutter_specs for plan in padded_plans),
        all_object_names=tuple(asset_bank.target_usd_paths),
        all_receptacle_names=tuple(asset_bank.receptacle_usd_paths),
        all_clutter_names=tuple(asset_bank.clutter_usd_paths),
        active_env_count=active_env_count,
        reset_scene=False,
    )

    shared_plan = episode_plans[0]
    set_dome_light(scene, shared_plan.sample.light_intensity, shared_plan.sample.light_color)
    set_table_color(scene, shared_plan.sample.table_color)

    policy = VectorPickPlaceScriptedPolicy(
        specs=tuple(plan.spec for plan in padded_plans),
        active_env_count=active_env_count,
    )
    policy.bind(scene, robot)
    policy.reset()
    ik.reset()

    sim_dt = sim.get_physics_dt()
    camera_interval_steps = max(1, round(1.0 / (camera_fps * sim_dt)))
    recorders = [
        _make_pick_place_recorder(
            output_dir=output_dir,
            episode_id=episode_id,
            plan=plan,
            scene_assets=scene_assets_by_episode[episode_id],
            sim_dt=sim_dt,
            ee_body_id=ik.end_effector_body_id,
            max_steps=max_steps,
            state_record_stride=state_record_stride,
            record_cameras=record_cameras,
            record_depth=record_depth,
            camera_width=camera_width,
            camera_height=camera_height,
            camera_fps=camera_fps,
            suite=suite,
            seed=seed,
            env_index=env_index,
        )
        for env_index, (episode_id, plan) in enumerate(zip(episode_ids, episode_plans, strict=True))
    ]
    for recorder in recorders:
        recorder.validate_output_path()

    sim_time_s = 0.0
    step = 0
    settling = [False] * active_env_count
    settle_steps = [0] * active_env_count
    completed = [False] * active_env_count
    max_settle_steps = int(settle_time_s / sim_dt)
    last_cmd = None

    while simulation_app.is_running() and step < max_steps:
        cmd = policy.step(None, sim_time_s)
        last_cmd = cmd
        if cmd.target_quat_w is None:
            raise RuntimeError("Vector pick-place policy must command target_quat_w.")

        ik.set_target_pose(cmd.target_pos_w, cmd.target_quat_w)
        ik.apply(scene, robot)
        gripper.set_width(cmd.finger_opening_m)
        gripper.apply(robot)

        scene.write_data_to_sim()

        for env_index, recorder in enumerate(recorders):
            if not completed[env_index]:
                recorder.record_step(scene, cmd, step, sim_time_s)

        if record_cameras and step % camera_interval_steps == 0:
            refreshed = False
            for env_index, recorder in enumerate(recorders):
                if not completed[env_index]:
                    recorder.record_cameras_step(scene, step, sim_time_s, refresh=not refreshed)
                    refreshed = True

        sim.step()
        sim_time_s += sim_dt
        step += 1
        scene.update(sim_dt)

        done_mask = cmd.done
        if not isinstance(done_mask, torch.Tensor):
            raise RuntimeError("Vector pick-place policy must return a per-env done tensor.")

        for env_index in range(active_env_count):
            if completed[env_index] or not bool(done_mask[env_index].item()):
                continue
            if not settling[env_index]:
                if policy.is_failed(env_index):
                    print(
                        "[WARN] Scripted pick-place policy failed "
                        f"for episode {episode_ids[env_index]}. Settling for {settle_time_s}s "
                        f"({max_settle_steps} steps) before saving failure...",
                        flush=True,
                    )
                else:
                    print(
                        "[INFO] Scripted pick-place policy completed execution "
                        f"for episode {episode_ids[env_index]}. Settling for {settle_time_s}s "
                        f"({max_settle_steps} steps)...",
                        flush=True,
                    )
                settling[env_index] = True
            settle_steps[env_index] += 1
            if settle_steps[env_index] >= max_settle_steps:
                completed[env_index] = True

        if all(completed):
            break

    if not all(completed):
        if step >= max_steps:
            incomplete = [episode_id for episode_id, is_done in zip(episode_ids, completed, strict=True) if not is_done]
            _print_vector_pick_place_timeout_diagnostics(
                scene=scene,
                policy=policy,
                ik=ik,
                episode_ids=episode_ids,
                completed=completed,
                last_cmd=last_cmd,
                sim_time_s=sim_time_s,
                step=step,
            )
            print(
                f"[WARN] Vector pick-place episodes exceeded max_steps={max_steps}; "
                f"saving incomplete episodes as failures: {incomplete}",
                flush=True,
            )
        else:
            raise RuntimeError("Simulation stopped before vector pick-place episodes completed.")

    saved_dirs = []
    for env_index, (episode_id, plan, recorder) in enumerate(
        zip(episode_ids, episode_plans, recorders, strict=True)
    ):
        success = (
            completed[env_index]
            and not policy.is_failed(env_index)
            and _pick_place_success_for_env(scene, plan.spec, env_index)
        )
        print(f"[INFO] Episode {episode_id} success: {success}", flush=True)
        saved_dir = recorder.save(success)
        print(f"[INFO] Saved episode data to: {saved_dir}", flush=True)
        if not success:
            failure_reason = policy.failure_reason(env_index)
            if failure_reason is None:
                failure_reason = "timeout" if not completed[env_index] else "success_check_failed"
            _write_vector_pick_place_failure_diagnostics(
                scene=scene,
                robot=robot,
                ik=ik,
                recorder=recorder,
                saved_dir=saved_dir,
                episode_id=episode_id,
                plan=plan,
                scene_assets=scene_assets_by_episode[episode_id],
                seed=seed,
                env_index=env_index,
                reason=failure_reason,
            )
        saved_dirs.append(saved_dir)

    wait_for_pending_episode_writes()
    return saved_dirs


def collect_pick_place_dataset(
    collection_cfg: dict,
    device: str,
    simulation_app,
) -> None:
    """Run the pick-and-place data collection pipeline."""
    target_object_cfg = collection_cfg["target_object"]
    placement_target_cfg = collection_cfg["placement_target"]

    seed = int(collection_cfg["seed"])
    pose_randomization = collection_cfg["pose_randomization"]
    object_xy_range = parse_xy_range(pose_randomization["object_xy_range"])
    place_xy_range = parse_xy_range(pose_randomization["place_xy_range"])

    lighting_randomization = collection_cfg["lighting_randomization"]
    lighting_options = parse_lighting_options(lighting_randomization)
    visual_options = parse_visual_randomization(collection_cfg.get("visual_randomization"))
    base_spec = _pick_place_task_spec_from_collection_config(collection_cfg)
    sampling_options = PickPlaceSamplingOptions(
        object_origin_xy=base_spec.object_pos_local[:2],
        place_origin_xy=base_spec.place_pos_local[:2],
        object_xy_range=object_xy_range,
        place_xy_range=place_xy_range,
        minimum_object_place_distance_m=float(
            pose_randomization["minimum_object_place_distance_m"]
        ),
        workspace=WorkspaceConstraint(
            robot_base_xy=tuple(
                float(value)
                for value in pose_randomization["workspace"]["robot_base_xy"]
            ),
            max_distance_m=float(pose_randomization["workspace"]["max_distance_m"]),
            max_sampling_attempts=int(
                pose_randomization["workspace"]["max_sampling_attempts"]
            ),
        ),
        lighting=lighting_options,
        visual=visual_options,
    )

    output_dir = Path(collection_cfg["output_dir"])
    start_episode_id = int(collection_cfg["start_episode_id"])
    num_episodes = int(collection_cfg["num_episodes"])
    max_steps = int(collection_cfg["max_steps"])
    settle_time_s = float(collection_cfg["settle_time_s"])
    record_cameras = bool(collection_cfg["record_cameras"])
    record_depth = bool(collection_cfg["record_depth"])
    camera_fps = int(collection_cfg["camera_fps"])
    camera_width, camera_height = _configured_camera_resolution(collection_cfg)
    use_fabric = bool(collection_cfg.get("use_fabric", True))
    num_envs = int(collection_cfg.get("num_envs", 1))
    if num_envs <= 0:
        raise ValueError(f"num_envs must be positive, got {num_envs}.")
    env_spacing = float(collection_cfg.get("env_spacing", 4.0))
    if env_spacing <= 0.0:
        raise ValueError(f"env_spacing must be positive, got {env_spacing}.")
    suite = suite_metadata_from_config(collection_cfg)
    requested_asset_bank_episode_batch_size = int(
        collection_cfg.get("asset_bank_episode_batch_size", DEFAULT_ASSET_BANK_EPISODE_BATCH_SIZE)
    )
    asset_bank_episode_batch_size = effective_asset_bank_episode_batch_size(
        requested_asset_bank_episode_batch_size,
        episode_count=num_episodes,
        record_cameras=record_cameras,
    )
    if asset_bank_episode_batch_size != requested_asset_bank_episode_batch_size:
        print(
            "[INFO] Camera recording enabled; using one pick-place asset-bank scene "
            f"for {num_episodes} episodes instead of configured "
            f"asset_bank_episode_batch_size={requested_asset_bank_episode_batch_size}. "
            "This avoids repeated RTX scene teardown in one Kit process.",
            flush=True,
        )

    saved_episode_dirs: list[Path] = []
    episode_ids = list(range(start_episode_id, start_episode_id + num_episodes))

    scene_assets_by_episode = _sample_all_scene_assets(
        collection_cfg=collection_cfg,
        target_object_cfg=target_object_cfg,
        placement_target_cfg=placement_target_cfg,
        seed=seed,
        episode_ids=range(start_episode_id, start_episode_id + num_episodes),
    )

    for batch_episode_ids in _episode_batches(episode_ids, asset_bank_episode_batch_size):
        batch_scene_assets = {
            episode_id: scene_assets_by_episode[episode_id]
            for episode_id in batch_episode_ids
        }
        asset_bank = _build_asset_bank(batch_scene_assets)
        first_episode_id = batch_episode_ids[0]
        first_scene_assets = scene_assets_by_episode[first_episode_id]
        first_asset_names = _episode_asset_names(asset_bank, first_scene_assets)
        first_episode_plan = _make_episode_plan(
            collection_cfg=collection_cfg,
            scene_assets=first_scene_assets,
            seed=seed,
            episode_id=first_episode_id,
            sampling_options=sampling_options,
            asset_names=first_asset_names,
        )
        validate_pick_place_plan(collection_cfg, first_scene_assets, first_episode_plan)
        scene_num_envs = min(num_envs, len(batch_episode_ids))

        print("[INFO] Creating pick-place scene...", flush=True)
        scene_cfg = make_pick_place_asset_bank_scene_cfg(
            target_usd_paths=asset_bank.target_usd_paths,
            receptacle_usd_paths=asset_bank.receptacle_usd_paths,
            clutter_usd_paths=asset_bank.clutter_usd_paths,
            initial_target_name=first_asset_names.object_name,
            initial_receptacle_name=first_asset_names.placement_target_name,
            initial_clutter_names=first_asset_names.clutter_names,
            initial_receptacle_pos=first_episode_plan.placement_receptacle_pos_local,
            initial_clutter_specs=first_episode_plan.clutter_specs,
            num_envs=scene_num_envs,
            env_spacing=env_spacing,
        )
        _apply_camera_resolution(
            scene_cfg,
            camera_width,
            camera_height,
            record_depth=record_depth,
            camera_fps=camera_fps,
        )

        sim_cfg = make_simulation_cfg(device, use_fabric=use_fabric)
        sim = sim_utils.SimulationContext(sim_cfg)
        scene = None
        robot = None
        ik = None
        gripper = None
        try:
            state_record_stride = _configured_state_record_stride(collection_cfg, sim.get_physics_dt())
            sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
            scene = InteractiveScene(scene_cfg)
            print("[INFO] Pick-place scene created.", flush=True)
            ik = CartesianIKController()
            gripper = GripperController()

            print("[INFO] Resetting simulation...", flush=True)
            sim.reset()
            print("[INFO] Simulation reset complete.", flush=True)
            sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
            robot = scene["robot"]
            print("[INFO] Binding controllers...", flush=True)
            ik.bind(scene, robot)
            gripper.bind(scene, robot)
            print("[INFO] Controllers bound.", flush=True)

            if num_envs == 1:
                for episode_id in batch_episode_ids:
                    print(f"[INFO] Starting episode {episode_id}", flush=True)
                    scene_assets = scene_assets_by_episode[episode_id]
                    asset_names = _episode_asset_names(asset_bank, scene_assets)
                    episode_plan = (
                        first_episode_plan
                        if episode_id == first_episode_id
                        else _make_episode_plan(
                            collection_cfg=collection_cfg,
                            scene_assets=scene_assets,
                            seed=seed,
                            episode_id=episode_id,
                            sampling_options=sampling_options,
                            asset_names=asset_names,
                        )
                    )
                    validate_pick_place_plan(collection_cfg, scene_assets, episode_plan)
                    inactive_object_names, inactive_receptacle_names, inactive_clutter_names = _inactive_asset_names(
                        asset_bank,
                        asset_names,
                    )


                    policy = PickPlaceScriptedPolicy(spec=episode_plan.spec)
                    policy.bind(scene, robot)

                    reset_pick_place_episode(
                        sim=sim,
                        scene=scene,
                        spec=episode_plan.spec,
                        clutter_specs=episode_plan.clutter_specs,
                        inactive_object_names=inactive_object_names,
                        inactive_receptacle_names=inactive_receptacle_names,
                        inactive_clutter_names=inactive_clutter_names,
                        reset_scene=False,
                    )
                    set_dome_light(scene, episode_plan.sample.light_intensity, episode_plan.sample.light_color)
                    set_table_color(scene, episode_plan.sample.table_color)
                    policy.reset()
                    ik.reset()

                    saved_dir = run_episode(
                        sim=sim,
                        scene=scene,
                        policy=policy,
                        ik=ik,
                        gripper=gripper,
                        output_dir=output_dir,
                        episode_id=episode_id,
                        max_steps=max_steps,
                        settle_time_s=settle_time_s,
                        record_cameras=record_cameras,
                        record_depth=record_depth,
                        camera_fps=camera_fps,
                        camera_width=camera_width,
                        camera_height=camera_height,
                        state_record_stride=state_record_stride,
                        simulation_app=simulation_app,
                        suite=suite,
                        seed=seed,
                        object_xy_offset=episode_plan.sample.object_xy_offset,
                        place_xy_offset=episode_plan.sample.place_xy_offset,
                        object_category_id=scene_assets.object_context.category_id,
                        object_variant_id=scene_assets.object_context.variant_id,
                        object_label=scene_assets.object_context.label,
                        object_usd_path=_repo_relative_path(scene_assets.object_context.usd_path),
                        object_grasp_strategy=scene_assets.object_context.grasp_strategy,
                        object_yaw_relevant=scene_assets.object_context.geometry.yaw_relevant,
                        object_planar_aspect_ratio=scene_assets.object_context.geometry.planar_aspect_ratio,
                        object_planar_minor_axis_local=scene_assets.object_context.geometry.planar_minor_axis_local,
                        object_planar_major_axis_local=scene_assets.object_context.geometry.planar_major_axis_local,
                        grasp_closing_axis_xy=episode_plan.spec.grasp_closing_axis_xy,
                        placement_target_category_id=scene_assets.placement_context.category_id,
                        placement_target_variant_id=scene_assets.placement_context.variant_id,
                        placement_target_label=scene_assets.placement_context.label,
                        placement_target_usd_path=_repo_relative_path(scene_assets.placement_context.usd_path),
                        placement_target_grasp_strategy=scene_assets.placement_context.grasp_strategy,
                        placement_target_pos_local=episode_plan.placement_receptacle_pos_local,
                        placement_target_quat_wxyz=episode_plan.spec.placement_target_quat_wxyz,
                        light_intensity=episode_plan.sample.light_intensity,
                        light_color=episode_plan.sample.light_color,
                        table_color=episode_plan.sample.table_color,
                        clutter_objects=episode_plan.clutter_metadata,
                        initial_object_receptacle_footprint_margin_m=episode_plan.initial_object_receptacle_footprint_margin_m,
                    )
                    saved_episode_dirs.append(saved_dir)
            else:
                episode_plans_by_id: dict[int, PickPlaceEpisodePlan] = {first_episode_id: first_episode_plan}
                for episode_id in batch_episode_ids:
                    if episode_id in episode_plans_by_id:
                        continue
                    scene_assets = scene_assets_by_episode[episode_id]
                    asset_names = _episode_asset_names(asset_bank, scene_assets)
                    episode_plan = _make_episode_plan(
                        collection_cfg=collection_cfg,
                        scene_assets=scene_assets,
                        seed=seed,
                        episode_id=episode_id,
                        sampling_options=sampling_options,
                        asset_names=asset_names,
                    )
                    validate_pick_place_plan(collection_cfg, scene_assets, episode_plan)
                    episode_plans_by_id[episode_id] = episode_plan

                for wave_episode_ids in _episode_waves(batch_episode_ids, scene_num_envs):
                    print(
                        f"[INFO] Starting vector pick-place episodes {wave_episode_ids} "
                        f"with num_envs={scene_num_envs}",
                        flush=True,
                    )
                    saved_episode_dirs.extend(
                        run_vector_pick_place_episodes(
                            sim=sim,
                            scene=scene,
                            robot=robot,
                            ik=ik,
                            gripper=gripper,
                            output_dir=output_dir,
                            episode_ids=wave_episode_ids,
                            episode_plans=[episode_plans_by_id[episode_id] for episode_id in wave_episode_ids],
                            scene_assets_by_episode=scene_assets_by_episode,
                            asset_bank=asset_bank,
                            max_steps=max_steps,
                            settle_time_s=settle_time_s,
                            record_cameras=record_cameras,
                            record_depth=record_depth,
                            camera_fps=camera_fps,
                            camera_width=camera_width,
                            camera_height=camera_height,
                            state_record_stride=state_record_stride,
                            simulation_app=simulation_app,
                            suite=suite,
                            seed=seed,
                        )
                    )
        finally:
            del scene, robot, ik, gripper
            clear_simulation_context(sim)
            gc.collect()

    wait_for_pending_episode_writes()
    if bool(collection_cfg.get("_skip_collection_manifest", False)):
        print("[INFO] Skipping collection manifest for process shard.", flush=True)
        return

    manifest_path = write_collection_manifest(
        output_dir=output_dir,
        collection_cfg=collection_cfg,
        episode_dirs=saved_episode_dirs,
    )
    print(f"[INFO] Saved collection manifest to: {manifest_path}", flush=True)
