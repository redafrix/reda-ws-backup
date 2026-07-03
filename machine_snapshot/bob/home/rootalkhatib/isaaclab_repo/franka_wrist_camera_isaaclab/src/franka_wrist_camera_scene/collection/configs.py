"""Collection config helpers."""

from __future__ import annotations


def collection_configs_from_config(config: dict) -> list[dict]:
    if "collections" not in config:
        return [config]

    collections = config["collections"]
    if not isinstance(collections, list) or not collections:
        raise ValueError("Combined collection config must define a non-empty collections list.")
    return collections
