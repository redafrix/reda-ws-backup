import torch
import numpy as np

def audit(path):
    data = torch.load(path)
    episodes = data['episodes']
    
    total = len(episodes)
    successes = sum([1 for e in episodes if e.get('success', False)])
    failures = total - successes
    
    print(f"Dataset Audit: {path}")
    print(f"Total Episodes: {total}")
    print(f"Successes: {successes} ({successes/total*100:.1f}%)")
    print(f"Failures:  {failures} ({failures/total*100:.1f}%)")
    
    if total > 0:
        sample_feat = np.array(episodes[0]['features'])
        print(f"Sample Feature Shape: {sample_feat.shape}")
        
audit("intern_ship_ws/runs/tdqc_dataset/final_calibrated_3492rollouts.pt")
