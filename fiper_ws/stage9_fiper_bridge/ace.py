import numpy as np
from typing import List, Dict, Any
from .stage9_io import read_jsonl, group_by_state_id, get_state_id

def load_same_state_groups(jsonl_path: str) -> Dict[str, List[Dict[str, Any]]]:
    rows = read_jsonl(jsonl_path)
    return group_by_state_id(rows)

def extract_action_chunks(group: List[Dict[str, Any]]) -> np.ndarray:
    """
    Extract action chunks from the group.
    Returns np.ndarray of shape (num_candidates, horizon, action_dim).
    """
    chunks = []
    for sample in group:
        cand_action = sample.get("candidate_action") or {}
        # Try normalized action first, then env action
        act = cand_action.get("candidate_action_normalized") or cand_action.get("candidate_action_env")
        if act is not None:
            chunks.append(act)
    if not chunks:
        # Try looking at top level candidate_action or actions
        for sample in group:
            act = sample.get("candidate_action_normalized") or sample.get("candidate_action_env") or sample.get("candidate_action")
            if isinstance(act, list):
                chunks.append(act)
    return np.array(chunks, dtype=np.float32)

def compute_action_chunk_diversity(action_chunks: np.ndarray) -> float:
    """
    Compute trajectory pairwise distance.
    action_chunks shape: (N, H, D)
    """
    N, H, D = action_chunks.shape
    if N <= 1:
        return 0.0
    flat_chunks = action_chunks.reshape(N, H * D)
    # Compute pairwise Euclidean distances
    dists = np.linalg.norm(flat_chunks[:, None, :] - flat_chunks[None, :, :], axis=-1)
    # Mean of off-diagonal elements
    triu_indices = np.triu_indices(N, k=1)
    mean_dist = np.mean(dists[triu_indices])
    return float(mean_dist)

def compute_gaussian_entropy(action_chunks: np.ndarray, eps: float = 1e-6) -> float:
    """
    Compute Gaussian entropy approximation of the action chunks.
    action_chunks shape: (N, H, D)
    """
    N, H, D = action_chunks.shape
    dim = H * D
    if N <= 1:
        return 0.0
    flat_chunks = action_chunks.reshape(N, dim)
    
    # Compute covariance matrix
    cov = np.cov(flat_chunks, rowvar=False)
    
    # Regularize to ensure positive definiteness
    if dim == 1:
        cov = np.array([[cov]])
    cov = cov + eps * np.eye(dim)
    
    # Compute log determinant
    sign, logdet = np.linalg.slogdet(cov)
    if sign <= 0:
        # Fallback in case of numeric instability
        return 0.0
        
    entropy = 0.5 * (dim * (1.0 + np.log(2.0 * np.pi)) + logdet)
    return float(entropy)

def compute_stepwise_action_std(action_chunks: np.ndarray) -> List[float]:
    """
    Compute per-step action standard deviation.
    action_chunks shape: (N, H, D)
    """
    if action_chunks.ndim < 3 or action_chunks.shape[0] <= 1:
        return [0.0] * action_chunks.shape[1]
    # std across candidates for each step and dimension
    std_per_step_dim = np.std(action_chunks, axis=0) # (H, D)
    # Average across dimensions for each step
    stepwise_std = np.mean(std_per_step_dim, axis=-1) # (H,)
    return [float(x) for x in stepwise_std]

def compute_gripper_entropy_or_std(action_chunks: np.ndarray) -> float:
    """
    Compute gripper std/entropy.
    Assumes gripper is the last dimension (index 6).
    action_chunks shape: (N, H, D)
    """
    N, H, D = action_chunks.shape
    if D < 7 or N <= 1:
        return 0.0
    gripper_actions = action_chunks[..., 6] # (N, H)
    gripper_std = np.std(gripper_actions, axis=0) # (H,)
    return float(np.mean(gripper_std))

def compute_ace_summary(group: List[Dict[str, Any]]) -> Dict[str, Any]:
    state_id_str = get_state_id(group[0])
    if "_seed" in state_id_str:
        state_id_str = state_id_str.split("_seed")[0]
        
    action_chunks = extract_action_chunks(group)
    if len(action_chunks) == 0:
        return {
            "state_id": state_id_str,
            "num_candidates": 0,
            "ace_score": 0.0,
            "action_std_mean": 0.0,
            "action_pairwise_distance_mean": 0.0,
            "stepwise_std": [],
            "gripper_std": 0.0,
            "translation_std": 0.0,
            "rotation_std": 0.0
        }
        
    N, H, D = action_chunks.shape
    
    # Calculate std elements
    std_per_step_dim = np.std(action_chunks, axis=0) if N > 1 else np.zeros((H, D)) # (H, D)
    
    # Translation (dims 0, 1, 2)
    translation_std = float(np.mean(std_per_step_dim[:, :3])) if D >= 3 else 0.0
    # Rotation (dims 3, 4, 5)
    rotation_std = float(np.mean(std_per_step_dim[:, 3:6])) if D >= 6 else 0.0
    # Gripper (dim 6)
    gripper_std = float(np.mean(std_per_step_dim[:, 6])) if D >= 7 else 0.0
    # Overall action std mean
    action_std_mean = float(np.mean(std_per_step_dim))
    
    # Pairwise distance
    action_pairwise_distance_mean = compute_action_chunk_diversity(action_chunks)
    
    # Stepwise std
    stepwise_std = compute_stepwise_action_std(action_chunks)
    
    # ACE score (Gaussian entropy)
    ace_score = compute_gaussian_entropy(action_chunks)
    
    return {
        "state_id": state_id_str,
        "num_candidates": N,
        "ace_score": ace_score,
        "action_std_mean": action_std_mean,
        "action_pairwise_distance_mean": action_pairwise_distance_mean,
        "stepwise_std": stepwise_std,
        "gripper_std": gripper_std,
        "translation_std": translation_std,
        "rotation_std": rotation_std
    }
