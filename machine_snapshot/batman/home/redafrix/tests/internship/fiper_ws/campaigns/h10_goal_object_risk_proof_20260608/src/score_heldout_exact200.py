#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import torch

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from train_frozen_detectors_h10_proof import (  # noqa: E402
    SeqRiskModel,
    build_rows_for_split,
    load_episode_meta,
    score_rows,
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def stats_to_numpy(stats: dict[str, Any]) -> dict[str, dict[str, np.ndarray]]:
    return {
        key: {inner_key: np.asarray(inner_value, dtype=np.float32) for inner_key, inner_value in value.items()}
        for key, value in stats.items()
    }


def episode_alarm_summary(scores: np.ndarray, ids: list[str], timesteps: np.ndarray, episodes: dict[str, Any], thresholds: dict[str, float]) -> dict[str, Any]:
    by_episode: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for eid, t, score in zip(ids, timesteps, scores):
        by_episode[str(eid)].append((int(t), float(score)))

    rows = []
    triggered = 0
    det25 = 0
    det50 = 0
    for eid, vals in sorted(by_episode.items()):
        vals.sort()
        mass = 0.0
        first_alarm = None
        for t, score in vals:
            mass += max(0.0, score - float(thresholds["q95"]))
            if first_alarm is None and mass >= float(thresholds["conformal_mass"]):
                first_alarm = t
        ep = episodes[eid]
        denom = max(1, int(ep.num_steps))
        if first_alarm is not None:
            triggered += 1
            if first_alarm / denom <= 0.25:
                det25 += 1
            if first_alarm / denom <= 0.50:
                det50 += 1
        rows.append(
            {
                "episode_id": eid,
                "task_id": int(ep.task_id),
                "success": bool(ep.success),
                "num_steps": int(ep.num_steps),
                "triggered": first_alarm is not None,
                "first_alarm_timestep": first_alarm,
                "final_mass": mass,
            }
        )
    n = len(rows)
    return {
        "episodes": n,
        "triggered": triggered,
        "alarm_rate": triggered / n if n else None,
        "det_at_25": det25 / n if n else None,
        "det_at_50": det50 / n if n else None,
        "rows": rows,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", required=True)
    p.add_argument("--model-dir", required=True)
    p.add_argument("--variant", choices=["base", "unc_topk8"], required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--default-suite", default="libero_goal_object")
    p.add_argument("--history-steps", type=int, default=16)
    p.add_argument("--cadence", choices=["native", "stride"], default="native")
    p.add_argument("--stride", type=int, default=10)
    p.add_argument("--batch-size", type=int, default=512)
    args = p.parse_args()

    run_root = Path(args.run_root)
    model_dir = Path(args.model_dir)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    episodes = load_episode_meta(run_root, args.default_suite)
    buckets = {
        "heldout_success": {eid for eid, ep in episodes.items() if ep.success},
        "heldout_failure": {eid for eid, ep in episodes.items() if not ep.success},
    }
    rows_by_bucket = build_rows_for_split(run_root, episodes, buckets, args.history_steps, args.cadence, args.stride)
    stats = stats_to_numpy(load_json(model_dir / "normalization.json"))
    thresholds = load_json(model_dir / "thresholds.json")

    state = torch.load(model_dir / "model.pt", map_location="cpu")
    static_dim = len(stats["static"]["mean"])
    model = SeqRiskModel(hist_dim=21, action_dim=7, static_dim=static_dim, width=128, layers=3, heads=4, dropout=0.0)
    model.load_state_dict(state)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    report: dict[str, Any] = {
        "run_root": str(run_root),
        "model_dir": str(model_dir),
        "variant": args.variant,
        "thresholds": thresholds,
        "buckets": {},
        "by_task": {},
    }
    all_episode_rows = []
    for bucket, rows in rows_by_bucket.items():
        scores, labels, ids, timesteps = score_rows(model, stats, rows, args.variant, args.batch_size, device)
        summary = episode_alarm_summary(scores, ids, timesteps, episodes, thresholds)
        report["buckets"][bucket] = {k: v for k, v in summary.items() if k != "rows"}
        all_episode_rows.extend(summary["rows"])

    by_task: dict[str, dict[str, int]] = defaultdict(lambda: {"episodes": 0, "success": 0, "failure": 0, "success_alarm": 0, "failure_alarm": 0})
    for row in all_episode_rows:
        t = str(row["task_id"])
        by_task[t]["episodes"] += 1
        if row["success"]:
            by_task[t]["success"] += 1
            by_task[t]["success_alarm"] += int(row["triggered"])
        else:
            by_task[t]["failure"] += 1
            by_task[t]["failure_alarm"] += int(row["triggered"])
    report["by_task"] = dict(sorted(by_task.items(), key=lambda kv: int(kv[0])))
    report["episodes"] = all_episode_rows
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "episodes"}, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
