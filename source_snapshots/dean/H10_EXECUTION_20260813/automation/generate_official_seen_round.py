#!/usr/bin/env python3
"""Generate a new deterministic broad round with the repository's official seen sampler."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
ISAAC_REPO = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab"
)
BASE_CONFIG = ISAAC_REPO / "configs/collect_reaching_pose_v1_4400.yaml"
SOURCE_MANIFEST = Path(
    "/media/redafrix/My Passport/reaching_pose_v1_4400/train/manifest.json"
)
EVAL_CONFIG = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/"
    "generated_simvla_configs/eval_softplus_110k.yaml"
)

sys.path.insert(0, str(ISAAC_REPO / "src"))

from franka_wrist_camera_scene.collection.configs import (  # noqa: E402
    collection_configs_from_config,
)
from franka_wrist_camera_scene.collection.reaching import (  # noqa: E402
    _build_asset_bank,
    _episode_asset_names,
    _make_episode_plan,
    _sample_scene_assets,
    validate_reaching_plan,
)
from franka_wrist_camera_scene.simvla.ood_benchmark import (  # noqa: E402
    build_manifest_payload,
    build_scene_payload,
    canonical_json_sha256,
    make_reaching_sampling_options,
)
from franka_wrist_camera_scene.utils.paths import load_yaml_config  # noqa: E402


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_atomic(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def collection_config_for_seed(path: Path, seed: int) -> None:
    text = BASE_CONFIG.read_text(encoding="utf-8")
    needle = "  seed: 123\n"
    if text.count(needle) != 1:
        raise RuntimeError("official config no longer has one anchored seed: 123")
    write_atomic(path, text.replace(needle, f"  seed: {seed}\n", 1))


def planned_scene(collection_cfg: dict[str, Any], source_id: int) -> dict[str, Any]:
    seed = int(collection_cfg["seed"])
    assets = _sample_scene_assets(collection_cfg, seed, source_id)
    bank = _build_asset_bank({source_id: assets})
    names = _episode_asset_names(bank, assets)
    base_spec, options = make_reaching_sampling_options(collection_cfg)
    plan = _make_episode_plan(
        collection_cfg, base_spec, assets, seed, source_id, options, names
    )
    validate_reaching_plan(collection_cfg, assets, plan)
    return build_scene_payload(source_id, assets, plan)


def prior_scene_fingerprints() -> set[str]:
    fingerprints: set[str] = set()
    paths = [WORKSPACE / "manifests/seen_4000_master.json"]
    paths.extend(sorted((WORKSPACE / "automation/generated").glob("round_*/manifest.json")))
    for path in paths:
        if not path.is_file():
            continue
        payload = json.loads(path.read_text())
        fingerprints.update(
            str(item["scene_fingerprint_sha256"]) for item in payload["episodes"]
        )
    return fingerprints


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round-id", type=int, required=True)
    parser.add_argument("--scene-seed", type=int, required=True)
    parser.add_argument("--policy-seed", type=int, required=True)
    parser.add_argument("--episodes", type=int, default=4000)
    parser.add_argument("--max-candidates", type=int, default=200000)
    args = parser.parse_args()
    if args.round_id <= 0 or args.round_id > 999:
        raise ValueError("generated round_id must be in [1, 999]")
    if args.episodes != 4000:
        raise ValueError("broad production rounds contain exactly 4000 scenes")

    generated = WORKSPACE / "automation/generated" / f"round_{args.round_id:03d}"
    manifest_path = generated / "manifest.json"
    collection_path = generated / "collection_config.yaml"
    run_config_path = generated / "run_config.yaml"
    report_path = generated / "generation_report.json"
    if any(path.exists() for path in (manifest_path, run_config_path, report_path)):
        existing = json.loads(report_path.read_text()) if report_path.exists() else None
        expected = {
            "round_id": args.round_id,
            "scene_seed": args.scene_seed,
            "policy_seed": args.policy_seed,
            "episode_count": args.episodes,
        }
        if existing and all(existing.get(key) == value for key, value in expected.items()):
            print(json.dumps(existing, indent=2, sort_keys=True))
            return 0
        raise RuntimeError(f"refusing to overwrite generated evidence: {generated}")

    collection_config_for_seed(collection_path, args.scene_seed)
    configs = collection_configs_from_config(load_yaml_config(str(collection_path)))
    collection_cfg = configs[0]
    if str(collection_cfg["suite"]["split"]) != "train":
        raise RuntimeError("official seen round must use the train suite")

    excluded = prior_scene_fingerprints()
    selected: list[dict[str, Any]] = []
    local_fingerprints: set[str] = set()
    invalid_candidates = 0
    duplicate_candidates = 0
    for source_id in range(args.max_candidates):
        try:
            scene = planned_scene(collection_cfg, source_id)
        except RuntimeError:
            invalid_candidates += 1
            continue
        fingerprint = canonical_json_sha256(scene)
        if fingerprint in excluded or fingerprint in local_fingerprints:
            duplicate_candidates += 1
            continue
        local_fingerprints.add(fingerprint)
        selected.append(
            {
                "benchmark_episode_id": len(selected),
                "risk_split": "unassigned",
                "scene": scene,
                "scene_fingerprint_sha256": fingerprint,
            }
        )
        if len(selected) == args.episodes:
            break
    if len(selected) != args.episodes:
        raise RuntimeError(
            f"generated only {len(selected)} unique valid scenes from "
            f"{args.max_candidates} candidates"
        )

    manifest = build_manifest_payload(
        benchmark_name=f"reaching_pose_v1_seen_risk_round_{args.round_id:03d}",
        collection_config=str(collection_path),
        collection_index=0,
        seed=args.scene_seed,
        episodes=selected,
        provenance={
            "source_manifest": str(SOURCE_MANIFEST),
            "source_manifest_sha256": sha256_file(SOURCE_MANIFEST),
            "source_suite": "reaching_pose_v1_train",
            "source_split": "train",
            "scene_derivation": (
                "official _sample_scene_assets + _make_episode_plan + "
                "validate_reaching_plan + build_scene_payload"
            ),
            "official_isaac_repo": str(ISAAC_REPO),
            "official_collection_config_base": str(BASE_CONFIG),
            "official_collection_config_base_sha256": sha256_file(BASE_CONFIG),
            "round_id": args.round_id,
            "scene_seed": args.scene_seed,
            "policy_seed": args.policy_seed,
            "prior_scene_fingerprints_excluded": len(excluded),
        },
    )
    write_atomic(manifest_path, json.dumps(manifest, indent=2) + "\n")

    output = WORKSPACE / "outputs" / (
        f"final_seen_h10_round_{args.round_id:03d}_seed{args.policy_seed}"
    )
    run_config = "\n".join(
        [
            f"collection_config: {collection_path}",
            "collection_index: 0",
            "expected_split: train",
            f"output_dir: {output}",
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
            f"policy_sampling_seed: {args.policy_seed}",
            "infrastructure_retry_count: 2",
            "",
            "simvla:",
            f"  eval_config: {EVAL_CONFIG}",
            "  stop_on_success: true",
            "",
        ]
    )
    write_atomic(run_config_path, run_config)
    report = {
        "schema_version": "simvla_official_seen_round_generation_v1",
        "round_id": args.round_id,
        "scene_seed": args.scene_seed,
        "policy_seed": args.policy_seed,
        "episode_count": len(selected),
        "invalid_candidate_count": invalid_candidates,
        "duplicate_candidate_count": duplicate_candidates,
        "manifest_path": str(manifest_path),
        "manifest_sha256": sha256_file(manifest_path),
        "manifest_fingerprint_sha256": manifest["manifest_fingerprint_sha256"],
        "collection_config_path": str(collection_path),
        "collection_config_sha256": sha256_file(collection_path),
        "run_config_path": str(run_config_path),
        "run_config_sha256": sha256_file(run_config_path),
        "output_dir": str(output),
        "source_fingerprint_overlap": 0,
        "official_seen_sampler": True,
    }
    write_atomic(report_path, json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
