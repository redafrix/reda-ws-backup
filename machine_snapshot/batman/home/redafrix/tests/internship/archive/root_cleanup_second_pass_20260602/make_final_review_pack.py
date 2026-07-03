import argparse
import json
import random
import shutil
import subprocess
from pathlib import Path
from typing import Any

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
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
        episode_id = ep_dir.name
        # Try to find real episode_id from metadata if available
        meta_path = ep_dir / "episode_metadata.json"
        if meta_path.exists():
            try:
                data = json.loads(meta_path.read_text())
                episode_id = str(data.get("episode_id") or episode_id)
            except:
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
    """
    Tries to find and load the image from path_str, alt_path_str, npz_path_str, alt_npz_path_str.
    Returns: (Image.Image, resolved_source_description, is_missing_flag)
    """
    bob_root = Path("/media/rootalkhatib/My Passport/reda_ws")
    
    def try_file_path(p_str: str | None) -> Path | None:
        if not p_str:
            return None
        p = Path(p_str)
        # 1. Direct path (absolute or relative to current cwd)
        if p.exists():
            return p
        
        # 2. Relative to Bob workspace root
        try_bob = bob_root / p_str
        if try_bob.exists():
            return try_bob
            
        # 3. If path contains 'asynchvla_ws', try relative to Bob root by stripping prefix
        parts = p.parts
        if 'asynchvla_ws' in parts:
            idx = parts.index('asynchvla_ws')
            rel_path = Path(*parts[idx:])
            if (bob_root / rel_path).exists():
                return bob_root / rel_path
            if rel_path.exists():
                return rel_path
                
        # 4. Try relative to ep_dir / "images" / basename
        filename = p.name
        try_ep_img = ep_dir / "images" / filename
        if try_ep_img.exists():
            return try_ep_img
            
        # 5. Try ep_dir / basename
        try_ep = ep_dir / filename
        if try_ep.exists():
            return try_ep

        # 6. Try relative to raw_root
        try_raw = raw_root / filename
        if try_raw.exists():
            return try_raw
            
        # 7. Try relative to raw_root by appending relative parts starting from broad_mini_failure_v1_...
        if 'broad_mini_failure_v1_20260522_1025' in parts:
            idx = parts.index('broad_mini_failure_v1_20260522_1025')
            rel_part = Path(*parts[idx+1:])
            if (raw_root / rel_part).exists():
                return raw_root / rel_part
                
        # 8. Try 'episodes' folder relative suffix
        if 'episodes' in parts:
            idx = parts.index('episodes')
            rel_ep_path = Path(*parts[idx+1:])
            if (ep_dir / rel_ep_path).exists():
                return ep_dir / rel_ep_path

        return None

    # Step A: Try primary image path
    p_resolved = try_file_path(path_str)
    if p_resolved:
        try:
            return Image.open(p_resolved).convert("RGB").resize(size), str(p_resolved), False
        except Exception:
            pass
            
    # Step B: Try alternative image path (e.g. after_agent_image if before is missing)
    alt_resolved = try_file_path(alt_path_str)
    if alt_resolved:
        try:
            return Image.open(alt_resolved).convert("RGB").resize(size), f"alt:{alt_resolved}", False
        except Exception:
            pass

    # Step C: Try loading from primary npz
    npz_resolved = try_file_path(npz_path_str)
    if npz_resolved:
        try:
            data = np.load(npz_resolved)
            if npz_key in data:
                img_arr = data[npz_key]
                # Flip it (rot180)
                img_arr = np.ascontiguousarray(img_arr[::-1, ::-1])
                return Image.fromarray(img_arr.astype(np.uint8)).resize(size), f"npz:{npz_resolved}", False
        except Exception:
            pass

    # Step D: Try loading from alternative npz
    alt_npz_resolved = try_file_path(alt_npz_path_str)
    if alt_npz_resolved:
        try:
            data = np.load(alt_npz_resolved)
            if npz_key in data:
                img_arr = data[npz_key]
                # Flip it (rot180)
                img_arr = np.ascontiguousarray(img_arr[::-1, ::-1])
                return Image.fromarray(img_arr.astype(np.uint8)).resize(size), f"alt_npz:{alt_npz_resolved}", False
        except Exception:
            pass

    # Step E: If all sources fail, draw a visible red warning panel
    warning_text = "IMAGE MISSING"
    if npz_key == "robot0_eye_in_hand_image":
        warning_text = "WRIST MISSING"
    
    img_warn = Image.new("RGB", size, (180, 40, 40)) # red background
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
        # Common paths on linux
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "DejaVuSans.ttf"
        ]
        for p in paths:
            if Path(p).exists():
                return ImageFont.truetype(p, 16), ImageFont.truetype(p, 20)
        raise Exception("No font found")
    except Exception:
        font = ImageFont.load_default()
        return font, font


