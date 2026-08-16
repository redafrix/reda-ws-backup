"""Deterministic identity and scheduling helpers for production rounds."""

from __future__ import annotations

from collections import defaultdict, deque
import hashlib
import json
import math
from typing import Any, Iterable


ROUND_SCHEDULE_VERSION = "seen_balanced_round_robin_v2"


def global_episode_id(round_id: int, source_episode_id: int) -> str:
    if round_id < 0 or round_id > 999:
        raise ValueError("round_id must be between 0 and 999")
    if source_episode_id < 0 or source_episode_id > 999_999:
        raise ValueError("source_episode_id must be between 0 and 999999")
    return f"r{round_id:03d}_s{source_episode_id:06d}"


def scene_family_id(scene_fingerprint_sha256: str) -> str:
    fingerprint = str(scene_fingerprint_sha256).lower()
    if len(fingerprint) != 64 or any(char not in "0123456789abcdef" for char in fingerprint):
        raise ValueError("scene fingerprint must be a lowercase SHA-256 digest")
    return f"scene_sha256:{fingerprint}"


def _distance_bin(scene: dict[str, Any]) -> int:
    x, y = (float(value) for value in scene["object_xy_offset"])
    # This is used only for execution ordering, never for inclusion or labels.
    return min(7, int(math.hypot(x, y) / 0.05))


def _bucket_key(entry: dict[str, Any]) -> tuple[Any, ...]:
    scene = entry["scene"]
    target = scene["target"]
    clutter = scene["clutter"]
    clutter_source_types = tuple(
        sorted(str(item["source_name"]) for item in clutter)
    )
    return (
        str(target["source_name"]),
        str(target["category_id"]),
        len(clutter),
        _distance_bin(scene),
        clutter_source_types,
    )


def _within_bucket_key(entry: dict[str, Any]) -> tuple[Any, ...]:
    scene = entry["scene"]
    clutter_signature = tuple(
        sorted(
            (str(item["source_name"]), str(item["category_id"]))
            for item in scene["clutter"]
        )
    )
    return (
        clutter_signature,
        int(scene["target_position_index"]),
        int(scene["clutter_position_index"]),
        str(entry["scene_fingerprint_sha256"]),
    )


def balanced_round_robin_order(entries: Iterable[dict[str, Any]]) -> list[int]:
    """Interleave target/category/clutter buckets without changing membership."""
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    materialized = list(entries)
    for entry in materialized:
        groups[_bucket_key(entry)].append(entry)
    queues = {
        key: deque(sorted(group, key=_within_bucket_key))
        for key, group in groups.items()
    }
    keys = sorted(
        queues,
        key=lambda key: hashlib.sha256(
            (ROUND_SCHEDULE_VERSION + "|" + json.dumps(key)).encode("utf-8")
        ).hexdigest(),
    )
    ordered: list[int] = []
    while queues:
        for key in list(keys):
            queue = queues.get(key)
            if queue is None:
                continue
            ordered.append(int(queue.popleft()["benchmark_episode_id"]))
            if not queue:
                queues.pop(key)
                keys.remove(key)
    if len(ordered) != len(materialized) or len(set(ordered)) != len(ordered):
        raise RuntimeError("balanced schedule did not preserve unique episode membership")
    return ordered


def schedule_sha256(
    benchmark_episode_ids: Iterable[int],
    *,
    version: str = ROUND_SCHEDULE_VERSION,
) -> str:
    payload = {
        "version": version,
        "benchmark_episode_ids": [int(value) for value in benchmark_episode_ids],
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()
