#!/usr/bin/env python3
"""Robustness & fcan03 diagnosis orchestrator.

Runs:
  Phase 1: 15 robustness episodes (5 pairs × 3 seeds)
  Phase 2: 4 fcan03 diagnosis variants
  Phase 3: 2 clutter robustness episodes
  Phase 4: 1 apple regression baseline
  Phase 5: Gallery generation

Total: 22 Isaac episodes
"""
from __future__ import annotations

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
REPORT = REPORTS / "ROBUSTNESS_AND_FCAN03_DIAGNOSIS_REPORT.md"
VIDEO_RUN_DIR = VIDEO_BASE / "005_robustness_and_fcan03"

VIDEO_RUN_DIR.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)


def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()[:16]


def cleanup_processes():
    """Kill only relevant stale Isaac Sim / Kit processes from this workspace."""
    print("[Orchestrator] Cleaning up stale Isaac Sim processes...", flush=True)
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
        print(f"[Orchestrator] Stopping relevant PIDs: {pids}", flush=True)
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
            print(f"[Orchestrator] Force killing remaining PIDs: {remaining}", flush=True)
            for pid in remaining:
                try:
                    os.kill(pid, 9)  # SIGKILL
                except ProcessLookupError:
                    pass
            time.sleep(5)
    else:
        print("[Orchestrator] No stale processes found.", flush=True)


