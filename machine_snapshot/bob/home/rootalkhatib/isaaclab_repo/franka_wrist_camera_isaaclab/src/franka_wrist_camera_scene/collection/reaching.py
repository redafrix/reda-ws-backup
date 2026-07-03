"""Reaching data collection orchestration pipeline."""

from __future__ import annotations

import gc
import random
import re
from dataclasses import dataclass, replace
from pathlib import Path

import isaaclab.sim as sim_utils
import torch
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene

from franka_wrist_camera_scene.app.simulation_config import make_simulation_cfg
from franka_wrist_camera_scene.app.stage_lifecycle import clear_simulation_context
from franka_wrist_camera_scene.collection.batching import effective_asset_bank_episode_batch_size
from franka_wrist_camera_scene.control.gripper import GripperController
from franka_wrist_camera_scene.control.ik import CartesianIKController, PostureBiasCfg
from franka_wrist_camera_scene.episode.manifest import write_collection_manifest
from franka_wrist_camera_scene.episode.recorder import EpisodeRecorder, wait_for_pending_episode_writes
from franka_wrist_camera_scene.episode.reset import reset_reaching_episode, reset_reaching_vector_episode
from franka_wrist_camera_scene.episode.success import reaching_success_metrics
from franka_wrist_camera_scene.episode.suite import (
    EMPTY_SUITE_METADATA,
    SuiteMetadata,
    suite_metadata_from_config,
)
from franka_wrist_camera_scene.policies.reaching_scripted import ReachingScriptedPolicy
from franka_wrist_camera_scene.policies.reaching_vector import VectorReachingScriptedPolicy
from franka_wrist_camera_scene.scene.clutter import (
    ClutterLayoutSamplingError,
    ClutterObjectSpec,
    layout_footprint_for_context,
    layout_margin_for_context,
    place_reaching_clutter_contexts,
    sample_clutter_contexts_from_sources,
    sample_clutter_count,
    validate_unique_active_scene_labels,
)
from franka_wrist_camera_scene.scene.lighting import set_dome_light
from franka_wrist_camera_scene.scene.object_context import CatalogObjectContext, load_catalog_object_context
from franka_wrist_camera_scene.scene.tabletop import (
    REACHING_CLUTTER_SLOT_COUNT,
    configure_scene_cameras,
    make_reaching_asset_bank_scene_cfg,
)
from franka_wrist_camera_scene.settings import CAMERA_HEIGHT, CAMERA_WIDTH, TABLE_HEIGHT_M
from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec, make_reaching_episode_spec
from franka_wrist_camera_scene.tasks.sampling import (
    ReachingSample,
    ReachingSamplingOptions,
    WorkspaceConstraint,
    parse_lighting_options,
    parse_xy_range,
    sample_reaching_offsets,
)
from franka_wrist_camera_scene.utils.paths import REPO_ROOT
from franka_wrist_camera_scene.utils.tensors import as_torch

REACHING_OBJECT_BOTTOM_CLEARANCE_M = 0.003
DEFAULT_ASSET_BANK_EPISODE_BATCH_SIZE = 8


@dataclass(frozen=True, slots=True)
class ReachingSceneAssets:
    object_context: CatalogObjectContext
    clutter_contexts: tuple[tuple[str, CatalogObjectContext], ...]
    target_source_name: str | None = None


@dataclass(frozen=True, slots=True)
class ReachingEpisodePlan:
    sample: ReachingSample
    spec: ReachingTaskSpec
    clutter_specs: tuple[ClutterObjectSpec, ...]
    clutter_metadata: list[dict[str, object]]


@dataclass(frozen=True, slots=True)
class ReachingAssetNames:
    object_name: str
    clutter_names: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ReachingAssetBank:
    target_names: dict[tuple[str, str], str]
    clutter_names: dict[tuple[int, str, str], str]
    target_usd_paths: dict[str, str]
    clutter_usd_paths: dict[str, str]


def _repo_relative_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _asset_key(context: CatalogObjectContext) -> tuple[str, str]:
    return (context.category_id, context.variant_id)


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


def _safe_entity_suffix(context: CatalogObjectContext) -> str:
    raw_name = f"{context.category_id}_{context.variant_id}"
    return re.sub(r"[^0-9A-Za-z_]+", "_", raw_name)


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