def make_frame(
    *,
    agent_img: Image.Image,
    wrist_img: Image.Image,
    meta: dict[str, Any],
    step: int,
    start: int,
    onset: int,
    end: int,
) -> Image.Image:
    small_font, title_font = font_pair()
    
    info_h = 180
    canvas = Image.new("RGB", (720, 360 + info_h), (18, 18, 20))
    canvas.paste(agent_img, (0, 0))
    canvas.paste(wrist_img, (360, 0))
    
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 720, 30), fill=(0, 0, 0, 150))
    draw.text((8, 4), "agent view", fill=(200, 200, 200), font=small_font)
    draw.text((368, 4), "wrist view", fill=(200, 200, 200), font=small_font)

    color = (255, 255, 255)
    role = "WINDOW"
    if step < onset:
        role = "PRE-ONSET"
        color = (245, 186, 72)
    elif step == onset:
        role = "ONSET"
        color = (255, 82, 82)
    else:
        role = "CORE"
        color = (255, 120, 120)

    # Progress bar
    draw.rectangle((20, 360 + 155, 700, 360 + 165), outline=(60, 60, 65))
    progress = (step - start) / max(1, end - start)
    draw.rectangle((20, 360 + 155, int(20 + 680 * progress), 360 + 165), fill=color)
    onset_pos = (onset - start) / max(1, end - start)
    draw.line((int(20 + 680 * onset_pos), 360 + 150, int(20 + 680 * onset_pos), 360 + 170), fill=(255, 255, 255), width=2)

    # Info text
    event_type = meta.get("event_type", "chunk_sample")
    risk_bin = meta.get("risk_bin", "N/A")
    risk_score = meta.get("risk_score", 0.0)
    confidence = meta.get("confidence", 0.0)
    task = meta.get("task_language", "N/A")
    target = meta.get("target_base", "N/A")
    goal = meta.get("goal_base", "N/A")
    held = meta.get("held_object", "N/A")
    episode_id = meta.get("episode_id", "N/A")

    draw.text((20, 370), f"{event_type} | {risk_bin} | {role}", fill=color, font=title_font)
    draw.text((20, 395), f"Step: {step} | Onset: {onset} | Risk: {risk_score:.2f} | Conf: {confidence:.2f}", fill=(235, 235, 235), font=small_font)
    draw.text((20, 420), f"Task: {task}", fill=(255, 255, 150), font=small_font)
    draw.text((20, 445), f"Target: {target} | Goal: {goal}", fill=(150, 255, 150), font=small_font)
    draw.text((20, 470), f"Held: {held}", fill=(150, 150, 255), font=small_font)
    draw.text((20, 495), f"ID: {episode_id}", fill=(150, 150, 160), font=small_font)

    return canvas


