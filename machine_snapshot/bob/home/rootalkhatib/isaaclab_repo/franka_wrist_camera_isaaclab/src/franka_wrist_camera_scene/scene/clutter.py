"""Geometry-aware deterministic tabletop clutter sampling."""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Any

from franka_wrist_camera_scene.scene.object_context import (
    CatalogObjectContext,
    load_catalog_object_context,
)
from franka_wrist_camera_scene.tasks.placement_geometry import object_root_pose_on_support
from franka_wrist_camera_scene.tasks.layout_geometry import (
    FootprintCircle,
    footprints_overlap_xy,
    planar_footprint_radius_from_bbox,
)

CONTAINER_EXCLUSION_AFFORDANCES = frozenset(("container", "physical_container", "support"))
CONTAINER_EXCLUSION_CATEGORY_IDS = frozenset(("basket", "bin", "bowl", "box", "cup", "plate", "tray"))


class ClutterLayoutSamplingError(RuntimeError):
    """Raised when clutter layout sampling cannot find a valid placement."""


@dataclass(frozen=True, slots=True)
class XYRange:
    x: tuple[float, float]
    y: tuple[float, float]


@dataclass(frozen=True, slots=True)
class FootprintDisk:
    xy: tuple[float, float]
    radius_m: float


@dataclass(frozen=True, slots=True)
class ClutterObjectSpec:
    prim_name: str
    context: CatalogObjectContext
    pos_local: tuple[float, float, float]
    footprint_radius_m: float
    source_name: str | None = None


def parse_xy_range(config: dict[str, Any]) -> XYRange:
    x_range = config["x"]
    y_range = config["y"]

    parsed = XYRange(
        x=(float(x_range[0]), float(x_range[1])),
        y=(float(y_range[0]), float(y_range[1])),
    )

    if parsed.x[1] <= parsed.x[0]:
        raise ValueError(f"Invalid clutter x range: {x_range}")
    if parsed.y[1] <= parsed.y[0]:
        raise ValueError(f"Invalid clutter y range: {y_range}")

    return parsed


def xy_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def planar_footprint_radius_m(
    bbox_min: tuple[float, float, float],
    bbox_max: tuple[float, float, float],
    margin_m: float,
) -> float:
    return planar_footprint_radius_from_bbox(bbox_min, bbox_max, margin_m)


def footprints_overlap(a: FootprintDisk, b: FootprintDisk) -> bool:
    return footprints_overlap_xy(
        FootprintCircle(name="a", xy=a.xy, radius_m=a.radius_m),
        FootprintCircle(name="b", xy=b.xy, radius_m=b.radius_m),
    )


def footprint_inside_xy_range(candidate: FootprintDisk, xy_range: XYRange) -> bool:
    x, y = candidate.xy
    r = candidate.radius_m
    return (
        x - r >= xy_range.x[0]
        and x + r <= xy_range.x[1]
        and y - r >= xy_range.y[0]
        and y + r <= xy_range.y[1]
    )


def _grid_search_non_overlapping_xy(
    xy_range: XYRange,
    candidate_radius_m: float,
    occupied: tuple[FootprintDisk, ...],
    grid_step_m: float,
) -> tuple[float, float] | None:
    if grid_step_m <= 0.0:
        raise ValueError(f"grid_step_m must be positive, got {grid_step_m}")

    x = xy_range.x[0] + candidate_radius_m
    x_limit = xy_range.x[1] - candidate_radius_m
    while x <= x_limit + 1e-9:
        y = xy_range.y[0] + candidate_radius_m
        y_limit = xy_range.y[1] - candidate_radius_m
        while y <= y_limit + 1e-9:
            candidate = FootprintDisk(xy=(x, y), radius_m=candidate_radius_m)
            if footprint_inside_xy_range(candidate, xy_range) and all(
                not footprints_overlap(candidate, existing) for existing in occupied
            ):
                return (x, y)
            y += grid_step_m
        x += grid_step_m

    return None


