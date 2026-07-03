from pathlib import Path
import argparse, json
import numpy as np

def norm_rgb(x):
    x = np.asarray(x)
    if x.ndim == 5 and x.shape[1] == 1:
        x = x[:, 0]
    if x.ndim == 4 and x.shape[1] in (3, 4) and x.shape[-1] not in (3, 4):
        x = np.transpose(x, (0, 2, 3, 1))
    if x.shape[-1] == 4:
        x = x[..., :3]
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
        yy = np.linspace(0, frame.shape[0]-1, h).astype(int)
        xx = np.linspace(0, frame.shape[1]-1, w).astype(int)
        return frame[yy][:, xx]

def label(frame, text):
    try:
        import cv2
        out = frame.copy()
        cv2.rectangle(out, (0,0), (out.shape[1],24), (0,0,0), -1)
        cv2.putText(out, text, (6,17), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)
        return out
    except Exception:
        return frame

ap = argparse.ArgumentParser()
ap.add_argument("--episode", required=True)
ap.add_argument("--output", required=True)
ap.add_argument("--fps", type=int, default=30)
args = ap.parse_args()

ep = Path(args.episode)
traj = np.load(ep / "trajectory.npz", allow_pickle=True)
meta = json.loads((ep / "meta.json").read_text())

agent = norm_rgb(traj["agent_rgb"])
wrist = norm_rgb(traj["wrist_rgb"])
n = min(len(agent), len(wrist))
h = max(agent.shape[1], wrist.shape[1])
w = max(agent.shape[2], wrist.shape[2])

frames = []
title = f"{meta.get('object_category_id')}/{meta.get('object_variant_id')} success={meta.get('success')}"
for i in range(n):
    a = label(resize(agent[i], h, w), f"agent view | {title} | frame {i}")
    b = label(resize(wrist[i], h, w), f"wrist view | {title} | frame {i}")
    frames.append(np.concatenate([a, b], axis=1))

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

print(out)
print("frames", n)
