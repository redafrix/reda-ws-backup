#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _policy_dirs(root: Path) -> list[Path]:
    return sorted(path for path in root.iterdir() if path.is_dir())


def summarize(root: Path) -> pd.DataFrame:
    records: list[dict[str, Any]] = []
    for policy_dir in _policy_dirs(root):
        rows = _read_jsonl(policy_dir / "episode_summaries.jsonl")
        if not rows:
            continue
        frame = pd.DataFrame(rows)
        records.append(
            {
                "policy": policy_dir.name,
                "episodes": len(frame),
                "successes": int(frame["success"].astype(bool).sum()),
                "success_rate": float(frame["success"].astype(bool).mean()),
                "errors": int(frame["outcome"].eq("error").sum()),
                "mean_steps": float(frame["num_steps"].mean()),
                "mean_queries": float(frame["num_queries"].mean()) if "num_queries" in frame else None,
                "fallback_calls": int(frame.get("fallback_calls", pd.Series(dtype=float)).fillna(0).sum()),
                "wm_accepted": int(frame.get("wm_accepted", pd.Series(dtype=float)).fillna(0).sum()),
                "wm_rejected": int(frame.get("wm_rejected", pd.Series(dtype=float)).fillna(0).sum()),
                "mean_selected_risk": float(frame["selected_risk_mean"].dropna().mean())
                if "selected_risk_mean" in frame
                else None,
                "mean_world_model_risk": float(frame["world_model_risk_mean"].dropna().mean())
                if "world_model_risk_mean" in frame and frame["world_model_risk_mean"].notna().any()
                else None,
            }
        )
    return pd.DataFrame(records)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Summarize SimVLA/world-model arbiter campaign outputs.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("results/simvla_world_model_arbiter/pro_goal_heldout400_20260608"),
    )
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = summarize(args.root)
    if summary.empty:
        raise SystemExit(f"No completed arbiter episodes found under {args.root}")
    output = args.output or (args.root / "summary_by_policy.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(output, index=False)
    print(summary.to_string(index=False))
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