def _clutter_metadata(clutter_specs: tuple[ClutterObjectSpec, ...]) -> list[dict[str, object]]:
    return [
        {
            "prim_name": clutter_spec.prim_name,
            "source_name": clutter_spec.source_name,
            "category_id": clutter_spec.context.category_id,
            "variant_id": clutter_spec.context.variant_id,
            "label": clutter_spec.context.label,
            "usd_path": _repo_relative_path(clutter_spec.context.usd_path),
            "grasp_strategy": clutter_spec.context.grasp_strategy,
            "affordances": list(clutter_spec.context.affordances),
            "pos_local": list(clutter_spec.pos_local),
            "local_bbox_min": list(clutter_spec.context.geometry.local_bbox_min),
            "local_bbox_max": list(clutter_spec.context.geometry.local_bbox_max),
            "footprint_radius_m": clutter_spec.footprint_radius_m,
        }
        for clutter_spec in clutter_specs
    ]


def _sample_scene_assets(
    collection_cfg: dict,
    seed: int,
    episode_id: int,
) -> ReachingSceneAssets:
    rng = random.Random(seed + episode_id)
    if "target_sources" not in collection_cfg:
        raise KeyError("Reaching collection configuration must define 'target_sources'.")
    sources = collection_cfg["target_sources"]
    weights = [float(s.get("weight", 1.0)) for s in sources]
    source_cfg = rng.choices(sources, weights=weights, k=1)[0]
    target_source_name = source_cfg["name"]
    target_cfg = source_cfg

    object_context = _load_collection_object_context(
        target_cfg,
        rng,
    )

    clutter_cfg = collection_cfg["clutter"]
    exclude_target_variant = clutter_cfg.get("exclude_target_variant", True)
    exclude_target_label = clutter_cfg.get("exclude_target_label", True)

    excluded_keys = ()
    if exclude_target_variant:
        excluded_keys = (_asset_key(object_context),)
    excluded_category_ids = ()
    excluded_labels = ()
    if exclude_target_label:
        excluded_category_ids = (object_context.category_id,)
        excluded_labels = (object_context.label,)

    active_clutter_count = sample_clutter_count(clutter_cfg, seed, episode_id)
    clutter_contexts = sample_clutter_contexts_from_sources(
        clutter_cfg=clutter_cfg,
        rng=random.Random(seed + 200_000 + episode_id),
        active_count=active_clutter_count,
        excluded_keys=excluded_keys,
        excluded_category_ids=excluded_category_ids,
        excluded_labels=excluded_labels,
    )
    return ReachingSceneAssets(
        object_context=object_context,
        clutter_contexts=clutter_contexts,
        target_source_name=target_source_name,
    )


