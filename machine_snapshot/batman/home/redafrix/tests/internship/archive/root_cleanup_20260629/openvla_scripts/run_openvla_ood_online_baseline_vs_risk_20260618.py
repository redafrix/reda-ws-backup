#!/usr/bin/env python3
import os, sys, time, json, argparse, hashlib, traceback
from pathlib import Path
from collections import deque, defaultdict
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

WORKSPACE = Path('/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616')
SRC_DIR = WORKSPACE / 'src'
OPENVLA_DIR = SRC_DIR / 'openvla-oft'
LIBERO_PRO = Path('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO')
SIMVLA_SITE = Path('/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages')
FINAL_DATASET = WORKSPACE / 'datasets/openvla_goal_object_final_1890_complete_rounds_20260618'
RISK_EXP = WORKSPACE / 'offline_risk_experiments/openvla_final1890_risk_20260618'
RISK_MODEL_PATH = RISK_EXP / 'models/model_300steps.pt'
SPLIT_DIR = RISK_EXP / 'splits'

for p in [SRC_DIR, OPENVLA_DIR, LIBERO_PRO, SIMVLA_SITE, Path('/usr/lib/python3/dist-packages')]:
    sys.path.append(str(p))

os.environ['LIBERO_CONFIG_PATH'] = '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob'
os.environ['HF_HOME'] = str(WORKSPACE / 'hf_cache')
os.environ['TRANSFORMERS_CACHE'] = str(WORKSPACE / 'hf_cache')
os.environ['HF_HUB_CACHE'] = str(WORKSPACE / 'hf_cache')
os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'
os.environ['MUJOCO_GL'] = 'egl'
os.environ['PYOPENGL_PLATFORM'] = 'egl'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
os.environ['USE_TF'] = '0'
os.environ['USE_FLAX'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

from experiments.robot.openvla_utils import get_vla, get_processor, get_proprio_projector, get_action_head, resize_image_for_policy
from experiments.robot.libero.libero_utils import get_libero_env, get_libero_image, get_libero_wrist_image, quat2axisangle, get_libero_dummy_action
from experiments.robot.robot_utils import get_action, get_image_resize_size, normalize_gripper_action, invert_gripper_action, set_seed_everywhere
from libero.libero import benchmark


def patch_libero_tabletop_manipulation():
    from libero.libero.envs.bddl_base_domain import TASK_MAPPING
    import libero.libero.envs.problems.libero_tabletop_manipulation
    from libero.libero.envs.objects import SiteObject, TargetZone
    from robosuite.utils.mjcf_utils import new_site, string_to_array

    def patched_load_sites_in_arena(self, mujoco_arena):
        object_sites_dict = {}
        region_dict = self.parsed_problem['regions']
        for object_region_name in list(region_dict.keys()):
            if 'main_table' in object_region_name:
                ranges = region_dict[object_region_name]['ranges'][0]
                zone_size = ((ranges[2] - ranges[0]) / 2, (ranges[3] - ranges[1]) / 2)
                zone_centroid_xy = ((ranges[2] + ranges[0]) / 2, (ranges[3] + ranges[1]) / 2)
                target_zone = TargetZone(name=object_region_name, rgba=region_dict[object_region_name]['rgba'], zone_size=zone_size, zone_centroid_xy=zone_centroid_xy)
                object_sites_dict[object_region_name] = target_zone
                mujoco_arena.table_body.append(new_site(name=target_zone.name, pos=target_zone.pos, quat=target_zone.quat, rgba=target_zone.rgba, size=target_zone.size, type='box'))
                continue

            for query_dict in [self.objects_dict, self.fixtures_dict]:
                for _name, body in query_dict.items():
                    try:
                        if 'worldbody' not in list(body.__dict__.keys()):
                            continue
                    except Exception:
                        continue
                    top_body = body.worldbody.find('body')
                    if top_body is None:
                        continue
                    all_bodies = [top_body] + top_body.findall('.//body')
                    exact_site = None
                    matching_clean_site = None
                    matching_clean_part = None
                    target_name_clean = object_region_name.replace('_site', '').replace('_region', '')
                    for part in all_bodies:
                        for site in part.findall('./site'):
                            site_name = site.get('name')
                            if site_name == object_region_name:
                                exact_site = site
                                matching_clean_part = part
                                break
                            site_name_clean = site_name.replace('_site', '').replace('_region', '')
                            if site_name_clean == target_name_clean and site_name_clean != '':
                                matching_clean_site = site
                                matching_clean_part = part
                        if exact_site is not None:
                            break
                    if exact_site is None and matching_clean_site is not None:
                        already = None
                        if body._obj is not None:
                            for site in body._obj.findall('.//site'):
                                if site.get('name') == object_region_name:
                                    already = site
                                    break
                        if already is None:
                            print(f"[Monkey Patch] Injected missing XML site '{object_region_name}' to body._obj at pos={matching_clean_site.get('pos')} (based on '{matching_clean_site.get('name')}')")
                            already = new_site(name=object_region_name, pos=matching_clean_site.get('pos'), quat=matching_clean_site.get('quat') if matching_clean_site.get('quat') is not None else '1 0 0 0', rgba=matching_clean_site.get('rgba'), size=matching_clean_site.get('size'), type=matching_clean_site.get('type') if matching_clean_site.get('type') is not None else 'sphere')
                            body._obj.append(already)
                        exact_site = already
                    if exact_site is not None:
                        joints = matching_clean_part.findall('./joint') if matching_clean_part is not None else []
                        size_arr = np.array([0.05, 0.05, 0.05])
                        size_val = exact_site.get('size')
                        if size_val is not None:
                            try:
                                raw_arr = string_to_array(size_val)
                                if isinstance(raw_arr, (float, int)):
                                    raw_arr = np.array([raw_arr])
                                for idx in range(min(3, len(raw_arr))):
                                    size_arr[idx] = max(0.05, raw_arr[idx])
                            except Exception as parse_err:
                                print(f"[Monkey Patch] Error parsing size '{size_val}': {parse_err}")
                        object_sites_dict[object_region_name] = SiteObject(name=object_region_name, parent_name=body.name, joints=[joint.get('name') for joint in joints], size=size_arr, rgba=exact_site.get('rgba'), site_type=exact_site.get('type'), site_pos=exact_site.get('pos'), site_quat=exact_site.get('quat') if exact_site.get('quat') is not None else '1 0 0 0', object_properties=body.object_properties)
        self.object_sites_dict = object_sites_dict
        for query_dict in [self.fixtures_dict, self.objects_dict]:
            for name, body in query_dict.items():
                if body.object_properties['vis_site_names'] != {}:
                    self.visualization_sites_list.append(name)

    target_class = TASK_MAPPING.get('libero_tabletop_manipulation')
    if target_class is not None:
        target_class._load_sites_in_arena = patched_load_sites_in_arena
        print(f'[Monkey Patch] Applied _load_sites_in_arena fix to {target_class.__name__}')

patch_libero_tabletop_manipulation()

class MockConfig:
    def __init__(self, suite='libero_goal_object_ood'):
        self.model_family = 'openvla'
        self.pretrained_checkpoint = 'moojink/openvla-7b-oft-finetuned-libero-goal'
        self.use_l1_regression = True
        self.use_diffusion = False
        self.use_film = False
        self.num_images_in_input = 2
        self.use_proprio = True
        self.center_crop = True
        self.lora_rank = 32
        self.load_in_8bit = True
        self.load_in_4bit = False
        self.unnorm_key = 'libero_goal_no_noops'
        self.task_suite_name = suite
        self.num_trials_per_task = 1
        self.initial_states_path = 'DEFAULT'
        self.env_img_res = 256
        self.num_open_loop_steps = 8
        self.num_steps_wait = 10
        self.use_wandb = False
        self.seed = 0

class SeqRiskModel(nn.Module):
    def __init__(self, hist_dim=21, action_dim=7, static_dim=43, width=128, layers=3, heads=4, dropout=0.1):
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=dropout, batch_first=True, activation='gelu')
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)
        self.static_in_dropout = nn.Dropout(0.0)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(nn.LayerNorm(width * 2), nn.Linear(width * 2, width), nn.GELU(), nn.Dropout(dropout), nn.Linear(width, 1))
    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch['history']), self.action_proj(batch['action'])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch['static']))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


