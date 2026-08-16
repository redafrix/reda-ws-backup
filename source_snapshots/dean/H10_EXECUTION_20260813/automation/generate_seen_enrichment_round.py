#!/usr/bin/env python3
"""Build a seen-only hard-case replay shard from audited broad-round evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
EVAL_CONFIG = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/"
    "generated_simvla_configs/eval_softplus_110k.yaml"
)


def sha256_file(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_once(path: Path, text: str) -> None:
    if path.exists():
        if path.read_text() != text:
            raise RuntimeError(f"refusing to overwrite enrichment evidence: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def choose_source_round() -> Path:
    candidates = []
    for summary_path in sorted(
        (WORKSPACE / "outputs").glob(
            "final_seen_h10_round_*_seed*/reports/round_audit_summary.json"
        )
    ):
        summary = json.loads(summary_path.read_text())
        if summary.get("exhaustive_audit_pass") and summary["round"]["round_kind"] == "broad":
            candidates.append(summary_path.parents[1])
    if not candidates:
        raise RuntimeError("no audited broad round exists for seen enrichment")
    return max(candidates, key=lambda root: int(json.loads((root / "run_manifest.json").read_text())["round"]["round_id"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round-id", type=int, required=True)
    parser.add_argument("--policy-seed", type=int, required=True)
    parser.add_argument("--episodes", type=int, default=1000)
    args = parser.parse_args()
    if args.episodes != 1000:
        raise ValueError("hard-case enrichment shards contain exactly 1000 scenes")
    source_root = choose_source_round()
    run_manifest = json.loads((source_root / "run_manifest.json").read_text())
    source_manifest_path = Path(run_manifest["manifest_path"])
    source_manifest = json.loads(source_manifest_path.read_text())
    entries = {
        int(item["scene"]["source_episode_id"]): item
        for item in source_manifest["episodes"]
    }
    ranked = []
    for path in (source_root / "episodes").glob("*/summary.json"):
        summary = json.loads(path.read_text())
        rank = (
            0 if summary["outcome"] == "failure_or_timeout" else 1,
            -int(summary["simulation_steps"]),
            -float(summary["minimum_tcp_distance_m"]),
            int(summary["source_episode_id"]),
        )
        ranked.append((rank, summary))
    ranked.sort(key=lambda item: item[0])
    selected_summaries = [item[1] for item in ranked[: args.episodes]]
    if len(selected_summaries) != args.episodes:
        raise RuntimeError("source broad round has too few valid enrichment scenes")

    generated = WORKSPACE / "automation/generated" / f"round_{args.round_id:03d}"
    manifest_path = generated / "manifest.json"
    collection_path = generated / "collection_config.yaml"
    run_config_path = generated / "run_config.yaml"
    source_collection = Path(run_manifest["collection_config_path"])
    write_once(collection_path, source_collection.read_text())
    records = []
    for benchmark_id, summary in enumerate(selected_summaries):
        source_id = int(summary["source_episode_id"])
        source = entries[source_id]
        records.append(
            {
                "benchmark_episode_id": benchmark_id,
                "risk_split": "unassigned",
                "scene": source["scene"],
                "scene_fingerprint_sha256": source["scene_fingerprint_sha256"],
            }
        )
    payload = {
        "schema_version": "simvla_reaching_ood_benchmark_v1",
        "benchmark_name": f"reaching_pose_v1_seen_enrichment_{args.round_id:03d}",
        "collection_config": str(collection_path),
        "collection_index": int(run_manifest["round"].get("collection_index", 0)),
        "seed": int(source_manifest["seed"]),
        "provenance": {
            "source_manifest": run_manifest["source_manifest_path"],
            "source_manifest_sha256": run_manifest["source_manifest_sha256"],
            "source_broad_round": str(source_root),
            "source_broad_run_manifest_sha256": sha256_file(source_root / "run_manifest.json"),
            "selection": "genuine failures first, then longest/highest-distance successful seen episodes",
            "scientific_split_pending": True,
            "ood_used": False,
            "scene_family_replays_grouped_at_split": True,
        },
        "episodes": records,
    }
    payload["manifest_fingerprint_sha256"] = canonical_hash(payload)
    write_once(manifest_path, json.dumps(payload, indent=2) + "\n")
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
    report = {
        "schema_version": "simvla_seen_hard_case_enrichment_v1",
        "round_id": args.round_id,
        "round_kind": "enrichment",
        "policy_seed": args.policy_seed,
        "episode_count": len(records),
        "source_broad_round": str(source_root),
        "manifest_path": str(manifest_path),
        "manifest_sha256": sha256_file(manifest_path),
        "run_config_path": str(run_config_path),
        "run_config_sha256": sha256_file(run_config_path),
        "output_dir": str(output),
        "ood_used_for_enrichment": False,
    }
    write_once(generated / "generation_report.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
