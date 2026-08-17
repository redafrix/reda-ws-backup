#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

def load_jsonl(path:Path): return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument('--baseline',type=Path,required=True); p.add_argument('--online',type=Path,required=True); p.add_argument('--output',type=Path,required=True); p.add_argument('--variant',required=True); a=p.parse_args()
 base={int(r['source_episode_id']):r for r in load_jsonl(a.baseline)}
 online=load_jsonl(a.online)
 if not online: raise RuntimeError('online summary empty')
 resc=[]; regs=[]; both_s=[]; both_f=[]; mods=0; changed=0
 for r in online:
  sid=int(r['source_episode_id']); b=base[sid]
  if bool(r['success']) and not bool(b['success']): resc.append(sid)
  elif not bool(r['success']) and bool(b['success']): regs.append(sid)
  elif bool(r['success']) and bool(b['success']): both_s.append(sid)
  else: both_f.append(sid)
  m=int(r.get('online_action_modifications_count',0)); mods+=m; changed+=int(m>0)
 result={
  'schema_version':'isaac_online_paired_summary_v1','variant':a.variant,'episodes':len(online),
  'baseline_successes':sum(bool(base[int(r['source_episode_id'])]['success']) for r in online),
  'online_successes':sum(bool(r['success']) for r in online),
  'rescues':len(resc),'regressions':len(regs),'unchanged_successes':len(both_s),'unchanged_failures':len(both_f),
  'net_success_delta':len(resc)-len(regs),'action_modifications':mods,'changed_episodes':changed,
  'rescue_source_episode_ids':resc,'regression_source_episode_ids':regs,
 }
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps(result,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
