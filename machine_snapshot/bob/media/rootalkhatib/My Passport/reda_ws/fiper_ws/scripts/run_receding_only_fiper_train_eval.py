import argparse
import shutil
import json
import os
import random
import time
import csv
from pathlib import Path
from typing import Dict, List, Tuple, Any

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

# Constants
INPUT_DIM = 70  # 10 steps * 7 dims
HIDDEN_DIM = 256
OUTPUT_DIM = 128

class RNDNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, x):
        return self.net(x)

class FIPERModel(nn.Module):
    def __init__(self, input_dim=INPUT_DIM, hidden_dim=HIDDEN_DIM, output_dim=OUTPUT_DIM):
        super().__init__()
        self.predictor = RNDNetwork(input_dim, hidden_dim, output_dim)
        self.prior = RNDNetwork(input_dim, hidden_dim, output_dim)
        for p in self.prior.parameters():
            p.requires_grad = False
            
    def get_rnd_score(self, x):
        with torch.no_grad():
            p_out = self.predictor(x)
            prior_out = self.prior(x)
            score = torch.norm(p_out - prior_out, dim=-1)**2
        return score

def load_jsonl_rows_efficient(ref_path: Path, max_rows: int = None, base_dir: Path = Path('.'), need_ace: bool = True) -> List[dict]:
    rows = []
    if not ref_path.exists():
        print(f'Warning: {ref_path} not found.')
        return rows
    
    sources = {}
    with ref_path.open('r') as f:
        for line in f:
            ref = json.loads(line)
            src = ref['source_jsonl']
            if src not in sources:
                sources[src] = []
            sources[src].append(ref)
            if max_rows and len(rows) + sum(len(v) for v in sources.values()) >= max_rows:
                break
    
    total_loaded = 0
    for src, refs in sources.items():
        src_path = base_dir / src
        if not src_path.exists():
            continue
        
        print(f'Reading {len(refs)} rows from {src}...', flush=True)
        refs.sort(key=lambda x: x['line_no'])
        needed_lines = {r['line_no']: r for r in refs}
        
        with src_path.open('r') as f:
            for line_no, line in enumerate(f, start=1):
                if line_no in needed_lines:
                    row_data = json.loads(line)
                    res = {
                        'main_candidate_action_chunk_normalized': row_data['main_candidate_action_chunk_normalized'],
                        'episode_outcome': row_data['episode_outcome'],
                        'episode_key': row_data['episode_id'],
                        'timestep': row_data['timestep'],
                        'suite': row_data['suite'],
                        'task_id': row_data['task_id']
                    }
                    if need_ace:
                        res['ace_candidate_chunks_normalized'] = row_data['ace_candidate_chunks_normalized']
                    
                    # The ref metadata is authoritative, but the action/ACE chunks above must
                    # come from the same 1-based JSONL line referenced by the manifest.
                    res.update(needed_lines[line_no])
                    rows.append(res)
                    total_loaded += 1
                    if max_rows and total_loaded >= max_rows:
                        return rows
    return rows

def compute_ace_metrics(ace_chunks_normalized: np.ndarray) -> Dict[str, float]:
    n_seeds = ace_chunks_normalized.shape[0]
    flat = ace_chunks_normalized.reshape(n_seeds, -1)
    
    # Gaussian Entropy
    cov = np.cov(flat, rowvar=False)
    eps = 1e-6
    sign, logdet = np.linalg.slogdet(cov + eps * np.eye(flat.shape[1]))
    entropy = 0.5 * (flat.shape[1] * (1.0 + np.log(2 * np.pi)) + logdet)
    
    # Mean Pairwise Distance
    diffs = flat[:, None, :] - flat[None, :, :]
    dists = np.sqrt(np.sum(diffs**2, axis=-1))
    mean_pairwise_dist = np.sum(dists) / (n_seeds * (n_seeds - 1)) if n_seeds > 1 else 0.0
    
    # Component-wise Std
    per_step_std = np.mean(np.std(ace_chunks_normalized, axis=0))
    translation_std = np.mean(np.std(ace_chunks_normalized[:, :, :3], axis=0))
    rotation_std = np.mean(np.std(ace_chunks_normalized[:, :, 3:6], axis=0))
    gripper_std = np.mean(np.std(ace_chunks_normalized[:, :, 6:], axis=0))
    
    return {
        'ace_gaussian_entropy': float(entropy),
        'ace_mean_pairwise_dist': float(mean_pairwise_dist),
        'ace_per_step_std': float(per_step_std),
        'ace_translation_std': float(translation_std),
        'ace_rotation_std': float(rotation_std),
        'ace_gripper_std': float(gripper_std)
    }

