from __future__ import annotations
import argparse,json,os
from pathlib import Path
from collections import Counter,defaultdict

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--dataset',required=True); ap.add_argument('--out',default=None); args=ap.parse_args(); rows=[json.loads(x) for x in Path(args.dataset).read_text().splitlines() if x.strip()]
 labels=Counter(r['label']['label'] for r in rows); bad=Counter(r['label'].get('bad_event_type') for r in rows); bytask=defaultdict(Counter)
 for r in rows: bytask[r['metadata']['task_name']][r['label']['label']]+=1
 rep={'num_samples':len(rows),'label_counts':dict(labels),'bad_event_types':dict(bad),'per_task':{k:dict(v) for k,v in bytask.items()}}
 out=Path(args.out or Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))/'asynchvla_ws/stage9_libero_pro_risk_data/reports/stage9_label_distribution_pilot.md'); out.write_text('# Stage 9 Label Distribution Pilot\n\n```json\n'+json.dumps(rep,indent=2)+'\n```\n'); print(out)
if __name__=='__main__': main()
