#!/usr/bin/env python3
import os
import sys
import time
import json
import argparse
import csv
import numpy as np
import cv2
import torch
from pathlib import Path
from datetime import datetime

# Add src to sys.path to find helper modules
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR / "src"))

# Import helper functions from local src (copied from main project)
from libero_pro_env_utils import make_env, obs_images, obs_to_proprio
from simvla_candidate_sampler import load_simvla, sample_candidate
from outcome_metrics import (
    detect_phase, 
    object_body_positions, 
    contact_summary, 
    check_success,
    _trace_task_values,
    eef_pos,
    gripper,
    _safe_float_list,
    obs_pos,
    body_pos_by_prefix
)
from task_parser import parse_task_context

def overlay_text(img, text_lines, font_scale=0.5, thickness=1):
    y0, dy = 20, 20
    for i, line in enumerate(text_lines):
        y = y0 + i * dy
        cv2.putText(img, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
    return img

def create_video(frames, output_path, fps=10):
    if not frames:
        return
    h, w, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (w, h))
    for frame in frames:
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    out.release()

def run_episode(env, model, processor, device, task_lang, task_id, suite, run_id, env_seed=0, max_steps=400, fps=10):
    # env.seed(env_seed) if possible. make_env already handles it if passed.
    obs = env.reset()
    obj_pos0 = object_body_positions(env)
    task_context = parse_task_context(task_lang, obs, all_bodies=list(obj_pos0.keys()))
    
    frames_agent = []
    frames_wrist = []
    frames_side = []
    step_metrics = []
    actions_data = []
    
    success = False
    done = False
    
    action_chunk = None
    
    for t in range(max_steps):
        # 1. Get images and proprio
        img_agent, img_wrist = obs_images(obs)
        proprio = obs_to_proprio(obs)
        
        # 2. Get action from SimVLA
        if t % 10 == 0 or action_chunk is None:
            res = sample_candidate(model, processor, task_lang, img_agent, img_wrist, proprio, seed=t, device=device)
            action_chunk = res['candidate_action_env']
            simvla_seed = res['simvla_seed']
        
        action = action_chunk[t % 10].numpy()
        
        # 3. Record metrics before step
        obj_pos = object_body_positions(env)
        contact = contact_summary(env)
        task_vals = _trace_task_values(obs, obj_pos, task_context)
        phase = detect_phase(obs, env, task_context)
        
        # Goal position extraction
        goal_base = task_context.get("goal_base")
        gp = obs_pos(obs, goal_base)
        if gp is None:
            gp = body_pos_by_prefix(obj_pos, task_context.get("goal_body_prefix"))
        
        metrics = {
            "run_id": run_id,
            "suite": suite,
            "task_id": task_id,
            "task_instruction": task_lang,
            "env_seed": env_seed,
            "simvla_seed": simvla_seed,
            "timestep": t,
            "chunk_index": t // 10,
            "reward": float(env.reward()) if hasattr(env, 'reward') else 0.0,
            "success": bool(check_success(env)),
            "done": bool(done),
            "action": action.tolist(),
            "proprio": proprio.tolist(),
            "eef_pos": _safe_float_list(eef_pos(obs)),
            "gripper": _safe_float_list(gripper(obs)),
            "object_positions": obj_pos,
            "target_object": task_context.get("target_base", ""),
            "target_object_pos": task_vals["target_object_position"],
            "goal_pos": _safe_float_list(gp),
            "target_goal_distance": task_vals["object_goal_distance"],
            "eef_target_distance": task_vals["eef_target_distance"],
            "object_height": task_vals["target_object_height"],
            "contact_info": contact,
            "phase": phase,
            "notes": ""
        }
        step_metrics.append(metrics)
        
        actions_data.append({
            "timestep": t,
            "action": action.tolist(),
            "action_chunk": action_chunk.tolist() if t % 10 == 0 else None
        })
        
        # 4. Create overlays
        overlay_lines = [
            f"Run: {run_id} | {suite} | T:{task_id}",
            f"Instr: {task_lang[:40]}",
            f"Step: {t} | Phase: {phase}",
            f"Success: {metrics['success']} | Done: {done}",
            f"ChunkIdx: {t // 10}",
            "manual label: write failure_start_t in annotation_sheet"
        ]
        
        img_agent_ov = overlay_text(img_agent.copy(), overlay_lines)
        img_wrist_ov = overlay_text(img_wrist.copy(), overlay_lines)
        
        # Side by side
        side_by_side = np.hstack([img_agent_ov, img_wrist_ov])
        
        frames_agent.append(img_agent_ov)
        frames_wrist.append(img_wrist_ov)
        frames_side.append(side_by_side)
        
        # 5. Step env
        obs, reward, done, info = env.step(action)
        success = bool(check_success(env))
        if success:
            # Record final state success
            metrics["success"] = True
            break
        if done:
            break
            
    return {
        "success": success,
        "frames_agent": frames_agent,
        "frames_wrist": frames_wrist,
        "frames_side": frames_side,
        "step_metrics": step_metrics,
        "actions_data": actions_data,
        "final_t": t,
        "task_context": task_context,
        "final_reward": float(env.reward()) if hasattr(env, 'reward') else 0.0
    }

