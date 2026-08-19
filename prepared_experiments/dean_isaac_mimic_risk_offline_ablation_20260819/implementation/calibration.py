"""Validation-only calibration module for successful-episode-max thresholds and best-F1."""

from __future__ import annotations

import math
from typing import Any, Dict, List, Tuple
import numpy as np

from .constants import CONFORMAL_ALPHAS, PERCENTILES


def compute_successful_episode_maxima(
    scores: np.ndarray,
    episode_labels: np.ndarray,
    episode_indices: np.ndarray,
) -> Dict[int, float]:
    """
    Compute maximum risk score for each successful validation episode.
    """
    scores_arr = np.asarray(scores, dtype=np.float64)
    labels_arr = np.asarray(episode_labels, dtype=np.int64)
    ep_ids_arr = np.asarray(episode_indices, dtype=np.int64)

    success_maxima: Dict[int, float] = {}
    unique_eps = np.unique(ep_ids_arr)

    for ep in unique_eps:
        mask = (ep_ids_arr == ep)
        ep_label = labels_arr[mask][0]
        if ep_label == 0:
            ep_max = float(np.max(scores_arr[mask]))
            success_maxima[int(ep)] = ep_max

    return success_maxima


def compute_conformal_threshold(
    success_maxima: List[float] | np.ndarray,
    alpha: float,
) -> float:
    """
    Compute corrected episode-max conformal threshold:
    k = min(n, ceil((n + 1) * (1 - alpha)))
    tau_alpha = sorted_maxima[k - 1] (1-indexed k-th order statistic).
    """
    arr = np.sort(np.asarray(success_maxima, dtype=np.float64))
    n = len(arr)
    if n == 0:
        raise ValueError("Cannot calibrate threshold on empty success maxima list")

    k = min(n, math.ceil((n + 1) * (1.0 - alpha)))
    tau = float(arr[k - 1])
    return tau


def compute_best_f1_threshold(
    y_true: np.ndarray,
    y_scores: np.ndarray,
) -> Dict[str, float]:
    """
    Compute validation row best-F1 threshold:
    Candidate thresholds = sorted unique validation scores.
    Alarm convention: score >= threshold.
    Tie-breaking: HIGHEST threshold among equal-max-F1 candidates.
    """
    yt = np.asarray(y_true, dtype=np.int64)
    ys = np.asarray(y_scores, dtype=np.float64)

    n_pos = int(np.sum(yt == 1))
    n_neg = int(np.sum(yt == 0))

    if n_pos == 0:
        return {"threshold": 0.5, "f1": 0.0, "precision": 0.0, "recall": 0.0}

    unique_scores = np.unique(ys)
    # Sort ascending
    unique_scores = np.sort(unique_scores)

    best_f1 = -1.0
    best_threshold = 0.5
    best_p = 0.0
    best_r = 0.0

    for thresh in unique_scores:
        pred_pos = (ys >= thresh)
        tp = int(np.sum(pred_pos & (yt == 1)))
        fp = int(np.sum(pred_pos & (yt == 0)))
        fn = int(np.sum((~pred_pos) & (yt == 1)))

        p = float(tp / (tp + fp)) if (tp + fp) > 0 else 0.0
        r = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        f1 = float(2 * p * r / (p + r)) if (p + r) > 0 else 0.0

        # Tie-break: highest threshold among equal max F1
        if f1 > best_f1 or (f1 == best_f1 and thresh > best_threshold):
            best_f1 = f1
            best_threshold = float(thresh)
            best_p = p
            best_r = r

    return {
        "threshold": best_threshold,
        "f1": best_f1,
        "precision": best_p,
        "recall": best_r,
    }


def compute_calibration_thresholds(
    success_maxima_dict: Dict[int, float],
    val_y_true: np.ndarray | None = None,
    val_y_scores: np.ndarray | None = None,
) -> Dict[str, float]:
    """
    Compute all standard conformal, empirical percentiles, and row best-F1 thresholds.
    """
    maxima_list = list(success_maxima_dict.values())
    if not maxima_list:
        raise ValueError("No successful validation episodes available for calibration")

    thresholds: Dict[str, float] = {
        "fixed_0.5": 0.5,
    }

    # Conformal thresholds
    for alpha in CONFORMAL_ALPHAS:
        tau = compute_conformal_threshold(maxima_list, alpha)
        thresholds[f"conformal_alpha_{alpha:.2f}"] = tau

    # Empirical percentiles
    for pct in PERCENTILES:
        tau = float(np.percentile(maxima_list, pct))
        thresholds[f"empirical_q{pct}"] = tau

    # Row best-F1
    if val_y_true is not None and val_y_scores is not None:
        f1_res = compute_best_f1_threshold(val_y_true, val_y_scores)
        thresholds["row_best_f1"] = f1_res["threshold"]

    return thresholds
