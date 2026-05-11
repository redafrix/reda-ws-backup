import torch
import argparse
from pathlib import Path
from torch.utils.data import DataLoader
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

def fixed_horizon_evaluation(ckpt_path, dataset_path, horizon=100, device="cuda"):
    device = torch.device(device if torch.cuda.is_available() else "cpu")
    
    # Load model
    ckpt = torch.load(ckpt_path, map_location="cpu")
    cfg = ckpt["config"]
    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"],
        hidden_dim=cfg["hidden_dim"],
        num_layers=cfg["num_layers"],
        dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)
    
    # Load dataset
    dataset = TDQCDataset(dataset_path)
    n_total = len(dataset)
    n_train = int(0.7 * n_total)
    n_val = int(0.15 * n_total)
    n_test = n_total - n_train - n_val
    
    # Reproduce the exact test split used in training
    _, _, test_set = torch.utils.data.random_split(
        dataset,
        [n_train, n_val, n_test],
        generator=torch.Generator().manual_seed(0), # Same seed as training
    )
    
    loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    total_brier_fixed = 0.0
    total_steps_fixed = 0.0
    
    total_brier_full = 0.0
    total_steps_full = 0.0

    print(f"\n--- Starting Fixed-Horizon Evaluation (Horizon={horizon} steps) ---")
    print(f"Model: {ckpt_path}")
    
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            q = model(x, batch["lengths"]) # [B, T]
            
            failure = batch["failure"][:, None].expand_as(q) # [B, T]
            mask = batch["mask"] # [B, T]
            
            # 1. Standard Brier (Full length)
            sq_err = (q - failure).pow(2) * mask
            total_brier_full += sq_err.sum().item()
            total_steps_full += mask.sum().item()
            
            # 2. Fixed Horizon Brier (Only first 100 steps)
            fixed_mask = mask.clone()
            if q.shape[1] > horizon:
                fixed_mask[:, horizon:] = 0.0
            
            sq_err_fixed = (q - failure).pow(2) * fixed_mask
            total_brier_fixed += sq_err_fixed.sum().item()
            total_steps_fixed += fixed_mask.sum().item()

    full_score = total_brier_full / max(total_steps_full, 1.0)
    fixed_score = total_brier_fixed / max(total_steps_fixed, 1.0)
    
    print(f"Full Sequence Brier:   {full_score:.6f}")
    print(f"Fixed-Horizon Brier:  {fixed_score:.6f}")
    
    if fixed_score < 0.15:
        print("\nCONCLUSION: The model remains strong within the first 100 steps!")
    else:
        print("\nCONCLUSION: Performance dropped in the fixed horizon.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt_path", type=str, required=True)
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument("--horizon", type=int, default=100)
    args = parser.parse_args()
    
    fixed_horizon_evaluation(args.ckpt_path, args.dataset_path, args.horizon)