def pad_flat(values, size):
    arr = np.asarray(values if values is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(size, dtype=np.float32)
    n = min(size, arr.size)
    if n: out[:n] = arr[:n]
    return out

def pad_seq(values, rows, cols):
    arr = np.asarray(values if values is not None else [], dtype=np.float32)
    if arr.size == 0: return np.zeros((rows, cols), dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, cols) if arr.size % cols == 0 else arr.reshape(1, -1)
    out = np.zeros((rows, cols), dtype=np.float32)
    rr = min(rows, arr.shape[0]); cc = min(cols, arr.shape[1])
    out[:rr, :cc] = arr[:rr, :cc]
    return out

def fit_seq_standardizer(x):
    mean = x.reshape(-1, x.shape[-1]).mean(axis=0)
    std = x.reshape(-1, x.shape[-1]).std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {'mean': mean.astype(np.float32), 'std': std.astype(np.float32)}

def fit_standardizer(x):
    mean = x.mean(axis=0); std = x.std(axis=0); std = np.where(std < 1e-5, 1.0, std)
    return {'mean': mean.astype(np.float32), 'std': std.astype(np.float32)}

def apply_seq_standardizer(x, stats): return np.clip((x - stats['mean']) / stats['std'], -10.0, 10.0).astype(np.float32)
def apply_standardizer(x, stats): return np.clip((x - stats['mean']) / stats['std'], -10.0, 10.0).astype(np.float32)

def make_risk_features(proprio, actions_np, history_buffer):
    action = pad_seq(actions_np, 10, 7)
    proprio = pad_flat(proprio, 8)
    ace = np.zeros(7, dtype=np.float32)
    action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
    static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
    hist = np.zeros((16, 21), dtype=np.float32)
    hist_src = history_buffer[-16:]
    offset = 16 - len(hist_src)
    for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
        hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])
    return hist, action, static_base

