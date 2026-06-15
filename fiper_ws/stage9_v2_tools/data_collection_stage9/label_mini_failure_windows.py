from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from .detect_mini_failures import label_steps_and_chunks, risk_bin
    from .mini_failure_features import append_jsonl, compute_features, iter_episode_dirs, load_episode, load_jsonl, write_json
except ImportError:  # pragma: no cover - supports direct script execution
    from detect_mini_failures import label_steps_and_chunks, risk_bin  # type: ignore
    from mini_failure_features import append_jsonl, compute_features, iter_episode_dirs, load_episode, load_jsonl, write_json  # type: ignore


WINDOW_LABEL_SCHEMA_VERSION = "stage9_mini_failure_window_relabel_v1"


def episode_id_from_path_or_meta(episode: dict[str, Any]) -> str:
    meta = episode.get("metadata") or {}
    summary = episode.get("summary") or {}
    return str(meta.get("episode_id") or summary.get("episode_id") or Path(str(episode.get("episode_dir"))).name)


def group_events(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        grouped.setdefault(str(event.get("episode_id")), []).append(event)
    return grouped


def summarize(labels: list[dict[str, Any]], chunks: list[dict[str, Any]]) -> dict[str, Any]:
    step_bins: dict[str, int] = {}
    chunk_bins: dict[str, int] = {}
    event_types: dict[str, int] = {}
    for row in labels:
        step_bins[str(row.get("risk_bin"))] = step_bins.get(str(row.get("risk_bin")), 0) + 1
        for event in row.get("events") or []:
            event_types[str(event.get("event_type"))] = event_types.get(str(event.get("event_type")), 0) + 1
    for row in chunks:
        chunk_bins[str(row.get("risk_bin"))] = chunk_bins.get(str(row.get("risk_bin")), 0) + 1
    return {
        "schema_version": WINDOW_LABEL_SCHEMA_VERSION,
        "step_labels": len(labels),
        "chunk_labels": len(chunks),
        "step_risk_bins": step_bins,
        "chunk_risk_bins": chunk_bins,
        "event_type_step_assignments": event_types,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    raw_root = Path(args.raw_root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    events = load_jsonl(Path(args.events_jsonl))
    by_episode = group_events(events)

    for name in ["mini_failure_step_labels.jsonl", "mini_failure_chunk_labels.jsonl"]:
        path = out_dir / name
        if path.exists():
            path.unlink()

    all_steps: list[dict[str, Any]] = []
    all_chunks: list[dict[str, Any]] = []
    missing_event_episodes = set(by_episode)
    for episode_dir in iter_episode_dirs(raw_root):
        episode = load_episode(episode_dir)
        episode_id = episode_id_from_path_or_meta(episode)
        features = compute_features(episode)
        episode_events = by_episode.get(episode_id, [])
        missing_event_episodes.discard(episode_id)
        step_labels, chunk_labels = label_steps_and_chunks(episode, features, episode_events, args)
        append_jsonl(out_dir / "mini_failure_step_labels.jsonl", step_labels)
        append_jsonl(out_dir / "mini_failure_chunk_labels.jsonl", chunk_labels)
        all_steps.extend(step_labels)
        all_chunks.extend(chunk_labels)

    summary = summarize(all_steps, all_chunks)
    summary.update({
        "raw_root": str(raw_root),
        "events_jsonl": str(args.events_jsonl),
        "out_dir": str(out_dir),
        "events": len(events),
        "episodes_with_events_not_found": sorted(missing_event_episodes),
    })
    write_json(out_dir / "mini_failure_window_label_summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", required=True)
    parser.add_argument("--events-jsonl", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--chunk-size", type=int, default=10)
    parser.add_argument("--pre-failure-steps", type=int, default=60)
    parser.add_argument("--core-label-steps", type=int, default=10)
    args = parser.parse_args()
    # These attributes are consumed by label_steps_and_chunks but are not used
    # for event detection in this relabel-only script.
    args.event_window = 10
    print(json.dumps(run(args), indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