def process_data(rows: List[dict], stats=None, compute_ace: bool = True):
    if not rows:
        raise ValueError('process_data received zero rows')

    actions = []
    ace_metrics_list = []
    outcomes = []
    meta = []
    
    for row in rows:
        chunk = np.array(row['main_candidate_action_chunk_normalized']).flatten()
        actions.append(chunk)
        
        if compute_ace:
            ace_chunks = np.array(row['ace_candidate_chunks_normalized'])
            ace_metrics_list.append(compute_ace_metrics(ace_chunks))
        
        outcomes.append(row['episode_outcome'])
        meta.append({
            'episode_key': row['episode_key'],
            'timestep': row['timestep'],
            'suite': row['suite'],
            'task_id': row['task_id']
        })
        
    actions = np.array(actions)
    if stats is None:
        mean = np.mean(actions, axis=0)
        std = np.std(actions, axis=0)
        stats = {'mean': mean, 'std': std}
    
    eps = 1e-4
    std_adj = np.where(stats['std'] < eps, 1.0, stats['std'])
    norm_actions = (actions - stats['mean']) / std_adj
    norm_actions = np.clip(norm_actions, -10, 10)
    norm_actions[:, stats['std'] < eps] = 0.0
    
    return torch.tensor(norm_actions, dtype=torch.float32), ace_metrics_list, outcomes, meta, stats

class ActionDataset(Dataset):
    def __init__(self, actions):
        self.actions = actions
    def __len__(self):
        return len(self.actions)
    def __getitem__(self, idx):
        return self.actions[idx]

def run_eval(model, device, split_name, rows, stats, rnd_thresholds, ace_thresholds):
    if not rows:
        return None
    
    actions, ace_metrics, outcomes, meta, _ = process_data(rows, stats, compute_ace=True)
    actions = actions.to(device)
    
    model.eval()
    with torch.no_grad():
        rnd_scores = model.get_rnd_score(actions).cpu().numpy()
    
    results = []
    for i in range(len(rows)):
        res = {
            'split': split_name,
            'rnd_score': float(rnd_scores[i]),
            'outcome': outcomes[i]
        }
        res.update(ace_metrics[i])
        res.update(meta[i])
        
        for q, thresh in rnd_thresholds.items():
            res[f'rnd_alarm_{q}'] = bool(rnd_scores[i] > thresh)
        
        primary_ace = res['ace_gaussian_entropy']
        for q, thresh in ace_thresholds.items():
            res[f'ace_alarm_{q}'] = bool(primary_ace > thresh)
            
        r95 = res.get('rnd_alarm_q95', False)
        a95 = res.get('ace_alarm_q95', False)
        res['fiper_alarm_or_q95'] = r95 or a95
        res['fiper_alarm_and_q95'] = r95 and a95
        
        if not r95 and not a95: res['quadrant'] = 'Normal'
        elif r95 and not a95: res['quadrant'] = 'OOD_Confident'
        elif not r95 and a95: res['quadrant'] = 'Action_Uncertain'
        else: res['quadrant'] = 'High_Risk'
        
        results.append(res)
    
    return results

