#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter

SRC = Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_20260625")
DST = Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_no_task9_20260625")
EXCLUDED_TASKS = {9}


def read_jsonl(path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
            n += 1
    return n


def main():
    DST.mkdir(parents=True, exist_ok=True)
    summaries = [r for r in read_jsonl(SRC / "episode_summaries.jsonl") if int(r["task_id"]) not in EXCLUDED_TASKS]
    keep_ids = {r["episode_id"] for r in summaries}
    n_summ = write_jsonl(DST / "episode_summaries.jsonl", summaries)
    n_rows = 0
    with (DST / "episode_rows.jsonl").open("w") as out:
        for row in read_jsonl(SRC / "episode_rows.jsonl"):
            if row.get("episode_id") in keep_ids:
                out.write(json.dumps(row) + "\n")
                n_rows += 1
                if n_rows % 100000 == 0:
                    print(f"wrote {n_rows} rows", flush=True)

    by_task = Counter(r["task_id"] for r in summaries)
    succ_by_task = Counter(r["task_id"] for r in summaries if r["success"])
    fail_by_task = Counter(r["task_id"] for r in summaries if not r["success"])
    report_lines = [
        "# Pi0.5 Goal-Object H10 Frozen Dataset Without Task 9",
        "",
        "Task 9 (`put the wine bottle on the rack`) is excluded because audit on 2026-06-25 found the rack target invalid/non-visible for Pi0.5 collection: all 409 episodes timed out and visual review showed no usable rack target.",
        "",
        f"- Source: `{SRC}`",
        f"- Destination: `{DST}`",
        f"- Excluded tasks: `{sorted(EXCLUDED_TASKS)}`",
        f"- Episodes kept: `{n_summ}`",
        f"- Rows kept: `{n_rows}`",
        f"- Successes: `{sum(1 for r in summaries if r['success'])}`",
        f"- Failures: `{sum(1 for r in summaries if not r['success'])}`",
        "",
        "| Task | Episodes | Success | Failure | Success Rate |",
        "|---:|---:|---:|---:|---:|",
    ]
    for task in sorted(by_task):
        n = by_task[task]
        s = succ_by_task[task]
        f = fail_by_task[task]
        report_lines.append(f"| {task} | {n} | {s} | {f} | {100*s/n:.2f}% |")

    (DST / "DATASET_FREEZE_REPORT_NO_TASK9_20260625.md").write_text("\n".join(report_lines) + "\n")
    manifest = {
        "schema_version": "pi05_libero_goal_object_frozen_no_task9_v1",
        "source": str(SRC),
        "excluded_tasks": sorted(EXCLUDED_TASKS),
        "num_episodes": n_summ,
        "num_rows": n_rows,
        "success_episodes": sum(1 for r in summaries if r["success"]),
        "failure_episodes": sum(1 for r in summaries if not r["success"]),
        "task_counts": {str(k): by_task[k] for k in sorted(by_task)},
    }
    (DST / "dataset_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
