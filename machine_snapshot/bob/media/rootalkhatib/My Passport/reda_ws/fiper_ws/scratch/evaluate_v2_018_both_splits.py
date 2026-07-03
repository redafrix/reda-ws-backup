import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd

@dataclass
class EpisodeTrace:
    split: str
    episode_key: str
    scores: list[float]

def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows

def quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    idx = int(math.ceil(q * len(xs))) - 1
    return xs[max(0, min(idx, len(xs) - 1))]

def conformal_upper_threshold(values: list[float], alpha: float) -> float:
    if not values:
        return float('inf')
    xs = sorted(values)
    rank_1indexed = int(math.ceil((len(xs) + 1) * (1.0 - alpha)))
    if rank_1indexed > len(xs):
        return float('inf')
    return xs[max(0, rank_1indexed - 1)]

def trigger_mass(scores: list[float], row_threshold: float, mass_threshold: float) -> int | None:
    mass = 0.0
    for idx, score in enumerate(scores):
        mass += max(0.0, score - row_threshold)
        if mass >= mass_threshold:
            return idx
    return None

def traces_from_row_scores(row_scores: list[tuple]) -> list[EpisodeTrace]:
    grouped = defaultdict(list)
    for split, episode_key, timestep, score in row_scores:
        grouped[(split, episode_key)].append((timestep, score))
    traces = []
    for (split, episode_key), values in grouped.items():
        values.sort(key=lambda item: item[0])
        traces.append(
            EpisodeTrace(
                split=split,
                episode_key=episode_key,
                scores=[float(score) for _, score in values],
            )
        )
    return traces

def calculate_split_metrics(success_traces, failure_traces, row_threshold, mass_threshold):
    success_alarms = []
    for trace in success_traces:
        fired = trigger_mass(trace.scores, row_threshold, mass_threshold)
        success_alarms.append(fired is not None)
    success_fa = np.mean(success_alarms) if success_alarms else 0.0
    
    failure_fired = []
    failure_lengths = []
    for trace in failure_traces:
        fired = trigger_mass(trace.scores, row_threshold, mass_threshold)
        failure_fired.append(fired)
        failure_lengths.append(len(trace.scores))
        
    detected = [f is not None for f in failure_fired]
    failure_det = np.mean(detected) if detected else 0.0
    never_det = 1.0 - failure_det
    
    det_10 = 0
    det_25 = 0
    det_50 = 0
    det_times = []
    
    for fired_idx, length in zip(failure_fired, failure_lengths):
        if fired_idx is not None:
            denom = min(length, 300)
            frac = fired_idx / (denom - 1) if denom > 1 else 0.0
            det_times.append(frac)
            if frac <= 0.10:
                det_10 += 1
            if frac <= 0.25:
                det_25 += 1
            if frac <= 0.50:
                det_50 += 1
                
    n_failures = len(failure_traces)
    det_10_rate = det_10 / n_failures if n_failures > 0 else 0.0
    det_25_rate = det_25 / n_failures if n_failures > 0 else 0.0
    det_50_rate = det_50 / n_failures if n_failures > 0 else 0.0
    mean_time = np.mean(det_times) if det_times else 0.0
    balanced_acc = (failure_det + (1.0 - success_fa)) / 2.0
    
    return {
        'Success FA': success_fa,
        'Failure Det': failure_det,
        'Det@10': det_10_rate,
        'Det@25': det_25_rate,
        'Det@50': det_50_rate,
        'Mean Time': mean_time,
        'Never': never_det,
        'Accuracy': balanced_acc,
        'TPR': failure_det,
        'TNR': 1.0 - success_fa
    }

def main():
    job_dir = Path('/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16')
    scores_path = job_dir / 'scores.jsonl'
    
    rows = read_jsonl(scores_path)
    row_scores = []
    for row in rows:
        split = row['split']
        score_val = row.get('score')
        if score_val is None:
            score_val = row.get('score_eventual')
        row_scores.append(
            (
                split,
                str(row['episode_key']),
                int(row['timestep']),
                float(score_val),
            )
        )
        
    calib_scores = [score for split, _, _, score in row_scores if split == 'success_calib_seen']
    q95 = float(quantile(calib_scores, 0.95))
    
    traces = traces_from_row_scores(row_scores)
    
    val_masses = []
    for trace in traces:
        if trace.split == 'success_val_seen':
            val_masses.append(sum(max(0.0, score - q95) for score in trace.scores))
    mass_t = conformal_upper_threshold(val_masses, 0.15)
    
    print(f'Row threshold (q95): {q95:.4f}')
    print(f'Conformal mass threshold (alpha=0.15): {mass_t:.4f}')
    
    # Seen (ID) test split
    seen_success = [t for t in traces if t.split == 'success_test_seen']
    seen_failure = [t for t in traces if t.split == 'failure_test_seen']
    
    # Unseen (OOD) test split
    ood_success = [t for t in traces if t.split == 'success_test_ood']
    ood_failure = [t for t in traces if t.split == 'failure_eval_ood']
    
    print(f'\nSeen (ID) trace counts - Success: {len(seen_success)}, Failure: {len(seen_failure)}')
    print(f'Unseen (OOD) trace counts - Success: {len(ood_success)}, Failure: {len(ood_failure)}')
    
    seen_metrics = calculate_split_metrics(seen_success, seen_failure, q95, mass_t)
    ood_metrics = calculate_split_metrics(ood_success, ood_failure, q95, mass_t)
    
    results = [
        {'Split': 'Seen (ID)', **seen_metrics},
        {'Split': 'Unseen (OOD)', **ood_metrics}
    ]
    
    df = pd.DataFrame(results)
    print('\n=== VERIFIED BASELINE v2_018_transformer_k16 RESULTS ===')
    print(df.to_string(index=False))

if __name__ == '__main__':
    main()
