import argparse
import torch
import numpy as np
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import roc_auc_score, accuracy_score
from pathlib import Path

# Local imports
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score
from tdqc_model import TDQCMambaCalibrator

def move_batch(batch, device):
    return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}

@torch.no_grad()
def evaluate_full(model, loader, mean, std, device):
    model.eval()
    all_valid_preds = []
    all_valid_labels = []

    for batch in loader:
        batch = move_batch(batch, device)
        x = normalize_features(batch["features"], mean, std)
        q = model(x) # [B, T]
        
        # Expand failure label [B] to [B, T]
        failure_expanded = batch["failure"][:, None].expand_as(q)
        mask = batch["mask"]

        # Extract only valid steps
        valid_q = q[mask == 1].cpu().numpy()
        valid_labels = failure_expanded[mask == 1].cpu().numpy()
        
        all_valid_preds.append(valid_q)
        all_valid_labels.append(valid_labels)

    valid_preds = np.concatenate(all_valid_preds)
    valid_labels = np.concatenate(all_valid_labels)

    brier = np.mean((valid_preds - valid_labels)**2)
    acc = accuracy_score(valid_labels, (valid_preds > 0.5).astype(float))
    try:
        auc = roc_auc_score(valid_labels, valid_preds)
    except:
        auc = 0.5 # Default for single-class or failure

    return {
        "brier": brier,
        "accuracy": acc,
        "auc_roc": auc,
        "n_steps": len(valid_preds)
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(args.ckpt, map_location=device)
    config = ckpt["config"]
    
    model = TDQCMambaCalibrator(
        input_dim=config["input_dim"],
        hidden_dim=config["hidden_dim"],
        num_layers=config["num_layers"],
        d_state=config.get("d_state", 16),
        d_conv=config.get("d_conv", 4),
        expand=config.get("expand", 2),
    ).to(device)
    model.load_state_dict(ckpt["model"])
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)

    # Reconstruct or Load Test Split
    if config.get("test_path"):
        print(f"Loading official test dataset from {config['test_path']}...", flush=True)
        test_set = TDQCDataset(config["test_path"])
    else:
        print(f"Reconstructing test split from {config['dataset_path']}...", flush=True)
        full_dataset = TDQCDataset(config["dataset_path"])
        n_total = len(full_dataset)
        n_train = int(config.get("train_ratio", 0.7) * n_total)
        n_val = int(config.get("val_ratio", 0.15) * n_total)
        n_test = n_total - n_train - n_val
        _, _, test_set = random_split(
            full_dataset, [n_train, n_val, n_test],
            generator=torch.Generator().manual_seed(config.get("seed", 0))
        )
    
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)

    print("\n" + "="*60)
    print(f"REPORT FOR CHECKPOINT: {args.ckpt}")
    print("="*60)

    # Internal Test
    metrics = evaluate_full(model, test_loader, mean, std, device)
    print(f"TEST SET ({config.get('test_path') or 'Split from ' + config['dataset_path']})")
    print(f"  Brier:    {metrics['brier']:.6f}")
    print(f"  Accuracy: {metrics['accuracy']:.6f}")
    print(f"  AUC-ROC:  {metrics['auc_roc']:.6f}")
    print("-" * 30)

    # OOD Tests
    ood_paths = [
        "../../data/v7_22d/v7_22d_ood.pt",
        "../../data/v8_balanced/v8_unseen_obj_ood.pt",
        "../../data/libero_object_object_new/v7_22d_ood.pt",
        "../../data/goal_object_ood/v7_22d_ood.pt"
    ]

    for p in ood_paths:
        if not Path(p).exists(): continue
        ds = TDQCDataset(p)
        loader = DataLoader(ds, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
        m = evaluate_full(model, loader, mean, std, device)
        print(f"OOD: {p}")
        print(f"  Brier:    {m['brier']:.6f}")
        print(f"  Accuracy: {m['accuracy']:.6f}")
        print(f"  AUC-ROC:  {m['auc_roc']:.6f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
