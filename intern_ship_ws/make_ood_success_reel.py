import os
import argparse
import imageio.v2 as imageio
import numpy as np
from pathlib import Path
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--runs_dir', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--speed', type=float, default=4.0)
    parser.add_argument('--fps', type=int, default=40)
    args = parser.parse_args()

    # We want one success from each task 0-17
    # Structure: runs/task{id}/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl
    
    writer = imageio.get_writer(args.output, fps=args.fps)
    total_frames = 0
    tasks_found = 0
    
    for tid in range(18):
        task_dir = os.path.join(args.runs_dir, f'task{tid}', 'risk_topk8_selected_cap', 'risk_topk8')
        summary_path = os.path.join(task_dir, 'episode_summaries.jsonl')
        
        if not os.path.exists(summary_path):
            print(f'Task {tid} summary not found.')
            continue
            
        # Find first success
        success_idx = None
        with open(summary_path, 'r') as f:
            for line in f:
                data = json.loads(line)
                if data.get('success'):
                    success_idx = data.get('episode_index')
                    break
        
        # If no success, find first failure
        is_failure = False
        if success_idx is None:
            print(f'Task {tid} has no successes. Using failure.')
            is_failure = True
            with open(summary_path, 'r') as f:
                line = f.readline()
                if line:
                    success_idx = json.loads(line).get('episode_index')
        
        if success_idx is not None:
            # We need to render the video. But wait, the runs directory doesn't have MP4s.
            # We assumed they are not saved.
            print(f'Task {tid} found episode {success_idx}. (Placeholder for rendering)')
            tasks_found += 1
            
    writer.close()
    print(f'Done. Found {tasks_found} tasks.')

if __name__ == "__main__":
    main()
