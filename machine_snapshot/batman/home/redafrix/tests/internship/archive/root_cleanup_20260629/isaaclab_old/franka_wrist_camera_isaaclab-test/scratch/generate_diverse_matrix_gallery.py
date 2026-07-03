import json
import hashlib
from pathlib import Path

VIDEO_RUN_DIR = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/004_diverse_object_receptacle_matrix")
OUT_DIR = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs")

runs = [
    ("01", "pair1_apple_bowl", "apple01", "bowl08"),
    ("02", "pair2_avocado_bowl", "avocado02", "bowl01"),
    ("03", "pair3_can_tray", "fcan03", "tray04"),
    ("04", "pair4_box_bowl", "onion00", "bowl07"),
    ("05", "pair5_kiwi_bowl", "kiwi00", "bowl10"),
    ("06", "pair6_beer_box", "lime00", "box00"),
    ("07", "master_integration_apple_baseline", "apple01", "baseline"),
]

results = []
for prefix, out_dir_name, obj_var, rec_var in runs:
    episode_dir = OUT_DIR / out_dir_name / "000000"
    meta_path = episode_dir / "meta.json"
    if not meta_path.exists():
        continue
        
    meta = json.loads(meta_path.read_text())
    is_success = meta.get("success", False)
    success_label = "SUCCESS" if is_success else "FAIL"
    
    if prefix == "07":
        video_name = f"{prefix}_{obj_var}_baseline_{success_label}_agent_plus_wrist.mp4"
        preview_name = f"{prefix}_{obj_var}_baseline_{success_label}_agent_plus_wrist.preview.jpg"
        run_title = f"Run {prefix}: {obj_var} Baseline"
    else:
        video_name = f"{prefix}_{obj_var}_into_{rec_var}_{success_label}_agent_plus_wrist.mp4"
        preview_name = f"{prefix}_{obj_var}_into_{rec_var}_{success_label}_agent_plus_wrist.preview.jpg"
        run_title = f"Run {prefix}: {obj_var} into {rec_var}"
    
    results.append({
        "prefix": prefix,
        "name": run_title,
        "video": video_name,
        "preview": preview_name,
        "instruction": meta.get("instruction", ""),
        "object_variant": f"{meta.get('object_category_id')}/{meta.get('object_variant_id')}",
        "placement_variant": f"{meta.get('placement_target_category_id')}/{meta.get('placement_target_variant_id')}" if meta.get("placement_target_category_id") else "none",
        "object_usd": meta.get("object_usd_path"),
        "placement_usd": meta.get("placement_target_usd_path") or "none",
        "success": is_success,
        "meta_path": str(meta_path),
    })

# Generate HTML
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Diverse Object & Receptacle Matrix Gallery</title>
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
    <h1>Diverse Object & Receptacle Matrix Gallery</h1>
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
                <div class="detail"><strong>Instruction:</strong> {r['instruction']}</div>
                <div class="detail"><strong>Object:</strong> {r['object_variant']}</div>
                <div class="detail"><strong>Receptacle:</strong> {r['placement_variant']}</div>
                <div class="detail"><strong>Object USD:</strong> {r['object_usd']}</div>
                <div class="detail"><strong>Placement USD:</strong> {r['placement_usd']}</div>
                <div class="detail"><strong>Metadata Path:</strong> <code>{r['meta_path']}</code></div>
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