def load_train_stats(max_fail_steps=300):
    train_ids = set(json.load(open(SPLIT_DIR / 'train_episode_ids.json')))
    eps = [json.loads(l) for l in open(FINAL_DATASET / 'episode_summaries.jsonl') if l.strip()]
    ep_map = {(e['task_id'], e['reset_seed']): e for e in eps if e['episode_index_global'] in train_ids}
    rows_h, rows_a, rows_st = [], [], []
    hist_by_ep = defaultdict(list)
    for line in open(FINAL_DATASET / 'query_records.jsonl'):
        if not line.strip(): continue
        q = json.loads(line)
        ep = ep_map.get((q['task_id'], q['reset_seed']))
        if ep is None: continue
        if (not ep['success']) and q['env_timestep'] > max_fail_steps: continue
        hb = hist_by_ep[(q['task_id'], q['reset_seed'])]
        actions_np = np.asarray(q['full_predicted_action_chunk'], dtype=np.float32)
        proprio = pad_flat(q['proprio_vector'], 8)
        hist, action, static = make_risk_features(proprio, actions_np, hb)
        rows_h.append(hist); rows_a.append(action); rows_st.append(static)
        executed = pad_flat((q.get('actual_executed_actions') or [actions_np[0]])[0], 7)
        hb.append((proprio, executed, np.zeros(7, dtype=np.float32)))
    h = np.stack(rows_h).astype(np.float32); a = np.stack(rows_a).astype(np.float32); st = np.stack(rows_st).astype(np.float32)
    return {'history': fit_seq_standardizer(h), 'action': fit_seq_standardizer(a), 'static': fit_standardizer(st), 'train_rows': len(rows_h)}

def load_risk_model(device):
    stats = load_train_stats(max_fail_steps=300)
    model = SeqRiskModel().to(device)
    state = torch.load(RISK_MODEL_PATH, map_location=device)
    model.load_state_dict(state)
    model.eval()
    return model, stats

def risk_score(model, stats, hist, action, static, device):
    batch = {
        'history': torch.tensor(apply_seq_standardizer(hist, stats['history']), device=device).unsqueeze(0),
        'action': torch.tensor(apply_seq_standardizer(action, stats['action']), device=device).unsqueeze(0),
        'static': torch.tensor(apply_standardizer(static, stats['static']), device=device).unsqueeze(0),
    }
    with torch.no_grad():
        return float(torch.sigmoid(model(batch)).cpu().item())

