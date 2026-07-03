"""Catalog candidate queries used by collection preflight."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from franka_wrist_camera_scene.objects.catalog import ObjectCategory, ObjectVariant, load_object_catalog
from franka_wrist_camera_scene.objects.geometry_registry import (
    ObjectPlanarGeometry,
    get_object_geometry,
    load_object_geometry_registry,
)
from franka_wrist_camera_scene.objects.selection import matching_variants, variant_visual_label
from franka_wrist_camera_scene.tasks.layout_geometry import planar_footprint_radius_from_bbox


@dataclass(frozen=True, slots=True)
class CatalogCandidate:
    category: ObjectCategory
    variant: ObjectVariant
    geometry: ObjectPlanarGeometry

    @property
    def key(self) -> tuple[str, str]:
        return (self.category.id, self.variant.id)

    @property
    def label(self) -> str:
        return variant_visual_label(self.category, self.variant)


@dataclass(frozen=True, slots=True)
class CandidatePool:
    name: str
    candidates: tuple[CatalogCandidate, ...]

    @property
    def category_ids(self) -> tuple[str, ...]:
        return tuple(sorted({candidate.category.id for candidate in self.candidates}))


@dataclass(frozen=True, slots=True)
class CatalogQuery:
    catalog_name: str
    geometry_name: str
    category_id: str
    variant_id: str
    split: str
    role: str
    affordances: tuple[str, ...]
    grasp_strategy: str


def target_query(config: dict[str, Any]) -> CatalogQuery:
    return CatalogQuery(
        catalog_name=str(config["catalog_config"]),
        geometry_name=str(config["geometry_config"]),
        category_id=str(config["category_id"]),
        variant_id=str(config["variant_id"]),
        split=str(config["split"]),
        role=str(config["role"]),
        affordances=tuple(str(value) for value in config["required_affordances"]),
        grasp_strategy=str(config["required_grasp_strategy"]),
    )


def clutter_query(config: dict[str, Any]) -> CatalogQuery:
    return CatalogQuery(
        catalog_name=str(config["catalog_config"]),
        geometry_name=str(config["geometry_config"]),
        category_id="sample",
        variant_id="sample",
        split=str(config["split"]),
        role=str(config["role"]),
        affordances=tuple(str(value) for value in config["required_affordances"]),
        grasp_strategy=str(config["required_grasp_strategy"]),
    )


def load_candidate_pool(name: str, query: CatalogQuery) -> CandidatePool:
    catalog_name = query.catalog_name
    geometry_name = query.geometry_name
    catalog = load_object_catalog(catalog_name)
    geometry = load_object_geometry_registry(geometry_name)
    if geometry.catalog_config != catalog_name:
        raise ValueError(
            f"Geometry config {geometry_name} belongs to {geometry.catalog_config}, "
            f"not {catalog_name}."
        )

    candidates: list[CatalogCandidate] = []

    for category in catalog.categories:
        if category.split != query.split:
            continue
        if query.role != "any" and category.role != query.role:
            continue
        if query.category_id != "sample" and category.id != query.category_id:
            continue
        for variant in matching_variants(category, query.affordances, query.grasp_strategy):
            if query.variant_id != "sample" and variant.id != query.variant_id:
                continue
            candidates.append(
                CatalogCandidate(
                    category=category,
                    variant=variant,
                    geometry=get_object_geometry(geometry, category.id, variant.id),
                )
            )

    if not candidates:
        raise ValueError(f"Candidate pool {name!r} is empty.")
    return CandidatePool(name=name, candidates=tuple(candidates))


def limit_target_width(pool: CandidatePool, max_width_m: float) -> CandidatePool:
    candidates = tuple(
        candidate
        for candidate in pool.candidates
        if candidate.geometry.planar_extent_minor <= max_width_m
    )
    if not candidates:
        raise ValueError(f"Candidate pool {pool.name!r} is empty after width filtering.")
    return CandidatePool(pool.name, candidates)


def limit_clutter_footprint(
    pool: CandidatePool,
    max_radius_m: float,
    margin_m: float,
) -> CandidatePool:
    def footprint_radius(candidate: CatalogCandidate) -> float:
        return planar_footprint_radius_from_bbox(
            candidate.geometry.local_bbox_min,
            candidate.geometry.local_bbox_max,
            margin_m,
        )

    candidates = tuple(
        candidate for candidate in pool.candidates if footprint_radius(candidate) <= max_radius_m
    )
    if not candidates:
        raise ValueError(f"Candidate pool {pool.name!r} is empty after footprint filtering.")
    return CandidatePool(pool.name, candidates)
