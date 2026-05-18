#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os
from pathlib import Path
import numpy as np
from calibration_methods import residual_eta, affine_fit, binned_residual
from calibration_metrics import coverage, risk_thresholds, bad_action_metrics

ROOT=Path(os.environ.get('REDA_WS','/media/rootalkhatib/My Passport/reda_ws'))
CK=ROOT/'asynchvla_ws/outputs/checkpoints/stage6'
OUT=ROOT/'asynchvla_ws/stage8_ultimate/reports'
SPLITS=['id_task_split','holdout_libero_object','holdout_object_bowl','holdout_libero_spatial','holdout_libero_goal','holdout_object_cabinet','holdout_scene_kitchen_scene2']
VARIANTS=['context_gated_action','action_only_baseline','full_old_baseline','full_engineered_simvla_focused']

def rows_for(split,variant):
    p=CK/split/variant/'predictions.json'
    if not p.exists(): return None
    return json.loads(p.read_text())

def xy(rows, simvla=False):
    if simvla: rows=[r for r in rows if str(r['candidate_type']).startswith('simvla_seed')]
    return np.array([float(r['pred']) for r in rows]), np.array([float(r['true']) for r in rows]), rows

def fmt(x): return 'n/a' if x is None else f'{x:.3f}' if isinstance(x,float) else str(x)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--target-coverage',type=float,default=0.9); args=ap.parse_args()
    q=args.target_coverage; OUT.mkdir(parents=True,exist_ok=True)
    all_results=[]
    lines=['# Stage 8 Calibration Sweep Summary','','Zero-shot means calibrators are fitted on the split calibration set only. No test labels are used.','']
    lines += ['| Split | Variant | Eval | Method | N | Coverage | Width | AUROC bad | Accepted50 true | Rejected50 true |','|---|---|---|---|---:|---:|---:|---:|---:|---:|']
    for split in SPLITS:
        for var in VARIANTS:
            pred=rows_for(split,var)
            if not pred or 'calib' not in pred: continue
            for simcal,name_suffix in [(False,'all'),(True,'simvla')]:
                pc,yc,_=xy(pred['calib'],simvla=simcal)
                if len(pc)==0: continue
                eta=residual_eta(pc,yc,q) or 0.0
                a,b=affine_fit(pc,yc)
                bins=binned_residual(pc,yc,5,q)
                for part in ['test_id','test_ood']:
                    if part not in pred: continue
                    for simeval, eval_name in [(False,part+'_all'),(True,part+'_simvla')]:
                        pe,ye,erows=xy(pred[part],simvla=simeval)
                        if len(pe)==0: continue
                        methods=[]
                        methods.append((f'global_residual_{name_suffix}', pe, eta))
                        methods.append((f'affine_plus_residual_{name_suffix}', a*pe+b, residual_eta(a*pc+b,yc,q) or 0.0))
                        # binned bound directly represented as per-row bound; summarize coverage manually
                        for mname,score,meta_eta in methods:
                            cov=coverage(score,ye,meta_eta); bad=bad_action_metrics(score,ye); risk=risk_thresholds(score,ye)[2]
                            row={'split':split,'variant':var,'eval':eval_name,'method':mname,**cov,**bad,'risk50':risk}
                            all_results.append(row)
                            lines.append(f"| `{split}` | `{var}` | `{eval_name}` | `{mname}` | {cov['n']} | {fmt(cov['coverage'])} | {fmt(cov['mean_width'])} | {fmt(bad['auroc'])} | {fmt(risk['accepted_mean_true'])} | {fmt(risk['rejected_mean_true'])} |")
    (OUT/'stage8_calibration_sweep_summary.json').write_text(json.dumps(all_results,indent=2))
    (OUT/'stage8_calibration_sweep_summary.md').write_text('\n'.join(lines)+'\n')
    for name,title in [('stage8_calibration_by_domain.md','Stage 8 Calibration By Domain'),('stage8_calibration_threshold_transfer.md','Stage 8 Calibration Threshold Transfer'),('stage8_calibration_best_method.md','Stage 8 Calibration Best Method')]:
        p=OUT/name
        if name.endswith('best_method.md'):
            best=sorted([r for r in all_results if r.get('coverage') is not None], key=lambda r:(abs(0.9-r['coverage']), r.get('mean_width') or 999))[:10]
            body='\n'.join([f"- `{r['split']}` `{r['variant']}` `{r['eval']}` `{r['method']}` coverage={r['coverage']:.3f} width={r['mean_width']:.3f}" for r in best])
        else:
            body='See `stage8_calibration_sweep_summary.md/json` for full tables. LIBERO-PRO calibration entries will appear after rollout/progress predictions are produced.'
        p.write_text(f'# {title}\n\n{body}\n')
    print(OUT/'stage8_calibration_sweep_summary.md')
if __name__=='__main__': main()
