#!/usr/bin/env python3
import torch, os, sys
import numpy as np

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/stage5_debug/multiseed_candidate_debug.pt'
    
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return

    sz = os.path.getsize(path)
    print(f"File size: {sz / 1024 / 1024:.2f} MB")
    
    data = torch.load(path, map_location='cpu')
    cands = data['candidates']
    
    contexts = set(c['context_id'] for c in cands)
    print(f"Number of contexts: {len(contexts)}")
    print(f"Number of candidate rows: {len(cands)}")
    
    from collections import defaultdict
    types = defaultdict(list)
    for c in cands:
        types[c['candidate_type']].append(c['true_chunk_l2_error'])
        
    print("\nCandidate types and counts:")
    for t, errs in types.items():
        print(f"  {t}: count={len(errs)}, mean_err={np.mean(errs):.4f}, min={np.min(errs):.4f}, max={np.max(errs):.4f}")

    print("\nSame-context proof table:")
    ctx_ids = list(contexts)[:3]
    for cid in ctx_ids:
        rows = [c for c in cands if c['context_id'] == cid]
        print(f"\nContext: {cid}")
        print(f"  Types found: {[r['candidate_type'] for r in rows]}")
        
        # Check identical features
        vlm_identical = all(torch.equal(rows[0]['pooled_vlm_features'], r['pooled_vlm_features']) for r in rows)
        proprio_identical = all(torch.equal(rows[0]['proprio'], r['proprio']) for r in rows)
        target_identical = all(torch.equal(rows[0]['target_expert_action_normalized'], r['target_expert_action_normalized']) for r in rows)
        
        print(f"  pooled VLM identical across candidates: {vlm_identical}")
        print(f"  proprio identical across candidates: {proprio_identical}")
        print(f"  target expert action identical across candidates: {target_identical}")

if __name__ == '__main__':
    main()
