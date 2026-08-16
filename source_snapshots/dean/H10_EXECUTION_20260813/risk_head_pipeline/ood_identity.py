"""Pure identity checks for the immutable locked OOD-150 benchmark."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


PINNED_OFFICIAL_FINGERPRINT = (
    "49ac35a2f77d2ca12ad2d9ca00a396c3f745d2c6bc179ee6d641638fad1cde4e"
)


def canonical_json_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validated_episode_identity(
    payload: dict[str, Any], *, expected_count: int
) -> dict[int, tuple[int, str]]:
    expected_fingerprint = str(payload.get("manifest_fingerprint_sha256", ""))
    fingerprint_payload = dict(payload)
    fingerprint_payload.pop("manifest_fingerprint_sha256", None)
    actual_fingerprint = canonical_json_sha256(fingerprint_payload)
    if actual_fingerprint != expected_fingerprint:
        raise RuntimeError(
            "manifest fingerprint mismatch: "
            f"recorded={expected_fingerprint} actual={actual_fingerprint}"
        )
    episodes = payload.get("episodes")
    if not isinstance(episodes, list) or len(episodes) != expected_count:
        raise RuntimeError(
            f"manifest episode count mismatch: {len(episodes or [])} != {expected_count}"
        )
    identities: dict[int, tuple[int, str]] = {}
    fingerprints: set[str] = set()
    for expected_benchmark_id, item in enumerate(episodes):
        benchmark_id = int(item["benchmark_episode_id"])
        if benchmark_id != expected_benchmark_id:
            raise RuntimeError(
                f"noncontiguous benchmark ID: {benchmark_id} != {expected_benchmark_id}"
            )
        scene = item["scene"]
        source_id = int(scene["source_episode_id"])
        fingerprint = str(item["scene_fingerprint_sha256"])
        if canonical_json_sha256(scene) != fingerprint:
            raise RuntimeError(f"scene fingerprint mismatch for source {source_id}")
        if source_id in identities:
            raise RuntimeError(f"duplicate source episode ID: {source_id}")
        if fingerprint in fingerprints:
            raise RuntimeError(f"duplicate scene fingerprint: {fingerprint}")
        identities[source_id] = (benchmark_id, fingerprint)
        fingerprints.add(fingerprint)
    return identities


def validate_locked_ood_identity(
    *,
    run_manifest: dict[str, Any],
    locked_manifest_path: Path,
    official_manifest_path: Path,
    round0_manifest_path: Path,
    collected_summaries: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    locked_manifest_path = locked_manifest_path.resolve()
    official_manifest_path = official_manifest_path.resolve()
    round0_manifest_path = round0_manifest_path.resolve()
    if Path(str(run_manifest["manifest_path"])).resolve() != locked_manifest_path:
        raise RuntimeError("run manifest does not reference the locked OOD manifest")
    if sha256_file(locked_manifest_path) != str(run_manifest["manifest_sha256"]):
        raise RuntimeError("locked OOD manifest SHA-256 differs from run provenance")

    locked = json.loads(locked_manifest_path.read_text())
    official = json.loads(official_manifest_path.read_text())
    round0 = json.loads(round0_manifest_path.read_text())
    locked_identity = validated_episode_identity(locked, expected_count=150)
    official_identity = validated_episode_identity(official, expected_count=150)
    if str(official["manifest_fingerprint_sha256"]) != PINNED_OFFICIAL_FINGERPRINT:
        raise RuntimeError("official OOD-150 fingerprint is not the pinned identity")
    provenance = locked.get("provenance", {})
    if str(provenance.get("official_manifest_fingerprint_sha256")) != PINNED_OFFICIAL_FINGERPRINT:
        raise RuntimeError("locked manifest lost the pinned official fingerprint")
    if Path(str(provenance.get("official_manifest_path", ""))).resolve() != official_manifest_path:
        raise RuntimeError("locked manifest official path mismatch")
    if str(provenance.get("official_manifest_sha256")) != sha256_file(
        official_manifest_path
    ):
        raise RuntimeError("official OOD manifest SHA-256 mismatch")
    if locked_identity != official_identity:
        raise RuntimeError("locked manifest episode identity differs from official OOD-150")
    if str(run_manifest["manifest_fingerprint_sha256"]) != str(
        locked["manifest_fingerprint_sha256"]
    ):
        raise RuntimeError("run manifest recorded the wrong locked fingerprint")

    round0_identity = validated_episode_identity(round0, expected_count=4000)
    ood_fingerprints = {value[1] for value in locked_identity.values()}
    round0_fingerprints = {value[1] for value in round0_identity.values()}
    overlap = sorted(ood_fingerprints & round0_fingerprints)
    if overlap:
        raise RuntimeError(f"OOD-150 overlaps H10 Round 0: {overlap[:10]}")

    collected: dict[int, tuple[int, str]] = {}
    for summary in collected_summaries:
        source_id = int(summary["source_episode_id"])
        identity = (
            int(summary["source_benchmark_episode_id"]),
            str(summary["scene_fingerprint_sha256"]),
        )
        if source_id in collected:
            raise RuntimeError(f"duplicate collected OOD source ID: {source_id}")
        collected[source_id] = identity
    if collected != locked_identity:
        missing = sorted(set(locked_identity) - set(collected))
        unexpected = sorted(set(collected) - set(locked_identity))
        mismatched = sorted(
            source_id
            for source_id in set(locked_identity) & set(collected)
            if locked_identity[source_id] != collected[source_id]
        )
        raise RuntimeError(
            "collected OOD membership differs from locked manifest: "
            f"missing={missing} unexpected={unexpected} mismatched={mismatched}"
        )
    return {
        "official_manifest_fingerprint_sha256": PINNED_OFFICIAL_FINGERPRINT,
        "official_manifest_sha256": sha256_file(official_manifest_path),
        "locked_manifest_fingerprint_sha256": str(
            locked["manifest_fingerprint_sha256"]
        ),
        "locked_manifest_sha256": sha256_file(locked_manifest_path),
        "exact_episode_membership": True,
        "collected_episode_count": len(collected),
        "round0_scene_overlap_count": 0,
        "official_identity_match": True,
    }
