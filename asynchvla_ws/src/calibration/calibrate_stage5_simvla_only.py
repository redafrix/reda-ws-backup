#!/usr/bin/env python3
"""Stage 5 — SimVLA-only conformal calibration.

Loads the predictions emitted by `train_stage5_rater.py` for a given split,
fits three calibration schemes on the `calib` partition, and evaluates
coverage on `test_id` and `test_ood` SimVLA candidates.

Calibration schemes
-------------------
1. global_residual
   Conformal residual on ALL calib candidates (any type). Predicts a
   prediction-symmetric interval [pred - q, pred + q] for any test point.
2. simvla_only_residual
   Conformal residual on `simvla_seed*` calib candidates only.
3. simvla_only_binned
   Same residual approach but bucket the calib SimVLA points into N bins by
   predicted uncertainty and use the bin-specific q. At test time, fall back
   to the global SimVLA q for empty bins.

We only report calibration on SimVLA-only test candidates (the deployable
case — runtime does not know whether an action is synthetic).

The script is robust to missing partitions and uses NpEncoder for JSON.
"""
from __future__ import annotations
import argparse, json, math, sys, time
from collections import defaultdict
from pathlib import Path

import numpy as np

REDA_WS = Path('/media/rootalkhatib/My Passport/reda_ws')
RROOT = REDA_WS / 'asynchvla_ws/outputs/reports'
CKROOT = REDA_WS / 'asynchvla_ws/outputs/checkpoints/stage5'

sys.path.insert(0, str(REDA_WS / 'asynchvla_ws/src'))


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, Path):
            return str(obj)
        return super().default(obj)


def _conformal_q(residuals, alpha):
    n = len(residuals)
    if n == 0:
        return None
    k = int(math.ceil((n + 1) * (1 - alpha)))
    k = min(max(k, 1), n)
    return float(np.sort(residuals)[k - 1])


def _coverage(pred, true, q):
    return float(np.mean(np.abs(true - pred) <= q))


def _width(q):
    return float(2 * q) if q is not None else None


def _simvla_only(rows):
    return [r for r in rows if str(r['candidate_type']).startswith('simvla_seed')]


def calibrate_split(split_name, alpha=0.1, n_bins=4):
    pred_path = CKROOT / split_name / 'predictions.json'
    if not pred_path.exists():
        raise FileNotFoundError(f'no predictions at {pred_path}')
    preds = json.loads(pred_path.read_text())
    if 'full' not in preds:
        raise KeyError(f'predictions.json for {split_name} has no `full` mode')

    full = preds['full']  # dict[part] -> list of {context_id, candidate_type, true, pred}
    calib = full.get('calib', [])
    if not calib:
        raise ValueError(f'no calib partition in predictions for {split_name}')

    test_parts = {p: full.get(p, []) for p in ('test_id', 'test_ood') if full.get(p)}
    if not test_parts:
        raise ValueError(f'no test_id/test_ood partitions in predictions for {split_name}')

    results = {
        'split_name': split_name,
        'alpha': alpha,
        'n_calib_all': len(calib),
        'n_calib_simvla': len(_simvla_only(calib)),
        'test_parts': {p: {'n_total': len(v), 'n_simvla': len(_simvla_only(v))}
                       for p, v in test_parts.items()},
        'schemes': {},
    }

    # ----- scheme 1: global residual on ALL calib candidates -----
    all_calib_pred = np.array([r['pred'] for r in calib])
    all_calib_true = np.array([r['true'] for r in calib])
    q_global = _conformal_q(np.abs(all_calib_pred - all_calib_true), alpha)

    # ----- scheme 2: simvla-only residual on calib SimVLA-only -----
    sim_calib = _simvla_only(calib)
    sim_calib_pred = np.array([r['pred'] for r in sim_calib]) if sim_calib else np.array([])
    sim_calib_true = np.array([r['true'] for r in sim_calib]) if sim_calib else np.array([])
    q_sim = _conformal_q(np.abs(sim_calib_pred - sim_calib_true), alpha) if len(sim_calib) else None

    # ----- scheme 3: binned (by predicted uncertainty) over simvla-only -----
    bin_quants = np.quantile(sim_calib_pred, np.linspace(0, 1, n_bins + 1)) if len(sim_calib_pred) else np.array([])
    bin_q = []
    for b in range(n_bins):
        lo, hi = bin_quants[b], bin_quants[b + 1]
        if b == n_bins - 1:
            mask = (sim_calib_pred >= lo) & (sim_calib_pred <= hi)
        else:
            mask = (sim_calib_pred >= lo) & (sim_calib_pred < hi)
        residuals = np.abs(sim_calib_pred[mask] - sim_calib_true[mask])
        bin_q.append({'lo': float(lo), 'hi': float(hi), 'n': int(mask.sum()),
                      'q': _conformal_q(residuals, alpha)})

    def assign_bin(p):
        if len(bin_quants) == 0:
            return None
        for b in range(n_bins):
            lo, hi = bin_quants[b], bin_quants[b + 1]
            if b == n_bins - 1:
                if p >= lo and p <= hi:
                    return b
            else:
                if p >= lo and p < hi:
                    return b
        # outside calib range -> clamp to nearest bin
        return n_bins - 1 if p > bin_quants[-1] else 0

    # ----- evaluate on test parts (SimVLA-only) -----
    schemes = ('global_residual', 'simvla_only_residual', 'simvla_only_binned')
    out_schemes = {s: {'q_calib': None, 'parts': {}} for s in schemes}
    out_schemes['global_residual']['q_calib'] = q_global
    out_schemes['global_residual']['mean_width'] = _width(q_global)
    out_schemes['simvla_only_residual']['q_calib'] = q_sim
    out_schemes['simvla_only_residual']['mean_width'] = _width(q_sim)
    out_schemes['simvla_only_binned']['bins'] = bin_q

    for part_name, rows in test_parts.items():
        sim_rows = _simvla_only(rows)
        if not sim_rows:
            continue
        p_arr = np.array([r['pred'] for r in sim_rows])
        t_arr = np.array([r['true'] for r in sim_rows])

        if q_global is not None:
            out_schemes['global_residual']['parts'][part_name] = {
                'n': len(sim_rows),
                'empirical_coverage': _coverage(p_arr, t_arr, q_global),
                'mean_width': _width(q_global),
            }
        if q_sim is not None:
            out_schemes['simvla_only_residual']['parts'][part_name] = {
                'n': len(sim_rows),
                'empirical_coverage': _coverage(p_arr, t_arr, q_sim),
                'mean_width': _width(q_sim),
            }
        if bin_q:
            bin_assignments = np.array([assign_bin(p) for p in p_arr])
            widths = []
            covered = []
            for p, t, b in zip(p_arr, t_arr, bin_assignments):
                q = bin_q[b]['q'] if (b is not None and bin_q[b]['q'] is not None) else q_sim
                if q is None:
                    continue
                widths.append(2 * q)
                covered.append(int(abs(t - p) <= q))
            out_schemes['simvla_only_binned']['parts'][part_name] = {
                'n': len(covered),
                'empirical_coverage': float(np.mean(covered)) if covered else None,
                'mean_width': float(np.mean(widths)) if widths else None,
                'bin_assignment_counts': [int((bin_assignments == b).sum()) for b in range(n_bins)],
            }

    results['schemes'] = out_schemes
    return results


