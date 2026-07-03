#!/usr/bin/env python3
"""Create concatenated success and failure videos from recorded episodes."""

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
    parser.add_argument(
        "collection_dir",
        type=Path,
        nargs="?",
        default=Path("data/raw/pick_place_episodes_1000"),
        help="Directory containing numbered episode folders.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed/summary_videos"),
        help="Directory where output videos are written.",
    )
    parser.add_argument("--speed", type=float, default=5.0, help="Playback speed multiplier.")
    parser.add_argument("--font", type=Path, default=DEFAULT_FONT, help="Font used for overlay text.")
    parser.add_argument("--crf", type=int, default=23, help="x264 CRF for output videos.")
    parser.add_argument("--preset", default="ultrafast", help="x264 preset for output videos.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return parser.parse_args()


def episode_dirs(collection_dir: Path) -> list[Path]:
    episodes = sorted(path for path in collection_dir.iterdir() if path.is_dir() and path.name.isdigit())
    if not episodes:
        raise FileNotFoundError(f"No numbered episode directories found in {collection_dir}")
    return episodes


def load_meta(episode_dir: Path) -> dict:
    meta_path = episode_dir / "meta.json"
    if not meta_path.is_file():
        raise FileNotFoundError(f"Missing metadata file: {meta_path}")
    return json.loads(meta_path.read_text())


def overlay_text(episode_dir: Path, meta: dict) -> str:
    instruction = str(meta.get("instruction") or "").strip()
    text = f"Episode {episode_dir.name}"
    if instruction:
        text = f"{text} | {instruction}"
    return text


def draw_label(frame: np.ndarray, text: str, font: ImageFont.FreeTypeFont) -> np.ndarray:
    image = Image.fromarray(frame)
    draw = ImageDraw.Draw(image, "RGBA")

    x = 12
    y = 12
    padding = 8
    text_bbox = draw.textbbox((x, y), text, font=font)
    box = (
        text_bbox[0] - padding,
        text_bbox[1] - padding,
        text_bbox[2] + padding,
        text_bbox[3] + padding,
    )
    draw.rectangle(box, fill=(0, 0, 0, 170))
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))
    return np.asarray(image)


def build_video(
    label: str,
    episodes: list[tuple[Path, dict]],
    output_dir: Path,
    font: Path,
    speed: float,
    crf: int,
    preset: str,
    force: bool,
) -> Path:
    output_path = output_dir / f"pick_place_{label}_5x.mp4"
    if output_path.exists() and not force:
        print(f"[SKIP] {output_path} already exists; pass --force to regenerate")
        return output_path

    pil_font = ImageFont.truetype(str(font), size=24)
    writer = None
    total = len(episodes)
    frames_written = 0

    try:
        for index, (episode_dir, meta) in enumerate(episodes, start=1):
            input_video = episode_dir / "agent_camera.mp4"
            if not input_video.is_file():
                raise FileNotFoundError(f"Missing video file: {input_video}")

            reader = imageio.get_reader(input_video, "ffmpeg")
            try:
                metadata = reader.get_meta_data()
                fps = float(metadata["fps"])
                if writer is None:
                    writer = imageio.get_writer(
                        output_path,
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

                text = overlay_text(episode_dir, meta)
                next_keep = 0.0
                episode_frames = 0
                for frame_index, frame in enumerate(reader):
                    if frame_index + 1e-9 >= next_keep:
                        writer.append_data(draw_label(frame, text, pil_font))
                        frames_written += 1
                        episode_frames += 1
                        next_keep += speed
            finally:
                reader.close()

            print(
                f"[{label}] wrote {index}/{total}: {episode_dir.name} "
                f"({episode_frames} output frames)",
                flush=True,
            )
    finally:
        if writer is not None:
            writer.close()

    print(f"[DONE] wrote {output_path} ({frames_written} frames)")
    return output_path


def main() -> None:
    args = parse_args()
    if args.speed <= 0:
        raise ValueError("--speed must be positive")
    if not args.font.is_file():
        raise FileNotFoundError(f"Font not found: {args.font}")

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    successes: list[tuple[Path, dict]] = []
    failures: list[tuple[Path, dict]] = []
    for episode_dir in episode_dirs(args.collection_dir):
        meta = load_meta(episode_dir)
        if meta.get("success") is True:
            successes.append((episode_dir, meta))
        elif meta.get("success") is False:
            failures.append((episode_dir, meta))

    print(f"[INFO] successes={len(successes)} failures={len(failures)} speed={args.speed}x")

    build_video(
        "successes",
        successes,
        output_dir,
        args.font,
        args.speed,
        args.crf,
        args.preset,
        args.force,
    )
    build_video(
        "failures",
        failures,
        output_dir,
        args.font,
        args.speed,
        args.crf,
        args.preset,
        args.force,
    )


if __name__ == "__main__":
    main()
