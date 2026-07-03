#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch

ROOT = Path('/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608')
TRAIN_SCRIPT = ROOT / 'src/train_frozen_detectors_h10_proof.py'
RUN_ROOT = ROOT / 'inputs/datasets/continuous_chunk10_flat'
MODEL_DIR = ROOT / 'models/h10_continuous/all_tasks_random/unc_topk8'
OUT_ROOT = ROOT / 'models/h10_continuous/all_tasks_random/unc_topk8_seen_calibration_audit_20260629'
VARIANT = 'unc_topk8'
SPLIT = 'all_tasks_random'

spec = importlib.util.spec_from_file_location('h10train', str(TRAIN_SCRIPT))
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def load_norm(path: Path):
    raw = json.loads(path.read_text())
    return {k: {kk: np.asarray(vv, dtype=np.float32) for kk, vv in val.items()} for k, val in raw.items()}


def by_episode(scores, ids, timesteps, episodes):
    out = defaultdict(list)
    for s, eid, t in zip(scores, ids, timesteps):
        out[eid].append((int(t), float(s)))
    for vals in out.values():
        vals.sort(key=lambda x: x[0])
    return out


def episode_final_mass(scores, ids, row_th):
    masses = defaultdict(float)
    for s, eid in zip(scores, ids):
        masses[eid] += max(0.0, float(s) - row_th)
    return dict(masses)


def metrics_for_threshold(scores, ids, timesteps, episodes, row_th, mass_th):
    groups = by_episode(scores, ids, timesteps, episodes)
    succ = fail = fa = det = det10 = det25 = det50 = 0
    times = []
    for eid, vals in groups.items():
        meta = episodes[eid]
        mass = 0.0
        first_t = None
        first_i = None
        for i, (t, s) in enumerate(vals):
            mass += max(0.0, s - row_th)
            if first_t is None and mass >= mass_th:
                first_t = t
                first_i = i
        if meta.success:
            succ += 1
            if first_t is not None:
                fa += 1
        else:
            fail += 1
            if first_t is not None:
                det += 1
                frac = first_t / max(1, meta.num_steps)
                qfrac = (first_i + 1) / max(1, len(vals))
                times.append(frac)
                if frac <= 0.10:
                    det10 += 1
                if frac <= 0.25:
                    det25 += 1
                if frac <= 0.50:
                    det50 += 1
    return {
        'success_episodes': succ,
        'failure_episodes': fail,
        'success_fa': fa / max(1, succ),
        'failure_det': det / max(1, fail),
        'det_at_10': det10 / max(1, fail),
        'det_at_25': det25 / max(1, fail),
        'det_at_50': det50 / max(1, fail),
        'mean_time': float(np.mean(times)) if times else None,
        'never': 1.0 - det / max(1, fail),
        'false_alarm_count': fa,
        'detected_failure_count': det,
    }


def fmt(x):
    return 'NA' if x is None else f'{100*x:.1f}%'


