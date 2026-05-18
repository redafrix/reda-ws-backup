from __future__ import annotations
import argparse,json,os
from pathlib import Path
from collections import Counter,defaultdict

def load_samples(path):
    p=Path(path)
    if p.suffix=='.jsonl':
        return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
    return json.loads(p.read_text()).get('samples',[])

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--dataset',required=True); ap.add_argument('--out',default=None); args=ap.parse_args(); rows=load_samples(args.dataset)
 labels=Counter(r.get('label',{}).get('label') or r.get('label') for r in rows); bad=Counter((r.get('label',{}) or {}).get('bad_event_type') for r in rows); conf=Counter((r.get('label',{}) or {}).get('label_confidence') for r in rows)
 suspicious=[]
 for r in rows:
   lab=(r.get('label',{}) or {}).get('label'); outc=r.get('outcome',{}); rew=float(outc.get('reward_sum_H',0)); succ=bool(outc.get('success_within_H') or outc.get('success_after'))
   if lab=='BAD' and (succ or rew>0): suspicious.append({'sample_id':r.get('sample_id'),'why':'BAD_but_success_or_reward','reward':rew,'success':succ})
   if lab=='GOOD' and rew==0 and not succ: suspicious.append({'sample_id':r.get('sample_id'),'why':'GOOD_but_no_reward_success'})
 rep={'num_samples':len(rows),'labels':labels,'bad_event_types':bad,'confidence':conf,'suspicious_count':len(suspicious),'suspicious_examples':suspicious[:50]}
 out=Path(args.out or Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))/'asynchvla_ws/stage9_libero_pro_risk_data/reports/stage9_label_consistency_audit.md'); out.write_text('# Stage 9 Label Consistency Audit\n\n```json\n'+json.dumps(rep,indent=2,default=str)+'\n```\n'); print(out)
if __name__=='__main__': main()
