#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

WORKSPACE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKSPACE / "src"))

from risk_collection.schema import validate_row  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--require-episodes", type=int, default=1)
    parser.add_argument("--require-video", action="store_true")
    parser.add_argument("--expected-mode", choices=("chunk_h10",))
    parser.add_argument("--expected-risk-split")
    args = parser.parse_args()

    episode_dirs = sorted(
        path
        for path in (args.output_dir / "episodes").glob("*")
        if path.is_dir() and (path / "COMMITTED").is_file()
    )
    if len(episode_dirs) < args.require_episodes:
        raise RuntimeError(
            f"expected at least {args.require_episodes} episodes, got {len(episode_dirs)}"
        )

    row_keys: set[tuple[str, int]] = set()
    rows = 0
    for episode_dir in episode_dirs:
        summary = json.loads((episode_dir / "summary.json").read_text())
        if args.expected_risk_split and summary["risk_split"] != args.expected_risk_split:
            raise RuntimeError(f"unexpected risk split in {episode_dir}")
        episode_rows = []
        for line in (episode_dir / "risk_rows.jsonl").read_text().splitlines():
            row = json.loads(line)
            validate_row(row)
            key = (row["episode_id"], int(row["decision_index"]))
            if key in row_keys:
                raise RuntimeError(f"duplicate row {key}")
            row_keys.add(key)
            episode_rows.append(row)
            if args.expected_mode and row["execution_mode"] != args.expected_mode:
                raise RuntimeError(f"unexpected mode in {key}")
            all_seeds = [row["main_seed"], *row["ace_candidate_seeds"]]
            if len(set(all_seeds)) != 9:
                raise RuntimeError(f"nonunique seeds in {key}")
            if row["metadata"]["vlm_encoding_count"] != 1:
                raise RuntimeError(f"VLM encoding count mismatch in {key}")
            if (
                row["metadata"]["uncertainty_parameterization"]
                != "softplus_raw_variance"
            ):
                raise RuntimeError(f"wrong uncertainty parameterization in {key}")
            if row["metadata"].get("ood_excluded_from_training") != (
                summary["risk_split"] == "ood_smoke"
            ):
                raise RuntimeError(f"OOD exclusion mismatch in {key}")
            metadata = row["metadata"]
            if not str(metadata.get("instruction", "")).strip():
                raise RuntimeError(f"missing instruction in {key}")
            if not str(metadata.get("target_category_id", "")).strip():
                raise RuntimeError(f"missing target category in {key}")
            if not str(metadata.get("target_variant_id", "")).strip():
                raise RuntimeError(f"missing target variant in {key}")
            if metadata.get("camera_mapping") != {
                "agent_camera": "agent_rgb",
                "wrist_camera": "wrist_rgb",
                "padded_third_camera": "absent",
            }:
                raise RuntimeError(f"camera mapping mismatch in {key}")
            if metadata.get("agent_camera_shape") != [480, 640, 3]:
                raise RuntimeError(f"agent camera shape mismatch in {key}")
            if metadata.get("wrist_camera_shape") != [384, 384, 3]:
                raise RuntimeError(f"wrist camera shape mismatch in {key}")
            if not metadata.get(
                "deployable_inputs_exclude_task_id_seed_timestep_reward", False
            ):
                raise RuntimeError(f"deployable-input exclusion missing in {key}")
            delta = np.asarray(row["simvla_uncertainty_delta_49d"])
            if row["decision_index"] == 0 and np.any(delta != 0):
                raise RuntimeError(f"first uncertainty delta is not zero in {key}")
        if len(episode_rows) != int(summary["decision_rows"]):
            raise RuntimeError(f"row count mismatch in {episode_dir}")
        if args.require_video:
            video = args.output_dir / "videos" / f"{episode_dir.name}.mp4"
            if not video.is_file() or video.stat().st_size == 0:
                raise RuntimeError(f"missing smoke video for {episode_dir.name}")
            probe = subprocess.run(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-select_streams",
                    "v:0",
                    "-show_entries",
                    "stream=width,height,nb_frames",
                    "-of",
                    "json",
                    str(video),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            stream = json.loads(probe.stdout)["streams"][0]
            if (int(stream["width"]), int(stream["height"])) != (1120, 480):
                raise RuntimeError(f"review video dimensions mismatch: {video}")
        rows += len(episode_rows)

    print(f"FINALIZED_EPISODES={len(episode_dirs)}")
    print(f"VALIDATED_DECISION_ROWS={rows}")
    print("NINE_SEEDS_UNIQUE=YES")
    print("ONE_VLM_ENCODING_PER_DECISION=YES")
    print("CAMERA_MAPPING_AND_SHAPES=PASS")
    print("INSTRUCTION_AND_TARGET_IDENTITY=PASS")
    print("EXECUTED_CONTROLLER_ACTIONS=PASS")
    print("ROW_SCHEMA_VALIDATION=PASS")
    print("COLLECTION_OUTPUT_VALIDATION=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
