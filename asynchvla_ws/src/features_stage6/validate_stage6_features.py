#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
import torch
REDA_WS=Path('/media/rootalkhatib/My Passport/reda_ws')
sys.path.insert(0,str(REDA_WS/'asynchvla_ws/src'))
from features_stage6.build_features import build_seed_stats, feature_vector
DATA=REDA_WS/'asynchvla_ws/data/processed_stage5/holdout_libero_object/multiseed_candidate_train.pt'
REPORT=REDA_WS/'asynchvla_ws/outputs/reports/stage6_feature_validation.md'
MODES=['A0_action_flat','A1_context','A2_full_old','F1_action_geometry','F2_proprio_action_delta','F3_seed_ensemble','F4_context_action_interactions','M2_engineered','M4_seed_relative','M3_gated_base']
def main():
    payload=torch.load(DATA,map_location='cpu'); rows=payload['candidates'][:500]
    seed_stats=build_seed_stats(rows)
    out={}
    for mode in MODES:
        xs=[]
        for r in rows[:100]: xs.append(feature_vector(r,mode,seed_stats))
        x=torch.stack(xs)
        out[mode]={'dim':int(x.shape[1]),'finite':bool(torch.isfinite(x).all()),'mean_abs':float(x.abs().mean()),'max_abs':float(x.abs().max())}
    sim_ctx=sum(1 for v in seed_stats.values() if len(v['stack'])>=5)
    lines=['# Stage 6 Feature Validation','',f'- Source dataset: `{DATA}`',f'- Rows checked: `{len(rows)}`',f'- Contexts with seed ensemble stats in checked subset: `{sim_ctx}`','','## Feature Modes','','| Mode | Dim | Finite | Mean abs | Max abs |','|---|---:|---|---:|---:|']
    for m,v in out.items(): lines.append(f'| `{m}` | {v["dim"]} | `{v["finite"]}` | {v["mean_abs"]:.6f} | {v["max_abs"]:.6f} |')
    lines += ['','## Flow Trace Features','', 'Current Stage 5 candidate datasets do not store denoising/flow path metadata. `F5_flow_trace_features` is pending until trace extraction stores update norms / velocity norms / final-step metadata.']
    REPORT.write_text('\n'.join(lines)+'\n')
    print(json.dumps(out,indent=2)); print('report',REPORT)
if __name__=='__main__': main()