def summarize_episodes_detailed(results, rnd_q='q95', ace_q='q95'):
    episodes = {}
    for r in results:
        ek = r['episode_key']
        if ek not in episodes: episodes[ek] = []
        episodes[ek].append(r)
    
    summary = []
    alarm_types = ['rnd_alarm_' + rnd_q, 'ace_alarm_' + ace_q, 'fiper_alarm_or_q95', 'fiper_alarm_and_q95']
    
    for ek, steps in episodes.items():
        steps.sort(key=lambda x: x['timestep'])
        n_steps = len(steps)
        row = {'episode_key': ek, 'outcome': steps[0]['outcome'], 'num_steps': n_steps}
        
        for atype in alarm_types:
            first_idx = -1
            for i, s in enumerate(steps):
                if s.get(atype, False):
                    first_idx = i
                    break
            
            norm_time = first_idx / n_steps if first_idx != -1 else 1.0
            
            prefix = atype.replace('fiper_alarm_', '').replace('_alarm_q95', '').replace('_alarm_', '')
            if 'rnd' in prefix: prefix = 'rnd'
            elif 'ace' in prefix: prefix = 'ace'
            elif 'or' in prefix: prefix = 'or'
            elif 'and' in prefix: prefix = 'and'
            
            row[f'{prefix}_first_idx'] = first_idx
            row[f'{prefix}_norm_time'] = norm_time
            row[f'{prefix}_detected_10'] = first_idx != -1 and norm_time <= 0.1
            row[f'{prefix}_detected_25'] = first_idx != -1 and norm_time <= 0.25
            row[f'{prefix}_detected_50'] = first_idx != -1 and norm_time <= 0.5
            row[f'{prefix}_never'] = first_idx == -1
            
        summary.append(row)
    return summary

def generate_corrupted_rows(rows, mode):
    corrupted = []
    for r in rows:
        rc = r.copy()
        chunk = np.array(rc['main_candidate_action_chunk_normalized']).reshape(10, 7)
        if mode == 'zero':
            chunk = np.zeros_like(chunk)
        elif mode == 'random_uniform':
            chunk = np.random.uniform(-1, 1, (10, 7))
        elif mode == 'shuffled_timestep_order':
            indices = np.arange(10)
            np.random.shuffle(indices)
            chunk = chunk[indices]
        elif mode == 'reversed_timestep_order':
            chunk = chunk[::-1]
        elif mode == 'scaled_x2_clipped':
            chunk = np.clip(chunk * 2.0, -1, 1)
        elif mode == 'gripper_flipped':
            chunk[:, 6:] = 1.0 - chunk[:, 6:]
        elif mode == 'repeated_first_action':
            chunk[:] = chunk[0]
        elif mode == 'gaussian_noise_low':
            chunk += np.random.normal(0, 0.01, (10, 7))
        elif mode == 'gaussian_noise_medium':
            chunk += np.random.normal(0, 0.1, (10, 7))
        elif mode == 'gaussian_noise_high':
            chunk += np.random.normal(0, 0.5, (10, 7))
            
        rc['main_candidate_action_chunk_normalized'] = chunk.tolist()
        corrupted.append(rc)
    return corrupted

