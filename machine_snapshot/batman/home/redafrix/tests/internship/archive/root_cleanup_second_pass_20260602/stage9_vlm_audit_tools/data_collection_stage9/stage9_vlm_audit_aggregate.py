from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_jsonl(path: Path):
    if not path.exists():
        return
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def parsed(row: dict[str, Any]) -> dict[str, Any]:
    return ((row.get("result") or {}).get("parsed") or {})


def is_suspicious(row: dict[str, Any]) -> bool:
    p = parsed(row)
    if row.get("status") != "ok":
        return True
    if p.get("parse_error"):
        return True
    if p.get("suspicious_label") is True:
        return True
    our = row.get("our_label")
    behavior = p.get("behavior")
    action = p.get("suggested_label_action")
    if our == "VALIDATED_BAD" and behavior in {"good", "unclear"}:
        return True
    if our == "GOOD_STRONG" and behavior == "bad":
        return True
    if action in {"downgrade_to_ambiguous", "upgrade_to_review", "manual_review"}:
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()

    rows: list[dict[str, Any]] = []
    for inp in args.inputs:
        rows.extend(list(load_jsonl(Path(inp)) or []))

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    by_model = Counter(r.get("vlm_model") for r in rows)
    by_status = Counter(r.get("status") for r in rows)
    by_category = Counter(r.get("category") for r in rows)
    behavior_by_label = defaultdict(Counter)
    action_by_label = defaultdict(Counter)
    failure_types = Counter()
    suspicious = []
    for row in rows:
        p = parsed(row)
        behavior_by_label[row.get("our_label")][p.get("behavior", "missing")] += 1
        action_by_label[row.get("our_label")][p.get("suggested_label_action", "missing")] += 1
        failure_types[p.get("failure_type", "missing")] += 1
        if is_suspicious(row):
            suspicious.append(row)

    suspicious.sort(key=lambda r: (
        0 if r.get("our_label") == "VALIDATED_BAD" else 1,
        r.get("category") or "",
        r.get("sample_id") or "",
    ))

    summary = {
        "num_results": len(rows),
        "by_model": dict(by_model),
        "by_status": dict(by_status),
        "by_category": dict(by_category),
        "behavior_by_label": {k: dict(v) for k, v in behavior_by_label.items()},
        "suggested_action_by_label": {k: dict(v) for k, v in action_by_label.items()},
        "failure_types": dict(failure_types),
        "suspicious_count": len(suspicious),
        "suspicious_by_label": dict(Counter(r.get("our_label") for r in suspicious)),
        "suspicious_by_category": dict(Counter(r.get("category") for r in suspicious)),
    }
    (out_dir / "vlm_audit_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    with (out_dir / "vlm_suspicious_labels.jsonl").open("w") as f:
        for row in suspicious:
            f.write(json.dumps(row, default=str) + "\n")

    md = [
        "# Stage 9 VLM Label Audit Report",
        "",
        "This audit uses VLM output only as a disagreement detector. It does not replace simulator metrics or same-state counterfactual evidence.",
        "",
        "## Summary",
        "",
        f"- Results: `{len(rows)}`",
        f"- Suspicious labels: `{len(suspicious)}`",
        f"- Status counts: `{dict(by_status)}`",
        f"- Model counts: `{dict(by_model)}`",
        f"- Category counts: `{dict(by_category)}`",
        "",
        "## Behavior By Current Label",
        "",
    ]
    for label, counts in sorted(behavior_by_label.items()):
        md.append(f"- `{label}`: `{dict(counts)}`")
    md += ["", "## Suggested Action By Current Label", ""]
    for label, counts in sorted(action_by_label.items()):
        md.append(f"- `{label}`: `{dict(counts)}`")
    md += ["", "## Suspicious By Category", ""]
    for cat, count in sorted(Counter(r.get("category") for r in suspicious).items()):
        md.append(f"- `{cat}`: `{count}`")
    md += ["", "## Top Suspicious Examples", ""]
    for row in suspicious[:30]:
        p = parsed(row)
        md.append(
            f"- `{row.get('sample_id')}` `{row.get('category')}` label=`{row.get('our_label')}` "
            f"behavior=`{p.get('behavior')}` action=`{p.get('suggested_label_action')}` "
            f"failure=`{p.get('failure_type')}` conf=`{p.get('confidence')}` sheet=`{row.get('contact_sheet_path')}`"
        )
    md += [
        "",
        "## Decision",
        "",
        "Any sample flagged here should be rechecked with simulator metrics and, if possible, replay video. VLM disagreement alone should downgrade to review, not create a final GOOD or BAD label.",
    ]
    (out_dir / "STAGE9_VLM_LABEL_AUDIT_REPORT.md").write_text("\n".join(md) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

