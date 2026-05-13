import os, sys, argparse, json, random
from pathlib import Path
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

# Force local import
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_losses import tdqc_mc_brier_loss, sequential_brier_score

class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super().__init__(); self.weight = nn.Parameter(torch.ones(dim)); self.eps = eps
    def forward(self, x): return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)).type_as(x) * self.weight

class TDQCMlp(nn.Module):
    def __init__(self, input_dim, hidden_dim=256, num_layers=4):
        super().__init__()
        in_d = input_dim * 4 + 16
        layers = []
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU()])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers); self.head = nn.Linear(hidden_dim, 1)
    def forward(self, x):
        # Physics Sentinel: Temporal Smoothing
        x_pad = F.pad(x.transpose(1, 2), (2, 0), mode='replicate')
        x_s = F.avg_pool1d(x_pad, kernel_size=3, stride=1).transpose(1, 2)
        v1 = torch.zeros_like(x_s); v1[:, 1:, :] = x_s[:, 1:, :] - x_s[:, :-1, :]
        v3 = torch.zeros_like(x_s); v3[:, 3:, :] = x_s[:, 3:, :] - x_s[:, :-3, :]
        v5 = torch.zeros_like(x_s); v5[:, 5:, :] = x_s[:, 5:, :] - x_s[:, :-5, :]
        u_v1 = F.softplus(v1[:, :, 14:22]); u_v5 = F.softplus(v5[:, :, 14:22])
        return torch.sigmoid(self.head(self.mlp(torch.cat([x_s, v1, v3, v5, u_v1, u_v5], dim=-1)))).squeeze(-1)

def evaluate(model, loader, mean, std, device):
    model.eval()
    total_count, total_brier = 0.0, 0.0
    with torch.no_grad():
        for batch in loader:
            x = normalize_features(batch['features'].to(device), mean, std)
            q = model(x)
            brier = sequential_brier_score(q, batch['failure'].to(device), batch['mask'].to(device))
            count = batch['mask'].sum().item()
            total_brier += brier.item() * count
            total_count += count
    return total_brier / max(total_count, 1.0)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--train_path', type=str, required=True)
    p.add_argument('--val_path', type=str, required=True)
    p.add_argument('--output_dir', type=str, required=True)
    p.add_argument('--hidden_dim', type=int, default=256)
    p.add_argument('--num_layers', type=int, default=4)
    p.add_argument('--lr', type=float, default=1e-4)
    p.add_argument('--epochs', type=int, default=100)
    args = p.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    os.makedirs(args.output_dir, exist_ok=True)

    train_set = TDQCDataset(args.train_path, is_train=True)
    val_set = TDQCDataset(args.val_path)
    train_loader = DataLoader(train_set, batch_size=512, shuffle=True, collate_fn=tdqc_collate, num_workers=4)
    val_loader = DataLoader(val_set, batch_size=512, shuffle=False, collate_fn=tdqc_collate, num_workers=2)

    model = TDQCMlp(train_set.input_dim, hidden_dim=args.hidden_dim, num_layers=args.num_layers).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=args.lr)
    
    # Pre-computed normalization from Idea 205 (best practice)
    # We'll recompute just to be safe for this new labeling paradigm
    print('Computing stats...')
    all_f = torch.cat([ep.features for ep in train_set.episodes], dim=0)
    mean = all_f.mean(dim=0).to(device)
    std = all_f.std(dim=0).clamp_min(1e-6).to(device)

    best_val = float('inf')
    for epoch in range(args.epochs):
        model.train()
        running_loss = 0.0
        for batch in train_loader:
            x = normalize_features(batch['features'].to(device), mean, std)
            q = model(x)
            loss = tdqc_mc_brier_loss(q, batch['failure'].to(device), batch['mask'].to(device), fail_weight=10.0)
            optim.zero_grad()
            loss.backward()
            optim.step()
            running_loss += loss.item()
        
        val_brier = evaluate(model, val_loader, mean, std, device)
        print(f'epoch={epoch:03d} loss={running_loss/len(train_loader):.6f} val_brier={val_brier:.6f}')
        
        if val_brier < best_val:
            best_val = val_brier
            torch.save({'model': model.state_dict(), 'mean': mean.cpu(), 'std': std.cpu(), 
                        'config': {'hidden_dim': args.hidden_dim, 'num_layers': args.num_layers}}, 
                       os.path.join(args.output_dir, 'best.pt'))

if __name__ == '__main__':
    main()