def is_temporal_subset_split(split_name: str) -> bool:
    return (
        split_name.endswith('_early')
        or split_name.endswith('_mid')
        or split_name.endswith('_late')
        or split_name.endswith('_near_end')
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment-dir', type=str, required=True)
    parser.add_argument('--device', type=str, default='cuda')
    parser.add_argument('--epochs', type=int, default=20)
    parser.add_argument('--batch-size', type=int, default=256)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--max-train-rows', type=int, default=None)
    parser.add_argument('--max-calib-rows', type=int, default=None)
    parser.add_argument('--max-eval-rows', type=int, default=None)
    parser.add_argument('--eval-only', action='store_true')
    parser.add_argument('--refs-dir', type=str, default='experiments/prepared_20260526/00_global_main/datasets/refs/')
    parser.add_argument('--train-split', type=str, default='success_train')
    parser.add_argument('--calib-split', type=str, default='success_calib')
    parser.add_argument('--success-eval-splits', nargs='+', default=['success_test_id'])
    parser.add_argument('--failure-eval-splits', nargs='+', default=['failure_eval_all', 'failure_eval_early', 'failure_eval_mid', 'failure_eval_late', 'failure_eval_near_end'])
    parser.add_argument('--episode-summary-splits', nargs='+', default=None)
    parser.add_argument('--report-name', type=str, default='FIPER_RECEDING_ONLY_GLOBAL_V1_REPORT.md')
    args = parser.parse_args()
    
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    
    base_dir = Path(args.experiment_dir)
    for d in ['models', 'thresholds', 'scores', 'evals', 'reports', 'logs', 'code']:
        (base_dir / d).mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(Path(__file__), base_dir / 'code' / Path(__file__).name)
    except Exception as exc:
        print(f'Warning: could not snapshot runner script: {exc}', flush=True)
    
    ref_base = Path(args.refs_dir)
    
    device = torch.device(args.device)
    model = FIPERModel().to(device)
    
    if args.eval_only:
        print('Evaluation only mode.', flush=True)
        model.predictor.load_state_dict(torch.load(base_dir / 'models/rnd_predictor.pt', map_location=device))
        model.prior.load_state_dict(torch.load(base_dir / 'models/rnd_target.pt', map_location=device))
        with (base_dir / 'models/rnd_normalization.json').open('r') as f:
            norm_stats = json.load(f)
            stats = {'mean': np.array(norm_stats['mean']), 'std': np.array(norm_stats['std'])}
        with (base_dir / 'thresholds/rnd_thresholds.json').open('r') as f:
            rnd_thresholds = json.load(f)
        with (base_dir / 'thresholds/ace_thresholds.json').open('r') as f:
            ace_thresholds = json.load(f)
    else:
        print('Loading data...', flush=True)
        train_rows = load_jsonl_rows_efficient(ref_base / f'{args.train_split}.rows.jsonl', args.max_train_rows, need_ace=False)
        calib_rows = load_jsonl_rows_efficient(ref_base / f'{args.calib_split}.rows.jsonl', args.max_calib_rows, need_ace=True)
        if not train_rows:
            raise RuntimeError(f'No training rows loaded from split {args.train_split}')
        if not calib_rows:
            raise RuntimeError(f'No calibration rows loaded from split {args.calib_split}')
        
        print('Processing training data...', flush=True)
        train_actions, _, _, _, stats = process_data(train_rows, compute_ace=False)
        optimizer = optim.Adam(model.predictor.parameters(), lr=1e-3)
        criterion = nn.MSELoss()
        
        train_loader = DataLoader(ActionDataset(train_actions), batch_size=args.batch_size, shuffle=True)
        
        print('Training RND...', flush=True)
        model.train()
        history = []
        for epoch in range(args.epochs):
            epoch_loss = 0
            for batch in train_loader:
                batch = batch.to(device)
                optimizer.zero_grad()
                p_out = model.predictor(batch)
                with torch.no_grad(): prior_out = model.prior(batch)
                loss = criterion(p_out, prior_out)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            history.append({'epoch': epoch, 'loss': epoch_loss / len(train_loader)})
            print(f'Epoch {epoch}, Loss: {epoch_loss/len(train_loader):.6f}', flush=True)
            
        torch.save(model.predictor.state_dict(), base_dir / 'models/rnd_predictor.pt')
        torch.save(model.prior.state_dict(), base_dir / 'models/rnd_target.pt')
        with (base_dir / 'models/rnd_normalization.json').open('w') as f:
            json.dump({'mean': stats['mean'].tolist(), 'std': stats['std'].tolist()}, f)
        with (base_dir / 'models/rnd_training_summary.json').open('w') as f:
            json.dump(history, f)
            
        print('Calibrating...', flush=True)
        calib_actions, calib_ace_metrics, _, _, _ = process_data(calib_rows, stats, compute_ace=True)
        model.eval()
        with torch.no_grad():
            calib_rnd_scores = model.get_rnd_score(calib_actions.to(device)).cpu().numpy()
        
        rnd_thresholds = {q: float(np.quantile(calib_rnd_scores, float(q.replace('q',''))/100.0)) for q in ['q90', 'q95', 'q99']}
        calib_entropies = [m['ace_gaussian_entropy'] for m in calib_ace_metrics]
        ace_thresholds = {q: float(np.quantile(calib_entropies, float(q.replace('q',''))/100.0)) for q in ['q90', 'q95', 'q99']}
        
        with (base_dir / 'thresholds/rnd_thresholds.json').open('w') as f: json.dump(rnd_thresholds, f)
        with (base_dir / 'thresholds/ace_thresholds.json').open('w') as f: json.dump(ace_thresholds, f)
    
    eval_splits = args.success_eval_splits + args.failure_eval_splits
    if args.episode_summary_splits is None:
        episode_summary_splits = {s for s in eval_splits if not is_temporal_subset_split(s)}
    else:
        episode_summary_splits = set(args.episode_summary_splits)
    all_summary_rows = []
    alarm_rates = {}
    temporal_curves = []
    
    for f in ['rnd_scores_by_split.jsonl', 'ace_scores_by_split.jsonl', 'fiper_scores_by_split.jsonl']:
        (base_dir / 'scores' / f).unlink(missing_ok=True)

    for split in eval_splits:
        print(f'Evaluating {split}...', flush=True)
        rows = load_jsonl_rows_efficient(ref_base / f'{split}.rows.jsonl', args.max_eval_rows, need_ace=True)
        if not rows: continue
        results = run_eval(model, device, split, rows, stats, rnd_thresholds, ace_thresholds)
        
        with (base_dir / 'scores/rnd_scores_by_split.jsonl').open('a') as f:
            for r in results: f.write(json.dumps({'split': split, 'rnd_score': r['rnd_score'], 'timestep': r['timestep'], 'ek': r['episode_key']}) + '\n')
        with (base_dir / 'scores/ace_scores_by_split.jsonl').open('a') as f:
            for r in results: f.write(json.dumps({'split': split, 'ace_entropy': r['ace_gaussian_entropy'], 'timestep': r['timestep'], 'ek': r['episode_key']}) + '\n')
        with (base_dir / 'scores/fiper_scores_by_split.jsonl').open('a') as f:
            for r in results:
                f.write(json.dumps({
                    'split': split,
                    'episode_key': r['episode_key'],
                    'timestep': r['timestep'],
                    'or': r['fiper_alarm_or_q95'],
                    'and': r['fiper_alarm_and_q95'],
                    'quadrant': r['quadrant']
                }) + '\n')
            
        for r in results:
            temporal_curves.append({
                'split': split, 'timestep': r['timestep'], 'rnd_score': r['rnd_score'], 
                'ace_entropy': r['ace_gaussian_entropy'], 'or_alarm': r['fiper_alarm_or_q95']
            })
            
        sum_rows = summarize_episodes_detailed(results)
        if split in episode_summary_splits:
            all_summary_rows.extend(sum_rows)
        
        rates = {}
        for k in ['rnd_alarm_q95', 'ace_alarm_q95', 'fiper_alarm_or_q95', 'fiper_alarm_and_q95']:
            rates[k] = np.mean([r[k] for r in results])
        alarm_rates[split] = rates

    with (base_dir / 'evals/alarm_rates_by_split.json').open('w') as f: json.dump(alarm_rates, f, indent=2)
    with (base_dir / 'evals/failure_temporal_alarm_curves.csv').open('w', newline='') as f:
        if temporal_curves:
            writer = csv.DictWriter(f, fieldnames=temporal_curves[0].keys())
            writer.writeheader()
            writer.writerows(temporal_curves)
    
    with (base_dir / 'evals/failure_early_detection_by_episode.csv').open('w', newline='') as f:
        if all_summary_rows:
            writer = csv.DictWriter(f, fieldnames=all_summary_rows[0].keys())
            writer.writeheader()
            writer.writerows(all_summary_rows)
        
    det_stats = {}
    for prefix in ['rnd', 'ace', 'or', 'and']:
        fail_episodes = [r for r in all_summary_rows if r['outcome'] != 'success']
        if not fail_episodes: continue
        times = [r[f'{prefix}_norm_time'] for r in fail_episodes if r[f'{prefix}_first_idx'] != -1]
        det_stats[prefix] = {
            'n_failure_episodes': len(fail_episodes),
            'mean_norm_time': float(np.mean(times)) if times else 1.0,
            'median_norm_time': float(np.median(times)) if times else 1.0,
            'det_10': float(np.mean([r[f'{prefix}_detected_10'] for r in fail_episodes])),
            'det_25': float(np.mean([r[f'{prefix}_detected_25'] for r in fail_episodes])),
            'det_50': float(np.mean([r[f'{prefix}_detected_50'] for r in fail_episodes])),
            'never': float(np.mean([r[f'{prefix}_never'] for r in fail_episodes]))
        }
    with (base_dir / 'evals/failure_early_detection_summary.json').open('w') as f: json.dump(det_stats, f, indent=2)

    print('Sanity checks...', flush=True)
    sanity_results = {}
    test_id_rows = load_jsonl_rows_efficient(ref_base / f'{args.success_eval_splits[0]}.rows.jsonl', args.max_eval_rows, need_ace=False)
    modes = ['zero', 'random_uniform', 'shuffled_timestep_order', 'reversed_timestep_order', 'scaled_x2_clipped', 'gripper_flipped', 'repeated_first_action', 'gaussian_noise_low', 'gaussian_noise_medium', 'gaussian_noise_high']
    if test_id_rows:
        for mode in modes:
            c_rows = generate_corrupted_rows(test_id_rows, mode)
            res = run_eval_no_ace(model, device, f'corrupted_{mode}', c_rows, stats, rnd_thresholds)
            rate = np.mean([r['rnd_alarm_q95'] for r in res])
            sanity_results[mode] = float(rate)
    else:
        print(f'Warning: no rows loaded for sanity split {args.success_eval_splits[0]}', flush=True)
    with (base_dir / 'evals/corrupted_action_eval.json').open('w') as f: json.dump(sanity_results, f, indent=2)
    with (base_dir / 'evals/corrupted_action_eval.csv').open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['mode', 'rnd_alarm_q95_rate'])
        for k, v in sanity_results.items(): writer.writerow([k, v])

    print('Reporting...', flush=True)
    generate_markdown_report(base_dir, det_stats, sanity_results, alarm_rates, rnd_thresholds, ace_thresholds, eval_splits, args.report_name)
    print('Done.', flush=True)

