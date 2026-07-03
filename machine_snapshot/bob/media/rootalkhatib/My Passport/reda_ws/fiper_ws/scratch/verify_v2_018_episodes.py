import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import numpy as np

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
    
    # Unseen (OOD) test split
    ood_success = [t for t in traces if t.split == 'success_test_ood']
    ood_failure = [t for t in traces if t.split == 'failure_eval_ood']
    
    print('--- DETAILED ROLLOUT SAMPLE FOR v2_018 (OOD Split) ---')
    print('| rollout_id | type | length | step_0_score | threshold | max_score | first_alarm_step | first_alarm_frac |')
    
    for idx, trace in enumerate(ood_success[:10] + ood_failure[:10]):
        type_str = 'success' if trace.split == 'success_test_ood' else 'failure'
        length = len(trace.scores)
        step_0_score = trace.scores[0]
        max_score = np.max(trace.scores)
        
        first_alarm = trigger_mass(trace.scores, q95, mass_t)
        
        if first_alarm is not None:
            denom = min(length, 300)
            first_frac = first_alarm / (denom - 1) if denom > 1 else 0.0
        else:
            first_frac = None
            
        print(f'| {idx:10d} | {type_str:7s} | {length:6d} | {step_0_score:12.4f} | {q95:9.4f} | {max_score:9.4f} | {str(first_alarm):16s} | {str(first_frac):16s} |')

if __name__ == '__main__':
    main()
