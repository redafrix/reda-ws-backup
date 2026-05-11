from __future__ import annotations

import torch


def make_td0_targets(
    q_target: torch.Tensor,
    failure: torch.Tensor,
    lengths: torch.Tensor,
    mask: torch.Tensor,
) -> torch.Tensor:
    """
    Build TD(0) targets for p_fail.

    q_target: [B, T]
    failure:  [B], 1 failed rollout, 0 successful rollout
    lengths:  [B]
    mask:     [B, T]

    Returns:
        target: [B, T]
    """
    B, T = q_target.shape
    target = torch.zeros_like(q_target)

    for b in range(B):
        L = int(lengths[b].item())
        if L <= 0:
            continue
        if L > 1:
            target[b, : L - 1] = q_target[b, 1:L]
        target[b, L - 1] = failure[b]

    # Padding values do not matter because mask removes them.
    return target


def tdqc_brier_td_loss(
    q_online: torch.Tensor,
    q_target: torch.Tensor,
    failure: torch.Tensor,
    lengths: torch.Tensor,
    mask: torch.Tensor,
    fail_weight: float = 1.0,
    success_weight: float = 1.0,
) -> torch.Tensor:
    """
    Masked TDQC loss for failure probability.

    q_online: [B, T]
    q_target: [B, T]
    failure:  [B]
    lengths:  [B]
    mask:     [B, T]
    """
    with torch.no_grad():
        targets = make_td0_targets(q_target, failure, lengths, mask)
        sample_w = torch.where(
            failure > 0.5,
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
    failure: torch.Tensor,
    mask: torch.Tensor,
) -> torch.Tensor:
    """
    Empirical sequential Brier score against terminal failure labels.
    """
    target = failure[:, None].expand_as(q)
    return ((q - target).pow(2) * mask).sum() / mask.sum().clamp_min(1.0)


def tdqc_mc_brier_loss(
    q_online: torch.Tensor,
    failure: torch.Tensor,
    mask: torch.Tensor,
    fail_weight: float = 1.0,
    success_weight: float = 1.0,
) -> torch.Tensor:
    """
    Monte Carlo (MC) Brier loss: each step predicts the terminal failure label.
    """
    # Expand terminal failure label [B] to [B, T]
    targets = failure[:, None].expand_as(q_online)
    
    # Calculate weights based on class
    with torch.no_grad():
        sample_w = torch.where(
            failure > 0.5,
            torch.tensor(float(fail_weight), device=failure.device),
            torch.tensor(float(success_weight), device=failure.device),
        )
        weights = sample_w[:, None] * mask

    losses = (q_online - targets).pow(2)
    loss = (losses * weights).sum() / weights.sum().clamp_min(1.0)
    return loss
