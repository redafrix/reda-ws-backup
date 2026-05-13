import os, sys, argparse, json, torch, numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from dataclasses import dataclass

@dataclass
class TDQCEpisode:
    features: torch.Tensor
    success: int

class BSeriesDataset(Dataset):
    def __init__(self, path, danger_zone=50):
        obj = torch.load(path, map_location='cpu')
        raw = obj['episodes'] if isinstance(obj, dict) else obj
        self.episodes = [TDQCEpisode(torch.tensor(ep['features'], dtype=torch.float32), int(ep['success'])) for ep in raw]
        self.danger_zone = danger_zone
    def __len__(self): return len(self.episodes)
    def __getitem__(self, idx): return self.episodes[idx]

def collate_b(batch, danger_zone=50):
    B = len(batch); T_max = max(ep.features.shape[0] for ep in batch); F = batch[0].features.shape[1]
    features = torch.zeros(B, T_max, F); mask = torch.zeros(B, T_max); labels = torch.zeros(B, T_max)
    for b, ep in enumerate(batch):
        T = ep.features.shape[0]; features[b, :T] = ep.features; mask[b, :T] = 1.0
        if ep.success == 0:
            start_idx = max(0, T - danger_zone)
            for t in range(start_idx, T):
                labels[b, t] = np.power((t - start_idx + 1) / danger_zone, 2)
    return {'features': features, 'mask': mask, 'labels': labels}

class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__(); self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x): return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * self.weight

class PhysicsHeavyMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim=256, num_layers=4):
        super().__init__()
        in_d = input_dim * 4 + 16
        layers = []
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU()])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers); self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x_phys = x.clone(); x_phys[:, :, 9:] *= 2.0
        x_pad = F.pad(x_phys.transpose(1, 2), (2, 0), mode='replicate')
        x_s = F.avg_pool1d(x_pad, kernel_size=3, stride=1).transpose(1, 2)
        v1 = torch.zeros_like(x_s); v1[:, 1:, :] = x_s[:, 1:, :] - x_s[:, :-1, :]
        v3 = torch.zeros_like(x_s); v3[:, 3:, :] = x_s[:, 3:, :] - x_s[:, :-3, :]
        v5 = torch.zeros_like(x_s); v5[:, 5:, :] = x_s[:, 5:, :] - x_s[:, :-5, :]
        u_v1 = F.softplus(v1[:, :, 14:22]); u_v5 = F.softplus(v5[:, :, 14:22])
        feat = torch.cat([x_s, v1, v3, v5, u_v1, u_v5], dim=-1)
        return torch.sigmoid(self.head(self.mlp(feat)).squeeze(-1))

def main():
    device = torch.device('cuda')
    train_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
    dataset = BSeriesDataset(train_path)
    loader = DataLoader(dataset, batch_size=1024, shuffle=True, collate_fn=collate_b, num_workers=4, pin_memory=True)
    model = PhysicsHeavyMLP(22).to(device); optim = torch.optim.AdamW(model.parameters(), lr=2e-4)
    all_f = torch.cat([ep.features for ep in dataset.episodes], dim=0)
    mean, std = all_f.mean(dim=0).to(device), all_f.std(dim=0).clamp_min(1e-6).to(device)
    for epoch in range(100):
        model.train(); total_loss = 0
        for batch in loader:
            x = (batch['features'].to(device) - mean) / std
            out = model(x)
            bce = F.binary_cross_entropy(out, batch['labels'].to(device), reduction='none')
            pt = torch.exp(-bce); loss = (0.25 * (1-pt)**2 * bce * batch['mask'].to(device)).sum() / batch['mask'].sum()
            optim.zero_grad(); loss.backward(); optim.step(); total_loss += loss.item()
        print(f'Physics-Heavy Epoch {epoch} Loss: {total_loss/len(loader):.6f}')
        if epoch % 20 == 0:
            torch.save({'model': model.state_dict(), 'mean': mean.cpu(), 'std': std.cpu()}, 'runs/best_312.pt')

if __name__ == '__main__':
    os.makedirs('runs', exist_ok=True)
    main()