def save_csv(path, data):
    if not data: return
    keys = data[0].keys()
    with open(path, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=[0])
    parser.add_argument("--target-failure-videos", type=int, default=10)
    parser.add_argument("--max-attempts", type=int, default=30)
    parser.add_argument("--max-steps", type=int, default=400)
    parser.add_argument("--fps", type=int, default=10)
    parser.add_argument("--out-dir", type=str, required=True)
    args = parser.parse_args()
    
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Load SimVLA
    print("Loading SimVLA...")
    model, processor, device = load_simvla()
    
    failures_found = 0
    attempts = 0
    
    all_runs_summary = []
    
    # Define tasks to rotate through
    tasks = []
    for suite in args.suites:
        for tid in args.task_ids:
            tasks.append((suite, tid))
    
    import random
    random.shuffle(tasks)
    
    while failures_found < args.target_failure_videos and attempts < args.max_attempts:
        suite, task_id = tasks[attempts % len(tasks)]
        
        print(f"Attempt {attempts+1}/{args.max_attempts} | Suite: {suite}, Task: {task_id}")
        
        env_seed = 20260521 + attempts
        try:
            env, bundle = make_env(suite, task_id, seed=env_seed)
            task_lang = bundle["task"].language
        except Exception as e:
            print(f"Error creating env: {e}")
            attempts += 1
            continue
            
        run_name = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{attempts:04d}"
        
        res = run_episode(env, model, processor, device, task_lang, task_id, suite, run_name, env_seed=env_seed, max_steps=args.max_steps, fps=args.fps)
        attempts += 1
        
        is_failure = not res['success']
        
        # Decide whether to save (mostly failures, but some successes for control)
        should_save = is_failure or (failures_found < 5) # save first few even if success for control
        
        if should_save:
            label = "failure" if is_failure else "control_success"
            if is_failure:
                failures_found += 1
                fid = f"failure_{failures_found:04d}"
            else:
                fid = f"success_{attempts:04d}"
            
            run_dir = out_dir / "runs" / fid
            run_dir.mkdir(parents=True, exist_ok=True)
            
            # Save videos
            create_video(res['frames_agent'], run_dir / f"{fid}_agent.mp4", fps=args.fps)
            create_video(res['frames_wrist'], run_dir / f"{fid}_wrist.mp4", fps=args.fps)
            create_video(res['frames_side'], run_dir / f"{fid}_side_by_side.mp4", fps=args.fps)
            
            # Save metrics
            with open(run_dir / "per_step_metrics.jsonl", "w") as f:
                for row in res['step_metrics']:
                    f.write(json.dumps(row) + "\n")
            
            # Save CSV metrics
            csv_data = []
            for m in res['step_metrics']:
                # Flatten dicts for CSV
                row = m.copy()
                row['object_positions'] = json.dumps(row['object_positions'])
                row['contact_info'] = json.dumps(row['contact_info'])
                csv_data.append(row)
            save_csv(run_dir / "per_step_metrics.csv", csv_data)
            
            # Save actions
            with open(run_dir / "actions.jsonl", "w") as f:
                for row in res['actions_data']:
                    f.write(json.dumps(row) + "\n")
            
            # Save ROI template
            roi = {
                "run_id": fid,
                "manual_failure_start_t": None,
                "roi_before": 20,
                "roi_after": 40,
                "analysis_window": "manual_failure_start_t -20 to +40",
                "metrics_file": "per_step_metrics.jsonl",
                "actions_file": "actions.jsonl"
            }
            with open(run_dir / "roi_template.json", "w") as f:
                json.dump(roi, f, indent=2)
            
            # Save metadata
            meta = {
                "run_id": fid,
                "original_run_id": run_name,
                "suite": suite,
                "task_id": task_id,
                "task_instruction": task_lang,
                "env_seed": env_seed,
                "num_steps": int(res['final_t']),
                "success": bool(res['success']),
                "final_reward": float(res['final_reward']),
                "attempts_so_far": int(attempts)
            }
            with open(run_dir / "run_metadata.json", "w") as f:
                json.dump(meta, f, indent=2)
            
            all_runs_summary.append(meta)
            print(f"Saved {label} {fid} | Failures found: {failures_found}/{args.target_failure_videos}")
        else:
            print("Episode succeeded and we have enough controls, skipping save.")
        
        env.close()
            
    # Save overall summary
    save_csv(out_dir / "overall_summary.csv", all_runs_summary)
    print(f"Done. Found {failures_found} failures in {attempts} attempts.")

if __name__ == "__main__":
    main()
