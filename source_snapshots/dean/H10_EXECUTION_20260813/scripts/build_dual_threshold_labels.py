#!/usr/bin/env python3
"""Build explicit strict-2cm and operational-4cm episode labels.

The authoritative collection rows remain unchanged. A strict success implies an
operational success because both metrics use the same target, displacement gate,
and dwell duration. Strict failures require exact saved-action replay evidence;
minimum distance alone is not enough to prove the 4 cm dwell condition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "simvla_isaac_dual_threshold_labels_v1"
STRICT_THRESHOLD_M = 0.02
OPERATIONAL_THRESHOLD_M = 0.04
SETTLE_TIME_S = 0.2
REQUIRED_PHYSICS_FRAMES = 24


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def load_replay_evidence(path: Path) -> dict[int, dict[str, Any]]:
    payload = json.loads(path.read_text())
    evidence: dict[int, dict[str, Any]] = {}
    for item in payload["episodes"]:
        source_id = int(item["source_episode_id"])
        if source_id in evidence:
            raise RuntimeError(f"duplicate replay evidence for source episode {source_id}")
        if not item.get("exact_saved_executed_actions_used"):
            raise RuntimeError(f"replay {source_id} did not use exact saved actions")
        if item.get("policy_resampled"):
            raise RuntimeError(f"replay {source_id} resampled policy actions")
        if int(item["required_consecutive_physics_frames"]) != REQUIRED_PHYSICS_FRAMES:
            raise RuntimeError(f"replay {source_id} has the wrong dwell frame count")
        evidence[source_id] = item
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("round_root", type=Path)
    parser.add_argument("--failure-replay-report", type=Path, required=True)
    parser.add_argument("--output-jsonl", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path, required=True)
    args = parser.parse_args()

    round_root = args.round_root.resolve()
    replay_report = args.failure_replay_report.resolve()
    replay_by_source = load_replay_evidence(replay_report)
    records: list[dict[str, Any]] = []
    strict_failure_ids: set[int] = set()

    for summary_path in sorted((round_root / "episodes").glob("*/summary.json")):
        summary = json.loads(summary_path.read_text())
        if summary.get("synthetic_smoke") or not summary.get("training_eligible"):
            raise RuntimeError(f"ineligible episode in production round: {summary_path}")
        source_id = int(summary["source_episode_id"])
        strict_success = summary["outcome"] == "success"
        expected_strict_label = 0 if strict_success else 1
        if int(summary["risk_label"]) != expected_strict_label:
            raise RuntimeError(f"strict label mismatch: {summary_path}")
        if float(summary["strict_success_threshold_m"]) != STRICT_THRESHOLD_M:
            raise RuntimeError(f"strict threshold mismatch: {summary_path}")
        if float(summary["settle_time_s"]) != SETTLE_TIME_S:
            raise RuntimeError(f"settle time mismatch: {summary_path}")

        if strict_success:
            operational_success = True
            operational_frames = None
            evidence_kind = "strict_success_monotonic_threshold_implication"
            replay_sha256 = None
        else:
            strict_failure_ids.add(source_id)
            replay = replay_by_source.get(source_id)
            if replay is None:
                raise RuntimeError(
                    f"strict failure {source_id} lacks exact 4 cm replay evidence"
                )
            if replay["original_outcome"] != "failure_or_timeout":
                raise RuntimeError(f"replay {source_id} is not evidence for a strict failure")
            if replay["scene_fingerprint_sha256"] != summary["scene_fingerprint_sha256"]:
                raise RuntimeError(f"scene fingerprint mismatch for replay {source_id}")
            if int(replay["simulation_steps"]) != int(summary["simulation_steps"]):
                raise RuntimeError(f"simulation-step mismatch for replay {source_id}")
            operational_success = bool(replay["counterfactual_4cm_dwell_success"])
            operational_frames = int(
                replay["maximum_consecutive_counterfactual_4cm_frames"]
            )
            if operational_success != (operational_frames >= REQUIRED_PHYSICS_FRAMES):
                raise RuntimeError(f"4 cm dwell evidence is inconsistent for {source_id}")
            evidence_kind = "exact_saved_action_physics_replay"
            replay_sha256 = sha256_file(replay_report)

        classification = (
            "success_both_thresholds"
            if strict_success
            else (
                "precision_near_miss_strict2cm_fail_operational4cm_success"
                if operational_success
                else "failure_both_thresholds"
            )
        )
        records.append(
            {
                "schema_version": SCHEMA_VERSION,
                "episode_id": str(summary["episode_id"]),
                "source_episode_id": source_id,
                "instruction": str(summary["instruction"]),
                "scene_fingerprint_sha256": str(summary["scene_fingerprint_sha256"]),
                "minimum_tcp_distance_m": float(summary["minimum_tcp_distance_m"]),
                "strict_2cm_success": strict_success,
                "strict_2cm_risk_label": expected_strict_label,
                "operational_4cm_success": operational_success,
                "operational_4cm_risk_label": 0 if operational_success else 1,
                "classification": classification,
                "settle_time_s": SETTLE_TIME_S,
                "required_consecutive_physics_frames": REQUIRED_PHYSICS_FRAMES,
                "maximum_consecutive_operational_4cm_frames": operational_frames,
                "operational_label_evidence": evidence_kind,
                "source_summary_path": str(summary_path.resolve()),
                "source_summary_sha256": sha256_file(summary_path),
                "failure_replay_report_sha256": replay_sha256,
            }
        )

    unused_replays = set(replay_by_source) - strict_failure_ids
    missing_replays = strict_failure_ids - set(replay_by_source)
    if unused_replays or missing_replays:
        raise RuntimeError(
            f"replay coverage mismatch: unused={sorted(unused_replays)} "
            f"missing={sorted(missing_replays)}"
        )
    if not records:
        raise RuntimeError(f"no committed episode summaries found under {round_root}")

    jsonl = "".join(json.dumps(item, sort_keys=True) + "\n" for item in records)
    atomic_text(args.output_jsonl.resolve(), jsonl)
    counts: dict[str, int] = {}
    for item in records:
        key = str(item["classification"])
        counts[key] = counts.get(key, 0) + 1
    summary_payload = {
        "schema_version": SCHEMA_VERSION,
        "round_root": str(round_root),
        "episodes": len(records),
        "strict_2cm_successes": sum(item["strict_2cm_success"] for item in records),
        "strict_2cm_failures": sum(not item["strict_2cm_success"] for item in records),
        "operational_4cm_successes": sum(
            item["operational_4cm_success"] for item in records
        ),
        "operational_4cm_failures": sum(
            not item["operational_4cm_success"] for item in records
        ),
        "classifications": counts,
        "label_contracts": {
            "paper_strict_2cm": "strict_2cm_risk_label",
            "operational_visual_4cm": "operational_4cm_risk_label",
        },
        "failure_replay_report": str(replay_report),
        "failure_replay_report_sha256": sha256_file(replay_report),
        "labels_jsonl": str(args.output_jsonl.resolve()),
        "labels_jsonl_sha256": sha256_file(args.output_jsonl.resolve()),
        "pass": True,
    }
    atomic_text(
        args.summary_json.resolve(),
        json.dumps(summary_payload, indent=2, sort_keys=True) + "\n",
    )
    print(json.dumps(summary_payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
