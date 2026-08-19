#!/usr/bin/env python3
"""Build OOD400 Composite Review Videos and Indexes with Visual Metadata Overlays.

Renders per-episode overlay text:
- Baseline: Mode, Episode ID, Task, Outcome, Min distance, Success tick / Timeout.
- TopK: Mode, Episode ID, Task, Outcome, Threshold A, C=0.90, Interventions count, Min distance, Success tick / Timeout.

Concatenates into:
- ALL400 review MP4
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
import tempfile
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


def render_annotated_clip(
    *,
    input_video: Path,
    output_video: Path,
    text_content: str,
    tmp_dir: Path,
) -> None:
    text_file = tmp_dir / f"overlay_{output_video.stem}.txt"
    text_file.write_text(text_content, encoding="utf-8")

    # Use ffmpeg drawtext filter with textfile parameter
    filter_expr = f"drawtext=textfile='{text_file}':fontsize=10:fontcolor=white:box=1:boxcolor=black@0.65:boxborderw=3:x=8:y=8"
    
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(input_video),
        "-vf", filter_expr,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "30",
        "-pix_fmt", "yuv420p",
        str(output_video)
    ]
    subprocess.run(cmd, check=True)


def build_review_videos(
    *,
    episodes_summary_path: Path,
    videos_dir: Path,
    output_dir: Path,
    mode: str = "baseline",
    decisions_jsonl_path: Path | None = None,
    controller_info: dict[str, Any] | None = None,
) -> dict[str, Any]:
    episodes_summary_path = Path(episodes_summary_path).resolve()
    videos_dir = Path(videos_dir).resolve()
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    summaries = [json.loads(line) for line in episodes_summary_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(summaries) != 400:
        raise ValueError(f"Expected 400 episodes, found {len(summaries)}")

    # Map interventions per episode if in topk mode
    interventions_map: dict[str, int] = {}
    if mode == "topk" and decisions_jsonl_path and Path(decisions_jsonl_path).exists():
        dec_lines = [json.loads(l) for l in Path(decisions_jsonl_path).read_text(encoding="utf-8").splitlines() if l.strip()]
        for d in dec_lines:
            if d.get("intervention_accepted") is True:
                ep_id = str(d["episode_id"])
                interventions_map[ep_id] = interventions_map.get(ep_id, 0) + 1

    prefix = "OOD400_BASELINE" if mode == "baseline" else "OOD400_TOPK"
    all_video_p = output_dir / f"{prefix}_ALL400_REVIEW.mp4"
    fail_video_p = output_dir / f"{prefix}_FAILURES_ONLY_REVIEW.mp4"
    index_csv_p = output_dir / f"{prefix}_VIDEO_INDEX.csv"

    index_rows: list[dict[str, Any]] = []
    current_time_all = 0.0

    print(f"=== Rendering annotated {mode} clips and composite review videos ===")

    with tempfile.TemporaryDirectory(prefix="ood400_video_build_") as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        annotated_clips_all: list[Path] = []
        annotated_clips_fail: list[Path] = []

        for s in summaries:
            ep_id = s["episode_id"]
            src_vid_p = videos_dir / f"{ep_id}.mp4"
            if not src_vid_p.exists():
                raise FileNotFoundError(f"Missing source video for ep {ep_id}: {src_vid_p}")

            succ = bool(s["success"])
            outcome_str = "SUCCESS" if succ else "FAILURE"
            min_dist = float(s["minimum_tcp_distance_m"])
            succ_tick = s.get("first_3cm_crossing_control_tick")
            end_note = f"3 CM REACHED @ tick {succ_tick}" if succ else "TIMEOUT @ 350"

            if mode == "baseline":
                overlay_lines = [
                    f"NORMAL SIMVLA | Episode: {ep_id}",
                    f"Task: {s['instruction']}",
                    f"Outcome: {outcome_str} | Min dist: {min_dist:.3f}m",
                    f"Result: {end_note}",
                ]
            else:
                a_rule = controller_info.get("main_threshold_name", "Best F1") if controller_info else "Best F1"
                a_val = float(controller_info.get("main_threshold_value", 0.5791)) if controller_info else 0.5791
                interv_cnt = interventions_map.get(ep_id, 0)
                overlay_lines = [
                    f"TOPK SIMVLA | Episode: {ep_id}",
                    f"Task: {s['instruction']}",
                    f"Outcome: {outcome_str} | Interventions: {interv_cnt}",
                    f"A: {a_rule} ({a_val:.4f}), C: 0.90 | Min dist: {min_dist:.3f}m",
                    f"Result: {end_note}",
                ]

            annotated_clip_p = tmp_dir / f"annotated_{ep_id}.mp4"
            render_annotated_clip(
                input_video=src_vid_p,
                output_video=annotated_clip_p,
                text_content="\n".join(overlay_lines),
                tmp_dir=tmp_dir,
            )

            dur = get_video_duration(annotated_clip_p)
            start_time = current_time_all
            end_time = current_time_all + dur
            current_time_all = end_time

            annotated_clips_all.append(annotated_clip_p)
            if not succ:
                annotated_clips_fail.append(annotated_clip_p)

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
                "source_video_path": str(src_vid_p),
            })

        # Concat all annotated clips
        all_concat_list_p = tmp_dir / "concat_all.txt"
        all_concat_list_p.write_text("\n".join(f"file '{p}'" for p in annotated_clips_all) + "\n")

        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(all_concat_list_p),
            "-c", "copy", str(all_video_p)
        ], check=True)

        # Concat failures annotated clips
        if annotated_clips_fail:
            fail_concat_list_p = tmp_dir / "concat_fail.txt"
            fail_concat_list_p.write_text("\n".join(f"file '{p}'" for p in annotated_clips_fail) + "\n")

            subprocess.run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-f", "concat", "-safe", "0", "-i", str(fail_concat_list_p),
                "-c", "copy", str(fail_video_p)
            ], check=True)

    # Write CSV
    with index_csv_p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()))
        writer.writeheader()
        writer.writerows(index_rows)

    manifest = {
        "schema_version": "ood400_review_video_manifest_v1",
        "mode": mode,
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
    manifest_json_p.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"=== Review videos complete: {all_video_p} ({manifest['all_video_size_bytes']/1024/1024:.2f} MB) ===")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summaries", type=Path, required=True)
    parser.add_argument("--videos-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=("baseline", "topk"), default="baseline")
    parser.add_argument("--decisions", type=Path, default=None)
    parser.add_argument("--controller-json", type=Path, default=None)
    args = parser.parse_args()

    ctrl_info = None
    if args.controller_json and args.controller_json.exists():
        ctrl_info = json.loads(args.controller_json.read_text(encoding="utf-8"))

    build_review_videos(
        episodes_summary_path=args.summaries,
        videos_dir=args.videos_dir,
        output_dir=args.output_dir,
        mode=args.mode,
        decisions_jsonl_path=args.decisions,
        controller_info=ctrl_info,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
