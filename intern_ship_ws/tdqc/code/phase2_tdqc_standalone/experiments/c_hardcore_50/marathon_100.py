import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os, sys, json, time, argparse
from torch.nn.utils import spectral_norm

# --- Constants ---
INPUT_DIM = 22
MAX_EPOCHS = 500
EARLY_STOPPING_PATIENCE = 100

# --- Advanced Architectures ---

class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__(); self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x): return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * self.weight

class HardcoreCalibrator(nn.Module):
    def __init__(self, in_d, out_d=1, idea_id='0'):
        super().__init__()
        self.idea_id = str(idea_id)
        h = 128 if self.idea_id in ['35', '60'] else 256
        
        def get_layer(i, o):
            layer = nn.Linear(i, o)
            # Idea 57/77: Spectral Normalization for OOD safety
            if self.idea_id in ['57', '77', '27']: return spectral_norm(layer)
            return layer

        self.layers = nn.ModuleList([
            get_layer(in_d, h),
            get_layer(h, h),
            get_layer(h, h)
        ])
        self.norms = nn.ModuleList([RMSNorm(h) for _ in range(3)])
        self.head = get_layer(h, out_d)
        
        # Idea 43: Recovery Head
        if self.idea_id == '43': self.recovery_head = nn.Linear(h, 1)
        # Idea 11/61: Evidential/Evidence Head
        if self.idea_id in ['11', '61']: self.evidence_head = nn.Sequential(nn.Linear(h, 2), nn.Softplus())

    def forward(self, x):
        B, L, D = x.shape
        # Idea 58: MC-Dropout (Force dropout even in eval)
        do_dropout = self.idea_id in ['8', '58']
        
        h = x.reshape(B * L, D)
        for i in range(len(self.layers)):
            h = self.layers[i](h)
            h = self.norms[i](h)
            h = F.silu(h)
            if do_dropout: h = F.dropout(h, p=0.2, training=True)
            
            # Idea 15/65: Liquid Neural Network Decay Proxy
            if self.idea_id in ['15', '65']:
                tau = torch.sigmoid(h[:, :1]) # Learned time constant
                h = h * torch.exp(-tau)
        
        out = self.head(h).reshape(B, L, -1)
        
        if self.idea_id == '43':
            rec = self.recovery_head(h).reshape(B, L, -1)
            return out, rec
        if self.idea_id in ['11', '61']:
            ev = self.evidence_head(h).reshape(B, L, 2)
            return out, ev
        return out

