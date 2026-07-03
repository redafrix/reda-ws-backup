from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def table(counter: dict[str, Any], name: str) -> str:
    lines = [f"| {name} | count |", "|---|---:|"]
    for key, value in sorted(counter.items(), key=lambda kv: (-int(kv[1]), str(kv[0]))):
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_old = Counter(r.get("old_label") for r in rows)
    by_bin = Counter(r.get("risk_bin") for r in rows)
    by_legacy = Counter(r.get("legacy_label_suggestion") for r in rows)
    by_subtype = Counter(r.get("bad_subtype") for r in rows)
    by_phase = defaultdict(list)
    by_task = defaultdict(list)
    by_perturbation = defaultdict(list)
    for row in rows:
        by_phase[row.get("phase")].append(float(row.get("risk_score", 0.5)))
        by_task[row.get("task_name")].append(float(row.get("risk_score", 0.5)))
        by_perturbation[row.get("perturbation_type")].append(float(row.get("risk_score", 0.5)))
    old_bad = [r for r in rows if r.get("old_label") == "VALIDATED_BAD"]
    old_good = [r for r in rows if r.get("old_label") == "GOOD_STRONG"]
    return {
        "num_samples": len(rows),
        "old_label_counts": dict(by_old),
        "risk_bin_counts": dict(by_bin),
        "legacy_label_suggestion_counts": dict(by_legacy),
        "bad_subtype_counts": dict(by_subtype),
        "old_validated_bad_mean_risk": mean([float(r.get("risk_score", 0.5)) for r in old_bad]),
        "old_good_strong_mean_risk": mean([float(r.get("risk_score", 0.5)) for r in old_good]),
        "old_validated_bad_low_or_uncertain_count": sum(
            1 for r in old_bad if float(r.get("risk_score", 0.5)) < 0.65 or not r.get("negative_evidence")
        ),
        "old_good_strong_high_risk_count": sum(1 for r in old_good if float(r.get("risk_score", 0.5)) >= 0.65),
        "phase_mean_risk": {str(k): mean(v) for k, v in by_phase.items()},
        "task_mean_risk": {str(k): mean(v) for k, v in by_task.items()},
        "perturbation_mean_risk": {str(k): mean(v) for k, v in by_perturbation.items()},
    }


def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--continuous-labels", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()

    rows = load_jsonl(Path(args.continuous_labels))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    summary = summarize(rows)
    write_json(out_dir / "method_comparison_summary.json", summary)

    report = f"""# Stage 9 Labeling Method Comparison

## Summary

This comparison evaluates the old discrete Stage 9 labels against the new continuous local chunk-risk labels.

- Samples: `{summary['num_samples']}`
- Old `VALIDATED_BAD` with low/uncertain continuous risk or no local negative evidence: `{summary['old_validated_bad_low_or_uncertain_count']}`
- Old `GOOD_STRONG` with high continuous risk: `{summary['old_good_strong_high_risk_count']}`
- Old `VALIDATED_BAD` mean risk: `{summary['old_validated_bad_mean_risk']}`
- Old `GOOD_STRONG` mean risk: `{summary['old_good_strong_mean_risk']}`

## Old Labels

{table(summary['old_label_counts'], 'old_label')}

## Continuous Risk Bins

{table(summary['risk_bin_counts'], 'risk_bin')}

## Legacy Suggestions From Continuous Risk

{table(summary['legacy_label_suggestion_counts'], 'legacy_suggestion')}

## Bad Subtypes

{table(summary['bad_subtype_counts'], 'bad_subtype')}

## Phase Mean Risk

```json
{json.dumps(summary['phase_mean_risk'], indent=2, sort_keys=True)}
```

## Decision

The continuous labels should replace old terminal-outcome labels for training targets. Terminal success/failure remains audit metadata only.
"""
    (out_dir / "STAGE9_LABELING_METHOD_COMPARISON.md").write_text(report)
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), "num_samples": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
