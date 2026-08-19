#!/usr/bin/env python3
"""Build OOD400 Composite Review Videos and Indexes for Baseline and TopK Runs.

Creates:
- ALL400 review MP4 (all 400 episodes concatenated with metadata overlays)
- FAILURES_ONLY review MP4
- Comprehensive Video Index CSV
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import sha256_file


def get_video_duration(path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=duration", "-of", "json", str(path)
    ]
    res = subprocess.check_output(cmd, text=True)
    d = json.loads(res)["streams"][0]
    return float(d.get("duration", 0.0))


def build_review_videos(
    *,
    episodes_summary_path: Path,
    videos_dir: Path,
    output_dir: Path,
    mode: str = "baseline",
    controller_info: dict[str, Any] | None = None,
) -> dict[str, Any]:
    episodes_summary_path = Path(episodes_summary_path).resolve()
    videos_dir = Path(videos_dir).resolve()
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    summaries = [json.loads(line) for line in episodes_summary_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(summaries) != 400:
        raise ValueError(f"Expected 400 episodes, found {len(summaries)}")

    prefix = "OOD400_BASELINE" if mode == "baseline" else "OOD400_TOPK"
    all_video_p = output_dir / f"{prefix}_ALL400_REVIEW.mp4"
    fail_video_p = output_dir / f"{prefix}_FAILURES_ONLY_REVIEW.mp4"
    index_csv_p = output_dir / f"{prefix}_VIDEO_INDEX.csv"

    index_rows: list[dict[str, Any]] = []
    current_time_all = 0.0

    all_concat_list_p = output_dir / f"concat_all.txt"
    fail_concat_list_p = output_dir / f"concat_fail.txt"

    all_lines = []
    fail_lines = []

    print(f"=== Building {mode} review videos for {len(summaries)} episodes ===")

    for s in summaries:
        ep_id = s["episode_id"]
        vid_p = videos_dir / f"{ep_id}.mp4"
        if not vid_p.exists():
            raise FileNotFoundError(f"Missing video for ep {ep_id}: {vid_p}")

        dur = get_video_duration(vid_p)
        succ = s["success"]
        outcome_str = "SUCCESS" if succ else "FAILURE"
        min_dist = float(s["minimum_tcp_distance_m"])
        succ_tick = s.get("first_3cm_crossing_control_tick")

        start_time = current_time_all
        end_time = current_time_all + dur
        current_time_all = end_time

        all_lines.append(f"file '{vid_p}'")
        if not succ:
            fail_lines.append(f"file '{vid_p}'")

        index_rows.append({
            "episode_id": ep_id,
            "instruction": s["instruction"],
            "outcome": outcome_str,
            "scene_fingerprint": s["scene_fingerprint_sha256"],
            "minimum_distance": min_dist,
            "success_tick": succ_tick if succ else "",
            "video_start_seconds": f"{start_time:.3f}",
            "video_end_seconds": f"{end_time:.3f}",
            "duration_seconds": f"{dur:.3f}",
            "source_video_path": str(vid_p),
        })

    # Write concat lists
    all_concat_list_p.write_text("
".join(all_lines) + "
")
    fail_concat_list_p.write_text("
".join(fail_lines) + "
")

    # Run ffmpeg concat
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", str(all_concat_list_p),
        "-c", "copy", str(all_video_p)
    ], check=True)

    if fail_lines:
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(fail_concat_list_p),
            "-c", "copy", str(fail_video_p)
        ], check=True)

    # Clean up temp concat lists
    all_concat_list_p.unlink(missing_ok=True)
    fail_concat_list_p.unlink(missing_ok=True)

    # Write CSV
    with index_csv_p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()))
        writer.writeheader()
        writer.writerows(index_rows)

    manifest = {
        "all_video_path": str(all_video_p),
        "all_video_sha256": sha256_file(all_video_p),
        "all_video_size_bytes": all_video_p.stat().st_size,
        "failures_video_path": str(fail_video_p) if fail_video_p.exists() else None,
        "failures_video_sha256": sha256_file(fail_video_p) if fail_video_p.exists() else None,
        "failures_video_size_bytes": fail_video_p.stat().st_size if fail_video_p.exists() else 0,
        "index_csv_path": str(index_csv_p),
        "index_csv_sha256": sha256_file(index_csv_p),
        "total_episodes_indexed": len(index_rows),
    }

    manifest_json_p = output_dir / f"{prefix}_VIDEO_MANIFEST.json"
    manifest_json_p.write_text(json.dumps(manifest, indent=2) + "
")

    print(f"=== Review videos complete: {all_video_p} ({manifest['all_video_size_bytes']/1024/1024:.2f} MB) ===")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summaries", type=Path, required=True)
    parser.add_argument("--videos-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=("baseline", "topk"), default="baseline")
    args = parser.parse_args()

    build_review_videos(
        episodes_summary_path=args.summaries,
        videos_dir=args.videos_dir,
        output_dir=args.output_dir,
        mode=args.mode,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
