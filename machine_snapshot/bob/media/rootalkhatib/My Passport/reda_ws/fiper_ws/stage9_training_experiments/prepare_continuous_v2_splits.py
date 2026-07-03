"""
prepare_continuous_v2_splits.py – Build group-safe train/calib/test splits
for Stage 9 V2 continuous risk training.

Lives in fiper_ws/stage9_training_experiments/

Usage:
    python3 -m stage9_training_experiments.prepare_continuous_v2_splits \
        --failure-jsonl /path/to/replay_counterfactual_samples.jsonl \
        --safe-jsonl /path/to/counterfactual_samples.jsonl \
        --expert-jsonl /path/to/expert_low_risk_anchors.jsonl \
        --out-dir /path/to/splits \
        --safe-cap 5000 --seed 42
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def get_state_group_id(sample: dict) -> str:
    """Extract a group ID for group-safe splitting. All seeds of the same state stay together."""
    meta = sample.get("metadata", {})
    # Try same_state_group_summary_v2 first
    cr = sample.get("continuous_risk", {})
    ssg = cr.get("same_state_group_summary_v2", {})
    state_id = ssg.get("state_id")
    if state_id:
        return str(state_id)
    # Fallback: task + env_seed + chunk_start
    task = meta.get("task_language") or meta.get("task_name") or meta.get("task_id", "unk")
    env_seed = meta.get("env_seed", meta.get("seed", "unk"))
    chunk_start = meta.get("chunk_start", meta.get("step_start", "unk"))
    return f"{task}_eseed{env_seed}_cs{chunk_start}"


def get_risk_fields(sample: dict) -> dict:
    """Extract continuous risk fields from a sample."""
    cr = sample.get("continuous_risk", {})
    if not isinstance(cr, dict):
        cr = {}
    lbl = sample.get("label", {})
    if not isinstance(lbl, dict):
        lbl_str = str(lbl) if lbl else "GOOD_STRONG"
        lbl = {}
    else:
        lbl_str = cr.get("legacy_label_suggestion", lbl.get("legacy_label_suggestion", "GOOD_STRONG"))

    return {
        "risk_score": float(cr.get("risk_score", lbl.get("risk_score", 0.0))),
        "risk_confidence": float(cr.get("risk_confidence", lbl.get("risk_confidence", 1.0))),
        "risk_bin": str(cr.get("risk_bin", lbl.get("risk_bin", "SAFE_STRONG"))),
        "legacy_label": str(cr.get("legacy_label_suggestion", lbl_str)),
        "bad_subtype": str(cr.get("bad_subtype", lbl.get("bad_subtype", "unknown"))),
    }


def assign_split(group_id: str, seed: int) -> str:
    """Deterministic group-safe split assignment using hash."""
    h = hashlib.md5(f"{group_id}_{seed}".encode()).hexdigest()
    val = int(h[:8], 16) / 0xFFFFFFFF
    if val < 0.70:
        return "train"
    elif val < 0.80:
        return "calib"
    elif val < 0.90:
        return "test_seen_task"
    else:
        return "test_unseen_group"


def load_jsonl(path: Path, source_tag: str, cap: int = 0) -> list[dict]:
    """Load JSONL rows with source tagging."""
    if not path.exists():
        print(f"  WARN: {path} not found")
        return []
    rows = []
    with path.open() as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                row["_source_tag"] = source_tag
                row["_source_jsonl"] = str(path.absolute())
                rows.append(row)
    if cap > 0 and len(rows) > cap:
        random.shuffle(rows)
        rows = rows[:cap]
    print(f"  Loaded {len(rows)} from {path} (source={source_tag}, cap={cap})")
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--failure-jsonl", required=True)
    parser.add_argument("--safe-jsonl", required=True)
    parser.add_argument("--expert-jsonl", default="")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--safe-cap", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Loading datasets...")
    failure_rows = load_jsonl(Path(args.failure_jsonl), "failure_mined")
    safe_rows = load_jsonl(Path(args.safe_jsonl), "safe_mass", cap=args.safe_cap)
    expert_rows = []
    if args.expert_jsonl and Path(args.expert_jsonl).exists():
        expert_rows = load_jsonl(Path(args.expert_jsonl), "expert_anchor")

    all_rows = failure_rows + safe_rows + expert_rows
    print(f"Total samples: {len(all_rows)}")

    if not all_rows:
        print("ERROR: No samples loaded!")
        return

    # Group by state
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in all_rows:
        gid = get_state_group_id(row)
        groups[gid].append(row)

    print(f"State groups: {len(groups)}")

    # Assign splits
    splits: dict[str, list[dict]] = defaultdict(list)
    for gid, members in groups.items():
        split = assign_split(gid, args.seed)
        for row in members:
            rf = get_risk_fields(row)
            manifest_row = {
                "sample_id": row.get("sample_id", ""),
                "split": split,
                "group_id": gid,
                "source_tag": row.get("_source_tag", ""),
                "label": rf["legacy_label"],
                "bad_subtype": rf["bad_subtype"],
                "risk_score": rf["risk_score"],
                "risk_confidence": rf["risk_confidence"],
                "risk_bin": rf["risk_bin"],
                "source_jsonl": row.get("_source_jsonl", ""),
            }
            splits[split].append(manifest_row)

    # Write split files
    for split_name, rows in splits.items():
        path = out_dir / f"{split_name}.jsonl"
        with path.open("w") as f:
            for r in rows:
                f.write(json.dumps(r, default=str) + "\n")
        print(f"  {split_name}: {len(rows)} samples")

    # Write combined manifest
    all_manifest = []
    for split_name, rows in splits.items():
        all_manifest.extend(rows)
    (out_dir / "all_manifest.jsonl").write_text(
        "\n".join(json.dumps(r, default=str) for r in all_manifest) + "\n"
    )

    # Summary stats
    summary: dict[str, Any] = {
        "total_samples": len(all_rows),
        "total_groups": len(groups),
        "splits": {},
        "source_counts": dict(Counter(r.get("_source_tag", "") for r in all_rows)),
    }

    for split_name, rows in splits.items():
        risk_scores = [r["risk_score"] for r in rows]
        labels = [r["label"] for r in rows]
        bins = [r["risk_bin"] for r in rows]
        subtypes = [r["bad_subtype"] for r in rows]
        sources = [r["source_tag"] for r in rows]
        summary["splits"][split_name] = {
            "count": len(rows),
            "label_counts": dict(Counter(labels)),
            "risk_bin_counts": dict(Counter(bins)),
            "bad_subtype_counts": dict(Counter(subtypes)),
            "source_counts": dict(Counter(sources)),
            "risk_score_mean": float(sum(risk_scores) / max(1, len(risk_scores))),
            "risk_score_min": float(min(risk_scores)) if risk_scores else None,
            "risk_score_max": float(max(risk_scores)) if risk_scores else None,
            "high_risk_count": sum(1 for r in risk_scores if r >= 0.75),
            "low_risk_count": sum(1 for r in risk_scores if r <= 0.20),
        }

    # Leakage check
    split_groups: dict[str, set] = defaultdict(set)
    for split_name, rows in splits.items():
        for r in rows:
            split_groups[split_name].add(r["group_id"])
    leakage = {}
    split_names = list(split_groups.keys())
    for i, s1 in enumerate(split_names):
        for s2 in split_names[i + 1:]:
            overlap = split_groups[s1] & split_groups[s2]
            leakage[f"{s1}_vs_{s2}"] = len(overlap)
    summary["leakage_check"] = leakage

    (out_dir / "split_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + "\n")
    print(f"\nSplit summary written to {out_dir / 'split_summary.json'}")
    print(json.dumps(summary, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
