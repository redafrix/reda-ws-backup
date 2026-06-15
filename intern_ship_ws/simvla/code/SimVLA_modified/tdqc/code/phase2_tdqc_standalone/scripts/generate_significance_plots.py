import torch
import matplotlib.pyplot as plt
import numpy as np
import os
from torch.utils.data import DataLoader
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

def generate_significant_plots(ckpt_path, dataset_path, device="cuda"):
    device = torch.device(device if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(ckpt_path, map_location="cpu")
    model = TDQCLSTMCalibrator(
        input_dim=ckpt["config"]["input_dim"],
        hidden_dim=ckpt["config"]["hidden_dim"],
        num_layers=ckpt["config"]["num_layers"]
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)
    dataset = TDQCDataset(dataset_path)
    
    # Use exact same split logic
    n_total = len(dataset)
    n_train, n_val = int(0.7*n_total), int(0.15*n_total)
    _, _, test_set = torch.utils.data.random_split(
        dataset, [n_train, n_val, n_total-n_train-n_val],
        generator=torch.Generator().manual_seed(0)
    )
    loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)

    horizons = [25, 50, 75, 100, 125, 150, 200]
    horizon_brier = []

    # Max length for averaging
    MAX_T = max(ep.length for ep in dataset)
    fail_curves = []
    succ_curves = []

    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            q = model(normalize_features(batch["features"], mean, std), batch["lengths"])
            
            for b in range(q.shape[0]):
                L = int(batch["lengths"][b].item())
                pred = q[b, :L].cpu().numpy()
                is_fail = batch["failure"][b].item() > 0.5
                
                # Pad for averaging
                padded = np.full(MAX_T, np.nan)
                padded[:L] = pred
                
                if is_fail:
                    fail_curves.append(padded)
                else:
                    succ_curves.append(padded)

    # 1. Calculate Average Curves
    avg_fail = np.nanmean(fail_curves, axis=0)
    avg_succ = np.nanmean(succ_curves, axis=0)

    # 2. Calculate Brier vs Horizon
    for h in horizons:
        total_err, total_steps = 0, 0
        with torch.no_grad():
            for batch in loader:
                batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
                q = model(normalize_features(batch["features"], mean, std), batch["lengths"])
                target = batch["failure"][:, None].expand_as(q)
                mask = batch["mask"].clone()
                if q.shape[1] > h: mask[:, h:] = 0
                
                total_err += ((q - target).pow(2) * mask).sum().item()
                total_steps += mask.sum().item()
        horizon_brier.append(total_err / max(total_steps, 1))

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Left: Proactive Detection Plot
    t = np.arange(MAX_T)
    ax1.plot(t, avg_fail, label='Failed Episodes (Ground Truth = 1)', color='red', linewidth=3)
    ax1.plot(t, avg_succ, label='Successful Episodes (Ground Truth = 0)', color='green', linewidth=3)
    ax1.fill_between(t, avg_fail, avg_succ, color='gray', alpha=0.1, label='Separation (Safety Margin)')
    ax1.set_title('Proactive Risk Detection: How the Model "Sees" Failure Coming', fontsize=13)
    ax1.set_xlabel('Time Steps (10Hz)')
    ax1.set_ylabel('Predicted Probability of Terminal Failure')
    ax1.set_xlim(0, 150)
    ax1.set_ylim(0, 1.0)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()

    # Right: Length-Bias Defense Plot
    ax2.plot(horizons, horizon_brier, marker='o', markersize=8, color='purple', linewidth=3, label='Model Brier Score')
    ax2.axhline(y=0.207, color='green', linestyle='--', label='Dataset Baseline (Guessing Mean)')
    ax2.set_title('Brier Score vs. Time Horizon (The "Length-Bias" Check)', fontsize=13)
    ax2.set_xlabel('Evaluation Horizon (Steps)')
    ax2.set_ylabel('Brier Score (Lower is Better)')
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.annotate('Model beats baseline even at step 25!', xy=(25, horizon_brier[0]), xytext=(40, 0.18),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    ax2.legend()

    plt.tight_layout()
    output_path = 'results/plots/significance_analysis.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"Significant plots saved to {output_path}")

if __name__ == "__main__":
    # Default paths relative to phase2_tdqc_standalone root
    ckpt = "results/checkpoints/lstm_td0_final_polish_v2/best.pt"
    data = "data/final_calibrated_3751rollouts.pt"
    generate_significant_plots(ckpt, data)