def _sample_all_scene_assets(
    collection_cfg: dict,
    seed: int,
    episode_ids: range,
) -> dict[int, ReachingSceneAssets]:
    return {
        episode_id: _sample_scene_assets(
            collection_cfg=collection_cfg,
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


def _build_asset_bank(scene_assets_by_episode: dict[int, ReachingSceneAssets]) -> ReachingAssetBank:
    if not scene_assets_by_episode:
        raise ValueError("Cannot build a reaching asset bank with no episodes.")

    first_assets = scene_assets_by_episode[min(scene_assets_by_episode)]
    target_names: dict[tuple[str, str], str] = {}
    clutter_names: dict[tuple[int, str, str], str] = {}
    target_usd_paths: dict[str, str] = {}
    clutter_usd_paths: dict[str, str] = {}

    _register_asset_name(
        names=target_names,
        usd_paths=target_usd_paths,
        key=_asset_key(first_assets.object_context),
        entity_name="target_cube",
        usd_path=first_assets.object_context.usd_path,
    )

    if not first_assets.clutter_contexts:
        raise ValueError(
            "Reaching asset bank construction requires at least one clutter context, "
            "but first_assets.clutter_contexts is empty."
        )
    first_clutter_context = first_assets.clutter_contexts[0][1]
    for slot_index in range(REACHING_CLUTTER_SLOT_COUNT):
        if slot_index < len(first_assets.clutter_contexts):
            context = first_assets.clutter_contexts[slot_index][1]
            key = (slot_index, context.category_id, context.variant_id)
        else:
            context = first_clutter_context
            key = (slot_index, "__parked__", str(slot_index))
        _register_asset_name(
            names=clutter_names,
            usd_paths=clutter_usd_paths,
            key=key,
            entity_name=f"clutter_{slot_index}",
            usd_path=context.usd_path,
        )

    for scene_assets in scene_assets_by_episode.values():
        _register_asset_name(
            names=target_names,
            usd_paths=target_usd_paths,
            key=_asset_key(scene_assets.object_context),
            entity_name=f"target_{_safe_entity_suffix(scene_assets.object_context)}",
            usd_path=scene_assets.object_context.usd_path,
        )

        for slot_index, (_, context) in enumerate(scene_assets.clutter_contexts):
            _register_asset_name(
                names=clutter_names,
                usd_paths=clutter_usd_paths,
                key=(slot_index, context.category_id, context.variant_id),
                entity_name=f"clutter_{slot_index}_{_safe_entity_suffix(context)}",
                usd_path=context.usd_path,
            )

    return ReachingAssetBank(
        target_names=target_names,
        clutter_names=clutter_names,
        target_usd_paths=target_usd_paths,
        clutter_usd_paths=clutter_usd_paths,
    )


def _episode_asset_names(
    asset_bank: ReachingAssetBank,
    scene_assets: ReachingSceneAssets,
) -> ReachingAssetNames:
    return ReachingAssetNames(
        object_name=asset_bank.target_names[_asset_key(scene_assets.object_context)],
        clutter_names=tuple(
            asset_bank.clutter_names[(slot_index, context.category_id, context.variant_id)]
            for slot_index, (_, context) in enumerate(scene_assets.clutter_contexts)
        ),
    )


def _inactive_reaching_asset_names(
    asset_bank: ReachingAssetBank,
    active_names: ReachingAssetNames,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    active_clutter_names = set(active_names.clutter_names)

    inactive_object_names = tuple(
        name
        for name in asset_bank.target_usd_paths
        if name != active_names.object_name
    )

    inactive_clutter_names = tuple(
        name
        for name in asset_bank.clutter_usd_paths
        if name not in active_clutter_names
    )

    return inactive_object_names, inactive_clutter_names


def _make_episode_plan(
    collection_cfg: dict,
    scene_assets: ReachingSceneAssets,
    seed: int,
    episode_id: int,
    sampling_options: ReachingSamplingOptions,
    asset_names: ReachingAssetNames,
) -> ReachingEpisodePlan:
    from franka_wrist_camera_scene.tasks.layout_geometry import (
        planar_footprint_radius_from_bbox,
    )
    spec = ReachingTaskSpec()
    max_attempts = sampling_options.workspace.max_sampling_attempts
    clutter_cfg = collection_cfg["clutter"]
    object_margin = layout_margin_for_context(
        scene_assets.object_context,
        float(clutter_cfg["object_margin_m"]),
        clutter_cfg,
    )
    object_r = planar_footprint_radius_from_bbox(
        scene_assets.object_context.geometry.local_bbox_min,
        scene_assets.object_context.geometry.local_bbox_max,
        margin_m=object_margin,
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

    last_layout_error: ClutterLayoutSamplingError | None = None
    for attempt in range(max_attempts):
        attempt_seed = seed + attempt * 100000
        candidate_sample = sample_reaching_offsets(
            seed=attempt_seed,
            episode_id=episode_id,
            options=sampling_options,
        )
        object_xy = (
            sampling_options.object_origin_xy[0] + candidate_sample.object_xy_offset[0],
            sampling_options.object_origin_xy[1] + candidate_sample.object_xy_offset[1],
        )

        if xy_range is not None:
            min_x, max_x, min_y, max_y = xy_range
            if not (
                object_xy[0] - object_r >= min_x
                and object_xy[0] + object_r <= max_x
                and object_xy[1] - object_r >= min_y
                and object_xy[1] + object_r <= max_y
            ):
                continue

        episode_spec = make_reaching_episode_spec(
            base_spec=spec,
            object_xy_offset=candidate_sample.object_xy_offset,
            object_label=scene_assets.object_context.label,
            object_local_bbox_min=scene_assets.object_context.geometry.local_bbox_min,
            object_local_bbox_max=scene_assets.object_context.geometry.local_bbox_max,
            object_category_id=scene_assets.object_context.category_id,
            object_affordances=scene_assets.object_context.affordances,
            robot_base_xy=sampling_options.workspace.robot_base_xy,
        )
        episode_spec = replace(episode_spec, object_name=asset_names.object_name)

        try:
            clutter_specs = place_reaching_clutter_contexts(
                clutter_cfg=collection_cfg["clutter"],
                rng=random.Random(seed + 300_000 + episode_id + attempt * 100_000),
                support_surface_z_local=TABLE_HEIGHT_M,
                object_bottom_clearance_m=REACHING_OBJECT_BOTTOM_CLEARANCE_M,
                target_object_context=scene_assets.object_context,
                target_object_xy=(episode_spec.object_pos_local[0], episode_spec.object_pos_local[1]),
                clutter_contexts=scene_assets.clutter_contexts,
            )
        except ClutterLayoutSamplingError as err:
            last_layout_error = err
            continue

        clutter_specs = tuple(
            ClutterObjectSpec(
                prim_name=clutter_name,
                context=clutter_spec.context,
                pos_local=clutter_spec.pos_local,
                footprint_radius_m=clutter_spec.footprint_radius_m,
                source_name=clutter_spec.source_name,
            )
            for clutter_name, clutter_spec in zip(asset_names.clutter_names, clutter_specs, strict=True)
        )
        validate_unique_active_scene_labels(
            named_contexts=(("target", scene_assets.object_context),),
            clutter_specs=clutter_specs,
        )

        return ReachingEpisodePlan(
            sample=candidate_sample,
            spec=episode_spec,
            clutter_specs=clutter_specs,
            clutter_metadata=_clutter_metadata(clutter_specs),
        )

    raise RuntimeError(
        f"Failed to sample a complete reaching layout within bounds after {max_attempts} attempts. "
        f"target={scene_assets.object_context.category_id}/{scene_assets.object_context.variant_id} "
        f"label={scene_assets.object_context.label}, "
        f"last_layout_error={last_layout_error}"
    )


def validate_reaching_plan(
    collection_cfg: dict,
    scene_assets: ReachingSceneAssets,
    episode_plan: ReachingEpisodePlan,
) -> None:
    from franka_wrist_camera_scene.tasks.layout_geometry import (
        FootprintCircle,
        require_non_overlapping_footprints,
        validate_non_overlapping_layout,
        planar_footprint_radius_from_bbox,
    )
    clutter_cfg = collection_cfg["clutter"]
    validate_unique_active_scene_labels(
        named_contexts=(("target", scene_assets.object_context),),
        clutter_specs=episode_plan.clutter_specs,
    )
    object_margin = layout_margin_for_context(
        scene_assets.object_context,
        float(clutter_cfg["object_margin_m"]),
        clutter_cfg,
    )

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

    clutter_circles = tuple(
        FootprintCircle(
            name=spec.prim_name,
            xy=spec.pos_local[:2],
            radius_m=spec.footprint_radius_m,
        )
        for spec in episode_plan.clutter_specs
    )
    target_clearance_clutter_circles = tuple(
        FootprintCircle(
            name=spec.prim_name,
            xy=spec.pos_local[:2],
            radius_m=layout_footprint_for_context(
                spec.context,
                float(clutter_cfg["clutter_margin_m"]),
                clutter_cfg,
            ),
        )
        for spec in episode_plan.clutter_specs
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

    for clutter_circle in target_clearance_clutter_circles:
        require_non_overlapping_footprints(target_circle, clutter_circle)
    validate_non_overlapping_layout(clutter_circles)

    if target_xy_range is not None:
        min_x, max_x, min_y, max_y = target_xy_range
        if not (
            min_x <= target_circle.xy[0] <= max_x
            and min_y <= target_circle.xy[1] <= max_y
        ):
            raise ValueError(
                f"Target object center '{target_circle.name}' (xy={target_circle.xy}) is not within "
                f"the configured object_xy_range boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )

    if xy_range is not None:
        min_x, max_x, min_y, max_y = xy_range
        all_circles = (target_circle, *clutter_circles)
        for circle in all_circles:
            if not (
                circle.xy[0] - circle.radius_m >= min_x
                and circle.xy[0] + circle.radius_m <= max_x
                and circle.xy[1] - circle.radius_m >= min_y
                and circle.xy[1] + circle.radius_m <= max_y
            ):
                raise ValueError(
                    f"Footprint '{circle.name}' (xy={circle.xy}, radius={circle.radius_m}m) is not within "
                    f"the configured layout boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
                )


def run_episode(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    policy: ReachingScriptedPolicy,
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
    object_category_id: str | None = None,
    object_variant_id: str | None = None,
    object_label: str | None = None,
    object_usd_path: str | None = None,
    object_grasp_strategy: str | None = None,
    target_source_name: str | None = None,
    object_affordances: list[str] | None = None,
    object_yaw_relevant: bool | None = None,
    object_planar_aspect_ratio: float | None = None,
    object_planar_minor_axis_local: tuple[float, float] | None = None,
    object_planar_major_axis_local: tuple[float, float] | None = None,
    object_reach_offset_local: tuple[float, float, float] | None = None,
    reach_success_threshold_m: float | None = None,
    reach_max_target_displacement_m: float | None = None,
    light_intensity: float | None = None,
    light_color: tuple[float, float, float] | None = None,
    clutter_objects: list[dict] | None = None,
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
        task_name="reaching",
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
        seed=seed,
        object_xy_offset=object_xy_offset,
        object_category_id=object_category_id,
        object_variant_id=object_variant_id,
        object_label=object_label,
        object_usd_path=object_usd_path,
        object_grasp_strategy=object_grasp_strategy,
        target_source_name=target_source_name,
        object_affordances=object_affordances,
        object_yaw_relevant=object_yaw_relevant,
        object_planar_aspect_ratio=object_planar_aspect_ratio,
        object_planar_minor_axis_local=object_planar_minor_axis_local,
        object_planar_major_axis_local=object_planar_major_axis_local,
        object_reach_offset_local=object_reach_offset_local,
        reach_success_threshold_m=reach_success_threshold_m,
        max_success_target_displacement_m=reach_max_target_displacement_m,
        light_intensity=light_intensity,
        light_color=light_color,
        active_clutter_count=len(clutter_objects) if clutter_objects is not None else None,
        clutter_objects=clutter_objects,
    )
    recorder.validate_output_path()

    settling = False
    settle_steps = 0
    max_settle_steps = int(settle_time_s / sim_dt)
    completed = False

    while simulation_app.is_running() and step < max_steps:
        # 1. Step the policy to get reference actions
        cmd = policy.step(None, sim_time_s)

        # 2. Update and apply Cartesian IK command
        if cmd.target_quat_w is None:
            raise RuntimeError("Reaching policy must command target_quat_w to keep wrist orientation fixed.")
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
                    f"[INFO] Scripted policy completed execution. Settling for {settle_time_s}s ({max_settle_steps} steps)...",
                    flush=True,
                )
                settling = True
            settle_steps += 1
            if settle_steps >= max_settle_steps:
                completed = True
                break

    if not completed:
        if step >= max_steps:
            raise RuntimeError(f"Episode exceeded max_steps={max_steps} before policy completion.")
        raise RuntimeError("Simulation stopped before episode completion.")

    # Check success
    metrics = reaching_success_metrics(
        scene=scene,
        spec=policy.spec,
        target_reach_pos_w=policy.latched_reach_pos_w,
        threshold_m=reach_success_threshold_m,
        max_target_displacement_m=reach_max_target_displacement_m,
    )
    success = bool(metrics.success[0].item())

    if bool(metrics.reached_latched_target[0].item()):
        success_mode = "latched_target"
    elif bool((metrics.reached_live_target & metrics.target_displacement_ok)[0].item()):
        success_mode = "live_target_with_small_displacement"
    else:
        success_mode = "failure"

    print(f"[INFO] Episode {episode_id} success: {success} (mode: {success_mode})", flush=True)

    # Save episode data
    saved_dir = recorder.save(success, success_mode=success_mode)
    print(f"[INFO] Saved episode data to: {saved_dir}", flush=True)

    if not success:
        import json
        import torch
        from franka_wrist_camera_scene.utils.tensors import as_torch

        obj = scene[policy.spec.object_name]
        obj_pos_w = as_torch(obj.data.root_pos_w)

        ee_body_id = ik.end_effector_body_id
        ee_pose_w = as_torch(robot.data.body_pose_w)[:, ee_body_id]
        ee_pos_w = ee_pose_w[:, :3]
        ee_quat_w = ee_pose_w[:, 3:7]
        tcp_offset_local = torch.tensor(policy.spec.tcp_offset_local, device=ee_pos_w.device).view(1, 3)
        from isaaclab.utils.math import quat_apply
        tcp_offset_w = quat_apply(ee_quat_w, tcp_offset_local.expand(ee_pos_w.shape[0], -1))
        tcp_pos_w = ee_pos_w + tcp_offset_w

        latched_pos = policy.latched_reach_pos_w.to(tcp_pos_w.device)
        reach_offset = torch.tensor(policy.spec.object_reach_offset_local, device=obj_pos_w.device).view(1, 3)
        live_pos = obj_pos_w[:, :3] + reach_offset

        target_displacement = float(metrics.target_displacement_m[0].item())
        final_tcp_dist_to_latched = float(metrics.latched_distance_m[0].item())
        final_tcp_dist_to_live = float(metrics.live_distance_m[0].item())

        failure_data = {
            "episode_id": episode_id,
            "task_name": "reaching",
            "instruction": policy.spec.instruction,
            "success": False,
            "success_mode": success_mode,
            "seed": seed,
            "object_category_id": object_category_id,
            "object_variant_id": object_variant_id,
            "object_label": object_label,
            "object_initial_pos_w": recorder.first_object_pos_w()[0].tolist(),
            "object_final_pos_w": obj_pos_w[0].tolist(),
            "tcp_final_pos_w": tcp_pos_w[0].tolist(),
            "active_clutter_count": len(clutter_objects) if clutter_objects is not None else 0,
            "clutter_objects": clutter_objects if clutter_objects is not None else [],
            "latched_target_reach_pos_w": latched_pos[0].tolist(),
            "live_target_reach_pos_w": live_pos[0].tolist(),
            "target_displacement_m": target_displacement,
            "final_tcp_distance_to_latched_target_m": final_tcp_dist_to_latched,
            "final_tcp_distance_to_live_target_m": final_tcp_dist_to_live,
            "success_threshold_m": reach_success_threshold_m if reach_success_threshold_m is not None else 0.01,
            "max_success_target_displacement_m": reach_max_target_displacement_m if reach_max_target_displacement_m is not None else 0.02,
            "target_source_name": target_source_name,
        }

        fail_file = saved_dir / "failure.json"
        fail_file.write_text(json.dumps(failure_data, indent=2), encoding="utf-8")
        print(f"[INFO] Saved failure diagnostics to: {fail_file}", flush=True)

    return saved_dir


def _make_reaching_recorder(
    *,
    output_dir: Path,
    episode_id: int,
    plan: ReachingEpisodePlan,
    scene_assets: ReachingSceneAssets,
    sim_dt: float,
    ee_body_id: int,
    max_steps: int,
    record_cameras: bool,
    record_depth: bool,
    camera_width: int,
    camera_height: int,
    state_record_stride: int,
    camera_fps: int,
    suite: SuiteMetadata,
    seed: int | None,
    env_index: int | None,
) -> EpisodeRecorder:
    return EpisodeRecorder(
        output_dir=output_dir,
        episode_id=episode_id,
        task_name="reaching",
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
        seed=seed,
        object_xy_offset=plan.sample.object_xy_offset,
        object_category_id=scene_assets.object_context.category_id,
        object_variant_id=scene_assets.object_context.variant_id,
        object_label=scene_assets.object_context.label,
        object_usd_path=_repo_relative_path(scene_assets.object_context.usd_path),
        object_grasp_strategy=scene_assets.object_context.grasp_strategy,
        target_source_name=scene_assets.target_source_name,
        object_affordances=list(scene_assets.object_context.affordances),
        object_yaw_relevant=scene_assets.object_context.geometry.yaw_relevant,
        object_planar_aspect_ratio=scene_assets.object_context.geometry.planar_aspect_ratio,
        object_planar_minor_axis_local=scene_assets.object_context.geometry.planar_minor_axis_local,
        object_planar_major_axis_local=scene_assets.object_context.geometry.planar_major_axis_local,
        object_reach_offset_local=plan.spec.object_reach_offset_local,
        reach_success_threshold_m=plan.spec.success_threshold_m,
        max_success_target_displacement_m=plan.spec.max_success_target_displacement_m,
        light_intensity=plan.sample.light_intensity,
        light_color=plan.sample.light_color,
        active_clutter_count=len(plan.clutter_metadata),
        clutter_objects=plan.clutter_metadata,
    )


def _reaching_success_for_env(
    scene: InteractiveScene,
    spec: ReachingTaskSpec,
    latched_reach_pos_w: torch.Tensor,
    env_index: int,
) -> tuple[bool, str]:
    metrics = reaching_success_metrics(
        scene=scene,
        spec=spec,
        target_reach_pos_w=latched_reach_pos_w,
        threshold_m=spec.success_threshold_m,
        max_target_displacement_m=spec.max_success_target_displacement_m,
    )
    success = bool(metrics.success[env_index].item())
    if bool(metrics.reached_latched_target[env_index].item()):
        return success, "latched_target"
    if bool((metrics.reached_live_target & metrics.target_displacement_ok)[env_index].item()):
        return success, "live_target_with_small_displacement"
    return success, "failure"


def _current_arm_posture_bias(robot: Articulation, gain: float) -> PostureBiasCfg:
    joint_names = getattr(robot, "joint_names", None)
    if joint_names is None:
        joint_names = getattr(robot.data, "joint_names", None)
    if joint_names is None:
        raise RuntimeError("Robot joint names are required to latch reaching posture bias.")

    joint_pos = as_torch(robot.data.joint_pos)[0]
    arm_joint_pos = {
        name: float(joint_pos[index].item())
        for index, name in enumerate(joint_names)
        if name.startswith("panda_joint")
    }
    return PostureBiasCfg(joint_pos=arm_joint_pos, gain=gain)


def run_vector_reaching_episodes(
    *,
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    robot: Articulation,
    ik: CartesianIKController,
    gripper: GripperController,
    output_dir: Path,
    episode_ids: list[int],
    episode_plans: list[ReachingEpisodePlan],
    scene_assets_by_episode: dict[int, ReachingSceneAssets],
    asset_bank: ReachingAssetBank,
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
    """Run a wave of reaching episodes in parallel across scene envs."""
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

    reset_reaching_vector_episode(
        sim=sim,
        scene=scene,
        specs=tuple(plan.spec for plan in padded_plans),
        clutter_specs_by_env=tuple(plan.clutter_specs for plan in padded_plans),
        all_object_names=tuple(asset_bank.target_usd_paths),
        all_clutter_names=tuple(asset_bank.clutter_usd_paths),
        active_env_count=active_env_count,
        reset_scene=False,
    )

    shared_light_plan = episode_plans[0]
    set_dome_light(scene, shared_light_plan.sample.light_intensity, shared_light_plan.sample.light_color)

    policy = VectorReachingScriptedPolicy(
        specs=tuple(plan.spec for plan in padded_plans),
        active_env_count=active_env_count,
    )
    policy.bind(scene, robot)
    policy.reset()

    ik.reset()
    ik.set_posture_bias(_current_arm_posture_bias(robot, gain=episode_plans[0].spec.posture_bias_gain))

    sim_dt = sim.get_physics_dt()
    camera_interval_steps = max(1, round(1.0 / (camera_fps * sim_dt)))
    recorders = [
        _make_reaching_recorder(
            output_dir=output_dir,
            episode_id=episode_id,
            plan=plan,
            scene_assets=scene_assets_by_episode[episode_id],
            sim_dt=sim_dt,
            ee_body_id=ik.end_effector_body_id,
            max_steps=max_steps,
            record_cameras=record_cameras,
            record_depth=record_depth,
            camera_width=camera_width,
            camera_height=camera_height,
            camera_fps=camera_fps,
            state_record_stride=state_record_stride,
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

    while simulation_app.is_running() and step < max_steps:
        cmd = policy.step(None, sim_time_s)
        if cmd.target_quat_w is None:
            raise RuntimeError("Vector reaching policy must command target_quat_w to keep wrist orientation fixed.")

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
            raise RuntimeError("Vector reaching policy must return a per-env done tensor.")

        for env_index in range(active_env_count):
            if completed[env_index] or not bool(done_mask[env_index].item()):
                continue
            if not settling[env_index]:
                print(
                    "[INFO] Scripted reaching policy completed execution "
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
            raise RuntimeError(
                f"Vector reaching episodes exceeded max_steps={max_steps} before completion: {incomplete}"
            )
        raise RuntimeError("Simulation stopped before vector reaching episodes completed.")

    saved_dirs = []
    for env_index, (episode_id, plan, recorder) in enumerate(
        zip(episode_ids, episode_plans, recorders, strict=True)
    ):
        success, success_mode = _reaching_success_for_env(
            scene=scene,
            spec=plan.spec,
            latched_reach_pos_w=policy.latched_reach_pos_w,
            env_index=env_index,
        )
        print(f"[INFO] Episode {episode_id} success: {success} (mode: {success_mode})", flush=True)
        saved_dir = recorder.save(success, success_mode=success_mode)
        print(f"[INFO] Saved episode data to: {saved_dir}", flush=True)
        saved_dirs.append(saved_dir)

    return saved_dirs


def collect_reaching_dataset(
    collection_cfg: dict,
    device: str,
    simulation_app,
) -> None:
    """Run the reaching data collection pipeline."""
    seed = int(collection_cfg["seed"])
    pose_randomization = collection_cfg["pose_randomization"]
    object_xy_range = parse_xy_range(pose_randomization["object_xy_range"])

    lighting_randomization = collection_cfg["lighting_randomization"]
    lighting_options = parse_lighting_options(lighting_randomization)
    base_spec_kwargs = {}
    if "success_threshold_m" in collection_cfg:
        base_spec_kwargs["success_threshold_m"] = float(collection_cfg["success_threshold_m"])
    if "max_success_target_displacement_m" in collection_cfg:
        base_spec_kwargs["max_success_target_displacement_m"] = float(collection_cfg["max_success_target_displacement_m"])
    base_spec = ReachingTaskSpec(**base_spec_kwargs)
    sampling_options = ReachingSamplingOptions(
        object_xy_range=object_xy_range,
        object_origin_xy=base_spec.object_pos_local[:2],
        workspace=WorkspaceConstraint(
            robot_base_xy=tuple(float(value) for value in pose_randomization["workspace"]["robot_base_xy"]),
            max_distance_m=float(pose_randomization["workspace"]["max_distance_m"]),
            max_sampling_attempts=int(pose_randomization["workspace"]["max_sampling_attempts"]),
        ),
        lighting=lighting_options,
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
            "[INFO] Camera recording enabled; using one reaching asset-bank scene "
            f"for {num_episodes} episodes instead of configured "
            f"asset_bank_episode_batch_size={requested_asset_bank_episode_batch_size}. "
            "This avoids repeated RTX scene teardown in one Kit process.",
            flush=True,
        )

    saved_episode_dirs: list[Path] = []
    episode_ids = list(range(start_episode_id, start_episode_id + num_episodes))
    scene_assets_by_episode = _sample_all_scene_assets(
        collection_cfg=collection_cfg,
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
        first_assets = scene_assets_by_episode[first_episode_id]
        first_asset_names = _episode_asset_names(asset_bank, first_assets)
        first_episode_plan = _make_episode_plan(
            collection_cfg=collection_cfg,
            scene_assets=first_assets,
            seed=seed,
            episode_id=first_episode_id,
            sampling_options=sampling_options,
            asset_names=first_asset_names,
        )
        validate_reaching_plan(collection_cfg, first_assets, first_episode_plan)
        scene_num_envs = min(num_envs, len(batch_episode_ids))

        scene_cfg = make_reaching_asset_bank_scene_cfg(
            target_usd_paths=asset_bank.target_usd_paths,
            clutter_usd_paths=asset_bank.clutter_usd_paths,
            initial_target_name=first_asset_names.object_name,
            initial_clutter_names=first_asset_names.clutter_names,
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
            ik = CartesianIKController(pose_error_weights=(1.0, 1.0, 1.0, 8.0, 8.0, 8.0))
            gripper = GripperController()

            sim.reset()
            sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
            robot = scene["robot"]
            ik.bind(scene, robot)
            gripper.bind(scene, robot)

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
                    validate_reaching_plan(collection_cfg, scene_assets, episode_plan)
                    inactive_object_names, inactive_clutter_names = _inactive_reaching_asset_names(
                        asset_bank,
                        asset_names,
                    )

                    policy = ReachingScriptedPolicy(spec=episode_plan.spec)
                    policy.bind(scene, robot)

                    reset_reaching_episode(
                        sim=sim,
                        scene=scene,
                        spec=episode_plan.spec,
                        clutter_specs=episode_plan.clutter_specs,
                        inactive_object_names=inactive_object_names,
                        inactive_clutter_names=inactive_clutter_names,
                        reset_scene=False,
                    )

                    set_dome_light(scene, episode_plan.sample.light_intensity, episode_plan.sample.light_color)
                    policy.reset()
                    ik.reset()
                    ik.set_posture_bias(_current_arm_posture_bias(robot, gain=episode_plan.spec.posture_bias_gain))

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
                        object_category_id=scene_assets.object_context.category_id,
                        object_variant_id=scene_assets.object_context.variant_id,
                        object_label=scene_assets.object_context.label,
                        object_usd_path=_repo_relative_path(scene_assets.object_context.usd_path),
                        object_grasp_strategy=scene_assets.object_context.grasp_strategy,
                        target_source_name=scene_assets.target_source_name,
                        object_affordances=list(scene_assets.object_context.affordances),
                        object_yaw_relevant=scene_assets.object_context.geometry.yaw_relevant,
                        object_planar_aspect_ratio=scene_assets.object_context.geometry.planar_aspect_ratio,
                        object_planar_minor_axis_local=scene_assets.object_context.geometry.planar_minor_axis_local,
                        object_planar_major_axis_local=scene_assets.object_context.geometry.planar_major_axis_local,
                        object_reach_offset_local=episode_plan.spec.object_reach_offset_local,
                        reach_success_threshold_m=episode_plan.spec.success_threshold_m,
                        reach_max_target_displacement_m=episode_plan.spec.max_success_target_displacement_m,
                        light_intensity=episode_plan.sample.light_intensity,
                        light_color=episode_plan.sample.light_color,
                        clutter_objects=episode_plan.clutter_metadata,
                    )
                    saved_episode_dirs.append(saved_dir)
            else:
                episode_plans_by_id: dict[int, ReachingEpisodePlan] = {first_episode_id: first_episode_plan}
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
                    validate_reaching_plan(collection_cfg, scene_assets, episode_plan)
                    episode_plans_by_id[episode_id] = episode_plan

                for wave_episode_ids in _episode_waves(batch_episode_ids, scene_num_envs):
                    print(
                        f"[INFO] Starting vector reaching episodes {wave_episode_ids} "
                        f"with num_envs={scene_num_envs}",
                        flush=True,
                    )
                    saved_episode_dirs.extend(
                        run_vector_reaching_episodes(
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
