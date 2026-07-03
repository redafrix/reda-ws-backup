import os
import sys
import subprocess
import time
import json
import hashlib
from pathlib import Path
import numpy as np

WS = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test")
REPO = WS / "franka_wrist_camera_isaaclab"
REPORTS = WS / "reports"
LOGS = WS / "logs"
OUT = WS / "outputs"
VIDEO_BASE = OUT / "object_test_videos"
TOOLS = WS / "video_tools"
ISAACLAB_ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab")
REPORT = REPORTS / "DIVERSE_OBJECT_RECEPTACLE_MATRIX_REPORT.md"
VIDEO_RUN_DIR = VIDEO_BASE / "004_diverse_object_receptacle_matrix"

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def cleanup_processes():
    print("[Orchestrator] Cleaning up stale Isaac Sim processes...", flush=True)
    user = os.environ.get("USER", "")
    out = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")
    
    pids = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 1)
        if len(parts) < 2:
            continue
        pid_s, args = parts
        if not pid_s.isdigit():
            continue
        pid = int(pid_s)
        if pid == os.getpid() or pid == os.getppid():
            continue
            
        if any(k in args for k in ["isaac-sim", "isaacsim", "kit/kit", "omni.kit", "collect.py"]) and \
           any(k in args for k in ["isaac_dynamicVLA-test", "franka_wrist_camera_isaaclab-test", "/home/redafrix/isaacsim"]):
            pids.append(pid)
            
    if pids:
        print(f"[Orchestrator] Stopping relevant PIDs: {pids}", flush=True)
        for pid in pids:
            try:
                os.kill(pid, 2)
            except ProcessLookupError:
                pass
        time.sleep(8)
        
        out2 = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")
        remaining = []
        for line in out2.splitlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split(None, 1)
            if len(parts) < 2:
                continue
            pid_s, args = parts
            if not pid_s.isdigit():
                continue
            pid = int(pid_s)
            if pid in pids:
                remaining.append(pid)
                
        if remaining:
            print(f"[Orchestrator] Force killing remaining PIDs: {remaining}", flush=True)
            for pid in remaining:
                try:
                    os.kill(pid, 9)
                except ProcessLookupError:
                    pass
            time.sleep(5)

configs = [
    ("01", "pair1_apple_bowl.yaml", "pair1_apple_bowl", "apple01", "bowl08"),
    ("02", "pair2_avocado_bowl.yaml", "pair2_avocado_bowl", "avocado02", "bowl01"),
    ("03", "pair3_can_tray.yaml", "pair3_can_tray", "fcan03", "tray04"),
    ("04", "pair4_box_bowl.yaml", "pair4_box_bowl", "onion00", "bowl07"),
    ("05", "pair5_kiwi_bowl.yaml", "pair5_kiwi_bowl", "kiwi00", "bowl10"),
    ("06", "pair6_beer_box.yaml", "pair6_beer_box", "lime00", "box00"),
]

results = []

