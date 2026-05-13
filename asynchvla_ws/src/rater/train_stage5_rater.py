#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from collections import defaultdict
from pathlib import Path
import numpy as np, torch, torch.nn as nn
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import roc_auc_score

REDA_WS = Path('/media/rootalkhatib/My Passport/reda_ws')
ROOT = REDA_WS / 'asynchvla_ws/data/stage5_debug'
CKROOT = REDA_WS / 'asynchvla_ws/outputs/checkpoints/stage5_debug'
RROOT = REDA_WS / 'asynchvla_ws/outputs/reports'

sys.path.insert(0, str(REDA_WS / 'asynchvla_ws/src'))
from eval.eval_simvla_only import eval_simvla_only

class MLP(nn.Module):
    def __init__(self, d): 
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d, 256), nn.ReLU(), nn.Dropout(.05), nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, 1), nn.Softplus())
    def forward(self, x): 
        return self.net(x).squeeze(-1)

def load_rows(data_dir, part):
    p = data_dir / f'multiseed_candidate_{part}.pt'
    return torch.load(p, map_location='cpu')['candidates'] if p.exists() else []

def feats(rows, mode):
    xs = []; y = []
    for r in rows:
        parts = []
        if mode in ('full', 'context'): parts += [r['pooled_vlm_features'].float().flatten(), r['proprio'].float().flatten()]
        if mode in ('full', 'action'): parts += [r['candidate_action_normalized'].float().flatten()]
        xs.append(torch.cat(parts))
        y.append(float(r['true_chunk_l2_error']))
    return torch.stack(xs), torch.tensor(y, dtype=torch.float32)

def norm(tr, *others):
    mu = tr.mean(0, keepdim=True)
    sd = tr.std(0, keepdim=True).clamp_min(1e-6)
    return [(x - mu) / sd for x in (tr, *others)], mu, sd

def risk(y, p):
    o = np.argsort(p)
    return [(c, float(np.mean(y[o[:max(1, int(round(len(y) * c)))]]))) for c in [.1, .25, .5, .75, 1.0]]

def same(rows, p):
    by = defaultdict(dict)
    for r, pp in zip(rows, p): 
        by[r['context_id']][r['candidate_type']] = (float(pp), float(r['true_chunk_l2_error']))
    
    def acc(a, b):
        n = o = 0
        for d in by.values():
            if a in d and b in d: 
                n += 1
                o += int(d[a][0] < d[b][0])
        return o / n if n else None
        
    std = [float(np.std([v[0] for v in d.values()])) for d in by.values() if len(d) > 1]
    return {
        'expert_lt_perturb_large': acc('expert_action', 'perturb_large'),
        'expert_lt_other_task': acc('expert_action', 'other_demo_or_other_task'),
        'expert_lt_simvla_seed0': acc('expert_action', 'simvla_seed0'),
        'action_sensitivity_std': float(np.mean(std)) if std else None
    }

def evalm(rows, y, p):
    yy = y.numpy()
    pp = p.numpy()
    lab = (yy >= np.quantile(yy, .7)).astype(int)
    
    res = {
        'n': len(rows),
        'pearson': float(pearsonr(pp, yy).statistic) if np.std(pp) > 1e-8 else None,
        'spearman': float(spearmanr(pp, yy).statistic) if np.std(pp) > 1e-8 else None,
        'auroc_top30_bad': float(roc_auc_score(lab, pp)) if len(set(lab)) == 2 and np.std(pp) > 1e-8 else None,
        'mae': float(np.mean(np.abs(pp - yy))),
        'mse': float(np.mean((pp - yy)**2)),
        'risk_coverage': risk(yy, pp),
        **same(rows, pp)
    }
    
    sim_idx = [i for i, r in enumerate(rows) if r['candidate_type'].startswith('simvla_seed')]
    if len(sim_idx) > 0:
        sim_preds = pp[sim_idx]
        sim_trues = yy[sim_idx]
        sim_cids = [rows[i]['context_id'] for i in sim_idx]
        sim_seeds = [int(rows[i]['candidate_type'].replace('simvla_seed', '')) for i in sim_idx]
        res['simvla_only'] = eval_simvla_only(sim_preds, sim_trues, sim_cids, sim_seeds)
        
        for k, v in res['simvla_only'].items():
            if isinstance(v, np.float64): res['simvla_only'][k] = float(v)
        for k, v in res['simvla_only'].get('best_seed', {}).items():
            if isinstance(v, np.float64): res['simvla_only']['best_seed'][k] = float(v)
        for c, v in res['simvla_only'].get('risk_coverage', {}).items():
            if isinstance(v, np.float64): res['simvla_only']['risk_coverage'][c] = float(v)
        for c, d in res['simvla_only'].get('switch_proxy', {}).items():
            for k2, v2 in d.items():
                if isinstance(v2, np.float64): res['simvla_only']['switch_proxy'][c][k2] = float(v2)
    return res

