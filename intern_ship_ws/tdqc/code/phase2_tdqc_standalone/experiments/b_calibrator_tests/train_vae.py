import os, argparse, torch, torch.nn as nn, torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from dataclasses import dataclass

# Only train on SUCCESS episodes for true anomaly detection
@dataclass
class TDQCEpisode:
    features: torch.Tensor
    success: int

class SuccessDataset(Dataset):
    def __init__(self, path):
        obj = torch.load(path, map_location='cpu')
        raw = obj['episodes'] if isinstance(obj, dict) else obj
        self.episodes = [TDQCEpisode(torch.tensor(ep['features'], dtype=torch.float32), 1) for ep in raw if ep['success'] == 1]
    def __len__(self): return len(self.episodes)
    def __getitem__(self, idx): return self.episodes[idx]

def collate(batch):
    B = len(batch); T_max = max(ep.features.shape[0] for ep in batch); F = batch[0].features.shape[1]
    features = torch.zeros(B, T_max, F); mask = torch.zeros(B, T_max)
    for b, ep in enumerate(batch):
        T = ep.features.shape[0]; features[b, :T] = ep.features; mask[b, :T] = 1.0
    return {'features': features, 'mask': mask}

class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim=8):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(input_dim, 64), nn.ReLU(), nn.Linear(64, latent_dim * 2))
        self.decoder = nn.Sequential(nn.Linear(latent_dim, 64), nn.ReLU(), nn.Linear(64, input_dim))
    
    def forward(self, x):
        h = self.encoder(x); mu, logvar = h.chunk(2, dim=-1)
        z = mu + torch.randn_like(mu) * torch.exp(0.5 * logvar)
        return self.decoder(z), mu, logvar

def main():
    device = torch.device('cuda')
    dataset = SuccessDataset('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt')
    loader = DataLoader(dataset, batch_size=256, shuffle=True, collate_fn=collate)
    model = VAE(22).to(device); optim = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    all_f = torch.cat([ep.features for ep in dataset.episodes], dim=0)
    mean, std = all_f.mean(dim=0).to(device), all_f.std(dim=0).clamp_min(1e-6).to(device)

    for epoch in range(100):
        total_loss = 0
        for batch in loader:
            x = (batch['features'].to(device) - mean) / std
            recon, mu, logvar = model(x)
            recon_loss = F.mse_loss(recon, x, reduction='none').mean(dim=-1) * batch['mask'].to(device)
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1) * batch['mask'].to(device)
            loss = (recon_loss + 0.01 * kl_loss).sum() / batch['mask'].sum()
            optim.zero_grad(); loss.backward(); optim.step(); total_loss += loss.item()
        print(f'VAE Epoch {epoch} Loss: {total_loss/len(loader):.6f}')
        if epoch % 20 == 0:
            torch.save({'model': model.state_dict(), 'mean': mean.cpu(), 'std': std.cpu()}, 'runs/best_301.pt')

if __name__ == '__main__':
    main()
