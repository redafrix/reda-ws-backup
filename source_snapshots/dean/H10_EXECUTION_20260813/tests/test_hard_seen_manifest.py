import json
from pathlib import Path

import pytest


WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
HARD = WORKSPACE / "automation/generated/hard_round_002"
OOD = WORKSPACE / "automation/generated/locked_ood150/manifest.json"
ROUND0 = WORKSPACE / "manifests/seen_4000_master.json"


def assets(payload):
    values = set()
    for item in payload["episodes"]:
        scene = item["scene"]
        target = scene["target"]
        values.add((target["category_id"], target["variant_id"]))
        values.update(
            (entry["category_id"], entry["variant_id"])
            for entry in scene.get("clutter", [])
        )
    return values


def fingerprints(payload):
    return {item["scene_fingerprint_sha256"] for item in payload["episodes"]}


def test_hard1000_manifest_preserves_locked_ood_separation():
    if not (HARD / "manifest.json").is_file():
        pytest.skip("H10 hard enrichment is generated only after audited H10 Round 0")
    hard = json.loads((HARD / "manifest.json").read_text())
    ood = json.loads(OOD.read_text())
    round0 = json.loads(ROUND0.read_text())
    report = json.loads((HARD / "generation_report.json").read_text())

    assert len(hard["episodes"]) == 1000
    assert len(fingerprints(hard)) == 1000
    assert not (fingerprints(hard) & fingerprints(ood))
    assert not (fingerprints(hard) & fingerprints(round0))
    assert not (assets(hard) & assets(ood))
    assert assets(hard) <= assets(round0)
    assert report["selected_asset_variant_overlap_with_ood150"] == 0
    assert report["selected_scene_fingerprint_overlap_with_ood150"] == 0
    assert report["selection_model"]["uses_ood_outcomes"] is False


def test_hard1000_run_config_keeps_production_semantics():
    if not (HARD / "run_config.yaml").is_file():
        pytest.skip("H10 hard enrichment is generated only after audited H10 Round 0")
    config = (HARD / "run_config.yaml").read_text()
    for value in (
        "max_steps: 2400",
        "success_threshold_m: 0.02",
        "settle_time_s: 0.2",
        "control_fps: 30",
        "save_training_rgb_arrays: false",
        "save_rgb_videos: false",
    ):
        assert value in config
