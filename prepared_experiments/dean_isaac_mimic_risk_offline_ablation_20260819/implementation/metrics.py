"""Metrics evaluation for row-level and episode-level risk monitoring (pure numpy)."""

from __future__ import annotations

from typing import Any, Dict, List, Tuple
import numpy as np


def compute_row_metrics(
    y_true: np.ndarray,
    y_scores: np.ndarray,
) -> Dict[str, float]:
    """Compute AUROC and AUPRC on row predictions using pure numpy."""
    yt = np.asarray(y_true, dtype=np.int64)
    ys = np.asarray(y_scores, dtype=np.float64)

    n_pos = int(np.sum(yt == 1))
    n_neg = int(np.sum(yt == 0))

    if n_pos == 0 or n_neg == 0:
        return {"auroc": 0.0, "auprc": 0.0}

    # Sort descending by score
    desc_indices = np.argsort(ys, kind="mergesort")[::-1]
    yt_sorted = yt[desc_indices]
    ys_sorted = ys[desc_indices]

    distinct_indices = np.where(np.diff(ys_sorted))[0]
    threshold_idxs = np.r_[distinct_indices, yt.size - 1]

    tps = np.cumsum(yt_sorted)[threshold_idxs]
    fps = (1 + threshold_idxs) - tps

    tpr = tps / n_pos
    fpr = fps / n_neg

    # AUROC
    tpr_roc = np.r_[0.0, tpr]
    fpr_roc = np.r_[0.0, fpr]
    auroc = float(np.trapz(tpr_roc, fpr_roc))

    # AUPRC (trapezoidal integration of Precision-Recall curve)
    precision = tps / (tps + fps)
    recall = tpr
    precision_pr = np.r_[1.0, precision]
    recall_pr = np.r_[0.0, recall]
    auprc = float(np.sum((recall_pr[1:] - recall_pr[:-1]) * precision_pr[1:]))

    return {
        "auroc": auroc,
        "auprc": auprc,
    }


def compute_episode_evaluation(
    scores: np.ndarray,
    labels: np.ndarray,
    episode_indices: np.ndarray,
    threshold: float,
) -> Dict[str, Any]:
    """
    Compute detailed episode-level evaluation matching the canonical Isaac evaluator:
    fraction = (first_alarm_index + 1) / len(episode_rows)
    det10: fraction <= 0.10
    det25: fraction <= 0.25
    det50: fraction <= 0.50
    """
    scores_arr = np.asarray(scores, dtype=np.float64)
    labels_arr = np.asarray(labels, dtype=np.int64)
    ep_ids_arr = np.asarray(episode_indices, dtype=np.int64)

    unique_eps = np.unique(ep_ids_arr)

    success_total = 0
    success_false_alarms = 0

    failure_total = 0
    failure_detected = 0
    det_10_count = 0
    det_25_count = 0
    det_50_count = 0
    first_alarm_fractions = []

    for ep in unique_eps:
        mask = (ep_ids_arr == ep)
        ep_scores = scores_arr[mask]
        ep_label = labels_arr[mask][0]
        ep_len = len(ep_scores)

        alarm_indices = np.where(ep_scores >= threshold)[0]
        has_alarm = len(alarm_indices) > 0

        if ep_label == 0:
            success_total += 1
            if has_alarm:
                success_false_alarms += 1
        else:
            failure_total += 1
            if has_alarm:
                failure_detected += 1
                first_t = int(alarm_indices[0])
                # Exact parity with evaluate_isaac_topk8.py
                frac = float((first_t + 1) / max(1, ep_len))
                first_alarm_fractions.append(frac)
                if frac <= 0.10:
                    det_10_count += 1
                if frac <= 0.25:
                    det_25_count += 1
                if frac <= 0.50:
                    det_50_count += 1

    never_detected = failure_total - failure_detected
    fpr = float(success_false_alarms / success_total) if success_total > 0 else 0.0
    recall = float(failure_detected / failure_total) if failure_total > 0 else 0.0
    det_10_rate = float(det_10_count / failure_total) if failure_total > 0 else 0.0
    det_25_rate = float(det_25_count / failure_total) if failure_total > 0 else 0.0
    det_50_rate = float(det_50_count / failure_total) if failure_total > 0 else 0.0

    mean_first_alarm_frac = float(np.mean(first_alarm_fractions)) if first_alarm_fractions else None

    return {
        "threshold": float(threshold),
        "success_total": success_total,
        "success_false_alarms": success_false_alarms,
        "fpr": fpr,
        "failure_total": failure_total,
        "failure_detected": failure_detected,
        "recall": recall,
        "det_10_count": det_10_count,
        "det_10_rate": det_10_rate,
        "det_25_count": det_25_count,
        "det_25_rate": det_25_rate,
        "det_50_count": det_50_count,
        "det_50_rate": det_50_rate,
        "never_detected": never_detected,
        "mean_first_alarm_fraction": mean_first_alarm_frac,
    }
