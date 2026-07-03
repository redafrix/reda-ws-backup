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
        # Fallback if cv2 is not available or fails
        try:
            import imageio.v2 as imageio
            imageio.imwrite(path, frame)
        except Exception as e:
            print(f"Failed to save image {path}: {e}")

def main():
    run_dir = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation")
    video_run_dir = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/007_smart_strict_collection")
    video_run_dir.mkdir(parents=True, exist_ok=True)
    
    episodes = sorted([d for d in run_dir.iterdir() if d.is_dir() and d.name.isdigit()])
    print(f"Found {len(episodes)} episodes: {[e.name for e in episodes]}")
    
    all_merged_frames = []
    gallery_items = []
    
    for idx, ep in enumerate(episodes):
        traj_path = ep / "trajectory.npz"
        meta_path = ep / "meta.json"
        
        if not traj_path.exists() or not meta_path.exists():
            continue
            
        traj = np.load(traj_path, allow_pickle=True)
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        
        obj = meta.get("object_variant_id", "object")
        rec = meta.get("placement_target_variant_id") or meta.get("receptacle_variant_id") or "receptacle"
        success = "SUCCESS" if meta.get("success", False) else "FAIL"
        
        # Name format: 01_<object>_into_<receptacle>_<SUCCESS_OR_FAIL>.mp4
        prefix = f"{idx + 1:02d}"
        video_name = f"{prefix}_{obj}_into_{rec}_{success}.mp4"
        image_name = f"{prefix}_{obj}_into_{rec}_{success}.jpg"
        
        video_path = video_run_dir / video_name
        image_path = video_run_dir / image_name
        
        agent = norm_rgb(traj["agent_rgb"])
        wrist = norm_rgb(traj["wrist_rgb"])
        n = min(len(agent), len(wrist))
        h = max(agent.shape[1], wrist.shape[1])
        w = max(agent.shape[2], wrist.shape[2])
        
        title = f"Ep {idx+1} | {obj} -> {rec} | {success}"
        
        ep_frames = []
        for i in range(n):
            a = label(resize(agent[i], h, w), f"agent view | {title} | frame {i}")
            b = label(resize(wrist[i], h, w), f"wrist view | {title} | frame {i}")
            combined = np.concatenate([a, b], axis=1)
            ep_frames.append(combined)
            all_merged_frames.append(combined)
            
        print(f"Saving episode {idx+1} video: {video_name}")
        save_video(ep_frames, video_path)
        
        # Generate preview JPG (take the 80% frame showing release)
        preview_idx = int(len(ep_frames) * 0.8)
        save_image(ep_frames[preview_idx], image_path)
        
        gallery_items.append({
            "index": idx + 1,
            "object": obj,
            "receptacle": rec,
            "success": success,
            "video": video_name,
            "preview": image_name,
            "frames": n
        })

    # Save merged 6-episode video
    merged_path = video_run_dir / "merged_6episodes_smart_collection.mp4"
    print(f"Saving merged 6-episode video to {merged_path}...")
    save_video(all_merged_frames, merged_path)
    
    # Generate interactive HTML gallery
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Smart strict collection - 6 Episodes Validation</title>
    <style>
        body {{
            background: #111;
            color: #eee;
            font-family: 'Outfit', sans-serif;
            margin: 0;
            padding: 24px;
        }}
        h1 {{
            color: #fff;
            text-align: center;
            margin-bottom: 8px;
        }}
        .subtitle {{
            text-align: center;
            color: #888;
            margin-bottom: 32px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .card {{
            background: #222;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: translateY(-4px);
        }}
        .media-container {{
            position: relative;
            cursor: pointer;
            aspect-ratio: 2 / 1;
            background: #000;
        }}
        .media-container img, .media-container video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}
        .media-container video {{
            display: none;
        }}
        .info {{
            padding: 16px;
        }}
        .title {{
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 8px;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .badge.success {{
            background: #1e4620;
            color: #a3e635;
        }}
        .badge.fail {{
            background: #7f1d1d;
            color: #fca5a5;
        }}
        .merged-video-card {{
            grid-column: 1 / -1;
            background: #1a1a1a;
            border: 1px solid #333;
            margin-bottom: 24px;
            text-align: center;
            padding: 24px;
            border-radius: 8px;
        }}
        .merged-video-card video {{
            max-width: 800px;
            width: 100%;
            border-radius: 8px;
        }}
    </style>
    <script>
        function playVideo(container) {{
            const img = container.querySelector('img');
            const video = container.querySelector('video');
            img.style.display = 'none';
            video.style.display = 'block';
            video.play();
        }}
        function stopVideo(container) {{
            const img = container.querySelector('img');
            const video = container.querySelector('video');
            video.pause();
            video.style.display = 'none';
            img.style.display = 'block';
        }}
    </script>
</head>
<body>
    <h1>Strict Multi-Episode Validation Gallery</h1>
    <p class="subtitle">6 consecutive episodes collected in strict receptacle mode</p>
    
    <div class="grid">
        <div class="merged-video-card">
            <h2>Merged 6-Episode Collection Video</h2>
            <video controls poster="{gallery_items[0]['preview']}">
                <source src="merged_6episodes_smart_collection.mp4" type="video/pipe">
                <source src="merged_6episodes_smart_collection.mp4" type="video/mp4">
            </video>
        </div>
        
        {"".join(f'''
        <div class="card">
            <div class="media-container" onmouseenter="playVideo(this)" onmouseleave="stopVideo(this)">
                <img src="{item['preview']}" alt="Episode {item['index']}">
                <video muted loop playsinline>
                    <source src="{item['video']}" type="video/mp4">
                </video>
            </div>
            <div class="info">
                <div class="title">Episode {item['index']}: {item['object']} &rarr; {item['receptacle']}</div>
                <div><span class="badge {item['success'].lower()}">{item['success']}</span> &bull; {item['frames']} frames</div>
            </div>
        </div>
        ''' for item in gallery_items)}
    </div>
</body>
</html>
"""
    
    html_path = video_run_dir / "index.html"
    html_path.write_text(html_content, encoding='utf-8')
    print(f"Gallery written to {html_path}")

if __name__ == "__main__":
    main()
