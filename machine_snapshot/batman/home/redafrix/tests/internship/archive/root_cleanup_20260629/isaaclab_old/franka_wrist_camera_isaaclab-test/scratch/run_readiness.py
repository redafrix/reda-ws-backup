#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import json
import hashlib
from pathlib import Path
from datetime import datetime
import numpy as np

WS = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test")
REPO = WS / "franka_wrist_camera_isaaclab"
REPORTS = WS / "reports"
LOGS = WS / "logs"
OUT = WS / "outputs"
VIDEO_BASE = OUT / "object_test_videos"
TOOLS = WS / "video_tools"
ISAACLAB_ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab")
REPORT_PATH = REPORTS / "FINAL_DATASET_READINESS_VALIDATION_REPORT.md"

# Determine VIDEO_RUN_DIR (e.g. 006_final_dataset_readiness)
last_num = 0
for p in VIDEO_BASE.glob("*_final_dataset_readiness"):
    if p.is_dir():
        try:
            num = int(p.name.split("_")[0])
            if num > last_num:
                last_num = num
        except Exception:
            pass
next_num = last_num if last_num > 0 else 6
VIDEO_RUN_DIR = VIDEO_BASE / f"{next_num:03d}_final_dataset_readiness"
VIDEO_RUN_DIR.mkdir(parents=True, exist_ok=True)

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()[:16]

def cleanup_relevant_isaac_processes():
    """Kill relevant stale Isaac Sim / Kit processes from this workspace."""
    user = os.environ.get("USER", "")
    try:
        out = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")
    except Exception:
        return

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
        print(f"[Orchestrator] Stopping stale processes: {pids}", flush=True)
        for pid in pids:
            try:
                os.kill(pid, 2)  # SIGINT
            except ProcessLookupError:
                pass
        time.sleep(8)

        # Check for remaining
        try:
            out2 = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")
        except Exception:
            return
        remaining = []
        for line in out2.splitlines():
            line = line.strip()
            parts = line.split(None, 1)
            if len(parts) < 2:
                continue
            pid_s = parts[0]
            if pid_s.isdigit() and int(pid_s) in pids:
                remaining.append(int(pid_s))
        if remaining:
            print(f"[Orchestrator] Force killing remaining processes: {remaining}", flush=True)
            for pid in remaining:
                try:
                    os.kill(pid, 9)  # SIGKILL
                except ProcessLookupError:
                    pass
            time.sleep(5)

