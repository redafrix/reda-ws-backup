#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from phase2_tdqc.dataset import build_dataset_from_jsonl, save_tdqc_dataset
from phase2_tdqc.features import DEFAULT_TRACE_FEATURE_KEYS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Convert SimVLA uncertainty JSONL to TDQC dataset")
    parser.add_argument("--input_jsonl", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--feature_keys", type=str, nargs="*", default=list(DEFAULT_TRACE_FEATURE_KEYS))
    parser.add_argument(
        "--feature_mode",
        choices=("summary", "summary_denoise", "raw", "raw_plus_summary", "compact8"),
        default="summary",
        help="Use scalar summaries, summary+denoise scalars, raw per-action variance vectors, or both.",
    )
    parser.add_argument(
        "--raw_action_dim",
        type=int,
        default=7,
        help="Action variance dimension for --feature_mode raw/raw_plus_summary.",
    )
    parser.add_argument("--no_log1p", action="store_true", help="Disable log1p transform on uncertainty features")
    parser.add_argument("--min_steps", type=int, default=2)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dataset = build_dataset_from_jsonl(
        args.input_jsonl,
        feature_keys=args.feature_keys,
        log1p=not args.no_log1p,
        min_steps=args.min_steps,
        feature_mode=args.feature_mode,
        raw_action_dim=args.raw_action_dim,
    )
    save_tdqc_dataset(dataset, args.output_path)

    episodes = dataset["episodes"]
    n_success = sum(int(ep["success"]) for ep in episodes)
    n_fail = len(episodes) - n_success
    lengths = [len(ep["features"]) for ep in episodes]
    print(f"Saved TDQC dataset: {args.output_path}")
    print(f"  episodes: {len(episodes)}")
    print(f"  success/fail: {n_success}/{n_fail}")
    print(f"  length min/mean/max: {min(lengths)}/{sum(lengths)/len(lengths):.1f}/{max(lengths)}")
    print(f"  feature_keys: {dataset['feature_keys']}")
    print(f"  feature_mode: {dataset['feature_mode']}")
    print(f"  skipped episodes: {dataset['skipped_episodes']}")


if __name__ == "__main__":
    main()
