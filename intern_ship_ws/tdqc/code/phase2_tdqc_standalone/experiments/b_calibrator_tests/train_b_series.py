import os, sys, argparse, json, torch, numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from dataclasses import dataclass
from pathlib import Path

# --- Dataset Logic ---
@dataclass
class TDQCEpisode:
    features: torch.Tensor
    success: int

class BSeriesDataset(Dataset):
    def __init__(self, path, danger_zone=100, is_train=False):
        obj = torch.load(path, map_location='cpu')
        raw = obj['episodes'] if isinstance(obj, dict) else obj
        self.episodes = []
        for ep in raw:
            feat = torch.tensor(ep['features'], dtype=torch.float32)
            # Use all 22 features, but emphasize physics (9-22)
            self.episodes.append(TDQCEpisode(feat, int(ep['success'])))
        self.danger_zone = danger_zone
        self.is_train = is_train

    def __len__(self): return len(self.episodes)
    def __getitem__(self, idx): return self.episodes[idx]

def collate_b(batch, danger_zone=100):
    B = len(batch); T_max = max(ep.features.shape[0] for ep in batch); F = batch[0].features.shape[1]
    features = torch.zeros(B, T_max, F); mask = torch.zeros(B, T_max); labels = torch.zeros(B, T_max)
    lengths = torch.zeros(B, dtype=torch.long)
    
    for b, ep in enumerate(batch):
        T = ep.features.shape[0]; features[b, :T] = ep.features; mask[b, :T] = 1.0; lengths[b] = T
        if ep.success == 0:
            # Danger Zone Ramp: Linear ramp from 0 to 1 in the last danger_zone steps
            start_idx = max(0, T - danger_zone)
            for t in range(start_idx, T):
                labels[b, t] = (t - start_idx + 1) / danger_zone
    return {'features': features, 'mask': mask, 'labels': labels, 'lengths': lengths}

# --- Models ---
class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__(); self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x): return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * self.weight

class CalibratorMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim=256, num_layers=4, mode='classifier'):
        super().__init__()
        self.mode = mode
        in_d = input_dim * 4 + 16 # Ms-Deltas + Softplus
        layers = []
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU()])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, input_dim if mode == 'forward' else 1)

    def forward(self, x):
        x_pad = F.pad(x.transpose(1, 2), (2, 0), mode='replicate')
        x_s = F.avg_pool1d(x_pad, kernel_size=3, stride=1).transpose(1, 2)
        v1 = torch.zeros_like(x_s); v1[:, 1:, :] = x_s[:, 1:, :] - x_s[:, :-1, :]
        v3 = torch.zeros_like(x_s); v3[:, 3:, :] = x_s[:, 3:, :] - x_s[:, :-3, :]
        v5 = torch.zeros_like(x_s); v5[:, 5:, :] = x_s[:, 5:, :] - x_s[:, :-5, :]
        u_v1 = F.softplus(v1[:, :, 14:22]); u_v5 = F.softplus(v5[:, :, 14:22])
        feat = torch.cat([x_s, v1, v3, v5, u_v1, u_v5], dim=-1)
        out = self.head(self.mlp(feat)).squeeze(-1)
        return torch.sigmoid(out) if self.mode == 'classifier' else out

# --- Training ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--idea_id', type=str, required=True)
    parser.add_argument('--mode', type=str, choices=['classifier', 'forward'], default='classifier')
    parser.add_argument('--danger_zone', type=int, default=100)
    args = parser.parse_args()

    device = torch.device('cuda')
    train_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
    val_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_val.pt'
    
    dataset = BSeriesDataset(train_path, danger_zone=args.danger_zone)
    loader = DataLoader(dataset, batch_size=256, shuffle=True, collate_fn=lambda b: collate_b(b, args.danger_zone))
    val_set = BSeriesDataset(val_path, danger_zone=args.danger_zone)
    val_loader = DataLoader(val_set, batch_size=256, shuffle=False, collate_fn=lambda b: collate_b(b, args.danger_zone))

    model = CalibratorMLP(22, mode=args.mode).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    print(f'Starting Idea {args.idea_id} [{args.mode}] with Danger Zone {args.danger_zone}')
    
    # Normalization
    all_f = torch.cat([ep.features for ep in dataset.episodes], dim=0)
    mean, std = all_f.mean(dim=0).to(device), all_f.std(dim=0).clamp_min(1e-6).to(device)

    for epoch in range(100):
        model.train(); total_loss = 0
        for batch in loader:
            x = (batch['features'].to(device) - mean) / std
            out = model(x)
            if args.mode == 'classifier':
                loss = F.binary_cross_entropy(out, batch['labels'].to(device), weight=batch['mask'].to(device))
            else: # Forward Predictor: Predict next state
                target = x[:, 1:, :]; pred = out[:, :-1, :]
                loss = F.mse_loss(pred, target, reduction='none').mean(dim=-1) * batch['mask'][:, :-1].to(device)
                loss = loss.sum() / batch['mask'].sum()
            
            optim.zero_grad(); loss.backward(); optim.step()
            total_loss += loss.item()
        
        print(f'Epoch {epoch:02d} Loss: {total_loss/len(loader):.6f}')
        if epoch % 10 == 0:
            torch.save({'model': model.state_dict(), 'mean': mean.cpu(), 'std': std.cpu(), 'config': {'hidden_dim': 256, 'num_layers': 4, 'mode': args.mode}}, f'runs/best_{args.idea_id}.pt')

if __name__ == '__main__':
    os.makedirs('runs', exist_ok=True)
    main()
