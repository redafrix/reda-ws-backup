from __future__ import annotations
import torch

def tdqc_mc_brier_loss(
    q_online: torch.Tensor,
    failure: torch.Tensor, # Expected [B, T] now
    mask: torch.Tensor,
    fail_weight: float = 1.0,
    success_weight: float = 1.0,
) -> torch.Tensor:
    """
    Monte Carlo (MC) Brier loss: each step predicts its per-step label.
    """
    targets = failure # Already [B, T]
    
    with torch.no_grad():
        # Global weighting per episode (if any step in the episode is a failure, use fail_weight)
        # Or we could weight only the failure steps. Let's keep it simple for now.
        is_fail_ep = (failure.sum(dim=1) > 0).float()
        sample_w = torch.where(
            is_fail_ep > 0.5,
            torch.tensor(float(fail_weight), device=failure.device),
            torch.tensor(float(success_weight), device=failure.device),
        )
        weights = sample_w[:, None] * mask

    losses = (q_online - targets).pow(2)
    loss = (losses * weights).sum() / weights.sum().clamp_min(1.0)
    return loss

@torch.no_grad()
def sequential_brier_score(
    q: torch.Tensor,
    failure: torch.Tensor, # Expected [B, T]
    mask: torch.Tensor,
) -> torch.Tensor:
    return ((q - failure).pow(2) * mask).sum() / mask.sum().clamp_min(1.0)
