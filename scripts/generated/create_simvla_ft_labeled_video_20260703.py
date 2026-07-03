#!/usr/bin/env python3
"""Create one fast, readable, agent-view video for SimVLA Isaac rollouts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


DEFAULT_FONT = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


TASK_LINES = [
    ("TASK 01/10  REACH", "reach the avocado"),
    ("TASK 02/10  REACH", "reach the bowl"),
    ("TASK 03/10  REACH", "reach the basket"),
    ("TASK 04/10  REACH", "reach the onion"),
    ("TASK 05/10  REACH", "reach the onion"),
    ("TASK 06/10  PICK + PLACE", "can -> tray"),
    ("TASK 07/10  PICK + PLACE", "can -> basket"),
    ("TASK 08/10  PICK + PLACE", "onion -> tray"),
    ("TASK 09/10  PICK + PLACE", "onion -> tray"),
    ("TASK 10/10  PICK + PLACE", "kiwi -> basket"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reaching-dir", type=Path, required=True)
    parser.add_argument("--pick-place-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--speed", type=float, default=4.0)
    parser.add_argument("--font", type=Path, default=DEFAULT_FONT)
    parser.add_argument("--crf", type=int, default=21)
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


def iter_episode_specs(reaching_dir: Path, pick_place_dir: Path) -> list[tuple[Path, dict]]:
    specs: list[tuple[Path, dict]] = []
    for collection_dir in (reaching_dir, pick_place_dir):
        for episode_dir in episode_dirs(collection_dir):
            specs.append((episode_dir, load_meta(episode_dir)))
    if len(specs) != len(TASK_LINES):
        raise RuntimeError(f"Expected {len(TASK_LINES)} episodes, found {len(specs)}")
    return specs


def iter_agent_frames(episode_dir: Path, meta: dict):
    video = episode_dir / "agent_camera.mp4"
    if video.is_file():
        reader = imageio.get_reader(video, "ffmpeg")
        try:
            fps = float(reader.get_meta_data()["fps"])
            yield fps, reader
            return
        finally:
            reader.close()

    rgb_path = episode_dir / "rgb.npz"
    if not rgb_path.is_file():
        raise FileNotFoundError(f"Missing agent_camera.mp4 and rgb.npz fallback for {episode_dir}")
    rgb_data = np.load(rgb_path)
    if "agent_rgb" not in rgb_data:
        raise KeyError(f"Missing agent_rgb in {rgb_path}")
    fps = float(meta.get("camera_fps") or 20.0)
    yield fps, rgb_data["agent_rgb"]


def fit_font(font_path: Path, text: str, max_width: int, start_size: int, min_size: int) -> ImageFont.FreeTypeFont:
    for size in range(start_size, min_size - 1, -1):
        font = ImageFont.truetype(str(font_path), size=size)
        bbox = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_width:
            return font
    return ImageFont.truetype(str(font_path), size=min_size)


def draw_centered(draw: ImageDraw.ImageDraw, y: int, text: str, font: ImageFont.FreeTypeFont, width: int) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    x = max(0, (width - (bbox[2] - bbox[0])) // 2)
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))


def draw_label(frame: np.ndarray, top_line: str, bottom_line: str, font_path: Path) -> np.ndarray:
    image = Image.fromarray(frame)
    draw = ImageDraw.Draw(image, "RGBA")
    width, _height = image.size
    banner_h = 70
    draw.rectangle((0, 0, width, banner_h), fill=(0, 0, 0, 225))
    top_font = fit_font(font_path, top_line, width - 16, 18, 10)
    bottom_font = fit_font(font_path, bottom_line, width - 16, 24, 12)
    draw_centered(draw, 8, top_line, top_font, width)
    draw_centered(draw, 35, bottom_line, bottom_font, width)
    return np.asarray(image)


def build_video(
    specs: list[tuple[Path, dict]],
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
    writer = None
    frames_written = 0
    episode_counts: list[dict] = []

    try:
        for idx, ((episode_dir, meta), (top_line, bottom_line)) in enumerate(zip(specs, TASK_LINES), start=1):
            expected_instruction = bottom_line.replace(" -> ", " and place it in the ")
            actual_instruction = " ".join(str(meta.get("instruction") or "").split())
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
                        writer.append_data(draw_label(frame, top_line, bottom_line, font_path))
                        frames_written += 1
                        episode_frames += 1
                        next_keep += speed
            episode_counts.append(
                {
                    "task_index": idx,
                    "episode_dir": str(episode_dir),
                    "label_top": top_line,
                    "label_bottom": bottom_line,
                    "actual_instruction": actual_instruction,
                    "expected_hint": expected_instruction,
                    "frames_written": episode_frames,
                }
            )
            print(f"[INFO] wrote {idx:02d}/10 {episode_dir} as {top_line} / {bottom_line} ({episode_frames} frames)", flush=True)
    finally:
        if writer is not None:
            writer.close()

    summary_path = output.with_suffix(".json")
    summary_path.write_text(
        json.dumps(
            {
                "output": str(output),
                "speed": speed,
                "frames_written": frames_written,
                "episodes": episode_counts,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[DONE] wrote {output} ({frames_written} frames)")
    print(f"[DONE] wrote {summary_path}")


def main() -> None:
    args = parse_args()
    specs = iter_episode_specs(args.reaching_dir, args.pick_place_dir)
    build_video(specs, args.output, args.speed, args.font, args.crf, args.preset, args.force)


if __name__ == "__main__":
    main()
