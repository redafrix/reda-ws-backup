#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

DATASET_ROOT = Path('/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622')
SCORES_PATH = Path('/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626/scores.npz')
CANDIDATES_PATH = Path('/tmp/seen_calibrated_threshold_candidates.json')
OUT_ROOT = Path('/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260629_seen_calibrated_thresholds')
OFFICIAL_FIPER_CSV = Path('/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629/official_fiper_threshold_sweep.csv')


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def load_summaries(path: Path, cap300: bool = False):
    out = {}
    for row in read_jsonl(path):
        eid = str(row.get('episode_id') or row.get('episode_uid'))
        success = bool(row.get('success'))
        steps = int(row.get('steps') or row.get('num_steps') or row.get('num_env_steps') or 0)
        if cap300 and steps >= 300:
            success = False
            steps = 300
        out[eid] = {'success': success, 'steps': steps, 'task_id': int(row.get('task_id', -1))}
    return out


def load_rows(summaries):
    rows = []
    for row in read_jsonl(DATASET_ROOT / 'fiper_receding_samples.jsonl'):
        eid = str(row.get('episode_id') or row.get('episode_uid'))
        if eid not in summaries:
            continue
        t = int(row.get('timestep') or 0)
        # for cap300 callers, remove post-300 evidence
        if summaries[eid]['steps'] == 300 and t >= 300:
            continue
        rows.append({'episode_id': eid, 'task_id': int(row.get('task_id', summaries[eid]['task_id'])), 'timestep': t, 'y': 0 if summaries[eid]['success'] else 1})
    return rows


def group_by_episode(rows, scores):
    by_ep = defaultdict(list)
    for r, s in zip(rows, scores):
        by_ep[r['episode_id']].append((r, float(s)))
    for vals in by_ep.values():
        vals.sort(key=lambda x: x[0]['timestep'])
    return dict(by_ep)


def metric(by_ep, row_th, mass_th):
    succ = fail = fa = det = det10 = det25 = det50 = 0
    times = []
    per_task = defaultdict(Counter)
    for eid, vals in by_ep.items():
        y = max(v[0]['y'] for v in vals)
        task = vals[0][0]['task_id']
        last_t = max(1, vals[-1][0]['timestep'])
        mass = 0.0
        first_idx = None
        first_t = None
        for i, (r, s) in enumerate(vals):
            mass += max(0.0, s - row_th)
            if first_idx is None and mass >= mass_th:
                first_idx = i
                first_t = r['timestep']
        if y:
            fail += 1
            per_task[task]['failure'] += 1
            if first_idx is not None:
                det += 1
                per_task[task]['detected'] += 1
                frac_q = (first_idx + 1) / max(1, len(vals))
                frac_t = first_t / last_t
                times.append(frac_t)
                if frac_q <= 0.10:
                    det10 += 1
                if frac_q <= 0.25:
                    det25 += 1
                if frac_q <= 0.50:
                    det50 += 1
        else:
            succ += 1
            per_task[task]['success'] += 1
            if first_idx is not None:
                fa += 1
                per_task[task]['false_alarm'] += 1
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
        'per_task': {str(k): dict(v) for k, v in sorted(per_task.items())},
    }


def fmt(x):
    return 'NA' if x is None else f'{100*x:.1f}%'


def run_eval(cap300: bool):
    summaries = load_summaries(DATASET_ROOT / 'episode_summaries.jsonl', cap300=cap300)
    rows = load_rows(summaries)
    z = np.load(SCORES_PATH)
    full_scores = z['scores'].astype(np.float64)
    if not cap300:
        scores = full_scores
        if len(scores) != len(rows):
            raise RuntimeError(f'row/score mismatch actual: rows={len(rows)} scores={len(scores)}')
    else:
        # Need filter scores with the same row predicate.
        full_rows = []
        actual_summaries = load_summaries(DATASET_ROOT / 'episode_summaries.jsonl', cap300=False)
        for row in read_jsonl(DATASET_ROOT / 'fiper_receding_samples.jsonl'):
            eid = str(row.get('episode_id') or row.get('episode_uid'))
            if eid in actual_summaries:
                full_rows.append({'episode_id': eid, 'timestep': int(row.get('timestep') or 0)})
        keep = []
        for r in full_rows:
            eid = r['episode_id']
            if eid in summaries and not (summaries[eid]['steps'] == 300 and r['timestep'] >= 300):
                keep.append(True)
            else:
                keep.append(False)
        keep = np.asarray(keep, dtype=bool)
        scores = full_scores[keep]
        if len(scores) != len(rows):
            raise RuntimeError(f'row/score mismatch cap300: rows={len(rows)} scores={len(scores)}')
    by_ep = group_by_episode(rows, scores)
    candidates = json.loads(CANDIDATES_PATH.read_text())['policies']
    out_rows = []
    for p in candidates:
        name = p['policy']
        # skip broken target-fa rows where mass threshold is zero unless it is explicitly original; zero means instant alarm.
        row_th = float(p['row_threshold'])
        mass_th = float(p['mass_threshold'])
        m = metric(by_ep, row_th, mass_th)
        out_rows.append({'policy': name, 'row_threshold': row_th, 'mass_threshold': mass_th, **m})
    return rows, by_ep, sorted(out_rows, key=lambda r: (r['failure_det'] - r['success_fa'], r['failure_det'], -r['success_fa']), reverse=True)


