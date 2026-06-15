from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def episode_dirs(raw_root: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for steps in raw_root.rglob("steps.jsonl"):
        ep_dir = steps.parent
        meta_path = ep_dir / "episode_metadata.json"
        summary_path = ep_dir / "summary.json"
        episode_id = ep_dir.name
        for path in [meta_path, summary_path]:
            if path.exists():
                try:
                    data = json.loads(path.read_text())
                    episode_id = str(data.get("episode_id") or episode_id)
                    break
                except Exception:
                    pass
        out[episode_id] = ep_dir
    return out


def load_steps(ep_dir: Path) -> dict[int, dict[str, Any]]:
    rows = load_jsonl(ep_dir / "steps.jsonl")
    return {int(row.get("env_step", 0)): row for row in rows}


def resolve_and_load_image(
    path_str: str | None,
    size: tuple[int, int],
    raw_root: Path,
    ep_dir: Path,
    alt_path_str: str | None = None,
    npz_path_str: str | None = None,
    alt_npz_path_str: str | None = None,
    npz_key: str = "agentview_image"
) -> tuple[Image.Image, str, bool]:
    bob_root = Path("/media/rootalkhatib/My Passport/reda_ws")
    
    def try_file_path(p_str: str | None) -> Path | None:
        if not p_str:
            return None
        p = Path(p_str)
        if p.exists():
            return p
        try_bob = bob_root / p_str
        if try_bob.exists():
            return try_bob
        parts = p.parts
        if 'asynchvla_ws' in parts:
            idx = parts.index('asynchvla_ws')
            rel_path = Path(*parts[idx:])
            if (bob_root / rel_path).exists():
                return bob_root / rel_path
            if rel_path.exists():
                return rel_path
        filename = p.name
        try_ep_img = ep_dir / "images" / filename
        if try_ep_img.exists():
            return try_ep_img
        try_ep = ep_dir / filename
        if try_ep.exists():
            return try_ep
        try_raw = raw_root / filename
        if try_raw.exists():
            return try_raw
        if 'broad_mini_failure_v1_20260522_1025' in parts:
            idx = parts.index('broad_mini_failure_v1_20260522_1025')
            rel_part = Path(*parts[idx+1:])
            if (raw_root / rel_part).exists():
                return raw_root / rel_part
        if 'episodes' in parts:
            idx = parts.index('episodes')
            rel_ep_path = Path(*parts[idx+1:])
            if (ep_dir / rel_ep_path).exists():
                return ep_dir / rel_ep_path
        return None

    # Step A: Try primary
    p_resolved = try_file_path(path_str)
    if p_resolved:
        try:
            return Image.open(p_resolved).convert("RGB").resize(size), str(p_resolved), False
        except Exception:
            pass
            
    # Step B: Try alt
    alt_resolved = try_file_path(alt_path_str)
    if alt_resolved:
        try:
            return Image.open(alt_resolved).convert("RGB").resize(size), f"alt:{alt_resolved}", False
        except Exception:
            pass

    # Step C: Try primary npz
    npz_resolved = try_file_path(npz_path_str)
    if npz_resolved:
        try:
            data = np.load(npz_resolved)
            if npz_key in data:
                img_arr = data[npz_key]
                img_arr = np.ascontiguousarray(img_arr[::-1, ::-1])
                return Image.fromarray(img_arr.astype(np.uint8)).resize(size), f"npz:{npz_resolved}", False
        except Exception:
            pass

    # Step D: Try alt npz
    alt_npz_resolved = try_file_path(alt_npz_path_str)
    if alt_npz_resolved:
        try:
            data = np.load(alt_npz_resolved)
            if npz_key in data:
                img_arr = data[npz_key]
                img_arr = np.ascontiguousarray(img_arr[::-1, ::-1])
                return Image.fromarray(img_arr.astype(np.uint8)).resize(size), f"alt_npz:{alt_npz_resolved}", False
        except Exception:
            pass

    # Step E: Warning panel
    warning_text = "IMAGE MISSING"
    if npz_key == "robot0_eye_in_hand_image":
        warning_text = "WRIST MISSING"
    
    img_warn = Image.new("RGB", size, (180, 40, 40))
    draw = ImageDraw.Draw(img_warn)
    try:
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "DejaVuSans-Bold.ttf"
        ]
        font = None
        for p in paths:
            if Path(p).exists():
                font = ImageFont.truetype(p, 18)
                break
        if font is None:
            font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()
        
    draw.text((10, size[1] // 2 - 10), warning_text, fill=(255, 255, 255), font=font)
    return img_warn, "MISSING_PLACEHOLDER", True


def font_pair() -> tuple[Any, Any]:
    try:
        return ImageFont.truetype("DejaVuSans.ttf", 18), ImageFont.truetype("DejaVuSans-Bold.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
        return font, font


def make_frame(
    *,
    agent_img: Image.Image,
    wrist_img: Image.Image,
    event: dict[str, Any],
    step: int,
    start: int,
    onset: int,
    end: int,
    out_path: Path,
) -> None:
    small_font, title_font = font_pair()
    info_h = 120
    canvas = Image.new("RGB", (720, 360 + info_h), (18, 18, 20))
    canvas.paste(agent_img, (0, 0))
    canvas.paste(wrist_img, (360, 0))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 720, 30), fill=(0, 0, 0))
    draw.text((8, 4), "agent view", fill=(255, 255, 255), font=small_font)
    draw.text((368, 4), "wrist view", fill=(255, 255, 255), font=small_font)

    if step < onset:
        role = "PRE-FAILURE"
        color = (245, 186, 72)
    else:
        role = "FAILURE CORE"
        color = (255, 82, 82)
    progress = (step - start) / max(1, end - start)
    draw.rectangle((0, 360, 720, 480), fill=(26, 26, 30))
    draw.rectangle((20, 452, 700, 468), outline=(90, 90, 96))
    draw.rectangle((20, 452, int(20 + 680 * progress), 468), fill=color)
    draw.line((20 + int(680 * ((onset - start) / max(1, end - start))), 448, 20 + int(680 * ((onset - start) / max(1, end - start))), 472), fill=(255, 255, 255), width=2)

    event_type = event.get("event_type")
    severity = float(event.get("severity", 0.0))
    confidence = float(event.get("confidence", 0.0))
    draw.text((20, 372), f"{event_type} | {role}", fill=color, font=title_font)
    draw.text((20, 402), f"step {step} / onset {onset} | severity {severity:.2f} | confidence {confidence:.2f}", fill=(235, 235, 235), font=small_font)
    draw.text((20, 426), str(event.get("episode_id")), fill=(190, 190, 198), font=small_font)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path)


