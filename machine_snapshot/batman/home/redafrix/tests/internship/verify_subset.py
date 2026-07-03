import json
import os
import numpy as np

SUBSET_DIR = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/seen_goal_object_fiper_subset"
EPISODES_JSON = os.path.join(SUBSET_DIR, "selected_episodes.json")
ROWS_JSONL = os.path.join(SUBSET_DIR, "selected_rows.jsonl")

def verify():
    print("Starting verification of subset metadata files...")
    
    if not os.path.exists(EPISODES_JSON):
        print(f"ERROR: {EPISODES_JSON} does not exist.")
        return False
    if not os.path.exists(ROWS_JSONL):
        print(f"ERROR: {ROWS_JSONL} does not exist.")
        return False
        
    # 1. Verify selected_episodes.json
    with open(EPISODES_JSON, 'r') as f:
        episodes_data = json.load(f)
        
    print(f"Total selected episodes: {len(episodes_data)}")
    
    # Check splits
    splits = {}
    for ep, data in episodes_data.items():
        sp = data['split']
        outcome = data['outcome']
        if sp not in splits:
            splits[sp] = []
        splits[sp].append((ep, outcome))
        
    print("Splits found:")
    for sp, eps in splits.items():
        print(f"  {sp}: {len(eps)} episodes")
        
    # Check constraints
    # - No failures in train/calib
    for sp in ['train_success', 'calib_success']:
        if sp in splits:
            failures = [ep for ep, outcome in splits[sp] if outcome != 'success']
            if failures:
                print(f"ERROR: Found failures in {sp}: {failures}")
                return False
            else:
                print(f"  {sp} contains only successes: verified.")
                
    # - No overlap between splits
    all_episodes_sets = [set(list(zip(*eps))[0]) for eps in splits.values() if eps]
    overlap = set()
    keys = list(splits.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            set_i = set(list(zip(*splits[keys[i]]))[0])
            set_j = set(list(zip(*splits[keys[j]]))[0])
            intersection = set_i & set_j
            if intersection:
                print(f"ERROR: Overlap between {keys[i]} and {keys[j]}: {intersection}")
                return False
    print("  No overlap between splits: verified.")
    
    # 2. Verify selected_rows.jsonl
    print("Scanning selected_rows.jsonl...")
    row_count = 0
    unique_episodes_in_rows = set()
    
    missing_sim_state_path = 0
    missing_sam_original = 0
    wrong_main_shape = 0
    wrong_ace_shape = 0
    nan_inf_found = 0
    local_path_check_failures = 0
    
    with open(ROWS_JSONL, 'r') as f:
        for idx, line in enumerate(f):
            row_count += 1
            row = json.loads(line)
            
            ep_id = row['episode_id']
            unique_episodes_in_rows.add(ep_id)
            
            # Check fields
            curr = row.get('current', {})
            sim_state_path = curr.get('sim_state_path')
            sim_state_path_sam_original = curr.get('sim_state_path_sam_original')
            
            if not sim_state_path:
                missing_sim_state_path += 1
            elif not sim_state_path.startswith("/media/rootalkhatib/My Passport"):
                local_path_check_failures += 1
                
            if not sim_state_path_sam_original:
                missing_sam_original += 1
                
            # Check shapes
            main_chunk = row.get('main_candidate_action_chunk_env')
            ace_chunks = row.get('ace_candidate_chunks_env')
            
            main_arr = np.array(main_chunk)
            ace_arr = np.array(ace_chunks)
            
            if main_arr.shape != (10, 7):
                wrong_main_shape += 1
            if ace_arr.shape != (8, 10, 7):
                wrong_ace_shape += 1
                
            # NaN/Inf check on all rows
            if not np.isfinite(main_arr).all() or not np.isfinite(ace_arr).all():
                nan_inf_found += 1
                
    print(f"Verification of rows completed. Results:")
    print(f"  Total rows: {row_count}")
    print(f"  Unique episodes in rows: {len(unique_episodes_in_rows)}")
    print(f"  Missing sim_state_path: {missing_sim_state_path}")
    print(f"  Local path check failures: {local_path_check_failures}")
    print(f"  Missing sam original path: {missing_sam_original}")
    print(f"  Wrong main shape: {wrong_main_shape}")
    print(f"  Wrong ACE shape: {wrong_ace_shape}")
    print(f"  NaN/Inf rows: {nan_inf_found}")
    
    # Check that all episodes in rows are in selected_episodes.json and vice versa
    episodes_in_json = set(episodes_data.keys())
    if unique_episodes_in_rows != episodes_in_json:
        diff_1 = unique_episodes_in_rows - episodes_in_json
        diff_2 = episodes_in_json - unique_episodes_in_rows
        if diff_1:
            print(f"ERROR: Episodes in rows but not in json: {diff_1}")
        if diff_2:
            print(f"ERROR: Episodes in json but not in rows: {diff_2}")
        return False
    else:
        print("  Episode matching between JSON and JSONL: verified.")
        
    if missing_sim_state_path or local_path_check_failures or missing_sam_original or wrong_main_shape or wrong_ace_shape or nan_inf_found:
        print("ERROR: One or more row validation checks failed!")
        return False
        
    print("\nSUCCESS: All metadata and row structure verifications passed successfully!")
    return True

if __name__ == '__main__':
    verify()
