import torch.nn.functional as F
from __future__ import annotations
import argparse, json, random, torch
from pathlib import Path
from torch.utils.data import DataLoader, random_split
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from phase2_tdqc.tdqc_losses import tdqc_brier_td_loss, sequential_brier_score
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator, hard_update

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", type=str, required=True)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--hidden_dim", type=int, default=128)
    p.add_argument("--num_layers", type=int, default=1)
    p.add_argument("--dropout", type=float, default=0.05)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--epochs", type=int, default=1000)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=1e-2)
    p.add_argument("--target_update_freq", type=int, default=100)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument("--patience", type=int, default=20) # Mandated Patience
    return p.parse_args()

@torch.no_grad()
def evaluate(model, loader, mean, std, device):
    model.eval()
    total_count, total_brier = 0.0, 0.0
    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])
        brier = sequential_brier_score(q, batch["failure"], batch["mask"])
        count = batch["mask"].sum().item()
        total_brier += brier.item() * count
        total_count += count
    return {"seq_brier": total_brier / max(total_count, 1.0)}

def main():
    args = parse_args()
    random.seed(args.seed); torch.manual_seed(args.seed)
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    out_dir = Path(args.output_dir); out_dir.mkdir(parents=True, exist_ok=True)
    dataset = TDQCDataset(args.dataset_path, max_horizon=150, is_train=True) # Truncation Mandate
    n_train = int(0.7 * len(dataset)); n_val = int(0.15 * len(dataset))
    train_set, val_set, test_set = random_split(dataset, [n_train, n_val, len(dataset)-n_train-n_val])
    train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, collate_fn=tdqc_collate)
    val_loader = DataLoader(val_set, batch_size=args.batch_size, collate_fn=tdqc_collate)
    
    
    # Properly collect all valid time-steps for normalization
    all_feats = torch.cat([ep.features for ep in train_set], dim=0)
    stats = compute_feature_stats(all_feats)
    
    mean, std = stats["mean"].to(device), stats["std"].to(device)
    
    model = TDQCTransformerCalibrator(input_dim=dataset.input_dim, hidden_dim=args.hidden_dim, num_layers=args.num_layers).to(device)
    target_model = TDQCTransformerCalibrator(input_dim=dataset.input_dim, hidden_dim=args.hidden_dim, num_layers=args.num_layers).to(device)
    target_model2 = TDQCTransformerCalibrator(input_dim=dataset.input_dim, hidden_dim=args.hidden_dim, num_layers=args.num_layers).to(device)
    hard_update(target_model, model); target_model.eval()
    optim = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    
    best_val, epochs_no_improve = float("inf"), 0
    for epoch in range(args.epochs):
        model.train(); running_loss = 0.0
        for batch in train_loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            out = model(x, mask=batch["mask"]); q_online = out[..., 0]; q_ttf = out[..., 1]
            with torch.no_grad(): out1 = target_model(x, mask=batch["mask"]); out2 = target_model2(x, mask=batch["mask"]); q_target = torch.min(out1[..., 0], out2[..., 0])
            # TTF Target: 1.0 at start, 0.0 at failure
            ttf_target = torch.linspace(1.0, 0.0, x.size(1), device=x.device).view(1, -1).expand(x.size(0), -1)
            loss_brier = tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])
            loss_ttf = F.mse_loss(q_ttf * batch["mask"], ttf_target * batch["mask"])
            loss = loss_brier + 0.1 * loss_ttf
            optim.zero_grad(); loss.backward(); optim.step()
            if random.random() < 0.01: hard_update(target_model, model)
            running_loss += loss.item()
        
        val_brier = evaluate(model, val_loader, mean, std, device)["seq_brier"]
        print(f"epoch={epoch:04d} loss={running_loss/len(train_loader):.6f} val_brier={val_brier:.6f}")
        if val_brier < best_val:
            best_val, epochs_no_improve = val_brier, 0
            torch.save({"model": model.state_dict(), "config": vars(args), "mean": mean, "std": std}, out_dir / "best.pt")
        else:
            epochs_no_improve += 1
        if epochs_no_improve >= args.patience: # Early Stopping Mandate
            print(f"Early stopping at epoch {epoch}"); break
