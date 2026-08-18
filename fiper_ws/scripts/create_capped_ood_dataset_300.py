#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


def read_jsonl(path: Path):
    with path.open() as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if line:
                yield line_no, json.loads(line)


def write_jsonl(path: Path, rows):
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\n")


def capped_success(summary: dict, cap_steps: int) -> bool:
    return bool(summary.get("success")) and int(summary.get("num_steps", 10**9)) < cap_steps


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, type=Path)
    ap.add_argument("--dst", required=True, type=Path)
    ap.add_argument("--cap-steps", type=int, default=300)
    args = ap.parse_args()

    src = args.src
    dst = args.dst
    cap_steps = int(args.cap_steps)
    if not (src / "episode_summaries.jsonl").exists():
        raise FileNotFoundError(src / "episode_summaries.jsonl")
    if not (src / "fiper_receding_samples.jsonl").exists():
        raise FileNotFoundError(src / "fiper_receding_samples.jsonl")

    dst.mkdir(parents=True, exist_ok=True)

    summaries = {}
    capped_summaries = []
    original_counts = Counter()
    capped_counts = Counter()
    task_counts = Counter()
    converted_success_to_failure = 0
    for _, row in read_jsonl(src / "episode_summaries.jsonl"):
        eid = str(row["episode_id"])
        orig_success = bool(row.get("success"))
        new_success = capped_success(row, cap_steps)
        if orig_success and not new_success:
            converted_success_to_failure += 1
        new = dict(row)
        new["source_episode_id"] = eid
        new["source_num_steps"] = int(row.get("num_steps", 0))
        new["source_success"] = orig_success
        new["cap_steps"] = cap_steps
        new["num_steps"] = min(int(row.get("num_steps", cap_steps)), cap_steps)
        new["success"] = new_success
        new["outcome"] = "success" if new_success else "failure_or_cap300_timeout"
        new["terminal_done"] = bool(new_success)
        new["derived_dataset"] = True
        new["derivation_rule"] = (
            f"Rows with timestep >= {cap_steps} are removed; an episode is successful only if "
            f"the original success occurred before {cap_steps} steps; reaching {cap_steps} is labeled failure."
        )
        new["updated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
        summaries[eid] = new
        capped_summaries.append(new)
        original_counts["success" if orig_success else "failure"] += 1
        capped_counts["success" if new_success else "failure"] += 1
        task_counts[int(row.get("task_id", -1))] += 1

    kept_rows = 0
    dropped_rows = 0
    row_task_counts = Counter()
    rows_per_ep = Counter()
    with (src / "fiper_receding_samples.jsonl").open() as fin, (dst / "fiper_receding_samples.jsonl").open("w") as fout:
        for line_no, line in enumerate(fin, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            timestep = int(row.get("timestep", 0))
            eid = str(row.get("episode_id") or row.get("episode_uid"))
            if timestep >= cap_steps:
                dropped_rows += 1
                continue
            if eid not in summaries:
                dropped_rows += 1
                continue
            label = summaries[eid]
            new_success = bool(label["success"])
            row["source_episode_outcome"] = row.get("episode_outcome")
            row["source_parent_episode_success"] = row.get("parent_episode_success")
            row["episode_outcome"] = "success" if new_success else "failure_or_cap300_timeout"
            row["parent_episode_success"] = new_success
            row["parent_failed_or_timeout"] = not new_success
            row["derived_dataset"] = True
            row["cap_steps"] = cap_steps
            row["allowed_use"] = "eval_only_derived_cap300"
            fout.write(json.dumps(row, sort_keys=True) + "\n")
            kept_rows += 1
            row_task_counts[int(row.get("task_id", -1))] += 1
            rows_per_ep[eid] += 1
            if line_no % 100000 == 0:
                print(f"[rows] line={line_no} kept={kept_rows} dropped={dropped_rows}", flush=True)

    write_jsonl(dst / "episode_summaries.jsonl", capped_summaries)

    for name in ["run_manifest.json", "live_status.json", "PIPELINE_MANIFEST.txt"]:
        src_path = src / name
        if src_path.exists():
            shutil.copy2(src_path, dst / f"source_{name}")

    manifest = {
        "schema_version": "derived_cap300_dataset_v1",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source_dataset": str(src),
        "derived_dataset": str(dst),
        "cap_steps": cap_steps,
        "rule": "keep rows with timestep < cap_steps; label success only when original summary success is true and original num_steps < cap_steps; reaching cap_steps is failure",
        "episodes": len(capped_summaries),
        "original_counts": dict(original_counts),
        "capped_counts": dict(capped_counts),
        "converted_success_to_failure": converted_success_to_failure,
        "kept_rows": kept_rows,
        "dropped_rows": dropped_rows,
        "task_episode_counts": dict(sorted(task_counts.items())),
        "row_task_counts": dict(sorted(row_task_counts.items())),
        "min_rows_per_episode": min(rows_per_ep.values()) if rows_per_ep else 0,
        "max_rows_per_episode": max(rows_per_ep.values()) if rows_per_ep else 0,
    }
    (dst / "DERIVED_CAP300_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    (dst / "README_DERIVED_CAP300.md").write_text(
        "# Derived 300-Step LIBERO Goal-Object-OOD Dataset\n\n"
        f"- Source: `{src}`\n"
        f"- Cap: `{cap_steps}` rows/steps per episode\n"
        "- This is an offline derived dataset, not a fresh rollout collection.\n"
        "- Rows with `timestep >= 300` were removed.\n"
        "- Any episode that did not finish successfully before step 300 is relabeled as failure.\n"
        "- This is intended for threshold/detector audits of the existing H10 TopK8 risk model.\n\n"
        "See `DERIVED_CAP300_MANIFEST.json` for counts.\n"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
