"""Pure Python layout geometry helpers for object footprints and overlap checks."""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True, slots=True)
class FootprintCircle:
    name: str
    xy: tuple[float, float]
    radius_m: float


def planar_footprint_radius_from_bbox(
    bbox_min: tuple[float, float, float],
    bbox_max: tuple[float, float, float],
    margin_m: float,
) -> float:
    if margin_m < 0.0:
        raise ValueError(f"Footprint margin must be non-negative, got {margin_m}")

    min_x, min_y = float(bbox_min[0]), float(bbox_min[1])
    max_x, max_y = float(bbox_max[0]), float(bbox_max[1])

    if max_x <= min_x or max_y <= min_y:
        raise ValueError(f"Invalid planar bbox size: bbox_min={bbox_min}, bbox_max={bbox_max}")

    root_radius = max(
        math.hypot(min_x, min_y),
        math.hypot(min_x, max_y),
        math.hypot(max_x, min_y),
        math.hypot(max_x, max_y),
    )
    return root_radius + margin_m


def footprints_overlap_xy(
    a: FootprintCircle,
    b: FootprintCircle,
) -> bool:
    dist = math.hypot(a.xy[0] - b.xy[0], a.xy[1] - b.xy[1])
    return dist < (a.radius_m + b.radius_m)


def require_non_overlapping_footprints(
    a: FootprintCircle,
    b: FootprintCircle,
) -> None:
    dist = math.hypot(a.xy[0] - b.xy[0], a.xy[1] - b.xy[1])
    sum_radii = a.radius_m + b.radius_m
    if dist < sum_radii:
        overlap = sum_radii - dist
        raise ValueError(
            f"Footprint overlap detected: '{a.name}' (xy={a.xy}, radius={a.radius_m}m) and "
            f"'{b.name}' (xy={b.xy}, radius={b.radius_m}m) overlap by {overlap:.4f}m (distance={dist:.4f}m)."
        )


def validate_non_overlapping_layout(
    footprints: tuple[FootprintCircle, ...],
) -> None:
    for i in range(len(footprints)):
        for j in range(i + 1, len(footprints)):
            require_non_overlapping_footprints(footprints[i], footprints[j])


def _is_inside_range(f: FootprintCircle, min_x: float, max_x: float, min_y: float, max_y: float) -> bool:
    return (
        f.xy[0] - f.radius_m >= min_x
        and f.xy[0] + f.radius_m <= max_x
        and f.xy[1] - f.radius_m >= min_y
        and f.xy[1] + f.radius_m <= max_y
    )


def validate_pick_place_initial_layout(
    target_object: FootprintCircle,
    placement_receptacle: FootprintCircle,
    clutter: tuple[FootprintCircle, ...],
    xy_range: tuple[float, float, float, float] | None = None,
    target_xy_range: tuple[float, float, float, float] | None = None,
    receptacle_xy_range: tuple[float, float, float, float] | None = None,
) -> None:
    # 1. target object footprint does not overlap placement receptacle footprint
    require_non_overlapping_footprints(target_object, placement_receptacle)

    # 2. target object footprint does not overlap any clutter footprint
    for c in clutter:
        require_non_overlapping_footprints(target_object, c)

    # 3. placement receptacle footprint does not overlap any clutter footprint
    for c in clutter:
        require_non_overlapping_footprints(placement_receptacle, c)

    # 4. clutter footprints do not overlap each other
    validate_non_overlapping_layout(clutter)

    # 5. footprints are inside their configured XY ranges
    if target_xy_range is not None:
        min_x, max_x, min_y, max_y = target_xy_range
        # Check center position for randomization range
        if not (min_x <= target_object.xy[0] <= max_x and min_y <= target_object.xy[1] <= max_y):
            raise ValueError(
                f"Target object center '{target_object.name}' (xy={target_object.xy}) is not within "
                f"the configured object_xy_range boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )

    if receptacle_xy_range is not None:
        min_x, max_x, min_y, max_y = receptacle_xy_range
        # Check center position for randomization range
        if not (min_x <= placement_receptacle.xy[0] <= max_x and min_y <= placement_receptacle.xy[1] <= max_y):
            raise ValueError(
                f"Placement receptacle center '{placement_receptacle.name}' (xy={placement_receptacle.xy}) is not within "
                f"the configured place_xy_range boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )

    if xy_range is not None:
        min_x, max_x, min_y, max_y = xy_range
        if not _is_inside_range(target_object, min_x, max_x, min_y, max_y):
            raise ValueError(
                f"Target object footprint '{target_object.name}' (xy={target_object.xy}, radius={target_object.radius_m}m) is not within "
                f"the configured layout boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )
        if not _is_inside_range(placement_receptacle, min_x, max_x, min_y, max_y):
            raise ValueError(
                f"Placement receptacle footprint '{placement_receptacle.name}' (xy={placement_receptacle.xy}, radius={placement_receptacle.radius_m}m) is not within "
                f"the configured layout boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )
        for f in clutter:
            if not _is_inside_range(f, min_x, max_x, min_y, max_y):
                raise ValueError(
                    f"Clutter footprint '{f.name}' (xy={f.xy}, radius={f.radius_m}m) is not within "
                    f"the configured layout boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
                )


def validate_reaching_initial_layout(
    target_object: FootprintCircle,
    clutter: tuple[FootprintCircle, ...],
    xy_range: tuple[float, float, float, float] | None = None,
    target_xy_range: tuple[float, float, float, float] | None = None,
) -> None:
    # 1. target object footprint does not overlap any clutter footprint
    for c in clutter:
        require_non_overlapping_footprints(target_object, c)

    # 2. clutter footprints do not overlap each other
    validate_non_overlapping_layout(clutter)

    # 3. footprints are inside their configured XY ranges
    if target_xy_range is not None:
        min_x, max_x, min_y, max_y = target_xy_range
        if not (min_x <= target_object.xy[0] <= max_x and min_y <= target_object.xy[1] <= max_y):
            raise ValueError(
                f"Target object center '{target_object.name}' (xy={target_object.xy}) is not within "
                f"the configured object_xy_range boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )

    if xy_range is not None:
        min_x, max_x, min_y, max_y = xy_range
        if not _is_inside_range(target_object, min_x, max_x, min_y, max_y):
            raise ValueError(
                f"Target object footprint '{target_object.name}' (xy={target_object.xy}, radius={target_object.radius_m}m) is not within "
                f"the configured layout boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
            )
        for f in clutter:
            if not _is_inside_range(f, min_x, max_x, min_y, max_y):
                raise ValueError(
                    f"Clutter footprint '{f.name}' (xy={f.xy}, radius={f.radius_m}m) is not within "
                    f"the configured layout boundary x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]."
                )
