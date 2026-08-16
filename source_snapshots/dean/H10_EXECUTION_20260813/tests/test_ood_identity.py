from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from risk_head_pipeline.ood_identity import (
    PINNED_OFFICIAL_FINGERPRINT,
    canonical_json_sha256,
    sha256_file,
    validate_locked_ood_identity,
)


WORKSPACE = Path(__file__).resolve().parents[1]
OFFICIAL = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/"
    "configs/benchmarks/reaching_train_ood150/full_ood.json"
)
ROUND0 = WORKSPACE / "manifests/seen_4000_master.json"


def prepared_identity(tmp_path: Path):
    official = json.loads(OFFICIAL.read_text())
    assert official["manifest_fingerprint_sha256"] == PINNED_OFFICIAL_FINGERPRINT
    locked = copy.deepcopy(official)
    locked["collection_config"] = "locked-test-config.yaml"
    locked["provenance"] = {
        **locked["provenance"],
        "official_manifest_path": str(OFFICIAL),
        "official_manifest_sha256": sha256_file(OFFICIAL),
        "official_manifest_fingerprint_sha256": PINNED_OFFICIAL_FINGERPRINT,
    }
    for item in locked["episodes"]:
        item["risk_split"] = "ood_smoke"
    locked.pop("manifest_fingerprint_sha256")
    locked["manifest_fingerprint_sha256"] = canonical_json_sha256(locked)
    locked_path = tmp_path / "locked.json"
    locked_path.write_text(json.dumps(locked))
    run = {
        "manifest_path": str(locked_path),
        "manifest_sha256": sha256_file(locked_path),
        "manifest_fingerprint_sha256": locked["manifest_fingerprint_sha256"],
    }
    summaries = [
        {
            "source_episode_id": item["scene"]["source_episode_id"],
            "source_benchmark_episode_id": item["benchmark_episode_id"],
            "scene_fingerprint_sha256": item["scene_fingerprint_sha256"],
        }
        for item in locked["episodes"]
    ]
    return run, locked_path, summaries


def test_locked_ood_exact_identity_and_round0_separation(tmp_path: Path) -> None:
    run, locked, summaries = prepared_identity(tmp_path)
    result = validate_locked_ood_identity(
        run_manifest=run,
        locked_manifest_path=locked,
        official_manifest_path=OFFICIAL,
        round0_manifest_path=ROUND0,
        collected_summaries=summaries,
    )
    assert result["exact_episode_membership"] is True
    assert result["collected_episode_count"] == 150
    assert result["round0_scene_overlap_count"] == 0


def test_locked_ood_rejects_substituted_collected_episode(tmp_path: Path) -> None:
    run, locked, summaries = prepared_identity(tmp_path)
    summaries[0] = {**summaries[0], "scene_fingerprint_sha256": "0" * 64}
    with pytest.raises(RuntimeError, match="collected OOD membership differs"):
        validate_locked_ood_identity(
            run_manifest=run,
            locked_manifest_path=locked,
            official_manifest_path=OFFICIAL,
            round0_manifest_path=ROUND0,
            collected_summaries=summaries,
        )


def test_locked_ood_rejects_round0_scene_overlap(tmp_path: Path) -> None:
    run, locked, summaries = prepared_identity(tmp_path)
    locked_payload = json.loads(locked.read_text())
    round0 = json.loads(ROUND0.read_text())
    round0["episodes"][0]["scene"] = copy.deepcopy(
        locked_payload["episodes"][0]["scene"]
    )
    round0["episodes"][0]["scene_fingerprint_sha256"] = locked_payload[
        "episodes"
    ][0]["scene_fingerprint_sha256"]
    round0.pop("manifest_fingerprint_sha256")
    round0["manifest_fingerprint_sha256"] = canonical_json_sha256(round0)
    overlapping = tmp_path / "round0-overlap.json"
    overlapping.write_text(json.dumps(round0))
    with pytest.raises(RuntimeError, match="overlaps H10 Round 0"):
        validate_locked_ood_identity(
            run_manifest=run,
            locked_manifest_path=locked,
            official_manifest_path=OFFICIAL,
            round0_manifest_path=overlapping,
            collected_summaries=summaries,
        )


def test_locked_ood_rejects_run_manifest_hash_mismatch(tmp_path: Path) -> None:
    run, locked, summaries = prepared_identity(tmp_path)
    run["manifest_sha256"] = "0" * 64
    with pytest.raises(RuntimeError, match="SHA-256 differs"):
        validate_locked_ood_identity(
            run_manifest=run,
            locked_manifest_path=locked,
            official_manifest_path=OFFICIAL,
            round0_manifest_path=ROUND0,
            collected_summaries=summaries,
        )
