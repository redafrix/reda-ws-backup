from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np


SAFE_BINS = {"SAFE_STRONG", "SAFE_WEAK"}
RISKY_BINS = {"RISKY_STRONG", "RISKY_WEAK"}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    if not path.exists():
        return rows
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                rows.append({"_corrupt_line": line[:500], "_source_path": str(path)})
    return rows


def label_dict(row: dict[str, Any]) -> dict[str, Any]:
    label = row.get("label")
    return label if isinstance(label, dict) else {}


def metadata(row: dict[str, Any]) -> dict[str, Any]:
    meta = row.get("metadata")
    return meta if isinstance(meta, dict) else {}


def state_id(row: dict[str, Any]) -> str:
    return str(metadata(row).get("state_id") or row.get("state_id") or "unknown")


def seed_value(row: dict[str, Any]) -> Any:
    meta = metadata(row)
    cand = row.get("candidate_action") if isinstance(row.get("candidate_action"), dict) else {}
    return meta.get("simvla_generation_seed", cand.get("simvla_seed"))


def risk_bin(row: dict[str, Any]) -> str:
    label = label_dict(row)
    return str(label.get("risk_bin") or label.get("final_label") or label.get("label") or "UNKNOWN")


def risk_score(row: dict[str, Any]) -> float | None:
    label = label_dict(row)
    value = label.get("risk_score")
    if value is None and isinstance(row.get("continuous_risk"), dict):
        value = row["continuous_risk"].get("risk_score")
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(value):
        return None
    return value


def bad_subtype(row: dict[str, Any]) -> str:
    return str(label_dict(row).get("bad_subtype") or "unknown")


def negative_tuple(row: dict[str, Any]) -> tuple[str, ...]:
    vals = label_dict(row).get("negative_evidence") or []
    return tuple(str(v) for v in vals)


def weak_negative_tuple(row: dict[str, Any]) -> tuple[str, ...]:
    vals = label_dict(row).get("weak_negative_evidence") or []
    return tuple(str(v) for v in vals)


def action_vector(row: dict[str, Any]) -> np.ndarray | None:
    cand = row.get("candidate_action")
    if not isinstance(cand, dict):
        return None
    action = cand.get("candidate_action_env")
    if action is None:
        return None
    try:
        arr = np.asarray(action, dtype=float).reshape(-1)
    except Exception:
        return None
    if arr.size == 0:
        return None
    return arr


def summarize_group(group: list[dict[str, Any]]) -> dict[str, Any]:
    bins = Counter(risk_bin(r) for r in group)
    subtypes = Counter(bad_subtype(r) for r in group)
    seeds = [seed_value(r) for r in group]
    unique_seeds = len({str(s) for s in seeds})
    scores = [s for s in (risk_score(r) for r in group) if s is not None]
    high = sum(1 for b in bins for _ in range(bins[b]) if b in RISKY_BINS)
    low = sum(1 for b in bins for _ in range(bins[b]) if b in SAFE_BINS)
    action_specific = subtypes.get("action_specific", 0)
    state_context = subtypes.get("state_context", 0)
    if high > 0 and low > 0 and action_specific > 0:
        group_type = "action_specific_mixed"
    elif high > 0 and low > 0:
        group_type = "mixed_needs_review"
    elif high == len(group) and group:
        group_type = "all_risky_state_context_candidate"
    elif low == len(group) and group:
        group_type = "all_safe_or_weak_safe"
    else:
        group_type = "uncertain_or_other"

    arrs = [a for a in (action_vector(r) for r in group) if a is not None]
    action_div = None
    first_action_div = None
    unique_action_hashes = 0
    if arrs:
        min_len = min(a.size for a in arrs)
        mat = np.stack([a[:min_len] for a in arrs])
        mean = mat.mean(axis=0)
        action_div = {
            "mean_l2_to_group_mean": float(np.linalg.norm(mat - mean, axis=1).mean()),
            "max_l2_to_group_mean": float(np.linalg.norm(mat - mean, axis=1).max()),
        }
        first_len = min(7, min_len)
        first = mat[:, :first_len]
        first_mean = first.mean(axis=0)
        first_action_div = {
            "mean_l2_to_group_mean": float(np.linalg.norm(first - first_mean, axis=1).mean()),
            "max_l2_to_group_mean": float(np.linalg.norm(first - first_mean, axis=1).max()),
        }
        unique_action_hashes = len({tuple(np.round(a[:min_len], 5).tolist()) for a in arrs})

    score_range = (max(scores) - min(scores)) if scores else None
    scorer_saturation = bool(
        scores
        and score_range is not None
        and score_range < 1e-9
        and action_div is not None
        and action_div["mean_l2_to_group_mean"] > 0.05
    )
    return {
        "state_id": state_id(group[0]) if group else "unknown",
        "num_samples": len(group),
        "group_type": group_type,
        "risk_bin_counts": dict(bins),
        "bad_subtype_counts": dict(subtypes),
        "unique_seed_count": unique_seeds,
        "duplicate_seed_count": len(seeds) - unique_seeds,
        "risk_score_min": min(scores) if scores else None,
        "risk_score_max": max(scores) if scores else None,
        "risk_score_range": score_range,
        "unique_action_hashes_rounded_5dp": unique_action_hashes,
        "action_diversity": action_div,
        "first_action_diversity": first_action_div,
        "scorer_saturation_possible": scorer_saturation,
        "task_name": metadata(group[0]).get("task_name") if group else None,
        "phase": metadata(group[0]).get("parent_phase") if group else None,
        "window_selection_reason": metadata(group[0]).get("window_selection_reason") if group else None,
    }


