#!/usr/bin/env python3
"""Stage 5 rater — v2.

Trains a small MLP that predicts the L2 chunk error of a candidate action
against the expert action for the same observation. Supports three modes:

- full     : pooled VLM + proprio + candidate action
- context  : pooled VLM + proprio (no action)
- action   : candidate action only

Splits:
- debug: load `data/stage5_debug/multiseed_candidate_debug.pt` and produce a
  deterministic CONTEXT-LEVEL train/val(=calib)/test partition (60/20/20)
  hashed on context_id, so candidates from the same context never leak
  between partitions.
- non-debug: load `data/processed_stage5/<split_name>/multiseed_candidate_{train,calib,test_id,test_ood}.pt`.

Metrics:
- All candidates: Pearson, Spearman, AUROC@top30, MAE, MSE, risk-coverage,
  same-context ranking (expert vs perturb_large / other_task / simvla_seed0),
  and action_sensitivity_std.
- SimVLA-only: Pearson, Spearman, AUROC, pairwise seed ranking, best-seed
  selection (predicted/seed0/random/oracle), risk-coverage, switch proxy.

Reports + JSON are written into outputs/reports/. All json.dumps calls use
NpEncoder for safe numpy/torch/Path serialisation.
"""
from __future__ import annotations
import argparse, hashlib, json, sys, time
from collections import defaultdict, Counter
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import roc_auc_score

REDA_WS = Path('/media/rootalkhatib/My Passport/reda_ws')
RROOT = REDA_WS / 'asynchvla_ws/outputs/reports'

sys.path.insert(0, str(REDA_WS / 'asynchvla_ws/src'))
from eval.eval_simvla_only import eval_simvla_only  # noqa: E402


# --------------------------------------------------------------------------- #
# Safe JSON encoder
# --------------------------------------------------------------------------- #
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, torch.Tensor):
            return obj.detach().cpu().tolist()
        if isinstance(obj, Path):
            return str(obj)
        if isinstance(obj, (set, tuple)):
            return list(obj)
        return super().default(obj)


def _dumps(obj, indent=None):
    return json.dumps(obj, indent=indent, cls=NpEncoder)


# --------------------------------------------------------------------------- #
# Model
# --------------------------------------------------------------------------- #
class MLP(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d, 256), nn.ReLU(), nn.Dropout(0.05),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 1), nn.Softplus(),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #
def load_rows(path: Path):
    if not path.exists():
        return []
    obj = torch.load(path, map_location='cpu', weights_only=False)
    return obj.get('candidates', [])


def feats(rows, mode):
    xs = []
    y = []
    for r in rows:
        parts = []
        if mode in ('full', 'context'):
            parts.append(r['pooled_vlm_features'].float().flatten())
            parts.append(r['proprio'].float().flatten())
        if mode in ('full', 'action'):
            parts.append(r['candidate_action_normalized'].float().flatten())
        xs.append(torch.cat(parts))
        y.append(float(r['true_chunk_l2_error']))
    return torch.stack(xs), torch.tensor(y, dtype=torch.float32)


def norm(tr, *others):
    mu = tr.mean(0, keepdim=True)
    sd = tr.std(0, keepdim=True).clamp_min(1e-6)
    return [(x - mu) / sd for x in (tr, *others)], mu, sd


