"""Typed collection-suite metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class SuiteMetadata:
    name: str | None = None
    split: str | None = None
    difficulty: str | None = None
    tags: list[str] | None = None
    description: str | None = None


EMPTY_SUITE_METADATA = SuiteMetadata()


def suite_metadata_from_config(collection_cfg: dict[str, Any]) -> SuiteMetadata:
    suite_cfg = collection_cfg.get("suite")
    if suite_cfg is None:
        return EMPTY_SUITE_METADATA

    return SuiteMetadata(
        name=str(suite_cfg["name"]),
        split=str(suite_cfg["split"]),
        difficulty=str(suite_cfg["difficulty"]),
        tags=[str(tag) for tag in suite_cfg["tags"]],
        description=str(suite_cfg["description"]),
    )
