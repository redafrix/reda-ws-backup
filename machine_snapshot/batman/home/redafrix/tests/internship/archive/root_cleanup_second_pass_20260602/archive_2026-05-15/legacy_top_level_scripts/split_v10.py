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
    
    # 1. Feature Slicing (Only first 8 features: Entropy/Uncertainty)
    print("Slicing features to first 8 indices (Ensemble Entropy)...")
    for ep in episodes:
        feats = ep["features"]
        if not isinstance(feats, torch.Tensor):
            feats = torch.tensor(feats, dtype=torch.float32)
        ep["features"] = feats[:, :8]
        
    # 2. Extract OOD (IDs 8, 9 from object suites)
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
            
    print(f"Extracted {len(ood_eps)} OOD episodes and {len(in_dist_eps)} In-Distribution episodes.")
    
    # 3. Shuffle and Split In-Distribution (No Balancing)
    random.shuffle(in_dist_eps)
    n = len(in_dist_eps)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    
    train_eps = in_dist_eps[:n_train]
    val_eps = in_dist_eps[n_train:n_train + n_val]
    test_eps = in_dist_eps[n_train + n_val:]
    
    print(f"Split Sizes: Train={len(train_eps)}, Val={len(val_eps)}, Test={len(test_eps)}, OOD={len(ood_eps)}")
    
    # 4. Normalization Stats
    print("Computing normalization stats on training set...")
    all_features = torch.cat([ep["features"] for ep in train_eps], dim=0)
    mean = all_features.mean(dim=0)
    std = all_features.std(dim=0).clamp_min(1e-6)
    
    stats = {"mean": mean, "std": std}
    torch.save(stats, os.path.join(output_dir, "v10_norm_stats.pt"))
    
    # 5. Save Splits
    def save_split(name, eps_list):
        split_data = {
            "episodes": eps_list,
            "feature_keys": data.get("feature_keys", [])[:8],
            "feature_mode": data.get("feature_mode", "summary"),
            "raw_action_dim": data.get("raw_action_dim", 7),
        }
        torch.save(split_data, os.path.join(output_dir, name))
        print(f"Saved {name}")

    save_split("v10_train.pt", train_eps)
    save_split("v10_val.pt", val_eps)
    save_split("v10_test.pt", test_eps)
    save_split("v10_unseen_obj_ood.pt", ood_eps)

if __name__ == "__main__":
    input_file = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp01/data/v9_full_49d.pt"
    output_directory = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v10_exp01/data"
    os.makedirs(output_directory, exist_ok=True)
    split_dataset(input_file, output_directory)