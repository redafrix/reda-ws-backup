#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

def main()->int:
 p=argparse.ArgumentParser(); p.add_argument('--dev',type=Path,required=True); p.add_argument('--holdout',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
 d=json.loads(a.dev.read_text()); h=json.loads(a.holdout.read_text())
 if d['variant']!=h['variant']: raise RuntimeError('variant mismatch')
 keys=['episodes','baseline_successes','online_successes','rescues','regressions','unchanged_successes','unchanged_failures','net_success_delta','action_modifications','changed_episodes']
 out={'schema_version':'isaac_online_selected_full150_secondary_v1','variant':d['variant'],'interpretation':'secondary descriptive full150 result; dev40 was used to select the controller variant, so heldout110 is the unbiased primary result'}
 for k in keys: out[k]=int(d[k])+int(h[k])
 out['baseline_success_rate']=out['baseline_successes']/out['episodes']; out['online_success_rate']=out['online_successes']/out['episodes']
 a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
