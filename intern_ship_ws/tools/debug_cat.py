import torch
from torch.utils.data import DataLoader
import sys
import os

from pathlib import Path
sys.path.append(str(Path(__file__).parent / "intern_ship_ws" / "smolvla_phase2"))
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate

dataset_path = "intern_ship_ws/runs/tdqc_dataset/final_calibrated_3492rollouts.pt"
dataset = TDQCDataset(dataset_path)
loader = DataLoader(dataset, batch_size=64, shuffle=False, collate_fn=tdqc_collate)

all_valid_feats = []
for i, batch in enumerate(loader):
    feats = batch["features"]
    mask = batch["mask"]
    valid_feats = feats[mask == 1.0]
    print(f"Batch {i}: feats shape {feats.shape}, mask shape {mask.shape}, valid_feats shape {valid_feats.shape}")
    all_valid_feats.append(valid_feats)
    try:
        torch.cat(all_valid_feats, dim=0)
    except Exception as e:
        print(f"FAILED at batch {i}!")
        print(f"Error: {e}")
        # Inspect the tensors in the list
        for j, t in enumerate(all_valid_feats):
            print(f"  Tensor {j} shape: {t.shape}")
        break
