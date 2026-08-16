#!/usr/bin/env python3
"""Exhaustively audit every authoritative row in a corrected collection."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

import numpy as np

WORKSPACE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKSPACE / "src"))

from risk_collection.constants import (  # noqa: E402
    TOPK8_INDICES,
    UNCERTAINTY_49D_KEYS,
)
from risk_collection.parity_audit import (  # noqa: E402
    EpisodeParityAuditor,
    ParityMetrics,
    merge_metrics,
)
from risk_collection.rounds import global_episode_id, scene_family_id  # noqa: E402
from risk_collection.storage import (  # noqa: E402
    authoritative_episode_dirs,
    verify_aggregate_indexes,
    write_json_atomic,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_manifest_hashes(run_manifest: dict[str, Any]) -> dict[str, str]:
    checks = {
        "selected_manifest": (
            run_manifest["manifest_path"],
            run_manifest["manifest_sha256"],
        ),
        "source_manifest": (
            run_manifest["source_manifest_path"],
            run_manifest["source_manifest_sha256"],
        ),
        "run_config": (
            run_manifest["run_config_path"],
            run_manifest["run_config_sha256"],
        ),
        "collection_config": (
            run_manifest["collection_config_path"],
            run_manifest["collection_config_sha256"],
        ),
        "evaluation_config": (
            run_manifest["evaluation_config_path"],
            run_manifest["evaluation_config_sha256"],
        ),
        "collector_source": (
            run_manifest["collector_source_path"],
            run_manifest["collector_source_sha256"],
        ),
        "checkpoint_model": (
            run_manifest["checkpoint"]["model_path"],
            run_manifest["checkpoint"]["model_sha256"],
        ),
        "checkpoint_config": (
            run_manifest["checkpoint"]["config_path"],
            run_manifest["checkpoint"]["config_sha256"],
        ),
        "normalization": (
            run_manifest["normalization"]["path"],
            run_manifest["normalization"]["sha256"],
        ),
    }
    actual: dict[str, str] = {}
    for name, (path_text, expected) in checks.items():
        path = Path(path_text)
        digest = sha256_file(path)
        actual[name] = digest
        if digest != expected:
            raise RuntimeError(
                f"{name} hash mismatch: actual={digest} expected={expected}"
            )
    return actual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--report-json", type=Path, required=True)
    parser.add_argument("--require-source-episode", type=int, action="append", default=[])
    parser.add_argument(
        "--expected-outcome",
        choices=("success", "synthetic_timeout", "production_round"),
        required=True,
    )
    args = parser.parse_args()

    root = args.output_dir.resolve()
    manifest = json.loads((root / "run_manifest.json").read_text())
    expect_synthetic = args.expected_outcome == "synthetic_timeout"
    expect_production = args.expected_outcome == "production_round"
    manifest_synthetic = bool(
        manifest.get("synthetic_smoke", {}).get("forced_timeout_enabled", False)
    )
    if manifest_synthetic != expect_synthetic:
        raise RuntimeError(
            "run manifest synthetic-smoke mode does not match expected outcome"
        )
    round_manifest = manifest.get("round", {})
    if expect_production:
        if not bool(round_manifest.get("enabled", False)):
            raise RuntimeError("production audit requires an enabled round manifest")
        expected_root = (
            WORKSPACE
            / "outputs"
            / (
                f"final_seen_h10_round_{int(round_manifest['round_id']):03d}_seed"
                f"{int(manifest['policy']['policy_sampling_seed'])}"
            )
        ).resolve()
        if root != expected_root:
            raise RuntimeError(
                f"production output path mismatch: {root} != {expected_root}"
            )
        live_status = json.loads((root / "live_status.json").read_text())
        if live_status.get("state") != "complete":
            raise RuntimeError(
                f"production round is not complete: {live_status.get('state')!r}"
            )
    elif bool(round_manifest.get("enabled", False)):
        raise RuntimeError("smoke audit must not target a production round")
    if expect_synthetic and not root.is_relative_to(
        (WORKSPACE / "smokes_timeout2400").resolve()
    ):
        raise RuntimeError("synthetic timeout output escaped smokes_timeout2400")
    timing = manifest["timing"]
    if (
        int(timing["max_sim_steps"]) != 2400
        or int(timing["max_control_ticks"]) != 600
        or int(timing["control_ticks_per_replan"]) != 10
        or int(timing["max_decision_rows"]) != 60
        or int(timing["physics_hz"]) != 120
        or int(timing["control_hz"]) != 30
        or int(timing["decimation"]) != 4
    ):
        raise RuntimeError("run manifest does not contain the H10 2400/600/60 timing")
    if manifest["execution_mode"] != "chunk_h10":
        raise RuntimeError("H10 production must use chunk_h10")
    if manifest["risk_features"]["feature_49d_key_order"] != list(
        UNCERTAINTY_49D_KEYS
    ):
        raise RuntimeError("run manifest 49D feature order mismatch")
    if manifest["risk_features"]["topk8_indices"] != list(TOPK8_INDICES):
        raise RuntimeError("run manifest TopK8 mismatch")

    norm = json.loads(Path(manifest["normalization"]["path"]).read_text())
    state_mean = np.asarray(norm["norm_stats"]["state"]["mean"], dtype=np.float32)
    state_std = np.asarray(norm["norm_stats"]["state"]["std"], dtype=np.float32)
    global_seed = int(manifest["policy"]["policy_sampling_seed"])

    episode_dirs = authoritative_episode_dirs(root)
    if not episode_dirs:
        raise RuntimeError("no committed episodes to audit")
    if expect_synthetic and len(episode_dirs) != 1:
        raise RuntimeError("synthetic timeout audit requires exactly one episode")

    seen_episode_ids: set[str] = set()
    seen_source_episode_ids: set[int] = set()
    seen_scene_family_ids: set[str] = set()
    seen_row_keys: set[tuple[str, int]] = set()
    collection_partitions: dict[str, str] = {}
    row_count = 0
    success_count = 0
    failure_count = 0
    parity_metrics = ParityMetrics()

    for episode_dir in episode_dirs:
        episode_id = episode_dir.name
        if episode_id in seen_episode_ids:
            raise RuntimeError(f"duplicate episode ID: {episode_id}")
        seen_episode_ids.add(episode_id)
        rows_payload = (episode_dir / "risk_rows.jsonl").read_bytes()
        summary = json.loads((episode_dir / "summary.json").read_text())
        source_episode_id = int(summary["source_episode_id"])
        if source_episode_id in seen_source_episode_ids:
            raise RuntimeError(f"duplicate source episode ID: {source_episode_id}")
        seen_source_episode_ids.add(source_episode_id)
        if expect_production:
            round_id = int(round_manifest["round_id"])
            expected_episode_id = global_episode_id(round_id, source_episode_id)
            if episode_id != expected_episode_id:
                raise RuntimeError(
                    f"global episode ID mismatch: {episode_id} != {expected_episode_id}"
                )
            fingerprint = str(summary["scene_fingerprint_sha256"])
            expected_family = scene_family_id(fingerprint)
            if summary.get("scene_family_id") != expected_family:
                raise RuntimeError(f"scene family mismatch: {episode_id}")
            seen_scene_family_ids.add(expected_family)
            if int(summary.get("round_id", -1)) != round_id:
                raise RuntimeError(f"round ID mismatch: {episode_id}")
            if summary.get("global_episode_id") != episode_id:
                raise RuntimeError(f"summary global ID mismatch: {episode_id}")
        elif episode_id != f"{source_episode_id:06d}":
            raise RuntimeError(f"smoke episode ID mismatch: {episode_id}")
        validation = json.loads((episode_dir / "validation.json").read_text())
        if hashlib.sha256(rows_payload).hexdigest() != validation["rows_sha256"]:
            raise RuntimeError(f"episode validation hash mismatch: {episode_id}")
        rows = [json.loads(line) for line in rows_payload.splitlines()]
        if len(rows) != int(summary["decision_rows"]):
            raise RuntimeError(f"summary row count mismatch: {episode_id}")
        if len(rows) != int(validation["decision_rows"]):
            raise RuntimeError(f"validation row count mismatch: {episode_id}")
        expected_split = "synthetic_smoke" if expect_synthetic else "unassigned_seen"
        if summary["risk_split"] != expected_split:
            raise RuntimeError(
                f"unexpected scientific split in {episode_id}: "
                f"{summary['risk_split']!r} != {expected_split!r}"
            )
        if bool(summary.get("synthetic_smoke", False)) != expect_synthetic:
            raise RuntimeError(f"summary synthetic marker mismatch: {episode_id}")
        if bool(summary.get("training_eligible", False)) != expect_production:
            raise RuntimeError(f"training eligibility mismatch: {episode_id}")
        if expect_synthetic and not bool(
            summary.get("success_termination_suppressed", False)
        ):
            raise RuntimeError(
                f"synthetic timeout did not record suppressed termination: {episode_id}"
            )
        partition = str(summary["collection_manifest_partition"])
        if partition == "ood_smoke":
            raise RuntimeError(f"OOD episode found in seen collection: {episode_id}")
        collection_partitions[episode_id] = partition
        if summary["outcome"] == "failure_or_timeout":
            failure_count += 1
            if int(summary["simulation_steps"]) != 2400 or len(rows) != 60:
                raise RuntimeError(
                    f"failure does not end at 2400 steps/600 controls/60 replans: {episode_id}"
                )
        elif summary["outcome"] == "success":
            success_count += 1
            if int(summary["simulation_steps"]) >= 2400 or len(rows) > 60:
                raise RuntimeError(
                    f"success is not below the 2400-step/60-replan bound: {episode_id}"
                )
        else:
            raise RuntimeError(f"invalid finalized outcome: {episode_id}")
        if expect_synthetic and summary["outcome"] != "failure_or_timeout":
            raise RuntimeError(f"synthetic timeout outcome mismatch: {episode_id}")
        if args.expected_outcome == "success" and summary["outcome"] != "success":
            raise RuntimeError(f"success smoke outcome mismatch: {episode_id}")
        expected_label = 0 if summary["outcome"] == "success" else 1
        if int(summary["risk_label"]) != expected_label:
            raise RuntimeError(f"summary label mismatch: {episode_id}")

        parity = EpisodeParityAuditor(
            global_seed=global_seed,
            source_episode_id=source_episode_id,
            state_mean=state_mean,
            state_std=state_std,
        )
        for decision_index, row in enumerate(rows):
            key = (str(row["episode_id"]), int(row["decision_index"]))
            if key in seen_row_keys:
                raise RuntimeError(f"duplicate row key: {key}")
            seen_row_keys.add(key)
            if key != (episode_id, decision_index):
                raise RuntimeError(f"noncontiguous row key: {key}")
            if row["execution_mode"] != "chunk_h10":
                raise RuntimeError(f"wrong execution mode: {key}")
            sequence = np.asarray(row["executed_action_sequence"], dtype=np.float32)
            is_terminal_row = decision_index == len(rows) - 1
            expected_sequence_length = (
                int(summary["control_ticks"]) - 10 * (len(rows) - 1)
                if is_terminal_row and summary["outcome"] == "success"
                else 10
            )
            if sequence.shape != (expected_sequence_length, 7):
                raise RuntimeError(
                    f"H10 execution length mismatch at {key}: "
                    f"{sequence.shape} != ({expected_sequence_length}, 7)"
                )
            if row["parent_episode_outcome"] != summary["outcome"]:
                raise RuntimeError(f"row outcome mismatch: {key}")
            if int(row["parent_episode_risk_label"]) != expected_label:
                raise RuntimeError(f"row label mismatch: {key}")
            metadata = row["metadata"]
            if metadata["risk_split"] != expected_split:
                raise RuntimeError(f"row scientific split mismatch: {key}")
            if bool(metadata.get("synthetic_smoke", False)) != expect_synthetic:
                raise RuntimeError(f"row synthetic marker mismatch: {key}")
            if bool(metadata.get("training_eligible", False)) != expect_production:
                raise RuntimeError(f"row training eligibility mismatch: {key}")
            if metadata["collection_manifest_partition"] != partition:
                raise RuntimeError(f"collection partition mismatch: {key}")
            if metadata["ood_excluded_from_training"]:
                raise RuntimeError(f"seen row incorrectly marked OOD: {key}")
            if expect_production:
                if metadata.get("global_episode_id") != episode_id:
                    raise RuntimeError(f"row global ID mismatch: {key}")
                if int(metadata.get("source_episode_id", -1)) != source_episode_id:
                    raise RuntimeError(f"row source ID mismatch: {key}")
                if int(metadata.get("round_id", -1)) != int(
                    round_manifest["round_id"]
                ):
                    raise RuntimeError(f"row round ID mismatch: {key}")
                if metadata.get("scene_family_id") != summary["scene_family_id"]:
                    raise RuntimeError(f"row scene family mismatch: {key}")

            parity.audit(row, decision_index)
            row_count += 1
        expected_decision_rows = (int(summary["control_ticks"]) + 9) // 10
        if len(rows) != expected_decision_rows:
            raise RuntimeError(
                f"H10 replan count mismatch for {episode_id}: "
                f"{len(rows)} != ceil({summary['control_ticks']}/10)"
            )
        merge_metrics(parity_metrics, parity.metrics)

    aggregate_identity = verify_aggregate_indexes(root, episode_dirs)

    required = set(args.require_source_episode)
    missing = required - seen_source_episode_ids
    if missing:
        raise RuntimeError(f"required source episodes missing: {sorted(missing)}")

    infrastructure_error_attempts = 0
    infrastructure_error_source_ids: set[int] = set()
    errors_path = root / "episode_errors.jsonl"
    if errors_path.exists():
        for line in errors_path.read_bytes().splitlines():
            error = json.loads(line)
            infrastructure_error_attempts += 1
            infrastructure_error_source_ids.add(int(error["source_episode_id"]))
            if bool(error.get("training_rows_written", True)):
                raise RuntimeError("infrastructure error wrote training rows")
            if bool(error.get("risk_label_written", True)):
                raise RuntimeError("infrastructure error wrote a risk label")

    permanently_excluded_source_ids = sorted(
        infrastructure_error_source_ids - seen_source_episode_ids
    )
    if expect_production:
        selected_manifest = json.loads(Path(manifest["manifest_path"]).read_text())
        expected_source_ids = {
            int(item["scene"]["source_episode_id"])
            for item in selected_manifest["episodes"]
        }
        if seen_source_episode_ids | set(permanently_excluded_source_ids) != expected_source_ids:
            missing_sources = expected_source_ids - seen_source_episode_ids - set(
                permanently_excluded_source_ids
            )
            unexpected_sources = (
                seen_source_episode_ids | set(permanently_excluded_source_ids)
            ) - expected_source_ids
            raise RuntimeError(
                "production source membership mismatch: "
                f"missing={sorted(missing_sources)} unexpected={sorted(unexpected_sources)}"
            )

    hashes = verify_manifest_hashes(manifest)
    result = {
        "schema_version": "simvla_isaac_risk_exhaustive_audit_v1",
        "output_dir": str(root),
        "committed_episodes": len(episode_dirs),
        "decision_rows": row_count,
        "success_episodes": success_count,
        "failure_episodes": failure_count,
        "expected_outcome": args.expected_outcome,
        "synthetic_smoke": expect_synthetic,
        "training_eligible": expect_production,
        "production_round": expect_production,
        "round_id": round_manifest.get("round_id") if expect_production else None,
        "unique_scene_families": len(seen_scene_family_ids),
        "infrastructure_error_attempts": infrastructure_error_attempts,
        "infrastructure_excluded_episodes": len(permanently_excluded_source_ids),
        "infrastructure_excluded_source_ids": permanently_excluded_source_ids,
        "infrastructure_errors_excluded_from_labels": True,
        "episode_ids": sorted(seen_episode_ids),
        "collection_partitions": collection_partitions,
        "max_ace_abs_difference": parity_metrics.max_ace_abs_difference,
        "max_feature49_abs_difference": parity_metrics.max_feature49_abs_difference,
        "max_feature_delta_abs_difference": parity_metrics.max_feature_delta_abs_difference,
        "max_history_abs_difference": parity_metrics.max_history_abs_difference,
        "max_executed_action_abs_difference": parity_metrics.max_executed_action_abs_difference,
        "max_candidate0_trace_abs_difference": parity_metrics.max_candidate0_trace_abs_difference,
        "max_candidate_seed_integer_difference": parity_metrics.max_candidate_seed_difference,
        **aggregate_identity,
        "verified_provenance_hashes": hashes,
        "all_jsonl_parsed": True,
        "all_values_finite": True,
        "all_shapes_valid": True,
        "canonical_numeric_dtype": "float32",
        "episode_and_row_ids_unique": True,
        "candidate_seeds_deterministic_and_distinct": True,
        "candidate_zero_trace_parity": True,
        "ace_new_training_parity": True,
        "feature49_parity": True,
        "history_16x21_parity": True,
        "executed_h10_parity": True,
        "episode_reset_history_zero_padded": True,
        "outcome_summary_parity": True,
        "no_ood150": True,
        "scientific_split_expected": True,
        "aggregate_exact_authoritative_concatenation": True,
        "stored_hashes_match": True,
        "pass": True,
    }
    write_json_atomic(args.report_json, result)
    print(json.dumps(result, indent=2, sort_keys=True))
    print("EXHAUSTIVE_RAW_DATA_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
