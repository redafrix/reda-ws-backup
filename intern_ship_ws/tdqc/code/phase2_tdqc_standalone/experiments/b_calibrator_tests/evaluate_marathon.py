import torch, numpy as np, os, json
import torch.nn as nn
import torch.nn.functional as F

# --- Model Definitions (Must match training) ---
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
        x_in = x.clone()
        if self.idea_id in ['306', '307', '310', '311']: x_in[:, :, 9:] *= 2.0
        x_pad = F.pad(x_in.transpose(1, 2), (2, 0), mode='replicate')
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

# --- Evaluation Logic ---
def evaluate_idea(idea_id, data_path, device):
    ckpt_path = f'runs/best_{idea_id}.pt'
    if not os.path.exists(ckpt_path): return None
    ckpt = torch.load(ckpt_path, map_location='cpu')
    model = VAE(22).to(device) if idea_id == '301' else CalibratorMLP(22, idea_id).to(device)
    model.load_state_dict(ckpt['model']); model.eval()
    mean, std = ckpt['mean'].to(device), ckpt['std'].to(device)

    obj = torch.load(data_path, map_location='cpu')
    episodes = obj['episodes'] if isinstance(obj, dict) else obj
    
    succ_confs = []
    fail_start = []
    fail_mid = []
    fail_end = []
    fail_step_150 = [] # Confidence when trajectory becomes 'Too Long'

    for ep in episodes:
        feat = torch.tensor(ep['features'], dtype=torch.float32).to(device)
        is_succ = ep['success'] == 1
        x = (feat - mean) / std
        
        with torch.no_grad():
            if idea_id == '301':
                recon, _, _ = model(x)
                error = F.mse_loss(recon, x, reduction='none').mean(dim=-1).cpu().numpy()
                conf = np.exp(-error * 2.0)
            elif idea_id == '305':
                target = x[1:, :]; pred = model(x.unsqueeze(0)).squeeze(0)[:-1, :]
                error = F.mse_loss(pred, target, reduction='none').mean(dim=-1).cpu().numpy()
                conf = np.exp(-error * 10.0)
            else:
                prob = model(x.unsqueeze(0)).squeeze(0).cpu().numpy()
                conf = 1.0 - prob
        
        if is_succ:
            succ_confs.append(np.mean(conf))
        else:
            fail_start.append(np.mean(conf[:10]))
            fail_mid.append(conf[len(conf)//2])
            fail_end.append(np.mean(conf[-10:]))
            if len(conf) > 150:
                fail_step_150.append(conf[150])

    return {
        'succ_mean': float(np.mean(succ_confs)) if succ_confs else 0,
        'fail_start': float(np.mean(fail_start)) if fail_start else 0,
        'fail_mid': float(np.mean(fail_mid)) if fail_mid else 0,
        'fail_end': float(np.mean(fail_end)) if fail_end else 0,
        'fail_150': float(np.mean(fail_step_150)) if fail_step_150 else 0
    }

def main():
    ideas = ['301', '302', '303', '304', '305', '306', '307', '308', '310', '311']
    ood_data = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt'
    device = torch.device('cuda')
    
    results = {}
    for idea in ideas:
        print(f'Evaluating {idea}...')
        results[idea] = evaluate_idea(idea, ood_data, device)
    
    with open('marathon_results.json', 'w') as f:
        json.dump(results, f, indent=4)
    print('Results saved to marathon_results.json')

if __name__ == '__main__':
    main()
