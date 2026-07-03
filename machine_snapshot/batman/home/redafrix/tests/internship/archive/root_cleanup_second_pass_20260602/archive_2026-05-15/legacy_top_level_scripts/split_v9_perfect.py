import torch
import random
import os

def split_dataset(input_path, output_dir, train_ratio=0.8, val_ratio=0.1):
    print(f"Loading dataset from {input_path}...")
    data = torch.load(input_path, map_location="cpu")
    
    episodes = data["episodes"] if isinstance(data, dict) and "episodes" in data else data
    if isinstance(data, list):
        data = {"episodes": data}
        
    random.seed(0)
    
    # 1. Grouping
    id_pools = {} # suite -> {1: [], 0: []}
    ood_pools = {} # suite -> {1: [], 0: []}
    
    ood_suites = {'libero_object_lan', 'libero_object_object', 'libero_object_swap'}
    
    for ep in episodes:
        suite = ep.get("task_suite", "")
        tid = ep.get("task_id", -1)
        succ = int(ep.get("success", 0))
        
        if suite in ood_suites and tid in {8, 9}:
            if suite not in ood_pools: ood_pools[suite] = {1: [], 0: []}
            ood_pools[suite][succ].append(ep)
        else:
            if suite not in id_pools: id_pools[suite] = {1: [], 0: []}
            id_pools[suite][succ].append(ep)
            
    # 2. Process ID Suites
    train_eps, val_eps, test_eps = [], [], []
    
    print("\nProcessing In-Distribution Suites:")
    for suite in sorted(id_pools.keys()):
        succs = id_pools[suite][1]
        fails = id_pools[suite][0]
        m = min(len(succs), len(fails))
        
        # Threshold: Need at least 10 pairs to give 1 pair to Val and 1 to Test (10% each)
        if m < 10:
            print(f"  [DROPPED] {suite:<25} | Balanced pairs: {m} (Not enough for split)")
            continue
            
        random.shuffle(succs)
        random.shuffle(fails)
        
        m_val = int(m * val_ratio)
        m_test = int(m * val_ratio)
        m_train = m - m_val - m_test
        
        # Split successes
        s_train = succs[:m_train]
        s_val   = succs[m_train : m_train + m_val]
        s_test  = succs[m_train + m_val : m]
        
        # Split failures
        f_train = fails[:m_train]
        f_val   = fails[m_train : m_train + m_val]
        f_test  = fails[m_train + m_val : m]
        
        train_eps.extend(s_train + f_train)
        val_eps.extend(s_val + f_val)
        test_eps.extend(s_test + f_test)
        
        print(f"  [KEPT]    {suite:<25} | Pairs: {m} (Train: {m_train}, Val: {m_val}, Test: {m_test})")

    # 3. Process OOD Suites
    print("\nProcessing OOD Suites:")
    ood_eps = []
    for suite in sorted(ood_pools.keys()):
        succs = ood_pools[suite][1]
        fails = ood_pools[suite][0]
        m = min(len(succs), len(fails))
        
        if m == 0:
            print(f"  [DROPPED] {suite:<25} | Balanced pairs: 0")
            continue
            
        random.shuffle(succs)
        random.shuffle(fails)
        
        ood_eps.extend(succs[:m] + fails[:m])
        print(f"  [KEPT]    {suite:<25} | Pairs: {m}")

    random.shuffle(train_eps)
    random.shuffle(val_eps)
    random.shuffle(test_eps)
    random.shuffle(ood_eps)
    
    print(f"\nFinal Dataset Sizes:")
    print(f"  Train: {len(train_eps)} eps ({len(train_eps)//2}S / {len(train_eps)//2}F)")
    print(f"  Val:   {len(val_eps)} eps ({len(val_eps)//2}S / {len(val_eps)//2}F)")
    print(f"  Test:  {len(test_eps)} eps ({len(test_eps)//2}S / {len(test_eps)//2}F)")
    print(f"  OOD:   {len(ood_eps)} eps ({len(ood_eps)//2}S / {len(ood_eps)//2}F)")
    
    # 4. Save
    def save_split(name, eps_list, compute_stats=False):
        split_data = {
            "episodes": eps_list,
            "feature_keys": data.get("feature_keys", []),
            "feature_mode": data.get("feature_mode", "summary"),
            "raw_action_dim": data.get("raw_action_dim", 7),
        }
        torch.save(split_data, os.path.join(output_dir, name))
        print(f"Saved {name}")
        
        if compute_stats:
            print("Computing normalization stats...")
            all_f = torch.cat([e["features"] if torch.is_tensor(e["features"]) else torch.tensor(e["features"]) for e in eps_list], dim=0)
            stats = {"mean": all_f.mean(dim=0), "std": all_f.std(dim=0).clamp_min(1e-6)}
            torch.save(stats, os.path.join(output_dir, "v9_norm_stats.pt"))
            print("Saved v9_norm_stats.pt")

    save_split("v9_train.pt", train_eps, compute_stats=True)
    save_split("v9_val.pt", val_eps)
    save_split("v9_test.pt", test_eps)
    save_split("v9_unseen_obj_ood.pt", ood_eps)

if __name__ == "__main__":
    input_file = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp01/data/v9_full_49d.pt"
    output_directory = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp04/data"
    os.makedirs(output_directory, exist_ok=True)
    split_dataset(input_file, output_directory)