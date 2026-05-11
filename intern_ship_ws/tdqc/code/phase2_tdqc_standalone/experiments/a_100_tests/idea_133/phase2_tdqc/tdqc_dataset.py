from __future__ import annotations
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
