#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np


def normalize_rgb(arr: np.ndarray) -> np.ndarray:
    arr = np.asarray(arr)

    # Remove singleton env dimension if present.
    if arr.ndim == 5 and arr.shape[1] == 1:
        arr = arr[:, 0]

    # Convert CHW to HWC if needed.
    if arr.ndim == 4 and arr.shape[1] in (3, 4) and arr.shape[-1] not in (3, 4):
        arr = np.transpose(arr, (0, 2, 3, 1))

    if arr.ndim != 4:
        raise ValueError(f"Expected video array ndim=4, got shape={arr.shape}")

    if arr.shape[-1] == 4:
        arr = arr[..., :3]

    if arr.dtype != np.uint8:
        if arr.max() <= 1.5:
            arr = arr * 255.0
        arr = np.clip(arr, 0, 255).astype(np.uint8)

    return arr


def find_rgb_keys(npz: np.lib.npyio.NpzFile) -> list[str]:
    keys = list(npz.files)
    candidates = []
    for k in keys:
        lk = k.lower()
        if "rgb" in lk and "depth" not in lk and "seg" not in lk:
            arr = npz[k]
            if arr.ndim in (4, 5):
                candidates.append(k)
    return candidates


def choose_views(keys: list[str]) -> tuple[str, str]:
    low = {k: k.lower() for k in keys}

    wrist = None
    for k, lk in low.items():
        if "wrist" in lk and "rgb" in lk:
            wrist = k
            break

    agent = None
    for k, lk in low.items():
        if any(x in lk for x in ["agent", "front", "external", "scene", "cam"]) and "wrist" not in lk and "rgb" in lk:
            agent = k
            break

    if wrist is None and keys:
        wrist = keys[-1]
    if agent is None:
        for k in keys:
            if k != wrist:
                agent = k
                break

    if agent is None or wrist is None:
        raise RuntimeError(f"Could not choose two RGB views from keys={keys}")

    return agent, wrist


def resize_frame(frame: np.ndarray, h: int, w: int) -> np.ndarray:
    try:
        import cv2
        return cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)
    except Exception:
        # Simple nearest fallback.
        y_idx = np.linspace(0, frame.shape[0] - 1, h).astype(int)
        x_idx = np.linspace(0, frame.shape[1] - 1, w).astype(int)
        return frame[y_idx][:, x_idx]


def add_label(frame: np.ndarray, text: str) -> np.ndarray:
    out = frame.copy()
    try:
        import cv2
        cv2.rectangle(out, (0, 0), (out.shape[1], 24), (0, 0, 0), -1)
        cv2.putText(out, text, (8, 17), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    except Exception:
        pass
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--fps", type=int, default=30)
    args = ap.parse_args()

    ep = Path(args.episode)
    traj = ep / "trajectory.npz"
    meta_path = ep / "meta.json"

    if not traj.exists():
        raise FileNotFoundError(traj)

    meta = {}
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())

    data = np.load(traj, allow_pickle=True)
    rgb_keys = find_rgb_keys(data)
    print("episode:", ep)
    print("npz keys:", data.files)
    print("rgb_keys:", rgb_keys)

    agent_key, wrist_key = choose_views(rgb_keys)
    print("selected_agent_key:", agent_key)
    print("selected_wrist_key:", wrist_key)

    agent = normalize_rgb(data[agent_key])
    wrist = normalize_rgb(data[wrist_key])

    n = min(len(agent), len(wrist))
    agent = agent[:n]
    wrist = wrist[:n]

    h = max(agent.shape[1], wrist.shape[1])
    w = max(agent.shape[2], wrist.shape[2])

    frames = []
    title = f"{meta.get('object_category_id', 'object')}/{meta.get('object_variant_id', '')} success={meta.get('success')}"
    for i in range(n):
        a = resize_frame(agent[i], h, w)
        b = resize_frame(wrist[i], h, w)
        a = add_label(a, f"agent view | {title} | frame {i}")
        b = add_label(b, f"wrist view | {title} | frame {i}")
        frames.append(np.concatenate([a, b], axis=1))

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    try:
        import imageio.v2 as imageio
        imageio.mimsave(out, frames, fps=args.fps, quality=8)
    except Exception:
        import cv2
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(out), fourcc, args.fps, (frames[0].shape[1], frames[0].shape[0]))
        for f in frames:
            writer.write(cv2.cvtColor(f, cv2.COLOR_RGB2BGR))
        writer.release()

    print("saved:", out)
    print("frames:", n)
    print("shape:", frames[0].shape if frames else None)


if __name__ == "__main__":
    main()
