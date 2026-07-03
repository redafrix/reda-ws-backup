import torch
import os
import argparse

def merge(primary_path, secondary_path, output_path):
    print(f"Loading primary: {primary_path}")
    primary = torch.load(primary_path)
    
    print(f"Loading secondary: {secondary_path}")
    secondary = torch.load(secondary_path)
    
    merged_episodes = primary['episodes'] + secondary['episodes']
    
    torch.save({'episodes': merged_episodes}, output_path)
    print(f"Merged {len(primary['episodes'])} + {len(secondary['episodes'])} = {len(merged_episodes)} episodes.")
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=str, required=True)
    parser.add_argument("--secondary", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    merge(args.primary, args.secondary, args.output)
