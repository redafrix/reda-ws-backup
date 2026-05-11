import os, sys, shutil

base_dir = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests'

# 1. Update tdqc_dataset.py
dataset_code = '''from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List
import torch
from torch.utils.data import Dataset
import random

@dataclass
class TDQCEpisode:
    features: torch.Tensor
    success: int
    task_id: int = -1
    episode_idx: int = -1
    instruction: str = ""

    @property
    def failure(self) -> int:
        return 1 - int(self.success)

    @property
    def length(self) -> int:
        return int(self.features.shape[0])

class TDQCDataset(Dataset):
    def __init__(self, path: str | Path, max_horizon: int = 150, is_train: bool = False):
        self.path = Path(path)
        self.max_horizon = max_horizon
        self.is_train = is_train
        obj = torch.load(self.path, map_location="cpu")
        raw_episodes = obj["episodes"] if isinstance(obj, dict) else obj
        
        self.episodes: List[TDQCEpisode] = []
        for ep in raw_episodes:
            features = ep["features"]
            if not isinstance(features, torch.Tensor):
                features = torch.tensor(features, dtype=torch.float32)
            else:
                features = features.float()
            
            self.episodes.append(TDQCEpisode(
                features=features,
                success=int(ep["success"]),
                task_id=int(ep.get("task_id", -1)),
                episode_idx=int(ep.get("episode_idx", -1)),
                instruction=str(ep.get("instruction", "")),
            ))
        self.input_dim = int(self.episodes[0].features.shape[-1])

    def __len__(self) -> int: return len(self.episodes)
    
    def __getitem__(self, idx: int) -> TDQCEpisode:
        ep = self.episodes[idx]
        features = ep.features
        L = features.shape[0]
        
        if self.is_train:
            # End-anchored random truncation to destroy Timer Bias
            min_len = 50
            if L > min_len:
                H = random.randint(min_len, min(L, self.max_horizon))
                features = features[-H:]
            else:
                features = features[-self.max_horizon:]
        else:
            if L > self.max_horizon:
                features = features[-self.max_horizon:]
                
        return TDQCEpisode(
            features=features,
            success=ep.success,
            task_id=ep.task_id,
            episode_idx=ep.episode_idx,
            instruction=ep.instruction
        )

def tdqc_collate(batch: List[TDQCEpisode]) -> Dict[str, torch.Tensor]:
    B = len(batch)
    T_max = max(ep.length for ep in batch)
    F = batch[0].features.shape[-1]
    features = torch.zeros(B, T_max, F)
    mask = torch.zeros(B, T_max)
    lengths = torch.zeros(B, dtype=torch.long)
    success = torch.zeros(B)
    for b, ep in enumerate(batch):
        T = ep.length
        features[b, :T] = ep.features
        mask[b, :T] = 1.0
        lengths[b] = T
        success[b] = float(ep.success)
    return {"features": features, "mask": mask, "lengths": lengths, "success": success, "failure": 1.0 - success}
'''
for i in range(101, 115):
    with open(f'{base_dir}/idea_{i:03d}/phase2_tdqc/tdqc_dataset.py', 'w') as f:
        f.write(dataset_code)

# 2. Update train_tdqc.py to use is_train=True
for i in range(101, 115):
    train_path = f'{base_dir}/idea_{i:03d}/phase2_tdqc/train_tdqc.py'
    if os.path.exists(train_path):
        with open(train_path, 'r') as f:
            content = f.read()
        content = content.replace('TDQCDataset(args.dataset_path, max_horizon=150)', 'TDQCDataset(args.dataset_path, max_horizon=150, is_train=True)')
        # Fix idea 109 future import
        if i == 109:
            lines = content.split('\n')
            for j, line in enumerate(lines):
                if 'from __future__' in line:
                    lines.pop(j)
                    lines.insert(0, line)
                    break
            content = '\n'.join(lines)
            
        with open(train_path, 'w') as f:
            f.write(content)

# 3. Update eval_tdqc.py to use is_train=False
for i in range(101, 115):
    eval_path = f'{base_dir}/idea_{i:03d}/phase2_tdqc/eval_tdqc.py'
    if os.path.exists(eval_path):
        with open(eval_path, 'r') as f:
            content = f.read()
        content = content.replace('TDQCDataset(args.dataset_path, max_horizon=150)', 'TDQCDataset(args.dataset_path, max_horizon=150, is_train=False)')
        content = content.replace('TDQCDataset(args.dataset_path, max_horizon=400)', 'TDQCDataset(args.dataset_path, max_horizon=150, is_train=False)')
        with open(eval_path, 'w') as f:
            f.write(content)

# 4. Specific bug fixes
# Idea 102
i102_train = f'{base_dir}/idea_102/phase2_tdqc/train_tdqc.py'
if os.path.exists(i102_train):
    with open(i102_train, 'r') as f:
        content = f.read()
    content = content.replace('            raw_x = normalize', '        raw_x = normalize')
    content = content.replace('            delta_x = torch.zeros', '        delta_x = torch.zeros')
    content = content.replace('            delta_x[:, 1:, :] = raw_x', '        delta_x[:, 1:, :] = raw_x')
    content = content.replace('            x = torch.cat', '        x = torch.cat')
    with open(i102_train, 'w') as f:
        f.write(content)

# Idea 104
i104_model = f'{base_dir}/idea_104/phase2_tdqc/tdqc_model.py'
if os.path.exists(i104_model):
    with open(i104_model, 'r') as f:
        content = f.read()
    content = content.replace('logits = self.head(x) + self.head(x.mean(dim=1, keepdim=True)).expand(-1, x.size(1), -1).squeeze(-1)', 'logits = self.head(x).squeeze(-1) + self.head(x.mean(dim=1, keepdim=True)).expand(-1, x.size(1), -1).squeeze(-1)')
    with open(i104_model, 'w') as f:
        f.write(content)

# Idea 107
i107_model = f'{base_dir}/idea_107/phase2_tdqc/tdqc_model.py'
if os.path.exists(i107_model):
    with open(i107_model, 'r') as f:
        lines = f.readlines()
    with open(i107_model, 'w') as f:
        for line in lines:
            if line.strip() == 'else:':
                continue # remove it entirely, it shouldn't be there
            # also remove duplicate lines that were under else
            if 'T = x.size(1)' in line and lines.index(line) > 165:
                continue
            if 'bias = torch.arange(T' in line and lines.index(line) > 165:
                continue
            if 'bias = -torch.abs(bias' in line and lines.index(line) > 165:
                continue
            if 'attn_mask = (causal_mask + bias).unsqueeze(0).unsqueeze(0)' in line and 'float_pad_mask' not in line:
                continue
            f.write(line)

print("All datasets, training scripts, and buggy models updated successfully.")