def sample_non_overlapping_xy(
    rng: random.Random,
    xy_range: XYRange,
    candidate_radius_m: float,
    occupied: tuple[FootprintDisk, ...],
    max_attempts: int,
    grid_step_m: float = 0.01,
) -> tuple[float, float]:
    if candidate_radius_m <= 0.0:
        raise ValueError(f"candidate_radius_m must be positive, got {candidate_radius_m}")
    if max_attempts <= 0:
        raise ValueError(f"max_attempts must be positive, got {max_attempts}")

    for _ in range(max_attempts):
        xy = (
            rng.uniform(xy_range.x[0], xy_range.x[1]),
            rng.uniform(xy_range.y[0], xy_range.y[1]),
        )
        candidate = FootprintDisk(xy=xy, radius_m=candidate_radius_m)

        if not footprint_inside_xy_range(candidate, xy_range):
            continue

        if all(not footprints_overlap(candidate, existing) for existing in occupied):
            return xy

    grid_xy = _grid_search_non_overlapping_xy(
        xy_range=xy_range,
        candidate_radius_m=candidate_radius_m,
        occupied=occupied,
        grid_step_m=grid_step_m,
    )
    if grid_xy is not None:
        return grid_xy

    occupied_summary = [
        {"xy": disk.xy, "radius_m": disk.radius_m}
        for disk in occupied
    ]
    raise ClutterLayoutSamplingError(
        "Failed to sample a non-overlapping clutter position "
        f"after {max_attempts} random attempts and a deterministic grid search. "
        f"candidate_radius_m={candidate_radius_m}, "
        f"xy_range={xy_range}, occupied={occupied_summary}"
    )


def sample_reaching_clutter_xy(
    rng: random.Random,
    xy_range: XYRange,
    target_disk: FootprintDisk,
    candidate_target_clearance_radius_m: float,
    candidate_clutter_radius_m: float,
    occupied_clutter: tuple[FootprintDisk, ...],
    max_attempts: int,
    grid_step_m: float = 0.01,
) -> tuple[float, float]:
    if candidate_target_clearance_radius_m <= 0.0:
        raise ValueError(
            "candidate_target_clearance_radius_m must be positive, "
            f"got {candidate_target_clearance_radius_m}"
        )
    if candidate_clutter_radius_m <= 0.0:
        raise ValueError(f"candidate_clutter_radius_m must be positive, got {candidate_clutter_radius_m}")
    if max_attempts <= 0:
        raise ValueError(f"max_attempts must be positive, got {max_attempts}")

    def candidate_is_valid(xy: tuple[float, float]) -> bool:
        clutter_disk = FootprintDisk(xy=xy, radius_m=candidate_clutter_radius_m)
        if not footprint_inside_xy_range(clutter_disk, xy_range):
            return False
        target_clearance_disk = FootprintDisk(xy=xy, radius_m=candidate_target_clearance_radius_m)
        if footprints_overlap(target_clearance_disk, target_disk):
            return False
        return all(not footprints_overlap(clutter_disk, existing) for existing in occupied_clutter)

    for _ in range(max_attempts):
        xy = (
            rng.uniform(xy_range.x[0], xy_range.x[1]),
            rng.uniform(xy_range.y[0], xy_range.y[1]),
        )
        if candidate_is_valid(xy):
            return xy

    x = xy_range.x[0] + candidate_clutter_radius_m
    x_limit = xy_range.x[1] - candidate_clutter_radius_m
    while x <= x_limit + 1e-9:
        y = xy_range.y[0] + candidate_clutter_radius_m
        y_limit = xy_range.y[1] - candidate_clutter_radius_m
        while y <= y_limit + 1e-9:
            if candidate_is_valid((x, y)):
                return (x, y)
            y += grid_step_m
        x += grid_step_m

    occupied_summary = [
        {"xy": disk.xy, "radius_m": disk.radius_m}
        for disk in occupied_clutter
    ]
    raise ClutterLayoutSamplingError(
        "Failed to sample a reaching clutter position after "
        f"{max_attempts} random attempts and a deterministic grid search. "
        f"candidate_target_clearance_radius_m={candidate_target_clearance_radius_m}, "
        f"candidate_clutter_radius_m={candidate_clutter_radius_m}, "
        f"target={target_disk}, xy_range={xy_range}, occupied_clutter={occupied_summary}"
    )


def footprint_for_context(
    context: CatalogObjectContext,
    margin_m: float,
) -> float:
    return planar_footprint_radius_m(
        bbox_min=context.geometry.local_bbox_min,
        bbox_max=context.geometry.local_bbox_max,
        margin_m=margin_m,
    )


def layout_margin_for_context(
    context: CatalogObjectContext,
    base_margin_m: float,
    clutter_cfg: dict[str, Any],
) -> float:
    extra_margin_m = float(clutter_cfg.get("container_exclusion_extra_margin_m", 0.0))
    affordances = set(getattr(context, "affordances", ()))
    category_id = str(getattr(context, "category_id", "")).lower()
    label = str(getattr(context, "label", "")).lower()
    if (
        CONTAINER_EXCLUSION_AFFORDANCES.intersection(affordances)
        or category_id in CONTAINER_EXCLUSION_CATEGORY_IDS
        or label in CONTAINER_EXCLUSION_CATEGORY_IDS
    ):
        return base_margin_m + extra_margin_m
    return base_margin_m


