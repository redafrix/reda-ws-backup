from __future__ import annotations

import argparse
import json
import os
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from .local_chunk_quality import (
    BAD_SUBTYPE_UNKNOWN,
    LEGACY_VALIDATED_BAD,
    sample_label,
    score_state_group,
    state_id,
    summarize_continuous_rows,
)


DEFAULT_REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
DEFAULT_STAGE9_ROOT = DEFAULT_REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data"


def load_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def resolve_path(path: str | Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return DEFAULT_REDA_WS / p


def source_jsonls(input_path: Path) -> list[Path]:
    """Find sample JSONLs from a frozen snapshot, chunk root, or one JSONL."""
    if input_path.is_file():
        return [input_path]
    manifest = input_path / "chunk_manifest.json"
    if manifest.exists():
        data = json.loads(manifest.read_text())
        paths: list[Path] = []
        for chunk in data.get("chunks") or []:
            if not chunk.get("has_samples", True):
                continue
            cpath = Path(chunk.get("path", ""))
            sample_path = cpath / "counterfactual_samples.jsonl"
            if sample_path.exists():
                paths.append(sample_path)
        return sorted(set(paths))
    direct = input_path / "counterfactual_samples.jsonl"
    if direct.exists():
        return [direct]
    chunks = sorted(input_path.glob("chunks/*/counterfactual_samples.jsonl"))
    if chunks:
        return chunks
    split_sources: set[Path] = set()
    for split_root in [input_path / "splits_group_safe", input_path / "splits"]:
        if not split_root.exists():
            continue
        for split_path in split_root.glob("*.jsonl"):
            for row in load_jsonl(split_path):
                src = row.get("source_jsonl")
                if src and Path(src).exists():
                    split_sources.add(Path(src))
    return sorted(split_sources)


def load_samples(paths: list[Path], limit: int | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        dataset_name = path.parent.name
        for row in load_jsonl(path):
            row["_source_jsonl"] = str(path)
            row["_dataset_name"] = row.get("_dataset_name") or dataset_name
            rows.append(row)
            if limit is not None and len(rows) >= limit:
                return rows
    return rows


def old_bad_reasons(sample: dict[str, Any]) -> list[str]:
    label = sample.get("label") or {}
    if not isinstance(label, dict):
        return []
    reasons = label.get("validated_bad_reasons") or label.get("label_reasons") or []
    return [str(r) for r in reasons if r is not None]


def compact_row(sample: dict[str, Any], risk: dict[str, Any]) -> dict[str, Any]:
    meta = sample.get("metadata") or {}
    out = sample.get("outcome") or {}
    return {
        "sample_id": sample.get("sample_id"),
        "state_id": state_id(sample),
        "source_jsonl": sample.get("_source_jsonl"),
        "old_label": sample_label(sample),
        "old_bad_subtype": (sample.get("label") or {}).get("bad_subtype") if isinstance(sample.get("label"), dict) else None,
        "old_reasons": old_bad_reasons(sample),
        "task_name": meta.get("task_name"),
        "task_language": meta.get("task_language"),
        "suite": meta.get("libero_pro_suite_or_task"),
        "perturbation_type": meta.get("perturbation_type"),
        "phase": meta.get("parent_phase"),
        "seed": meta.get("simvla_generation_seed"),
        "parent_failed_or_timeout": meta.get("parent_failed_or_timeout"),
        "distance_to_failure_or_timeout": meta.get("distance_to_failure_or_timeout"),
        "terminal_success_audit_only": out.get("terminal_success"),
        "terminal_failure_audit_only": out.get("terminal_failure"),
        "terminal_timeout_audit_only": out.get("terminal_timeout"),
        "risk_score": risk["risk_score"],
        "risk_score_raw": risk["risk_score_raw"],
        "chunk_quality": risk["chunk_quality"],
        "risk_confidence": risk["risk_confidence"],
        "risk_bin": risk["risk_bin"],
        "legacy_label_suggestion": risk["legacy_label_suggestion"],
        "bad_subtype": risk.get("bad_subtype") or BAD_SUBTYPE_UNKNOWN,
        "positive_evidence": risk.get("positive_evidence") or [],
        "negative_evidence": risk.get("negative_evidence") or [],
        "weak_negative_evidence": risk.get("weak_negative_evidence") or [],
        "ambiguous_evidence": risk.get("ambiguous_evidence") or [],
        "risk_components": risk.get("risk_components") or {},
        "same_state_comparison_v2": risk.get("same_state_comparison_v2") or {},
        "numeric_evidence": risk.get("numeric_evidence") or {},
        "score_version": risk.get("score_version"),
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    old_counts = Counter(r["old_label"] for r in rows)
    risk_summary = summarize_continuous_rows(rows)
    cross = Counter((r["old_label"], r["risk_bin"]) for r in rows)
    old_bad = [r for r in rows if r["old_label"] == LEGACY_VALIDATED_BAD]
    old_bad_low_or_uncertain = [
        r for r in old_bad
        if r["risk_score"] < 0.65 or r["risk_confidence"] < 0.55 or not r["negative_evidence"]
    ]
    terminal_timeout_high = [
        r for r in rows
        if r["terminal_timeout_audit_only"] and r["risk_score"] >= 0.80 and not r["negative_evidence"]
    ]
    risky_unknown = [
        r for r in rows
        if r["risk_score"] >= 0.80 and r.get("bad_subtype") == BAD_SUBTYPE_UNKNOWN
    ]
    success_high_risk = [
        r for r in rows
        if r["terminal_success_audit_only"] and r["risk_score"] >= 0.80
    ]
    return {
        **risk_summary,
        "old_label_counts": dict(old_counts),
        "old_label_by_risk_bin": {f"{a}|{b}": c for (a, b), c in sorted(cross.items())},
        "old_validated_bad_count": len(old_bad),
        "old_validated_bad_low_or_uncertain_risk_count": len(old_bad_low_or_uncertain),
        "terminal_timeout_high_risk_without_negative_evidence_count": len(terminal_timeout_high),
        "high_risk_unknown_subtype_count": len(risky_unknown),
        "terminal_success_high_risk_count": len(success_high_risk),
        "continuous_label_gate_failures": {
            "old_validated_bad_low_or_uncertain": len(old_bad_low_or_uncertain),
            "terminal_timeout_high_risk_without_negative_evidence": len(terminal_timeout_high),
            "high_risk_unknown_subtype": len(risky_unknown),
        },
    }


def markdown_table(counter: dict[str, Any], key_name: str = "key") -> str:
    lines = [f"| {key_name} | count |", "|---|---:|"]
    for key, value in sorted(counter.items(), key=lambda kv: (-int(kv[1]), str(kv[0]))):
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def write_report(out_dir: Path, input_path: Path, source_paths: list[Path], summary: dict[str, Any], examples: dict[str, list[dict[str, Any]]]) -> Path:
    report_path = out_dir / "STAGE9_CONTINUOUS_RISK_LABELING_METHOD_COMPARISON_REPORT.md"
    ready = "YES"
    blockers = []
    gates = summary.get("continuous_label_gate_failures") or {}
    if summary.get("high_risk_confident_count", 0) <= 0:
        ready = "NO"
        blockers.append("static relabel produced zero confident high-risk chunks, so it cannot train a risk detector yet")
    if summary.get("old_validated_bad_low_or_uncertain_risk_count", 0):
        ready = "NO"
        blockers.append("all or some old VALIDATED_BAD labels are low/uncertain under local chunk evidence")
    if gates.get("terminal_timeout_high_risk_without_negative_evidence", 0):
        ready = "NO"
        blockers.append("some high-risk scores still lack local negative evidence")
    if gates.get("high_risk_unknown_subtype", 0):
        ready = "NO"
        blockers.append("some high-risk samples have unknown bad_subtype")

    text = f"""# Stage 9 Continuous Risk Labeling Method Comparison Report

Generated: `{time.strftime('%Y-%m-%dT%H:%M:%S')}`

## Executive Summary

Implemented and ran the Stage 9 V2 continuous relabeler on:

`{input_path}`

The main target is now:

`risk_score in [0.0, 1.0]`

where `0.0` means clearly safe/good/expert-like, `0.5` means uncertain or mixed, and `1.0` means clearly risky/bad for the local SimVLA action chunk.

Important policy change: terminal continuation success/failure/timeout is audit metadata only. It is not used as the primary source for continuous risk.

`CONTINUOUS_RISK_LABELS_READY_FOR_TRAINING = {ready}`

## Source Data

- Source JSONL files: `{len(source_paths)}`
- Samples scored: `{summary.get('num_samples')}`
- Old `VALIDATED_BAD` samples: `{summary.get('old_validated_bad_count')}`

## Continuous Label Distribution

{markdown_table(summary.get('risk_bin_counts') or {}, 'risk_bin')}

## Legacy Suggestion Distribution

These are audit bins derived from continuous risk. They are not the main training target.

{markdown_table(summary.get('legacy_label_suggestion_counts') or {}, 'legacy_label_suggestion')}

## Bad Subtype Distribution

{markdown_table(summary.get('bad_subtype_counts') or {}, 'bad_subtype')}

## Old Label Distribution

{markdown_table(summary.get('old_label_counts') or {}, 'old_label')}

## Old Label By New Risk Bin

{markdown_table(summary.get('old_label_by_risk_bin') or {}, 'old_label|risk_bin')}

## Gate Checks

- Old `VALIDATED_BAD` now low/uncertain risk or missing local negative evidence: `{summary.get('old_validated_bad_low_or_uncertain_risk_count')}`
- High-risk terminal-timeout samples without local negative evidence: `{summary.get('terminal_timeout_high_risk_without_negative_evidence_count')}`
- High-risk samples with unknown subtype: `{summary.get('high_risk_unknown_subtype_count')}`
- Terminal-success samples with high local risk: `{summary.get('terminal_success_high_risk_count')}`

## Method Ranking Implemented

1. Local simulator continuous chunk reward: implemented as `local_chunk_quality.py`.
2. Same-state local counterfactual ranking: implemented in the state-group scoring pass.
3. Expert LIBERO calibration: interface is ready; it must be run once expert demo chunks are indexed.
4. Scripted failed-episode mining: implemented separately as a risk-peak mining utility.
5. VLM/AHA audit: remains an auditor/miner, not a final label source.
6. Horizon sensitivity: diagnostic only; terminal timeout is no longer label proof.

## Examples: Low Risk

```json
{json.dumps(examples.get('low_risk', [])[:5], indent=2, sort_keys=True, default=str)}
```

## Examples: High Risk

```json
{json.dumps(examples.get('high_risk', [])[:5], indent=2, sort_keys=True, default=str)}
```

## Examples: Old VALIDATED_BAD Downgraded By Continuous Risk

```json
{json.dumps(examples.get('old_bad_downgrade', [])[:5], indent=2, sort_keys=True, default=str)}
```

## Remaining Blockers

{chr(10).join(f'- {b}' for b in blockers) if blockers else '- No relabeler gate blocker in this static pass.'}

## Output Paths

- Compact continuous labels: `{out_dir / 'continuous_risk_labels.jsonl'}`
- Summary JSON: `{out_dir / 'continuous_risk_summary.json'}`
- Examples JSON: `{out_dir / 'continuous_risk_examples.json'}`
- This report: `{report_path}`

## Final Statement

`CONTINUOUS_RISK_LABELS_READY_FOR_TRAINING = {ready}`

This is a static relabel pass over existing traces. A new V2 collection pilot is still required to get true local-only chunks, wrist/agent videos, expert-demo calibration, and failed-episode onset mining.
"""
    report_path.write_text(text)
    return report_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Frozen dir, chunk root, or counterfactual_samples.jsonl")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    input_path = resolve_path(args.input)
    out_dir = resolve_path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    paths = source_jsonls(input_path)
    if not paths:
        raise SystemExit(f"No source sample JSONLs found under {input_path}")
    samples = load_samples(paths, limit=args.limit)

    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in samples:
        groups[state_id(sample)].append(sample)

    compact_rows: list[dict[str, Any]] = []
    for _, group in sorted(groups.items()):
        risks = score_state_group(group)
        for sample, risk in zip(group, risks):
            compact_rows.append(compact_row(sample, risk))

    summary = summarize(compact_rows)
    low = sorted(compact_rows, key=lambda r: (r["risk_score"], -r["risk_confidence"]))[:20]
    high = sorted(compact_rows, key=lambda r: (-r["risk_score"], -r["risk_confidence"]))[:20]
    old_bad_downgrade = [
        r for r in compact_rows
        if r["old_label"] == LEGACY_VALIDATED_BAD and (r["risk_score"] < 0.65 or not r["negative_evidence"])
    ][:50]
    examples = {
        "low_risk": low,
        "high_risk": high,
        "old_bad_downgrade": old_bad_downgrade,
    }

    write_jsonl(out_dir / "continuous_risk_labels.jsonl", compact_rows)
    write_json(out_dir / "continuous_risk_summary.json", summary)
    write_json(out_dir / "continuous_risk_examples.json", examples)
    report_path = write_report(out_dir, input_path, paths, summary, examples)
    print(json.dumps({
        "status": "ok",
        "input": str(input_path),
        "out_dir": str(out_dir),
        "num_sources": len(paths),
        "num_samples": len(compact_rows),
        "report": str(report_path),
        "ready": "NO" if summary.get("high_risk_unknown_subtype_count") or summary.get("high_risk_confident_count", 0) <= 0 else "YES",
    }, indent=2))


if __name__ == "__main__":
    main()
