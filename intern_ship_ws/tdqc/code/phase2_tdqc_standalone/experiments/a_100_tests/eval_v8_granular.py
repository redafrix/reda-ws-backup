import os
import sys
import json
import argparse
import torch
import numpy as np
from pathlib import Path

# Add current directory to path to find local phase2_tdqc package
sys.path.append(os.getcwd())

from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score, accuracy_score, brier_score_loss

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator

def compute_metrics(y_true, y_prob):
    if len(y_true) == 0:
        return {"Acc": 0.0, "Brier": 0.0, "AUC": 0.0, "N": 0}
    
    y_true_np = np.array(y_true)
    y_prob_np = np.array(y_prob)
    y_pred_np = (y_prob_np > 0.5).astype(float)
    
    acc = accuracy_score(y_true_np, y_pred_np)
    brier = brier_score_loss(y_true_np, y_prob_np)
    
    try:
        if len(np.unique(y_true_np)) > 1:
            auc = roc_auc_score(y_true_np, y_prob_np)
        else:
            auc = 0.5
    except:
        auc = 0.5
        
    return {
        "Acc": float(acc),
        "Brier": float(brier),
        "AUC": float(auc),
        "N": int(len(y_true))
    }

@torch.no_grad()
def run_granular_eval(model, loader, mean, std, device):
    model.eval()
    
    # Target steps for evaluation
    target_steps = [10, 12, 15, 50, 100, 150, 200, 300]
    
    # Store predictions and labels for each step and overall
    # We use "Horizon Max-Pooling" for step-based evaluation:
    # the score for step T is the max probability observed from 0 to T.
    results_by_step = {step: {"true": [], "prob": []} for step in target_steps}
    results_overall = {"true": [], "prob": []}
    
    for batch in loader:
        features = batch["features"].to(device)
        mask = batch["mask"].to(device)
        labels = batch["failure"].to(device)
        lengths = batch["lengths"].to(device)
        
        x = normalize_features(features, mean, std)
        probs = model(x, mask=mask)
        if len(probs.shape) == 3:
            probs = probs[..., 0] # [B, T]
        
        B, T = probs.shape
        for b in range(B):
            L = int(lengths[b].item())
            true_label = labels[b].item()
            
            # Overall: max prob across all valid steps
            max_prob_overall = probs[b, :L].max().item()
            results_overall["true"].append(true_label)
            results_overall["prob"].append(max_prob_overall)
            
            # Per-step proactivity
            for step in target_steps:
                if L > step:
                    # Model gets credit for any early warning up to 'step'
                    max_prob_step = probs[b, :step].max().item()
                    results_by_step[step]["true"].append(true_label)
                    results_by_step[step]["prob"].append(max_prob_step)

    # Compute final metrics
    final_metrics = {}
    for step in target_steps:
        final_metrics[str(step)] = compute_metrics(
            results_by_step[step]["true"], 
            results_by_step[step]["prob"]
        )
    
    final_metrics["Overall"] = compute_metrics(
        results_overall["true"], 
        results_overall["prob"]
    )
    
    return final_metrics

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--test_dataset", type=str, required=True)
    parser.add_argument("--ood_dataset", type=str, required=True)
    parser.add_argument("--output_file", type=str, default="granular_results.json")
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()
    
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    
    print(f"Loading checkpoint from {args.checkpoint}...")
    ckpt = torch.load(args.checkpoint, map_location=device)
    config = ckpt["config"]
    
    model = TDQCTransformerCalibrator(
        input_dim=config["input_dim"],
        hidden_dim=config["hidden_dim"],
        num_layers=config["num_layers"],
        dropout=config["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)
    
    # Load Datasets
    print(f"Loading Test dataset: {args.test_dataset}")
    test_ds = TDQCDataset(args.test_dataset)
    test_loader = DataLoader(test_ds, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    print(f"Loading OOD dataset: {args.ood_dataset}")
    ood_ds = TDQCDataset(args.ood_dataset)
    ood_loader = DataLoader(ood_ds, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    print("Running evaluation on Test set...")
    test_results = run_granular_eval(model, test_loader, mean, std, device)
    
    print("Running evaluation on OOD set...")
    ood_results = run_granular_eval(model, ood_loader, mean, std, device)
    
    final_output = {
        "test": test_results,
        "ood": ood_results
    }
    
    with open(args.output_file, "w") as f:
        json.dump(final_output, f, indent=2)
    
    print(f"Results saved to {args.output_file}")
    
    # Print a nice table for summary
    print("\n" + "="*50)
    print(f"{'Step':<10} | {'Test Brier':<12} | {'OOD Brier':<12} | {'Test AUC':<10}")
    print("-" * 50)
    for step in ["10", "12", "15", "50", "100", "150", "200", "300", "Overall"]:
        if step in test_results and step in ood_results:
            tb = test_results[step]["Brier"]
            ob = ood_results[step]["Brier"]
            ta = test_results[step]["AUC"]
            print(f"{step:<10} | {tb:<12.4f} | {ob:<12.4f} | {ta:<10.4f}")
        else:
            print(f"{step:<10} | {'N/A':<12} | {'N/A':<12} | {'N/A':<10}")
    print("="*50)

if __name__ == "__main__":
    main()
