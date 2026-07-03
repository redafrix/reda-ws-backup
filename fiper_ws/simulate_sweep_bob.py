import json
import numpy as np

step_scores_path = '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7/03_topk8_balanced/risk_unc_topk8/step_scores_risk_unc_topk8.jsonl'

# Load steps grouped by episode
episodes = {}
with open(step_scores_path) as f:
    for line in f:
        if not line.strip(): continue
        d = json.loads(line)
        ep_idx = d['episode_index']
        if ep_idx not in episodes:
            episodes[ep_idx] = []
        episodes[ep_idx].append(d)

print(f"Loaded {len(episodes)} episodes.")

# We will simulate the selection logic for each hyperparameter set
def simulate(min_margin, min_streak, require_candidate_below_q95, max_first_action_l2, max_mods):
    total_mods = 0
    episodes_modified = 0
    q95 = 0.8500646352767944
    q99 = 0.9937206506729126
    
    for ep_idx, steps in episodes.items():
        mods_count = 0
        streak = 0
        for step in steps:
            main_score = step['main_score']
            candidate_scores = np.array(step['candidate_scores'])
            action_l2 = np.array(step['candidate_first_action_l2'])
            
            # streak logic
            if main_score >= q95:
                streak += 1
            else:
                streak = 0
                
            if mods_count >= max_mods:
                continue
                
            if streak < min_streak:
                continue
                
            # selection logic
            eligible = np.arange(1, len(candidate_scores))
            eligible = eligible[action_l2[eligible] <= max_first_action_l2]
            
            if len(eligible) == 0:
                continue
                
            best_idx = eligible[np.argmin(candidate_scores[eligible])]
            best_score = candidate_scores[best_idx]
            
            if main_score <= best_score:
                continue
                
            diff = main_score - best_score
            
            if main_score < q95:
                continue
                
            if diff < min_margin:
                continue
                
            if require_candidate_below_q95 and best_score >= q95:
                continue
                
            # Trigger intervention!
            mods_count += 1
            
        total_mods += mods_count
        if mods_count > 0:
            episodes_modified += 1
            
    return total_mods, episodes_modified

# Run sweep
print(f"{'Streak':<8}{'Margin':<8}{'ReqQ95':<8}{'L2':<8}{'MaxMods':<8}{'TotalMods':<10}{'EpModded':<10}")
print('-'*60)
for streak in [1, 2, 3]:
    for margin in [0.01, 0.05, 0.08, 0.10, 0.15, 0.20]:
        for req_q95 in [True, False]:
            for l2 in [0.35, 0.50]:
                for max_mods in [1, 2, 5]:
                    t_mods, ep_mod = simulate(margin, streak, req_q95, l2, max_mods)
                    if t_mods > 0:
                        print(f"{streak:<8}{margin:<8}{str(req_q95):<8}{l2:<8}{max_mods:<8}{t_mods:<10}{ep_mod:<10}")
