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
    ood_suites = {'libero_object_lan', 'libero_object_object', 'libero_object_swap'}
    ood_eps_by_suite = {}
    in_dist_eps_by_suite = {}
    
    for ep in episodes:
        suite = ep.get("task_suite", "")
        tid = ep.get("task_id", -1)
        
        if suite in ood_suites and tid in {8, 9}:
            if suite not in ood_eps_by_suite:
                ood_eps_by_suite[suite] = []
            ood_eps_by_suite[suite].append(ep)
        else:
            if suite not in in_dist_eps_by_suite:
                in_dist_eps_by_suite[suite] = []
            in_dist_eps_by_suite[suite].append(ep)
            
    # Per-Suite Balancing Function
    def balance_per_suite(eps_dict, label):
        balanced_list = []
        for suite, eps in eps_dict.items():
            succs = [e for e in eps if int(e.get("success", 0)) == 1]
            fails = [e for e in eps if int(e.get("success", 0)) == 0]
            m = min(len(succs), len(fails))
            
            print(f"  {label} [{suite}]: {len(succs)} succ, {len(fails)} fail -> taking {m} of each")
            
            random.shuffle(succs)
            random.shuffle(fails)
            balanced_list.extend(succs[:m])
            balanced_list.extend(fails[:m])
            
        random.shuffle(balanced_list)
        return balanced_list

    print("\nBalancing OOD strictly per-suite...")
    balanced_ood_eps = balance_per_suite(ood_eps_by_suite, "OOD")
    print(f"Final OOD episodes after per-suite balance: {len(balanced_ood_eps)}")
    
    print("\nBalancing In-Distribution strictly per-suite...")
    balanced_id_eps = balance_per_suite(in_dist_eps_by_suite, "ID")
    print(f"Final In-Distribution episodes after per-suite balance: {len(balanced_id_eps)}")
    
    # 3. Split ID
    n = len(balanced_id_eps)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    
    train_eps = balanced_id_eps[:n_train]
    val_eps = balanced_id_eps[n_train:n_train + n_val]
    test_eps = balanced_id_eps[n_train + n_val:]
    
    print(f"\nSplit In-Distribution: Train={len(train_eps)}, Val={len(val_eps)}, Test={len(test_eps)}")
    
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