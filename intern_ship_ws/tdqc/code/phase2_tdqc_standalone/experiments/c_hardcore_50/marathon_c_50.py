import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os, sys, json, time, argparse

# --- Constants ---
INPUT_DIM = 22
HIDDEN_DIM = 256
MAX_EPOCHS = 500
EARLY_STOPPING_PATIENCE = 100

# --- Models ---
class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__(); self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x): return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * self.weight

class CalibratorMLP(nn.Module):
    def __init__(self, in_d, out_d=1, idea_id='0'):
        super().__init__()
        self.idea_id = idea_id
        h = 128 if idea_id == '35' else 256
        self.mlp = nn.Sequential(
            nn.Linear(in_d, h), RMSNorm(h), nn.SiLU(),
            nn.Linear(h, h), RMSNorm(h), nn.SiLU(),
            nn.Linear(h, h), RMSNorm(h), nn.SiLU(),
            nn.Linear(h, out_d)
        )
        if idea_id == '43': self.recovery_head = nn.Linear(h, 1)

    def forward(self, x):
        # Flatten B, L for the MLP
        B, L, D = x.shape
        x_flat = x.view(B * L, D)
        features = self.mlp[:-1](x_flat)
        out = self.mlp[-1](features).view(B, L, -1)
        if self.idea_id == '43':
            rec = self.recovery_head(features).view(B, L, -1)
            return out, rec
        return out

# --- Feature Engineering ---
def apply_feature_eng(x, idea_id):
    # x: [B, L, D]
    if idea_id == '4': # Derivatives Only
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(v); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        return torch.cat([v, a], dim=-1)
    
    if idea_id == '13': # FFT Spectrum
        x_fft = torch.fft.rfft(x, dim=1).abs()
        return x_fft.mean(dim=1, keepdim=True).repeat(1, x.shape[1], 1)

    if idea_id == '22': # Work/Power (Force * Velocity)
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        power = (x[:, :, 14:22] * v[:, :, 0:8]).sum(dim=-1, keepdim=True)
        return torch.cat([x, power], dim=-1)
        
    if idea_id == '23': # Kinetic Energy (v^2)
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        ke = (v[:, :, 0:8]**2).sum(dim=-1, keepdim=True)
        return torch.cat([x, ke], dim=-1)

    if idea_id == '24': # Velocity Inversion Count (Vibration)
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        inv = (v[:, 1:, :] * v[:, :-1, :] < 0).float().sum(dim=-1, keepdim=True)
        inv_pad = torch.zeros(x.shape[0], 1, 1).to(x.device)
        inv = torch.cat([inv_pad, inv], dim=1)
        return torch.cat([x, inv], dim=-1)

    if idea_id == '29': # Jerk (3rd Derivative)
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(v); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        j = torch.zeros_like(a); j[:, 1:, :] = a[:, 1:, :] - a[:, :-1, :]
        return torch.cat([x, j], dim=-1)

    return x

# --- Dataset ---
class HardcoreDataset(Dataset):
    def __init__(self, episodes, idea_id, mean, std):
        self.episodes = episodes
        self.idea_id = str(idea_id)
        self.mean = mean
        self.std = std
        self.processed = self._process()

    def _process(self):
        out = []
        for ep in self.episodes:
            f = (torch.tensor(ep['features'], dtype=torch.float32) - self.mean) / self.std
            y_base = 1.0 - ep['success']
            
            # Idea 2: Success Padding
            if self.idea_id == '2' and ep['success'] == 1:
                pad = f[-1:].repeat(max(0, 400 - len(f)), 1)
                f = torch.cat([f, pad], dim=0)
            
            # Labeling Rules
            if self.idea_id == '45' and ep['success'] == 0:
                labels = torch.zeros(len(f))
                labels[-50:] = 1.0
                y = labels
            elif self.idea_id == '46': # Velocity-Smoothed
                v = torch.zeros_like(f); v[1:] = f[1:] - f[:-1]
                speed = v[:, 0:8].norm(dim=-1)
                y = torch.ones(len(f)) * y_base
                if ep['success'] == 1: y[speed < 0.01] = 0.2
            else:
                y = torch.ones(len(f)) * y_base
                
            out.append({'x': f, 'y': y})
        return out

    def __len__(self): return len(self.processed)
    def __getitem__(self, i): return self.processed[i]

