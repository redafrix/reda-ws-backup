import json
import numpy as np
from pathlib import Path
from collections import defaultdict

def run_analysis():
    rnd_path = Path("/home/redafrix/tests/internship/fiper_ws/scratch/scores/rnd_scores_by_split.jsonl")
    ace_path = Path("/home/redafrix/tests/internship/fiper_ws/scratch/scores/ace_scores_by_split.jsonl")
    
    print("Loading RND scores...")
    rnd_data = []
    with rnd_path.open() as f:
        for line in f:
            if line.strip():
                rnd_data.append(json.loads(line))
                
    print("Loading ACE scores...")
    ace_data = []
    with ace_path.open() as f:
        for line in f:
            if line.strip():
                ace_data.append(json.loads(line))
                
    print(f"Loaded {len(rnd_data)} RND rows and {len(ace_data)} ACE rows.")
    assert len(rnd_data) == len(ace_data), "Row count mismatch!"
    
    # Organize by split -> episode_key -> list of timesteps
    # We will build a merged dictionary:
    # merged[split][ek][timestep] = (rnd_score, ace_entropy)
    merged = defaultdict(lambda: defaultdict(dict))
    
    for r_row, a_row in zip(rnd_data, ace_data):
        assert r_row["split"] == a_row["split"], f"Split mismatch! {r_row['split']} vs {a_row['split']}"
        assert r_row["ek"] == a_row["ek"], f"Episode key mismatch! {r_row['ek']} vs {a_row['ek']}"
        assert r_row["timestep"] == a_row["timestep"], f"Timestep mismatch! {r_row['timestep']} vs {a_row['timestep']}"
        
        split = r_row["split"]
        ek = r_row["ek"]
        t = r_row["timestep"]
        merged[split][ek][t] = (r_row["rnd_score"], a_row["ace_entropy"])
        
    print("Finished merging scores.")
    
    # Success calibration thresholds
    rnd_q90 = 0.028685735538601875
    rnd_q95 = 0.03691943734884262
    rnd_q99 = 0.05899343639612198
    
    ace_q90 = -342.28604759682406
    ace_q95 = -341.2813874319598
    ace_q99 = -338.71100278593815
    
    # We need to evaluate:
    # 1. RND-only (q90, q95, q99) with K=1,2,3,5
    # 2. ACE-only (q90, q95, q99) with K=1,2,3,5
    # 3. OR (q90, q95, q99) with K=1,2,3,5
    # 4. AND (q90, q95, q99) with K=1,2,3,5
    # 5. Tiered rule: YELLOW = OR q95 K=3, RED = AND q95 K=2 or OR q99 K=2
    # 6. Weighted score rule: 
    #    risk = max(rnd_score/rnd_q95, ace_entropy/ace_q95_direction_corrected)
    #    let's try:
    #    - risk_v1: ace_q95 / ace_entropy
    #    - risk_v2: 2 - (ace_entropy / ace_q95)
    
    # Let's write a function to calculate metrics for a given rule
    # A rule is a function: condition(rnd, ace) -> bool
    
    splits_to_evaluate = [
        "success_test_seen",
        "success_test_ood",
        "failure_eval_seen",
        "failure_eval_ood"
    ]
    
    def evaluate_rule(name, condition_fn, K_vals=[1, 2, 3, 5]):
        results = {}
        for K in K_vals:
            results[K] = {}
            for split in splits_to_evaluate:
                episodes = merged[split]
                ep_alarms = []
                ep_first_indices = []
                ep_norm_times = []
                ep_alarm_counts = []
                
                for ek, steps_dict in episodes.items():
                    # Sort steps by timestep
                    steps = [steps_dict[t] for t in sorted(steps_dict.keys())]
                    n_steps = len(steps)
                    
                    # Compute step-level raw alarms
                    raw_alarms = [condition_fn(rnd, ace) for rnd, ace in steps]
                    
                    # Compute debounced alarm at each timestep
                    debounced_alarms = []
                    consec = 0
                    first_idx = -1
                    for idx, raw in enumerate(raw_alarms):
                        if raw:
                            consec += 1
                        else:
                            consec = 0
                        
                        is_alarm = consec >= K
                        debounced_alarms.append(is_alarm)
                        if is_alarm and first_idx == -1:
                            first_idx = idx
                            
                    alarmed = first_idx != -1
                    ep_alarms.append(alarmed)
                    ep_first_indices.append(first_idx)
                    ep_norm_times.append(first_idx / n_steps if alarmed else 1.0)
                    ep_alarm_counts.append(sum(debounced_alarms))
                    
                # Calculate metrics
                n_ep = len(episodes)
                fa_or_det_pct = sum(ep_alarms) / n_ep * 100.0 if n_ep > 0 else 0.0
                
                # For failure splits:
                times_detected = [t for t, alarmed in zip(ep_norm_times, ep_alarms) if alarmed]
                mean_time = np.mean(times_detected) if times_detected else 1.0
                
                det_10 = sum(1 for t, alarmed in zip(ep_norm_times, ep_alarms) if alarmed and t <= 0.1) / n_ep * 100.0 if n_ep > 0 else 0.0
                det_25 = sum(1 for t, alarmed in zip(ep_norm_times, ep_alarms) if alarmed and t <= 0.25) / n_ep * 100.0 if n_ep > 0 else 0.0
                never_pct = sum(1 for alarmed in ep_alarms if not alarmed) / n_ep * 100.0 if n_ep > 0 else 0.0
                
                mean_alarms = np.mean(ep_alarm_counts) if ep_alarm_counts else 0.0
                median_alarms = np.median(ep_alarm_counts) if ep_alarm_counts else 0.0
                
                results[K][split] = {
                    "fa_or_det_pct": fa_or_det_pct,
                    "mean_time": mean_time,
                    "det_10": det_10,
                    "det_25": det_25,
                    "never_pct": never_pct,
                    "mean_alarms": mean_alarms,
                    "median_alarms": median_alarms,
                }
        return results

    # Run RND-only
    print("Running RND sweeps...")
    rnd_rules = {
        "RND_q90": lambda rnd, ace: rnd > rnd_q90,
        "RND_q95": lambda rnd, ace: rnd > rnd_q95,
        "RND_q99": lambda rnd, ace: rnd > rnd_q99,
    }
    
    # Run ACE-only
    print("Running ACE sweeps...")
    ace_rules = {
        "ACE_q90": lambda rnd, ace: ace > ace_q90,
        "ACE_q95": lambda rnd, ace: ace > ace_q95,
        "ACE_q99": lambda rnd, ace: ace > ace_q99,
    }
    
    # Run OR
    print("Running OR sweeps...")
    or_rules = {
        "OR_q90": lambda rnd, ace: (rnd > rnd_q90) or (ace > ace_q90),
        "OR_q95": lambda rnd, ace: (rnd > rnd_q95) or (ace > ace_q95),
        "OR_q99": lambda rnd, ace: (rnd > rnd_q99) or (ace > ace_q99),
    }
    
    # Run AND
    print("Running AND sweeps...")
    and_rules = {
        "AND_q90": lambda rnd, ace: (rnd > rnd_q90) and (ace > ace_q90),
        "AND_q95": lambda rnd, ace: (rnd > rnd_q95) and (ace > ace_q95),
        "AND_q99": lambda rnd, ace: (rnd > rnd_q99) and (ace > ace_q99),
    }
    
    all_results = {}
    for name, fn in {**rnd_rules, **ace_rules, **or_rules, **and_rules}.items():
        all_results[name] = evaluate_rule(name, fn)
        
    # Tiered rule
    print("Running Tiered rule...")
    # RED = AND q95 K=2 or OR q99 K=2
    # Since RED combines conditions with K=2, we need to evaluate the RED rule directly.
    # Specifically, at each timestep, RED is triggered if (AND q95 has been active for >=2 steps) or (OR q99 has been active for >=2 steps).
    # Let's write the logic for RED:
    # For each episode, we compute consecutive counts for (AND q95) and (OR q99).
    # RED is active at t if consec(AND q95) >= 2 or consec(OR q99) >= 2.
    # Note that this is already a debounced rule, so we treat it as K=1 for the RED condition itself.
    # Wait, does the tiered rule require K=1,2,3,5? The tiered rule itself is defined with specific K values inside it:
    # "YELLOW = OR q95 K=3" and "RED = AND q95 K=2 or OR q99 K=2".
    # So the tiered rule's red alarm triggers when the RED condition is met (which is K=1 on the RED condition).
    # Let's evaluate RED directly!
    
    tiered_results = {}
    for split in splits_to_evaluate:
        episodes = merged[split]
        ep_alarms_red = []
        ep_first_indices_red = []
        ep_norm_times_red = []
        ep_alarm_counts_red = []
        
        ep_alarms_yellow = []
        ep_first_indices_yellow = []
        ep_norm_times_yellow = []
        ep_alarm_counts_yellow = []
        
        for ek, steps_dict in episodes.items():
            steps = [steps_dict[t] for t in sorted(steps_dict.keys())]
            n_steps = len(steps)
            
            # Step conditions
            and_q95_raw = [(rnd > rnd_q95) and (ace > ace_q95) for rnd, ace in steps]
            or_q99_raw = [(rnd > rnd_q99) or (ace > ace_q99) for rnd, ace in steps]
            or_q95_raw = [(rnd > rnd_q95) or (ace > ace_q95) for rnd, ace in steps]
            
            # Debounce
            consec_and_q95 = 0
            consec_or_q99 = 0
            consec_or_q95 = 0
            
            red_active = []
            yellow_active = []
            
            first_idx_red = -1
            first_idx_yellow = -1
            
            for idx in range(n_steps):
                if and_q95_raw[idx]: consec_and_q95 += 1
                else: consec_and_q95 = 0
                
                if or_q99_raw[idx]: consec_or_q99 += 1
                else: consec_or_q99 = 0
                
                if or_q95_raw[idx]: consec_or_q95 += 1
                else: consec_or_q95 = 0
                
                is_red = (consec_and_q95 >= 2) or (consec_or_q99 >= 2)
                is_yellow = (consec_or_q95 >= 3)
                
                red_active.append(is_red)
                yellow_active.append(is_yellow)
                
                if is_red and first_idx_red == -1:
                    first_idx_red = idx
                if is_yellow and first_idx_yellow == -1:
                    first_idx_yellow = idx
                    
            ep_alarms_red.append(first_idx_red != -1)
            ep_first_indices_red.append(first_idx_red)
            ep_norm_times_red.append(first_idx_red / n_steps if first_idx_red != -1 else 1.0)
            ep_alarm_counts_red.append(sum(red_active))
            
            ep_alarms_yellow.append(first_idx_yellow != -1)
            ep_first_indices_yellow.append(first_idx_yellow)
            ep_norm_times_yellow.append(first_idx_yellow / n_steps if first_idx_yellow != -1 else 1.0)
            ep_alarm_counts_yellow.append(sum(yellow_active))
            
        n_ep = len(episodes)
        
        # Red metrics
        fa_or_det_pct = sum(ep_alarms_red) / n_ep * 100.0 if n_ep > 0 else 0.0
        times_detected = [t for t, alarmed in zip(ep_norm_times_red, ep_alarms_red) if alarmed]
        mean_time = np.mean(times_detected) if times_detected else 1.0
        det_10 = sum(1 for t, alarmed in zip(ep_norm_times_red, ep_alarms_red) if alarmed and t <= 0.1) / n_ep * 100.0 if n_ep > 0 else 0.0
        det_25 = sum(1 for t, alarmed in zip(ep_norm_times_red, ep_alarms_red) if alarmed and t <= 0.25) / n_ep * 100.0 if n_ep > 0 else 0.0
        never_pct = sum(1 for alarmed in ep_alarms_red if not alarmed) / n_ep * 100.0 if n_ep > 0 else 0.0
        mean_alarms = np.mean(ep_alarm_counts_red) if ep_alarm_counts_red else 0.0
        median_alarms = np.median(ep_alarm_counts_red) if ep_alarm_counts_red else 0.0
        
        tiered_results[split] = {
            "fa_or_det_pct": fa_or_det_pct,
            "mean_time": mean_time,
            "det_10": det_10,
            "det_25": det_25,
            "never_pct": never_pct,
            "mean_alarms": mean_alarms,
            "median_alarms": median_alarms,
        }
    all_results["Tiered_RED"] = {1: tiered_results} # tiered is evaluated as a single debounced system

    # Run Weighted Risk Rule
    print("Running Weighted Risk sweeps...")
    # risk = max(rnd_score/rnd_q95, ace_entropy/ace_q95_direction_corrected)
    # We will test two risk versions:
    # risk_v1 = max(rnd/rnd_q95, ace_q95/ace)
    # risk_v2 = max(rnd/rnd_q95, 2 - ace/ace_q95)
    
    # We sweep risk thresholds: e.g. 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.5, 2.0 with K=1, 2, 3, 5
    risk_thresholds = [0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.3, 1.5]
    
    for r_thresh in risk_thresholds:
        # V1
        name_v1 = f"RiskV1_t{r_thresh}"
        fn_v1 = lambda rnd, ace: max(rnd / rnd_q95, ace_q95 / ace) > r_thresh
        all_results[name_v1] = evaluate_rule(name_v1, fn_v1)
        
        # V2
        name_v2 = f"RiskV2_t{r_thresh}"
        fn_v2 = lambda rnd, ace: max(rnd / rnd_q95, 2.0 - ace / ace_q95) > r_thresh
        all_results[name_v2] = evaluate_rule(name_v2, fn_v2)

    # Let's save the results to a json file for easy plotting/reporting
    with Path("/home/redafrix/tests/internship/fiper_ws/scratch/sweep_results.json").open("w") as f:
        json.dump(all_results, f, indent=2)
        
    print("Sweep analysis complete. Saved to scratch/sweep_results.json")

if __name__ == "__main__":
    run_analysis()