def run_episode(cfg_name: str, cfg_subdir: str, out_dir: Path, log_name: str) -> dict:
    """Run a single episode and return result metadata."""
    cleanup_processes()

    if out_dir.exists():
        print(f"[Orchestrator] Removing existing output directory: {out_dir}", flush=True)
        subprocess.run(["rm", "-rf", str(out_dir)], check=True)

    env = os.environ.copy()
    env["TERM"] = "xterm-256color"
    env["PYTHONPATH"] = str(REPO / "src")

    log_file = LOGS / f"{log_name}.log"
    cmd = [
        str(ISAACLAB_ROOT / "isaaclab.sh"),
        "-p", "scripts/collect.py",
        "--headless",
        "--collection_config", f"{cfg_subdir}/{cfg_name}",
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

    meta_path = out_dir / "000000/meta.json"
    traj_path = out_dir / "000000/trajectory.npz"

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

    return result


def generate_video(result: dict, video_idx: int, label_prefix: str) -> dict:
    """Generate video and preview for a completed episode."""
    if "error" in result or "episode_dir" not in result:
        return result

    obj = result.get("object_variant_id", "unknown")
    tgt = result.get("placement_target_variant_id", "")
    success_label = "SUCCESS" if result.get("success") else "FAIL"

    if tgt:
        video_name = f"{video_idx:02d}_{label_prefix}_{obj}_into_{tgt}_{success_label}_agent_plus_wrist"
    else:
        video_name = f"{video_idx:02d}_{label_prefix}_{obj}_{success_label}_agent_plus_wrist"

    video_path = VIDEO_RUN_DIR / f"{video_name}.mp4"
    preview_path = VIDEO_RUN_DIR / f"{video_name}.preview.jpg"

    cmd = [
        "python3", str(TOOLS / "make_episode_side_by_side_video.py"),
        "--episode", result["episode_dir"],
        "--output", str(video_path),
        "--fps", "30"
    ]

    print(f"[Orchestrator] Generating video: {video_name}", flush=True)
    try:
        subprocess.run(cmd, check=True, timeout=300)
        result["video_path"] = str(video_path)
        result["preview_path"] = str(preview_path)
        if video_path.exists():
            result["video_hash"] = sha256_file(video_path)
        print(f"[Orchestrator] Video OK: {video_path.name}", flush=True)
    except Exception as e:
        result["video_error"] = str(e)
        print(f"[ERROR] Video generation failed: {e}", flush=True)

    return result


def write_results_section(title: str, results: list[dict]):
    """Append a results section to the report."""
    with open(REPORT, "a", encoding="utf-8") as f:
        f.write(f"\n## {title}\n\n")
        f.write(f"| # | Config | Object | Target | Seed | Success | Metric | Steps | Duration |\n")
        f.write(f"|---|--------|--------|--------|------|---------|--------|-------|----------|\n")
        for i, r in enumerate(results, 1):
            if "error" in r:
                f.write(f"| {i} | {r['cfg_name']} | — | — | — | ❌ ERROR: {r['error']} | — | — | {r.get('duration_s','-')}s |\n")
            else:
                succ = "✅" if r.get("success") else "❌"
                f.write(f"| {i} | {r['cfg_name'][:30]} | {r.get('object_variant_id','-')} | "
                        f"{r.get('placement_target_variant_id','-')} | {r.get('seed','-')} | "
                        f"{succ} | {r.get('success_metric','-')[:25]} | {r.get('num_steps','-')} | "
                        f"{r.get('duration_s','-')}s |\n")
        f.write("\n")

        # Summary
        successes = sum(1 for r in results if r.get("success"))
        errors = sum(1 for r in results if "error" in r)
        total = len(results)
        f.write(f"**Summary**: {successes}/{total} succeeded, {total-successes-errors} failed, {errors} errors\n\n")


def generate_gallery(all_results: list[dict]):
    """Generate an HTML gallery for the 005 folder."""
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
        entries.append((video_file, preview_file, succ, obj, tgt, seed, r.get("cfg_name", "")))

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>005 Robustness & fcan03 Diagnosis Gallery</title>
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
<h1>🔬 005 — Robustness & fcan03 Diagnosis</h1>
<p>Generated: """ + datetime.now().isoformat() + """</p>
<div class="grid">
"""
    for vf, pf, succ, obj, tgt, seed, cfg in entries:
        succ_cls = "success" if "SUCCESS" in succ else "fail"
        html += f"""<div class="card">
  <img src="{pf}" onclick="var v=this.nextElementSibling;v.style.display=v.style.display=='none'?'block':'none';this.style.display='none';v.play();">
  <video src="{vf}" controls loop onended="this.style.display='none';this.previousElementSibling.style.display='block';"></video>
  <div class="meta">
    <strong class="{succ_cls}">{succ}</strong><br>
    Object: {obj} → Target: {tgt}<br>
    Seed: {seed}<br>
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
    print(f"[Orchestrator] ROBUSTNESS & FCAN03 DIAGNOSIS", flush=True)
    print(f"[Orchestrator] Started: {datetime.now().isoformat()}", flush=True)
    print(f"[Orchestrator] Video dir: {VIDEO_RUN_DIR}", flush=True)
    print(f"{'='*60}\n", flush=True)

    all_results = []
    video_idx = 0

    # ================= PHASE 1: ROBUSTNESS MATRIX (15 episodes) =================
    print(f"\n{'='*60}\nPHASE 1: ROBUSTNESS MATRIX (15 episodes)\n{'='*60}", flush=True)

    robustness_configs = sorted(
        [f.name for f in (REPO / "configs/robustness_validation").glob("robust_*.yaml")]
    )
    print(f"[Orchestrator] Found {len(robustness_configs)} robustness configs", flush=True)

    robustness_results = []
    for cfg_name in robustness_configs:
        out_name = cfg_name.replace(".yaml", "")
        out_dir = OUT / out_name
        result = run_episode(cfg_name, "robustness_validation", out_dir, f"robust_{out_name}")
        video_idx += 1
        result = generate_video(result, video_idx, "robust")
        robustness_results.append(result)
        all_results.append(result)

    write_results_section("Phase 1 — Robustness Matrix (5 pairs × 3 seeds)", robustness_results)

    # ================= PHASE 2: FCAN03 DIAGNOSIS (4 episodes) =================
    print(f"\n{'='*60}\nPHASE 2: FCAN03 DIAGNOSIS (4 episodes)\n{'='*60}", flush=True)

    diag_configs = sorted(
        [f.name for f in (REPO / "configs/fcan03_diagnosis").glob("fcan03_diag_*.yaml")]
    )
    print(f"[Orchestrator] Found {len(diag_configs)} diagnosis configs", flush=True)

    diag_results = []
    for cfg_name in diag_configs:
        out_name = cfg_name.replace(".yaml", "")
        out_dir = OUT / out_name
        result = run_episode(cfg_name, "fcan03_diagnosis", out_dir, f"diag_{out_name}")
        video_idx += 1
        result = generate_video(result, video_idx, "fcan03_diag")
        diag_results.append(result)
        all_results.append(result)

    write_results_section("Phase 2 — fcan03 Diagnosis Variants", diag_results)

    # Analyze fcan03 results
    with open(REPORT, "a", encoding="utf-8") as f:
        f.write("### fcan03 Diagnosis Analysis\n\n")
        for r in diag_results:
            f.write(f"**{r['cfg_name']}**: success={r.get('success','?')}\n\n")
        
        # Determine fix
        successes = [r for r in diag_results if r.get("success")]
        if successes:
            best = successes[0]  # First successful one in alphabetical order
            f.write(f"**Recommended fix**: Use configuration from `{best['cfg_name']}`\n\n")
        else:
            f.write("**WARNING**: No fcan03 variant succeeded. Further investigation needed.\n\n")

    # ================= PHASE 3: CLUTTER ROBUSTNESS (2 episodes) =================
    print(f"\n{'='*60}\nPHASE 3: CLUTTER ROBUSTNESS (2 episodes)\n{'='*60}", flush=True)

    # Create clutter configs inline
    clutter_pairs = [
        ("apple01", "apple", "bowl08", "bowl", 501, "clutter_apple_bowl"),
        ("lime00", "lime", "box00", "box", 502, "clutter_lime_box"),
    ]

    clutter_results = []
    for obj_var, obj_cat, tgt_var, tgt_cat, seed, label_name in clutter_pairs:
        cfg_name = f"{label_name}.yaml"
        cfg_path = REPO / f"configs/robustness_validation/{cfg_name}"
        out_dir = OUT / label_name

        cfg_text = f"""task: pick_place
output_dir: {out_dir}
start_episode_id: 0
num_episodes: 1
max_steps: 4800
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: {seed}
top_grasp_depth_m: 0.025

target_object:
  catalog_config: object_catalog.generated.yaml
  geometry_config: object_geometry.generated.yaml
  category_id: {obj_cat}
  variant_id: {obj_var}
  split: train
  role: target
  required_affordances: [pickable]
  required_grasp_strategy: center_top

placement_target:
  catalog_config: object_catalog.generated.yaml
  geometry_config: object_geometry.generated.yaml
  category_id: {tgt_cat}
  variant_id: {tgt_var}
  split: train
  role: target
  required_affordances: [container]
  required_grasp_strategy: unsupported

clutter:
  catalog_config: object_catalog.generated.yaml
  geometry_config: object_geometry.generated.yaml
  count: 3
  split: train
  role: clutter
  required_affordances: [reachable]
  required_grasp_strategy: unsupported
  xy_range:
    x: [0.34, 0.90]
    y: [-0.45, 0.45]
  object_margin_m: 0.035
  placement_target_margin_m: 0.035
  clutter_margin_m: 0.025
  max_footprint_radius_m: 0.17
  max_asset_sampling_attempts: 128
  max_layout_sampling_attempts: 128
  max_sampling_attempts: 256
  grid_step_m: 0.015

pose_randomization:
  object_xy_range:
    x: [-0.02, 0.02]
    y: [-0.02, 0.02]
  place_xy_range:
    x: [-0.03, 0.03]
    y: [-0.03, 0.03]

lighting_randomization:
  dome_light_intensity_range: [800.0, 800.0]
  dome_light_color_options:
    - [1.0, 1.0, 1.0]
"""
        cfg_path.write_text(cfg_text)
        result = run_episode(cfg_name, "robustness_validation", out_dir, f"clutter_{label_name}")
        video_idx += 1
        result = generate_video(result, video_idx, "clutter")
        clutter_results.append(result)
        all_results.append(result)

    write_results_section("Phase 3 — Clutter Robustness", clutter_results)

    # ================= PHASE 4: APPLE REGRESSION (1 episode) =================
    print(f"\n{'='*60}\nPHASE 4: APPLE REGRESSION BASELINE\n{'='*60}", flush=True)

    apple_cfg_name = "apple_regression_final.yaml"
    apple_cfg_path = REPO / f"configs/robustness_validation/{apple_cfg_name}"
    apple_out_dir = OUT / "apple_regression_robustness"

    apple_cfg = f"""task: pick_place
output_dir: {apple_out_dir}
start_episode_id: 0
num_episodes: 1
max_steps: 4800
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 42
top_grasp_depth_m: 0.025

target_object:
  catalog_config: object_catalog.generated.yaml
  geometry_config: object_geometry.generated.yaml
  category_id: apple
  variant_id: apple01
  split: train
  role: target
  required_affordances: [pickable]
  required_grasp_strategy: center_top

pose_randomization:
  object_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]
  place_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]

lighting_randomization:
  dome_light_intensity_range: [800.0, 800.0]
  dome_light_color_options:
    - [1.0, 1.0, 1.0]
"""
    apple_cfg_path.write_text(apple_cfg)
    apple_result = run_episode(apple_cfg_name, "robustness_validation", apple_out_dir, "apple_regression")
    video_idx += 1
    apple_result = generate_video(apple_result, video_idx, "regression")
    all_results.append(apple_result)

    write_results_section("Phase 4 — Apple Regression Baseline", [apple_result])

    # ================= PHASE 5: GALLERY =================
    print(f"\n{'='*60}\nPHASE 5: GALLERY GENERATION\n{'='*60}", flush=True)
    generate_gallery(all_results)

    # Final summary
    with open(REPORT, "a", encoding="utf-8") as f:
        f.write("\n## Final Summary\n\n")
        f.write(f"- **Total episodes**: {len(all_results)}\n")
        f.write(f"- **Successful**: {sum(1 for r in all_results if r.get('success'))}\n")
        f.write(f"- **Failed**: {sum(1 for r in all_results if not r.get('success') and 'error' not in r)}\n")
        f.write(f"- **Errors**: {sum(1 for r in all_results if 'error' in r)}\n")
        f.write(f"- **Video folder**: `{VIDEO_RUN_DIR}`\n")
        f.write(f"- **Gallery**: `{VIDEO_RUN_DIR / 'index.html'}`\n")
        f.write(f"- **Completed**: {datetime.now().isoformat()}\n\n")

        # Robustness success rate by pair
        f.write("### Robustness Success Rate by Pair\n\n")
        f.write("| Pair | Seed 301 | Seed 302 | Seed 303 | Rate |\n")
        f.write("|------|----------|----------|----------|------|\n")
        pair_names = ["apple01→bowl08", "avocado02→bowl01", "onion00→bowl07", "kiwi00→bowl10", "lime00→box00"]
        for pair_idx, pair_name in enumerate(pair_names):
            pair_results = robustness_results[pair_idx*3:(pair_idx+1)*3]
            cells = []
            for r in pair_results:
                if r.get("success"):
                    cells.append("✅")
                elif "error" in r:
                    cells.append("⚠️")
                else:
                    cells.append("❌")
            rate = f"{sum(1 for r in pair_results if r.get('success'))}/3"
            f.write(f"| {pair_name} | {cells[0]} | {cells[1]} | {cells[2]} | {rate} |\n")
        f.write("\n")

    # Save all results as JSON for post-analysis
    results_json = VIDEO_RUN_DIR / "results.json"
    with open(results_json, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"[Orchestrator] Results JSON: {results_json}", flush=True)

    total_success = sum(1 for r in all_results if r.get("success"))
    total = len(all_results)
    print(f"\n{'='*60}", flush=True)
    print(f"[Orchestrator] COMPLETE: {total_success}/{total} succeeded", flush=True)
    print(f"[Orchestrator] Finished: {datetime.now().isoformat()}", flush=True)
    print(f"{'='*60}\n", flush=True)


if __name__ == "__main__":
    main()
