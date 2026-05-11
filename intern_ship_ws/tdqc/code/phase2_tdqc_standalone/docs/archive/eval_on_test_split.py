import torch
from torch.utils.data import DataLoader, random_split
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator
import argparse

def evaluate(model, loader, mean, std, device, use_task_ids=False):
    model.eval()
    total_count = 0.0
    total_brier = 0.0
    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        if use_task_ids:
            task_ids = batch.get("task_ids")
            q = model(x, batch["lengths"], task_ids=task_ids)
        else:
            q = model(x, batch["lengths"])
        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count
    return total_brier / max(total_count, 1.0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--use_task_ids", action="store_true")
    args = parser.parse_args()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataset = TDQCDataset(args.dataset)
    n_total = len(dataset)
    n_train = int(0.7 * n_total)
    n_val = int(0.15 * n_total)
    n_test = n_total - n_train - n_val
    
    _, _, test_set = random_split(
        dataset, [n_train, n_val, n_test],
        generator=torch.Generator().manual_seed(0)
    )
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    ckpt = torch.load(args.ckpt, map_location="cpu")
    cfg = ckpt["config"]
    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"],
        hidden_dim=cfg["hidden_dim"],
        num_layers=cfg["num_layers"],
        dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    
    mean = ckpt["mean"].to(device)
    std = ckpt["std"].to(device)
    
    test_brier = evaluate(model, test_loader, mean, std, device, use_task_ids=args.use_task_ids)
    print(f"Test Sequential Brier: {test_brier:.6f}")
