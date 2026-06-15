import numpy as np
from typing import List, Union, Dict, Any

def constant_quantile_threshold(scores: Union[List[float], List[List[float]]], q: float) -> float:
    """
    Computes the constant quantile threshold.
    If scores is a list of episodes (list of lists), it takes the max of each episode first.
    If scores is a flat list, it directly computes the quantile.
    """
    if not scores:
        return 0.0
    if isinstance(scores[0], list):
        # List of episodes: take max score per episode
        max_scores = [max(episode) for episode in scores if len(episode) > 0]
        if not max_scores:
            return 0.0
        return float(np.quantile(max_scores, q))
    else:
        # Flat list of step-level scores
        return float(np.quantile(scores, q))

def moving_window_scores(scores: List[float], window_size: int) -> List[float]:
    """
    Applies a moving window sum of size window_size to the scores.
    Matches FIPER's _apply_window_size behavior.
    """
    if not scores:
        return []
    window_scores = []
    for i in range(len(scores)):
        start = max(0, i - window_size + 1)
        window_scores.append(float(sum(scores[start:i+1])))
    return window_scores

def calibrate_success_thresholds(
    success_scores: List[List[float]], 
    q: float = 0.95,
    window_size: int = 5
) -> Dict[str, Any]:
    """
    Fits constant and time-varying thresholds using successful calibration episodes.
    """
    # 1. Raw constant threshold
    ct_threshold = constant_quantile_threshold(success_scores, q)
    
    # 2. Moving window constant threshold
    mw_scores = [moving_window_scores(ep, window_size) for ep in success_scores]
    mw_ct_threshold = constant_quantile_threshold(mw_scores, q)
    
    # 3. Time-varying threshold (quantile at each step t)
    # Group scores by step index
    max_len = max([len(ep) for ep in success_scores]) if success_scores else 0
    step_scores = {t: [] for t in range(max_len)}
    for ep in success_scores:
        for t, val in enumerate(ep):
            step_scores[t].append(val)
            
    tvt_thresholds = []
    for t in range(max_len):
        vals = step_scores[t]
        if vals:
            tvt_thresholds.append(float(np.quantile(vals, q)))
        else:
            tvt_thresholds.append(0.0)
            
    return {
        "q": q,
        "window_size": window_size,
        "ct_threshold": ct_threshold,
        "mw_ct_threshold": mw_ct_threshold,
        "tvt_thresholds": tvt_thresholds
    }

def apply_threshold(scores: List[float], threshold: Union[float, List[float]]) -> List[bool]:
    """
    Compares uncertainty scores to a threshold (constant or time-varying).
    Returns a list of booleans where True means alarm (score exceeds threshold).
    """
    alarms = []
    if isinstance(threshold, list):
        # Time-varying threshold
        for t, score in enumerate(scores):
            # Extend threshold with the last value if episode is longer than threshold list
            thresh_val = threshold[t] if t < len(threshold) else threshold[-1]
            alarms.append(bool(score > thresh_val))
    else:
        # Constant threshold
        for score in scores:
            alarms.append(bool(score > threshold))
    return alarms
