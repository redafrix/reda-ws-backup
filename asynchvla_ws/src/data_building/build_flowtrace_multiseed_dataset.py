#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, sys, time
from pathlib import Path
import torch

REDA_WS = Path(os.environ.get('REDA_WS', '/media/rootalkhatib/My Passport/reda_ws'))
SIM = REDA_WS / 'intern_ship_ws/simvla/code/SimVLA_modified'
CKPT = REDA_WS / 'intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000'
BACK = REDA_WS / 'intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct'
OUTROOT = REDA_WS / 'asynchvla_ws/data/processed_stage7_flow'

sys.path.insert(0, str(REDA_WS / 'asynchvla_ws/src'))
sys.path.insert(0, str(SIM))

from datasets.dataset_smolvlm import SmolVLMDataReader
from models.configuration_smolvlm_vla import SmolVLMVLAConfig
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor
from simvla_trace.trace import generate_actions_trace


def remap_path(path: str) -> str:
    old = '/media/rootalkhatib/My Passport/reda_ws'
    path = str(path)
    if path.startswith(old):
        return str(REDA_WS) + path[len(old):]
    return path


def task(path: str) -> str:
    p = Path(path)
    s = p.stem.removesuffix('_demo')
    m = re.search(r'(KITCHEN|LIVING_ROOM|STUDY|LIBERO)_SCENE\d+_', s)
    s = s[m.end():] if m else s
    return s.replace('_', ' ')


def meta_for(path: str, out: Path) -> Path:
    meta = {
        'dataset_name': 'libero_hdf5',
        'data_dir': str(Path(path).parent.parent),
        'datalist': [{'path': path, 'task': task(path), 'subset': Path(path).parent.name}],
        'num_episodes': 1,
        'state_dim': 8,
        'action_dim': 7,
    }
    out.write_text(json.dumps(meta))
    return out


def load_model():
    cfg = SmolVLMVLAConfig.from_pretrained(str(CKPT))
    cfg.smolvlm_model_path = str(BACK)
    model = SmolVLMVLA.from_pretrained(str(CKPT), config=cfg)
    dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    return model.to(dev).eval(), dev


def _cpu_summary(summary: dict) -> dict:
    out = {}
    for k, v in summary.items():
        if isinstance(v, torch.Tensor):
            out[k] = v.squeeze(0).detach().cpu()
        else:
            out[k] = v
    return out


def build_part(files, part, max_samples, cap, model, dev, proc, outdir, steps, seeds):
    samples = []
    metas = outdir / 'metas'
    metas.mkdir(parents=True, exist_ok=True)
    idx = 0
    for fi, path in enumerate(files):
        path = remap_path(path)
        if len(samples) >= max_samples:
            break
        ds = SmolVLMDataReader(str(meta_for(path, metas / f'{part}_{fi:04d}.json')), num_actions=10, num_views=3, training=False, action_mode='libero_joint', image_size=384)
        for li, sample in enumerate(ds):
            if len(samples) >= max_samples or li >= cap:
                break
            ids = proc.encode_language(sample['language_instruction'])['input_ids'].to(dev)
            image = sample['image_input'].unsqueeze(0).to(dev)
            mask = sample['image_mask'].unsqueeze(0).to(dev)
            proprio = sample['proprio'].unsqueeze(0).to(dev)
            expert = sample['action'].unsqueeze(0).to(dev)
            expert_norm = model.action_space.normalize_action(expert) if hasattr(model.action_space, 'normalize_action') else expert
            item = {
                'sample_id': f'{part}_{idx:07d}',
                'context_id': f'{part}_ctx_{idx:07d}',
                'task_name': task(path),
                'source_hdf5': path,
                'source_local_index': li,
                'language_instruction': sample['language_instruction'],
                'proprio': proprio.squeeze(0).detach().cpu(),
                'expert_normalized_action': expert_norm.squeeze(0).detach().cpu(),
                'expert_postprocessed_action': expert.squeeze(0).detach().cpu(),
                'split': part,
            }
            for seed in seeds:
                trace = generate_actions_trace(model, input_ids=ids, image_input=image, image_mask=mask, proprio=proprio, steps=steps, seed=seed, return_flow_trace=True)
                if 'pooled_vlm_features' not in item:
                    item['pooled_vlm_features'] = trace['pooled_vlm_features'].squeeze(0).detach().cpu()
                gen = trace['generated_normalized_action']
                err = torch.linalg.vector_norm(gen - expert_norm, dim=-1).squeeze(0)
                prefix = f'simvla_seed{seed}'
                item[f'{prefix}_normalized_action'] = gen.squeeze(0).detach().cpu()
                item[f'{prefix}_postprocessed_action'] = trace['generated_postprocessed_action'].squeeze(0).detach().cpu()
                item[f'{prefix}_per_step_l2_error'] = err.detach().cpu()
                item[f'{prefix}_chunk_l2_error'] = float(err.mean().cpu())
                item[f'{prefix}_flow_trace_summary'] = _cpu_summary(trace['flow_trace_summary'])
                item[f'{prefix}_num_flow_steps'] = int(trace['num_flow_steps'])
            samples.append(item)
            idx += 1
            if len(samples) % 25 == 0:
                print(part, len(samples), flush=True)
    out_file = outdir / f'flowtrace_multiseed_trace_{part}.pt'
    torch.save({'schema_version': 'flowtrace_multiseed_trace_v1', 'part': part, 'seeds': seeds, 'samples': samples, 'num_samples': len(samples), 'checkpoint': str(CKPT)}, out_file)
    print('saved', out_file, len(samples), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--split-manifest', required=True)
    ap.add_argument('--split-name', required=True)
    ap.add_argument('--max-contexts', type=int, default=200)
    ap.add_argument('--max-calib', type=int, default=80)
    ap.add_argument('--max-test-id', type=int, default=80)
    ap.add_argument('--max-test-ood', type=int, default=80)
    ap.add_argument('--cap-per-file', type=int, default=10)
    ap.add_argument('--steps', type=int, default=10)
    ap.add_argument('--simvla-seeds', nargs='+', type=int, default=[0,1,2,3,4])
    args = ap.parse_args()
    start = time.time()
    man = json.load(open(args.split_manifest))
    outdir = OUTROOT / args.split_name
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / 'manifest_used.json').write_text(json.dumps(man, indent=2))
    model, dev = load_model()
    proc = SmolVLMVLAProcessor.from_pretrained(str(BACK))
    for part, files, mx in [
        ('train', man['train_files'], args.max_contexts),
        ('calib', man['calib_files'], args.max_calib),
        ('test_id', man.get('test_id_files', []), args.max_test_id),
        ('test_ood', man.get('test_ood_files', []), args.max_test_ood),
    ]:
        if files and mx > 0:
            build_part(files, part, mx, args.cap_per_file, model, dev, proc, outdir, args.steps, args.simvla_seeds)
    print('done_sec', time.time() - start)


if __name__ == '__main__':
    main()
