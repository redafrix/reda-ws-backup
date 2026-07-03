"""Deterministic task-parameter sampling."""

from __future__ import annotations

from dataclasses import dataclass
import math
import random

from franka_wrist_camera_scene.settings import TABLE_COLOR


TABLE_COLOR_SEED_OFFSET = 300_000


@dataclass(frozen=True, slots=True)
class XYRange:
    x: tuple[float, float]
    y: tuple[float, float]


@dataclass(frozen=True, slots=True)
class LightingOptions:
    intensity_range: tuple[float, float]
    color_options: tuple[tuple[float, float, float], ...]


@dataclass(frozen=True, slots=True)
class VisualRandomizationOptions:
    table_color_options: tuple[tuple[float, float, float], ...]


@dataclass(frozen=True, slots=True)
class WorkspaceConstraint:
    robot_base_xy: tuple[float, float]
    max_distance_m: float
    max_sampling_attempts: int


@dataclass(frozen=True, slots=True)
class PickPlaceSamplingOptions:
    object_origin_xy: tuple[float, float]
    place_origin_xy: tuple[float, float]
    object_xy_range: XYRange
    place_xy_range: XYRange
    minimum_object_place_distance_m: float
    workspace: WorkspaceConstraint
    lighting: LightingOptions
    visual: VisualRandomizationOptions


@dataclass(frozen=True, slots=True)
class PickPlaceSample:
    object_xy_offset: tuple[float, float]
    place_xy_offset: tuple[float, float]
    light_intensity: float
    light_color: tuple[float, float, float]
    table_color: tuple[float, float, float]


def parse_xy_range(config: dict) -> XYRange:
    return XYRange(
        x=(float(config["x"][0]), float(config["x"][1])),
        y=(float(config["y"][0]), float(config["y"][1])),
    )


def parse_lighting_options(config: dict) -> LightingOptions:
    return LightingOptions(
        intensity_range=(float(config["dome_light_intensity_range"][0]), float(config["dome_light_intensity_range"][1])),
        color_options=tuple(tuple(float(x) for x in color) for color in config["dome_light_color_options"]),
    )


def parse_visual_randomization(config: dict | None) -> VisualRandomizationOptions:
    if config is None:
        return VisualRandomizationOptions(table_color_options=(TABLE_COLOR,))

    table_colors = tuple(
        tuple(float(channel) for channel in color)
        for color in config["table_color_options"]
    )
    if not table_colors:
        raise ValueError("visual_randomization.table_color_options must not be empty.")
    for color in table_colors:
        if len(color) != 3:
            raise ValueError(f"Table colors must contain three channels, got {color!r}.")
        if any(channel < 0.0 or channel > 1.0 for channel in color):
            raise ValueError(f"Table color channels must be within [0, 1], got {color!r}.")
    return VisualRandomizationOptions(table_color_options=table_colors)


def sample_table_color(
    seed: int,
    episode_id: int,
    options: VisualRandomizationOptions,
) -> tuple[float, float, float]:
    rng = random.Random(seed + TABLE_COLOR_SEED_OFFSET + episode_id)
    return rng.choice(options.table_color_options)


def sample_pick_place(
    seed: int,
    episode_id: int,
    options: PickPlaceSamplingOptions,
) -> PickPlaceSample:
    rng = random.Random(seed + episode_id)

    object_xy_offset = _sample_reachable_xy_offset(
        rng,
        options.object_xy_range,
        options.object_origin_xy,
        options.workspace,
    )
    object_xy = tuple(
        origin + offset
        for origin, offset in zip(options.object_origin_xy, object_xy_offset)
    )
    for _ in range(options.workspace.max_sampling_attempts):
        place_xy_offset = _sample_reachable_xy_offset(
            rng,
            options.place_xy_range,
            options.place_origin_xy,
            options.workspace,
        )
        place_xy = tuple(
            origin + offset
            for origin, offset in zip(options.place_origin_xy, place_xy_offset)
        )
        if math.dist(object_xy, place_xy) >= options.minimum_object_place_distance_m:
            break
    else:
        raise RuntimeError(
            "Failed to sample object and receptacle offsets with the configured minimum separation."
        )
    light_intensity = rng.uniform(
        options.lighting.intensity_range[0],
        options.lighting.intensity_range[1],
    )
    light_color = options.lighting.color_options[
        rng.randrange(len(options.lighting.color_options))
    ]

    return PickPlaceSample(
        object_xy_offset=object_xy_offset,
        place_xy_offset=place_xy_offset,
        light_intensity=light_intensity,
        light_color=light_color,
        table_color=sample_table_color(seed, episode_id, options.visual),
    )


@dataclass(frozen=True, slots=True)
class ReachingSample:
    object_xy_offset: tuple[float, float]
    light_intensity: float
    light_color: tuple[float, float, float]


@dataclass(frozen=True, slots=True)
class ReachingSamplingOptions:
    object_xy_range: XYRange
    object_origin_xy: tuple[float, float]
    workspace: WorkspaceConstraint
    lighting: LightingOptions


def _sample_reachable_xy_offset(
    rng: random.Random,
    xy_range: XYRange,
    origin_xy: tuple[float, float],
    workspace: WorkspaceConstraint,
) -> tuple[float, float]:
    for _ in range(workspace.max_sampling_attempts):
        offset = (
            rng.uniform(xy_range.x[0], xy_range.x[1]),
            rng.uniform(xy_range.y[0], xy_range.y[1]),
        )
        position = tuple(origin + delta for origin, delta in zip(origin_xy, offset))
        if math.dist(position, workspace.robot_base_xy) <= workspace.max_distance_m:
            return offset
    raise RuntimeError("Failed to sample a target position inside the reachable workspace.")


def sample_reaching_offsets(
    seed: int,
    episode_id: int,
    options: ReachingSamplingOptions,
) -> ReachingSample:
    rng = random.Random(seed + episode_id)

    object_xy_offset = _sample_reachable_xy_offset(
        rng,
        options.object_xy_range,
        options.object_origin_xy,
        options.workspace,
    )
    light_intensity = rng.uniform(
        options.lighting.intensity_range[0], options.lighting.intensity_range[1]
    )
    light_color = options.lighting.color_options[
        rng.randrange(len(options.lighting.color_options))
    ]

    return ReachingSample(
        object_xy_offset=object_xy_offset,
        light_intensity=light_intensity,
        light_color=light_color,
    )