def write_outputs():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    all_results = {}
    for style, cap300 in [('actual_max800', False), ('cap300_forensic', True)]:
        rows, by_ep, results = run_eval(cap300)
        all_results[style] = {'n_rows': len(rows), 'n_episodes': len(by_ep), 'results': results}
        with (OUT_ROOT / f'{style}_seen_calibrated_ood_metrics.csv').open('w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['Policy','Row_Threshold','Mass_Threshold','Success_FA','Failure_Det','Det@10','Det@25','Det@50','Mean_Time','Never','False_Alarms','Detected_Failures'])
            for r in results:
                w.writerow([r['policy'], r['row_threshold'], r['mass_threshold'], r['success_fa'], r['failure_det'], r['det_at_10'], r['det_at_25'], r['det_at_50'], r['mean_time'], r['never'], r['false_alarm_count'], r['detected_failure_count']])
    (OUT_ROOT / 'seen_calibrated_ood_results.json').write_text(json.dumps(all_results, indent=2, sort_keys=True) + '\n')

    report = []
    report.append('# H10 TopK8 Seen-Calibrated Thresholds Applied to Official OOD180')
    report.append('')
    report.append('Protocol: train/model unchanged; row thresholds and mass thresholds selected only from seen `libero_goal_object` buckets on Bob. The official `libero_goal_object_ood` 180 episode dataset is used only once as final test.')
    report.append('')
    for style in ['actual_max800', 'cap300_forensic']:
        results = all_results[style]['results']
        report.append(f'## {style}')
        report.append('')
        report.append(f"- Rows: `{all_results[style]['n_rows']}`")
        report.append(f"- Episodes: `{all_results[style]['n_episodes']}`")
        report.append('')
        report.append('| Policy | Row Th | Mass Th | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |')
        report.append('|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
        keep = []
        names = {'saved_original_q95_mass_0.15','q95_seen_success_FA050','q95_seen_success_FA025','q95_seen_supervised_FAle25','q95_seen_supervised_FAle10','q97_seen_supervised_FAle25','q97_seen_success_FA025','q99_seen_supervised_FAle25','q99_seen_success_FA010'}
        for r in results:
            if r['policy'] in names:
                keep.append(r)
        # add best under several FA constraints
        for maxfa in [0.50, 0.25, 0.10, 0.05, 0.03]:
            eligible = [r for r in results if r['success_fa'] <= maxfa and r['mass_threshold'] > 0]
            if eligible:
                best = max(eligible, key=lambda r: (r['failure_det'] - r['success_fa'], r['failure_det'], -r['success_fa']))
                if best not in keep:
                    keep.append(best)
        seen = set()
        for r in keep:
            key = r['policy']
            if key in seen:
                continue
            seen.add(key)
            mt = 'NA' if r['mean_time'] is None else f"{r['mean_time']:.3f}"
            report.append(f"| {r['policy']} | {r['row_threshold']:.4f} | {r['mass_threshold']:.4f} | {fmt(r['success_fa'])} | {fmt(r['failure_det'])} | {fmt(r['det_at_10'])} | {fmt(r['det_at_25'])} | {fmt(r['det_at_50'])} | {mt} | {fmt(r['never'])} |")
        report.append('')
    report.append('## Key Interpretation')
    report.append('')
    report.append('- `saved_original_q95_mass_0.15` is the old seen-calibrated online point. It over-alarms on OOD.')
    report.append('- `*_seen_success_*` thresholds use only success episodes for calibration, closest to conformal/FIPER style.')
    report.append('- `*_seen_supervised_*` thresholds use seen validation successes plus seen validation failures. This is legitimate for our supervised risk model and is not available to original FIPER, but must be labeled as supervised calibration.')
    report.append('- No threshold in this report is selected from OOD performance.')
    (OUT_ROOT / 'H10_TOPK8_SEEN_CALIBRATED_ON_OFFICIAL_OOD180_20260629.md').write_text('\n'.join(report) + '\n')
    print(OUT_ROOT / 'H10_TOPK8_SEEN_CALIBRATED_ON_OFFICIAL_OOD180_20260629.md')

if __name__ == '__main__':
    write_outputs()
