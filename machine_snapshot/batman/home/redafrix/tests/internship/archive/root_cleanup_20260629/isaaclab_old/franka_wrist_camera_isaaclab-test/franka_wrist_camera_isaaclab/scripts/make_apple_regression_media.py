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

def save_video(frames, path, fps=30):
    try:
        import imageio.v2 as imageio
        imageio.mimsave(path, frames, fps=fps, quality=8)
    except Exception as e:
        print(f"imageio failed ({e}), falling back to cv2.VideoWriter")
        import cv2
        writer = cv2.VideoWriter(str(path), cv2.VideoWriter_fourcc(*"mp4v"), fps, (frames[0].shape[1], frames[0].shape[0]))
        for f in frames:
            writer.write(cv2.cvtColor(f, cv2.COLOR_RGB2BGR))
        writer.release()

def save_image(frame, path):
    try:
        import cv2
        cv2.imwrite(str(path), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    except Exception:
        try:
            import imageio.v2 as imageio
            imageio.imwrite(path, frame)
        except Exception as e:
            print(f"Failed to save image {path}: {e}")

def main():
    ep_dir = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/apple_regression_smart/000000")
    video_run_dir = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/007_smart_strict_collection")
    
    traj_path = ep_dir / "trajectory.npz"
    meta_path = ep_dir / "meta.json"
    
    if not traj_path.exists() or not meta_path.exists():
        print("Error: trajectory.npz or meta.json not found for apple regression")
        return
        
    traj = np.load(traj_path, allow_pickle=True)
    meta = json.loads(meta_path.read_text(encoding='utf-8'))
    
    obj = meta.get("object_variant_id", "apple01")
    rec = "None"
    success = "SUCCESS" if meta.get("success", False) else "FAIL"
    
    video_name = f"apple_regression_{obj}_into_{rec}_{success}.mp4"
    image_name = f"apple_regression_{obj}_into_{rec}_{success}.jpg"
    
    video_path = video_run_dir / video_name
    image_path = video_run_dir / image_name
    
    agent = norm_rgb(traj["agent_rgb"])
    wrist = norm_rgb(traj["wrist_rgb"])
    n = min(len(agent), len(wrist))
    h = max(agent.shape[1], wrist.shape[1])
    w = max(agent.shape[2], wrist.shape[2])
    
    title = f"Apple Regression | {obj} -> {rec} | {success}"
    
    frames = []
    for i in range(n):
        a = label(resize(agent[i], h, w), f"agent view | {title} | frame {i}")
        b = label(resize(wrist[i], h, w), f"wrist view | {title} | frame {i}")
        frames.append(np.concatenate([a, b], axis=1))
        
    print(f"Saving apple regression video: {video_name}")
    save_video(frames, video_path)
    
    preview_idx = int(len(frames) * 0.8)
    save_image(frames[preview_idx], image_path)
    print("Done compiling apple regression media.")

if __name__ == "__main__":
    main()
