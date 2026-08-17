#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

def main()->int:
 p=argparse.ArgumentParser(); p.add_argument('--grid',type=Path,required=True); p.add_argument('--summaries-dir',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
 grid=json.loads(a.grid.read_text()); rows=[]
 for v in grid['variants']:
  path=a.summaries_dir/f"{v['id']}.json"
  r=json.loads(path.read_text()); r['main_threshold_name']=v['main_threshold']; r['selected_cap_name']=v['selected_cap']; rows.append(r)
 rows.sort(key=lambda r:(-int(r['online_successes']),int(r['regressions']),int(r['changed_episodes']),str(r['variant'])))
 best=rows[0]
 payload={'schema_version':'isaac_online_dev_selection_v1','selected_variant':best['variant'],'main_threshold_name':best['main_threshold_name'],'selected_cap_name':best['selected_cap_name'],'selection_key':['max_online_successes','min_regressions','min_changed_episodes','lexical_id'],'ranked_dev_results':rows}
 a.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n'); print(json.dumps(payload,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