def verify_review_pack(out_dir: Path) -> tuple[bool, str]:
    """
    Verifies that the generated review pack contains valid, non-black images.
    Writes diagnostics JSON to out_dir / "verification_diagnostics.json"
    and a Markdown table to out_dir / "verification_report.md".
    """
    frames_root = out_dir / "frames"
    if not frames_root.exists():
        return False, f"Frames directory {frames_root} does not exist"
        
    video_dirs = [d for d in frames_root.iterdir() if d.is_dir()]
    if not video_dirs:
        return False, f"No video frame folders found under {frames_root}"
        
    diagnostics = {}
    passed = True
    failure_reasons = []
    
    # We will build a markdown table for the report
    md_lines = [
        "# Review Pack Non-Black Verification Report",
        "",
        "| Video Index | Video Name | Frames | Agent Missing % | Wrist Missing % | Avg Mean RGB | Avg Std RGB | Status |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |"
    ]
    
    for v_dir in sorted(video_dirs):
        frame_files = sorted([f for f in v_dir.glob("frame_*.png")])
        total_frames = len(frame_files)
        if total_frames == 0:
            diagnostics[v_dir.name] = {"error": "No frames found"}
            passed = False
            failure_reasons.append(f"{v_dir.name} has 0 frames")
            md_lines.append(f"| N/A | {v_dir.name} | 0 | - | - | - | - | FAIL (No frames) |")
            continue
            
        agent_missing_count = 0
        wrist_missing_count = 0
        total_mean_rgb = np.zeros(3)
        total_std_rgb = np.zeros(3)
        near_black_pixels_fraction_sum = 0.0
        
        for f_path in frame_files:
            img = Image.open(f_path).convert("RGB")
            arr = np.array(img)
            
            # Agent half: y in [30, 360], x in [0, 360]
            agent_half = arr[30:360, 0:360]
            # Wrist half: y in [30, 360], x in [360, 720]
            wrist_half = arr[30:360, 360:720]
            
            # Standard deviation check for placeholder (std < 5.0 means uniform red warning or black placeholder)
            # The red warning panel has some text, but let's check standard deviation
            if agent_half.std() < 5.0:
                agent_missing_count += 1
            if wrist_half.std() < 5.0:
                wrist_missing_count += 1
                
            # Pixel averages
            total_mean_rgb += arr.mean(axis=(0, 1))
            total_std_rgb += arr.std(axis=(0, 1))
            
            # Near-black pixels (value < 30)
            near_black_pixels_fraction_sum += (arr < 30).mean()
            
        # Compute averages across all frames in this video
        avg_mean_rgb = (total_mean_rgb / total_frames).tolist()
        avg_std_rgb = (total_std_rgb / total_frames).tolist()
        avg_near_black_fraction = near_black_pixels_fraction_sum / total_frames
        
        agent_missing_pct = (agent_missing_count / total_frames) * 100
        wrist_missing_pct = (wrist_missing_count / total_frames) * 100
        
        video_status = "PASS"
        video_reasons = []
        
        # We fail if agent view is missing in > 20% of frames
        if agent_missing_pct > 20.0:
            video_status = "FAIL"
            video_reasons.append(f"Agent view missing in {agent_missing_pct:.1f}% of frames")
        
        # We fail if wrist is missing in > 20% of frames
        if wrist_missing_pct > 20.0:
            video_status = "FAIL"
            video_reasons.append(f"Wrist view missing in {wrist_missing_pct:.1f}% of frames")
            
        if np.mean(avg_std_rgb) < 5.0:
            video_status = "FAIL"
            video_reasons.append("Pixel standard deviation is tiny (almost uniform frame)")
            
        if video_status == "FAIL":
            passed = False
            failure_reasons.extend([f"{v_dir.name}: {r}" for r in video_reasons])
            
        diagnostics[v_dir.name] = {
            "total_frames": total_frames,
            "agent_missing_pct": agent_missing_pct,
            "wrist_missing_pct": wrist_missing_pct,
            "avg_mean_rgb": avg_mean_rgb,
            "avg_std_rgb": avg_std_rgb,
            "avg_near_black_fraction": avg_near_black_fraction,
            "status": video_status,
            "reasons": video_reasons
        }
        
        try:
            v_idx = int(v_dir.name.split("_")[0])
        except:
            v_idx = 0
            
        md_lines.append(
            f"| {v_idx:03d} | {v_dir.name} | {total_frames} | {agent_missing_pct:.1f}% | {wrist_missing_pct:.1f}% | "
            f"[{', '.join(f'{x:.1f}' for x in avg_mean_rgb)}] | [{', '.join(f'{x:.1f}' for x in avg_std_rgb)}] | {video_status} |"
        )
        
    write_json(out_dir / "verification_diagnostics.json", {
        "passed": passed,
        "failure_reasons": failure_reasons,
        "diagnostics": diagnostics
    })
    
    md_lines.insert(2, f"**Overall Status: {'PASSED' if passed else 'FAILED'}**")
    if failure_reasons:
        md_lines.insert(3, "\n### Failure Reasons:\n" + "\n".join(f"- {r}" for r in failure_reasons) + "\n")
        
    (out_dir / "verification_report.md").write_text("\n".join(md_lines) + "\n")
    
    if not passed:
        return False, f"Verification failed: {'; '.join(failure_reasons[:3])}"
    return True, "Verification passed successfully!"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", required=True)
    parser.add_argument("--label-root", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--pre-steps", type=int, default=60)
    parser.add_argument("--core-steps", type=int, default=10)
    parser.add_argument("--fps", type=int, default=20)
    args = parser.parse_args()

    raw_root = Path(args.raw_root)
    label_root = Path(args.label_root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    chunks = load_jsonl(label_root / "mini_failure_chunk_labels.jsonl")
    events = load_jsonl(label_root / "mini_failure_events.jsonl")
    eps = episode_dirs(raw_root)

    # Sampling
    selected_samples = []

    # 1. 50 wrong_object_picked risky chunks
    risky_bins = ["RISKY_STRONG", "RISKY_WEAK"]
    risky_chunks = [c for c in chunks if c.get("risk_bin") in risky_bins and "wrong_object_picked" in c.get("event_types", [])]
    risky_chunks.sort(key=lambda x: (x.get("risk_bin") == "RISKY_STRONG", x.get("risk_score", 0)), reverse=True)
    selected_samples.extend(risky_chunks[:50])
    print(f"Selected {min(len(risky_chunks), 50)} risky wrong_object_picked chunks")

    # 2. Every remaining non-wrong-object risky event/chunk
    other_risky = [c for c in chunks if c.get("risk_bin") in risky_bins and "wrong_object_picked" not in c.get("event_types", [])]
    selected_samples.extend(other_risky)
    print(f"Selected {len(other_risky)} other risky chunks")

    # 3. 20 random UNCERTAIN chunks
    uncertain = [c for c in chunks if c.get("risk_bin") == "UNCERTAIN"]
    random.seed(42)
    selected_samples.extend(random.sample(uncertain, min(len(uncertain), 20)))
    print(f"Selected {min(len(uncertain), 20)} uncertain chunks")

    # 4. 20 SAFE_STRONG / SAFE_WEAK controls
    safe = [c for c in chunks if c.get("risk_bin") in ["SAFE_STRONG", "SAFE_WEAK"]]
    selected_samples.extend(random.sample(safe, min(len(safe), 20)))
    print(f"Selected {min(len(safe), 20)} safe chunks")

    # Process samples
    manifest = []
    for idx, sample in enumerate(selected_samples, 1):
        ep_id = sample.get("episode_id")
        if ep_id not in eps:
            print(f"Skipping {ep_id}: not found in raw_root")
            continue
        
        ep_dir = eps[ep_id]
        steps = load_steps(ep_dir)
        
        # Determine onset and window
        onset = sample.get("peak_step") or sample.get("start_step")
        event_types = sample.get("event_types", [])
        primary_event = event_types[0] if event_types else "none"
        
        # Meta for display
        meta = {
            "episode_id": ep_id,
            "risk_bin": sample.get("risk_bin"),
            "risk_score": sample.get("risk_score", 0.0),
            "confidence": sample.get("confidence", 0.0),
            "event_type": primary_event,
            "task_language": sample.get("task_language"),
            "target_base": sample.get("target_base"),
            "goal_base": sample.get("goal_base"),
            "held_object": "N/A"
        }
        
        # Try to find matching event for held_object
        for ev in events:
            if ev.get("episode_id") == ep_id and abs(ev.get("onset_step", 0) - onset) < 10:
                meta["event_type"] = ev.get("event_type")
                meta["confidence"] = ev.get("confidence", meta["confidence"])
                evidence = ev.get("evidence", {})
                non_target = evidence.get("non_target_held_objects")
                if non_target:
                    meta["held_object"] = ", ".join(non_target)
                elif "dominant_moving_object" in evidence:
                    meta["held_object"] = evidence["dominant_moving_object"].get("object", "N/A")
                break

        start = max(0, onset - args.pre_steps)
        end = onset + args.core_steps - 1
        total_frames = end - start + 1
        
        video_name_no_ext = f"{idx:03d}_{sample['risk_bin']}_{primary_event}_step{onset}_{ep_id}"
        video_name = f"{video_name_no_ext}.mp4"
        video_path = out_dir / video_name
        
        frames_dir = out_dir / "frames" / video_name_no_ext
        frames_dir.mkdir(parents=True, exist_ok=True)
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        vw = cv2.VideoWriter(str(video_path), fourcc, args.fps, (720, 360 + 180))
        
        frames_missing_agent = 0
        frames_missing_wrist = 0
        variances = []
        resolved_agent_sources = []
        resolved_wrist_sources = []
        
        for s in range(start, end + 1):
            step_row = steps.get(s) or {}
            paths = step_row.get("paths") or {}
            
            # Extract possible sources for agent
            agent_path = paths.get("before_agent_image")
            alt_agent_path = paths.get("after_agent_image")
            npz_agent_path = paths.get("before_obs_npz")
            alt_npz_agent_path = paths.get("after_obs_npz")
            
            # Extract possible sources for wrist
            wrist_path = paths.get("before_wrist_image")
            alt_wrist_path = paths.get("after_wrist_image")
            npz_wrist_path = paths.get("before_obs_npz")
            alt_npz_wrist_path = paths.get("after_obs_npz")
            
            # Load images robustly
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
            
            # Compute pixel variance of the two views
            a_arr = np.array(agent_img)
            w_arr = np.array(wrist_img)
            variances.append(float((a_arr.var() + w_arr.var()) / 2.0))
            
            # Render frame
            canvas = make_frame(
                agent_img=agent_img,
                wrist_img=wrist_img,
                meta=meta,
                step=s,
                start=start,
                onset=onset,
                end=end
            )
            
            # Save frame to disk (keep frames too for debugging)
            canvas.save(frames_dir / f"frame_{s-start:04d}.png")
            
            # Write to video
            frame_cv = cv2.cvtColor(np.array(canvas), cv2.COLOR_RGB2BGR)
            vw.write(frame_cv)
            
        vw.release()
        
        # Calculate diagnostics
        mean_pixel_variance = float(np.mean(variances))
        frames_missing_both = sum(
            1 for a_src, w_src in zip(resolved_agent_sources, resolved_wrist_sources)
            if a_src == "MISSING_PLACEHOLDER" and w_src == "MISSING_PLACEHOLDER"
        )
        black_frame_fraction = float(frames_missing_both / total_frames)
        
        manifest_entry = {
            "index": idx,
            "video": str(video_path),
            "episode_id": ep_id,
            "risk_bin": sample.get("risk_bin"),
            "risk_score": sample.get("risk_score"),
            "onset_step": onset,
            "event_type": primary_event,
            "task": meta["task_language"],
            "diagnostics": {
                "total_frames": total_frames,
                "frames_with_agent_image": total_frames - frames_missing_agent,
                "frames_with_wrist_image": total_frames - frames_missing_wrist,
                "frames_missing_agent": frames_missing_agent,
                "frames_missing_wrist": frames_missing_wrist,
                "mean_pixel_variance": mean_pixel_variance,
                "black_frame_fraction": black_frame_fraction
            },
            "resolved_image_paths": {
                "agent_sources": resolved_agent_sources,
                "wrist_sources": resolved_wrist_sources
            }
        }
        manifest.append(manifest_entry)
        print(f"Generated {video_name} (variance: {mean_pixel_variance:.1f}, missing agent: {frames_missing_agent}, missing wrist: {frames_missing_wrist})")

    with (out_dir / "manifest.jsonl").open("w") as f:
        for m in manifest:
            f.write(json.dumps(m) + "\n")

    print(f"\nDone! Generated {len(manifest)} videos in {out_dir}")
    
    print("\nRunning automated non-black verification...")
    success, msg = verify_review_pack(out_dir)
    print(msg)
    if not success:
        print("Warning: verification failed!")
        exit(1)


if __name__ == "__main__":
    main()
