#!/usr/bin/env python3
import os, sys, time, json
from pathlib import Path
import numpy as np
import torch

WORKSPACE = Path('/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616')
sys.path.append(str(WORKSPACE / 'src'))

# Let's ensure the compat monkey patches are applied
import run_openvla_ood_online_baseline_vs_risk_20260618 as runner

def run_episode_h1(policy, task_id, reset_seed, episode_idx, episode_global_idx, task_suite, cfg, vla, processor, action_head, proprio_projector, risk_model, risk_stats, args, paths, resize_size, device):
    task = task_suite.get_task(task_id)
    initial_states = task_suite.get_task_init_states(task_id)
    if args.suite == 'libero_goal_object_ood' and getattr(task, 'problem_folder', None) == 'libero_goal_object_ood':
        if hasattr(task, '_replace'):
            task = task._replace(problem_folder='libero_goal_object_ood_temp')
        else:
            import copy
            task = copy.copy(task)
            object.__setattr__(task, 'problem_folder', 'libero_goal_object_ood_temp')
    runner.set_seed_everywhere(reset_seed)
    env, task_description = runner.get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
    obs = None
    success = False; error = ''; terminal_done=False
    risk_trigger_count = 0; num_queries = 0
    risk_scores = []
    executed_horizons = []
    history_buffer = []
    action_queue = runner.deque()
    t = 0; start = runner.time.time()
    try:
        env.reset()
        obs = env.set_init_state(initial_states[episode_idx % len(initial_states)])
        while t < args.max_steps + cfg.num_steps_wait:
            if t < cfg.num_steps_wait:
                obs, reward, done, info = env.step(runner.get_libero_dummy_action(cfg.model_family))
                t += 1
                continue
            step_idx = t - cfg.num_steps_wait
            if len(action_queue) == 0:
                observation, img = runner.prepare_observation(obs, resize_size)
                t0 = runner.time.time()
                actions = runner.get_action(cfg, vla, observation, task_description, processor=processor, action_head=action_head, proprio_projector=proprio_projector, noisy_action_projector=None, use_film=cfg.use_film)
                inference_time = runner.time.time() - t0
                actions_np = np.asarray(actions, dtype=np.float32)
                if actions_np.shape != (8,7): raise RuntimeError(f'action shape {actions_np.shape}, expected (8,7)')
                if not np.isfinite(actions_np).all(): raise RuntimeError('non-finite action chunk')
                proprio = observation['state']
                hist, risk_action, static = runner.make_risk_features(proprio, actions_np, history_buffer)
                
                # FOR BASIC H1, WE FORCE EXEC_H = 1!
                score = None; exec_h = 1
                
                risk_scores.append(score)
                executed_horizons.append(exec_h)
                selected = actions_np[:exec_h]
                action_queue.extend(selected)
                runner.append_jsonl(paths['query'], {
                    'policy': policy, 'suite': args.suite, 'task_id': task_id, 'task_name': task.language,
                    'episode_index_global': episode_global_idx, 'episode_index_for_task': episode_idx, 'reset_seed': reset_seed,
                    'query_index': num_queries, 'env_timestep': step_idx, 'risk_score': score,
                    'risk_threshold': args.risk_threshold if policy == 'openvla_risk_horizon' else None,
                    'risk_triggered': bool(score is not None and score >= args.risk_threshold),
                    'executed_horizon': exec_h, 'native_prediction_horizon': 8,
                    'inference_time': inference_time, 'action_norm_statistics': {
                        'mean': float(np.mean(actions_np)), 'std': float(np.std(actions_np)), 'min': float(np.min(actions_np)),
                        'max': float(np.max(actions_np)), 'l1_norm': float(np.sum(np.abs(actions_np))), 'l2_norm': float(np.sqrt(np.sum(actions_np**2)))
                    }
                })
                num_queries += 1
                history_buffer.append((runner.pad_flat(proprio,8), runner.pad_flat(selected[0],7), np.zeros(7,dtype=np.float32)))
            action = action_queue.popleft()
            action_processed = runner.process_action(action, cfg.model_family)
            obs, reward, done, info = env.step(action_processed.tolist())
            if done:
                success = True; terminal_done=True; break
            t += 1
    except KeyboardInterrupt:
        raise
    except Exception as e:
        error = repr(e)
        runner.traceback.print_exc()
    finally:
        try: env.close()
        except Exception: pass
    num_steps = max(0, t - cfg.num_steps_wait)
    return {
        'policy': policy, 'suite': args.suite, 'task_id': task_id, 'task_name': task.language,
        'episode_index_for_task': episode_idx, 'reset_seed': reset_seed, 'success': bool(success),
        'terminal_done': bool(terminal_done), 'timeout': bool(num_steps >= args.max_steps), 'num_steps': int(num_steps),
        'max_steps': args.max_steps, 'wall_time_seconds': runner.time.time() - start, 'model_id': cfg.pretrained_checkpoint,
        'quantization': '8-bit', 'unnorm_key': cfg.unnorm_key, 'native_prediction_horizon': 8,
        'risk_threshold': args.risk_threshold if policy == 'openvla_risk_horizon' else None,
        'risk_horizon': args.risk_horizon if policy == 'openvla_risk_horizon' else None,
        'risk_trigger_count': int(risk_trigger_count), 'num_queries': int(num_queries),
        'horizon1_query_count': int(sum(1 for h in executed_horizons if h == args.risk_horizon)),
        'horizon8_query_count': int(sum(1 for h in executed_horizons if h == 8)),
        'risk_score_min': None if not [s for s in risk_scores if s is not None] else float(min(s for s in risk_scores if s is not None)),
        'risk_score_max': None if not [s for s in risk_scores if s is not None] else float(max(s for s in risk_scores if s is not None)),
        'error_message': error,
    }

def main():
    output_root = Path("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/focused_ood_task2_task8_basic_h1_seeds_10ep_20260619")
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
    # Actually, we only run openvla_basic (which will use H=1)!
    policies = ['openvla_basic']
    
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
            self.policies = 'openvla_basic'
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
        'risk_horizon_policy': f'H=1 always for openvla_basic',
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
            print(f'[{done_count+1}/{total_runs}] Running policy={policy} task={task_id} seed={seed} (H=1)', flush=True)
            # episode_idx corresponds to (seed - 10) to match the original environment's selected initial state index
            row = run_episode_h1(
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