def layout_footprint_for_context(
    context: CatalogObjectContext,
    base_margin_m: float,
    clutter_cfg: dict[str, Any],
) -> float:
    return footprint_for_context(
        context,
        margin_m=layout_margin_for_context(context, base_margin_m, clutter_cfg),
    )


def validate_unique_active_labels(
    target_context: CatalogObjectContext,
    clutter_specs: tuple[ClutterObjectSpec, ...],
) -> None:
    validate_unique_active_scene_labels(
        named_contexts=(("target", target_context),),
        clutter_specs=clutter_specs,
    )


def validate_unique_active_scene_labels(
    named_contexts: tuple[tuple[str, CatalogObjectContext], ...],
    clutter_specs: tuple[ClutterObjectSpec, ...],
) -> None:
    """Reject ambiguous active scenes with repeated visual labels or exact assets."""
    labels = [getattr(context, "label") for _, context in named_contexts] + [
        getattr(spec.context, "label") for spec in clutter_specs
    ]
    duplicates = sorted({label for label in labels if labels.count(label) > 1})
    if duplicates:
        raise ValueError(f"Active scene has duplicate visual labels: {duplicates}")

    keys = []
    for _, context in named_contexts:
        if hasattr(context, "category_id") and hasattr(context, "variant_id"):
            keys.append((context.category_id, context.variant_id))
    for spec in clutter_specs:
        context = spec.context
        if hasattr(context, "category_id") and hasattr(context, "variant_id"):
            keys.append((context.category_id, context.variant_id))
    duplicate_keys = sorted({key for key in keys if keys.count(key) > 1})
    if duplicate_keys:
        raise ValueError(f"Active scene has duplicate object assets: {duplicate_keys}")


def _context_key(context: CatalogObjectContext) -> tuple[str, str]:
    return (context.category_id, context.variant_id)


def normalize_clutter_source_config(
    clutter_cfg: dict[str, Any],
    source_cfg: dict[str, Any],
) -> dict[str, Any]:
    res = {
        "catalog_config": clutter_cfg["catalog_config"],
        "geometry_config": clutter_cfg["geometry_config"],
        "category_id": source_cfg["category_id"],
        "variant_id": source_cfg["variant_id"],
        "split": source_cfg["split"],
        "role": source_cfg["role"],
        "required_affordances": source_cfg["required_affordances"],
        "required_grasp_strategy": source_cfg["required_grasp_strategy"],
    }
    if "max_count" in source_cfg:
        res["max_count"] = source_cfg["max_count"]
    return res


def clutter_slot_count(clutter_cfg: dict[str, Any]) -> int:
    if "slot_count" in clutter_cfg:
        return int(clutter_cfg["slot_count"])
    if "count" in clutter_cfg:
        return int(clutter_cfg["count"])
    if "count_options" in clutter_cfg:
        count_options = tuple(int(count) for count in clutter_cfg["count_options"])
        if not count_options:
            raise ValueError("clutter.count_options must not be empty.")
        return max(count_options)
    raise ValueError("clutter config must define one of slot_count, count, or count_options.")


def clutter_count_options(clutter_cfg: dict[str, Any]) -> tuple[int, ...]:
    if "count_options" not in clutter_cfg:
        return (int(clutter_cfg["count"]),)

    count_options = tuple(int(count) for count in clutter_cfg["count_options"])
    if not count_options:
        raise ValueError("clutter.count_options must not be empty.")

    slot_count = clutter_slot_count(clutter_cfg)
    for count in count_options:
        if count < 0 or count > slot_count:
            raise ValueError(
                f"clutter.count_options values must be within [0, {slot_count}], got {count}."
            )
    return count_options


def sample_clutter_count(clutter_cfg: dict[str, Any], seed: int, episode_id: int) -> int:
    count_options = clutter_count_options(clutter_cfg)
    rng = random.Random(seed + 400_000 + episode_id)
    return rng.choice(count_options)


def _source_min_count(source_cfg: dict[str, Any]) -> int:
    if "min_count" not in source_cfg:
        raise ValueError("Clutter source config must define explicit 'min_count'.")
    return int(source_cfg["min_count"])


