from __future__ import annotations

import torch
from torch import nn
from torch.nn import functional as F


def compute_stage9_loss(outputs: dict[str, torch.Tensor], batch: dict[str, torch.Tensor], target_mode: str) -> tuple[torch.Tensor, dict[str, float]]:
    if target_mode == "ordinal":
        logits = outputs["risk_logits"]
        loss = F.cross_entropy(logits, batch["ordinal"], reduction="mean")
        return loss, {"ordinal_ce": float(loss.detach().cpu())}

    logits = outputs["risk_logits"].squeeze(-1)
    weights = batch["weight"].float()
    bce = F.binary_cross_entropy_with_logits(logits, batch["target"].float(), reduction="none")
    denom = torch.clamp(weights.sum(), min=1.0)
    risk_loss = (bce * weights).sum() / denom
    if target_mode != "subtype_multitask":
        return risk_loss, {"risk_bce": float(risk_loss.detach().cpu())}

    subtype_logits = outputs.get("subtype_logits")
    subtype_target = batch["subtype"]
    subtype_mask = subtype_target >= 0
    if subtype_logits is not None and subtype_mask.any():
        subtype_loss = F.cross_entropy(subtype_logits[subtype_mask], subtype_target[subtype_mask], reduction="mean")
    else:
        subtype_loss = torch.zeros((), device=logits.device)
    total = risk_loss + 0.35 * subtype_loss
    return total, {
        "risk_bce": float(risk_loss.detach().cpu()),
        "subtype_ce": float(subtype_loss.detach().cpu()),
        "total": float(total.detach().cpu()),
    }


def risk_prob_from_outputs(outputs: dict[str, torch.Tensor], target_mode: str) -> torch.Tensor:
    logits = outputs["risk_logits"]
    if target_mode == "ordinal":
        probs = torch.softmax(logits, dim=-1)
        # Deployment risk is the probability of the VALIDATED_BAD ordinal class.
        return probs[:, 3]
    return torch.sigmoid(logits.squeeze(-1))
