#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import json
from pathlib import Path

# Paths
WS = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test")
REPO = WS / "franka_wrist_camera_isaaclab"
REPORTS = WS / "reports"
LOGS = WS / "logs"
OUT = WS / "outputs"
VIDEOS = OUT / "object_test_videos"
TOOLS = WS / "video_tools"
CLEANUP_SCRIPT = WS / "cleanup_isaac_processes.py"
ISAACLAB_ROOT = Path(os.environ.get("ISAACLAB_ROOT", "/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab"))

# Video numbering state
session_run_dir = None
video_counter = 1

def init_session_dir():
    global session_run_dir
    VIDEOS.mkdir(parents=True, exist_ok=True)
    existing_runs = [d for d in VIDEOS.iterdir() if d.is_dir() and d.name.startswith("run_")]
    run_numbers = []
    for d in existing_runs:
        try:
            num = int(d.name.split("_")[1])
            run_numbers.append(num)
        except (IndexError, ValueError):
            pass
    next_num = max(run_numbers) + 1 if run_numbers else 1
    session_run_dir = VIDEOS / f"run_{next_num:03d}"
    session_run_dir.mkdir(parents=True, exist_ok=True)
    print(f"[Receptacle Orchestrator] Initialized video session directory: {session_run_dir}")

def cleanup_stale_processes():
    print("[Receptacle Orchestrator] Running process cleanup...")
    try:
        subprocess.run([sys.executable, str(CLEANUP_SCRIPT)], check=True)
    except Exception as e:
        print(f"[Receptacle Orchestrator] Cleanup failed: {e}")

def run_collection(run_name, config_path, out_dir):
    cleanup_stale_processes()
    
    log_file_path = LOGS / f"{run_name}.log"
    print(f"[Receptacle Orchestrator] Launching {run_name}, logging to {log_file_path}")
    
    # Environment variables
    env = os.environ.copy()
    env["TERM"] = "xterm"
    env["PYTHONPATH"] = (
        f"{ISAACLAB_ROOT}/source/isaaclab:"
        f"{ISAACLAB_ROOT}/source/isaaclab_assets:"
        f"{ISAACLAB_ROOT}/source/isaaclab_mimic:"
        f"{ISAACLAB_ROOT}/source/isaaclab_rl:"
        f"{ISAACLAB_ROOT}/source/isaaclab_tasks:"
        f"{REPO}/src"
    )
    
    cmd = [
        str(ISAACLAB_ROOT / "isaaclab.sh"),
        "-p", "scripts/collect.py",
        "--headless",
        "--collection_config", str(config_path.relative_to(REPO / "configs")),
        "--output_dir", str(out_dir)
    ]
    
    # Run the process
    proc = subprocess.Popen(
        cmd,
        cwd=str(REPO),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
        text=True,
        bufsize=1
    )
    
    saved_manifest = False
    with open(log_file_path, "w", encoding="utf-8") as log_f:
        for line in proc.stdout:
            log_f.write(line)
            log_f.flush()
            # print to stdout for debugging progress
            if "Step " in line or "Episode " in line or "Saved " in line:
                print(f"[{run_name}] {line.strip()}", flush=True)
            
            if "Saved collection manifest to:" in line:
                print(f"[Receptacle Orchestrator] Manifest saved. Finding and sending SIGINT directly to the python process...")
                saved_manifest = True
                
                # Try to find the actual python process running our script and send SIGINT
                try:
                    pids_output = subprocess.check_output(["pgrep", "-f", f"collect.py.*{run_name}"]).decode().strip()
                    pids = pids_output.split()
                    for pid_str in pids:
                        pid = int(pid_str)
                        if pid != os.getpid():
                            print(f"[Receptacle Orchestrator] Sending SIGINT to PID {pid}")
                            os.kill(pid, subprocess.signal.SIGINT)
                except Exception as e:
                    print(f"[Receptacle Orchestrator] Failed to send SIGINT directly to PID: {e}. Falling back to parent proc.")
                    proc.send_signal(subprocess.signal.SIGINT)
                
    # Wait for process to exit
    try:
        status = proc.wait(timeout=60)
    except subprocess.TimeoutExpired:
        print(f"[Receptacle Orchestrator] Process did not exit after SIGINT. Killing...")
        proc.kill()
        status = proc.wait()
        
    print(f"[Receptacle Orchestrator] Process exited with status {status}")
    return saved_manifest

