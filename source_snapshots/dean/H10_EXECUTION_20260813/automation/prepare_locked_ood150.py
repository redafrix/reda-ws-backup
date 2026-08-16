#!/usr/bin/env python3
"""Prepare an immutable, explicitly test-only copy of the official OOD-150 manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
ISAAC_REPO = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab"
)
OFFICIAL_MANIFEST = (
    ISAAC_REPO / "configs/benchmarks/reaching_train_ood150/full_ood.json"
)
OFFICIAL_CONFIG = ISAAC_REPO / "configs/collect_reaching_pose_v1_train_ood150.yaml"
SOURCE_MANIFEST = Path(
    "/media/redafrix/My Passport/reaching_pose_v1_4400/train/manifest.json"
)
EVAL_CONFIG = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/"
    "generated_simvla_configs/eval_softplus_110k.yaml"
)
OUTPUT_DIR = WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728"
GENERATED = WORKSPACE / "automation/generated/locked_ood150"

sys.path.insert(0, str(ISAAC_REPO / "src"))
from franka_wrist_camera_scene.simvla.ood_benchmark import (  # noqa: E402
    canonical_json_sha256,
)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def write_once(path: Path, text: str) -> None:
    if path.exists():
        if path.read_text() != text:
            raise RuntimeError(f"refusing to overwrite immutable OOD evidence: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    payload = json.loads(OFFICIAL_MANIFEST.read_text())
    official_fingerprint = str(payload["manifest_fingerprint_sha256"])
    if official_fingerprint != "49ac35a2f77d2ca12ad2d9ca00a396c3f745d2c6bc179ee6d641638fad1cde4e":
        raise RuntimeError("official OOD-150 manifest identity changed")
    if len(payload["episodes"]) != 150 or int(payload["collection_index"]) != 1:
        raise RuntimeError("official locked benchmark is not full OOD-150")
    payload["collection_config"] = str(OFFICIAL_CONFIG)
    payload["provenance"] = {
        **payload["provenance"],
        "source_manifest": str(SOURCE_MANIFEST),
        "source_manifest_sha256": digest(SOURCE_MANIFEST),
        "official_manifest_path": str(OFFICIAL_MANIFEST),
        "official_manifest_sha256": digest(OFFICIAL_MANIFEST),
        "official_manifest_fingerprint_sha256": official_fingerprint,
        "scientific_role": "locked_final_ood150_test_only",
        "used_for_training": False,
        "used_for_normalization": False,
        "used_for_model_selection": False,
        "used_for_threshold_calibration": False,
    }
    for item in payload["episodes"]:
        item["risk_split"] = "ood_smoke"
    payload.pop("manifest_fingerprint_sha256", None)
    payload["manifest_fingerprint_sha256"] = canonical_json_sha256(payload)
    manifest_path = GENERATED / "manifest.json"
    write_once(manifest_path, json.dumps(payload, indent=2) + "\n")
    run_config = "\n".join(
        [
            f"collection_config: {OFFICIAL_CONFIG}",
            "collection_index: 1",
            "expected_split: ood",
            f"output_dir: {OUTPUT_DIR}",
            "num_envs: 1",
            "max_steps: 2400",
            "success_threshold_m: 0.02",
            "settle_time_s: 0.2",
            "record_cameras: true",
            "record_depth: false",
            "save_training_rgb_arrays: false",
            "save_rgb_videos: false",
            "camera_fps: 30",
            "state_record_fps: 30",
            "control_fps: 30",
            "use_fabric: true",
            "policy_sampling_seed: 20260728",
            "infrastructure_retry_count: 2",
            "",
            "simvla:",
            f"  eval_config: {EVAL_CONFIG}",
            "  stop_on_success: true",
            "",
        ]
    )
    config_path = GENERATED / "run_config.yaml"
    write_once(config_path, run_config)
    report = {
        "schema_version": "simvla_locked_ood150_preparation_v1",
        "official_manifest_path": str(OFFICIAL_MANIFEST),
        "official_manifest_sha256": digest(OFFICIAL_MANIFEST),
        "official_manifest_fingerprint_sha256": official_fingerprint,
        "test_only_manifest_path": str(manifest_path),
        "test_only_manifest_sha256": digest(manifest_path),
        "test_only_manifest_fingerprint_sha256": payload["manifest_fingerprint_sha256"],
        "run_config_path": str(config_path),
        "run_config_sha256": digest(config_path),
        "output_dir": str(OUTPUT_DIR),
        "episode_count": 150,
        "ood_used_for_training_or_calibration": False,
    }
    report_path = GENERATED / "preparation_report.json"
    write_once(report_path, json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
