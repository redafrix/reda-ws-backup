#!/usr/bin/env python3
"""Freeze audited real seen rounds into group-disjoint TopK8 training arrays."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import sys
import time
from typing import Any

import numpy as np
from numpy.lib.format import open_memmap

PIPELINE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE))

from common import (  # noqa: E402
    ACTION_SHAPE,
    FEATURE_SCHEMA_VERSION,
    HISTORY_SHAPE,
    STATIC_DIM,
    feature_tensors,
    fit_normalization,
    serialize_stats,
    sha256_file,
    write_json_atomic,
)

WORKSPACE = PIPELINE.parent
OUTPUTS = WORKSPACE / "outputs"
DEFAULT_OUTPUT = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1"
SPLIT_SEED = 20260622


@dataclass(frozen=True)
class Episode:
    episode_id: str
    group_id: str
    label: int
    strict_label: int
    rows: int
    rows_path: Path
    summary_path: Path
    round_output: Path


def open_rows(path: Path):
    if path.suffix != ".zst":
        return path.open()
    process = subprocess.Popen(
        ["zstd", "-q", "-dc", str(path)],
        stdout=subprocess.PIPE,
        text=True,
    )
    if process.stdout is None:
        raise RuntimeError(f"failed to open zstd stream: {path}")

    class Stream:
        def __enter__(self):
            return process.stdout

        def __exit__(self, exc_type, exc, traceback):
            process.stdout.close()
            return_code = process.wait()
            if exc_type is None and return_code:
                raise RuntimeError(f"zstd stream failed rc={return_code}: {path}")

    return Stream()


def audited_rounds() -> list[Path]:
    roots: list[Path] = []
    for summary_path in sorted(
        OUTPUTS.glob("final_seen_h10_round_*_seed*/reports/round_audit_summary.json")
    ):
        if "SUPERSEDED" in str(summary_path) or "TIMEOUT3600" in str(summary_path):
            continue
        summary = json.loads(summary_path.read_text())
        audit_path = summary_path.parent / "exhaustive_audit.json"
        if not summary.get("exhaustive_audit_pass") or not audit_path.is_file():
            continue
        audit = json.loads(audit_path.read_text())
        if not audit.get("pass"):
            continue
        roots.append(summary_path.parents[1].resolve())
    return roots


def load_operational_labels(root: Path) -> dict[str, int]:
    path = root / "reports/dual_threshold_episode_labels.jsonl"
    if not path.is_file():
        raise RuntimeError(
            "operational_4cm labels require exact dual-threshold evidence: "
            f"{path}"
        )
    labels: dict[str, int] = {}
    with path.open() as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            episode_id = str(item["episode_id"])
            if episode_id in labels:
                raise RuntimeError(f"duplicate operational label: {path}:{line_number}")
            labels[episode_id] = int(item["operational_4cm_risk_label"])
    return labels


def inventory(rounds: list[Path], label_contract: str) -> list[Episode]:
    episodes: list[Episode] = []
    ids: set[str] = set()
    for root in rounds:
        operational_labels = (
            load_operational_labels(root)
            if label_contract == "operational_4cm"
            else {}
        )
        root_episode_ids: set[str] = set()
        for episode_dir in sorted((root / "episodes").iterdir()):
            if not episode_dir.is_dir() or not (episode_dir / "COMMITTED").is_file():
                continue
            summary_path = episode_dir / "summary.json"
            rows_path = episode_dir / "risk_rows.jsonl"
            if not rows_path.is_file():
                rows_path = episode_dir / "risk_rows.jsonl.zst"
            if not rows_path.is_file():
                raise FileNotFoundError(f"missing episode rows: {episode_dir}")
            summary = json.loads(summary_path.read_text())
            episode_id = str(summary["episode_id"])
            root_episode_ids.add(episode_id)
            if episode_id in ids:
                raise RuntimeError(f"duplicate global episode ID: {episode_id}")
            ids.add(episode_id)
            if summary.get("synthetic_smoke") or not summary.get("training_eligible"):
                raise RuntimeError(f"ineligible episode entered audited seen round: {episode_id}")
            if summary.get("risk_split") != "unassigned_seen":
                raise RuntimeError(f"premature scientific split in {episode_id}")
            outcome = str(summary["outcome"])
            if outcome not in {"success", "failure_or_timeout"}:
                raise RuntimeError(f"invalid outcome in {episode_id}: {outcome}")
            strict_label = 0 if outcome == "success" else 1
            if int(summary["risk_label"]) != strict_label:
                raise RuntimeError(f"summary label mismatch in {episode_id}")
            label = (
                operational_labels[episode_id]
                if label_contract == "operational_4cm"
                else strict_label
            )
            episodes.append(
                Episode(
                    episode_id=episode_id,
                    group_id=str(
                        summary.get("scene_family_id")
                        or f"scene_sha256:{summary['scene_fingerprint_sha256']}"
                    ),
                    label=label,
                    strict_label=strict_label,
                    rows=int(summary["decision_rows"]),
                    rows_path=rows_path,
                    summary_path=summary_path,
                    round_output=root,
                )
            )
        if label_contract == "operational_4cm" and set(operational_labels) != root_episode_ids:
            missing = sorted(root_episode_ids - set(operational_labels))
            extra = sorted(set(operational_labels) - root_episode_ids)
            raise RuntimeError(
                f"operational label coverage mismatch for {root}: "
                f"missing={missing[:10]} extra={extra[:10]}"
            )
    return episodes


def split_groups(
    episodes: list[Episode], minimum_holdout_failures: int
) -> tuple[dict[str, str], dict[str, Any]]:
    by_group: dict[str, list[Episode]] = defaultdict(list)
    for episode in episodes:
        by_group[episode.group_id].append(episode)
    strata: dict[int, list[str]] = {0: [], 1: []}
    for group_id, group in by_group.items():
        strata[max(episode.label for episode in group)].append(group_id)
    rng = random.Random(SPLIT_SEED)
    assignments: dict[str, str] = {}
    counts: dict[str, Counter[str]] = {}
    for label, groups in strata.items():
        groups.sort()
        rng.shuffle(groups)
        train_count = int(round(len(groups) * 0.70))
        validation_count = int(round(len(groups) * 0.15))
        partitions = {
            "train": groups[:train_count],
            "validation": groups[train_count : train_count + validation_count],
            "test": groups[train_count + validation_count :],
        }
        counts[str(label)] = Counter({name: len(values) for name, values in partitions.items()})
        for name, values in partitions.items():
            for group_id in values:
                assignments[group_id] = name
    if set(assignments) != set(by_group):
        raise RuntimeError("not every scene family received a scientific split")
    episode_counts = Counter(assignments[episode.group_id] for episode in episodes)
    failure_counts = Counter(
        assignments[episode.group_id] for episode in episodes if episode.label == 1
    )
    if (
        failure_counts["validation"] < minimum_holdout_failures
        or failure_counts["test"] < minimum_holdout_failures
    ):
        raise RuntimeError(
            "scientific split has too few genuine failures in validation or test: "
            f"required={minimum_holdout_failures}, actual={dict(failure_counts)}"
        )
    return assignments, {
        "seed": SPLIT_SEED,
        "ratios": {"train": 0.70, "validation": 0.15, "test": 0.15},
        "group_key": "scene_family_id (scene fingerprint fallback)",
        "stratification": "group-level any-failure outcome",
        "group_stratum_counts": {key: dict(value) for key, value in counts.items()},
        "episode_counts": dict(episode_counts),
        "failure_episode_counts": dict(failure_counts),
        "group_count": len(by_group),
        "minimum_holdout_failures_required": minimum_holdout_failures,
    }


def write_split(
    root: Path,
    split: str,
    episodes: list[Episode],
) -> dict[str, Any]:
    destination = root / split
    destination.mkdir(parents=True)
    row_count = sum(episode.rows for episode in episodes)
    history = open_memmap(destination / "history.npy", mode="w+", dtype="float32", shape=(row_count, *HISTORY_SHAPE))
    action = open_memmap(destination / "action.npy", mode="w+", dtype="float32", shape=(row_count, *ACTION_SHAPE))
    static = open_memmap(destination / "static.npy", mode="w+", dtype="float32", shape=(row_count, STATIC_DIM))
    label = open_memmap(destination / "label.npy", mode="w+", dtype="float32", shape=(row_count,))
    episode_index = open_memmap(destination / "episode_index.npy", mode="w+", dtype="int32", shape=(row_count,))
    decision_index = open_memmap(destination / "decision_index.npy", mode="w+", dtype="int32", shape=(row_count,))
    episode_metadata: list[dict[str, Any]] = []
    cursor = 0
    for output_episode_index, episode in enumerate(sorted(episodes, key=lambda item: item.episode_id)):
        summary = json.loads(episode.summary_path.read_text())
        start = cursor
        with open_rows(episode.rows_path) as handle:
            for expected_decision, line in enumerate(handle):
                if not line.strip():
                    continue
                row = json.loads(line)
                if row["episode_id"] != episode.episode_id:
                    raise RuntimeError(f"row episode identity mismatch: {episode.episode_id}")
                if int(row["decision_index"]) != expected_decision:
                    raise RuntimeError(f"noncontiguous row index in {episode.episode_id}")
                if int(row["parent_episode_risk_label"]) != episode.strict_label:
                    raise RuntimeError(f"strict source-row label mismatch in {episode.episode_id}")
                metadata = row.get("metadata", {})
                if metadata.get("synthetic_smoke") or not metadata.get("training_eligible"):
                    raise RuntimeError(f"ineligible row in {episode.episode_id}")
                if metadata.get("risk_split") != "unassigned_seen":
                    raise RuntimeError(f"OOD or assigned row in {episode.episode_id}")
                h, a, s = feature_tensors(row)
                history[cursor] = h
                action[cursor] = a
                static[cursor] = s
                label[cursor] = episode.label
                episode_index[cursor] = output_episode_index
                decision_index[cursor] = expected_decision
                cursor += 1
        if cursor - start != episode.rows:
            raise RuntimeError(
                f"row count mismatch {episode.episode_id}: {cursor-start} != {episode.rows}"
            )
        episode_metadata.append(
            {
                "episode_index": output_episode_index,
                "episode_id": episode.episode_id,
                "scene_family_id": episode.group_id,
                "label": episode.label,
                "strict_2cm_label": episode.strict_label,
                "rows": episode.rows,
                "row_start": start,
                "row_end_exclusive": cursor,
                "instruction": summary["instruction"],
                "source_episode_id": summary["source_episode_id"],
                "round_id": summary["round_id"],
                "summary_path": str(episode.summary_path),
                "summary_sha256": sha256_file(episode.summary_path),
                "rows_path": str(episode.rows_path),
                "rows_sha256": sha256_file(episode.rows_path),
            }
        )
    if cursor != row_count:
        raise RuntimeError(f"split row count mismatch: {cursor} != {row_count}")
    for array in (history, action, static, label, episode_index, decision_index):
        array.flush()
    write_json_atomic(destination / "episodes.json", episode_metadata)
    return {
        "episodes": len(episodes),
        "failures": sum(episode.label for episode in episodes),
        "successes": sum(1 - episode.label for episode in episodes),
        "rows": row_count,
        "files": {
            path.name: {"bytes": path.stat().st_size, "sha256": sha256_file(path)}
            for path in sorted(destination.glob("*.npy"))
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--label-contract",
        choices=("strict_2cm", "operational_4cm"),
        required=True,
        help="Scientific episode outcome used as the risk target.",
    )
    parser.add_argument("--minimum-total-failures", type=int, default=300)
    parser.add_argument("--minimum-holdout-failures", type=int, default=40)
    parser.add_argument("--allow-limited-failures", action="store_true")
    parser.add_argument("--limited-failure-override-file", type=Path)
    args = parser.parse_args()
    limited_override = (
        args.minimum_total_failures < 300 or args.minimum_holdout_failures < 40
    )
    if limited_override:
        if not args.allow_limited_failures:
            raise RuntimeError("reduced failure gates require --allow-limited-failures")
        if (
            args.limited_failure_override_file is None
            or not args.limited_failure_override_file.is_file()
        ):
            raise RuntimeError(
                "reduced failure gates require an existing override evidence file"
            )
        override_reason = args.limited_failure_override_file.read_text().strip()
        if not override_reason:
            raise RuntimeError("limited-failure override evidence is empty")
    else:
        override_reason = None
    destination = args.output_root.resolve()
    completed = destination / "FROZEN_AND_VALIDATED"
    if completed.is_file():
        print((destination / "dataset_manifest.json").read_text())
        return 0
    rounds = audited_rounds()
    if not rounds:
        raise RuntimeError("no completed exhaustively audited broad round exists")
    episodes = inventory(rounds, args.label_contract)
    successes = sum(episode.label == 0 for episode in episodes)
    failures = sum(episode.label == 1 for episode in episodes)
    if successes < 3000 or failures < args.minimum_total_failures:
        raise RuntimeError(
            "collection gate not met: "
            f"successes={successes}, failures={failures}, "
            f"minimum_failures={args.minimum_total_failures}"
        )
    assignments, split_contract = split_groups(
        episodes, args.minimum_holdout_failures
    )
    staging = destination.parent / f".{destination.name}.staging-{os.getpid()}"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    started = time.time()
    split_reports: dict[str, Any] = {}
    for split in ("train", "validation", "test"):
        selected = [episode for episode in episodes if assignments[episode.group_id] == split]
        split_reports[split] = write_split(staging, split, selected)

    train = staging / "train"
    stats = fit_normalization(
        np.load(train / "history.npy", mmap_mode="r"),
        np.load(train / "action.npy", mmap_mode="r"),
        np.load(train / "static.npy", mmap_mode="r"),
    )
    normalization = serialize_stats(
        stats,
        provenance={
            "fit_split": "train",
            "train_rows": split_reports["train"]["rows"],
            "train_episodes": split_reports["train"]["episodes"],
            "round_outputs": [str(path) for path in rounds],
        },
    )
    write_json_atomic(staging / "normalization.json", normalization)
    split_assignments = {
        episode.episode_id: {
            "split": assignments[episode.group_id],
            "scene_family_id": episode.group_id,
            "label": episode.label,
            "strict_2cm_label": episode.strict_label,
        }
        for episode in sorted(episodes, key=lambda item: item.episode_id)
    }
    write_json_atomic(staging / "split_assignments.json", split_assignments)
    manifest = {
        "schema_version": "simvla_isaac_topk8_frozen_dataset_v1",
        "feature_schema_version": FEATURE_SCHEMA_VERSION,
        "label_contract": args.label_contract,
        "limited_failure_override": {
            "enabled": limited_override,
            "reason": override_reason,
            "evidence_path": (
                str(args.limited_failure_override_file.resolve())
                if args.limited_failure_override_file is not None
                else None
            ),
            "minimum_total_failures": args.minimum_total_failures,
            "minimum_holdout_failures": args.minimum_holdout_failures,
            "observed_total_failures": failures,
        },
        "created_at_unix_s": time.time(),
        "source_rounds": [
            {
                "output": str(root),
                "run_manifest_sha256": sha256_file(root / "run_manifest.json"),
                "exhaustive_audit_sha256": sha256_file(root / "reports/exhaustive_audit.json"),
                "round_summary_sha256": sha256_file(root / "reports/round_audit_summary.json"),
                "dual_threshold_labels_sha256": (
                    sha256_file(root / "reports/dual_threshold_episode_labels.jsonl")
                    if args.label_contract == "operational_4cm"
                    else None
                ),
            }
            for root in rounds
        ],
        "split_contract": split_contract,
        "splits": split_reports,
        "normalization": {
            "path": str(destination / "normalization.json"),
            "fit_split": "train",
            "sha256": sha256_file(staging / "normalization.json"),
        },
        "excluded": {
            "synthetic_smokes": True,
            "infrastructure_errors": True,
            "timeout3600_quarantine": True,
            "ood150": True,
        },
        "elapsed_seconds": time.time() - started,
    }
    write_json_atomic(staging / "dataset_manifest.json", manifest)
    (staging / "FROZEN_AND_VALIDATED").write_text("validated\n")
    if destination.exists():
        raise RuntimeError(f"refusing to overwrite frozen dataset: {destination}")
    staging.replace(destination)
    print((destination / "dataset_manifest.json").read_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