def summarize_dir(path: Path) -> dict[str, Any]:
    replay = load_jsonl(path / "replay_counterfactual_samples.jsonl")
    dense_replay = load_jsonl(path / "dense_replay_counterfactual_samples.jsonl")
    counterfactual = load_jsonl(path / "counterfactual_samples.jsonl")
    episode_chunks = load_jsonl(path / "episode_chunks.jsonl")
    dense_parent = load_jsonl(path / "dense_parent_timesteps.jsonl")
    rows = replay or dense_replay or counterfactual
    groups = defaultdict(list)
    for row in rows:
        groups[state_id(row)].append(row)
    group_summaries = [summarize_group(group) for group in groups.values()]
    group_types = Counter(g["group_type"] for g in group_summaries)
    score_ranges = [g["risk_score_range"] for g in group_summaries if g["risk_score_range"] is not None]
    action_divs = [
        g["action_diversity"]["mean_l2_to_group_mean"]
        for g in group_summaries
        if g.get("action_diversity")
    ]
    out = {
        "path": str(path),
        "replay_samples": len(replay),
        "dense_replay_samples": len(dense_replay),
        "counterfactual_samples": len(counterfactual),
        "episode_chunks": len(episode_chunks),
        "dense_parent_timesteps": len(dense_parent),
        "analyzed_samples": len(rows),
        "same_state_groups": len(group_summaries),
        "risk_bin_counts": dict(Counter(risk_bin(r) for r in rows)),
        "bad_subtype_counts": dict(Counter(bad_subtype(r) for r in rows)),
        "negative_evidence_counts": {" | ".join(k) if k else "none": v for k, v in Counter(negative_tuple(r) for r in rows).most_common(20)},
        "weak_negative_evidence_counts": {" | ".join(k) if k else "none": v for k, v in Counter(weak_negative_tuple(r) for r in rows).most_common(20)},
        "group_type_counts": dict(group_types),
        "groups_with_duplicate_seeds": sum(1 for g in group_summaries if g["duplicate_seed_count"] > 0),
        "groups_with_possible_scorer_saturation": sum(1 for g in group_summaries if g["scorer_saturation_possible"]),
        "risk_score_range_mean": float(np.mean(score_ranges)) if score_ranges else None,
        "risk_score_range_max": float(np.max(score_ranges)) if score_ranges else None,
        "action_diversity_mean": float(np.mean(action_divs)) if action_divs else None,
        "action_diversity_max": float(np.max(action_divs)) if action_divs else None,
        "top_mixed_groups": [
            g for g in group_summaries if g["group_type"] in {"action_specific_mixed", "mixed_needs_review"}
        ][:20],
        "top_saturation_groups": [
            g for g in group_summaries if g["scorer_saturation_possible"]
        ][:20],
        "example_all_risky_groups": [
            g for g in group_summaries if g["group_type"] == "all_risky_state_context_candidate"
        ][:10],
        "example_all_safe_groups": [
            g for g in group_summaries if g["group_type"] == "all_safe_or_weak_safe"
        ][:10],
    }
    return out


def write_report(path: Path, summaries: list[dict[str, Any]]) -> None:
    lines = ["# Stage 9 V2 Collection Diagnosis", ""]
    for s in summaries:
        lines.extend([
            f"## {s['path']}",
            "",
            f"- Analyzed samples: `{s['analyzed_samples']}`",
            f"- Replay samples: `{s['replay_samples']}`",
            f"- Dense replay samples: `{s.get('dense_replay_samples')}`",
            f"- Episode chunks: `{s['episode_chunks']}`",
            f"- Dense parent timesteps: `{s.get('dense_parent_timesteps')}`",
            f"- Same-state groups: `{s['same_state_groups']}`",
            f"- Risk bins: `{s['risk_bin_counts']}`",
            f"- Bad subtypes: `{s['bad_subtype_counts']}`",
            f"- Group types: `{s['group_type_counts']}`",
            f"- Duplicate-seed groups: `{s['groups_with_duplicate_seeds']}`",
            f"- Possible scorer saturation groups: `{s['groups_with_possible_scorer_saturation']}`",
            f"- Mean risk-score range/group: `{s['risk_score_range_mean']}`",
            f"- Max risk-score range/group: `{s['risk_score_range_max']}`",
            f"- Mean action diversity/group: `{s['action_diversity_mean']}`",
            f"- Max action diversity/group: `{s['action_diversity_max']}`",
            "",
        ])
        if s["top_mixed_groups"]:
            lines.append("### Mixed Groups")
            lines.append("")
            for g in s["top_mixed_groups"][:10]:
                lines.append(f"- `{g['state_id']}` `{g['group_type']}` bins={g['risk_bin_counts']} subtypes={g['bad_subtype_counts']} range={g['risk_score_range']} div={g.get('action_diversity')}")
            lines.append("")
        if s["top_saturation_groups"]:
            lines.append("### Possible Scorer Saturation")
            lines.append("")
            for g in s["top_saturation_groups"][:10]:
                lines.append(f"- `{g['state_id']}` bins={g['risk_bin_counts']} range={g['risk_score_range']} div={g.get('action_diversity')}")
            lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--out-json", default=None)
    parser.add_argument("--out-md", default=None)
    args = parser.parse_args()

    summaries = [summarize_dir(Path(p)) for p in args.paths]
    print(json.dumps({"summaries": summaries}, indent=2, sort_keys=True, default=str))
    if args.out_json:
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_json).write_text(json.dumps({"summaries": summaries}, indent=2, sort_keys=True, default=str) + "\n")
    if args.out_md:
        write_report(Path(args.out_md), summaries)


if __name__ == "__main__":
    main()