def collate(batch):
    xs = [b['x'] for b in batch]
    ys = [b['y'] for b in batch]
    L = max(len(x) for x in xs); D = xs[0].shape[-1]
    xb = torch.zeros(len(batch), L, D); yb = torch.zeros(len(batch), L); mb = torch.zeros(len(batch), L)
    for i, (x, y) in enumerate(zip(xs, ys)):
        l = len(x)
        xb[i, :l, :] = x; yb[i, :l] = y; mb[i, :l] = 1.0
    return xb, yb, mb

# --- Training ---
def run_marathon(idea_id):
    device = torch.device('cuda')
    data_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt'
    data = torch.load(data_path, map_location='cpu')
    eps = data['episodes']
    
    all_f = torch.cat([torch.tensor(e['features'], dtype=torch.float32) for e in eps], dim=0)
    mean, std = all_f.mean(0), all_f.std(0) + 1e-6
    
    ds = HardcoreDataset(eps, idea_id, mean, std)
    loader = DataLoader(ds, batch_size=512, shuffle=True, collate_fn=collate, num_workers=4)
    
    test_x = ds[0]['x'].unsqueeze(0).to(device)
    test_x = apply_feature_eng(test_x, idea_id)
    in_dim = test_x.shape[-1]
    
    model = CalibratorMLP(in_dim, idea_id=idea_id).to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    
    best_loss = float('inf'); patience = 0
    print(f'>>> STARTING IDEA {idea_id} | In-Dim: {in_dim}')
    
    for epoch in range(MAX_EPOCHS):
        model.train()
        epoch_loss = 0
        for x, y, m in loader:
            x, y, m = x.to(device), y.to(device), m.to(device)
            x = apply_feature_eng(x, idea_id)
            
            # Idea 1: Chunking
            if idea_id == '1' and x.shape[1] > 20:
                s = np.random.randint(0, x.shape[1]-20)
                x, y, m = x[:, s:s+20], y[:, s:s+20], m[:, s:s+20]
            
            if idea_id == '43':
                logits, recovery = model(x)
                loss = (F.binary_cross_entropy_with_logits(logits.squeeze(-1), y, reduction='none') * m).sum() / m.sum()
                loss += (F.binary_cross_entropy_with_logits(recovery.squeeze(-1), y, reduction='none') * m).sum() / m.sum()
            else:
                logits = model(x).squeeze(-1)
                
                # Idea 47: Focal Loss
                if idea_id == '47':
                    p = torch.sigmoid(logits); pt = torch.where(y == 1, p, 1 - p)
                    loss = (F.binary_cross_entropy_with_logits(logits, y, reduction='none') * (1-pt).pow(2) * m).sum() / m.sum()
                
                # Idea 33: Entropy Regularization
                elif idea_id == '33':
                    loss = (F.binary_cross_entropy_with_logits(logits, y, reduction='none') * m).sum() / m.sum()
                    p = torch.sigmoid(logits)
                    entropy = -(p * torch.log(p + 1e-6) + (1-p) * torch.log(1-p + 1e-6)).mean()
                    loss -= 0.01 * entropy # Penalize low entropy (overconfidence)
                
                # Idea 49: MMD Regularization
                elif idea_id == '49':
                    loss = (F.binary_cross_entropy_with_logits(logits, y, reduction='none') * m).sum() / m.sum()
                    h = model.mlp[:-1](x.view(-1, x.shape[-1]))
                    y_f = y.view(-1); h_s = h[y_f<0.5].mean(0); h_f = h[y_f>0.5].mean(0)
                    if not torch.isnan(h_s).any() and not torch.isnan(h_f).any(): loss += 0.1*(h_s-h_f).pow(2).mean()
                
                else:
                    loss = (F.binary_cross_entropy_with_logits(logits, y, reduction='none') * m).sum() / m.sum()
            
            optimizer.zero_grad(); loss.backward(); optimizer.step(); epoch_loss += loss.item()
            
        avg = epoch_loss / len(loader)
        if epoch % 20 == 0: print(f'Idea {idea_id} | Epoch {epoch} | Loss {avg:.6f}')
        if avg < best_loss:
            best_loss = avg; patience = 0
            torch.save({'model': model.state_dict(), 'mean': mean, 'std': std}, f'runs/best_{idea_id}.pt')
        else:
            patience += 1
            if patience >= EARLY_STOPPING_PATIENCE: break
            
    print(f'FINISHED MARATHON IDEA: {idea_id}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--idea', type=str, required=True)
    args = parser.parse_args()
    run_marathon(args.idea)