for prefix, cfg_name, out_dir_name, obj_var, rec_var in configs:
    cfg_path = REPO / f"configs/diversity_validation/{cfg_name}"
    run_out_dir = OUT / out_dir_name
    
    print(f"\n========================================\nRunning {cfg_name}...\n========================================", flush=True)
    
    cleanup_processes()
    
    if run_out_dir.exists():
        print(f"[Orchestrator] Removing existing output directory: {run_out_dir}", flush=True)
        subprocess.run(["rm", "-rf", str(run_out_dir)], check=True)
        
    env = os.environ.copy()
    env["TERM"] = "xterm-256color"
    env["PYTHONPATH"] = str(REPO / "src")
    
    log_file = LOGS / f"matrix_{cfg_name.replace('.yaml', '.log')}"
    cmd = [
        str(ISAACLAB_ROOT / "isaaclab.sh"),
        "-p", "scripts/collect.py",
        "--headless",
        "--collection_config", f"diversity_validation/{cfg_name}",
        "--output_dir", str(run_out_dir)
    ]
    
    print(f"[Orchestrator] Executing command: {' '.join(cmd)}", flush=True)
    print(f"[Orchestrator] Logs redirected to: {log_file}", flush=True)
    
    t0 = time.time()
    with open(log_file, "w", encoding="utf-8") as lf:
        proc = subprocess.run(cmd, cwd=str(REPO), env=env, stdout=lf, stderr=subprocess.STDOUT, timeout=1800)
        
    duration = time.time() - t0
    exit_status = proc.returncode
    print(f"[Orchestrator] Exit status: {exit_status} (took {duration:.1f}s)", flush=True)
    
    meta_path = run_out_dir / "000000/meta.json"
    traj_path = run_out_dir / "000000/trajectory.npz"
    
    if not meta_path.exists() or not traj_path.exists():
        print(f"[ERROR] Outputs not written for {cfg_name}!", flush=True)
        results.append({
            "prefix": prefix,
            "cfg_name": cfg_name,
            "success": False,
            "error": "Outputs missing",
            "exit_status": exit_status
        })
        continue
        
    meta = json.loads(meta_path.read_text())
    is_success = meta.get("success", False)
    
    traj = np.load(traj_path, allow_pickle=True)
    if "agent_rgb" not in traj.files or "wrist_rgb" not in traj.files:
        print(f"[ERROR] Missing rgb arrays in trajectory for {cfg_name}!", flush=True)
        results.append({
            "prefix": prefix,
            "cfg_name": cfg_name,
            "success": False,
            "error": "Missing arrays in trajectory",
            "exit_status": exit_status
        })
        continue
        
    success_label = "SUCCESS" if is_success else "FAIL"
    video_name = f"{prefix}_{obj_var}_into_{rec_var}_{success_label}_agent_plus_wrist.mp4"
    video_path = VIDEO_RUN_DIR / video_name
    preview_path = VIDEO_RUN_DIR / f"{prefix}_{obj_var}_into_{rec_var}_{success_label}_agent_plus_wrist.preview.jpg"
    
    video_cmd = [
        "python3", str(TOOLS / "make_episode_side_by_side_video.py"),
        "--episode", str(run_out_dir / "000000"),
        "--output", str(video_path),
        "--fps", "30"
    ]
    print(f"[Orchestrator] Generating video: {' '.join(video_cmd)}", flush=True)
    subprocess.run(video_cmd, check=True)
    
    traj_hash = sha256_file(traj_path)
    meta_hash = sha256_file(meta_path)
    video_hash = sha256_file(video_path)
    
    agent_rgb = traj["agent_rgb"]
    wrist_rgb = traj["wrist_rgb"]
    agent_first_frame_hash = sha256_bytes(agent_rgb[0].tobytes())
    wrist_first_frame_hash = sha256_bytes(wrist_rgb[0].tobytes())
    
    results.append({
        "prefix": prefix,
        "cfg_name": cfg_name,
        "success": is_success,
        "exit_status": exit_status,
        "instruction": meta.get("instruction"),
        "success_metric": meta.get("success_metric"),
        "object_category_id": meta.get("object_category_id"),
        "object_variant_id": meta.get("object_variant_id"),
        "object_usd_path": meta.get("object_usd_path"),
        "placement_target_category_id": meta.get("placement_target_category_id"),
        "placement_target_variant_id": meta.get("placement_target_variant_id"),
        "placement_target_usd_path": meta.get("placement_target_usd_path"),
        "object_pos_local": meta.get("object_pos_local"),
        "place_pos_local": meta.get("place_pos_local"),
        "placement_target_pos_local": meta.get("placement_target_pos_local"),
        "trajectory_hash": traj_hash,
        "meta_hash": meta_hash,
        "video_hash": video_hash,
        "agent_first_frame_hash": agent_first_frame_hash,
        "wrist_first_frame_hash": wrist_first_frame_hash,
        "video_path": str(video_path),
        "preview_path": str(preview_path),
    })

