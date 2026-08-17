#!/usr/bin/env python3
"""Create immutable OOD150 shadow/dev/holdout manifests for online controller tuning."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

WORKSPACE=Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813')
sys.path.insert(0,str(WORKSPACE/'src'))
from risk_collection.storage import canonical_sha256


def rank(seed:int, row:dict)->str:
    raw=f"isaac-online-ood150-dev-v1|{seed}|{int(row['source_episode_id'])}|{row['scene_fingerprint_sha256']}"
    return hashlib.sha256(raw.encode('ascii')).hexdigest()

def subset(master:dict, ids:set[int], role:str, parent_sha:str, controller_selection:bool)->dict:
    episodes=[]
    for source in master['episodes']:
        sid=int(source['scene']['source_episode_id'])
        if sid not in ids: continue
        item=json.loads(json.dumps(source))
        item['benchmark_episode_id']=len(episodes)
        episodes.append(item)
    payload={k:json.loads(json.dumps(v)) for k,v in master.items() if k not in {'episodes','manifest_fingerprint_sha256','benchmark_name','provenance'}}
    payload['benchmark_name']=f"reaching_pose_v1_locked_ood150_online_{role}"
    payload['provenance']={
        **json.loads(json.dumps(master['provenance'])),
        'online_parent_manifest_sha256': parent_sha,
        'online_subset_role': role,
        'online_subset_episode_count': len(episodes),
        'used_for_online_controller_selection': bool(controller_selection),
        'used_for_risk_model_training': False,
        'used_for_risk_model_threshold_calibration': False,
    }
    payload['episodes']=episodes
    payload['manifest_fingerprint_sha256']=canonical_sha256(payload)
    return payload

def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument('--master-manifest',type=Path,required=True)
    p.add_argument('--baseline-summaries',type=Path,required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--seed',type=int,default=20260817)
    args=p.parse_args()
    master=json.loads(args.master_manifest.read_text())
    rows=[json.loads(x) for x in args.baseline_summaries.read_text().splitlines() if x.strip()]
    if len(master['episodes'])!=150 or len(rows)!=150: raise RuntimeError('expected exact locked OOD150')
    if sum(bool(r['success']) for r in rows)!=72 or sum(not bool(r['success']) for r in rows)!=78:
        raise RuntimeError('baseline OOD150 outcome identity changed from verified 72/78')
    byid={int(r['source_episode_id']):r for r in rows}
    manifest_ids={int(e['scene']['source_episode_id']) for e in master['episodes']}
    if set(byid)!=manifest_ids: raise RuntimeError('baseline summaries and locked manifest membership differ')
    successes=sorted((r for r in rows if r['success']),key=lambda r:rank(args.seed,r))
    failures=sorted((r for r in rows if not r['success']),key=lambda r:rank(args.seed,r))
    dev_ids={int(r['source_episode_id']) for r in successes[:20]+failures[:20]}
    holdout_ids=manifest_ids-dev_ids
    shadow_ids={0,1,2}
    if not shadow_ids <= manifest_ids: raise RuntimeError('shadow source IDs 0,1,2 not present')
    out=args.output_dir; out.mkdir(parents=True,exist_ok=True)
    parent_sha=hashlib.sha256(args.master_manifest.read_bytes()).hexdigest()
    specs=[('shadow3',shadow_ids,False),('dev40',dev_ids,True),('holdout110',holdout_ids,False)]
    for role,ids,sel in specs:
        payload=subset(master,ids,role,parent_sha,sel)
        (out/f'{role}.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    split={
      'schema_version':'isaac_online_ood150_split_v1','seed':args.seed,
      'parent_manifest_sha256':parent_sha,
      'baseline_successes':72,'baseline_failures':78,
      'dev40':{'successes':20,'failures':20,'source_episode_ids':sorted(dev_ids)},
      'holdout110':{'successes':52,'failures':58,'source_episode_ids':sorted(holdout_ids)},
      'shadow3':{'source_episode_ids':[0,1,2]},
      'selection_policy':'controller hyperparameters may use dev40 online success only; holdout110 is untouched until one variant is selected',
    }
    # Derive actual holdout counts instead of trusting arithmetic.
    split['holdout110']['successes']=sum(bool(byid[i]['success']) for i in holdout_ids)
    split['holdout110']['failures']=sum(not bool(byid[i]['success']) for i in holdout_ids)
    (out/'SPLIT.json').write_text(json.dumps(split,indent=2,sort_keys=True)+'\n')
    print(json.dumps(split,indent=2,sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
