import os
from pathlib import Path

base_dir = Path('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests')
for i in range(200, 250):
    train_path = base_dir / f'idea_{i}' / 'phase2_tdqc' / 'train_tdqc.py'
    if train_path.exists():
        with open(train_path, 'r') as f:
            content = f.read()
        
        # Add prints for visibility
        content = content.replace('dataset = TDQCDataset', 'print("Loading Dataset..."); dataset = TDQCDataset')
        content = content.replace('all_feats = torch.cat', 'print("Concatenating features (this takes a few mins)... "); all_feats = torch.cat')
        content = content.replace('stats = compute_feature_stats', 'print("Computing normalization stats..."); stats = compute_feature_stats')
        content = content.replace('mean, std = stats', 'print("Starting training loop..."); mean, std = stats')
        
        with open(train_path, 'w') as f:
            f.write(content)