def train(debug=True, split_name=None):
    if debug:
        data_dir = REDA_WS / 'asynchvla_ws/data/stage5_debug'
        parts = ['debug'] 
        split_id = 'stage5_debug'
        CK = REDA_WS / 'asynchvla_ws/outputs/checkpoints/stage5_debug'
    else:
        data_dir = REDA_WS / 'asynchvla_ws/data/processed_stage5' / split_name
        parts = ['train', 'calib', 'test_id', 'test_ood']
        split_id = split_name
        CK = REDA_WS / f'asynchvla_ws/outputs/checkpoints/stage5/{split_name}'
        
    rows = {p: load_rows(data_dir, p) for p in parts}
    out = {'split_name': split_id, 'parts': {k: len(v) for k, v in rows.items()}, 'models': {}}
    CK.mkdir(parents=True, exist_ok=True)
    pred_dump = {}
    
    for mode in ['full', 'context', 'action']:
        if debug:
            xtr, ytr = feats(rows['debug'][:400], mode) 
            xca, yca = feats(rows['debug'][400:], mode) 
        else:
            if not rows['train']: continue
            xtr, ytr = feats(rows['train'], mode)
            xca, yca = feats(rows['calib'], mode)
            
        (xtrn, xcan), mu, sd = norm(xtr, xca)
        model = MLP(xtr.shape[1])
        opt = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)
        lossfn = nn.HuberLoss(delta=.25)
        best = (9e9, None, 0)
        
        for ep in range(1, 100 if debug else 251):
            model.train()
            perm = torch.randperm(len(xtrn))
            for st in range(0, len(perm), 256):
                ix = perm[st:st+256]
                loss = lossfn(model(xtrn[ix]), ytr[ix])
                opt.zero_grad()
                loss.backward()
                opt.step()
            with torch.no_grad(): 
                vl = float(lossfn(model(xcan), yca))
            if vl < best[0]: 
                best = (vl, {k: v.detach().clone() for k, v in model.state_dict().items()}, ep)
                
        model.load_state_dict(best[1])
        model.eval()
        metrics = {}
        preds = {}
        
        eval_parts = {'debug': rows['debug']} if debug else rows
        
        for part, rs in eval_parts.items():
            if not rs: continue
            x, y = feats(rs, mode)
            x = (x - mu) / sd
            with torch.no_grad(): 
                p = model(x).cpu()
            metrics[part] = evalm(rs, y, p)
            preds[part] = [{'context_id': r['context_id'], 'candidate_type': r['candidate_type'], 'true': float(r['true_chunk_l2_error']), 'pred': float(pp)} for r, pp in zip(rs, p)]
            
        out['models'][mode] = {'best_epoch': best[2], 'best_calib_loss': best[0], 'metrics': metrics}
        pred_dump[mode] = preds
        torch.save({'state_dict': model.state_dict(), 'input_mean': mu, 'input_std': sd, 'input_dim': xtr.shape[1], 'mode': mode}, CK / f'{mode}_rater.pt')
        
    (CK / 'predictions.json').write_text(json.dumps(pred_dump))
    
    report_name = 'stage5_debug_rater_metrics.md' if debug else f'stage5_{split_name}_metrics.md'
    lines = ['# Stage 5 Rater Metrics: ' + split_id, '', f'- Checkpoint dir: `{CK}`', '', '## Metrics JSON', '', '```json', json.dumps(out, indent=2), '```']
    RROOT.mkdir(parents=True, exist_ok=True)
    (RROOT / report_name).write_text('\n'.join(lines) + '\n')
    print('trained', split_id, json.dumps(out['parts']), RROOT / report_name)
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--split-name', required=False)
    ap.add_argument('--debug', type=lambda x: str(x).lower() == 'true', default=False)
    args = ap.parse_args()
    train(debug=args.debug, split_name=args.split_name)
