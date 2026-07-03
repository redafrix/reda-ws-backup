#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import numpy as np
import h5py

try:
    import cv2
    HAS_CV2 = True
except Exception:
    HAS_CV2 = False

try:
    import imageio.v2 as imageio
    HAS_IMAGEIO = True
except Exception:
    HAS_IMAGEIO = False


RGB_KEYS = ["wrist_cam_rgb", "side_cam_rgb", "opst_cam_rgb"]
SEG_KEYS = ["wrist_cam_seg", "side_cam_seg", "opst_cam_seg"]


def to_uint8_rgb(arr):
    arr = np.asarray(arr)
    if arr.ndim == 2:
        arr = arr[..., None]
    if arr.shape[-1] == 1:
        arr = np.repeat(arr, 3, axis=-1)
    if arr.dtype != np.uint8:
        arr = np.clip(arr, 0, 255).astype(np.uint8)
    return arr[..., :3]


def colorize_seg(seg):
    seg = np.asarray(seg)
    if seg.ndim == 3 and seg.shape[-1] == 1:
        seg = seg[..., 0]
    if seg.ndim == 3 and seg.shape[-1] == 3:
        return to_uint8_rgb(seg)

    seg = seg.astype(np.int64)
    out = np.zeros((*seg.shape, 3), dtype=np.uint8)

    # Deterministic simple color map.
    out[..., 0] = (seg * 37 + 17) % 255
    out[..., 1] = (seg * 67 + 29) % 255
    out[..., 2] = (seg * 97 + 53) % 255

    # Keep background dark if seg is 0.
    out[seg == 0] = 0
    return out


def resize(img, width=480, height=360):
    img = to_uint8_rgb(img)
    if img.shape[1] == width and img.shape[0] == height:
        return img
    if HAS_CV2:
        return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    # Basic fallback nearest resize
    y_idx = np.linspace(0, img.shape[0] - 1, height).astype(int)
    x_idx = np.linspace(0, img.shape[1] - 1, width).astype(int)
    return img[y_idx][:, x_idx]


def add_label(img, text):
    img = img.copy()
    if HAS_CV2:
        cv2.rectangle(img, (0, 0), (img.shape[1], 32), (0, 0, 0), -1)
        cv2.putText(img, text, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2, cv2.LINE_AA)
    else:
        # Minimal fallback: no text
        pass
    return img


def make_placeholder(text, width=480, height=360):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    if HAS_CV2:
        cv2.putText(img, text, (30, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    return img


def build_frame(h5, idx, include_seg=True, width=480, height=360, title=""):
    top = []
    bottom = []

    for key in RGB_KEYS:
        if key in h5:
            img = resize(h5[key][idx], width, height)
            img = add_label(img, key)
        else:
            img = make_placeholder(f"missing {key}", width, height)
        top.append(img)

    if include_seg:
        for key in SEG_KEYS:
            if key in h5:
                img = colorize_seg(h5[key][idx])
                img = resize(img, width, height)
                img = add_label(img, key)
            else:
                img = make_placeholder(f"missing {key}", width, height)
            bottom.append(img)

    frame = np.concatenate(top, axis=1)
    if include_seg:
        frame2 = np.concatenate(bottom, axis=1)
        frame = np.concatenate([frame, frame2], axis=0)

    if HAS_CV2:
        cv2.rectangle(frame, (0, frame.shape[0] - 34), (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)
        cv2.putText(
            frame,
            f"{title} | frame {idx}",
            (8, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

    return frame


def write_video_cv2(frames, out_path, fps):
    first = frames[0]
    h, w = first.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(out_path), fourcc, fps, (w, h))
    for fr in frames:
        writer.write(cv2.cvtColor(fr, cv2.COLOR_RGB2BGR))
    writer.release()


def write_video_streaming(h5_path, out_path, fps=20, max_frames=None, include_seg=True):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with h5py.File(h5_path, "r") as h5:
        frame_count = None
        for key in RGB_KEYS + SEG_KEYS + ["action"]:
            if key in h5:
                frame_count = h5[key].shape[0]
                break
        if frame_count is None:
            raise RuntimeError(f"No known frame-like keys found in {h5_path}")

        if max_frames is not None:
            frame_count = min(frame_count, max_frames)

        title = Path(h5_path).stem

        print("input:", h5_path)
        print("output:", out_path)
        print("frame_count:", frame_count)
        print("available_keys:", list(h5.keys()))

        if HAS_IMAGEIO:
            with imageio.get_writer(out_path, fps=fps, codec="libx264", quality=8) as writer:
                for i in range(frame_count):
                    frame = build_frame(h5, i, include_seg=include_seg, title=title)
                    writer.append_data(frame)
        elif HAS_CV2:
            # CV2 fallback stores frames temporarily. OK for small videos.
            frames = [build_frame(h5, i, include_seg=include_seg, title=title) for i in range(frame_count)]
            write_video_cv2(frames, out_path, fps)
        else:
            raise RuntimeError("Neither imageio nor cv2 is available. Cannot write MP4.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input H5/HDF5 file")
    parser.add_argument("--output", required=True, help="Output MP4 file")
    parser.add_argument("--fps", type=int, default=20)
    parser.add_argument("--max_frames", type=int, default=None)
    parser.add_argument("--rgb_only", action="store_true")
    args = parser.parse_args()

    write_video_streaming(
        h5_path=args.input,
        out_path=args.output,
        fps=args.fps,
        max_frames=args.max_frames,
        include_seg=not args.rgb_only,
    )


if __name__ == "__main__":
    main()