def _source_weight(source_cfg: dict[str, Any], min_count: int) -> float:
    return float(source_cfg.get("weight", max(1, min_count)))


def _allocate_source_counts(
    sources: list[tuple[str, dict[str, Any]]],
    active_count: int,
) -> tuple[tuple[str, int, dict[str, Any]], ...]:
    min_counts = []
    max_counts = []
    weights = []

    for name, source_cfg in sources:
        min_c = _source_min_count(source_cfg)
        min_counts.append(min_c)

        max_c = source_cfg.get("max_count")
        if max_c is not None:
            max_c = int(max_c)
            if max_c < min_c:
                raise ValueError(f"max_count ({max_c}) cannot be less than min_count ({min_c}) for source {name!r}.")
        max_counts.append(max_c)

        w = _source_weight(source_cfg, min_c)
        if w <= 0.0:
            raise ValueError(f"Clutter source weights must be positive, got weight={w} for source {name!r}.")
        weights.append(w)

    min_total = sum(min_counts)
    if active_count < min_total:
        raise ValueError(
            "Active clutter count is smaller than source minimums. "
            f"active_count={active_count}, source_min_total={min_total}"
        )

    max_total = 0
    has_infinite_capacity = False
    for max_c in max_counts:
        if max_c is None:
            has_infinite_capacity = True
        else:
            max_total += max_c
    if not has_infinite_capacity and max_total < active_count:
        raise ValueError(
            f"Active clutter count {active_count} exceeds the total maximum capacity {max_total} of all sources combined."
        )

    counts = list(min_counts)
    extra_count = active_count - min_total

    for _ in range(extra_count):
        active_indices = [
            i for i in range(len(sources))
            if max_counts[i] is None or counts[i] < max_counts[i]
        ]
        if not active_indices:
            raise ValueError("No capacity for remaining extras after respecting max_count.")

        best_index = min(
            active_indices,
            key=lambda idx: ((counts[idx] - min_counts[idx]) / weights[idx], idx),
        )
        counts[best_index] += 1

    return tuple(
        (source_name, count, source_cfg)
        for (source_name, source_cfg), count in zip(sources, counts, strict=True)
    )


def clutter_source_counts(
    clutter_cfg: dict[str, Any],
    active_count: int | None = None,
) -> tuple[tuple[str, int, dict[str, Any]], ...]:
    """Return named clutter source configs and requested counts."""
    requested_count = int(active_count) if active_count is not None else max(clutter_count_options(clutter_cfg))

    sources: list[tuple[str, dict[str, Any]]] = []
    for source_cfg in clutter_cfg["sources"]:
        source_name = str(source_cfg["name"])
        min_count = _source_min_count(source_cfg)
        if min_count < 0:
            raise ValueError(f"clutter source {source_name!r} count must be non-negative.")
        sources.append((source_name, normalize_clutter_source_config(clutter_cfg, source_cfg) | {
            "min_count": min_count,
            "weight": _source_weight(source_cfg, min_count),
        }))

    return _allocate_source_counts(sources, requested_count)



def sample_clutter_contexts(
    clutter_cfg: dict[str, Any],
    rng: random.Random,
    count: int,
    excluded_keys: tuple[tuple[str, str], ...] = (),
    excluded_category_ids: tuple[str, ...] = (),
    excluded_labels: tuple[str, ...] = (),
) -> tuple[CatalogObjectContext, ...]:
    if count == 0:
        return ()

    contexts: list[CatalogObjectContext] = []
    max_attempts = int(clutter_cfg["max_asset_sampling_attempts"])
    max_footprint_radius_m = float(clutter_cfg["max_footprint_radius_m"])
    clutter_margin_m = float(clutter_cfg["clutter_margin_m"])
    unique_labels = bool(clutter_cfg.get("unique_labels", False))
    blocked_keys = set(excluded_keys)
    blocked_category_ids = set(excluded_category_ids)
    blocked_labels = set(excluded_labels)

    for _ in range(max_attempts):
        context = load_catalog_object_context(
            catalog_config=clutter_cfg["catalog_config"],
            geometry_config=clutter_cfg["geometry_config"],
            category_id=clutter_cfg["category_id"],
            variant_id=clutter_cfg["variant_id"],
            split=clutter_cfg["split"],
            role=clutter_cfg["role"],
            required_affordances=tuple(clutter_cfg["required_affordances"]),
            required_grasp_strategy=clutter_cfg["required_grasp_strategy"],
            rng=rng,
            excluded_category_ids=tuple(blocked_category_ids),
            excluded_labels=tuple(blocked_labels),
        )
        if _context_key(context) in blocked_keys:
            continue
        if footprint_for_context(context, margin_m=clutter_margin_m) > max_footprint_radius_m:
            continue

        contexts.append(context)
        blocked_keys.add(_context_key(context))
        if unique_labels:
            blocked_category_ids.add(context.category_id)
            blocked_labels.add(context.label)
        if len(contexts) == count:
            return tuple(contexts)

    raise RuntimeError(
        "Failed to sample enough clutter assets within the configured footprint limit. "
        f"count={count}, max_attempts={max_attempts}, "
        f"max_footprint_radius_m={max_footprint_radius_m}"
    )


