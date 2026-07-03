import os
import json
import csv
import numpy as np
import pandas as pd
from pathlib import Path
import subprocess
from datetime import datetime

# --- CONFIG ---
ROOT_DIR = Path("/home/redafrix/tests/internship")
RUNS_DIR = ROOT_DIR / "videos_testes/runs"
OUTPUT_DIR = ROOT_DIR / "videos_testes"
SANDBOX_DIR = ROOT_DIR / "reda_ws/video_labeling_ws"
ROI_DIR = OUTPUT_DIR / "predicted_roi_clips"

os.makedirs(ROI_DIR, exist_ok=True)

def load_data(run_dir):
    metrics_path = Path(run_dir) / "per_step_metrics.jsonl"
    if not metrics_path.exists():
        return None
    data = []
    with open(metrics_path, 'r') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except:
                continue
    return data

def compute_signals(data):
    if not data: return None
    steps = len(data)
    # Proprio: [x, y, z, ...] - assume first 3 are EEF
    eef_pos = np.array([d['proprio'][:3] for d in data])
    
    obj_keys = list(data[0]['object_positions'].keys())
    obj_trajectories = {k: np.array([d['object_positions'][k] for d in data]) for k in obj_keys}
    
    # Target Object Selection: Moves most and isn't a known fixed structure
    target_obj = None
    max_move = -1
    for k, traj in obj_trajectories.items():
        if any(x in k.lower() for x in ["cabinet", "stove", "table", "counter", "burner"]):
            continue
        move = np.linalg.norm(traj[-1] - traj[0])
        if move > max_move:
            max_move = move
            target_obj = k
    
    if not target_obj: 
        # Fallback to anything that isn't cabinet
        for k in obj_keys:
            if "cabinet" not in k.lower():
                target_obj = k
                break
    
    if not target_obj: target_obj = obj_keys[0]
    
    target_pos = obj_trajectories[target_obj]
    dist_eef_target = np.linalg.norm(eef_pos - target_pos, axis=1)
    
    # Velocities and Deltas
    target_z = target_pos[:, 2]
    eef_z = eef_pos[:, 2]
    target_z_delta = np.diff(target_z, prepend=target_z[0])
    eef_z_delta = np.diff(eef_z, prepend=eef_z[0])
    
    # Progress: displacement from start towards goal?
    # Hard to know goal without parsing, but we can use distance to other objects
    
    # Action Norm
    actions = np.array([d['action'] for d in data])
    action_norm = np.linalg.norm(actions[:, :3], axis=1)
    
    return {
        "timesteps": np.arange(steps),
        "eef_pos": eef_pos,
        "target_pos": target_pos,
        "dist_eef_target": dist_eef_target,
        "target_z": target_z,
        "eef_z": eef_z,
        "target_z_delta": target_z_delta,
        "eef_z_delta": eef_z_delta,
        "action_norm": action_norm,
        "target_name": target_obj,
        "raw_data": data
    }

def detect_events(signals):
    events = []
    T = len(signals['timesteps'])
    
    # Heuristic 1: Missed Grasp
    # Robot is close, then moves up, but target stays at same height
    for t in range(5, T - 25):
        if signals['dist_eef_target'][t] < 0.07:
            # Check if robot rises in the next 15 steps
            eef_rise = signals['eef_z'][t+15] - signals['eef_z'][t]
            target_rise = signals['target_z'][t+15] - signals['target_z'][t]
            
            if eef_rise > 0.03 and target_rise < 0.01:
                events.append({
                    "start_t": max(0, t - 10),
                    "end_t": t + 15,
                    "bad_type": "missed_grasp",
                    "confidence": 0.85,
                    "evidence": f"EEF rose {eef_rise:.3f}m, target stayed at z={signals['target_z'][t]:.3f}"
                })

    # Heuristic 2: Lost Grasp / Drop
    # Target was elevated, then falls while EEF is still nearby or moving away
    for t in range(10, T - 20):
        if signals['target_z'][t] > signals['target_z'][0] + 0.03: # Elevated
            # Check for sudden drop
            if signals['target_z'][t+10] < signals['target_z'][t] - 0.02:
                # Did EEF follow?
                eef_drop = signals['eef_z'][t+10] - signals['eef_z'][t]
                if eef_drop > -0.01: # EEF didn't drop as much
                    events.append({
                        "start_t": t - 5,
                        "end_t": t + 15,
                        "bad_type": "lost_grasp",
                        "confidence": 0.8,
                        "evidence": f"Target dropped from {signals['target_z'][t]:.3f} to {signals['target_z'][t+10]:.3f}"
                    })

    # Heuristic 3: Stuck / No Progress (Retry Loop)
    # Action is high but Target/EEF movement is low for a sustained period
    window = 40
    for t in range(0, T - window, 20):
        target_std = np.std(signals['target_pos'][t:t+window], axis=0).mean()
        eef_std = np.std(signals['eef_pos'][t:t+window], axis=0).mean()
        avg_action = np.mean(signals['action_norm'][t:t+window])
        
        if avg_action > 0.2 and target_std < 0.003 and eef_std < 0.008:
            events.append({
                "start_t": t,
                "end_t": t + window,
                "bad_type": "stuck_retry_loop",
                "confidence": 0.7,
                "evidence": f"High action ({avg_action:.2f}) with minimal progress (target_std={target_std:.4f})"
            })

    # Heuristic 4: Bad Placement
    # Happens late in the episode, near some other object, object is static but not "success"
    if T > 100:
        for t in range(T - 60, T - 10):
            # If target is near its final position and robot is still acting
            if signals['action_norm'][t] > 0.1 and signals['target_vel_avg_window'] < 0.001:
                # This needs better logic, but let's use the 'stuck' logic as a proxy for now
                pass

    # Merge overlapping events of same type
    if not events: return []
    events.sort(key=lambda x: x['start_t'])
    
    merged = []
    curr = events[0]
    for i in range(1, len(events)):
        nxt = events[i]
        # If same type and overlaps or very close
        if nxt['bad_type'] == curr['bad_type'] and nxt['start_t'] < curr['end_t'] + 15:
            curr['end_t'] = max(curr['end_t'], nxt['end_t'])
            curr['confidence'] = max(curr['confidence'], nxt['confidence'])
        else:
            merged.append(curr)
            curr = nxt
    merged.append(curr)
    
    # Post-process
    for e in merged:
        e['center_t'] = (e['start_t'] + e['end_t']) // 2
        e['start_t'] = int(e['start_t'])
        e['end_t'] = int(e['end_t'])
        e['center_t'] = int(e['center_t'])
        
    return merged

