import json
import hashlib
from pathlib import Path
import numpy as np

VIDEO_RUN_DIR = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/002_upstream_master_integration")
OUT_DIR = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs")

runs = [
    {
        "name": "Apple Baseline",
        "episode_dir": OUT_DIR / "master_integration_apple_baseline/000000",
        "video_name": "apple_baseline_integrated_000000_SUCCESS_agent_plus_wrist.mp4",
        "preview_name": "apple_baseline_integrated_000000_SUCCESS_agent_plus_wrist.preview.jpg",
    },
    {
        "name": "Sampled Receptacle",
        "episode_dir": OUT_DIR / "master_integration_sampled_receptacle/000000",
        "video_name": "sampled_receptacle_integrated_000000_SUCCESS_agent_plus_wrist.mp4",
        "preview_name": "sampled_receptacle_integrated_000000_SUCCESS_agent_plus_wrist.preview.jpg",
    },
    {
        "name": "Clutter Smoke",
        "episode_dir": OUT_DIR / "master_integration_clutter/000000",
        "video_name": "clutter_integrated_000000_SUCCESS_agent_plus_wrist.mp4",
        "preview_name": "clutter_integrated_000000_SUCCESS_agent_plus_wrist.preview.jpg",
    }
]

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def get_array_sha256(arr):
    return hashlib.sha256(arr.tobytes()).hexdigest()

results = []
for run in runs:
    meta_path = run["episode_dir"] / "meta.json"
    traj_path = run["episode_dir"] / "trajectory.npz"
    
    meta = json.loads(meta_path.read_text())
    traj = np.load(traj_path, allow_pickle=True)
    
    traj_sha = get_sha256(traj_path)
    first_agent_sha = get_array_sha256(traj["agent_rgb"][0])
    first_wrist_sha = get_array_sha256(traj["wrist_rgb"][0])
    
    results.append({
        "name": run["name"],
        "video": run["video_name"],
        "preview": run["preview_name"],
        "object_variant": f"{meta.get('object_category_id')}/{meta.get('object_variant_id')}",
        "placement_variant": f"{meta.get('placement_target_category_id')}/{meta.get('placement_target_variant_id')}" if meta.get("placement_target_category_id") else "none",
        "object_usd": meta.get("object_usd_path"),
        "placement_usd": meta.get("placement_target_usd_path") or "none",
        "trajectory_sha256": traj_sha,
        "first_agent_frame_sha256": first_agent_sha,
        "first_wrist_frame_sha256": first_wrist_sha,
        "success": meta.get("success"),
    })

# Print console table
print(f"{'Run Name':<20} | {'Object':<18} | {'Receptacle':<18} | {'Success':<8} | {'Traj SHA256':<12}...")
print("-" * 100)
for r in results:
    print(f"{r['name']:<20} | {r['object_variant']:<18} | {r['placement_variant']:<18} | {str(r['success']):<8} | {r['trajectory_sha256'][:10]}...")

# Generate HTML
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Upstream Master Integration Validation Gallery</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #121212; color: #e0e0e0; margin: 30px; }
        h1 { color: #ffffff; text-align: center; margin-bottom: 30px; font-weight: 300; }
        .gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 30px; margin-top: 20px; }
        .card { background-color: #1e1e1e; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid #333; transition: transform 0.2s; }
        .card:hover { transform: translateY(-5px); }
        .preview-img { width: 100%; height: auto; border-bottom: 1px solid #333; display: block; }
        .info { padding: 20px; }
        .run-title { font-size: 1.3em; margin: 0 0 10px 0; color: #00e676; font-weight: 400; }
        .detail { margin: 5px 0; font-size: 0.9em; color: #b0b0b0; }
        .detail strong { color: #ffffff; }
        .btn { display: inline-block; background-color: #2979ff; color: white; padding: 10px 15px; border-radius: 4px; text-decoration: none; font-weight: bold; margin-top: 15px; font-size: 0.9em; }
        .btn:hover { background-color: #2962ff; }
        .badge { display: inline-block; padding: 3px 8px; border-radius: 3px; font-size: 0.8em; font-weight: bold; text-transform: uppercase; }
        .badge-success { background-color: #2e7d32; color: #a5d6a7; }
        .badge-fail { background-color: #c62828; color: #ef9a9a; }
    </style>
</head>
<body>
    <h1>Upstream Master Integration Validation Gallery</h1>
    <div class="gallery">
"""

for r in results:
    badge_class = "badge-success" if r["success"] else "badge-fail"
    status_str = "SUCCESS" if r["success"] else "FAIL"
    
    html_content += f"""
        <div class="card">
            <a href="{r['video']}"><img class="preview-img" src="{r['preview']}" alt="{r['name']} Preview"></a>
            <div class="info">
                <div class="run-title">{r['name']}</div>
                <div class="detail"><strong>Status:</strong> <span class="badge {badge_class}">{status_str}</span></div>
                <div class="detail"><strong>Object Variant:</strong> {r['object_variant']}</div>
                <div class="detail"><strong>Placement Target:</strong> {r['placement_variant']}</div>
                <div class="detail"><strong>Object USD:</strong> {r['object_usd']}</div>
                <div class="detail"><strong>Placement USD:</strong> {r['placement_usd']}</div>
                <div class="detail"><strong>Trajectory SHA:</strong> <code>{r['trajectory_sha256'][:16]}</code></div>
                <div class="detail"><strong>First Agent Frame SHA:</strong> <code>{r['first_agent_frame_sha256'][:16]}</code></div>
                <div class="detail"><strong>First Wrist Frame SHA:</strong> <code>{r['first_wrist_frame_sha256'][:16]}</code></div>
                <a class="btn" href="{r['video']}">Watch MP4 Video</a>
            </div>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

(VIDEO_RUN_DIR / "index.html").write_text(html_content)
print(f"Generated gallery at: {VIDEO_RUN_DIR / 'index.html'}")

# Validate uniqueness of checksums
traj_shas = [r["trajectory_sha256"] for r in results]
first_agent_shas = [r["first_agent_frame_sha256"] for r in results]
first_wrist_shas = [r["first_wrist_frame_sha256"] for r in results]

if len(set(traj_shas)) != len(traj_shas):
    print("WARNING: Duplicate trajectory SHA256 checksums detected!")
else:
    print("SUCCESS: Trajectory checksums are unique.")
    
if len(set(first_agent_shas)) != len(first_agent_shas) or len(set(first_wrist_shas)) != len(first_wrist_shas):
    print("WARNING: Duplicate image frame checksums detected!")
else:
    print("SUCCESS: First frame image checksums are unique.")
