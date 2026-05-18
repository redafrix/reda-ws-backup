#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from collections import defaultdict
from pathlib import Path
import numpy as np
REDA_WS=Path('/media/rootalkhatib/My Passport/reda_ws'); CK=REDA_WS/'asynchvla_ws/outputs/checkpoints/stage4'; REP=REDA_WS/'asynchvla_ws/outputs/reports/stage4_calibration_comparison.md'
def cov(rows, key):
    if not rows: return None
    y=np.array([r['true'] for r in rows]); u=np.array([r[key] for r in rows]); return float(np.mean(y<=u))
def apply(split):
    preds=json.load(open(CK/split/'predictions.json'))['full']; calib=preds['calib']; res=np.array([r['true']-r['pred'] for r in calib]); eta=max(0,float(np.quantile(res,.9)))
    type_eta={}
    for t in sorted({r['candidate_type'] for r in calib}):
        rr=np.array([r['true']-r['pred'] for r in calib if r['candidate_type']==t]); type_eta[t]=max(0,float(np.quantile(rr,.9))) if len(rr) else eta
    cp=np.array([r['pred'] for r in calib]); qs=np.quantile(cp,[0,.33,.66,1.0]); bin_eta=[]
    for i in range(3):
        lo,hi=qs[i],qs[i+1]; rows=[r for r in calib if (r['pred']>=lo and (r['pred']<=hi if i==2 else r['pred']<hi))]; rr=np.array([r['true']-r['pred'] for r in rows]); bin_eta.append((float(lo),float(hi),max(0,float(np.quantile(rr,.9))) if len(rr) else eta))
    out={'split':split,'global_eta':eta,'type_eta':type_eta,'bin_eta':bin_eta,'parts':{}}
    for part,rows in preds.items():
        annotated=[]
        for r in rows:
            b=next((be for lo,hi,be in bin_eta if r['pred']>=lo and r['pred']<=hi),eta)
            annotated.append({**r,'global':r['pred']+eta,'type':r['pred']+type_eta.get(r['candidate_type'],eta),'bin':r['pred']+b})
        per_type={}
        for t in sorted({r['candidate_type'] for r in annotated}):
            rs=[r for r in annotated if r['candidate_type']==t]
            per_type[t]={'n':len(rs),'global':cov(rs,'global'),'type':cov(rs,'type'),'bin':cov(rs,'bin'),'mean_true':float(np.mean([r['true'] for r in rs])),'mean_pred':float(np.mean([r['pred'] for r in rs]))}
        out['parts'][part]={'n':len(annotated),'overall':{'global':cov(annotated,'global'),'type':cov(annotated,'type'),'bin':cov(annotated,'bin')},'per_candidate_type':per_type}
    return out
def main():
    splits=['id_task_split','holdout_libero_object','holdout_object_bowl']; results=[apply(s) for s in splits]
    lines=['# Stage 4 Calibration Comparison','','Methods: global 90% residual conformal; candidate-type conditional residual conformal for analysis; predicted-error-bin residual conformal using 3 calibration quantile bins. Quantile rater was not trained in this pilot; the three conformal variants are the implemented calibration comparison.','','```json',json.dumps(results,indent=2),'```']
    REP.write_text('\n'.join(lines)+'\n'); print('calibration_comparison_ok', REP)
if __name__=='__main__': main()