def cut_clip(run_dir, event, output_path):
    video_path = Path(run_dir) / "failure_side_by_side.mp4"
    if not video_path.exists():
        # Try finding any mp4 with side_by_side
        for f in os.listdir(run_dir):
            if "side_by_side.mp4" in f:
                video_path = Path(run_dir) / f
                break
    
    if not video_path.exists(): return False
    
    start_s = max(0, event['start_t'] - 20) / 10.0 # 10 FPS
    duration_s = (event['end_t'] - event['start_t'] + 60) / 10.0
    
    cmd = [
        "ffmpeg", "-y", "-ss", str(start_s), "-i", str(video_path),
        "-t", str(duration_s), "-c", "copy", str(output_path)
    ]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def main():
    manual_data = []
    manual_csv = OUTPUT_DIR / "manual_failure_events.csv"
    if manual_csv.exists():
        manual_df = pd.read_csv(manual_csv)
        manual_data = manual_df.to_dict('records')
    
    all_runs = sorted([d for d in os.listdir(RUNS_DIR) if d.startswith("fail_")])
    
    predicted_events = []
    
    for run_folder in all_runs:
        print(f"Processing {run_folder}...")
        run_path = RUNS_DIR / run_folder
        data = load_data(run_path)
        if not data: continue
        
        signals = compute_signals(data)
        if not signals: continue
        
        # Helper for bad placement
        signals['target_vel_avg_window'] = np.std(signals['target_pos'][-30:], axis=0).mean()
        
        events = detect_events(signals)
        
        # Rank by confidence and pick top 3
        events.sort(key=lambda x: x['confidence'], reverse=True)
        top_events = events[:3]
        
        for idx, e in enumerate(top_events):
            e['run_folder'] = run_folder
            e['pred_event_id'] = idx + 1
            e['side_by_side_video'] = str(list(run_path.glob("*side_by_side.mp4"))[0].name if list(run_path.glob("*side_by_side.mp4")) else "")
            
            # ROI Clip
            roi_run_dir = ROI_DIR / run_folder
            os.makedirs(roi_run_dir, exist_ok=True)
            clip_name = f"event_{e['pred_event_id']}_{e['bad_type']}.mp4"
            clip_path = roi_run_dir / clip_name
            if cut_clip(run_path, e, clip_path):
                e['roi_clip'] = str(clip_path.relative_to(OUTPUT_DIR))
            else:
                e['roi_clip'] = ""
                
            predicted_events.append(e)

    # Save outputs
    if predicted_events:
        df = pd.DataFrame(predicted_events)
        df.to_csv(OUTPUT_DIR / "predicted_failure_regions.csv", index=False)
        
        with open(OUTPUT_DIR / "predicted_failure_regions.jsonl", 'w') as f:
            for e in predicted_events:
                f.write(json.dumps(e) + "\n")
                
        # Review-friendly todo
        todo_cols = ["run_folder", "pred_event_id", "pred_start_t", "pred_end_t", "pred_bad_type", "confidence", "evidence", "human_correct", "human_failure_start_t", "human_failure_end_t", "human_bad_type", "human_notes"]
        todo_df = df.reindex(columns=todo_cols)
        todo_df.to_csv(OUTPUT_DIR / "failure_review_todo.csv", index=False)
        
    print(f"Done. Detected {len(predicted_events)} events across {len(all_runs)} runs.")

if __name__ == "__main__":
    main()
