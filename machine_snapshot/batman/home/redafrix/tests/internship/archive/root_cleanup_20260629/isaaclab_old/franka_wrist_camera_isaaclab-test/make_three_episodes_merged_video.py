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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run_dir", required=True, help="Directory containing the episodes (e.g. 000000, 000001, 000002)")
    ap.add_argument("--output", required=True, help="Path to output the merged MP4 video")
    ap.add_argument("--fps", type=int, default=30)
    args = ap.parse_args()

    run_dir = Path(args.run_dir)
    episodes = sorted([d for d in run_dir.iterdir() if d.is_dir() and d.name.isdigit()])
    print(f"Found {len(episodes)} episodes: {[e.name for e in episodes]}")

    all_frames = []
    
    for ep_idx, ep in enumerate(episodes):
        traj_path = ep / "trajectory.npz"
        meta_path = ep / "meta.json"
        
        if not traj_path.exists() or not meta_path.exists():
            print(f"Skipping {ep.name}: trajectory.npz or meta.json missing")
            continue
            
        print(f"Processing episode {ep.name}...")
        traj = np.load(traj_path, allow_pickle=True)
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        
        agent = norm_rgb(traj["agent_rgb"])
        wrist = norm_rgb(traj["wrist_rgb"])
        n = min(len(agent), len(wrist))
        h = max(agent.shape[1], wrist.shape[1])
        w = max(agent.shape[2], wrist.shape[2])
        
        title = f"Ep {ep.name} | {meta.get('object_category_id')}/{meta.get('object_variant_id')} success={meta.get('success')}"
        
        for i in range(n):
            a = label(resize(agent[i], h, w), f"agent view | {title} | frame {i}")
            b = label(resize(wrist[i], h, w), f"wrist view | {title} | frame {i}")
            all_frames.append(np.concatenate([a, b], axis=1))

    if not all_frames:
        print("No frames found to save!")
        return

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Saving {len(all_frames)} frames to {out}...")
    try:
        import imageio.v2 as imageio
        imageio.mimsave(out, all_frames, fps=args.fps, quality=8)
    except Exception as e:
        print(f"imageio failed ({e}), falling back to cv2.VideoWriter")
        import cv2
        writer = cv2.VideoWriter(str(out), cv2.VideoWriter_fourcc(*"mp4v"), args.fps, (all_frames[0].shape[1], all_frames[0].shape[0]))
        for f in all_frames:
            writer.write(cv2.cvtColor(f, cv2.COLOR_RGB2BGR))
        writer.release()
        
    print("Done! Merged video saved.")

if __name__ == "__main__":
    main()