def sample_clutter_contexts_from_sources(
    clutter_cfg: dict[str, Any],
    rng: random.Random,
    active_count: int | None = None,
    excluded_keys: tuple[tuple[str, str], ...] = (),
    excluded_category_ids: tuple[str, ...] = (),
    excluded_labels: tuple[str, ...] = (),
) -> tuple[tuple[str, CatalogObjectContext], ...]:
    """Sample clutter contexts from explicit named source counts."""
    sampled: list[tuple[str, CatalogObjectContext]] = []
    blocked_keys = set(excluded_keys)
    unique_labels = bool(clutter_cfg.get("unique_labels", False))
    blocked_category_ids = set(excluded_category_ids)
    blocked_labels = set(excluded_labels)
    for source_name, count, source_cfg in clutter_source_counts(clutter_cfg, active_count):
        if count > 0:
            try:
                source_contexts = sample_clutter_contexts(
                    clutter_cfg={**clutter_cfg, **source_cfg},
                    rng=rng,
                    count=count,
                    excluded_keys=tuple(blocked_keys),
                    excluded_category_ids=tuple(blocked_category_ids),
                    excluded_labels=tuple(blocked_labels),
                )
            except ValueError as e:
                if source_cfg.get("min_count", 0) == 0:
                    print(
                        f"[WARNING] Skipping optional clutter source {source_name!r} because no variants "
                        f"match the query after target exclusions. Error: {e}",
                        flush=True,
                    )
                    source_contexts = ()
                else:
                    raise e
        else:
            source_contexts = ()

        sampled.extend((source_name, context) for context in source_contexts)
        blocked_keys.update(_context_key(context) for context in source_contexts)
        if unique_labels:
            blocked_category_ids.update(context.category_id for context in source_contexts)
            blocked_labels.update(context.label for context in source_contexts)
    return tuple(sampled)


def _sort_clutter_slots_by_descending_footprint(
    sampled_slots: list[tuple[int, CatalogObjectContext, float]],
) -> list[tuple[int, CatalogObjectContext, float]]:
    return sorted(sampled_slots, key=lambda item: (-item[2], item[0]))


def place_clutter_contexts(
    clutter_cfg: dict[str, Any],
    rng: random.Random,
    support_surface_z_local: float,
    object_bottom_clearance_m: float,
    target_object_context: CatalogObjectContext,
    target_object_xy: tuple[float, float],
    placement_target_context: CatalogObjectContext,
    placement_target_xy: tuple[float, float],
    clutter_contexts: tuple[CatalogObjectContext, ...],
) -> tuple[ClutterObjectSpec, ...]:
    active_count = len(clutter_contexts)
    if active_count not in clutter_count_options(clutter_cfg):
        raise ValueError(
            f"Unexpected active pick-place clutter count: {active_count}."
        )
    xy_range = parse_xy_range(clutter_cfg["xy_range"])
    max_attempts = int(clutter_cfg["max_layout_sampling_attempts"])
    grid_step_m = float(clutter_cfg["grid_step_m"])

    occupied: list[FootprintDisk] = [
        FootprintDisk(
            xy=target_object_xy,
            radius_m=footprint_for_context(
                target_object_context,
                margin_m=layout_margin_for_context(
                    target_object_context,
                    float(clutter_cfg["object_margin_m"]),
                    clutter_cfg,
                ),
            ),
        ),
        FootprintDisk(
            xy=placement_target_xy,
            radius_m=footprint_for_context(
                placement_target_context,
                margin_m=layout_margin_for_context(
                    placement_target_context,
                    float(clutter_cfg["placement_target_margin_m"]),
                    clutter_cfg,
                ),
            ),
        ),
    ]

    clutter_margin_m = float(clutter_cfg["clutter_margin_m"])
    sampled_slots: list[tuple[int, CatalogObjectContext, float]] = []

    for clutter_index, context in enumerate(clutter_contexts):
        footprint_radius = layout_footprint_for_context(context, clutter_margin_m, clutter_cfg)
        sampled_slots.append((clutter_index, context, footprint_radius))

    placement_order = _sort_clutter_slots_by_descending_footprint(sampled_slots)
    placed_xy: dict[int, tuple[float, float]] = {}

    for clutter_index, context, footprint_radius in placement_order:
        xy = sample_non_overlapping_xy(
            rng=rng,
            xy_range=xy_range,
            candidate_radius_m=footprint_radius,
            occupied=tuple(occupied),
            max_attempts=max_attempts,
            grid_step_m=grid_step_m,
        )
        placed_xy[clutter_index] = xy
        occupied.append(FootprintDisk(xy=xy, radius_m=footprint_radius))

    specs: list[ClutterObjectSpec] = []
    for clutter_index, context, footprint_radius in sampled_slots:
        xy = placed_xy[clutter_index]
        pos_local = object_root_pose_on_support(
            xy_pos=xy,
            support_surface_z=support_surface_z_local,
            object_bbox_min_z=context.geometry.local_bbox_min[2],
            bottom_clearance_m=object_bottom_clearance_m,
        )
        specs.append(
            ClutterObjectSpec(
                prim_name=f"ClutterObject{clutter_index}",
                context=context,
                pos_local=pos_local,
                footprint_radius_m=footprint_radius,
            )
        )

    return tuple(specs)