def obs_to_proprio(obs):
    ee_pos = obs.get('robot0_eef_pos', np.zeros(3))
    ee_quat = obs.get('robot0_eef_quat', np.array([0,0,0,1.0]))
    grip = obs.get('robot0_gripper_qpos', np.zeros(2))
    state = np.concatenate([ee_pos, quat2axisangle(ee_quat), grip])[:8]
    if state.size < 8: state = np.pad(state, (0, 8-state.size))
    return state

def prepare_observation(obs, resize_size):
    img = get_libero_image(obs); wrist = get_libero_wrist_image(obs)
    return {'full_image': resize_image_for_policy(img, resize_size), 'wrist_image': resize_image_for_policy(wrist, resize_size), 'state': obs_to_proprio(obs)}, img

def process_action(action, model_family):
    action = normalize_gripper_action(action, binarize=True)
    if model_family == 'openvla': action = invert_gripper_action(action)
    return action

def append_jsonl(path, row):
    with open(path, 'a') as f: f.write(json.dumps(row, sort_keys=True) + '\n')

def run_episode(policy, task_id, reset_seed, episode_idx, episode_global_idx, task_suite, cfg, vla, processor, action_head, proprio_projector, risk_model, risk_stats, args, paths, resize_size, device):
    task = task_suite.get_task(task_id)
    # LIBERO-PRO OOD alias: init files live under libero_goal_object_ood,
    # while BDDL files live under libero_goal_object_ood_temp on Bob.
    initial_states = task_suite.get_task_init_states(task_id)
    if args.suite == 'libero_goal_object_ood' and getattr(task, 'problem_folder', None) == 'libero_goal_object_ood':
        if hasattr(task, '_replace'):
            task = task._replace(problem_folder='libero_goal_object_ood_temp')
        else:
            import copy
            task = copy.copy(task)
            object.__setattr__(task, 'problem_folder', 'libero_goal_object_ood_temp')
    set_seed_everywhere(reset_seed)
    env, task_description = get_libero_env(task, cfg.model_family, resolution=cfg.env_img_res)
    obs = None
    success = False; error = ''; terminal_done=False
    risk_trigger_count = 0; num_queries = 0
    risk_scores = []
    executed_horizons = []
    history_buffer = []
    action_queue = deque()
    t = 0; start = time.time()
    try:
        env.reset()
        obs = env.set_init_state(initial_states[episode_idx % len(initial_states)])
        while t < args.max_steps + cfg.num_steps_wait:
            if t < cfg.num_steps_wait:
                obs, reward, done, info = env.step(get_libero_dummy_action(cfg.model_family))
                t += 1
                continue
            step_idx = t - cfg.num_steps_wait
            if len(action_queue) == 0:
                observation, img = prepare_observation(obs, resize_size)
                t0 = time.time()
                actions = get_action(cfg, vla, observation, task_description, processor=processor, action_head=action_head, proprio_projector=proprio_projector, noisy_action_projector=None, use_film=cfg.use_film)
                inference_time = time.time() - t0
                actions_np = np.asarray(actions, dtype=np.float32)
                if actions_np.shape != (8,7): raise RuntimeError(f'action shape {actions_np.shape}, expected (8,7)')
                if not np.isfinite(actions_np).all(): raise RuntimeError('non-finite action chunk')
                proprio = observation['state']
                hist, risk_action, static = make_risk_features(proprio, actions_np, history_buffer)
                score = None; exec_h = 8
                if policy == 'openvla_risk_horizon':
                    score = risk_score(risk_model, risk_stats, hist, risk_action, static, device)
                    if score >= args.risk_threshold:
                        exec_h = args.risk_horizon
                        risk_trigger_count += 1
                risk_scores.append(score)
                executed_horizons.append(exec_h)
                selected = actions_np[:exec_h]
                action_queue.extend(selected)
                append_jsonl(paths['query'], {
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
                # Training history updates once per query using first executed action from the planned chunk.
                history_buffer.append((pad_flat(proprio,8), pad_flat(selected[0],7), np.zeros(7,dtype=np.float32)))
            action = action_queue.popleft()
            action_processed = process_action(action, cfg.model_family)
            obs, reward, done, info = env.step(action_processed.tolist())
            if done:
                success = True; terminal_done=True; break
            t += 1
    except KeyboardInterrupt:
        raise
    except Exception as e:
        error = repr(e)
        traceback.print_exc()
    finally:
        try: env.close()
        except Exception: pass
    num_steps = max(0, t - cfg.num_steps_wait)
    return {
        'policy': policy, 'suite': args.suite, 'task_id': task_id, 'task_name': task.language,
        'episode_index_for_task': episode_idx, 'reset_seed': reset_seed, 'success': bool(success),
        'terminal_done': bool(terminal_done), 'timeout': bool(num_steps >= args.max_steps), 'num_steps': int(num_steps),
        'max_steps': args.max_steps, 'wall_time_seconds': time.time() - start, 'model_id': cfg.pretrained_checkpoint,
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
    ap = argparse.ArgumentParser()
    ap.add_argument('--suite', default='libero_goal_object_ood')
    ap.add_argument('--output-root', required=True)
    ap.add_argument('--episodes-per-task', type=int, default=100)
    ap.add_argument('--seed-start', type=int, default=10)
    ap.add_argument('--max-steps', type=int, default=800)
    ap.add_argument('--policies', default='openvla_basic,openvla_risk_horizon')
    ap.add_argument('--task-ids', default='all')
    ap.add_argument('--risk-threshold', type=float, default=0.8049)
    ap.add_argument('--risk-horizon', type=int, default=1)
    args = ap.parse_args()

    out = Path(args.output_root); out.mkdir(parents=True, exist_ok=True)
    paths = {'summary': out/'episode_summaries.jsonl', 'query': out/'query_records.jsonl', 'manifest': out/'run_manifest.json'}
    cfg = MockConfig(args.suite)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    set_seed_everywhere(0)
    print('Loading OpenVLA...')
    vla = get_vla(cfg); openvla_oft_bob_compat.align_rotary_emb_devices(vla)
    processor = get_processor(cfg)
    llm_dim = vla.llm_dim if hasattr(vla, 'llm_dim') else vla.config.text_config.hidden_size
    proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
    action_head = get_action_head(cfg, llm_dim=llm_dim)
    print('Loading risk model/stats...')
    risk_model, risk_stats = load_risk_model(device)
    print('Risk train rows for stats:', risk_stats['train_rows'])
    task_suite = benchmark.get_benchmark_dict()[args.suite]()
    n_tasks = task_suite.get_num_tasks()
    if args.task_ids == 'all': task_ids = list(range(n_tasks))
    else: task_ids = [int(x) for x in args.task_ids.split(',')]
    policies = [p.strip() for p in args.policies.split(',') if p.strip()]
    resize_size = get_image_resize_size(cfg)
    manifest = {
        'suite': args.suite, 'task_count': n_tasks, 'task_ids': task_ids, 'task_names': [task_suite.get_task(i).language for i in task_ids],
        'policies': policies, 'episodes_per_task': args.episodes_per_task, 'seed_start': args.seed_start,
        'seed_end': args.seed_start + args.episodes_per_task - 1, 'max_steps': args.max_steps,
        'risk_model_path': str(RISK_MODEL_PATH), 'risk_model': 'model_300steps.pt', 'risk_threshold_source': 'final 1890 validation q95',
        'risk_threshold': args.risk_threshold, 'risk_horizon_policy': f'H={args.risk_horizon} when risk>=threshold else H=8',
        'ACE_AVAILABLE': 'NO', 'SIMVLA_UNCERTAINTY_FEATURES_AVAILABLE': 'NO', 'created_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    paths['manifest'].write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
    completed = set()
    if paths['summary'].exists():
        for line in open(paths['summary']):
            if line.strip():
                r=json.loads(line); completed.add((r['policy'], r['task_id'], r['reset_seed']))
    total = len(policies) * len(task_ids) * args.episodes_per_task
    done_count = len(completed)
    for policy in policies:
        for task_id in task_ids:
            for ep in range(args.episodes_per_task):
                seed = args.seed_start + ep
                key=(policy, task_id, seed)
                if key in completed: continue
                print(f'[{done_count+1}/{total}] policy={policy} task={task_id} seed={seed}', flush=True)
                row = run_episode(policy, task_id, seed, ep, done_count, task_suite, cfg, vla, processor, action_head, proprio_projector, risk_model, risk_stats, args, paths, resize_size, device)
                row['episode_index_global'] = done_count
                append_jsonl(paths['summary'], row)
                completed.add(key); done_count += 1
    print('DONE')

if __name__ == '__main__':
    main()
