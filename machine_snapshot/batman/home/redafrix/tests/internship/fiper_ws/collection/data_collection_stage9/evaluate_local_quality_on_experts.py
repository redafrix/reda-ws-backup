from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .local_chunk_quality import score_state_group, state_id


def load_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expert-jsonl", required=True, help="Expert chunk JSONL in Stage 9 sample-like schema")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--max-samples", type=int, default=None)
    args = parser.parse_args()

    rows = []
    for row in load_jsonl(Path(args.expert_jsonl)):
        row.setdefault("metadata", {})
        row["metadata"].setdefault("state_id", row.get("state_id") or row.get("sample_id"))
        rows.append(row)
        if args.max_samples and len(rows) >= args.max_samples:
            break

    groups = defaultdict(list)
    for row in rows:
        groups[state_id(row)].append(row)

    scored = []
    for group in groups.values():
        scored.extend(score_state_group(group))

    scores = [float(r["risk_score"]) for r in scored]
    false_bad = [r for r in scored if float(r["risk_score"]) >= 0.75 and float(r["risk_confidence"]) >= 0.55]
    summary = {
        "num_expert_chunks": len(scored),
        "mean_risk": sum(scores) / len(scores) if scores else None,
        "max_risk": max(scores) if scores else None,
        "risk_bin_counts": dict(Counter(r["risk_bin"] for r in scored)),
        "expert_false_high_risk_count": len(false_bad),
        "expert_false_high_risk_rate": len(false_bad) / len(scored) if scored else None,
        "gate_expert_false_high_risk_rate_lte_1_percent": (len(false_bad) / len(scored) <= 0.01) if scored else False,
    }

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "expert_continuous_risk_summary.json", summary)
    write_json(out_dir / "expert_false_high_risk_examples.json", false_bad[:50])
    report = f"""# Expert LIBERO Continuous Risk Calibration

- Expert chunks scored: `{summary['num_expert_chunks']}`
- Mean risk: `{summary['mean_risk']}`
- Max risk: `{summary['max_risk']}`
- False high-risk expert chunks: `{summary['expert_false_high_risk_count']}`
- False high-risk expert rate: `{summary['expert_false_high_risk_rate']}`
- Gate `expert_false_high_risk_rate <= 1%`: `{summary['gate_expert_false_high_risk_rate_lte_1_percent']}`

Expert chunks should mostly sit in the low-risk region. If this gate fails, tune the dense local risk formula before using the labels for training.
"""
    (out_dir / "STAGE9_EXPERT_CONTINUOUS_RISK_CALIBRATION.md").write_text(report)
    print(json.dumps({"status": "ok", **summary}, indent=2))


if __name__ == "__main__":
    main()
