import json, sys, os
from pathlib import Path
import numpy as np
from collections import defaultdict

def main():
    ds_path = Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen_h10_topk8_v1')
    model_path = Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_h10_topk8_temporal_v1')
    out_dir = Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/online_evals/isaac_ood150_offline_select_single_online_v1/offline')
    out_dir.mkdir(parents=True, exist_ok=True)

    scores = np.load(model_path / 'seen_scores.npz')
    thresholds_file = json.loads((model_path / 'thresholds.json').read_text())
    
    allowed_keys = ["q90_success", "q95_success", "q99_success", "best_val_f1", "fixed_0.5"]
    allowed_thresholds = {k: thresholds_file[k] for k in allowed_keys}
    
    def evaluate_split(split_name, score_key):
        ep_idx = np.load(ds_path / split_name / 'episode_index.npy')
        labels = np.load(ds_path / split_name / 'label.npy')
        split_scores = scores[score_key]
        
        # Group by episode
        by_ep = defaultdict(list)
        for i, ep in enumerate(ep_idx):
            by_ep[ep].append((labels[i], split_scores[i]))
            
        metrics_by_th = {}
        for th_name, th_val in allowed_thresholds.items():
            succ_eps = 0
            fail_eps = 0
            false_alarm = 0
            detected = 0
            det10 = 0
            det25 = 0
            det50 = 0
            det_fracs = []
            
            for ep, rows in by_ep.items():
                y = max(r[0] for r in rows)
                n = len(rows)
                hit_positions = [i for i, r in enumerate(rows) if r[1] >= th_val]
                
                if y >= 0.5:
                    fail_eps += 1
                    if hit_positions:
                        detected += 1
                        first = hit_positions[0]
                        frac = (first + 1) / max(1, n)
                        det_fracs.append(frac)
                        if frac <= 0.10: det10 += 1
                        if frac <= 0.25: det25 += 1
                        if frac <= 0.50: det50 += 1
                else:
                    succ_eps += 1
                    if hit_positions:
                        false_alarm += 1
            
            metrics_by_th[th_name] = {
                "threshold_value": th_val,
                "successful_episodes": succ_eps,
                "failed_episodes": fail_eps,
                "episode_false_alarm_rate": false_alarm / max(1, succ_eps),
                "failure_detection_rate": detected / max(1, fail_eps),
                "det_at_10": det10 / max(1, fail_eps),
                "det_at_25": det25 / max(1, fail_eps),
                "det_at_50": det50 / max(1, fail_eps),
                "never_detected": fail_eps - detected,
                "mean_normalized_detection_time": float(np.mean(det_fracs)) if det_fracs else None
            }
        return metrics_by_th
    
    val_metrics = evaluate_split("validation", "validation_scores")
    test_metrics = evaluate_split("test", "test_scores")
    
    sweep_results = {}
    for th in allowed_keys:
        sweep_results[th] = {
            "validation": val_metrics[th],
            "test": test_metrics[th]
        }
        
    (out_dir / 'SEEN4000_THRESHOLD_SWEEP.json').write_text(json.dumps(sweep_results, indent=2))
    
    # Shortlist logic
    # 1. aggressive: highest test Det@25 among thresholds with test success false-alarm <= 20% and total failure detection >= 95%
    # 2. balanced: highest test Det@25 among thresholds with test success false-alarm <= 10% and total failure detection >= 95%
    # 3. conservative: lowest test success false-alarm among thresholds with total failure detection >= 95%
    
    candidates = []
    for th in allowed_keys:
        m = test_metrics[th]
        candidates.append({
            "name": th,
            "fa": m["episode_false_alarm_rate"],
            "det": m["failure_detection_rate"],
            "det25": m["det_at_25"]
        })
        
    def find_best(fa_limit, require_det=0.95, maximize="det25", minimize=None):
        valid = [c for c in candidates if c["fa"] <= fa_limit and c["det"] >= require_det]
        if not valid:
            valid = [c for c in candidates if c["det"] >= require_det] # fallback
        if not valid:
            valid = candidates
        
        if maximize:
            best = max(valid, key=lambda c: c[maximize])
        else:
            best = min(valid, key=lambda c: c[minimize])
        return best["name"]
        
    agg = find_best(fa_limit=0.20, maximize="det25")
    bal = find_best(fa_limit=0.10, maximize="det25")
    con = find_best(fa_limit=1.00, minimize="fa") # Conservative: lowest FA among those with det >= 95%
    
    shortlist = list(set([agg, bal, con]))
    shortlist_dict = {
        "aggressive": agg,
        "balanced": bal,
        "conservative": con,
        "unique_shortlisted_thresholds": shortlist
    }
    (out_dir / 'SEEN_SHORTLIST.json').write_text(json.dumps(shortlist_dict, indent=2))
    
    # Phase B: OOD150 offline evaluation
    # Read locked OOD150 frozen arrays and scores
    ood_ds_path = Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/locked_h10_ood150_eval')
    ood_eval_path = Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/evaluations/locked_h10_ood150_topk8_v1')
    
    ood_ep_idx = np.load(ood_ds_path / 'episode_index.npy')
    ood_labels = np.load(ood_eval_path / 'scores.npz')['labels']
    ood_scores_arr = np.load(ood_eval_path / 'scores.npz')['scores']
    
    by_ep_ood = defaultdict(list)
    for i, ep in enumerate(ood_ep_idx):
        by_ep_ood[ep].append((ood_labels[i], ood_scores_arr[i]))
        
    ood_metrics_by_th = {}
    for th_name in shortlist:
        th_val = allowed_thresholds[th_name]
        succ_eps = 0
        fail_eps = 0
        false_alarm = 0
        detected = 0
        det10 = 0
        det25 = 0
        det50 = 0
        det_fracs = []
        
        for ep, rows in by_ep_ood.items():
            y = max(r[0] for r in rows)
            n = len(rows)
            hit_positions = [i for i, r in enumerate(rows) if r[1] >= th_val]
            
            if y >= 0.5:
                fail_eps += 1
                if hit_positions:
                    detected += 1
                    first = hit_positions[0]
                    frac = (first + 1) / max(1, n)
                    det_fracs.append(frac)
                    if frac <= 0.10: det10 += 1
                    if frac <= 0.25: det25 += 1
                    if frac <= 0.50: det50 += 1
            else:
                succ_eps += 1
                if hit_positions:
                    false_alarm += 1
        
        ood_metrics_by_th[th_name] = {
            "threshold_value": th_val,
            "successful_episodes": succ_eps,
            "failed_episodes": fail_eps,
            "episode_false_alarm_rate": false_alarm / max(1, succ_eps),
            "failure_detection_rate": detected / max(1, fail_eps),
            "det_at_10": det10 / max(1, fail_eps),
            "det_at_25": det25 / max(1, fail_eps),
            "det_at_50": det50 / max(1, fail_eps),
            "never_detected": fail_eps - detected,
            "mean_normalized_detection_time": float(np.mean(det_fracs)) if det_fracs else None
        }
        
    (out_dir / 'OOD150_SHORTLIST_OFFLINE.json').write_text(json.dumps(ood_metrics_by_th, indent=2))
    
    # deterministic selection rule
    # 1. require total OOD failure detection >= 95%;
    # 2. prefer candidates with OOD success false-alarm <= 10%;
    # 3. within that feasible set maximize Det@25;
    # 4. tie-break by higher Det@10;
    # 5. then lower success false-alarm;
    # 6. then higher total failure detection;
    # 7. final deterministic tie-break: lexical threshold name.
    
    ood_cands = []
    for th in shortlist:
        m = ood_metrics_by_th[th]
        ood_cands.append({
            "name": th,
            "det": m["failure_detection_rate"],
            "fa": m["episode_false_alarm_rate"],
            "det25": m["det_at_25"],
            "det10": m["det_at_10"]
        })
        
    def score_cand(c):
        return (c["det25"], c["det10"], -c["fa"], c["det"], c["name"])
        
    valid = [c for c in ood_cands if c["det"] >= 0.95 and c["fa"] <= 0.10]
    if not valid:
        valid = [c for c in ood_cands if c["det"] >= 0.95 and c["fa"] <= 0.15]
    if not valid:
        valid = ood_cands
        
    best_cand = max(valid, key=score_cand)
    final_selected = best_cand["name"]
    
    selected_controller = {
      "schema_version": "isaac_offline_selected_controller_v1",
      "main_threshold_name": final_selected,
      "selected_cap_name": "q90_success",
      "selection_source": "seen4000 shortlist then locked OOD150 offline balanced ranking",
      "historical_baseline_successes": 72,
      "historical_baseline_failures": 78,
      "seen_test_metrics": test_metrics[final_selected],
      "ood_offline_metrics": ood_metrics_by_th[final_selected],
      "selection_reason": "Deterministic balanced rule"
    }
    
    (out_dir / 'SELECTED_CONTROLLER.json').write_text(json.dumps(selected_controller, indent=2))
    print(f"Sweep complete. Selected: {final_selected}")

if __name__ == '__main__':
    main()
