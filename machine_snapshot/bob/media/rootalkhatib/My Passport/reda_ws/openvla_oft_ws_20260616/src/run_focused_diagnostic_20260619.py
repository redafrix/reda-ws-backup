#!/usr/bin/env python3
import os, sys, time, json
from pathlib import Path
import torch

WORKSPACE = Path('/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616')
sys.path.append(str(WORKSPACE / 'src'))

# Let's ensure the compat monkey patches are applied
import run_openvla_ood_online_baseline_vs_risk_20260618 as runner

def main():
    output_root = Path("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/focused_ood_task2_task8_rescue_seeds_10ep_20260619")
    output_root.mkdir(parents=True, exist_ok=True)
    
    paths = {
        'summary': output_root / 'episode_summaries.jsonl',
        'query': output_root / 'query_records.jsonl',
        'manifest': output_root / 'run_manifest.json'
    }
    
    # Selected (task_id, reset_seed) pairs
    # Prioritizing: task 8, then task 2
    selected_pairs = [
        (8, 11), (8, 18), (8, 19), (8, 22), (8, 25),
        (2, 12), (2, 14), (2, 27), (2, 43), (2, 49)
    ]
    
    # We will run both basic and risk_horizon policies
    policies = ['openvla_basic', 'openvla_risk_horizon']
    
    cfg = runner.MockConfig('libero_goal_object_ood')
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    runner.set_seed_everywhere(0)
    
    print('Loading OpenVLA...', flush=True)
    vla = runner.get_vla(cfg)
    runner.openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    processor = runner.get_processor(cfg)
    
    llm_dim = vla.llm_dim if hasattr(vla, 'llm_dim') else vla.config.text_config.hidden_size
    proprio_projector = runner.get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = runner.get_action_head(cfg, llm_dim=llm_dim)
    
    print('Loading risk model/stats...', flush=True)
    risk_model, risk_stats = runner.load_risk_model(device)
    print('Risk train rows for stats:', risk_stats['train_rows'], flush=True)
    
    task_suite = runner.benchmark.get_benchmark_dict()['libero_goal_object_ood']()
    resize_size = runner.get_image_resize_size(cfg)
    
    # We create an args namespace to mimic the argparser namespace from the original runner
    class ArgsNamespace:
        def __init__(self):
            self.suite = 'libero_goal_object_ood'
            self.output_root = str(output_root)
            self.episodes_per_task = 10
            self.seed_start = 10
            self.max_steps = 800
            self.policies = 'openvla_basic,openvla_risk_horizon'
            self.task_ids = '2,8'
            self.risk_threshold = 0.8049
            self.risk_horizon = 1
            
    args = ArgsNamespace()
    
    manifest = {
        'suite': args.suite,
        'selected_pairs': selected_pairs,
        'policies': policies,
        'max_steps': args.max_steps,
        'risk_model_path': str(runner.RISK_MODEL_PATH),
        'risk_model': 'model_300steps.pt',
        'risk_threshold_source': 'final 1890 validation q95',
        'risk_threshold': args.risk_threshold,
        'risk_horizon_policy': f'H={args.risk_horizon} when risk>=threshold else H=8',
        'ACE_AVAILABLE': 'NO',
        'SIMVLA_UNCERTAINTY_FEATURES_AVAILABLE': 'NO',
        'created_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    paths['manifest'].write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
    
    completed = set()
    if paths['summary'].exists():
        with open(paths['summary'], 'r') as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    completed.add((r['policy'], r['task_id'], r['reset_seed']))
                    
    total_runs = len(policies) * len(selected_pairs)
    done_count = len(completed)
    
    # Loop over policies and selected pairs
    # Note: run policy by policy, and pair by pair
    for policy in policies:
        for idx, (task_id, seed) in enumerate(selected_pairs):
            key = (policy, task_id, seed)
            if key in completed:
                continue
            print(f'[{done_count+1}/{total_runs}] Running policy={policy} task={task_id} seed={seed}', flush=True)
            # episode_idx corresponds to (seed - 10) to match the original environment's selected initial state index
            row = runner.run_episode(
                policy=policy,
                task_id=task_id,
                reset_seed=seed,
                episode_idx=seed - 10,
                episode_global_idx=done_count,
                task_suite=task_suite,
                cfg=cfg,
                vla=vla,
                processor=processor,
                action_head=action_head,
                proprio_projector=proprio_projector,
                risk_model=risk_model,
                risk_stats=risk_stats,
                args=args,
                paths=paths,
                resize_size=resize_size,
                device=device
            )
            row['episode_index_global'] = done_count
            runner.append_jsonl(paths['summary'], row)
            completed.add(key)
            done_count += 1
            
    print('DIAGNOSTIC DONE', flush=True)

if __name__ == '__main__':
    main()
