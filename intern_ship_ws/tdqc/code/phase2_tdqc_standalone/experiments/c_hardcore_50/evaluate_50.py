import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import os, json
from torch.nn.utils import spectral_norm

class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(dim))
    def forward(self, x): 
        return (x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + 1e-6)) * self.weight

class CalibratorMLP(nn.Module):
    def __init__(self, in_d, out_d=1, idea_id='0'):
        super().__init__()
        self.idea_id = str(idea_id)
        h = 128 if self.idea_id in ['35', '60'] else 256
        self.mlp = nn.Sequential(
            nn.Linear(in_d, h), RMSNorm(h), nn.SiLU(),
            nn.Linear(h, h), RMSNorm(h), nn.SiLU(),
            nn.Linear(h, h), RMSNorm(h), nn.SiLU(),
            nn.Linear(h, out_d)
        )
        if idea_id == '43': self.recovery_head = nn.Linear(h, 1)

    def forward(self, x):
        B, L, D = x.shape
        x_flat = x.reshape(B * L, D)
        features = self.mlp[:-1](x_flat)
        out = self.mlp[-1](features).reshape(B, L, -1)
        if self.idea_id == '43':
            rec = self.recovery_head(features).reshape(B, L, -1)
            return out, rec
        return out

class HardcoreCalibrator(nn.Module):
    def __init__(self, in_d, out_d=1, idea_id='0'):
        super().__init__()
        self.idea_id = str(idea_id)
        h = 128 if self.idea_id in ['35', '60'] else 256
        def get_layer(i, o):
            layer = nn.Linear(i, o)
            if self.idea_id in ['57', '77', '27']: return spectral_norm(layer)
            return layer
        self.layers = nn.ModuleList([get_layer(in_d, h), get_layer(h, h), get_layer(h, h)])
        self.norms = nn.ModuleList([RMSNorm(h) for _ in range(3)])
        self.head = get_layer(h, out_d)
        if self.idea_id == '43': self.recovery_head = nn.Linear(h, 1)
        if self.idea_id in ['11', '61']: self.evidence_head = nn.Sequential(nn.Linear(h, 2), nn.Softplus())

    def forward(self, x):
        B, L, D = x.shape
        do_dropout = self.idea_id in ['8', '58']
        h = x.reshape(B * L, D)
        for i in range(len(self.layers)):
            h = self.layers[i](h)
            h = self.norms[i](h)
            h = F.silu(h)
            if do_dropout: h = F.dropout(h, p=0.2, training=False) # Keep dropout False for eval unless forced
            if self.idea_id in ['15', '65']:
                tau = torch.sigmoid(h[:, :1])
                h = h * torch.exp(-tau)
        out = self.head(h).reshape(B, L, -1)
        if self.idea_id == '43':
            rec = self.recovery_head(h).reshape(B, L, -1)
            return out, rec
        if self.idea_id in ['11', '61']:
            ev = self.evidence_head(h).reshape(B, L, 2)
            return out, ev
        return out

def apply_feature_eng(x, idea_id):
    idea_id = str(idea_id)
    B, L, D = x.shape
    if idea_id in ['4', '54']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(v); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        if idea_id == '4': return torch.cat([v, a], dim=-1)
        return torch.cat([x, v, a], dim=-1)
    if idea_id in ['22', '72']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        power = (x[:, :, 14:22] * v[:, :, 0:8]).sum(dim=-1, keepdim=True)
        return torch.cat([x, power], dim=-1)
    if idea_id in ['23', '73']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        ke = (v[:, :, 0:8]**2).sum(dim=-1, keepdim=True)
        return torch.cat([x, ke], dim=-1)
    if idea_id in ['29', '79']:
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(v); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        j = torch.zeros_like(a); j[:, 1:, :] = a[:, 1:, :] - a[:, :-1, :]
        return torch.cat([x, j], dim=-1)
    if idea_id == '87':
        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        return torch.sign(v)
    if idea_id in ['13', '86']:
        v1 = x[:, 1:, :] - x[:, :-1, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        return torch.cat([x, v1.mean(1, keepdim=True).repeat(1, L, 1), v3.mean(1, keepdim=True).repeat(1, L, 1)], dim=-1)
    return x

def evaluate():
    import warnings
    warnings.filterwarnings('ignore')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    data_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt'
    data = torch.load(data_path, map_location='cpu')
    eps = data['episodes']
    results = {}
    for i in range(1, 51):
        idea_id = str(i)
        ckpt_path = f'runs/best_{idea_id}.pt'
        if not os.path.exists(ckpt_path): continue
        print(f'Evaluating Idea {idea_id}...')
        try:
            ckpt = torch.load(ckpt_path, map_location=device)
            dummy_x = torch.zeros(1, 10, 22).to(device)
            dummy_x = apply_feature_eng(dummy_x, idea_id)
            in_dim = dummy_x.shape[-1]
            
            if 'mlp.0.weight' in ckpt['model']:
                model = CalibratorMLP(in_dim, idea_id=idea_id).to(device)
            else:
                model = HardcoreCalibrator(in_dim, idea_id=idea_id).to(device)
                
            model.load_state_dict(ckpt['model'])
            model.eval()
            mean = ckpt['mean'].to(device)
            std = ckpt['std'].to(device)
            
            sc, ec, fpr_f, rec_f, lt = [], [], [], [], []
            with torch.no_grad():
                for ep in eps:
                    f = (torch.tensor(ep['features'], dtype=torch.float32).to(device) - mean) / std
                    f = f.unsqueeze(0)
                    f_eng = apply_feature_eng(f, idea_id)
                    res = model(f_eng)
                    
                    if idea_id == '43': logits = res[0]
                    elif idea_id in ['11', '61'] and isinstance(model, HardcoreCalibrator):
                        ev = res[1]
                        s_ev = ev[:, :, 0]; f_ev = ev[:, :, 1]
                        conf = (s_ev / (s_ev + f_ev + 1e-6)).squeeze(0).cpu().numpy()
                    else: logits = res
                    
                    if idea_id not in ['11', '61'] or isinstance(model, CalibratorMLP):
                        logits = logits.squeeze(-1)
                        if idea_id == '51':
                            hazard = torch.exp(logits).squeeze(0).cpu().numpy()
                            conf = np.exp(-hazard)
                        else:
                            conf = 1.0 - torch.sigmoid(logits).squeeze(0).cpu().numpy()
                            
                    if len(conf.shape) > 1: conf = conf[:, 0]
                    L = len(conf)
                    if ep['success'] == 1:
                        sc.append(np.mean(conf[:10]))
                        ec.append(np.mean(conf[-10:]))
                        fpr_f.append(1 if np.min(conf) < 0.5 else 0)
                    else:
                        fail_idx = np.where(conf < 0.5)[0]
                        if len(fail_idx) > 0:
                            rec_f.append(1)
                            lt.append(L - fail_idx[0])
                        else:
                            rec_f.append(0)
            
            results[idea_id] = {
                'Recall': float(np.mean(rec_f) * 100) if rec_f else 0.0,
                'FPR': float(np.mean(fpr_f) * 100) if fpr_f else 0.0,
                'LeadTime': float(np.mean(lt)) if lt else 0.0,
                'StartConf': float(np.mean(sc) * 100) if sc else 0.0,
                'EndConf': float(np.mean(ec) * 100) if ec else 0.0,
                'Total': float(np.mean(rec_f)*100 - np.mean(fpr_f)*100) if rec_f and fpr_f else 0.0
            }
        except Exception as e:
            print(f'Error evaluating Idea {idea_id}: {e}')
            
    with open('eval_results_1_50.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == '__main__':
    evaluate()
