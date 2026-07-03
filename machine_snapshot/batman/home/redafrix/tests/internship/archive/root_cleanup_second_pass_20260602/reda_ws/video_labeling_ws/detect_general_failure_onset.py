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
ROI_DIR = OUTPUT_DIR / "general_failure_onset_clips"

os.makedirs(ROI_DIR, exist_ok=True)

# Manual Examples for Calibration
MANUAL_EXAMPLES = [
    {"run_folder": "fail_0001_libero_spatial_with_mug_t5", "manual_center": 75, "manual_region": (70, 80)},
    {"run_folder": "fail_0001_libero_spatial_with_mug_t5", "manual_center": 180, "manual_region": (170, 190)},
    {"run_folder": "fail_0002_libero_spatial_with_mug_t5", "manual_center": 30, "manual_region": (25, 35)},
    {"run_folder": "fail_0003_libero_spatial_with_mug_t0", "manual_center": 40, "manual_region": (35, 45)},
    {"run_folder": "fail_0004_libero_spatial_with_mug_t4", "manual_center": 120, "manual_region": (115, 125)},
]

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
    eef_pos = np.array([d['proprio'][:3] for d in data])
    
    obj_keys = list(data[0]['object_positions'].keys())
    obj_trajectories = {k: np.array([d['object_positions'][k] for d in data]) for k in obj_keys}
    
    # Identify active object
    target_obj = None
    max_move = -1
    for k, traj in obj_trajectories.items():
        if any(x in k.lower() for x in ["cabinet", "stove", "table", "counter", "burner"]):
            continue
        move = np.linalg.norm(traj[-1] - traj[0])
        if move > max_move:
            max_move = move
            target_obj = k
    
    if not target_obj: target_obj = obj_keys[0]
    target_pos = obj_trajectories[target_obj]
    
    # Distance EEF-Target
    dist_eef_target = np.linalg.norm(eef_pos - target_pos, axis=1)
    
    # EEF and Target Z
    eef_z = eef_pos[:, 2]
    target_z = target_pos[:, 2]
    
    # Action Norm (EEF velocity commands)
    actions = np.array([d['action'] for d in data])
    action_norm = np.linalg.norm(actions[:, :3], axis=1)
    
    # Moving averages/stds
    def rolling_std(x, w):
        return pd.Series(x).rolling(window=w, center=True).std().fillna(0).values

    def rolling_mean(x, w):
        return pd.Series(x).rolling(window=w, center=True).mean().fillna(0).values

    return {
        "timesteps": np.arange(steps),
        "eef_pos": eef_pos,
        "target_pos": target_pos,
        "dist_eef_target": dist_eef_target,
        "eef_z": eef_z,
        "target_z": target_z,
        "action_norm": action_norm,
        "target_name": target_obj,
        "target_std_15": rolling_std(np.linalg.norm(target_pos, axis=1), 15),
        "eef_std_15": rolling_std(np.linalg.norm(eef_pos, axis=1), 15),
        "action_mean_15": rolling_mean(action_norm, 15)
    }

def calculate_failure_score(signals):
    T = len(signals['timesteps'])
    scores = np.zeros(T)
    evidence = [""] * T
    
    for t in range(5, T - 5):
        # Component 1: Mismatch (Moving but not moving object)
        # High action + low target movement
        s_mismatch = signals['action_mean_15'][t] * (1.0 - np.clip(signals['target_std_15'][t] * 50, 0, 1))
        s_mismatch = np.clip(s_mismatch * 2, 0, 1)
        
        # Component 2: Missed/Dropped (Gripper rises, object doesn't)
        # Look at 15 step window
        w = 10
        t_end = min(t + w, T - 1)
        eef_rise = signals['eef_z'][t_end] - signals['eef_z'][t]
        obj_rise = signals['target_z'][t_end] - signals['target_z'][t]
        dist = signals['dist_eef_target'][t]
        
        s_missed = 0
        if dist < 0.1 and eef_rise > 0.02 and obj_rise < 0.005:
            s_missed = 0.9
            
        # Component 3: Stall/Stuck
        s_stall = 0
        if signals['action_mean_15'][t] > 0.3 and signals['eef_std_15'][t] < 0.01 and signals['target_std_15'][t] < 0.005:
            s_stall = 0.7
            
        # Combine
        scores[t] = max(s_mismatch, s_missed, s_stall)
        
        # Brief evidence
        if s_missed > 0.8: ev = "EEF rise/Obj still"
        elif s_mismatch > 0.6: ev = "High Action/Low Obj move"
        elif s_stall > 0.6: ev = "Stuck/Retry"
        else: ev = ""
        evidence[t] = ev

    return scores, evidence

