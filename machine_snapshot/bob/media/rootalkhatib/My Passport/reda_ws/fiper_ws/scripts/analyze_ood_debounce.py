import json
from pathlib import Path
import numpy as np
import sys

def load_scores(path, split_name):
    scores = {}
    if not Path(path).exists(): return scores
    with open(path, 'r') as f:
        for line in f:
            data = json.loads(line)
            if data['split'] == split_name:
                ek = data['ek']
                if ek not in scores: scores[ek] = []
                scores[ek].append(data)
    for ek in scores:
        scores[ek].sort(key=lambda x: x['timestep'])
    return scores

def analyze_debounce_all(exp_dir, success_splits, failure_splits, k_vals=[1, 2, 3]):
    exp_dir = Path(exp_dir)
    rnd_thresh = json.load(open(exp_dir / 'thresholds/rnd_thresholds.json'))['q95']
    ace_thresh = json.load(open(exp_dir / 'thresholds/ace_thresholds.json'))['q95']
    
    # Preload all needed scores
    rnd_all = {}
    ace_all = {}
    for split in success_splits + failure_splits:
        rnd_all[split] = load_scores(exp_dir / 'scores/rnd_scores_by_split.jsonl', split)
        ace_all[split] = load_scores(exp_dir / 'scores/ace_scores_by_split.jsonl', split)

    results = []
    for k in k_vals:
        for split in success_splits + failure_splits:
            ep_rnd = rnd_all[split]
            ep_ace = ace_all[split]
            
            n_episodes = len(ep_rnd)
            if n_episodes == 0: continue
            
            ep_detected = 0
            first_times = []
            
            for ek in ep_rnd:
                rnd = ep_rnd[ek]
                ace = ep_ace[ek]
                alarms = [r['rnd_score'] > rnd_thresh or a['ace_entropy'] > ace_thresh for r, a in zip(rnd, ace)]
                
                debounced = []
                count = 0
                for a in alarms:
                    if a: count += 1
                    else: count = 0
                    debounced.append(count >= k)
                
                if any(debounced):
                    ep_detected += 1
                    first_idx = debounced.index(True)
                    first_times.append(first_idx / len(debounced))
                else:
                    first_times.append(1.0)
            
            det_rate = ep_detected / n_episodes
            mean_time = np.mean([t for t in first_times if t < 1.0]) if any(t < 1.0 for t in first_times) else 1.0
            det_25_all = np.mean([t <= 0.25 for t in first_times])

            results.append({
                'k': k,
                'split': split,
                'ep_rate': float(det_rate),
                'mean_time': float(mean_time),
                'det_25': float(det_25_all)
            })
            
    return results

if __name__ == '__main__':
    exp_dir = sys.argv[1]
    success_splits = ['success_test_seen', 'success_test_ood']
    failure_splits = ['failure_eval_seen', 'failure_eval_ood', 'failure_eval_ood_late', 'failure_eval_ood_near_end']
    res = analyze_debounce_all(exp_dir, success_splits, failure_splits)
    print(json.dumps(res, indent=2))
