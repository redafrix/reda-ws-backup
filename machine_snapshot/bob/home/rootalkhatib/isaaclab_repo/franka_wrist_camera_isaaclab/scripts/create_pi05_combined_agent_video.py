#!/usr/bin/env python3
"""Create one labeled agent-view video for Pi0.5 rollout collections."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


DEFAULT_FONT = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reaching-dir", type=Path, required=True)
    parser.add_argument("--pick-place-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--speed", type=float, default=2.0)
    parser.add_argument("--font", type=Path, default=DEFAULT_FONT)
    parser.add_argument("--crf", type=int, default=23)
    parser.add_argument("--preset", default="ultrafast")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def episode_dirs(collection_dir: Path) -> list[Path]:
    episodes = sorted(path for path in collection_dir.iterdir() if path.is_dir() and path.name.isdigit())
    if not episodes:
        raise FileNotFoundError(f"No numbered episodes found in {collection_dir}")
    return episodes


def load_meta(episode_dir: Path) -> dict:
    path = episode_dir / "meta.json"
    if not path.is_file():
        raise FileNotFoundError(f"Missing metadata: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def compact_instruction(text: str, max_chars: int = 80) -> str:
    text = " ".join(str(text).split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def label_for(task_name: str, episode_dir: Path, index: int, total: int, meta: dict) -> str:
    instruction = compact_instruction(meta.get("instruction") or "")
    success = meta.get("success")
    status = "success" if success is True else "failure" if success is False else "unknown"
    parts = [f"Pi0.5 {index:02d}/{total:02d}", task_name, f"episode {episode_dir.name}", status]
    if instruction:
        parts.append(instruction)
    return " | ".join(parts)


def iter_agent_frames(episode_dir: Path, meta: dict):
    input_video = episode_dir / "agent_camera.mp4"
    if input_video.is_file():
        reader = None
        try:
            reader = imageio.get_reader(input_video, "ffmpeg")
            fps = float(reader.get_meta_data()["fps"])
            yield fps, reader
            return
        except Exception as exc:
            if reader is not None:
                reader.close()
            print(f"[WARN] falling back to rgb.npz for {episode_dir}: {exc}", flush=True)

    rgb_path = episode_dir / "rgb.npz"
    if not rgb_path.is_file():
        raise FileNotFoundError(f"Missing agent video and rgb fallback for {episode_dir}")
    rgb_data = np.load(rgb_path)
    if "agent_rgb" not in rgb_data:
        raise KeyError(f"Missing agent_rgb in {rgb_path}")
    fps = float(meta.get("camera_fps") or 20.0)
    yield fps, rgb_data["agent_rgb"]


def draw_label(frame: np.ndarray, text: str, font: ImageFont.FreeTypeFont) -> np.ndarray:
    image = Image.fromarray(frame)
    draw = ImageDraw.Draw(image, "RGBA")
    x, y = 12, 12
    padding = 8
    bbox = draw.textbbox((x, y), text, font=font)
    box = (bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding)
    draw.rectangle(box, fill=(0, 0, 0, 175))
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))
    return np.asarray(image)


def iter_episode_specs(reaching_dir: Path, pick_place_dir: Path) -> list[tuple[str, Path, dict]]:
    specs: list[tuple[str, Path, dict]] = []
    for task_name, collection_dir in (("reaching", reaching_dir), ("pick_place", pick_place_dir)):
        for episode_dir in episode_dirs(collection_dir):
            specs.append((task_name, episode_dir, load_meta(episode_dir)))
    return specs


def build_video(
    specs: list[tuple[str, Path, dict]],
    output: Path,
    speed: float,
    font_path: Path,
    crf: int,
    preset: str,
    force: bool,
) -> None:
    if output.exists() and not force:
        raise FileExistsError(f"Output already exists; pass --force: {output}")
    if speed <= 0:
        raise ValueError("--speed must be positive")
    if not font_path.is_file():
        raise FileNotFoundError(f"Font not found: {font_path}")

    output.parent.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype(str(font_path), size=24)
    writer = None
    total = len(specs)
    frames_written = 0

    try:
        for index, (task_name, episode_dir, meta) in enumerate(specs, start=1):
            label = label_for(task_name, episode_dir, index, total, meta)
            episode_frames = 0
            for fps, frames in iter_agent_frames(episode_dir, meta):
                if writer is None:
                    writer = imageio.get_writer(
                        output,
                        fps=fps,
                        codec="libx264",
                        quality=None,
                        ffmpeg_params=[
                            "-preset",
                            preset,
                            "-crf",
                            str(crf),
                            "-pix_fmt",
                            "yuv420p",
                            "-movflags",
                            "+faststart",
                        ],
                        macro_block_size=1,
                    )

                next_keep = 0.0
                for frame_index, frame in enumerate(frames):
                    if frame_index + 1e-9 >= next_keep:
                        writer.append_data(draw_label(frame, label, font))
                        frames_written += 1
                        episode_frames += 1
                        next_keep += speed
                if hasattr(frames, "close"):
                    frames.close()
            print(f"[INFO] wrote {index}/{total}: {task_name} {episode_dir.name} ({episode_frames} frames)")
    finally:
        if writer is not None:
            writer.close()

    print(f"[DONE] wrote {output} ({frames_written} frames)")


def main() -> None:
    args = parse_args()
    specs = iter_episode_specs(args.reaching_dir, args.pick_place_dir)
    build_video(specs, args.output, args.speed, args.font, args.crf, args.preset, args.force)


if __name__ == "__main__":
    main()
