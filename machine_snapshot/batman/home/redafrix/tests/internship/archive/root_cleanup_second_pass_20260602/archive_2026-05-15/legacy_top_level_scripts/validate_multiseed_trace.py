#!/usr/bin/env python3
import torch, os, sys
import numpy as np

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/stage5_debug/multiseed_trace_debug.pt'
    
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return

    sz = os.path.getsize(path)
    print(f"File size: {sz / 1024 / 1024:.2f} MB")
    
    data = torch.load(path, map_location='cpu')
    samples = data['samples']
    seeds = data.get('seeds', [0,1,2,3,4])
    
    print(f"Number of contexts: {len(samples)}")
    if len(samples) == 0: return

    s0 = samples[0]
    print("\nKeys and shapes (first sample):")
    for k, v in s0.items():
        if isinstance(v, torch.Tensor):
            print(f"  {k}: {list(v.shape)} {v.dtype}")
        else:
            print(f"  {k}: {type(v).__name__}")

    # NaN/Inf checks
    has_nan = False
    for i, s in enumerate(samples):
        for k, v in s.items():
            if isinstance(v, torch.Tensor) and (torch.isnan(v).any() or torch.isinf(v).any()):
                print(f"NaN/Inf found in sample {i} key {k}")
                has_nan = True
    if not has_nan: print("\nNo NaN/Inf found in tensors.")

    print("\nError stats per seed:")
    for seed in seeds:
        errs = [s[f'simvla_seed{seed}_chunk_l2_error'] for s in samples]
        print(f"  Seed {seed}: mean={np.mean(errs):.4f}, std={np.std(errs):.4f}, min={np.min(errs):.4f}, max={np.max(errs):.4f}")

    print("\nSeed diversity:")
    diversity = []
    identical_count = 0
    
    for i, s in enumerate(samples):
        actions = [s[f'simvla_seed{seed}_normalized_action'] for seed in seeds]
        
        dists = []
        for j in range(len(seeds)):
            for k in range(j+1, len(seeds)):
                dist = torch.linalg.vector_norm(actions[j] - actions[k], dim=-1).mean().item()
                dists.append(dist)
        
        mean_dist = np.mean(dists)
        diversity.append({'ctx': s['context_id'], 'mean_dist': mean_dist, 'task': s['task_name']})
        
        if mean_dist < 1e-4:
            identical_count += 1
            
    print(f"Contexts where all seeds are nearly identical (dist < 1e-4): {identical_count} / {len(samples)} ({identical_count/len(samples)*100:.1f}%)")
    
    diversity.sort(key=lambda x: x['mean_dist'])
    
    print("\nExamples of LOW seed diversity:")
    for d in diversity[:3]:
        print(f"  {d['ctx']} ({d['task']}): mean pairwise distance = {d['mean_dist']: .6f}")
        
    print("\nExamples of HIGH seed diversity:")
    for d in diversity[-3:]:
        print(f"  {d['ctx']} ({d['task']}): mean pairwise distance = {d['mean_dist']: .6f}")

if __name__ == '__main__':
    main()