def deterministic_context_split(rows, ratios=(0.6, 0.2, 0.2), salt='stage5_debug'):
    """Hash context_id -> bucket; return (train_rows, val_rows, test_rows, info)."""
    by_ctx = defaultdict(list)
    for r in rows:
        by_ctx[r['context_id']].append(r)

    cids = sorted(by_ctx.keys())
    rng_keys = []
    for cid in cids:
        h = hashlib.md5(f'{salt}:{cid}'.encode()).hexdigest()
        rng_keys.append((int(h[:8], 16) / 0xFFFFFFFF, cid))
    rng_keys.sort()
    n = len(rng_keys)
    n_tr = int(round(n * ratios[0]))
    n_va = int(round(n * ratios[1]))
    train_cids = {c for _, c in rng_keys[:n_tr]}
    val_cids = {c for _, c in rng_keys[n_tr:n_tr + n_va]}
    test_cids = {c for _, c in rng_keys[n_tr + n_va:]}

    train_rows = [r for cid in cids if cid in train_cids for r in by_ctx[cid]]
    val_rows = [r for cid in cids if cid in val_cids for r in by_ctx[cid]]
    test_rows = [r for cid in cids if cid in test_cids for r in by_ctx[cid]]

    info = {
        'train': {'contexts': len(train_cids), 'rows': len(train_rows)},
        'val':   {'contexts': len(val_cids),   'rows': len(val_rows)},
        'test':  {'contexts': len(test_cids),  'rows': len(test_rows)},
        'total_contexts': n,
        'total_rows': len(rows),
        'salt': salt,
        'ratios': list(ratios),
    }
    return train_rows, val_rows, test_rows, info


# --------------------------------------------------------------------------- #
# Metrics
# --------------------------------------------------------------------------- #
def risk_coverage(y, p):
    o = np.argsort(p)
    out = []
    for c in [0.1, 0.25, 0.5, 0.75, 1.0]:
        k = max(1, int(round(len(y) * c)))
        out.append([float(c), float(np.mean(y[o[:k]]))])
    return out


def same_context_pairs(rows, p):
    by = defaultdict(dict)
    for r, pp in zip(rows, p):
        by[r['context_id']][r['candidate_type']] = (float(pp), float(r['true_chunk_l2_error']))

    def acc(a, b):
        n = ok = 0
        for d in by.values():
            if a in d and b in d:
                n += 1
                ok += int(d[a][0] < d[b][0])
        return float(ok / n) if n else None

    stds = [float(np.std([v[0] for v in d.values()])) for d in by.values() if len(d) > 1]
    return {
        'expert_lt_perturb_large': acc('expert_action', 'perturb_large'),
        'expert_lt_other_task': acc('expert_action', 'other_demo_or_other_task'),
        'expert_lt_simvla_seed0': acc('expert_action', 'simvla_seed0'),
        'action_sensitivity_std_mean': float(np.mean(stds)) if stds else None,
        'action_sensitivity_std_min': float(np.min(stds)) if stds else None,
    }


def evalm(rows, y, p):
    yy = y.numpy() if hasattr(y, 'numpy') else np.asarray(y, dtype=np.float32)
    pp = p.numpy() if hasattr(p, 'numpy') else np.asarray(p, dtype=np.float32)
    lab = (yy >= np.quantile(yy, 0.7)).astype(int)

    res = {
        'n': len(rows),
        'pearson': float(pearsonr(pp, yy).statistic) if np.std(pp) > 1e-8 else None,
        'spearman': float(spearmanr(pp, yy).statistic) if np.std(pp) > 1e-8 else None,
        'auroc_top30_bad': float(roc_auc_score(lab, pp)) if len(set(lab)) == 2 and np.std(pp) > 1e-8 else None,
        'mae': float(np.mean(np.abs(pp - yy))),
        'mse': float(np.mean((pp - yy) ** 2)),
        'risk_coverage': risk_coverage(yy, pp),
        **same_context_pairs(rows, pp),
    }

    sim_idx = [i for i, r in enumerate(rows) if str(r['candidate_type']).startswith('simvla_seed')]
    if len(sim_idx) > 1:
        sim_preds = pp[sim_idx]
        sim_trues = yy[sim_idx]
        sim_cids = [rows[i]['context_id'] for i in sim_idx]
        sim_seeds = [int(rows[i]['candidate_type'].replace('simvla_seed', '')) for i in sim_idx]
        try:
            res['simvla_only'] = eval_simvla_only(sim_preds, sim_trues, sim_cids, sim_seeds)
        except Exception as exc:
            res['simvla_only'] = {'error': repr(exc), 'n_simvla': len(sim_idx)}
        # ensure JSON-safe values in nested dicts
        try:
            json.dumps(res['simvla_only'], cls=NpEncoder)
        except Exception as exc:
            res['simvla_only'] = {'error_serialize': repr(exc), 'n_simvla': len(sim_idx)}
    else:
        res['simvla_only'] = None
    return res


