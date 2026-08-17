#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--grid',type=Path,required=True); ap.add_argument('--summaries-dir',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    grid=json.loads(a.grid.read_text()); rows=[]
    for v in grid['variants']:
        r=json.loads((a.summaries_dir/f"{v['id']}.json").read_text())
        if int(r['episodes'])!=150: raise RuntimeError(f"{v['id']} is not a complete 150-episode result")
        if int(r['baseline_successes'])!=72: raise RuntimeError(f"{v['id']} baseline pairing is not the locked 72/150 baseline")
        r['main_threshold_name']=v['main_threshold']; r['selected_cap_name']=v['selected_cap']; rows.append(r)
    rows.sort(key=lambda r:(-int(r['online_successes']),int(r['regressions']),int(r['changed_episodes']),str(r['variant'])))
    best=rows[0]
    payload={
      'schema_version':'isaac_online_full150_selection_v1',
      'selection_scope':'same_complete_locked_ood150_used_for_all_predeclared_variants',
      'historical_locked_baseline_successes':72,
      'historical_locked_baseline_failures':78,
      'selected_variant':best['variant'],
      'main_threshold_name':best['main_threshold_name'],
      'selected_cap_name':best['selected_cap_name'],
      'best_online_successes':int(best['online_successes']),
      'best_online_failures':150-int(best['online_successes']),
      'net_success_delta_vs_historical_baseline':int(best['online_successes'])-72,
      'selection_key':['max_online_successes','min_regressions_vs_historical_locked_baseline','min_changed_episodes','lexical_id'],
      'ranked_full150_results':rows,
      'reporting_note':'Threshold/controller pair is selected on the same OOD150 campaign; headline result is the best predefined seen-derived operating point on OOD150, not an untouched holdout estimate.'
    }
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n'); print(json.dumps(payload,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