def get_onset_regions(scores, evidence, threshold=0.5):
    T = len(scores)
    regions = []
    
    in_region = False
    start = 0
    
    for t in range(T):
        if scores[t] >= threshold and not in_region:
            in_region = True
            start = t
        elif scores[t] < threshold and in_region:
            in_region = False
            end = t
            if end - start >= 5: # Min duration
                regions.append({
                    "start_t": start,
                    "end_t": end,
                    "center_t": (start + end) // 2,
                    "score": np.max(scores[start:end]),
                    "evidence": evidence[start + (end-start)//2]
                })
    
    if in_region:
        regions.append({
            "start_t": start,
            "end_t": T-1,
            "center_t": (start + T-1) // 2,
            "score": np.max(scores[start:]),
            "evidence": evidence[start + (T-1-start)//2]
        })
        
    # Merge close regions
    if not regions: return []
    regions.sort(key=lambda x: x['start_t'])
    
    merged = []
    if regions:
        curr = regions[0]
        for i in range(1, len(regions)):
            nxt = regions[i]
            if nxt['start_t'] < curr['end_t'] + 30:
                curr['end_t'] = max(curr['end_t'], nxt['end_t'])
                curr['score'] = max(curr['score'], nxt['score'])
                # keep earliest evidence usually
            else:
                merged.append(curr)
                curr = nxt
        merged.append(curr)
        
    for m in merged:
        m['center_t'] = (m['start_t'] + m['end_t']) // 2
        
    # Pick top 2, prefer earlier
    merged.sort(key=lambda x: x['start_t'])
    return merged[:2]

def create_compact_roi(run_dir, region, output_path, run_name):
    video_path = next(run_dir.glob("*side_by_side.mp4"), None)
    if not video_path: return False
    
    start_t = max(0, region['start_t'] - 20)
    end_t = region['end_t'] + 40
    start_s = start_t / 10.0
    dur_s = (end_t - start_t) / 10.0
    
    # Simplified text for drawtext and ESCAPE colons for FFmpeg
    clean_run_name = run_name.replace(":", "_").replace("'", "")
    text = f"Run_ {clean_run_name[:15]} | T_{region['start_t']}-{region['end_t']} | S_{region['score']:.2f}"
    # Replace any remaining colons with underscores just in case
    text = text.replace(":", "_")
    
    # Use a simpler drawtext and explicit fontfile if common linux path exists
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    if os.path.exists(font_path):
        drawtext = f"drawtext=fontfile={font_path}:text='{text}':x=10:y=10:fontsize=16:fontcolor=white:box=1:boxcolor=black@0.5"
    else:
        drawtext = f"drawtext=text='{text}':x=10:y=10:fontcolor=white:box=1:boxcolor=black@0.5"
    
    cmd = [
        "ffmpeg", "-y", "-i", str(video_path),
        "-ss", str(start_s), "-t", str(dur_s),
        "-vf", drawtext,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(output_path)
    ]
    
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def main():
    all_runs = sorted([d for d in os.listdir(RUNS_DIR) if d.startswith("fail_")])
    
    predictions = []
    calibration_results = []
    
    for run_folder in all_runs:
        print(f"Detecting onset for {run_folder}...")
        run_path = RUNS_DIR / run_folder
        data = load_data(run_path)
        if not data: continue
        
        signals = compute_signals(data)
        if not signals: continue
        
        scores, evidence = calculate_failure_score(signals)
        regions = get_onset_regions(scores, evidence)
        
        for idx, reg in enumerate(regions):
            run_roi_dir = ROI_DIR / run_folder
            os.makedirs(run_roi_dir, exist_ok=True)
            clip_name = f"onset_{idx+1}.mp4"
            clip_path = run_roi_dir / clip_name
            
            success = create_compact_roi(run_path, reg, clip_path, run_folder)
            
            pred = {
                "run_folder": run_folder,
                "pred_start_t": int(reg['start_t']),
                "pred_end_t": int(reg['end_t']),
                "pred_center_t": int(reg['center_t']),
                "confidence": float(reg['score']),
                "general_failure_score": float(reg['score']),
                "evidence_summary": reg['evidence'],
                "side_by_side_video": str(next(run_path.glob("*side_by_side.mp4"), Path("")).name),
                "roi_clip": str(clip_path.relative_to(OUTPUT_DIR)) if success else "",
                "human_correct": "",
                "human_timestep_optional": "",
                "human_notes": ""
            }
            predictions.append(pred)
            
            # Check Calibration
            for ex in MANUAL_EXAMPLES:
                if ex['run_folder'] == run_folder:
                    if abs(reg['center_t'] - ex['manual_center']) <= 25:
                        calibration_results.append({
                            "run": run_folder,
                            "manual": ex['manual_center'],
                            "pred": reg['center_t'],
                            "hit": True,
                            "diff": reg['center_t'] - ex['manual_center'],
                            "evidence": reg['evidence']
                        })

    # Save CSV
    df = pd.DataFrame(predictions)
    df.to_csv(OUTPUT_DIR / "failure_onset_review.csv", index=False)
    
    # Save JSONL
    with open(OUTPUT_DIR / "failure_onset_predictions.jsonl", 'w') as f:
        for p in predictions:
            f.write(json.dumps(p) + "\n")
            
    # Calibration Report Data
    print("\n--- Calibration Results ---")
    for res in calibration_results:
        print(f"{res['run']} | Manual: {res['manual']} | Pred: {res['pred']} | Diff: {res['diff']} | HIT: {res['hit']}")

if __name__ == "__main__":
    main()
