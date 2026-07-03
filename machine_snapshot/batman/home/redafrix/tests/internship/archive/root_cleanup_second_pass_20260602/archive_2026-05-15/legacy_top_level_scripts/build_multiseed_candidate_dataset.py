#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from collections import defaultdict
from pathlib import Path
import torch

REDA_WS = Path('/media/rootalkhatib/My Passport/reda_ws')
ROOT = REDA_WS / 'asynchvla_ws/data/processed_stage5'

def add(rows, ctx, typ, act):
    exp = ctx['expert_normalized_action']
    per = torch.linalg.vector_norm(act - exp, dim=-1)
    
    rows.append({
        'context_id': ctx['context_id'],
        'sample_id': ctx['sample_id'],
        'task_name': ctx['task_name'],
        'source_hdf5': ctx['source_hdf5'],
        'language_instruction': ctx['language_instruction'],
        'candidate_type': typ,
        'candidate_action_normalized': act.clone(),
        'target_expert_action_normalized': exp.clone(),
        'true_per_step_l2_error': per.clone(),
        'true_chunk_l2_error': float(per.mean()),
        'pooled_vlm_features': ctx['pooled_vlm_features'].clone(),
        'proprio': ctx['proprio'].clone(),
        'split': ctx['split']
    })

def build(trace_path, out_path, debug=False, seed=123):
    if not trace_path.exists(): 
        print(f"File not found: {trace_path}")
        return None
    data = torch.load(trace_path, map_location='cpu')
    samples = data['samples']
    seeds = data.get('seeds', [0,1,2,3,4])
    g = torch.Generator().manual_seed(seed)
    
    bytask = defaultdict(list)
    for i, s in enumerate(samples): 
        bytask[s['task_name']].append(i)
        
    rows = []
    for i, s in enumerate(samples):
        exp = s['expert_normalized_action']
        add(rows, s, 'expert_action', exp)
        
        # Add all SimVLA seeds
        for seed_idx in seeds:
            seed_act = s[f'simvla_seed{seed_idx}_normalized_action']
            add(rows, s, f'simvla_seed{seed_idx}', seed_act)
            
        add(rows, s, 'perturb_small', exp + 0.10 * torch.randn(exp.shape, generator=g))
        add(rows, s, 'perturb_large', exp + 0.75 * torch.randn(exp.shape, generator=g))
        
        same = [j for j in bytask[s['task_name']] if j != i]
        if same: 
            add(rows, s, 'same_task_far', samples[max(same, key=lambda j: abs(j - i))]['expert_normalized_action'])
            
        other = [j for j, x in enumerate(samples) if x['task_name'] != s['task_name']]
        if other: 
            add(rows, s, 'other_demo_or_other_task', samples[other[(i * 37) % len(other)]]['expert_normalized_action'])
            
    torch.save({
        'schema_version': 'multiseed_candidate_v1',
        'source_trace': str(trace_path),
        'num_contexts': len(samples),
        'num_candidates': len(rows),
        'candidates': rows
    }, out_path)
    return len(samples), len(rows)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--split-name', required=False)
    ap.add_argument('--debug', type=lambda x: str(x).lower() == 'true', default=False)
    args = ap.parse_args()

    if args.debug:
        debug_dir = REDA_WS / 'asynchvla_ws/data/stage5_debug'
        res = build(debug_dir / 'multiseed_trace_debug.pt', debug_dir / 'multiseed_candidate_debug.pt', debug=True)
        print("Debug", res)
    else:
        if not args.split_name:
            print("Missing --split-name")
            return
            
        d = ROOT / args.split_name
        summary = {}
        for part in ['train', 'calib', 'test_id', 'test_ood']:
            res = build(d / f'multiseed_trace_{part}.pt', d / f'multiseed_candidate_{part}.pt')
            if res: 
                summary[part] = {'contexts': res[0], 'candidates': res[1]}
                print(part, res)
        (d / 'multiseed_candidate_build_summary.json').write_text(json.dumps(summary, indent=2))
        print('done', args.split_name)

if __name__ == '__main__': 
    main()
