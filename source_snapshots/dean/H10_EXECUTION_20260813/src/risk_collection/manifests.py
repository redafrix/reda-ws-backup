"""Deterministic seen-distribution manifests derived from the immutable source manifest."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import json
from pathlib import Path
from typing import Any

from .storage import canonical_sha256

MANIFEST_SCHEMA_VERSION = "simvla_reaching_ood_benchmark_v1"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_episode_to_scene(source: dict[str, Any]) -> dict[str, Any]:
    source_id = int(source["episode_id"])
    target_label = str(source["object_label"])
    scene = {
        "source_episode_id": source_id,
        "instruction": f"reach the {target_label}",
        "target": {
            "category_id": str(source["object_category_id"]),
            "variant_id": str(source["object_variant_id"]),
            "label": target_label,
            "source_name": str(source["target_source_name"]),
        },
        "target_position_index": source_id % 64,
        "object_xy_offset": [float(value) for value in source["object_xy_offset"]],
        "clutter_position_index": source_id % 64,
        "clutter": [
            {
                "slot_index": slot,
                "category_id": str(item["category_id"]),
                "variant_id": str(item["variant_id"]),
                "label": str(item["label"]),
                "source_name": str(item["source_name"]),
                "pos_local": [float(value) for value in item["pos_local"]],
            }
            for slot, item in enumerate(source["clutter_objects"])
        ],
        "lighting": {
            "intensity": float(source["light_intensity"]),
            "color": [float(value) for value in source["light_color"]],
        },
    }
    target_category = scene["target"]["category_id"]
    for item in scene["clutter"]:
        if item["category_id"] == target_category or item["label"] == target_label:
            raise ValueError(
                f"source episode {source_id} has ambiguous target in clutter"
            )
    return scene


def assign_risk_splits(episodes: list[dict[str, Any]]) -> dict[int, str]:
    """Deterministic category-stratified 80/10/10 assignment."""
    by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for episode in episodes:
        by_label[episode["scene"]["target"]["label"]].append(episode)
    assignments: dict[int, str] = {}
    for label, group in sorted(by_label.items()):
        ranked = sorted(
            group,
            key=lambda item: hashlib.sha256(
                (
                    f"simvla-risk-split-v1|{label}|"
                    f"{item['scene_fingerprint_sha256']}"
                ).encode("ascii")
            ).hexdigest(),
        )
        for index, episode in enumerate(ranked):
            bucket = index % 10
            split = "calibration" if bucket == 0 else "test" if bucket == 1 else "train"
            assignments[int(episode["scene"]["source_episode_id"])] = split
    return assignments


def build_seen_manifest(
    source_manifest_path: Path,
    collection_config_path: Path,
) -> tuple[dict[str, Any], dict[int, str]]:
    source_payload = json.loads(source_manifest_path.read_text())
    source_episodes = sorted(
        source_payload["episodes"], key=lambda item: int(item["episode_id"])
    )
    if int(source_payload["num_episodes"]) != 4000 or len(source_episodes) != 4000:
        raise ValueError("expected exactly 4,000 accepted seen source episodes")
    source_ids = [int(item["episode_id"]) for item in source_episodes]
    if len(set(source_ids)) != 4000:
        raise ValueError("source manifest episode IDs must be unique")

    episodes: list[dict[str, Any]] = []
    for benchmark_id, source in enumerate(source_episodes):
        if not bool(source["success"]):
            raise ValueError(
                f"source episode {source['episode_id']} is not successful"
            )
        scene = source_episode_to_scene(source)
        episodes.append(
            {
                "benchmark_episode_id": benchmark_id,
                "scene": scene,
                "scene_fingerprint_sha256": canonical_sha256(scene),
            }
        )

    split_assignments = assign_risk_splits(episodes)
    for episode in episodes:
        source_id = int(episode["scene"]["source_episode_id"])
        episode["risk_split"] = split_assignments[source_id]

    payload: dict[str, Any] = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "benchmark_name": "reaching_pose_v1_seen_risk_4000",
        "collection_config": str(collection_config_path.resolve()),
        "collection_index": 0,
        "seed": 123,
        "provenance": {
            "source_manifest": str(source_manifest_path.resolve()),
            "source_manifest_sha256": sha256_file(source_manifest_path),
            "source_episode_count": 4000,
            "source_suite": source_payload["suite_name"],
            "source_split": source_payload["suite_split"],
            "scene_derivation": (
                "scene fields from immutable train manifest; "
                "target_position_index=clutter_position_index=source_episode_id%64"
            ),
        },
        "episodes": episodes,
    }
    payload["manifest_fingerprint_sha256"] = canonical_sha256(payload)
    return payload, split_assignments


def subset_manifest(master: dict[str, Any], split: str) -> dict[str, Any]:
    selected = [
        episode for episode in master["episodes"] if episode["risk_split"] == split
    ]
    episodes = []
    for output_id, source in enumerate(selected):
        item = dict(source)
        item["benchmark_episode_id"] = output_id
        episodes.append(item)
    payload = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "benchmark_name": f"reaching_pose_v1_seen_risk_{split}",
        "collection_config": master["collection_config"],
        "collection_index": master["collection_index"],
        "seed": master["seed"],
        "provenance": {
            "master_manifest_fingerprint_sha256": master[
                "manifest_fingerprint_sha256"
            ],
            "risk_split": split,
            "episode_count": len(episodes),
        },
        "episodes": episodes,
    }
    payload["manifest_fingerprint_sha256"] = canonical_sha256(payload)
    return payload
