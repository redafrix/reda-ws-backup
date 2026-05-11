import torch
import os
import numpy as np

path = "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/final_calibrated_3924rollouts_v2.pt"
data = torch.load(path)
episodes = data['episodes']

print(f"Total episodes: {len(episodes)}")

# Track mins and maxes for each dimension across all steps of all episodes
all_features = []
for ep in episodes:
    feats = torch.tensor(ep['features'])
    if feats.shape[0] > 0:
        all_features.append(feats)

all_features = torch.cat(all_features, dim=0)

print(f"Total steps across all episodes: {all_features.shape[0]}")
print(f"Shape of feature vector: {all_features.shape[1]}")

print("\nFeature statistics (across all steps):")
for dim in range(all_features.shape[1]):
    dim_data = all_features[:, dim]
    print(f"Dim {dim}: min={dim_data.min().item():.6f}, max={dim_data.max().item():.6f}, mean={dim_data.mean().item():.6f}, zeros={(dim_data == 0).sum().item()}")