def choose_events(events: list[dict[str, Any]], max_videos: int) -> list[dict[str, Any]]:
    by_type: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        by_type.setdefault(str(event.get("event_type")), []).append(event)
    for rows in by_type.values():
        rows.sort(key=lambda e: float(e.get("severity", 0.0)) * float(e.get("confidence", 0.0)), reverse=True)
    selected: list[dict[str, Any]] = []
    while len(selected) < max_videos:
        added = False
        for event_type in sorted(by_type):
            if by_type[event_type] and len(selected) < max_videos:
                selected.append(by_type[event_type].pop(0))
                added = True
        if not added:
            break
    return selected


def run_ffmpeg(frame_dir: Path, out_mp4: Path, fps: int) -> None:
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-framerate",
        str(fps),
        "-i",
        str(frame_dir / "frame_%04d.png"),
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        str(out_mp4),
    ]
    subprocess.run(cmd, check=True)


def make_event_video(
    *,
    event: dict[str, Any],
    ep_dir: Path,
    out_dir: Path,
    pre_steps: int,
    core_steps: int,
    fps: int,
    index: int,
    frames_only: bool = False,
) -> dict[str, Any]:
    steps = load_steps(ep_dir)
    onset = int(event.get("onset_step", 0))
    start = max(0, onset - pre_steps)
    end = onset + core_steps - 1
    event_type = str(event.get("event_type", "event"))
    episode_id = str(event.get("episode_id", ep_dir.name))
    safe_ep = "".join(c if c.isalnum() or c in "-_" else "_" for c in episode_id)
    name = f"{index:02d}_{event_type}_onset{onset}_{safe_ep}"
    frame_dir = out_dir / "frames" / name
    if frame_dir.exists():
        shutil.rmtree(frame_dir)
    frame_dir.mkdir(parents=True, exist_ok=True)
    
    raw_root = ep_dir.parent.parent
    
    frames_missing_agent = 0
    frames_missing_wrist = 0
    resolved_agent_sources = []
    resolved_wrist_sources = []
    
    for i, step in enumerate(range(start, end + 1)):
        step_row = steps.get(step) or {}
        paths = step_row.get("paths") or {}
        
        agent_path = paths.get("before_agent_image")
        alt_agent_path = paths.get("after_agent_image")
        npz_agent_path = paths.get("before_obs_npz")
        alt_npz_agent_path = paths.get("after_obs_npz")
        
        wrist_path = paths.get("before_wrist_image")
        alt_wrist_path = paths.get("after_wrist_image")
        npz_wrist_path = paths.get("before_obs_npz")
        alt_npz_wrist_path = paths.get("after_obs_npz")
        
        agent_img, agent_src, agent_missing = resolve_and_load_image(
            path_str=agent_path,
            size=(360, 360),
            raw_root=raw_root,
            ep_dir=ep_dir,
            alt_path_str=alt_agent_path,
            npz_path_str=npz_agent_path,
            alt_npz_path_str=alt_npz_agent_path,
            npz_key="agentview_image"
        )
        
        wrist_img, wrist_src, wrist_missing = resolve_and_load_image(
            path_str=wrist_path,
            size=(360, 360),
            raw_root=raw_root,
            ep_dir=ep_dir,
            alt_path_str=alt_wrist_path,
            npz_path_str=npz_wrist_path,
            alt_npz_path_str=alt_npz_wrist_path,
            npz_key="robot0_eye_in_hand_image"
        )
        
        if agent_missing:
            frames_missing_agent += 1
        if wrist_missing:
            frames_missing_wrist += 1
            
        resolved_agent_sources.append(agent_src)
        resolved_wrist_sources.append(wrist_src)
        
        make_frame(
            agent_img=agent_img,
            wrist_img=wrist_img,
            event=event,
            step=step,
            start=start,
            onset=onset,
            end=end,
            out_path=frame_dir / f"frame_{i:04d}.png",
        )
        
    mp4 = out_dir / f"{name}.mp4"
    if not frames_only:
        run_ffmpeg(frame_dir, mp4, fps)
        
    total_frames = end - start + 1
    return {
        "index": index,
        "video": str(mp4) if not frames_only else None,
        "frame_dir": str(frame_dir),
        "event_type": event_type,
        "episode_id": episode_id,
        "onset_step": onset,
        "start_step": start,
        "end_step": end,
        "duration_seconds": total_frames / fps,
        "severity": event.get("severity"),
        "confidence": event.get("confidence"),
        "diagnostics": {
            "total_frames": total_frames,
            "frames_with_agent_image": total_frames - frames_missing_agent,
            "frames_with_wrist_image": total_frames - frames_missing_wrist,
            "frames_missing_agent": frames_missing_agent,
            "frames_missing_wrist": frames_missing_wrist
        },
        "resolved_image_paths": {
            "agent_sources": resolved_agent_sources,
            "wrist_sources": resolved_wrist_sources
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", required=True)
    parser.add_argument("--events-jsonl", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--max-videos", type=int, default=10)
    parser.add_argument("--pre-steps", type=int, default=60)
    parser.add_argument("--core-steps", type=int, default=10)
    parser.add_argument("--fps", type=int, default=20)
    parser.add_argument("--keep-frames", action="store_true")
    parser.add_argument("--frames-only", action="store_true")
    args = parser.parse_args()

    raw_root = Path(args.raw_root)
    out_dir = Path(args.out_dir)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    events = load_jsonl(Path(args.events_jsonl))
    eps = episode_dirs(raw_root)
    selected = [event for event in choose_events(events, args.max_videos) if str(event.get("episode_id")) in eps]
    manifest = []
    for idx, event in enumerate(selected, 1):
        manifest.append(
            make_event_video(
                event=event,
                ep_dir=eps[str(event.get("episode_id"))],
                out_dir=out_dir,
                pre_steps=args.pre_steps,
                core_steps=args.core_steps,
                fps=args.fps,
                index=idx,
                frames_only=args.frames_only,
            )
        )
    if not args.keep_frames and not args.frames_only:
        shutil.rmtree(out_dir / "frames", ignore_errors=True)
    with (out_dir / "manifest.jsonl").open("w") as f:
        for row in manifest:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")
    write_json(out_dir / "summary.json", {
        "raw_root": str(raw_root),
        "events_jsonl": str(args.events_jsonl),
        "out_dir": str(out_dir),
        "videos": len(manifest),
        "pre_steps": args.pre_steps,
        "core_steps": args.core_steps,
        "fps": args.fps,
        "duration_seconds": (args.pre_steps + args.core_steps) / args.fps,
        "manifest": manifest,
    })
    print(json.dumps({"out_dir": str(out_dir), "videos": len(manifest)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
