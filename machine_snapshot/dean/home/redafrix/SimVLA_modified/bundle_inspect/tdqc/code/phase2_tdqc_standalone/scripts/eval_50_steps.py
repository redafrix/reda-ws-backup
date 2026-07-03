import torch
import argparse
from torch.utils.data import DataLoader
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator
import numpy as np

def eval_early_horizon(ckpt_path, dataset_path, horizon=50):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Load model and normalization stats
    ckpt = torch.load(ckpt_path, map_location="cpu")
    model = TDQCLSTMCalibrator(
        input_dim=ckpt["config"]["input_dim"],
        hidden_dim=ckpt["config"]["hidden_dim"],
        num_layers=ckpt["config"]["num_layers"]
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)
    
    # Reproduce the exact Test Split (15%)
    dataset = TDQCDataset(dataset_path)
    n_total = len(dataset)
    n_train, n_val = int(0.7 * n_total), int(0.15 * n_total)
    _, _, test_set = torch.utils.data.random_split(
        dataset, [n_train, n_val, n_total - n_train - n_val],
        generator=torch.Generator().manual_seed(0)
    )
    loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    total_brier = 0.0
    total_steps = 0.0
    trajectory_accuracies = []
    
    print(f"\n--- Evaluation at Horizon: {horizon} steps (5.0s) ---")
    print(f"Model: {ckpt_path}")
    
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            q = model(normalize_features(batch["features"], mean, std), batch["lengths"])
            
            # Ground truth for these episodes
            is_failure = batch["failure"] # [B]
            mask = batch["mask"] # [B, T]
            
            # Apply horizon cutoff
            if q.shape[1] > horizon:
                mask[:, horizon:] = 0.0
            
            # Calculate Brier
            target = is_failure[:, None].expand_as(q)
            sq_err = (q - target).pow(2) * mask
            total_brier += sq_err.sum().item()
            total_steps += mask.sum().item()
            
            # Calculate % of Correct Predictions per trajectory
            preds_binary = (q >= 0.5).float()
            correct_mask = (preds_binary == target).float() * mask
            
            for b in range(q.shape[0]):
                steps_in_horizon = mask[b].sum().item()
                if steps_in_horizon > 0:
                    correct_in_horizon = correct_mask[b].sum().item()
                    trajectory_accuracies.append(correct_in_horizon / steps_in_horizon)

    final_brier = total_brier / max(total_steps, 1.0)
    final_acc = np.mean(trajectory_accuracies) * 100
    
    print(f"Brier Score (0-50 steps):    {final_brier:.6f}")
    print(f"Mean Accuracy per Trajectory: {final_acc:.2f}%")
    print(f"---------------------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt_path", type=str, required=True)
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument("--horizon", type=int, default=50)
    args = parser.parse_args()
    
    eval_early_horizon(args.ckpt_path, args.dataset_path, args.horizon)
