#!/usr/bin/env python3
"""Summarize a completed, exhaustively audited production round."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time
from typing import Any


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_bytes(root: Path) -> int:
    return sum(path.stat().st_size for path in root.rglob("*") if path.is_file())


def load_summaries(root: Path) -> list[dict[str, Any]]:
    summaries = []
    for episode_dir in sorted((root / "episodes").iterdir()):
        if not episode_dir.is_dir() or not (episode_dir / "COMMITTED").is_file():
            continue
        summaries.append(json.loads((episode_dir / "summary.json").read_text()))
    return summaries


def completion_span_seconds(root: Path) -> float:
    committed = [
        path.stat().st_mtime
        for path in (root / "episodes").glob("*/COMMITTED")
        if path.is_file()
    ]
    return max(committed) - min(committed) if len(committed) > 1 else 0.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--audit-json", type=Path, required=True)
    parser.add_argument("--report-json", type=Path, required=True)
    args = parser.parse_args()

    root = args.output_dir.resolve()
    audit = json.loads(args.audit_json.read_text())
    if not bool(audit.get("pass", False)):
        raise RuntimeError("refusing to summarize a round that failed exhaustive audit")
    manifest = json.loads((root / "run_manifest.json").read_text())
    selected_manifest = json.loads(Path(manifest["manifest_path"]).read_text())
    target_source_by_source_id = {
        int(item["scene"]["source_episode_id"]): str(
            item["scene"]["target"]["source_name"]
        )
        for item in selected_manifest["episodes"]
    }
    status = json.loads((root / "live_status.json").read_text())
    if status.get("state") != "complete":
        raise RuntimeError("round is not complete")

    summaries = load_summaries(root)
    successes = [item for item in summaries if item["outcome"] == "success"]
    failures = [item for item in summaries if item["outcome"] == "failure_or_timeout"]
    if len(successes) + len(failures) != len(summaries):
        raise RuntimeError("unknown finalized outcome in production round")
    if any(item.get("synthetic_smoke") for item in summaries):
        raise RuntimeError("synthetic smoke entered production round")
    if any(not item.get("training_eligible") for item in summaries):
        raise RuntimeError("production round contains an ineligible finalized episode")
    if any(item.get("risk_split") != "unassigned_seen" for item in summaries):
        raise RuntimeError("production scientific split was assigned before freezing")

    fingerprints = [str(item["scene_fingerprint_sha256"]) for item in summaries]
    fingerprint_counts = Counter(fingerprints)
    elapsed = completion_span_seconds(root)
    rows = sum(int(item["decision_rows"]) for item in summaries)
    size_bytes = tree_bytes(root)
    statvfs = os.statvfs(root)
    free_bytes = statvfs.f_bavail * statvfs.f_frsize
    if free_bytes < 100 * 1024**3:
        raise RuntimeError("free SSD space fell below the 100 GiB safety floor")

    error_attempts = int(audit.get("infrastructure_error_attempts", 0))
    infra_excluded = int(audit.get("infrastructure_excluded_episodes", 0))
    report = {
        "schema_version": "simvla_isaac_risk_round_summary_v1",
        "generated_at_unix_s": time.time(),
        "output_dir": str(root),
        "round": manifest["round"],
        "audit_path": str(args.audit_json.resolve()),
        "audit_sha256": sha256_file(args.audit_json),
        "run_manifest_sha256": sha256_file(root / "run_manifest.json"),
        "aggregate_rows_sha256": sha256_file(root / "risk_receding_samples.jsonl"),
        "aggregate_summaries_sha256": sha256_file(root / "episode_summaries.jsonl"),
        "valid_episodes": len(summaries),
        "successes": len(successes),
        "genuine_failures": len(failures),
        "infrastructure_error_attempts": error_attempts,
        "infrastructure_excluded_episodes": infra_excluded,
        "decision_rows": rows,
        "target_source_coverage": dict(
            sorted(
                Counter(
                    target_source_by_source_id[int(item["source_episode_id"])]
                    for item in summaries
                ).items()
            )
        ),
        "target_category_coverage": dict(
            sorted(Counter(str(item["target_category_id"]) for item in summaries).items())
        ),
        "clutter_cardinality_coverage": dict(
            sorted(Counter(str(item["clutter_cardinality"]) for item in summaries).items())
        ),
        "unique_scene_fingerprints": len(fingerprint_counts),
        "duplicate_scene_fingerprint_groups": sum(
            count > 1 for count in fingerprint_counts.values()
        ),
        "maximum_scene_fingerprint_multiplicity": max(
            fingerprint_counts.values(), default=0
        ),
        "output_bytes": size_bytes,
        "ssd_free_bytes": free_bytes,
        "completion_span_seconds": elapsed,
        "episodes_per_hour": (
            (len(summaries) - 1) * 3600.0 / elapsed if elapsed > 0 else None
        ),
        "rows_per_second": rows / elapsed if elapsed > 0 else None,
        "no_ood150": True,
        "no_synthetic_rows": True,
        "exhaustive_audit_pass": True,
    }

    round_summaries = [report]
    outputs_root = root.parent
    for path in sorted(outputs_root.glob("final_seen_h10_round_*_seed*/reports/round_audit_summary.json")):
        if path.resolve() == args.report_json.resolve():
            continue
        prior = json.loads(path.read_text())
        if prior.get("exhaustive_audit_pass"):
            round_summaries.append(prior)
    total_episodes = sum(int(item["valid_episodes"]) for item in round_summaries)
    total_successes = sum(int(item["successes"]) for item in round_summaries)
    total_failures = sum(int(item["genuine_failures"]) for item in round_summaries)
    target_met = total_successes >= 3000 and total_failures >= 300
    report["adaptive_collection"] = {
        "audited_round_count": len(round_summaries),
        "total_valid_episodes": total_episodes,
        "total_successes": total_successes,
        "total_genuine_failures": total_failures,
        "minimum_complete_broad_round_met": True,
        "minimum_300_failures_met": total_failures >= 300,
        "minimum_3000_successes_met": total_successes >= 3000,
        "minimum_40_failures_per_15pct_split_feasible": total_failures >= 267,
        "preferred_500_failures_met": total_failures >= 500,
        "target_met": target_met,
        "hard_cap_episodes": 16000,
        "next_action": (
            "freeze_scientific_dataset"
            if target_met
            else "prepare_second_official_seen_broad_round"
            if total_episodes < 8000
            else "prepare_seen_only_hard_case_enrichment"
        ),
    }

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.report_json.with_suffix(args.report_json.suffix + ".tmp")
    temporary.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    temporary.replace(args.report_json)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
