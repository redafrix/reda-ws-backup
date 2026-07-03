"""Pure-Python validation for collection configs and catalog pools."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Any

from franka_wrist_camera_scene.episode.suite import SuiteMetadata, suite_metadata_from_config
from franka_wrist_camera_scene.objects.candidates import (
    CandidatePool,
    clutter_query,
    limit_clutter_footprint,
    limit_target_width,
    load_candidate_pool,
    target_query,
)
from franka_wrist_camera_scene.objects.selection import variant_affordances
from franka_wrist_camera_scene.scene.clutter import (
    clutter_count_options,
    clutter_slot_count,
    clutter_source_counts,
    normalize_clutter_source_config,
)
from franka_wrist_camera_scene.tasks.placement_compatibility import object_fits_receptacle
from franka_wrist_camera_scene.tasks.sampling import parse_visual_randomization


PREFLIGHT_EPISODES = 16
PICK_PLACE_MIN_CLUTTER_COUNT = 5
PICK_PLACE_MAX_CLUTTER_COUNT = 8
REACHING_CLUTTER_SLOT_COUNT = 12


@dataclass(frozen=True, slots=True)
class CollectionPreflightReport:
    suite: SuiteMetadata
    target_objects: CandidatePool
    placement_targets: CandidatePool | None
    clutter: CandidatePool | None
    compatible_pairs: tuple[tuple[tuple[str, str], tuple[str, str]], ...]


def _pick_place_target_pool(config: dict[str, Any]) -> CandidatePool:
    target_config = config["target_object"]
    pool = limit_target_width(
        load_candidate_pool("target_object", target_query(target_config)),
        float(target_config["max_planar_minor_extent_m"]),
    )
    if not pool.candidates:
        raise ValueError("Pick-place target pool is empty.")
    return pool


def _validate_receptacles(pool: CandidatePool) -> None:
    if not pool.candidates:
        raise ValueError(f"Receptacle candidate pool {pool.name!r} is empty.")
    for candidate in pool.candidates:
        affordances = variant_affordances(candidate.category, candidate.variant)
        if "physical_container" not in affordances:
            raise ValueError(f"Receptacle {candidate.key} is not a physical container.")
        if candidate.category.label.lower() == "cup":
            raise ValueError(f"Cup {candidate.key} cannot be a physical receptacle.")


def _combined_clutter_pool(config: dict[str, Any], prefix: str = "clutter") -> CandidatePool:
    pools: list[CandidatePool] = []
    for source_config in config["sources"]:
        source_name = source_config["name"]
        merged_config = normalize_clutter_source_config(config, source_config)
        pool = limit_clutter_footprint(
            load_candidate_pool(f"{prefix}:{source_name}", target_query(merged_config)),
            float(config["max_footprint_radius_m"]),
            float(config["clutter_margin_m"]),
        )
        pools.append(pool)

    candidates = tuple(candidate for pool in pools for candidate in pool.candidates)
    if not candidates:
        raise ValueError(f"Candidate pool {prefix!r} is empty.")
    return CandidatePool(prefix, candidates)


def _sample_compatible_pairs(
    config: dict[str, Any],
    targets: CandidatePool,
    receptacles: CandidatePool,
) -> tuple[tuple[tuple[str, str], tuple[str, str]], ...]:
    compatibility = config["object_receptacle_compatibility"]
    max_attempts = int(compatibility["max_sampling_attempts"])
    max_height_to_width = float(compatibility["max_height_to_receptacle_width"])
    seed = int(config["seed"])
    pairs: list[tuple[tuple[str, str], tuple[str, str]]] = []

    for episode_id in range(PREFLIGHT_EPISODES):
        target_rng = random.Random(seed + episode_id)
        receptacle_rng = random.Random(seed + 100_000 + episode_id)
        for _ in range(max_attempts):
            target = target_rng.choice(targets.candidates)
            receptacle = receptacle_rng.choice(receptacles.candidates)
            if object_fits_receptacle(
                target.geometry,
                receptacle.geometry,
                max_height_to_width,
            ):
                pairs.append((target.key, receptacle.key))
                break
        else:
            raise ValueError(
                f"No compatible target/receptacle pair for preflight episode {episode_id}."
            )

    return tuple(pairs)


def load_reaching_target_pool(config: dict[str, Any]) -> CandidatePool:
    """Validate reaching target config and load candidate target pools."""
    if "target_sources" not in config:
        raise ValueError("Reaching configs must define explicit target_sources.")
    target_pools = []
    for sc in config["target_sources"]:
        for field in ["catalog_config", "geometry_config", "category_id", "variant_id"]:
            if field not in sc:
                raise ValueError(f"Reaching target source {sc['name']!r} is missing explicit field {field!r}.")
        pool = load_candidate_pool(f"reaching_target:{sc['name']}", target_query(sc))
        if any(aff in sc.get("required_affordances", []) for aff in ["container", "physical_container"]):
            _validate_receptacles(pool)
        target_pools.append(pool)
    candidates = tuple(candidate for pool in target_pools for candidate in pool.candidates)
    targets = CandidatePool("reaching_targets", candidates)
    if not targets.candidates:
        raise ValueError("Reaching target pool is empty.")
    return targets


def validate_reaching_clutter_exclusions(config: dict[str, Any], clutter_config: dict[str, Any]) -> None:
    """Simulate episode generation and ensure clutter source pools remain non-empty after exclusions."""
    seed = int(config["seed"])
    from franka_wrist_camera_scene.scene.object_context import load_catalog_object_context
    for episode_id in range(PREFLIGHT_EPISODES):
        rng = random.Random(seed + episode_id)
        sources = config["target_sources"]
        weights = [float(s.get("weight", 1.0)) for s in sources]
        source_cfg = rng.choices(sources, weights=weights, k=1)[0]
        target_cfg = source_cfg

        object_context = load_catalog_object_context(
            target_cfg["catalog_config"],
            target_cfg["geometry_config"],
            target_cfg["category_id"],
            target_cfg["variant_id"],
            target_cfg["split"],
            target_cfg["role"],
            tuple(target_cfg["required_affordances"]),
            target_cfg["required_grasp_strategy"],
            rng,
        )

        exclude_target_variant = clutter_config.get("exclude_target_variant", True)
        exclude_target_label = clutter_config.get("exclude_target_label", True)
        unique_labels = bool(clutter_config.get("unique_labels", False))

        excluded_keys = ()
        if exclude_target_variant:
            excluded_keys = ((object_context.category_id, object_context.variant_id),)
        excluded_category_ids = ()
        excluded_labels = ()
        if exclude_target_label:
            excluded_category_ids = (object_context.category_id,)
            excluded_labels = (object_context.label,)

        _validate_clutter_source_capacity(
            clutter_config=clutter_config,
            excluded_keys=excluded_keys,
            excluded_category_ids=excluded_category_ids,
            excluded_labels=excluded_labels,
            active_count=max(clutter_count_options(clutter_config)),
            context=f"reaching target={object_context.category_id}/{object_context.variant_id}",
        )


def _validate_clutter_source_capacity(
    clutter_config: dict[str, Any],
    excluded_keys: tuple[tuple[str, str], ...],
    excluded_category_ids: tuple[str, ...],
    excluded_labels: tuple[str, ...],
    active_count: int,
    context: str,
) -> None:
    unique_labels = bool(clutter_config.get("unique_labels", False))
    blocked_keys = set(excluded_keys)
    blocked_category_ids = set(excluded_category_ids)
    blocked_labels = set(excluded_labels)
    for source_name, count, source_cfg in clutter_source_counts(clutter_config, active_count):
        if count == 0:
            continue
        raw_pool = load_candidate_pool(f"clutter:{source_name}", target_query(source_cfg))
        filtered_candidates = [
            candidate
            for candidate in raw_pool.candidates
            if candidate.key not in blocked_keys
            and candidate.category.id not in blocked_category_ids
            and candidate.label not in blocked_labels
        ]
        if not filtered_candidates:
            if source_cfg.get("min_count", 0) == 0:
                continue
            raise ValueError(
                f"Clutter source pool {source_name!r} is empty after exclusions for {context}."
            )
        if unique_labels:
            unique_filtered_labels = {candidate.label for candidate in filtered_candidates}
            if len(unique_filtered_labels) < count:
                if source_cfg.get("min_count", 0) == 0:
                    continue
                raise ValueError(
                    f"Clutter source pool {source_name!r} does not have enough unique labels "
                    f"({len(unique_filtered_labels)}) to satisfy requested count ({count}) "
                    f"after exclusions for {context}."
                )
            selected_candidates = []
            selected_labels = set()
            for candidate in sorted(
                filtered_candidates,
                key=lambda item: (item.label, item.category.id, item.variant.id),
            ):
                if candidate.label in selected_labels:
                    continue
                selected_candidates.append(candidate)
                selected_labels.add(candidate.label)
                if len(selected_candidates) == count:
                    break
        else:
            if len(filtered_candidates) < count and source_cfg.get("min_count", 0) != 0:
                raise ValueError(
                    f"Clutter source pool {source_name!r} has only {len(filtered_candidates)} "
                    f"candidates for requested count ({count}) after exclusions for {context}."
                )
            selected_candidates = filtered_candidates[:count]

        blocked_keys.update(candidate.key for candidate in selected_candidates)
        if unique_labels:
            blocked_category_ids.update(candidate.category.id for candidate in selected_candidates)
            blocked_labels.update(candidate.label for candidate in selected_candidates)


def validate_pick_place_clutter(config: dict[str, Any]) -> CandidatePool:
    """Validate pick-place clutter config constraints."""
    clutter_config = config["clutter"]
    if not bool(clutter_config.get("unique_labels", False)):
        raise ValueError(
            "Pick-place collection requires clutter.unique_labels=true to avoid language ambiguity."
        )
    count_options = clutter_count_options(clutter_config)
    if min(count_options) < PICK_PLACE_MIN_CLUTTER_COUNT or max(count_options) > PICK_PLACE_MAX_CLUTTER_COUNT:
        raise ValueError(
            "pick-place clutter.count_options must stay within "
            f"[{PICK_PLACE_MIN_CLUTTER_COUNT}, {PICK_PLACE_MAX_CLUTTER_COUNT}], "
            f"got count_options={count_options}."
        )
    if "sources" in clutter_config:
        for active_count in count_options:
            clutter_source_counts(clutter_config, active_count)

    clutter = limit_clutter_footprint(
        load_candidate_pool("clutter", clutter_query(clutter_config)),
        float(clutter_config["max_footprint_radius_m"]),
        float(clutter_config["clutter_margin_m"]),
    )
    if not clutter.candidates:
        raise ValueError("Pick-place clutter candidate pool is empty.")
    return clutter


def validate_pick_place_clutter_exclusions(
    config: dict[str, Any],
    clutter_config: dict[str, Any],
    targets: CandidatePool,
    receptacles: CandidatePool,
) -> None:
    """Validate pick-place clutter pools after active target and receptacle exclusions."""
    compatibility = config["object_receptacle_compatibility"]
    max_attempts = int(compatibility["max_sampling_attempts"])
    max_height_to_width = float(compatibility["max_height_to_receptacle_width"])
    seed = int(config["seed"])
    active_count = max(clutter_count_options(clutter_config))

    for episode_id in range(PREFLIGHT_EPISODES):
        target_rng = random.Random(seed + episode_id)
        receptacle_rng = random.Random(seed + 100_000 + episode_id)
        object_candidate = None
        receptacle_candidate = None
        for _ in range(max_attempts):
            candidate_object = target_rng.choice(targets.candidates)
            candidate_receptacle = receptacle_rng.choice(receptacles.candidates)
            if candidate_object.label == candidate_receptacle.label:
                continue
            if object_fits_receptacle(
                candidate_object.geometry,
                candidate_receptacle.geometry,
                max_height_to_width,
            ):
                object_candidate = candidate_object
                receptacle_candidate = candidate_receptacle
                break
        if object_candidate is None or receptacle_candidate is None:
            continue

        _validate_clutter_source_capacity(
            clutter_config=clutter_config,
            excluded_keys=(object_candidate.key, receptacle_candidate.key),
            excluded_category_ids=(object_candidate.category.id, receptacle_candidate.category.id),
            excluded_labels=(object_candidate.label, receptacle_candidate.label),
            active_count=active_count,
            context=(
                f"pick_place target={object_candidate.category.id}/{object_candidate.variant.id} "
                f"and receptacle={receptacle_candidate.category.id}/{receptacle_candidate.variant.id}"
            ),
        )


def validate_reaching_config(config: dict[str, Any]) -> CollectionPreflightReport:
    """Validate reaching configuration parameters and candidate pools."""
    suite = suite_metadata_from_config(config)
    targets = load_reaching_target_pool(config)

    clutter_config = config.get("clutter")
    clutter = None
    if clutter_config is not None:
        if not bool(clutter_config.get("unique_labels", False)):
            raise ValueError(
                "Reaching collection requires clutter.unique_labels=true to avoid language ambiguity."
            )
        if clutter_slot_count(clutter_config) != REACHING_CLUTTER_SLOT_COUNT:
            raise ValueError(f"reaching clutter.slot_count must be {REACHING_CLUTTER_SLOT_COUNT}.")

        count_opts = clutter_count_options(clutter_config)
        if not count_opts:
            raise ValueError("reaching clutter count_options must be non-empty.")
        if min(count_opts) < 1:
            raise ValueError(
                f"reaching clutter count_options minimum value must be >= 1 to avoid unallocated slots, got count_options={count_opts}."
            )
        for active_count in count_opts:
            clutter_source_counts(clutter_config, active_count)

        clutter = _combined_clutter_pool(clutter_config, "reaching_clutter")
        validate_reaching_clutter_exclusions(config, clutter_config)

    return CollectionPreflightReport(suite, targets, None, clutter, ())


def validate_pick_place_config(config: dict[str, Any]) -> CollectionPreflightReport:
    """Validate pick-place configuration parameters and candidate pools."""
    suite = suite_metadata_from_config(config)
    targets = _pick_place_target_pool(config)
    receptacles = load_candidate_pool(
        "placement_target",
        target_query(config["placement_target"]),
    )
    _validate_receptacles(receptacles)

    clutter = validate_pick_place_clutter(config)
    validate_pick_place_clutter_exclusions(config, config["clutter"], targets, receptacles)
    compatible_pairs = _sample_compatible_pairs(config, targets, receptacles)

    return CollectionPreflightReport(
        suite,
        targets,
        receptacles,
        clutter,
        compatible_pairs,
    )


def validate_collection_config(config: dict[str, Any]) -> CollectionPreflightReport:
    """Validate task-agnostic configuration and delegate to specific validate functions."""
    parse_visual_randomization(config.get("visual_randomization"))

    if "clutter" in config and "sources" in config["clutter"]:
        for sc in config["clutter"]["sources"]:
            for field in ["category_id", "variant_id"]:
                if field not in sc:
                    raise ValueError(f"Clutter source {sc['name']!r} is missing explicit field {field!r}.")

    if config["task"] == "reaching":
        return validate_reaching_config(config)
    elif config["task"] == "pick_place":
        return validate_pick_place_config(config)
    else:
        raise ValueError(f"Unsupported collection task: {config['task']!r}")
