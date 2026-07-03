import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import List, Dict, Any, Union

class RNDTarget(nn.Module):
    def __init__(self, input_dim: int, output_dim: int = 512, hidden_dim: int = 1024):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LeakyReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
        # Freeze weights
        for p in self.parameters():
            p.requires_grad = False
            
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)

class RNDPredictor(nn.Module):
    def __init__(self, input_dim: int, output_dim: int = 512, hidden_dim: int = 1024):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LeakyReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)

def build_feature_vector(sample: Dict[str, Any], mode: str = "deployable_numeric") -> np.ndarray:
    """
    Extracts or constructs the feature vector for RND.
    Modes:
      - 'simvla_embedding': Extract pooled VLM features (internal visual/language embeddings).
      - 'deployable_numeric': Fallback option using proprio and historic actions.
    """
    if mode == "simvla_embedding":
        # TODO: SimVLA internal visual/language observation embeddings (pooled_vlm_features)
        # are extracted at runtime by sample_candidate() in simvla_candidate_sampler.py.
        # However, they are NOT saved in the counterfactual_samples.jsonl dataset files.
        # If we need them here, we either need to:
        #   1. Re-run SimVLA on the raw images to extract features.
        #   2. Modify data collection to save 'pooled_vlm_features' in the output JSONL files.
        #
        # For now, check if 'pooled_vlm_features' or 'vlm_features' exists in the sample.
        vlm_features = sample.get("pooled_vlm_features") or sample.get("candidate_action", {}).get("pooled_vlm_features")
        if vlm_features is not None:
            return np.array(vlm_features, dtype=np.float32)
        
        # Fall back to deployable_numeric with warning
        # print("Warning: simvla_embedding requested but not found in sample. Falling back to deployable_numeric.")
        mode = "deployable_numeric"
        
    if mode == "deployable_numeric":
        # Extract current proprio (e.g., 7-dim joint/EEF positions + gripper)
        current = sample.get("current") or {}
        proprio = current.get("proprio") or []
        
        # Extract history proprio if available
        history = sample.get("history") or []
        history_features = []
        for hist_step in history:
            if isinstance(hist_step, dict):
                # check if there is proprio
                h_proprio = hist_step.get("proprio") or hist_step.get("current", {}).get("proprio") or []
                history_features.extend(h_proprio)
                # check if there is action
                h_action = hist_step.get("action") or hist_step.get("candidate_action", {}).get("candidate_action_normalized") or []
                if isinstance(h_action, list):
                    if len(h_action) > 0 and isinstance(h_action[0], list):
                        # flatten action chunk if it's a list of lists
                        for a in h_action:
                            history_features.extend(a)
                    else:
                        history_features.extend(h_action)
                        
        # Pad or truncate history_features to keep a fixed size (e.g. last 8 steps)
        # Suppose each step is 7-dim proprio + 7-dim action = 14 dims.
        # For 8 steps, history is 112 dims.
        # Let's flatten everything and pad to 128 dims.
        feature_vector = list(proprio) + list(history_features)
        
        target_len = 128
        if len(feature_vector) < target_len:
            feature_vector = feature_vector + [0.0] * (target_len - len(feature_vector))
        else:
            feature_vector = feature_vector[:target_len]
            
        return np.array(feature_vector, dtype=np.float32)
        
    raise ValueError(f"Unknown feature mode: {mode}")

def fit_rnd_success_only(
    success_samples: List[Dict[str, Any]],
    mode: str = "deployable_numeric",
    epochs: int = 10,
    lr: float = 1e-4,
    batch_size: int = 32,
    device: str = "cpu"
) -> tuple:
    """
    Fits an RND model on success-only calibration anchors.
    This function sets up the training pipeline but does not run by default unless triggered.
    """
    print(f"RND training scaffold called on {len(success_samples)} success-only samples (Mode: {mode})")
    
    # 1. Extract feature vectors
    features = []
    for sample in success_samples:
        vec = build_feature_vector(sample, mode)
        features.append(vec)
        
    if not features:
        print("No features extracted. Training aborted.")
        return None, None
        
    features = np.array(features, dtype=np.float32)
    input_dim = features.shape[1]
    
    # 2. Instantiate networks
    target = RNDTarget(input_dim=input_dim).to(device)
    predictor = RNDPredictor(input_dim=input_dim).to(device)
    
    optimizer = optim.Adam(predictor.parameters(), lr=lr)
    criterion = nn.MSELoss()
    
    # Convert to PyTorch Tensor
    features_t = torch.tensor(features, dtype=torch.float32).to(device)
    
    # 3. Dummy/real training loop
    print("Scaffolding training loop:")
    for epoch in range(epochs):
        predictor.train()
        permutation = torch.randperm(features_t.size(0))
        epoch_loss = 0.0
        
        for i in range(0, features_t.size(0), batch_size):
            indices = permutation[i:i+batch_size]
            batch_x = features_t[indices]
            
            optimizer.zero_grad()
            with torch.no_grad():
                target_y = target(batch_x)
            pred_y = predictor(batch_x)
            
            loss = criterion(pred_y, target_y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * batch_x.size(0)
            
        epoch_loss /= features_t.size(0)
        print(f"  Epoch {epoch+1}/{epochs} - Distillation Loss: {epoch_loss:.6f}")
        
    print("Scaffolding training completed.")
    return predictor, target

def score_rnd(
    predictor: nn.Module,
    target: nn.Module,
    sample: Dict[str, Any],
    mode: str = "deployable_numeric",
    device: str = "cpu"
) -> float:
    """
    Computes the RND score (distillation error) for a single sample.
    """
    predictor.eval()
    vec = build_feature_vector(sample, mode)
    vec_t = torch.tensor(vec, dtype=torch.float32).unsqueeze(0).to(device)
    
    with torch.no_grad():
        target_y = target(vec_t)
        pred_y = predictor(vec_t)
        # Compute mean squared error (unreduced distance)
        loss = torch.mean((pred_y - target_y) ** 2, dim=-1)
        
    return float(loss.cpu().item())
