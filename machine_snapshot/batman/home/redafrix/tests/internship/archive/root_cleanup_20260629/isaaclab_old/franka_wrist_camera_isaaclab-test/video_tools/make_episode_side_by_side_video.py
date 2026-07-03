#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np


def norm_rgb(x):
    x = np.asarray(x)

    if x.ndim == 5 and x.shape[1] == 1:
        x = x[:, 0]

    if x.ndim == 4 and x.shape[1] in (3, 4) and x.shape[-1] not in (3, 4):
        x = np.transpose(x, (0, 2, 3, 1))

    if x.ndim != 4:
        raise ValueError(f"Expected RGB video ndim=4, got {x.shape}")

    if x.shape[-1] == 4:
        x = x[..., :3]

    if x.shape[1] == 3 and x.shape[2] != 3: # channel first check
        x = np.transpose(x, (0, 2, 3, 1))

    if x.dtype != np.uint8:
        if x.max() <= 1.5:
            x = x * 255
        x = np.clip(x, 0, 255).astype(np.uint8)

    return x


def resize(frame, h, w):
    try:
        import cv2
        return cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
    except Exception:
        yy = np.linspace(0, frame.shape[0] - 1, h).astype(int)
        xx = np.linspace(0, frame.shape[1] - 1, w).astype(int)
        return frame[yy][:, xx]


def label(frame, text):
    try:
        import cv2
        out = frame.copy()
        cv2.rectangle(out, (0, 0), (out.shape[1], 28), (0, 0, 0), -1)
        cv2.putText(out, text, (6, 19), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        return out
    except Exception:
        return frame


def make_preview(frames, out):
    try:
        if not frames:
            return
        idxs = np.linspace(0, max(0, len(frames) - 1), min(8, len(frames))).astype(int)
        selected = [frames[int(i)] for i in idxs]
        h = min(f.shape[0] for f in selected)
        selected = [f[:h] for f in selected]
        sheet = np.concatenate(selected, axis=1)
        try:
            import imageio.v2 as imageio
            imageio.imwrite(out, sheet)
        except Exception:
            import cv2
            cv2.imwrite(str(out), cv2.cvtColor(sheet, cv2.COLOR_RGB2BGR))
    except Exception as e:
        print("PREVIEW_FAILED", repr(e))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--fps", type=int, default=30)
    args = ap.parse_args()

    ep = Path(args.episode)
    meta_path = ep / "meta.json"
    traj_path = ep / "trajectory.npz"

    meta = json.loads(meta_path.read_text())
    traj = np.load(traj_path, allow_pickle=True)

    if "agent_rgb" not in traj.files or "wrist_rgb" not in traj.files:
        raise RuntimeError(f"Missing agent_rgb/wrist_rgb in {traj_path}; keys={traj.files}")

    agent = norm_rgb(traj["agent_rgb"])
    wrist = norm_rgb(traj["wrist_rgb"])

    n = min(len(agent), len(wrist))
    agent = agent[:n]
    wrist = wrist[:n]

    h = max(agent.shape[1], wrist.shape[1])
    w = max(agent.shape[2], wrist.shape[2])

    obj = f"{meta.get('object_category_id')}/{meta.get('object_variant_id')}"
    goal_type = meta.get("goal_type", "target_area")
    receptacle = f"{meta.get('receptacle_category_id')}/{meta.get('receptacle_variant_id')}" if meta.get("receptacle_category_id") else "none"
    success = meta.get("success")
    instr = str(meta.get("instruction", ""))[:70]

    frames = []
    for i in range(n):
        left = resize(agent[i], h, w)
        right = resize(wrist[i], h, w)

        left = label(left, f"agent | {obj} | success={success} | frame {i}")
        right = label(right, f"wrist | goal={goal_type} | receptacle={receptacle} | {instr}")

        frames.append(np.concatenate([left, right], axis=1))

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    try:
        import imageio.v2 as imageio
        imageio.mimsave(out, frames, fps=args.fps, quality=8)
    except Exception:
        import cv2
        writer = cv2.VideoWriter(str(out), cv2.VideoWriter_fourcc(*"mp4v"), args.fps, (frames[0].shape[1], frames[0].shape[0]))
        for f in frames:
            writer.write(cv2.cvtColor(f, cv2.COLOR_RGB2BGR))
        writer.release()

    preview = out.with_suffix(".preview.jpg")
    make_preview(frames, preview)

    print("VIDEO", out)
    print("PREVIEW", preview)
    print("FRAMES", n)
    print("SUCCESS", success)
    print("OBJECT", obj)
    print("GOAL_TYPE", goal_type)
    print("RECEPTACLE", receptacle)


if __name__ == "__main__":
    main()