def run_episode(cfg_name: str, out_dir: Path, log_name: str) -> dict:
    """Run a single episode and return result metadata."""
    meta_path = out_dir / "000000/meta.json"
    traj_path = out_dir / "000000/trajectory.npz"
    log_file = LOGS / f"{log_name}.log"

    if meta_path.exists() and traj_path.exists():
        print(f"\n[Orchestrator] Found cached output for {cfg_name}, skipping simulation.", flush=True)
        exit_status = 0
        duration = 0.0
    else:
        cleanup_relevant_isaac_processes()

        if out_dir.exists():
            subprocess.run(["rm", "-rf", str(out_dir)], check=True)

        env = os.environ.copy()
        env["TERM"] = "xterm-256color"
        env["PYTHONPATH"] = str(REPO / "src")

        cmd = [
            str(ISAACLAB_ROOT / "isaaclab.sh"),
            "-p", "scripts/collect.py",
            "--headless",
            "--collection_config", f"final_readiness_validation/{cfg_name}",
            "--output_dir", str(out_dir)
        ]

        print(f"\n[Orchestrator] Running: {cfg_name}", flush=True)
        print(f"[Orchestrator] Command: {' '.join(cmd)}", flush=True)
        print(f"[Orchestrator] Log: {log_file}", flush=True)

        t0 = time.time()
        try:
            with open(log_file, "w", encoding="utf-8") as lf:
                proc = subprocess.run(cmd, cwd=str(REPO), env=env, stdout=lf, stderr=subprocess.STDOUT, timeout=1800)
            exit_status = proc.returncode
        except subprocess.TimeoutExpired:
            exit_status = -1
            print(f"[ERROR] Timeout for {cfg_name}!", flush=True)
        duration = time.time() - t0

        print(f"[Orchestrator] Exit: {exit_status} ({duration:.1f}s)", flush=True)

    result = {
        "cfg_name": cfg_name,
        "exit_status": exit_status,
        "duration_s": round(duration, 1),
        "log_file": str(log_file),
    }

    if not meta_path.exists() or not traj_path.exists():
        result["error"] = "Outputs missing"
        print(f"[ERROR] Outputs not written for {cfg_name}!", flush=True)
        return result

    meta = json.loads(meta_path.read_text())
    result["success"] = meta.get("success", False)
    result["instruction"] = meta.get("instruction")
    result["success_metric"] = meta.get("success_metric")
    result["object_variant_id"] = meta.get("object_variant_id")
    result["object_category_id"] = meta.get("object_category_id")
    result["placement_target_variant_id"] = meta.get("placement_target_variant_id")
    result["placement_target_category_id"] = meta.get("placement_target_category_id")
    result["object_pos_local"] = meta.get("object_pos_local")
    result["place_pos_local"] = meta.get("place_pos_local")
    result["placement_target_pos_local"] = meta.get("placement_target_pos_local")
    result["seed"] = meta.get("seed")
    result["num_steps"] = meta.get("num_steps")
    result["num_camera_frames"] = meta.get("num_camera_frames")

    # Validate trajectory
    try:
        traj = np.load(traj_path, allow_pickle=True)
        has_agent = "agent_rgb" in traj.files
        has_wrist = "wrist_rgb" in traj.files
        result["has_agent_rgb"] = has_agent
        result["has_wrist_rgb"] = has_wrist
        if has_agent:
            result["agent_rgb_shape"] = list(traj["agent_rgb"].shape)
        if has_wrist:
            result["wrist_rgb_shape"] = list(traj["wrist_rgb"].shape)
    except Exception as e:
        result["error"] = f"Trajectory load failed: {e}"
        return result

    if not has_agent or not has_wrist:
        result["error"] = "Missing RGB arrays in trajectory"
        return result

    result["trajectory_hash"] = sha256_file(traj_path)
    result["meta_hash"] = sha256_file(meta_path)
    result["episode_dir"] = str(out_dir / "000000")

    # Programmatic Physical Quality Audit
    audit_status = "ACCEPTED"
    failure_stage = ""
    
    if not result.get("success"):
        audit_status = "FAILED"
        failure_stage = "task_failure"
    else:
        # Check for teleportation and table/receptacle penetration
        try:
            o_pos = traj["object_pos_w"] # shape: (num_steps, 1, 3) or (num_steps, 3)
            if o_pos.ndim == 3:
                o_pos = o_pos[:, 0]
            
            # 1. Teleportation check (position jump > 0.25m per step)
            diffs = np.linalg.norm(np.diff(o_pos, axis=0), axis=1)
            max_jump = float(np.max(diffs))
            result["max_position_jump_m"] = round(max_jump, 4)
            if max_jump > 0.25:
                audit_status = "TECHNICALLY_SUCCESSFUL_BUT_VISUALLY_BAD"
                failure_stage = "teleportation"
                print(f"[Warning] Object teleported! Max jump={max_jump:.3f}m", flush=True)
            
            # 2. Table penetration check (Z coordinate goes below table height 1.00m)
            min_z = float(np.min(o_pos[:, 2]))
            result["min_z_coordinate_m"] = round(min_z, 4)
            if min_z < 1.00:
                audit_status = "TECHNICALLY_SUCCESSFUL_BUT_VISUALLY_BAD"
                if not failure_stage:
                    failure_stage = "table_penetration"
                print(f"[Warning] Object penetrated table! Min Z={min_z:.3f}m", flush=True)

        except Exception as e:
            print(f"[ERROR] Quality audit crashed: {e}", flush=True)
            audit_status = "ERROR"
            failure_stage = "audit_crash"

    result["physical_classification"] = audit_status
    result["failure_stage"] = failure_stage
    return result

