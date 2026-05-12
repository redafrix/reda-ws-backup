import torch
import random
import os
import sys

def split_dataset(input_path, output_dir, train_ratio=0.8, val_ratio=0.1):
    print(f"Loading dataset from {input_path}...")
    data = torch.load(input_path, map_location="cpu")
    
    episodes = data["episodes"] if isinstance(data, dict) and "episodes" in data else data
    if isinstance(data, list):
        data = {"episodes": data}
        
    random.seed(0)
    
    # 1. Extract OOD
    # OOD: Task IDs 8 and 9 from the libero_object suites
    ood_suites = {'libero_object_lan', 'libero_object_object', 'libero_object_swap'}
    ood_eps = []
    in_dist_eps = []
    
    for ep in episodes:
        suite = ep.get("task_suite", "")
        tid = ep.get("task_id", -1)
        if suite in ood_suites and tid in {8, 9}:
            ood_eps.append(ep)
        else:
            in_dist_eps.append(ep)
            
    print(f"Extracted {len(ood_eps)} OOD episodes before balancing.")
    
    # Balance OOD
    ood_succ = []
    ood_fail = []
    for ep in ood_eps:
        if int(ep.get("success", 0)) == 1:
            ood_succ.append(ep)
        else:
            ood_fail.append(ep)
            
    ood_min = min(len(ood_succ), len(ood_fail))
    print(f"OOD counts before balancing: {len(ood_succ)} successes, {len(ood_fail)} failures")
    print(f"Balancing OOD to {ood_min} each...")
    random.shuffle(ood_succ)
    random.shuffle(ood_fail)
    balanced_ood_eps = ood_succ[:ood_min] + ood_fail[:ood_min]
    random.shuffle(balanced_ood_eps)
    print(f"Final OOD episodes: {len(balanced_ood_eps)}")
    
    # 2. Balance In-Distribution
    success_eps = []
    failure_eps = []
    for ep in in_dist_eps:
        if int(ep.get("success", 0)) == 1:
            success_eps.append(ep)
        else:
            failure_eps.append(ep)
            
    min_count = min(len(success_eps), len(failure_eps))
    print(f"In-Distribution counts before balancing: {len(success_eps)} successes, {len(failure_eps)} failures")
    print(f"Balancing ID to {min_count} each...")
    
    random.shuffle(success_eps)
    random.shuffle(failure_eps)
    balanced_eps = success_eps[:min_count] + failure_eps[:min_count]
    random.shuffle(balanced_eps)
    
    # 3. Split
    n = len(balanced_eps)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    
    train_eps = balanced_eps[:n_train]
    val_eps = balanced_eps[n_train:n_train + n_val]
    test_eps = balanced_eps[n_train + n_val:]
    
    print(f"Split In-Distribution: Train={len(train_eps)}, Val={len(val_eps)}, Test={len(test_eps)}")
    
    # Compute normalization stats on train set
    print("Computing normalization stats on training set...")
    all_features = []
    for ep in train_eps:
        feats = ep["features"]
        if not isinstance(feats, torch.Tensor):
            feats = torch.tensor(feats, dtype=torch.float32)
        all_features.append(feats)
    
    all_features = torch.cat(all_features, dim=0)
    mean = all_features.mean(dim=0)
    std = all_features.std(dim=0).clamp_min(1e-6)
    
    stats = {"mean": mean, "std": std}
    torch.save(stats, os.path.join(output_dir, "v9_norm_stats.pt"))
    print(f"Saved norm stats to {os.path.join(output_dir, 'v9_norm_stats.pt')}")
    
    # Save splits
    def save_split(name, eps_list):
        split_data = {
            "episodes": eps_list,
            "feature_keys": data.get("feature_keys", []),
            "feature_mode": data.get("feature_mode", "summary"),
            "raw_action_dim": data.get("raw_action_dim", 7),
        }
        torch.save(split_data, os.path.join(output_dir, name))
        print(f"Saved {name} with {len(eps_list)} episodes")

    save_split("v9_train.pt", train_eps)
    save_split("v9_val.pt", val_eps)
    save_split("v9_test.pt", test_eps)
    save_split("v9_unseen_obj_ood.pt", balanced_ood_eps)

if __name__ == "__main__":
    input_file = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp01/data/v9_full_49d.pt"
    output_directory = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp01/data"
    split_dataset(input_file, output_directory)