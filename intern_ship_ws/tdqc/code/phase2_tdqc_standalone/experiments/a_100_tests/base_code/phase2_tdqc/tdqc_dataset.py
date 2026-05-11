from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List
import torch
from torch.utils.data import Dataset

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
    def __init__(self, path: str | Path, max_horizon: int = 150):
        self.path = Path(path)
        obj = torch.load(self.path, map_location="cpu")
        raw_episodes = obj["episodes"] if isinstance(obj, dict) else obj
        
        self.episodes: List[TDQCEpisode] = []
        for ep in raw_episodes:
            features = ep["features"]
            if not isinstance(features, torch.Tensor):
                features = torch.tensor(features, dtype=torch.float32)
            else:
                features = features.float()
            
            # TRUNCATION: Match success average to remove Timer Bias
            if features.shape[0] > max_horizon:
                features = features[:max_horizon]
            
            self.episodes.append(TDQCEpisode(
                features=features,
                success=int(ep["success"]),
                task_id=int(ep.get("task_id", -1)),
                episode_idx=int(ep.get("episode_idx", -1)),
                instruction=str(ep.get("instruction", "")),
            ))
        self.input_dim = int(self.episodes[0].features.shape[-1])

    def __len__(self) -> int: return len(self.episodes)
    def __getitem__(self, idx: int) -> TDQCEpisode: return self.episodes[idx]

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
