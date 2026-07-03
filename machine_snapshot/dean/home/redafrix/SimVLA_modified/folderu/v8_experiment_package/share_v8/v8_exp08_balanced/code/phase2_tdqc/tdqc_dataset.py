from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import torch
from torch.utils.data import Dataset

SUITE_TO_ID = { 
    "libero_10_lan": 0,
    "libero_10_object": 1,                                                                                                                                                                                
    "libero_10_swap": 2,  
    "libero_goal_lan": 3,                                                                                                                                                                                 
    "libero_goal_swap": 4,
    "libero_object_lan": 5,
    "libero_object_object": 6,                                                                                                                                                                            
    "libero_object_swap": 7,  
    "libero_spatial_lan": 8,                                                                                                                                                                              
    "libero_spatial_object": 9,                                                                                                                                                                           
    "libero_spatial_swap": 10, 
}

@dataclass
class TDQCEpisode:
    features: torch.Tensor      # [T, F]
    success: int                # 1 success, 0 failure
    suite_id: int = -1
    episode_idx: int = -1
    instruction: str = ""

    @property
    def failure(self) -> int:
        return 1 - int(self.success)

    @property
    def length(self) -> int:
        return int(self.features.shape[0])


class TDQCDataset(Dataset):
    def __init__(self, path: str | Path):
        self.path = Path(path)
        obj = torch.load(self.path, map_location="cpu")

        if isinstance(obj, dict) and "episodes" in obj:
            raw_episodes = obj["episodes"]
        elif isinstance(obj, list):
            raw_episodes = obj
        else:
            raise ValueError(
                "Dataset must be either a list of episodes or a dict with key 'episodes'."
            )

        from tqdm import tqdm
        self.episodes: List[TDQCEpisode] = []
        print(f"Processing {len(raw_episodes)} episodes...")
        for ep in tqdm(raw_episodes, desc="Loading Episodes"):
            features = ep["features"]
            if not isinstance(features, torch.Tensor):
                features = torch.tensor(features, dtype=torch.float32)
            else:
                features = features.float()
            
            success = int(ep["success"])
            self.episodes.append(
                TDQCEpisode(
                    features=features,
                    success=success,
                    suite_id=SUITE_TO_ID.get(ep.get("task_suite", ""), -1),
                    episode_idx=int(ep.get("episode_idx", -1)),
                    instruction=str(ep.get("instruction", "")),
                )
            )

        if len(self.episodes) == 0:
            raise ValueError(f"No episodes found in {self.path}")

        self.input_dim = int(self.episodes[0].features.shape[-1])

    def __len__(self) -> int:
        return len(self.episodes)

    def __getitem__(self, idx: int) -> TDQCEpisode:
        return self.episodes[idx]


def tdqc_collate(batch: List[TDQCEpisode]) -> Dict[str, torch.Tensor]:
    B = len(batch)
    T_max = max(ep.length for ep in batch)
    F = batch[0].features.shape[-1]

    features = torch.zeros(B, T_max, F, dtype=torch.float32)
    mask = torch.zeros(B, T_max, dtype=torch.float32)
    lengths = torch.zeros(B, dtype=torch.long)
    success = torch.zeros(B, dtype=torch.float32)
    suite_id = torch.zeros(B, dtype=torch.long)
    episode_idx = torch.zeros(B, dtype=torch.long)

    for b, ep in enumerate(batch):
        T = ep.length
        features[b, :T] = ep.features
        mask[b, :T] = 1.0
        lengths[b] = T
        success[b] = float(ep.success)
        suite_id[b] = int(ep.suite_id)
        episode_idx[b] = int(ep.episode_idx)

    failure = 1.0 - success

    return {
        "features": features,
        "mask": mask,
        "lengths": lengths,
        "success": success,
        "failure": failure,
        "suite_id": suite_id,
        "episode_idx": episode_idx,
    }
