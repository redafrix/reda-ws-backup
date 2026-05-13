import os, sys, argparse, torch, numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from dataclasses import dataclass

@dataclass
class TDQCEpisode:
    features: torch.Tensor
    success: int

class BSeriesDataset(Dataset):
    def __init__(self, path, idea_id):
        obj = torch.load(path, map_location='cpu')
        raw = obj['episodes'] if isinstance(obj, dict) else obj
        if idea_id == '301':
            self.episodes = [TDQCEpisode(torch.tensor(ep['features'], dtype=torch.float32), 1) for ep in raw if ep['success'] == 1]
        else:
            self.episodes = [TDQCEpisode(torch.tensor(ep['features'], dtype=torch.float32), int(ep['success'])) for ep in raw]
    def __len__(self): return len(self.episodes)
    def __getitem__(self, idx): return self.episodes[idx]

def collate_b(batch, idea_id):
    B = len(batch); T_max = max(ep.features.shape[0] for ep in batch); F = batch[0].features.shape[1]
    features = torch.zeros(B, T_max, F); mask = torch.zeros(B, T_max); labels = torch.zeros(B, T_max)
    for b, ep in enumerate(batch):
        T = ep.features.shape[0]; features[b, :T] = ep.features; mask[b, :T] = 1.0
        if ep.success == 0:
            dz = 100 if idea_id in ['302', '304', '307', '310'] else (50 if idea_id in ['303', '306', '311'] else 10)
            start_idx = max(0, T - dz)
            for t in range(start_idx, T):
                prog = (t - start_idx + 1) / dz
                labels[b, t] = np.power(prog, 2) if idea_id in ['304', '307', '310', '311'] else prog
    return {'features': features, 'mask': mask, 'labels': labels}

class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__(); self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x): return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * self.weight

class CalibratorMLP(nn.Module):
    def __init__(self, input_dim, idea_id):
        super().__init__(); self.idea_id = idea_id; in_d = input_dim * 4 + 16
        self.mlp = nn.Sequential(nn.Linear(in_d, 256), RMSNorm(256), nn.SiLU(), nn.Linear(256, 256), RMSNorm(256), nn.SiLU(), nn.Linear(256, 256), RMSNorm(256), nn.SiLU())
        self.head = nn.Linear(256, input_dim if idea_id == '305' else 1)
    def forward(self, x):
        if self.idea_id in ['306', '307', '310', '311']: x = x.clone(); x[:, :, 9:] *= 2.0
        x_pad = F.pad(x.transpose(1, 2), (2, 0), mode='replicate')
        x_s = F.avg_pool1d(x_pad, kernel_size=3, stride=1).transpose(1, 2)
        v1 = torch.zeros_like(x_s); v1[:, 1:, :] = x_s[:, 1:, :] - x_s[:, :-1, :]
        v3 = torch.zeros_like(x_s); v3[:, 3:, :] = x_s[:, 3:, :] - x_s[:, :-3, :]
        v5 = torch.zeros_like(x_s); v5[:, 5:, :] = x_s[:, 5:, :] - x_s[:, :-5, :]
        u_v1 = torch.log1p(v1[:, :, 14:22].abs()); u_v5 = torch.log1p(v5[:, :, 14:22].abs())
        feat = torch.cat([x_s, v1, v3, v5, u_v1, u_v5], dim=-1)
        out = self.head(self.mlp(feat)).squeeze(-1)
        return torch.sigmoid(out) if self.idea_id != '305' else out

class VAE(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(input_dim, 64), nn.ReLU(), nn.Linear(64, 16))
        self.decoder = nn.Sequential(nn.Linear(8, 64), nn.ReLU(), nn.Linear(64, input_dim))
    def forward(self, x):
        h = self.encoder(x); mu, logvar = h.chunk(2, dim=-1)
        z = mu + torch.randn_like(mu) * torch.exp(0.5 * logvar)
        return self.decoder(z), mu, logvar

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--idea_id', type=str, required=True); args = parser.parse_args()
    device = torch.device('cuda'); train_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
    dataset = BSeriesDataset(train_path, args.idea_id)
    loader = DataLoader(dataset, batch_size=1024, shuffle=True, collate_fn=lambda b: collate_b(b, args.idea_id), num_workers=4, pin_memory=True)
    model = VAE(22).to(device) if args.idea_id == '301' else CalibratorMLP(22, args.idea_id).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=2e-4)
    all_f = torch.cat([ep.features for ep in dataset.episodes], dim=0); mean, std = all_f.mean(dim=0).to(device), all_f.std(dim=0).clamp_min(1e-6).to(device)
    for epoch in range(100):
        total_loss = 0
        for batch in loader:
            x = (batch['features'].to(device) - mean) / std
            if args.idea_id == '301':
                recon, mu, logvar = model(x)
                loss = (F.mse_loss(recon, x, reduction='none').mean(dim=-1) + 0.01 * (-0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1))).sum() / batch['mask'].sum()
            elif args.idea_id == '305':
                target = x[:, 1:, :]; pred = model(x)[:, :-1, :]
                loss = (F.mse_loss(pred, target, reduction='none').mean(dim=-1) * batch['mask'][:, :-1].to(device)).sum() / batch['mask'].sum()
            else:
                out = model(x)
                if args.idea_id in ['306', '307', '310', '311']:
                    bce = F.binary_cross_entropy(out, batch['labels'].to(device), reduction='none')
                    pt = torch.exp(-bce); loss = (0.25 * (1-pt)**2 * bce * batch['mask'].to(device)).sum() / batch['mask'].sum()
                else:
                    loss = F.binary_cross_entropy(out, batch['labels'].to(device), weight=batch['mask'].to(device))
            optim.zero_grad(); loss.backward(); optim.step(); total_loss += loss.item()
        print(f'Idea {args.idea_id} | Epoch {epoch:02d} | Loss: {total_loss/len(loader):.6f}')
    torch.save({'model': model.state_dict(), 'mean': mean.cpu(), 'std': std.cpu()}, f'runs/best_{args.idea_id}.pt')
if __name__ == '__main__':
    os.makedirs('runs', exist_ok=True); main()