def place_reaching_clutter_contexts(
    clutter_cfg: dict[str, Any],
    rng: random.Random,
    support_surface_z_local: float,
    object_bottom_clearance_m: float,
    target_object_context: CatalogObjectContext,
    target_object_xy: tuple[float, float],
    clutter_contexts: tuple[tuple[str, CatalogObjectContext], ...],
) -> tuple[ClutterObjectSpec, ...]:
    active_count = len(clutter_contexts)
    if active_count not in clutter_count_options(clutter_cfg):
        raise ValueError(f"Unexpected active reaching clutter count: {active_count}.")

    xy_range = parse_xy_range(clutter_cfg["xy_range"])
    target_disk = FootprintDisk(
        xy=target_object_xy,
        radius_m=layout_footprint_for_context(
            target_object_context,
            float(clutter_cfg["object_margin_m"]),
            clutter_cfg,
        ),
    )
    max_attempts = int(clutter_cfg["max_layout_sampling_attempts"])
    grid_step_m = float(clutter_cfg["grid_step_m"])
    clutter_margin_m = float(clutter_cfg["clutter_margin_m"])

    sampled_slots = [
        (
            index,
            source_name,
            context,
            footprint_for_context(context, clutter_margin_m),
            layout_footprint_for_context(context, clutter_margin_m, clutter_cfg),
        )
        for index, (source_name, context) in enumerate(clutter_contexts)
    ]
    placement_order = sorted(sampled_slots, key=lambda item: (-max(item[3], item[4]), item[0]))
    placed_xy: dict[int, tuple[float, float]] = {}
    occupied_clutter: list[FootprintDisk] = []

    for clutter_index, _, _, clutter_radius, target_clearance_radius in placement_order:
        xy = sample_reaching_clutter_xy(
            rng=rng,
            xy_range=xy_range,
            target_disk=target_disk,
            candidate_target_clearance_radius_m=target_clearance_radius,
            candidate_clutter_radius_m=clutter_radius,
            occupied_clutter=tuple(occupied_clutter),
            max_attempts=max_attempts,
            grid_step_m=grid_step_m,
        )
        placed_xy[clutter_index] = xy
        occupied_clutter.append(FootprintDisk(xy=xy, radius_m=clutter_radius))

    specs: list[ClutterObjectSpec] = []
    for clutter_index, source_name, context, footprint_radius, _ in sampled_slots:
        pos_local = object_root_pose_on_support(
            xy_pos=placed_xy[clutter_index],
            support_surface_z=support_surface_z_local,
            object_bbox_min_z=context.geometry.local_bbox_min[2],
            bottom_clearance_m=object_bottom_clearance_m,
        )
        specs.append(
            ClutterObjectSpec(
                prim_name=f"ClutterObject{clutter_index}",
                context=context,
                pos_local=pos_local,
                footprint_radius_m=footprint_radius,
                source_name=source_name,
            )
        )

    return tuple(specs)