def run_eval_no_ace(model, device, split_name, rows, stats, rnd_thresholds):
    actions, _, outcomes, meta, _ = process_data(rows, stats, compute_ace=False)
    actions = actions.to(device)
    model.eval()
    with torch.no_grad():
        rnd_scores = model.get_rnd_score(actions).cpu().numpy()
    results = []
    for i in range(len(rows)):
        res = {'split': split_name, 'rnd_score': float(rnd_scores[i]), 'outcome': outcomes[i]}
        res.update(meta[i])
        for q, thresh in rnd_thresholds.items():
            res[f'rnd_alarm_{q}'] = bool(rnd_scores[i] > thresh)
        results.append(res)
    return results

def generate_markdown_report(base_dir, det_stats, sanity_results, alarm_rates, rnd_thresholds, ace_thresholds, eval_splits, report_name):
    with (base_dir / f'reports/{report_name}').open('w') as f:
        f.write('# FIPER Training Report\n\n')
        f.write('## 1. Thresholds\n')
        f.write(f'RND q95: {rnd_thresholds["q95"]:.6f}\n')
        f.write(f'ACE q95: {ace_thresholds["q95"]:.6f}\n\n')
        f.write('## 2. Success False Alarm Rates (q95)\n')
        success_splits = [s for s in eval_splits if s.startswith('success')]
        primary_success_split = success_splits[0] if success_splits else None
        s_rates = alarm_rates.get(primary_success_split, {}) if primary_success_split else {}
        for split in success_splits:
            r = alarm_rates.get(split, {})
            f.write(f'- {split} RND: {r.get("rnd_alarm_q95", 0):.4f}\n')
            f.write(f'- {split} ACE: {r.get("ace_alarm_q95", 0):.4f}\n')
            f.write(f'- {split} OR:  {r.get("fiper_alarm_or_q95", 0):.4f}\n')
            f.write(f'- {split} AND: {r.get("fiper_alarm_and_q95", 0):.4f}\n')
        f.write('\n')
        f.write('## 3. Failure Detection Summary (q95)\n')
        f.write('| Split | RND | ACE | OR | AND |\n|---|---|---|---|---|\n')
        for split in eval_splits:
            if split.startswith('success'): continue
            r = alarm_rates.get(split, {})
            f.write(f'| {split} | {r.get("rnd_alarm_q95", 0):.4f} | {r.get("ace_alarm_q95", 0):.4f} | {r.get("fiper_alarm_or_q95", 0):.4f} | {r.get("fiper_alarm_and_q95", 0):.4f} |\n')
        f.write('\n## 4. Early Detection Performance (q95)\n')
        f.write('| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |\n|---|---|---|---|---|---|\n')
        for prefix in ['rnd', 'ace', 'or', 'and']:
            d = det_stats.get(prefix, {})
            f.write(f'| {prefix.upper()} | {d.get("mean_norm_time", 1):.4f} | {d.get("det_10", 0):.4f} | {d.get("det_25", 0):.4f} | {d.get("det_50", 0):.4f} | {d.get("never", 1):.4f} |\n')
        f.write('\n## 5. Corrupted-Action Sanity (RND q95)\n')
        for mode, rate in sanity_results.items():
            f.write(f'- {mode}: {rate:.4f}\n')
        f.write('\n## 6. Audit Verdicts\n')
        or_stats = det_stats.get('or', {})
        rnd_stats = det_stats.get('rnd', {})
        ace_stats = det_stats.get('ace', {})
        f.write(f'EARLY_FAILURE_DETECTION_USEFUL = {"YES" if or_stats.get("mean_norm_time", 1.0) < 0.5 and or_stats.get("never", 1.0) < 0.25 else "NO"}\n')
        f.write(f'RND_ADDS_VALUE_BEYOND_ACE = {"YES" if or_stats.get("never", 1.0) < ace_stats.get("never", 1.0) else "NO"}\n')
        f.write(f'ACE_ADDS_VALUE_BEYOND_RND = {"YES" if or_stats.get("never", 1.0) < rnd_stats.get("never", 1.0) else "NO"}\n')
        f.write(f'ACE_IS_PRIMARY_EARLY_SIGNAL = {"YES" if ace_stats.get("det_25", 0) > rnd_stats.get("det_25", 0) else "NO"}\n')
        f.write(f'SUCCESS_ROW_FALSE_ALARM_UNDER_15PCT = {"YES" if s_rates.get("fiper_alarm_or_q95", 1.0) < 0.15 else "NO"}\n')
        f.write('CORRUPTED_ACTION_SANITY_REVIEW_REQUIRED = YES\n')
        f.write('READY_FOR_NEXT_EXPERIMENT_REVIEW_REQUIRED = YES\n')

if __name__ == '__main__':
    main()
