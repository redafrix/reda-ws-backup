#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,os,subprocess
from pathlib import Path

WORKSPACE=Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813')
MODEL=WORKSPACE/'models/isaac_h10_topk8_temporal_v1'
NORM=WORKSPACE/'frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json'
OOD_MANIFEST=WORKSPACE/'automation/generated/locked_ood150/manifest.json'
OOD_RUNCFG=WORKSPACE/'automation/generated/locked_ood150/run_config.yaml'
BASELINE=WORKSPACE/'outputs/final_locked_h10_ood150_seed20260728'
EXPECTED={
 'model.pt':'ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38',
 'normalization.json':'78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050',
 'locked_manifest':'7ff10101f7d61966ef85246850aa4b08f158da3ef1c8867217d1e2a4a9fc8829',
 'locked_run_config':'0df8c2df4d6c23b03487afdf9b525b2db0b4898fdc287639b667323b37e0c582',
 'baseline_rows':'0651da79baeabb3e90f0d4f1cde955751947d78dc228472261f5c61081362a84',
 'baseline_summaries':'161f1911fb12d4781c8459f6b1d1c8e18cc62c0e59f0f648befe9cd9aedd0785',
}
EXPECTED_THRESHOLDS={
 'best_val_f1':0.7990124225616455,
 'q90_success':0.2370966076850891,
 'q95_success':0.3443679213523865,
 'q99_success':0.7373747229576111,
}
def sha(p:Path):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1024*1024),b''):h.update(c)
 return h.hexdigest()
def procs(pattern:str):
 r=subprocess.run(['pgrep','-af',pattern],text=True,capture_output=True,check=False)
 return [x for x in r.stdout.splitlines() if x.strip() and str(os.getpid()) not in x.split(maxsplit=1)[:1]]
def main()->int:
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 files={
  'model.pt':MODEL/'model.pt','normalization.json':NORM,'locked_manifest':OOD_MANIFEST,'locked_run_config':OOD_RUNCFG,
  'baseline_rows':BASELINE/'risk_receding_samples.jsonl','baseline_summaries':BASELINE/'episode_summaries.jsonl',
 }
 checks=[]
 for key,path in files.items():
  actual=sha(path); ok=actual==EXPECTED[key]; checks.append({'name':key,'path':str(path),'expected_sha256':EXPECTED[key],'actual_sha256':actual,'pass':ok})
 thresholds=json.loads((MODEL/'thresholds.json').read_text())
 for k,v in EXPECTED_THRESHOLDS.items():
  actual=float(thresholds[k]); checks.append({'name':f'threshold:{k}','expected':v,'actual':actual,'pass':abs(actual-v)<1e-12})
 cfg=OOD_RUNCFG.read_text()
 checks += [
  {'name':'strict_2cm','pass':'success_threshold_m: 0.02' in cfg},
  {'name':'h10_timeout_2400','pass':'max_steps: 2400' in cfg},
  {'name':'policy_seed_20260728','pass':'policy_sampling_seed: 20260728' in cfg},
 ]
 summaries=[json.loads(x) for x in (BASELINE/'episode_summaries.jsonl').read_text().splitlines() if x.strip()]
 checks += [
  {'name':'baseline_150','actual':len(summaries),'pass':len(summaries)==150},
  {'name':'baseline_72_success','actual':sum(bool(x['success']) for x in summaries),'pass':sum(bool(x['success']) for x in summaries)==72},
  {'name':'baseline_78_failure','actual':sum(not bool(x['success']) for x in summaries),'pass':sum(not bool(x['success']) for x in summaries)==78},
  {'name':'baseline_all_strict_2cm','pass':all(abs(float(x['strict_success_threshold_m'])-.02)<1e-12 for x in summaries)},
 ]
 active=procs('[c]ollect_isaac_risk.py')+procs('[r]un_isaac_online_risk.py')+procs('[t]rain_isaac_topk8.py')
 checks.append({'name':'gpu_experiment_processes_absent','active':active,'pass':not active})
 result={'schema_version':'isaac_online_preflight_v1','pass':all(c['pass'] for c in checks),'checks':checks}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2,sort_keys=True));return 0 if result['pass'] else 2
if __name__=='__main__':raise SystemExit(main())
