import torch
import os

def analyze_entropy_distributions(dataset_path):
    print(f"Loading {dataset_path}...")
    data = torch.load(dataset_path, map_location="cpu")
    episodes = data["episodes"]
    
    feature_names = [
        "weighted_path", "weighted_last", "first_path", "first_last",
        "max_path", "max_last", "gripper_path", "gripper_last"
    ]
    
    success_feats = []
    failure_feats = []
    
    for ep in episodes:
        feats = ep["features"] # [T, 8]
        if ep["success"]: success_feats.append(feats)
        else: failure_feats.append(feats)
            
    check_steps = [10, 50, 100, 200]
    
    print(f"\n{'Step':<5} | {'Feature':<15} | {'Success Mean':<15} | {'Failure Mean':<15} | {'Diff (%)':<10}")
    print("-" * 70)
    
    for t in check_steps:
        for idx in [1, 5]: # weighted_last, max_last
            s_vals = [f[t, idx].item() for f in success_feats if len(f) > t]
            f_vals = [f[t, idx].item() for f in failure_feats if len(f) > t]
            
            if s_vals and f_vals:
                sm = sum(s_vals) / len(s_vals)
                fm = sum(f_vals) / len(f_vals)
                diff = (fm - sm) / (sm + 1e-8) * 100
                print(f"{t:<5} | {feature_names[idx]:<15} | {sm:<15.6f} | {fm:<15.6f} | {diff:>+8.1f}%")
        print("-" * 70)

if __name__ == "__main__":
    path = "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v10_exp01/data/v10_test.pt"
    analyze_entropy_distributions(path)
