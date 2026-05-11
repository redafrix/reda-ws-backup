import argparse
import torch
import numpy as np
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score, accuracy_score
from pathlib import Path
from collections import defaultdict

# Local imports
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from tdqc_model import TDQCMambaCalibrator

def move_batch(batch, device):
    return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}

@torch.no_grad()
def evaluate_per_task(model, loader, mean, std, device):
    model.eval()
    task_preds = defaultdict(list)
    task_labels = defaultdict(list)

    # Need to keep track of absolute index to access original episodes for suite/instruction
    abs_idx = 0
    dataset = loader.dataset

    for batch in loader:
        batch = move_batch(batch, device)
        x = normalize_features(batch["features"], mean, std)
        q = model(x) # [B, T]
        
        failure_expanded = batch["failure"][:, None].expand_as(q)
        mask = batch["mask"]

        for i in range(len(batch["task_id"])):
            # Access the original episode data which is NOT in the batch
            # Note: This assumes loader is NOT shuffled!
            ep = dataset[abs_idx]
            
            # Since TDQCEpisode doesn't have task_suite, we'll use instruction or raw dict if we had it
            # Wait, TDQCDataset converts to TDQCEpisode objects. 
            # Let's check what's in ep.
            
            t_id = ep.task_id
            instr = ep.instruction[:30] # First 30 chars
            key = f"ID{t_id}_{instr}"
            
            m = mask[i] == 1
            if m.any():
                task_preds[key].append(q[i][m].cpu().numpy())
                task_labels[key].append(failure_expanded[i][m].cpu().numpy())
            
            abs_idx += 1

    results = {}
    for key in sorted(task_preds.keys()):
        preds = np.concatenate(task_preds[key])
        labels = np.concatenate(task_labels[key])
        
        brier = np.mean((preds - labels)**2)
        acc = accuracy_score(labels, (preds > 0.5).astype(float))
        try:
            auc = roc_auc_score(labels, preds)
        except:
            auc = 0.5
            
        results[key] = {
            "brier": brier,
            "accuracy": acc,
            "auc_roc": auc,
            "n_steps": len(preds)
        }
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(args.ckpt, map_location=device)
    config = ckpt["config"]
    
    model = TDQCMambaCalibrator(
        input_dim=config["input_dim"],
        hidden_dim=config["hidden_dim"],
        num_layers=config["num_layers"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)

    ds = TDQCDataset(args.dataset)
    loader = DataLoader(ds, batch_size=32, shuffle=False, collate_fn=tdqc_collate)

    print(f"\nTask-wise Report for {args.dataset}")
    print("="*80)
    task_metrics = evaluate_per_task(model, loader, mean, std, device)
    
    print(f"{'Task Key':<40} | {'Brier':<10} | {'Acc':<8} | {'AUC':<8}")
    print("-" * 80)
    for key, m in task_metrics.items():
        print(f"{key:<40} | {m['brier']:.4f}     | {m['accuracy']:.2%} | {m['auc_roc']:.4f}")

if __name__ == "__main__":
    main()
