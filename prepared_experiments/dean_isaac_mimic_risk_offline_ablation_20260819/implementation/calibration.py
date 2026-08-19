"""Validation-only calibration module for successful-episode-max thresholds."""

from __future__ import annotations

import math
from typing import Dict, List, Tuple
import numpy as np

from .constants import CONFORMAL_ALPHAS, PERCENTILES


def compute_successful_episode_maxima(
    scores: np.ndarray,
    episode_labels: np.ndarray,
    episode_indices: np.ndarray,
) -> Dict[int, float]:
    """
    Compute maximum risk score for each successful validation episode.
    
    Args:
        scores: [N] float array of sigmoid risk scores
        episode_labels: [N] int array of episode outcome labels (0=success, 1=failure)
        episode_indices: [N] int array of episode IDs
        
    Returns:
        dict mapping successful episode_id -> max risk score
    """
    scores_arr = np.asarray(scores, dtype=np.float64)
    labels_arr = np.asarray(episode_labels, dtype=np.int64)
    ep_ids_arr = np.asarray(episode_indices, dtype=np.int64)

    success_maxima: Dict[int, float] = {}
    unique_eps = np.unique(ep_ids_arr)

    for ep in unique_eps:
        mask = (ep_ids_arr == ep)
        ep_label = labels_arr[mask][0]
        if ep_label == 0:  # Success episode only
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


def compute_calibration_thresholds(
    success_maxima_dict: Dict[int, float],
) -> Dict[str, float]:
    """
    Compute all standard conformal and empirical calibration thresholds from successful episode maxima.
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

    return thresholds