def generate_video(result: dict, custom_name: str) -> dict:
    """Generate side-by-side video and preview using workspace tool."""
    if "error" in result or "episode_dir" not in result:
        return result

    video_path = VIDEO_RUN_DIR / f"{custom_name}.mp4"
    preview_path = VIDEO_RUN_DIR / f"{custom_name}.preview.jpg"

    if video_path.exists() and preview_path.exists():
        print(f"[Orchestrator] Found cached video for {custom_name}, skipping generation.", flush=True)
        result["video_path"] = str(video_path)
        result["preview_path"] = str(preview_path)
        result["video_hash"] = sha256_file(video_path)
        result["preview_hash"] = sha256_file(preview_path)
        return result

    cmd = [
        "python3", str(TOOLS / "make_episode_side_by_side_video.py"),
        "--episode", result["episode_dir"],
        "--output", str(video_path),
        "--fps", "30"
    ]

    print(f"[Orchestrator] Generating video: {custom_name}", flush=True)
    try:
        subprocess.run(cmd, check=True, timeout=300)
        result["video_path"] = str(video_path)
        result["preview_path"] = str(preview_path)
        if video_path.exists():
            result["video_hash"] = sha256_file(video_path)
        if preview_path.exists():
            result["preview_hash"] = sha256_file(preview_path)
        print(f"[Orchestrator] Video OK: {video_path.name}", flush=True)
    except Exception as e:
        result["video_error"] = str(e)
        print(f"[ERROR] Video generation failed: {e}", flush=True)

    return result

def write_results_section(title: str, results: list[dict]):
    """Append a results section to the report."""
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n## {title}\n\n")
        f.write(f"| # | Config | Object | Target | Seed | Success | Audit | Steps | Duration |\n")
        f.write(f"|---|--------|--------|--------|------|---------|-------|-------|----------|\n")
        for i, r in enumerate(results, 1):
            if "error" in r:
                f.write(f"| {i} | {r['cfg_name']} | — | — | — | ❌ ERROR: {r['error']} | ERROR | — | {r.get('duration_s','-')}s |\n")
            else:
                succ = "✅" if r.get("success") else "❌"
                f.write(f"| {i} | {r['cfg_name'][:30]} | {r.get('object_variant_id','-')} | "
                        f"{r.get('placement_target_variant_id','-')} | {r.get('seed','-')} | "
                        f"{succ} | {r.get('physical_classification','-')} | {r.get('num_steps','-')} | "
                        f"{r.get('duration_s','-')}s |\n")
        f.write("\n")

        # Summary
        successes = sum(1 for r in results if r.get("success"))
        accepted = sum(1 for r in results if r.get("physical_classification") == "ACCEPTED")
        errors = sum(1 for r in results if "error" in r)
        total = len(results)
        f.write(f"**Summary**: {successes}/{total} succeeded programmatically, {accepted}/{total} accepted physically, {errors} errors\n\n")