def render_md(res):
    lines = [f'# Stage 5 SimVLA-only calibration: {res["split_name"]}', '',
             f'- alpha (miscoverage budget): {res["alpha"]}',
             f'- target coverage: {1 - res["alpha"]:.2f}',
             f'- n_calib_all = {res["n_calib_all"]}, n_calib_simvla = {res["n_calib_simvla"]}',
             '']
    lines.append('## Test sizes')
    lines.append('')
    lines.append('| part | n_total | n_simvla |')
    lines.append('| --- | ---: | ---: |')
    for p, d in res['test_parts'].items():
        lines.append(f'| {p} | {d["n_total"]} | {d["n_simvla"]} |')

    lines.append('')
    lines.append('## Coverage and width per scheme')
    lines.append('')
    lines.append('| scheme | part | n | coverage | mean_width |')
    lines.append('| --- | --- | ---: | ---: | ---: |')
    for sname, sdata in res['schemes'].items():
        for part, m in sdata.get('parts', {}).items():
            lines.append(f'| {sname} | {part} | {m["n"]} | {m["empirical_coverage"]:.3f} | {m["mean_width"]:.3f} |')

    lines.append('')
    lines.append('## Calib q values')
    lines.append('')
    lines.append('```json')
    lines.append(json.dumps({k: {ik: iv for ik, iv in v.items() if ik not in ('parts',)} for k, v in res['schemes'].items()}, indent=2, cls=NpEncoder))
    lines.append('```')

    lines.append('')
    lines.append('## Full JSON')
    lines.append('')
    lines.append('```json')
    lines.append(json.dumps(res, indent=2, cls=NpEncoder))
    lines.append('```')
    return '\n'.join(lines) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--split-name', required=True)
    ap.add_argument('--alpha', type=float, default=0.1)
    ap.add_argument('--n-bins', type=int, default=4)
    ap.add_argument('--out-md', default=None)
    ap.add_argument('--out-json', default=None)
    args = ap.parse_args()

    res = calibrate_split(args.split_name, alpha=args.alpha, n_bins=args.n_bins)
    out_md = Path(args.out_md) if args.out_md else RROOT / f'stage5_{args.split_name}_simvla_only_calibration.md'
    out_json = Path(args.out_json) if args.out_json else RROOT / f'stage5_{args.split_name}_simvla_only_calibration.json'
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(render_md(res))
    out_json.write_text(json.dumps(res, indent=2, cls=NpEncoder))
    print('calibration written', args.split_name, out_md)


if __name__ == '__main__':
    main()