def generate_video_and_preview(run_name, out_dir, success):
    global video_counter
    label = "SUCCESS" if success else "FAIL"
    video_out = session_run_dir / f"{video_counter:04d}_{run_name}_000000_{label}_agent_plus_wrist.mp4"
    episode_dir = out_dir / "000000"
    
    if not (episode_dir / "trajectory.npz").exists():
        print(f"[Receptacle Orchestrator] No trajectory.npz found for {run_name}. Skipping video.")
        return None
        
    cmd = [
        sys.executable,
        str(TOOLS / "make_episode_side_by_side_video.py"),
        "--episode", str(episode_dir),
        "--output", str(video_out),
        "--fps", "30"
    ]
    
    print(f"[Receptacle Orchestrator] Generating video for {run_name}")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(res.stdout)
        video_counter += 1
        return video_out
    except Exception as e:
        print(f"[Receptacle Orchestrator] Video generation failed for {run_name}: {e}")
        return None

def write_report_entry(run_name, out_dir, success, video_path):
    report_file = REPORTS / "RECEPTACLE_GOAL_OBJECT_TEST_REPORT.md"
    log_file_path = LOGS / f"{run_name}.log"
    
    # Read status from log
    log_tail = ""
    if log_file_path.exists():
        lines = log_file_path.read_text(encoding="utf-8").splitlines()
        # Find lines of interest
        interesting_lines = [
            l for l in lines 
            if any(k in l.lower() for k in ["success", "traceback", "exception", "error", "exceeded", "max_steps", "saved", "goalreceptacle", "receptacle"])
        ]
        log_tail = "\n".join(interesting_lines[-50:])
        
    meta_content = ""
    meta_path = out_dir / "000000" / "meta.json"
    if meta_path.exists():
        meta_content = meta_path.read_text(encoding="utf-8")
        
    entry = f"""
## Result {run_name}
- status: 0
- success_center_approx: {"YES" if success else "NO"}
- output_dir: {out_dir}
- video: {video_path or "None"}
"""
    if video_path and video_path.exists():
        entry += f"- video_size: {video_path.stat().st_size} bytes\n"
        preview_path = video_path.with_suffix(".preview.jpg")
        if preview_path.exists():
            entry += f"- preview_size: {preview_path.stat().st_size} bytes\n"
            
    entry += f"""
### log tail
```
{log_tail}
```

### meta
```json
{meta_content}
```
"""
    with open(report_file, "a", encoding="utf-8") as f:
        f.write(entry)

def check_success(out_dir):
    meta_path = out_dir / "000000" / "meta.json"
    if not meta_path.exists():
        return False
    try:
        data = json.loads(meta_path.read_text())
        return data.get("success") is True
    except Exception:
        return False

def main():
    cfg_dir = REPO / "configs" / "receptacle_goal_tests"
    configs = sorted(list(cfg_dir.glob("*.yaml")))
    
    print(f"Loaded {len(configs)} configs to run.")
    init_session_dir()
    
    for cfg in configs:
        run_name = cfg.stem
        out_dir = OUT / run_name
        
        print(f"\n======================================")
        print(f"RUNNING CONFIG: {run_name}")
        print(f"======================================")
        
        run_collection(run_name, cfg, out_dir)
        success = check_success(out_dir)
        video_path = generate_video_and_preview(run_name, out_dir, success)
        write_report_entry(run_name, out_dir, success, video_path)

if __name__ == "__main__":
    main()
