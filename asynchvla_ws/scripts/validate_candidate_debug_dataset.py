#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
DATA = REDA_WS / "asynchvla_ws/data/debug/candidate_debug.pt"
REPORT = REDA_WS / "asynchvla_ws/outputs/reports/candidate_debug_dataset_report.md"


def stats(xs):
    t = torch.tensor(xs, dtype=torch.float32)
    return float(t.min()), float(t.mean()), float(t.max())


def main() -> int:
    payload = torch.load(DATA, map_location="cpu")
    rows = payload["candidates"]
    by_type = defaultdict(list)
    by_ctx = defaultdict(list)
    for r in rows:
        by_type[r["candidate_type"]].append(r)
        by_ctx[r["context_id"]].append(r)
    type_lines = []
    for typ in sorted(by_type):
        vals = [r["true_chunk_l2_error"] for r in by_type[typ]]
        mn, mean, mx = stats(vals)
        type_lines.append(f"- `{typ}`: count=`{len(vals)}`, min=`{mn:.6f}`, mean=`{mean:.6f}`, max=`{mx:.6f}`")
    example_ctx = next(k for k, v in by_ctx.items() if len(v) >= 6)
    example_rows = by_ctx[example_ctx]
    pooled_equal = all(torch.equal(example_rows[0]["pooled_vlm_features"], r["pooled_vlm_features"]) for r in example_rows[1:])
    proprio_equal = all(torch.equal(example_rows[0]["proprio"], r["proprio"]) for r in example_rows[1:])
    expert_equal = all(torch.equal(example_rows[0]["target_expert_action_normalized"], r["target_expert_action_normalized"]) for r in example_rows[1:])
    example_lines = [
        f"- context_id: `{example_ctx}`",
        f"- candidate types: `{[r['candidate_type'] for r in example_rows]}`",
        f"- true errors: `{[(r['candidate_type'], round(r['true_chunk_l2_error'], 6)) for r in example_rows]}`",
        f"- pooled VLM identical across candidates: `{pooled_equal}`",
        f"- proprio identical across candidates: `{proprio_equal}`",
        f"- target expert action identical across candidates: `{expert_equal}`",
    ]
    lines = [
        "# Candidate Debug Dataset Report",
        "",
        f"- Dataset: `{DATA}`",
        f"- File size bytes: `{DATA.stat().st_size}`",
        f"- Number of contexts: `{len(by_ctx)}`",
        f"- Number of candidates: `{len(rows)}`",
        f"- Schema: `{payload.get('schema_version')}`",
        "",
        "## Candidate Types",
        "",
        *type_lines,
        "",
        "## Same-Context Proof",
        "",
        *example_lines,
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")
    print("candidate_debug_validation: OK")
    print("contexts", len(by_ctx))
    print("candidates", len(rows))
    for line in type_lines:
        print(line)
    print("same_context_proof", example_lines)
    print("report", REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