def candidate_type_counts(rows):
    return dict(Counter(r['candidate_type'] for r in rows))


# --------------------------------------------------------------------------- #
# Training loop
# --------------------------------------------------------------------------- #
def train_one(mode, train_rows, val_rows, eval_parts, epochs, lr=2e-3):
    xtr, ytr = feats(train_rows, mode)
    xva, yva = feats(val_rows, mode)
    (xtrn, xvan), mu, sd = norm(xtr, xva)

    model = MLP(xtr.shape[1])
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    lossfn = nn.HuberLoss(delta=0.25)
    best = (9e9, None, 0)
    bs = 256

    for ep in range(1, epochs + 1):
        model.train()
        perm = torch.randperm(len(xtrn))
        for st in range(0, len(perm), bs):
            ix = perm[st:st + bs]
            loss = lossfn(model(xtrn[ix]), ytr[ix])
            opt.zero_grad()
            loss.backward()
            opt.step()
        with torch.no_grad():
            vl = float(lossfn(model(xvan), yva))
        if vl < best[0]:
            best = (vl, {k: v.detach().clone() for k, v in model.state_dict().items()}, ep)

    model.load_state_dict(best[1])
    model.eval()
    metrics = {}
    preds = {}
    for part, rs in eval_parts.items():
        if not rs:
            continue
        x, y = feats(rs, mode)
        x = (x - mu) / sd
        with torch.no_grad():
            p = model(x).cpu()
        metrics[part] = evalm(rs, y, p)
        preds[part] = [
            {'context_id': r['context_id'],
             'candidate_type': r['candidate_type'],
             'true': float(r['true_chunk_l2_error']),
             'pred': float(pp)} for r, pp in zip(rs, p)
        ]

    return {
        'model': model,
        'mu': mu, 'sd': sd, 'input_dim': xtr.shape[1],
        'best_epoch': best[2], 'best_val_loss': best[0],
        'metrics': metrics, 'preds': preds,
    }


# --------------------------------------------------------------------------- #
# Report rendering
# --------------------------------------------------------------------------- #
def _fmt(v, n=4):
    if v is None or (isinstance(v, float) and (np.isnan(v) or np.isinf(v))):
        return 'n/a'
    if isinstance(v, float):
        return f'{v:.{n}f}'
    return str(v)


