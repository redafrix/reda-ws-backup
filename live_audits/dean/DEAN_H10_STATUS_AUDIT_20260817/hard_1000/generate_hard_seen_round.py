#!/usr/bin/env python3
"""Select a new official seen-only hard-scene round without using OOD outcomes."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import shutil
from typing import Any

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict


WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
ROUND0 = WORKSPACE / "outputs/final_seen_h10_round_000_seed20260730"
ROUND0_MANIFEST = WORKSPACE / "manifests/seen_4000_master.json"
CANDIDATE_MANIFEST = WORKSPACE / "automation/generated/round_001/manifest.json"
OOD_MANIFEST = WORKSPACE / "automation/generated/locked_ood150/manifest.json"
EVAL_CONFIG = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/"
    "generated_simvla_configs/eval_softplus_110k.yaml"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_once(path: Path, text: str) -> None:
    if path.exists():
        if path.read_text() != text:
            raise RuntimeError(f"refusing to overwrite immutable evidence: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def scene_assets(scene: dict[str, Any]) -> set[tuple[str, str]]:
    target = scene["target"]
    values = {(str(target["category_id"]), str(target["variant_id"]))}
    values.update(
        (str(item["category_id"]), str(item["variant_id"]))
        for item in scene.get("clutter", [])
    )
    return values


def scene_features(scene: dict[str, Any]) -> dict[str, float]:
    target = scene["target"]
    offset = np.asarray(scene["object_xy_offset"], dtype=np.float64)
    target_xy = np.asarray([0.58 + offset[0], -0.16 + offset[1]])
    clutter = scene.get("clutter", [])
    distances = []
    features: dict[str, float] = {
        f"target_category={target['category_id']}": 1.0,
        f"target_variant={target['category_id']}:{target['variant_id']}": 1.0,
        f"target_source={target['source_name']}": 1.0,
        "target_x": float(target_xy[0]),
        "target_y": float(target_xy[1]),
        "target_radius": float(np.linalg.norm(target_xy - np.asarray([0.58, -0.16]))),
        "target_position_index": float(scene["target_position_index"]),
        "clutter_count": float(len(clutter)),
        "lighting_intensity": float(scene.get("lighting", {}).get("intensity", 0.0)) / 1000.0,
    }
    for item in clutter:
        category = str(item["category_id"])
        source = str(item["source_name"])
        features[f"clutter_category={category}"] = (
            features.get(f"clutter_category={category}", 0.0) + 1.0
        )
        features[f"clutter_source={source}"] = (
            features.get(f"clutter_source={source}", 0.0) + 1.0
        )
        position = np.asarray(item["pos_local"][:2], dtype=np.float64)
        distances.append(float(np.linalg.norm(position - target_xy)))
    if distances:
        features["minimum_target_clutter_xy"] = min(distances)
        features["mean_target_clutter_xy"] = float(np.mean(distances))
        features["clutter_within_15cm"] = float(sum(value <= 0.15 for value in distances))
        features["clutter_within_25cm"] = float(sum(value <= 0.25 for value in distances))
    else:
        features["minimum_target_clutter_xy"] = 2.0
        features["mean_target_clutter_xy"] = 2.0
        features["clutter_within_15cm"] = 0.0
        features["clutter_within_25cm"] = 0.0
    return features


def committed_fingerprints() -> set[str]:
    values: set[str] = set()
    for summary in (WORKSPACE / "outputs").glob("final_seen_h10_round_*_seed*/episodes/*/summary.json"):
        values.add(str(json.loads(summary.read_text())["scene_fingerprint_sha256"]))
    return values


def select_diverse_hard(
    candidates: list[tuple[float, dict[str, Any]]],
    count: int,
    minimum_per_category: int,
    maximum_per_category: int,
) -> list[tuple[float, dict[str, Any]]]:
    by_category: dict[str, list[tuple[float, dict[str, Any]]]] = defaultdict(list)
    for item in candidates:
        category = str(item[1]["scene"]["target"]["category_id"])
        by_category[category].append(item)
    for values in by_category.values():
        values.sort(key=lambda item: (-item[0], item[1]["scene_fingerprint_sha256"]))

    selected: list[tuple[float, dict[str, Any]]] = []
    selected_fingerprints: set[str] = set()
    category_counts: Counter[str] = Counter()
    for category in sorted(by_category):
        for item in by_category[category][:minimum_per_category]:
            selected.append(item)
            selected_fingerprints.add(str(item[1]["scene_fingerprint_sha256"]))
            category_counts[category] += 1

    for item in sorted(candidates, key=lambda value: (-value[0], value[1]["scene_fingerprint_sha256"])):
        if len(selected) == count:
            break
        fingerprint = str(item[1]["scene_fingerprint_sha256"])
        category = str(item[1]["scene"]["target"]["category_id"])
        if fingerprint in selected_fingerprints or category_counts[category] >= maximum_per_category:
            continue
        selected.append(item)
        selected_fingerprints.add(fingerprint)
        category_counts[category] += 1
    if len(selected) != count:
        raise RuntimeError(
            f"hard-scene diversity constraints selected {len(selected)} of {count}"
        )
    return sorted(selected, key=lambda item: (-item[0], item[1]["scene_fingerprint_sha256"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round-id", type=int, default=2)
    parser.add_argument("--policy-seed", type=int, default=20260804)
    parser.add_argument("--episodes", type=int, default=1000)
    parser.add_argument("--candidate-manifest", type=Path, default=CANDIDATE_MANIFEST)
    parser.add_argument("--minimum-per-category", type=int, default=30)
    parser.add_argument("--maximum-per-category", type=int, default=100)
    args = parser.parse_args()
    if args.episodes != 1000:
        raise ValueError("the hard enrichment round must contain exactly 1000 scenes")

    generated = WORKSPACE / "automation/generated" / f"hard_round_{args.round_id:03d}"
    manifest_path = generated / "manifest.json"
    collection_path = generated / "collection_config.yaml"
    run_config_path = generated / "run_config.yaml"
    report_path = generated / "generation_report.json"
    if report_path.is_file():
        print(report_path.read_text())
        return 0
    if generated.exists() and any(generated.iterdir()):
        raise RuntimeError(f"refusing to overwrite partial hard-round evidence: {generated}")

    round0_manifest = json.loads(ROUND0_MANIFEST.read_text())
    round0_entries = {
        int(item["scene"]["source_episode_id"]): item
        for item in round0_manifest["episodes"]
    }
    summaries = []
    for path in sorted((ROUND0 / "episodes").glob("*/summary.json")):
        item = json.loads(path.read_text())
        if not item.get("training_eligible") or item.get("synthetic_smoke"):
            continue
        summaries.append(item)
    if len(summaries) != 4000:
        raise RuntimeError(f"expected 4000 audited Round 0 summaries, got {len(summaries)}")
    training_scenes = [round0_entries[int(item["source_episode_id"])]["scene"] for item in summaries]
    labels = np.asarray(
        [item["outcome"] == "failure_or_timeout" for item in summaries], dtype=np.int64
    )

    vectorizer = DictVectorizer(sparse=True)
    training_matrix = vectorizer.fit_transform([scene_features(scene) for scene in training_scenes])
    classifier = LogisticRegression(
        C=0.5,
        class_weight="balanced",
        max_iter=2000,
        random_state=20260810,
        solver="liblinear",
    )
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=20260810)
    cross_validated = cross_val_predict(
        classifier, training_matrix, labels, cv=folds, method="predict_proba"
    )[:, 1]
    classifier.fit(training_matrix, labels)

    candidate_payload = json.loads(args.candidate_manifest.read_text())
    candidate_provenance = candidate_payload.get("provenance", {})
    source_manifest = Path(str(candidate_provenance["source_manifest"])).resolve()
    source_manifest_sha256 = sha256_file(source_manifest)
    recorded_source_sha256 = str(candidate_provenance["source_manifest_sha256"])
    if source_manifest_sha256 != recorded_source_sha256:
        raise RuntimeError(
            "candidate manifest source hash no longer matches the immutable source "
            f"manifest: actual={source_manifest_sha256} "
            f"recorded={recorded_source_sha256}"
        )
    ood_payload = json.loads(OOD_MANIFEST.read_text())
    seen_assets = set().union(*(scene_assets(item["scene"]) for item in round0_manifest["episodes"]))
    ood_assets = set().union(*(scene_assets(item["scene"]) for item in ood_payload["episodes"]))
    if seen_assets & ood_assets:
        raise RuntimeError("seen and OOD asset-variant sets unexpectedly overlap")
    ood_fingerprints = {
        str(item["scene_fingerprint_sha256"]) for item in ood_payload["episodes"]
    }
    prior_fingerprints = committed_fingerprints() | {
        str(item["scene_fingerprint_sha256"]) for item in round0_manifest["episodes"]
    }

    eligible = []
    rejected = Counter()
    for item in candidate_payload["episodes"]:
        fingerprint = str(item["scene_fingerprint_sha256"])
        assets = scene_assets(item["scene"])
        if fingerprint in ood_fingerprints:
            rejected["ood_fingerprint"] += 1
            continue
        if fingerprint in prior_fingerprints:
            rejected["previously_committed_or_round0_fingerprint"] += 1
            continue
        if assets & ood_assets:
            rejected["ood_asset_variant"] += 1
            continue
        if not assets <= seen_assets:
            rejected["not_in_seen_asset_allowlist"] += 1
            continue
        eligible.append(item)
    if len(eligible) < args.episodes:
        raise RuntimeError(f"only {len(eligible)} OOD-safe unique candidates remain")

    candidate_matrix = vectorizer.transform([scene_features(item["scene"]) for item in eligible])
    scores = classifier.predict_proba(candidate_matrix)[:, 1]
    selected = select_diverse_hard(
        list(zip(scores.tolist(), eligible, strict=True)),
        args.episodes,
        args.minimum_per_category,
        args.maximum_per_category,
    )
    records = []
    for benchmark_id, (score, item) in enumerate(selected):
        records.append(
            {
                "benchmark_episode_id": benchmark_id,
                "risk_split": "unassigned",
                "scene": item["scene"],
                "scene_fingerprint_sha256": item["scene_fingerprint_sha256"],
                "hard_selection": {
                    "rank": benchmark_id,
                    "predicted_failure_score": score,
                    "uses_ood_outcomes": False,
                },
            }
        )

    source_collection = Path(candidate_payload["collection_config"])
    generated.mkdir(parents=True)
    shutil.copy2(source_collection, collection_path)
    manifest = {
        "schema_version": "simvla_reaching_ood_benchmark_v1",
        "benchmark_name": f"reaching_pose_v1_seen_hard_enrichment_{args.round_id:03d}",
        "collection_config": str(collection_path),
        "collection_index": int(candidate_payload.get("collection_index", 0)),
        "seed": int(candidate_payload["seed"]),
        "provenance": {
            "source_suite": "reaching_pose_v1_train",
            "source_split": str(candidate_provenance.get("source_split", "train")),
            "source_manifest": str(source_manifest),
            "source_manifest_sha256": source_manifest_sha256,
            "candidate_manifest": str(args.candidate_manifest.resolve()),
            "candidate_manifest_sha256": sha256_file(args.candidate_manifest),
            "round0_manifest": str(ROUND0_MANIFEST),
            "round0_manifest_sha256": sha256_file(ROUND0_MANIFEST),
            "round0_audit": str(ROUND0 / "reports/exhaustive_audit.json"),
            "round0_audit_sha256": sha256_file(ROUND0 / "reports/exhaustive_audit.json"),
            "selection": "Round0-only metadata logistic difficulty model plus category diversity quotas",
            "ood_manifest": str(OOD_MANIFEST),
            "ood_manifest_sha256": sha256_file(OOD_MANIFEST),
            "ood_outcomes_used": False,
            "ood_asset_variants_excluded": True,
            "ood_scene_fingerprints_excluded": True,
            "scene_family_replays_grouped_at_split": True,
            "scientific_split_pending": True,
        },
        "episodes": records,
    }
    manifest["manifest_fingerprint_sha256"] = canonical_hash(manifest)
    write_once(manifest_path, json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    output = WORKSPACE / "outputs" / f"final_seen_h10_round_{args.round_id:03d}_seed{args.policy_seed}"
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
    write_once(run_config_path, run_config)

    selected_scores = np.asarray([item[0] for item in selected])
    report = {
        "schema_version": "simvla_seen_hard_case_enrichment_v2",
        "round_id": args.round_id,
        "round_kind": "enrichment",
        "enrichment_strategy": "hard_scene_metadata_selection",
        "policy_seed": args.policy_seed,
        "episode_count": len(records),
        "output_dir": str(output),
        "manifest_path": str(manifest_path),
        "manifest_sha256": sha256_file(manifest_path),
        "run_config_path": str(run_config_path),
        "run_config_sha256": sha256_file(run_config_path),
        "round0_failure_rate": float(labels.mean()),
        "selection_model": {
            "type": "balanced logistic regression",
            "features": sorted(vectorizer.feature_names_),
            "cross_validated_auprc": float(average_precision_score(labels, cross_validated)),
            "cross_validated_auroc": float(roc_auc_score(labels, cross_validated)),
            "uses_round0_seen_outcomes_only": True,
            "uses_ood_outcomes": False,
        },
        "candidate_count": len(candidate_payload["episodes"]),
        "eligible_candidate_count": len(eligible),
        "candidate_rejections": dict(rejected),
        "selected_score": {
            "minimum": float(selected_scores.min()),
            "mean": float(selected_scores.mean()),
            "maximum": float(selected_scores.max()),
        },
        "target_category_counts": dict(
            sorted(Counter(item[1]["scene"]["target"]["category_id"] for item in selected).items())
        ),
        "selected_scene_fingerprint_overlap_with_ood150": 0,
        "selected_asset_variant_overlap_with_ood150": 0,
        "selected_scene_fingerprint_overlap_with_committed_data": 0,
        "ood150_remains_test_only": True,
    }
    write_once(report_path, json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