def generate_gallery(all_results: list[dict]):
    """Generate an HTML gallery for the run folder."""
    entries = []
    for r in all_results:
        if "video_path" not in r:
            continue
        video_file = Path(r["video_path"]).name
        preview_file = Path(r.get("preview_path", "")).name
        succ = "✅ SUCCESS" if r.get("success") else "❌ FAIL"
        obj = r.get("object_variant_id", "?")
        tgt = r.get("placement_target_variant_id", "—")
        seed = r.get("seed", "?")
        audit = r.get("physical_classification", "UNKNOWN")
        fail_stage = r.get("failure_stage", "—")
        meta_path = f"outputs/{r['cfg_name'].replace('.yaml','')}/000000/meta.json"
        
        entries.append((video_file, preview_file, succ, obj, tgt, seed, audit, fail_stage, meta_path, r.get("cfg_name", "")))

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Final Dataset Readiness Validation Gallery</title>
<style>
body { font-family: Arial, sans-serif; background: #1a1a2e; color: #eee; margin: 20px; }
h1 { color: #0ff; }
h2 { color: #f90; margin-top: 40px; }
.grid { display: flex; flex-wrap: wrap; gap: 16px; }
.card { background: #16213e; border-radius: 12px; padding: 12px; width: 420px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
.card img { width: 100%; border-radius: 8px; cursor: pointer; }
.card video { width: 100%; border-radius: 8px; display: none; }
.card .meta { font-size: 12px; margin-top: 8px; line-height: 1.5; }
.success { color: #0f0; } .fail { color: #f44; }
.card:hover { transform: translateY(-2px); transition: 0.2s; }
</style>
</head>
<body>
<h1>🔬 Final Dataset Readiness Validation</h1>
<p>Generated: """ + datetime.now().isoformat() + """</p>
<div class="grid">
"""
    for vf, pf, succ, obj, tgt, seed, audit, fail_stage, m_path, cfg in entries:
        succ_cls = "success" if "SUCCESS" in succ else "fail"
        html += f"""<div class="card">
  <img src="{pf}" onclick="var v=this.nextElementSibling;v.style.display=v.style.display=='none'?'block':'none';this.style.display='none';v.play();">
  <video src="{vf}" controls loop onended="this.style.display='none';this.previousElementSibling.style.display='block';"></video>
  <div class="meta">
    <strong class="{succ_cls}">{succ} ({audit})</strong><br>
    Object: {obj} → Target: {tgt}<br>
    Seed: {seed} | Failure Stage: {fail_stage}<br>
    Meta Path: {m_path}<br>
    Config: {cfg}
  </div>
</div>
"""
    html += "</div>\n</body>\n</html>"

    gallery_path = VIDEO_RUN_DIR / "index.html"
    gallery_path.write_text(html)
    print(f"[Orchestrator] Gallery: {gallery_path}", flush=True)

def main():
    print(f"\n{'='*60}", flush=True)
    print(f"[Orchestrator] STARTING FINAL DATASET READINESS VALIDATION", flush=True)
    print(f"[Orchestrator] Video run dir: {VIDEO_RUN_DIR}", flush=True)
    print(f"{'='*60}\n", flush=True)

    all_results = []

    # ================= PHASE 1: FCAN03 VERIFICATION (5 episodes) =================
    print(f"\n{'='*60}\nPHASE 1: FCAN03 VERIFICATION (5 seeds)\n{'='*60}", flush=True)
    fcan_configs = [f"fcan03_verification_seed{s}.yaml" for s in [601, 602, 603, 604, 605]]
    fcan_results = []
    
    for i, cfg_name in enumerate(fcan_configs, 1):
        out_name = cfg_name.replace(".yaml", "")
        out_dir = OUT / out_name
        res = run_episode(cfg_name, out_dir, f"verification_{out_name}")
        
        success_label = "SUCCESS" if res.get("success") else "FAIL"
        custom_video_name = f"{i:02d}_fcan03_into_tray04_seed{res.get('seed', 600+i)}_{success_label}"
        res = generate_video(res, custom_video_name)
        fcan_results.append(res)
        all_results.append(res)

    write_results_section("Phase 1 — fcan03 Verification (5 seeds)", fcan_results)

    # ================= PHASE 2: HARD OBJECT GEOMETRIES (6 episodes) =================
    print(f"\n{'='*60}\nPHASE 2: HARD OBJECT GEOMETRIES (6 objects)\n{'='*60}", flush=True)
    hard_configs = [
        ("hard_01_beer00_into_bowl01_seed701.yaml", 701, "beer00", "bowl01"),
        ("hard_02_box01_into_bowl08_seed702.yaml", 702, "box01", "bowl08"),
        ("hard_03_tangerine06_into_tray04_seed703.yaml", 703, "tangerine06", "tray04"),
        ("hard_04_egg03_into_box00_seed704.yaml", 704, "egg03", "box00"),
        ("hard_05_potato00_into_bowl10_seed705.yaml", 705, "potato00", "bowl10"),
        ("hard_06_wbottle01_into_bowl07_seed706.yaml", 706, "wbottle01", "bowl07"),
    ]
    hard_results = []

    for idx, (cfg_name, seed, obj, tgt) in enumerate(hard_configs, 6):
        out_name = cfg_name.replace(".yaml", "")
        out_dir = OUT / out_name
        res = run_episode(cfg_name, out_dir, f"hard_{out_name}")
        
        success_label = "SUCCESS" if res.get("success") else "FAIL"
        custom_video_name = f"{idx:02d}_{obj}_into_{tgt}_seed{seed}_{success_label}"
        res = generate_video(res, custom_video_name)
        hard_results.append(res)
        all_results.append(res)

    write_results_section("Phase 2 — Hard Object Geometries (6 objects)", hard_results)

    # ================= PHASE 3: CLUTTER ROBUSTNESS (2 episodes) =================
    print(f"\n{'='*60}\nPHASE 3: CLUTTER ROBUSTNESS (2 episodes)\n{'='*60}", flush=True)
    clutter_configs = [
        ("clutter_01_avocado_bowl_seed801.yaml", 801, "avocado02", "bowl01", 12),
        ("clutter_02_lime_box_seed802.yaml", 802, "lime00", "box00", 13),
    ]
    clutter_results = []

    for cfg_name, seed, obj, tgt, idx in clutter_configs:
        out_name = cfg_name.replace(".yaml", "")
        out_dir = OUT / out_name
        res = run_episode(cfg_name, out_dir, f"clutter_{out_name}")
        
        success_label = "SUCCESS" if res.get("success") else "FAIL"
        custom_video_name = f"{idx:02d}_{obj}_into_{tgt}_seed{seed}_{success_label}"
        res = generate_video(res, custom_video_name)
        clutter_results.append(res)
        all_results.append(res)

    write_results_section("Phase 3 — Clutter Robustness", clutter_results)

    # ================= PHASE 4: APPLE REGRESSION (1 episode) =================
    print(f"\n{'='*60}\nPHASE 4: APPLE REGRESSION BASELINE\n{'='*60}", flush=True)
    apple_cfg_name = "apple_regression_final.yaml"
    apple_out_dir = OUT / "apple_regression_readiness"
    res = run_episode(apple_cfg_name, apple_out_dir, "apple_regression_readiness")
    
    success_label = "SUCCESS" if res.get("success") else "FAIL"
    custom_video_name = f"14_apple_baseline_{success_label}"
    res = generate_video(res, custom_video_name)
    all_results.append(res)

    write_results_section("Phase 4 — Apple Regression Baseline", [res])

    # ================= PHASE 5: GALLERY & AUDIT REPORT =================
    print(f"\n{'='*60}\nPHASE 5: HTML GALLERY AND READINESS DECISION\n{'='*60}", flush=True)
    generate_gallery(all_results)

    # Calculate scores
    fcan03_runs_total = len(fcan_results)
    fcan03_runs_accepted = sum(1 for r in fcan_results if r.get("physical_classification") == "ACCEPTED")
    fcan03_supported = "YES" if fcan03_runs_accepted >= 4 else "NO"

    hard_object_runs_total = len(hard_results)
    hard_object_runs_accepted = sum(1 for r in hard_results if r.get("physical_classification") == "ACCEPTED")
    
    clutter_runs_total = len(clutter_results)
    clutter_runs_accepted = sum(1 for r in clutter_results if r.get("physical_classification") == "ACCEPTED")

    apple_regression_accepted = "YES" if res.get("physical_classification") == "ACCEPTED" else "NO"

    # Decision logic
    decision = "NOT_READY"
    if fcan03_runs_accepted >= 4 and hard_object_runs_accepted >= 4 and clutter_runs_accepted == 2 and apple_regression_accepted == "YES":
        decision = "READY_FOR_MEDIUM_SCALE"
    elif hard_object_runs_accepted >= 2 and clutter_runs_accepted >= 1 and apple_regression_accepted == "YES":
        decision = "READY_WITH_EXCLUSIONS"

    # Append supported / unsupported objects list
    supported_list = ["avocado02", "onion00", "kiwi00", "lime00"]
    if fcan03_supported == "YES":
        supported_list.append("fcan03")
    
    unsupported_list = []
    for r in hard_results:
        obj = r.get("object_variant_id")
        if not obj:
            # Fall back to checking config name mapping
            cfg = r.get("cfg_name", "")
            matched_obj = None
            for hc in hard_configs:
                if hc[0] == cfg:
                    matched_obj = hc[2]
                    break
            obj = matched_obj
        
        if not obj:
            continue

        if r.get("physical_classification") == "ACCEPTED":
            if obj not in supported_list:
                supported_list.append(obj)
        else:
            if obj not in unsupported_list:
                unsupported_list.append(obj)
    if fcan03_supported == "NO":
        unsupported_list.append("fcan03")

    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        f.write("\n## Dataset Readiness Decision\n\n")
        f.write(f"- **Decision**: `{decision}`\n")
        f.write(f"- **fcan03 Verification**: {fcan03_runs_accepted}/{fcan03_runs_total} accepted (Supported: `{fcan03_supported}`)\n")
        f.write(f"- **Hard Objects**: {hard_object_runs_accepted}/{hard_object_runs_total} accepted\n")
        f.write(f"- **Clutter Robustness**: {clutter_runs_accepted}/{clutter_runs_total} accepted\n")
        f.write(f"- **Apple Regression**: Accepted: `{apple_regression_accepted}`\n\n")

        f.write("### Object Compatibility Profile\n\n")
        supported_str = ", ".join([str(x) for x in supported_list if x is not None])
        unsupported_str = ", ".join([str(x) for x in unsupported_list if x is not None])
        f.write(f"- **Supported Objects**: {supported_str}\n")
        f.write(f"- **Unsupported Objects**: {unsupported_str}\n\n")
        
        f.write("### Audit Explanations\n\n")
        for r in all_results:
            cfg = r.get("cfg_name")
            audit = r.get("physical_classification")
            fail_stage = r.get("failure_stage")
            if audit != "ACCEPTED":
                f.write(f"- **{cfg}**: classified as `{audit}` due to `{fail_stage}`. ")
                if fail_stage == "table_penetration":
                    f.write(f"The object's Z coordinate fell to {r.get('min_z_coordinate_m')}m (below the table surface).\n")
                elif fail_stage == "teleportation":
                    f.write(f"The object made a sudden physical jump of {r.get('max_position_jump_m')}m in a single step.\n")
                elif fail_stage == "task_failure":
                    f.write("The policy finished but the object did not land within the success tolerance boundary.\n")
                else:
                    f.write("Simulation or execution error occurred.\n")
        f.write("\n")

    # Write final result JSON
    with open(VIDEO_RUN_DIR / "readiness_results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n{'='*60}", flush=True)
    print(f"[Orchestrator] ALL DONE! Decision: {decision}", flush=True)
    print(f"[Orchestrator] Report: {REPORT_PATH}", flush=True)
    print(f"{'='*60}\n", flush=True)

if __name__ == "__main__":
    main()
