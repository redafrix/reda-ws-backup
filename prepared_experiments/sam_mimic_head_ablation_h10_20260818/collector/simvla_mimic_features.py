
import numpy as np

def generate_genuine_8_candidates(model_call_fn, ...):
    # Generates candidate 0 alone, candidates 1..7 in batch
    pass

def compute_denoising_metrics(X_d: np.ndarray, V_d: np.ndarray) -> dict:
    # X_d: [8, 10, 7], V_d: [8, 10, 7]
    sample_variance = np.var(X_d, axis=0, ddof=0) # [10, 7]
    
    # pairwise mse
    diff = X_d[:, None, :, :] - X_d[None, :, :, :]
    pairwise_mse = np.mean(diff**2) # Simplified mean over all pairs
    
    vel_diff = V_d[:, None, :, :] - V_d[None, :, :, :]
    vel_mse = np.mean(vel_diff**2)
    
    l2_mean = np.mean(np.linalg.norm(V_d, axis=-1))
    
    return {
        "sample_pairwise_mse_mean": float(pairwise_mse),
        "sample_variance_max": float(np.max(sample_variance)),
        "sample_variance_mean": float(np.mean(sample_variance)),
        "sample_velocity_mse_mean": float(vel_mse),
        "vector_field_l2_mean": float(l2_mean)
    }