def render_full_table(out):
    lines = ['## Full-candidate metrics', '', '| mode | part | n | pearson | spearman | AUROC | MAE | exp<perturb | exp<other | exp<seed0 | act_std_mean |',
             '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for mode, mdata in out['models'].items():
        for part, m in mdata['metrics'].items():
            lines.append('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |'.format(
                mode, part, m['n'],
                _fmt(m.get('pearson')), _fmt(m.get('spearman')),
                _fmt(m.get('auroc_top30_bad')), _fmt(m.get('mae')),
                _fmt(m.get('expert_lt_perturb_large')),
                _fmt(m.get('expert_lt_other_task')),
                _fmt(m.get('expert_lt_simvla_seed0')),
                _fmt(m.get('action_sensitivity_std_mean')),
            ))
    return '\n'.join(lines)


def render_simvla_table(out):
    lines = ['## SimVLA-only metrics', '',
             '| mode | part | n_sim | pearson | spearman | AUROC | pairwise | best-pred | seed0 | random | oracle | impr_over_seed0 | gap_to_oracle |',
             '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for mode, mdata in out['models'].items():
        for part, m in mdata['metrics'].items():
            so = m.get('simvla_only') or {}
            if not so or 'error' in so:
                continue
            bs = so.get('best_seed', {})
            lines.append('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |'.format(
                mode, part,
                _fmt(bs.get('predicted_best') is not None and len(m.get('risk_coverage', [])) or '-'),
                _fmt(so.get('pearson')), _fmt(so.get('spearman')),
                _fmt(so.get('auroc')), _fmt(so.get('pairwise_acc')),
                _fmt(bs.get('predicted_best')), _fmt(bs.get('seed0')),
                _fmt(bs.get('random')), _fmt(bs.get('oracle_best')),
                _fmt(bs.get('improvement_over_seed0')),
                _fmt(bs.get('gap_to_oracle')),
            ))
    return '\n'.join(lines)


def render_switch_proxy(out):
    lines = ['## SimVLA-only switch proxy (reject highest-uncertainty)', '',
             '| mode | part | reject% | accepted_mean | rejected_mean |',
             '| --- | --- | ---: | ---: | ---: |']
    for mode, mdata in out['models'].items():
        for part, m in mdata['metrics'].items():
            so = m.get('simvla_only') or {}
            for rr, d in (so.get('switch_proxy') or {}).items():
                lines.append('| {} | {} | {} | {} | {} |'.format(
                    mode, part, _fmt(rr * 100 if isinstance(rr, float) else rr, 0),
                    _fmt(d.get('accepted_mean')), _fmt(d.get('rejected_mean'))))
    return '\n'.join(lines)


# --------------------------------------------------------------------------- #
# Main driver
# --------------------------------------------------------------------------- #
def run(debug=True, split_name=None, train_setting='mixed', epochs=None):
    started = time.time()
    if debug:
        data_dir = REDA_WS / 'asynchvla_ws/data/stage5_debug'
        cand_path = data_dir / 'multiseed_candidate_debug.pt'
        all_rows = load_rows(cand_path)
        if not all_rows:
            raise FileNotFoundError(f'No candidates loaded from {cand_path}')

        train_rows, val_rows, test_rows, split_info = deterministic_context_split(
            all_rows, ratios=(0.6, 0.2, 0.2), salt='stage5_debug')

        eval_parts = {'train': train_rows, 'val': val_rows, 'test': test_rows}
        split_id = 'stage5_debug'
        CK = REDA_WS / 'asynchvla_ws/outputs/checkpoints/stage5_debug'
        report_md = RROOT / 'stage5_debug_rater_metrics_v2.md'
        report_json = RROOT / 'stage5_debug_rater_metrics_v2.json'
        epochs = epochs or 100
    else:
        if not split_name:
            raise ValueError('--split-name required when --debug is false')
        data_dir = REDA_WS / 'asynchvla_ws/data/processed_stage5' / split_name
        parts = {p: load_rows(data_dir / f'multiseed_candidate_{p}.pt')
                 for p in ['train', 'calib', 'test_id', 'test_ood']}
        train_rows = parts['train']
        val_rows = parts['calib']
        if not train_rows or not val_rows:
            raise FileNotFoundError(f'Missing train/calib in {data_dir}')
        eval_parts = {k: v for k, v in parts.items() if v}
        split_info = {k: {'rows': len(v),
                          'contexts': len({r['context_id'] for r in v}),
                          'candidate_types': candidate_type_counts(v)}
                      for k, v in parts.items() if v}
        split_id = split_name
        CK = REDA_WS / f'asynchvla_ws/outputs/checkpoints/stage5/{split_name}'
        report_md = RROOT / f'stage5_{split_name}_metrics.md'
        report_json = RROOT / f'stage5_{split_name}_metrics.json'
        epochs = epochs or 251

    if train_setting == 'simvla_focused':
        def is_simvla(r):
            return str(r['candidate_type']).startswith('simvla_seed')

        def is_balance(r):
            return r['candidate_type'] in ('expert_action', 'perturb_small', 'perturb_large',
                                           'same_task_far', 'other_demo_or_other_task')

        sim_train = [r for r in train_rows if is_simvla(r)]
        bal_train = [r for r in train_rows if is_balance(r)]
        # cap balance rows at the size of simvla rows so training is simvla-dominant
        bal_keep = bal_train[:max(1, len(sim_train))]
        train_rows = sim_train + bal_keep

    out = {
        'split_id': split_id,
        'train_setting': train_setting,
        'split_info': split_info,
        'epochs': epochs,
        'models': {},
        'candidate_type_counts': {part: candidate_type_counts(rs)
                                   for part, rs in eval_parts.items()},
    }

    CK.mkdir(parents=True, exist_ok=True)
    RROOT.mkdir(parents=True, exist_ok=True)
    pred_dump = {}

    for mode in ['full', 'context', 'action']:
        info = train_one(mode, train_rows, val_rows, eval_parts, epochs=epochs)
        out['models'][mode] = {
            'best_epoch': info['best_epoch'],
            'best_val_loss': info['best_val_loss'],
            'input_dim': info['input_dim'],
            'metrics': info['metrics'],
        }
        pred_dump[mode] = info['preds']
        torch.save({
            'state_dict': info['model'].state_dict(),
            'input_mean': info['mu'], 'input_std': info['sd'],
            'input_dim': info['input_dim'], 'mode': mode,
        }, CK / f'{mode}_rater.pt')

    out['runtime_seconds'] = time.time() - started

    # Save predictions and machine-readable JSON
    (CK / 'predictions.json').write_text(_dumps(pred_dump))
    report_json.write_text(_dumps(out, indent=2))

    # Markdown report
    lines = [
        f'# Stage 5 Rater Metrics v2: {split_id}',
        '',
        f'- Train setting: `{train_setting}`',
        f'- Epochs: {epochs}',
        f'- Runtime: {out["runtime_seconds"]:.1f}s',
        f'- Checkpoint dir: `{CK}`',
        '',
        '## Split info',
        '',
        '```json',
        _dumps(split_info, indent=2),
        '```',
        '',
        '## Candidate type counts per part',
        '',
        '```json',
        _dumps(out['candidate_type_counts'], indent=2),
        '```',
        '',
        render_full_table(out),
        '',
        render_simvla_table(out),
        '',
        render_switch_proxy(out),
        '',
        '## Best epoch / val loss per mode',
        '',
        '```json',
        _dumps({m: {'best_epoch': d['best_epoch'], 'best_val_loss': d['best_val_loss']}
                for m, d in out['models'].items()}, indent=2),
        '```',
        '',
        '## Full metrics JSON',
        '',
        '```json',
        _dumps(out, indent=2),
        '```',
        '',
    ]
    report_md.write_text('\n'.join(lines))
    print('trained', split_id,
          'parts', _dumps({p: len(rs) for p, rs in eval_parts.items()}),
          'report', str(report_md))
    return out


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _parse_bool(x):
    if isinstance(x, bool):
        return x
    s = str(x).strip().lower()
    if s in ('', 'true', '1', 'yes', 'y'):
        return True
    if s in ('false', '0', 'no', 'n'):
        return False
    raise ValueError(f'unrecognized boolean: {x}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--split-name', required=False, default=None)
    ap.add_argument('--debug', nargs='?', const='true', default='false')
    ap.add_argument('--train-setting', default='mixed', choices=['mixed', 'simvla_focused'])
    ap.add_argument('--epochs', type=int, default=0)
    args = ap.parse_args()
    debug = _parse_bool(args.debug)
    epochs = args.epochs if args.epochs > 0 else None
    run(debug=debug, split_name=args.split_name,
        train_setting=args.train_setting, epochs=epochs)


if __name__ == '__main__':
    main()
