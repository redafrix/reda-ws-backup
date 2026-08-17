#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

def load_jsonl(p: Path):
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--baseline-root',type=Path,required=True); ap.add_argument('--shadow-root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    bs={int(x['source_episode_id']):x for x in load_jsonl(a.baseline_root/'episode_summaries.jsonl')}
    ss={int(x['source_episode_id']):x for x in load_jsonl(a.shadow_root/'episode_summaries.jsonl')}
    br=load_jsonl(a.baseline_root/'risk_receding_samples.jsonl'); sr=load_jsonl(a.shadow_root/'risk_receding_samples.jsonl')
    bb={}; sb={}
    for x in br: bb.setdefault(int(x['metadata']['source_episode_id']),[]).append(x)
    for x in sr: sb.setdefault(int(x['metadata']['source_episode_id']),[]).append(x)
    checks=[]
    for sid in (0,1,2):
        checks.append({'episode':sid,'check':'present','pass':sid in bs and sid in ss})
        if sid not in bs or sid not in ss: continue
        checks += [
            {'episode':sid,'check':'outcome_match','pass':bool(bs[sid]['success'])==bool(ss[sid]['success']),'baseline':bool(bs[sid]['success']),'shadow':bool(ss[sid]['success'])},
            {'episode':sid,'check':'decision_rows_match','pass':int(bs[sid]['decision_rows'])==int(ss[sid]['decision_rows']),'baseline':int(bs[sid]['decision_rows']),'shadow':int(ss[sid]['decision_rows'])},
            {'episode':sid,'check':'shadow_zero_executed_modifications','pass':int(ss[sid].get('online_action_modifications_count',0))==0,'actual':int(ss[sid].get('online_action_modifications_count',0))},
        ]
        brow=bb.get(sid,[]); srow=sb.get(sid,[])
        checks.append({'episode':sid,'check':'row_count_match','pass':len(brow)==len(srow),'baseline':len(brow),'shadow':len(srow)})
        if len(brow)!=len(srow): continue
        main_seed_ok=all(int(x['main_seed'])==int(y['main_seed']) for x,y in zip(brow,srow))
        ace_seed_ok=all(list(x['ace_candidate_seeds'])==list(y['ace_candidate_seeds']) for x,y in zip(brow,srow))
        checks += [
            {'episode':sid,'check':'main_seed_sequence_match','pass':main_seed_ok},
            {'episode':sid,'check':'ace_seed_sequence_match','pass':ace_seed_ok},
        ]
        internal=0.0
        for x in srow:
            ex=np.asarray(x['executed_action_sequence'],dtype=np.float32)
            main=np.asarray(x['main_candidate_action_chunk_env'],dtype=np.float32)[:len(ex)]
            if ex.shape!=main.shape: internal=float('inf'); break
            internal=max(internal,float(np.max(np.abs(ex-main))) if ex.size else 0.0)
        checks.append({'episode':sid,'check':'shadow_executes_candidate0','max_abs_diff':internal,'pass':internal<=1e-6})
    ok=all(c['pass'] for c in checks)
    out={'schema_version':'isaac_shadow_functional_gate_v1','pass':ok,'meaning':'Functional safety gate only; historical fresh-replay bitwise equality is not required. Shadow must preserve outcomes/row counts on 3 episodes, use identical candidate seeds, report zero executed interventions, and execute candidate-0 actions internally.','checks':checks}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True)); return 0 if ok else 2
if __name__=='__main__': raise SystemExit(main())
