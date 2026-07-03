#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
DATA = REDA_WS / "asynchvla_ws/data/debug/trace_debug.pt"
REPORT = REDA_WS / "asynchvla_ws/outputs/reports/trace_debug_dataset_report.md"


def tensor_info(x):
    return {"shape": list(x.shape), "dtype": str(x.dtype)} if torch.is_tensor(x) else type(x).__name__


def finite_ok(x):
    return bool(torch.isfinite(x).all()) if torch.is_tensor(x) and x.is_floating_point() else True


def main() -> int:
    payload = torch.load(DATA, map_location="cpu")
    samples = payload["samples"]
    errors = torch.tensor([s["chunk_l2_error_normalized"] for s in samples], dtype=torch.float32)
    keys = list(samples[0].keys()) if samples else []
    shape_lines = []
    for k in keys:
        shape_lines.append(f"- `{k}`: `{tensor_info(samples[0][k])}`")
    nan_lines = []
    for k in keys:
        vals = [s[k] for s in samples if torch.is_tensor(s[k])]
        if vals:
            ok = all(finite_ok(v) for v in vals)
            nan_lines.append(f"- `{k}` finite: `{ok}`")
    task_counts = {}
    for s in samples:
        task_counts[s["task_name"]] = task_counts.get(s["task_name"], 0) + 1
    examples = []
    for s in samples[:8]:
        examples.append(f"- `{s['sample_id']}` task=`{s['task_name']}` instruction=`{s['language_instruction']}` source_index=`{s['source_local_index']}`")
    lines = [
        "# Trace Debug Dataset Report",
        "",
        f"- Dataset: `{DATA}`",
        f"- File size bytes: `{DATA.stat().st_size}`",
        f"- Number of samples: `{len(samples)}`",
        f"- Schema: `{payload.get('schema_version')}`",
        f"- Checkpoint: `{payload.get('checkpoint')}`",
        "",
        "## Keys And First-Sample Shapes",
        "",
        *shape_lines,
        "",
        "## NaN/Inf Checks",
        "",
        *nan_lines,
        "",
        "## Error Stats",
        "",
        f"- chunk L2 min: `{float(errors.min())}`",
        f"- chunk L2 mean: `{float(errors.mean())}`",
        f"- chunk L2 max: `{float(errors.max())}`",
        "",
        "## Task Counts",
        "",
        *[f"- `{k}`: `{v}`" for k, v in sorted(task_counts.items())],
        "",
        "## Examples",
        "",
        *examples,
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")
    print("trace_debug_validation: OK")
    print("num_samples", len(samples))
    print("keys", keys)
    print("file_size", DATA.stat().st_size)
    print("chunk_l2_min_mean_max", float(errors.min()), float(errors.mean()), float(errors.max()))
    print("tasks", task_counts)
    print("report", REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