with open(REPORT, "a", encoding="utf-8") as f:
    f.write("\n## Step 5 & 6 — Diverse Matrix Results\n\n")
    
    for r in results:
        f.write(f"### Run {r['prefix']}: {r['cfg_name']}\n")
        if "error" in r:
            f.write(f"- **Status**: FAILED TO RUN ({r['error']})\n")
            f.write(f"- **Exit Status**: {r['exit_status']}\n\n")
            continue
            
        f.write(f"- **Instruction**: {r['instruction']}\n")
        f.write(f"- **Success**: {r['success']}\n")
        f.write(f"- **Success Metric**: {r['success_metric']}\n")
        f.write(f"- **Object Category**: {r['object_category_id']}\n")
        f.write(f"- **Object Variant**: {r['object_variant_id']}\n")
        f.write(f"- **Object USD Path**: {r['object_usd_path']}\n")
        f.write(f"- **Placement Target Category**: {r['placement_target_category_id']}\n")
        f.write(f"- **Placement Target Variant**: {r['placement_target_variant_id']}\n")
        f.write(f"- **Placement Target USD Path**: {r['placement_target_usd_path']}\n")
        f.write(f"- **Object Position (Local)**: {r['object_pos_local']}\n")
        f.write(f"- **Placement-Target Position (Local)**: {r['placement_target_pos_local']}\n")
        f.write(f"- **Place Position (Local)**: {r['place_pos_local']}\n")
        f.write(f"- **Trajectory SHA256**: {r['trajectory_hash']}\n")
        f.write(f"- **Agent First-Frame SHA256**: {r['agent_first_frame_hash']}\n")
        f.write(f"- **Wrist First-Frame SHA256**: {r['wrist_first_frame_hash']}\n")
        f.write(f"- **Video Path**: {r['video_path']}\n")
        f.write(f"- **Preview Path**: {r['preview_path']}\n\n")

print("[Orchestrator] Running diversity validation checks...", flush=True)
all_ok = True
validation_errors = []

traj_hashes = [r['trajectory_hash'] for r in results if 'trajectory_hash' in r]
agent_ff_hashes = [r['agent_first_frame_hash'] for r in results if 'agent_first_frame_hash' in r]
wrist_ff_hashes = [r['wrist_first_frame_hash'] for r in results if 'wrist_first_frame_hash' in r]

if len(traj_hashes) != len(set(traj_hashes)):
    msg = f"ERROR: Identical trajectory hashes found: {traj_hashes}"
    validation_errors.append(msg)
    all_ok = False
if len(agent_ff_hashes) != len(set(agent_ff_hashes)):
    msg = f"ERROR: Identical agent first-frame hashes found: {agent_ff_hashes}"
    validation_errors.append(msg)
    all_ok = False
if len(wrist_ff_hashes) != len(set(wrist_ff_hashes)):
    msg = f"ERROR: Identical wrist first-frame hashes found: {wrist_ff_hashes}"
    validation_errors.append(msg)
    all_ok = False

obj_variants = [r['object_variant_id'] for r in results if 'object_variant_id' in r]
rec_variants = [r['placement_target_variant_id'] for r in results if 'placement_target_variant_id' in r]

if len(obj_variants) != len(set(obj_variants)):
    msg = f"ERROR: Duplicate object variants found: {obj_variants}"
    validation_errors.append(msg)
    all_ok = False
if len(rec_variants) != len(set(rec_variants)):
    msg = f"ERROR: Duplicate receptacle variants found: {rec_variants}"
    validation_errors.append(msg)
    all_ok = False

with open(REPORT, "a", encoding="utf-8") as f:
    f.write("\n## Step 6 — Diversity Validation Checks\n\n")
    if all_ok:
        f.write("- **Validation Status**: PASSED\n")
        f.write("- **Checks**: All trajectory and camera hashes are distinct. All object/receptacle variants are distinct.\n")
    else:
        f.write("- **Validation Status**: FAILED\n")
        for err in validation_errors:
            f.write(f"- {err}\n")

if not all_ok:
    print(f"[ERROR] Diversity validation failed! Errors:\n" + "\n".join(validation_errors), flush=True)
    sys.exit(1)
else:
    print("[Orchestrator] All validation checks passed successfully!", flush=True)
