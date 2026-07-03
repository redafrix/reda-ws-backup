from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def episode_key(row: dict[str, Any]) -> str:
    sid = str(row.get("state_id") or "")
    if "_s" in sid:
        return sid.split("_s", 1)[0]
    return str(row.get("task_name") or "unknown")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--continuous-labels", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--risk-threshold", type=float, default=0.75)
    args = parser.parse_args()

    rows = list(load_jsonl(Path(args.continuous_labels)))
    by_episode = defaultdict(list)
    for row in rows:
        by_episode[episode_key(row)].append(row)

    windows: list[dict[str, Any]] = []
    for ep, ep_rows in by_episode.items():
        ep_rows.sort(key=lambda r: int(r.get("distance_to_failure_or_timeout") or 10**9), reverse=True)
        risky = [
            r for r in ep_rows
            if float(r.get("risk_score", 0.5)) >= args.risk_threshold and r.get("negative_evidence")
        ]
        if not risky:
            continue
        first = risky[0]
        windows.append({
            "episode_key": ep,
            "candidate_sample_id": first.get("sample_id"),
            "state_id": first.get("state_id"),
            "task_name": first.get("task_name"),
            "phase": first.get("phase"),
            "seed": first.get("seed"),
            "risk_score": first.get("risk_score"),
            "risk_confidence": first.get("risk_confidence"),
            "negative_evidence": first.get("negative_evidence"),
            "distance_to_failure_or_timeout": first.get("distance_to_failure_or_timeout"),
            "mined_window_type": "scripted_risk_peak",
        })

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(out_dir / "scripted_failure_windows.jsonl", windows)
    summary = {
        "num_input_samples": len(rows),
        "num_episode_keys": len(by_episode),
        "num_scripted_failure_windows": len(windows),
        "risk_threshold": args.risk_threshold,
    }
    write_json(out_dir / "scripted_failure_windows_summary.json", summary)
    report = f"""# Stage 9 Scripted Failure Window Mining

- Input samples: `{summary['num_input_samples']}`
- Episode keys: `{summary['num_episode_keys']}`
- Scripted windows found: `{summary['num_scripted_failure_windows']}`
- Risk threshold: `{summary['risk_threshold']}`

This miner does not create labels by itself. It proposes windows that should be replayed or reviewed.
"""
    (out_dir / "STAGE9_SCRIPTED_FAILURE_WINDOW_MINING.md").write_text(report)
    print(json.dumps({"status": "ok", **summary}, indent=2))


if __name__ == "__main__":
    main()
