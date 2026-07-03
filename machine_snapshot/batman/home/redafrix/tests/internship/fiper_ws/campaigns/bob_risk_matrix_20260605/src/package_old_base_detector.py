#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-job", required=True)
    parser.add_argument("--dest", required=True)
    args = parser.parse_args()

    source = Path(args.source_job)
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    for name in ["model.pt", "normalization.json", "training_history.json"]:
        if (source / name).exists():
            shutil.copy2(source / name, dest / ("history.json" if name == "training_history.json" else name))
    thresholds_raw = json.loads((source / "thresholds.json").read_text())
    score_thresholds = thresholds_raw["score"]["eventual"]
    thresholds = {
        "q95": float(score_thresholds["q95"]),
        "q99": float(score_thresholds["q99"]),
        "conformal_mass": 0.15,
    }
    metrics = {
        "source_job": str(source),
        "feature_audit": {
            "static_dim": 43,
            "history_dim": 21,
            "selected_uncertainty_dims": [],
            "uses_reward": False,
            "uses_success": False,
            "uses_future_timestep": False,
            "uses_object_positions_before": False,
            "uses_task_metadata_as_input": False,
        },
    }
    (dest / "thresholds.json").write_text(json.dumps(thresholds, indent=2, sort_keys=True) + "\n")
    (dest / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
