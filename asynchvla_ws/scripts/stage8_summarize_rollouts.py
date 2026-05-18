#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean


def numeric(xs):
    return [x for x in xs if isinstance(x, (int, float))]


def summarize_file(path: Path):
    data = json.loads(path.read_text())
    rows = []
    for ep in data.get("episodes", []):
        trace = ep.get("trace", [])
        unc = []
        rejects = 0
        replan = 0
        rewards = []
        for item in trace:
            if "chosen_seed_unc" in item:
                unc.append(item["chosen_seed_unc"])
            if "seed0_uncertainty" in item:
                unc.append(item["seed0_uncertainty"])
            if item.get("seed0_rejected_by_threshold") is True:
                rejects += 1
            if item.get("kind") == "replan":
                replan += 1
            if "reward" in item:
                rewards.append(item["reward"])
        rows.append(
            {
                "path": str(path),
                "suite": data.get("task_suite", ""),
                "task_id": data.get("task_id", ""),
                "language": data.get("task_language", ""),
                "mode": ep.get("mode", ""),
                "success": bool(ep.get("success", False)),
                "steps": ep.get("steps", None),
                "walltime_sec": ep.get("walltime_sec", None),
                "unc_mean": mean(numeric(unc)) if numeric(unc) else None,
                "unc_max": max(numeric(unc)) if numeric(unc) else None,
                "replan_count": replan,
                "reject_count": rejects,
                "reward_sum": sum(numeric(rewards)) if numeric(rewards) else 0.0,
                "nonzero_rewards": sum(1 for r in numeric(rewards) if abs(r) > 1e-9),
            }
        )
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--glob", default="*.json")
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--title", default="Stage 8 Rollout Summary")
    args = ap.parse_args()

    in_dir = Path(args.input_dir)
    paths = sorted(in_dir.glob(args.glob))
    rows = []
    for p in paths:
        try:
            rows.extend(summarize_file(p))
        except Exception as exc:
            rows.append({"path": str(p), "error": repr(exc)})

    grouped = defaultdict(list)
    for r in rows:
        grouped[(r.get("suite", ""), r.get("task_id", ""), r.get("mode", ""))].append(r)

    lines = [f"# {args.title}", "", f"- Input dir: `{in_dir}`", f"- Files: `{len(paths)}`", f"- Episodes: `{sum(1 for r in rows if 'error' not in r)}`", ""]
    if any("error" in r for r in rows):
        lines += ["## Parse Errors", ""]
        for r in rows:
            if "error" in r:
                lines.append(f"- `{r['path']}`: `{r['error']}`")
        lines.append("")

    lines += ["## Aggregate By Suite/Task/Mode", "", "| suite | task | mode | episodes | success_rate | avg_steps | avg_unc | max_unc | avg_rejects | reward_sum |", "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for (suite, task_id, mode), rs in sorted(grouped.items()):
        valid = [r for r in rs if "error" not in r]
        if not valid:
            continue
        success_rate = mean([1.0 if r["success"] else 0.0 for r in valid])
        steps = numeric([r["steps"] for r in valid])
        unc_mean = numeric([r["unc_mean"] for r in valid])
        unc_max = numeric([r["unc_max"] for r in valid])
        rejects = numeric([r["reject_count"] for r in valid])
        reward = numeric([r["reward_sum"] for r in valid])
        lines.append(
            f"| {suite} | {task_id} | {mode} | {len(valid)} | {success_rate:.3f} | "
            f"{(mean(steps) if steps else float('nan')):.2f} | {(mean(unc_mean) if unc_mean else float('nan')):.3f} | "
            f"{(max(unc_max) if unc_max else float('nan')):.3f} | {(mean(rejects) if rejects else 0.0):.2f} | "
            f"{(sum(reward) if reward else 0.0):.3f} |"
        )

    lines += ["", "## Episode Rows", "", "| file | suite | task | mode | success | steps | unc_mean | unc_max | rejects |", "|---|---|---:|---|---:|---:|---:|---:|---:|"]
    for r in rows:
        if "error" in r:
            continue
        lines.append(
            f"| `{Path(r['path']).name}` | {r['suite']} | {r['task_id']} | {r['mode']} | "
            f"{int(r['success'])} | {r['steps']} | {r['unc_mean'] if r['unc_mean'] is not None else 'NA'} | "
            f"{r['unc_max'] if r['unc_max'] is not None else 'NA'} | {r['reject_count']} |"
        )

    out = Path(args.out_md)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print(out)


if __name__ == "__main__":
    main()