# --- Feature Engineering Kernels ---
def apply_feature_eng(x, idea_id):
    idea_id = str(idea_id)
    B, L, D = x.shape
    
    # Idea 4/54: Derivatives
    if idea_id in ['4', '54']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(v); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        if idea_id == '4': return torch.cat([v, a], dim=-1)
        return torch.cat([x, v, a], dim=-1)

    # Idea 22/72: Power (Force * Velocity)
    if idea_id in ['22', '72']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        power = (x[:, :, 14:22] * v[:, :, 0:8]).sum(dim=-1, keepdim=True)
        return torch.cat([x, power], dim=-1)

    # Idea 29/79: Jerk (3rd Derivative)
    if idea_id in ['29', '79']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(v); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        j = torch.zeros_like(a); j[:, 1:, :] = a[:, 1:, :] - a[:, :-1, :]
        return torch.cat([x, j], dim=-1)

    # Idea 87: Delta Encoding (+1, 0, -1)
    if idea_id == '87':
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        return torch.sign(v)

    # Idea 13/86: Wavelet/FFT Proxy (Temporal Smoothness)
    if idea_id in ['13', '86']:
        # Use a strided diff to simulate frequency analysis
        v1 = x[:, 1:, :] - x[:, :-1, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        return torch.cat([x, v1.mean(1, keepdim=True).repeat(1, L, 1), v3.mean(1, keepdim=True).repeat(1, L, 1)], dim=-1)

    return x

# --- Dataset Logic ---
class HardcoreDataset(Dataset):
    def __init__(self, episodes, idea_id, mean, std):
        self.episodes = episodes; self.idea_id = str(idea_id); self.mean = mean; self.std = std
        self.processed = self._process()

    def _process(self):
        out = []
        for ep in self.episodes:
            f = (torch.tensor(ep['features'], dtype=torch.float32) - self.mean) / self.std
            y_base = 1.0 - ep['success']
            
            # Idea 53: Dynamic Time Warping (Warped Augmentation)
            if self.idea_id == '53' and np.random.rand() > 0.5:
                # Randomly skip 20% of frames to simulate speed change
                idx = np.sort(np.random.choice(len(f), int(len(f)*0.8), replace=False))
                f = f[idx]
            
            # Idea 2/52: Success Padding (400 Steps)
            if self.idea_id in ['2', '52'] and ep['success'] == 1:
                pad = f[-1:].repeat(max(0, 400 - len(f)), 1)
                f = torch.cat([f, pad], dim=0)

            # Idea 56: Fractional Progression (t/L)
            if self.idea_id == '56' and ep['success'] == 0:
                y = torch.linspace(0, 1, len(f))
            # Idea 52: RUL (Remaining Useful Life)
            elif self.idea_id == '52' and ep['success'] == 0:
                y = torch.linspace(100, 0, len(f)) / 100.0 # Normalized RUL
            # Idea 45/96: Dynamic Competence (Last 50 steps)
            elif self.idea_id in ['45', '96'] and ep['success'] == 0:
                y = torch.zeros(len(f)); y[-50:] = 1.0
            else:
                y = torch.ones(len(f)) * y_base
                
            out.append({'x': f, 'y': y})
        return out

    def __len__(self): return len(self.processed)
    def __getitem__(self, i): return self.processed[i]

def collate(batch):
    xs = [b['x'] for b in batch]; ys = [b['y'] for b in batch]
    L = max(len(x) for x in xs); D = xs[0].shape[-1]
    xb = torch.zeros(len(batch), L, D); yb = torch.zeros(len(batch), L); mb = torch.zeros(len(batch), L)
    for i, (x, y) in enumerate(zip(xs, ys)):
        l = len(x); xb[i, :l, :] = x; yb[i, :l] = y; mb[i, :l] = 1.0
    return xb, yb, mb

# --- Training Kernel ---
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
    
    model = HardcoreCalibrator(in_dim, idea_id=idea_id).to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    best_loss = float('inf'); patience = 0
    
    print(f'>>> HARCORE 100 | STARTING IDEA {idea_id} | In-Dim: {in_dim}')
    
    for epoch in range(MAX_EPOCHS):
        model.train(); epoch_loss = 0
        for x, y, m in loader:
            x, y, m = x.to(device), y.to(device), m.to(device)
            x = apply_feature_eng(x, idea_id)
            
            # Idea 1/5: Chunking & TD-10
            if idea_id in ['1', '5'] and x.shape[1] > 10:
                win = 20 if idea_id == '1' else 10
                s = np.random.randint(0, x.shape[1]-win)
                x, y, m = x[:, s:s+win], y[:, s:s+win], m[:, s:s+win]
            
            # Forward Pass
            res = model(x)
            
            # Loss Logic
            if idea_id == '43':
                logits, rec = res
                loss = (F.binary_cross_entropy_with_logits(logits.squeeze(-1), y, reduction='none') * m).sum() / m.sum()
                loss += (F.binary_cross_entropy_with_logits(rec.squeeze(-1), y, reduction='none') * m).sum() / m.sum()
            elif idea_id in ['11', '61']:
                logits, ev = res
                # Evidential Loss: Evidence should be high for correct class
                success_ev = ev[:, :, 0]; fail_ev = ev[:, :, 1]
                loss = (torch.abs(y - (fail_ev / (success_ev + fail_ev + 1e-6))) * m).sum() / m.sum()
            else:
                logits = res.squeeze(-1)
                # Idea 51: Cox Partial Likelihood Proxy
                if idea_id == '51':
                    hazard = torch.exp(logits)
                    loss = (hazard * m).sum() / m.sum() # Simplified for 0/1 labels
                # Idea 47/97: Focal Loss
                elif idea_id in ['47', '97']:
                    p = torch.sigmoid(logits); pt = torch.where(y == 1, p, 1 - p)
                    loss = (F.binary_cross_entropy_with_logits(logits, y, reduction='none') * (1-pt).pow(2) * m).sum() / m.sum()
                # Idea 49/99: Distribution Matching (MMD)
                elif idea_id in ['49', '99']:
                    loss = (F.binary_cross_entropy_with_logits(logits, y, reduction='none') * m).sum() / m.sum()
                    # Latent space matching
                    h = model.layers[0](x.reshape(-1, in_dim))
                    h_s = h[y.reshape(-1) < 0.5].mean(0); h_f = h[y.reshape(-1) > 0.5].mean(0)
                    if not torch.isnan(h_s).any() and not torch.isnan(h_f).any(): loss += 0.5 * (h_s - h_f).pow(2).mean()
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
