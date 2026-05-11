import argparse
import torch
from torch.utils.data import DataLoader
from pathlib import Path

# Local imports
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score
from tdqc_model import TDQCMambaCalibrator

def move_batch(batch, device):
    return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}

@torch.no_grad()
def evaluate(model, loader, mean, std, device):
    model.eval()
    total_count = 0.0
    total_brier = 0.0

    for batch in loader:
        batch = move_batch(batch, device)
        x = normalize_features(batch["features"], mean, std)
        q = model(x)
        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count

    return total_brier / max(total_count, 1.0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--device", type=str, default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"Loading checkpoint from {args.ckpt}...")
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

    ood_datasets = [
        "../../data/v7_22d/v7_22d_ood.pt",
        "../../data/v8_balanced/v8_unseen_obj_ood.pt",
        "../../data/ood/goal_object_ood.pt"
    ]

    print("\n--- OOD Evaluation Results ---")
    for ds_path in ood_datasets:
        if not Path(ds_path).exists():
            print(f"Skipping {ds_path} (not found)")
            continue
            
        dataset = TDQCDataset(ds_path)
        loader = DataLoader(dataset, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
        
        brier = evaluate(model, loader, mean, std, device)
        print(f"Dataset: {ds_path}")
        print(f"  Episodes: {len(dataset)}")
        print(f"  Sequential Brier: {brier:.6f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
