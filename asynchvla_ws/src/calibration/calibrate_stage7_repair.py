#!/usr/bin/env python3
from __future__ import annotations
import json, argparse
from pathlib import Path
import numpy as np

REDA_WS = Path('/media/rootalkhatib/My Passport/reda_ws')
CKROOT = REDA_WS / 'asynchvla_ws/outputs/checkpoints/stage6'
OUT = REDA_WS / 'asynchvla_ws/outputs/reports/stage7/stage7_calibration_repair.md'
LOCAL = Path('/home/redafrix/tests/internship/codex_reports/stage7/stage7_calibration_repair.md')
SPLITS = ['id_task_split', 'holdout_libero_object', 'holdout_object_bowl', 'holdout_libero_spatial']
VARIANT = 'context_gated_action'


def load_preds(split, variant=VARIANT):
    path = CKROOT / split / variant / 'predictions.json'
    if not path.exists():
        return None
    return json.loads(path.read_text())


def simvla_only(rows):
    return [r for r in rows if str(r['candidate_type']).startswith('simvla_seed')]


def eta_from(rows, q=0.90):
    residual = np.array([float(r['true']) - float(r['pred']) for r in rows], dtype=float)
    if len(residual) == 0:
        return None
    return float(np.quantile(residual, q))


def coverage(rows, eta):
    y = np.array([float(r['true']) for r in rows], dtype=float)
    p = np.array([float(r['pred']) for r in rows], dtype=float)
    bound = p + eta
    return {'n': int(len(rows)), 'coverage': float(np.mean(y <= bound)) if len(rows) else None, 'mean_width': float(np.mean(bound - p)) if len(rows) else None, 'mean_bound': float(np.mean(bound)) if len(rows) else None}


def binned_eta(calib_rows, test_rows, bins=4):
    cp = np.array([float(r['pred']) for r in calib_rows], dtype=float)
    if len(cp) < bins * 5:
        eta = eta_from(calib_rows)
        return [coverage(test_rows, eta)] if eta is not None else []
    qs = np.quantile(cp, np.linspace(0, 1, bins + 1))
    rows = []
    for i in range(bins):
        lo, hi = qs[i], qs[i + 1]
        cmask = [r for r in calib_rows if (float(r['pred']) >= lo and (float(r['pred']) <= hi if i == bins - 1 else float(r['pred']) < hi))]
        tmask = [r for r in test_rows if (float(r['pred']) >= lo and (float(r['pred']) <= hi if i == bins - 1 else float(r['pred']) < hi))]
        eta = eta_from(cmask)
        if eta is None:
            eta = eta_from(calib_rows)
        cov = coverage(tmask, eta)
        cov.update({'bin': i, 'lo': float(lo), 'hi': float(hi), 'eta': eta})
        rows.append(cov)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--variant', default=VARIANT)
    args = ap.parse_args()
    lines = ['# Stage 7 Calibration Repair', '', f'- Variant: `{args.variant}`', '- Target coverage: `0.90`', '- Candidate-type conditional calibration is not used as the main deployable method.', '']
    summary = []
    for split in SPLITS:
        pred = load_preds(split, args.variant)
        if pred is None:
            lines += [f'## `{split}`', '', '- Missing predictions; skipped.', '']
            continue
        calib = pred.get('calib', [])
        train = pred.get('train', [])
        parts = [p for p in ['test_id', 'test_ood'] if p in pred]
        eta_global = eta_from(calib)
        eta_sim = eta_from(simvla_only(calib))
        eta_large_pool = eta_from(calib + train)
        lines += [f'## `{split}`', '', f'- Calib rows: `{len(calib)}`; SimVLA calib rows: `{len(simvla_only(calib))}`', f'- Global eta: `{eta_global}`', f'- SimVLA-only eta: `{eta_sim}`', f'- Analysis-only train+calib eta: `{eta_large_pool}`', '', '| Part | Method | N | Coverage | Mean width |', '|---|---|---:|---:|---:|']
        for part in parts:
            rows = pred[part]
            simrows = simvla_only(rows)
            for name, eta, eval_rows in [
                ('global_all_candidates', eta_global, rows),
                ('global_simvla_only_eval', eta_global, simrows),
                ('simvla_only_eta_simvla_eval', eta_sim, simrows),
                ('analysis_train_plus_calib_eta_simvla_eval', eta_large_pool, simrows),
            ]:
                if eta is None:
                    continue
                cov = coverage(eval_rows, eta)
                lines.append(f"| `{part}` | `{name}` | {cov['n']} | {cov['coverage']:.3f} | {cov['mean_width']:.3f} |")
                summary.append({'split': split, 'part': part, 'method': name, **cov})
            bins = binned_eta(simvla_only(calib), simrows)
            if bins:
                total_n = sum(b['n'] for b in bins)
                cov_avg = sum((b['coverage'] or 0) * b['n'] for b in bins) / max(1, total_n)
                width_avg = sum((b['mean_width'] or 0) * b['n'] for b in bins) / max(1, total_n)
                lines.append(f"| `{part}` | `binned_simvla_quantile_eta_simvla_eval` | {total_n} | {cov_avg:.3f} | {width_avg:.3f} |")
                summary.append({'split': split, 'part': part, 'method': 'binned_simvla_quantile_eta_simvla_eval', 'n': total_n, 'coverage': cov_avg, 'mean_width': width_avg})
        if split == 'holdout_object_bowl':
            lines += ['', 'Holdout-object-bowl note: undercoverage remains visible when calibration uses only the designated calibration contexts. The analysis-only train+calib pool indicates whether the issue is calibration-set size/composition, but it is not a deployable claim unless such an additional labeled calibration pool is allowed.', '']
        lines.append('')
    worst = min((x for x in summary if x.get('coverage') is not None), key=lambda x: x['coverage'], default=None)
    if worst:
        lines += ['## Worst Case', '', f"- Worst observed coverage: `{worst['coverage']:.3f}` for split `{worst['split']}`, part `{worst['part']}`, method `{worst['method']}`.", '']
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines) + '\n')
    print(OUT)

if __name__ == '__main__':
    main()