def main():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'[info] device={device}', flush=True)

    cfg = json.loads((MODEL_DIR / 'config.json').read_text())
    seed = int(cfg.get('seed', 2026060801))
    args = SimpleNamespace(
        width=128, layers=3, heads=4, dropout=0.1, unc_raw_static_dropout=0.0,
        batch_size=1024, seed=seed,
        train_success_limit=1000000, train_failure_limit=1000000,
        val_success_limit=1000000, val_failure_limit=1000000,
        calib_success_limit=1000000, test_success_limit=1000000,
        test_failure_limit=1000000, ood_success_limit=1000000, ood_failure_limit=1000000,
    )
    limits = {
        'train_success': args.train_success_limit,
        'train_failure': args.train_failure_limit,
        'val_success': args.val_success_limit,
        'val_failure': args.val_failure_limit,
        'calib_success': args.calib_success_limit,
        'test_success': args.test_success_limit,
        'test_failure': args.test_failure_limit,
        'ood_success': args.ood_success_limit,
        'ood_failure': args.ood_failure_limit,
    }

    episodes = mod.load_episode_meta(RUN_ROOT, 'libero_goal_object')
    buckets = mod.make_split_assignments(episodes, SPLIT, seed, limits)
    rows_by_bucket = mod.build_rows_for_split(RUN_ROOT, episodes, buckets, history_steps=16, cadence='native', stride=10)

    stats = load_norm(MODEL_DIR / 'normalization.json')
    model = mod.SeqRiskModel(hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1, static_input_dropout=0.0).to(device)
    state = torch.load(MODEL_DIR / 'model.pt', map_location=device)
    model.load_state_dict(state)
    model.eval()

    target_buckets = ['success_calib_seen', 'success_val_seen', 'failure_val_seen']
    scored = {}
    for b in target_buckets:
        print(f'[score] {b} rows={len(rows_by_bucket[b])} eps={len(set(r.episode_id for r in rows_by_bucket[b]))}', flush=True)
        scores, y, ids, ts = mod.score_rows(model, stats, rows_by_bucket[b], VARIANT, args.batch_size, device)
        scored[b] = {'scores': scores, 'ids': ids, 'timesteps': ts}

    calib_scores = scored['success_calib_seen']['scores']
    q95 = float(np.quantile(calib_scores, 0.95))
    q97 = float(np.quantile(calib_scores, 0.97))
    q99 = float(np.quantile(calib_scores, 0.99))
    row_thresholds = {'q95': q95, 'q97': q97, 'q99': q99, 'fixed_0.5': 0.5}

    policies = []
    for row_name, row_th in row_thresholds.items():
        succ_masses = episode_final_mass(scored['success_val_seen']['scores'], scored['success_val_seen']['ids'], row_th)
        fail_masses = episode_final_mass(scored['failure_val_seen']['scores'], scored['failure_val_seen']['ids'], row_th)
        succ_vals = np.asarray(list(succ_masses.values()), dtype=np.float64)
        fail_vals = np.asarray(list(fail_masses.values()), dtype=np.float64)
        candidate_mass = {}
        # Success-only conformal targets: legal, like original but variable alpha.
        for target_fa in [0.20, 0.15, 0.10, 0.075, 0.05, 0.025, 0.01]:
            candidate_mass[f'{row_name}_seen_success_FA{int(target_fa*1000):03d}'] = float(np.quantile(succ_vals, 1.0 - target_fa))
        # Supervised seen validation target: use failures as a plus; choose smallest threshold with target false alarm while maximizing det-minus-fa on seen val.
        grid = np.unique(np.concatenate([
            np.quantile(succ_vals, np.linspace(0, 1, 301)),
            np.quantile(fail_vals, np.linspace(0, 1, 301)),
            np.asarray([0.15, 0.5, 1, 2, 5, 10, 20, 30, 50, 75, 100], dtype=np.float64),
        ]))
        for max_fa in [0.25, 0.20, 0.15, 0.10, 0.05]:
            best = None
            for mt in grid:
                m_s = metrics_for_threshold(scored['success_val_seen']['scores'], scored['success_val_seen']['ids'], scored['success_val_seen']['timesteps'], episodes, row_th, float(mt))
                m_f = metrics_for_threshold(scored['failure_val_seen']['scores'], scored['failure_val_seen']['ids'], scored['failure_val_seen']['timesteps'], episodes, row_th, float(mt))
                fa = m_s['success_fa']
                det = m_f['failure_det']
                mean = m_f['mean_time'] if m_f['mean_time'] is not None else 999.0
                score = (det - fa, det, -mean, -fa)
                if fa <= max_fa and (best is None or score > best[0]):
                    best = (score, float(mt), fa, det, mean)
            if best is not None:
                candidate_mass[f'{row_name}_seen_supervised_FAle{int(max_fa*100):02d}'] = best[1]
        for name, mt in candidate_mass.items():
            mv_s = metrics_for_threshold(scored['success_val_seen']['scores'], scored['success_val_seen']['ids'], scored['success_val_seen']['timesteps'], episodes, row_th, mt)
            mv_f = metrics_for_threshold(scored['failure_val_seen']['scores'], scored['failure_val_seen']['ids'], scored['failure_val_seen']['timesteps'], episodes, row_th, mt)
            policies.append({
                'policy': name,
                'row_threshold_name': row_name,
                'row_threshold': row_th,
                'mass_threshold': mt,
                'seen_success_val': mv_s,
                'seen_failure_val': mv_f,
            })

    # Include original saved point explicitly.
    saved = json.loads((MODEL_DIR / 'thresholds.json').read_text())
    policies.append({
        'policy': 'saved_original_q95_mass_0.15',
        'row_threshold_name': 'saved_q95',
        'row_threshold': float(saved['q95']),
        'mass_threshold': float(saved['conformal_mass']),
        'seen_success_val': metrics_for_threshold(scored['success_val_seen']['scores'], scored['success_val_seen']['ids'], scored['success_val_seen']['timesteps'], episodes, float(saved['q95']), float(saved['conformal_mass'])),
        'seen_failure_val': metrics_for_threshold(scored['failure_val_seen']['scores'], scored['failure_val_seen']['ids'], scored['failure_val_seen']['timesteps'], episodes, float(saved['q95']), float(saved['conformal_mass'])),
    })

    out = {
        'protocol': 'seen-only calibration; OOD test not used here',
        'run_root': str(RUN_ROOT),
        'model_dir': str(MODEL_DIR),
        'split': SPLIT,
        'seed': seed,
        'bucket_counts': {b: {'episodes': len(set(r.episode_id for r in rows_by_bucket[b])), 'rows': len(rows_by_bucket[b])} for b in rows_by_bucket},
        'row_thresholds': row_thresholds,
        'saved_thresholds': saved,
        'policies': policies,
    }
    (OUT_ROOT / 'seen_calibrated_threshold_candidates.json').write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')

    lines = []
    lines.append('# Seen-Only Calibration Candidates for H10 TopK8')
    lines.append('')
    lines.append('No OOD rows are read by this calibration script. Thresholds are chosen from `success_calib_seen`, `success_val_seen`, and optionally `failure_val_seen` only.')
    lines.append('')
    lines.append('| Policy | Row Th | Mass Th | Seen Success FA | Seen Failure Det | Det@25 | Det@50 | Mean Time |')
    lines.append('|---|---:|---:|---:|---:|---:|---:|---:|')
    for p in sorted(policies, key=lambda p: (p['seen_failure_val']['failure_det'] - p['seen_success_val']['success_fa'], p['seen_failure_val']['failure_det']), reverse=True)[:80]:
        ms = p['seen_success_val']; mf = p['seen_failure_val']
        mt = mf['mean_time']
        lines.append(f"| {p['policy']} | {p['row_threshold']:.4f} | {p['mass_threshold']:.4f} | {fmt(ms['success_fa'])} | {fmt(mf['failure_det'])} | {fmt(mf['det_at_25'])} | {fmt(mf['det_at_50'])} | {mt if mt is not None else 'NA'} |")
    (OUT_ROOT / 'SEEN_ONLY_CALIBRATION_CANDIDATES_20260629.md').write_text('\n'.join(lines) + '\n')
    print(f'[done] wrote {OUT_ROOT}', flush=True)

if __name__ == '__main__':
    main()
