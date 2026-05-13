from __future__ import annotations

from typing import Dict, List

import numpy as np
import torch

from .model import predict_tdqc_sequence


def binary_auroc(scores: np.ndarray, labels: np.ndarray) -> float:
    """Compute AUROC without sklearn. labels: 1 for failure, 0 for success."""
    scores = np.asarray(scores, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    pos = labels == 1
    neg = labels == 0
    n_pos = int(pos.sum())
    n_neg = int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        return float("nan")

    order = np.argsort(scores)
    ranks = np.empty_like(order, dtype=np.float64)
    ranks[order] = np.arange(1, len(scores) + 1, dtype=np.float64)

    # Average ranks for ties.
    sorted_scores = scores[order]
    start = 0
    while start < len(scores):
        end = start + 1
        while end < len(scores) and sorted_scores[end] == sorted_scores[start]:
            end += 1
        if end - start > 1:
            avg_rank = (start + 1 + end) / 2.0
            ranks[order[start:end]] = avg_rank
        start = end

    sum_pos_ranks = ranks[pos].sum()
    auc = (sum_pos_ranks - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg)
    return float(auc)


@torch.no_grad()
def evaluate_calibrator(model, loader, device: torch.device) -> Dict[str, float]:
    model.eval()
    all_step_losses: List[float] = []
    all_max_scores: List[float] = []
    all_final_scores: List[float] = []
    all_labels: List[int] = []

    for batch in loader:
        features = batch["features"].to(device)
        masks = batch["valid_masks"].to(device)
        failure = batch["failure"].to(device)
        lengths = batch["lengths"].to(device)

        q = predict_tdqc_sequence(
            model,
            features,
            masks,
            window_batch_size=getattr(model, "window_eval_batch_size", None),
        )
        y = failure[:, None].expand_as(q)
        step_loss = ((q - y).pow(2) * masks).sum() / masks.sum().clamp_min(1.0)
        all_step_losses.append(float(step_loss.cpu()))

        for b in range(q.shape[0]):
            L = int(lengths[b].item())
            if L <= 0:
                continue
            valid_q = q[b, :L]
            all_max_scores.append(float(valid_q.max().cpu()))
            all_final_scores.append(float(valid_q[-1].cpu()))
            all_labels.append(int(failure[b].item()))

    if not all_labels:
        return {"seq_brier": float("nan"), "terminal_auroc": float("nan"), "max_auroc": float("nan")}

    labels = np.asarray(all_labels, dtype=np.int64)
    max_scores = np.asarray(all_max_scores, dtype=np.float64)
    final_scores = np.asarray(all_final_scores, dtype=np.float64)
    seq_brier = float(np.mean(all_step_losses)) if all_step_losses else float("nan")
    terminal_brier = float(np.mean((final_scores - labels) ** 2))
    max_brier = float(np.mean((max_scores - labels) ** 2))
    return {
        "seq_brier": seq_brier,
        "terminal_brier": terminal_brier,
        "max_brier": max_brier,
        "terminal_auroc": binary_auroc(final_scores, labels),
        "max_auroc": binary_auroc(max_scores, labels),
        "mean_failure_rate": float(labels.mean()),
    }
