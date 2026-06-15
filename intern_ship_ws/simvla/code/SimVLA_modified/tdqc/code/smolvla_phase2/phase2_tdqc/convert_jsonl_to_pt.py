import json
import torch
import os
import argparse
from tqdm import tqdm

def convert(jsonl_path, output_path):
    episodes = []
    print(f"Reading {jsonl_path}...")
    
    with open(jsonl_path, 'r') as f:
        for line in tqdm(f):
            data = json.loads(line)
            
            steps_data = []
            for step in data.get('uncertainty_trace', []):
                # Matching local 'features' structure: 8D [mean_p, std_p, max_p, min_p, mean_h, std_h, max_h, min_h]
                feat = [
                    step.get('mean_path_var', 0.0),
                    0.0, # std_p
                    step.get('max_path_var', 0.0),
                    0.0, # min_p
                    step.get('mean_last_var', 0.0),
                    0.0, # std_h
                    step.get('max_last_var', 0.0),
                    0.0  # min_h
                ]
                steps_data.append(feat)
            
            episodes.append({
                'features': steps_data,
                'success': data.get('success', False),
                'task_id': data.get('task_id', -1),
                'episode_idx': data.get('episode', -1),
                'instruction': data.get('task_description', '')
            })
    
    torch.save({'episodes': episodes}, output_path)
    print(f"Saved {len(episodes)} episodes to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    convert(args.input, args.output)
