#!/usr/bin/env python3
from __future__ import annotations
import csv, json
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

CAL_ROOT = Path('/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610/runs')
TEST_ROOT = Path('/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622')
TEST_SCORES = Path('/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626/scores.npz')
OUT = Path('/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260629_distinct_ood_calibration')


def read_jsonl(p):
    with open(p) as f:
        for line in f:
            if line.strip(): yield json.loads(line)


def load_calib():
    eps = {}
    rows = []
    for tdir in sorted(CAL_ROOT.glob('task*')):
        root = tdir/'risk_topk8_selected_cap/risk_topk8'
        sp = root/'episode_summaries.jsonl'
        rp = root/'step_scores_risk_topk8.jsonl'
        if not sp.exists() or not rp.exists(): continue
        for r in read_jsonl(sp):
            eid=str(r.get('episode_uid') or r.get('episode_id'))
            eps[eid]={'success': bool(r.get('success')), 'steps': int(r.get('num_steps') or 0), 'task_id': int(r.get('task_id', -1)), 'reset_seed': r.get('reset_seed')}
        for r in read_jsonl(rp):
            eid=str(r.get('episode_uid') or r.get('episode_id'))
            if eid not in eps: continue
            rows.append({'episode_id':eid,'task_id':int(r.get('task_id',eps[eid]['task_id'])),'timestep':int(r.get('timestep') or 0),'score':float(r.get('main_score')),'y':0 if eps[eid]['success'] else 1})
    return eps, rows


def load_test(cap300=False):
    eps={}
    for r in read_jsonl(TEST_ROOT/'episode_summaries.jsonl'):
        eid=str(r.get('episode_id') or r.get('episode_uid'))
        success=bool(r.get('success'))
        steps=int(r.get('steps') or r.get('num_steps') or r.get('num_env_steps') or 0)
        if cap300 and steps>=300:
            success=False; steps=300
        eps[eid]={'success':success,'steps':steps,'task_id':int(r.get('task_id',-1))}
    full_rows=[]
    for r in read_jsonl(TEST_ROOT/'fiper_receding_samples.jsonl'):
        eid=str(r.get('episode_id') or r.get('episode_uid'))
        if eid not in eps: continue
        t=int(r.get('timestep') or 0)
        full_rows.append({'episode_id':eid,'task_id':int(r.get('task_id',eps[eid]['task_id'])),'timestep':t,'y':0 if eps[eid]['success'] else 1})
    scores=np.load(TEST_SCORES)['scores'].astype(float)
    if len(scores)!=len(full_rows): raise RuntimeError((len(scores),len(full_rows)))
    if cap300:
        keep=np.array([not (eps[r['episode_id']]['steps']==300 and r['timestep']>=300) for r in full_rows], dtype=bool)
        rows=[r for r,k in zip(full_rows,keep) if k]
        scores=scores[keep]
    else:
        rows=full_rows
    for r,s in zip(rows,scores): r['score']=float(s)
    return eps, rows


def group(rows):
    g=defaultdict(list)
    for r in rows: g[r['episode_id']].append(r)
    for v in g.values(): v.sort(key=lambda x:x['timestep'])
    return g


def final_masses(rows, row_th):
    out=defaultdict(float)
    for r in rows: out[r['episode_id']]+=max(0.0, r['score']-row_th)
    return dict(out)


def eval_policy(rows, row_th, mass_th):
    g=group(rows)
    succ=fail=fa=det=det10=det25=det50=0; times=[]
    for eid, vals in g.items():
        y=max(r['y'] for r in vals); last=max(1, vals[-1]['timestep'])
        mass=0; hit_i=None; hit_t=None
        for i,r in enumerate(vals):
            mass += max(0.0, r['score']-row_th)
            if hit_i is None and mass>=mass_th:
                hit_i=i; hit_t=r['timestep']
        if y:
            fail+=1
            if hit_i is not None:
                det+=1
                q=(hit_i+1)/max(1,len(vals)); times.append(hit_t/last)
                if q<=.10: det10+=1
                if q<=.25: det25+=1
                if q<=.50: det50+=1
        else:
            succ+=1
            if hit_i is not None: fa+=1
    return {'success_episodes':succ,'failure_episodes':fail,'success_fa':fa/max(1,succ),'failure_det':det/max(1,fail),'det_at_10':det10/max(1,fail),'det_at_25':det25/max(1,fail),'det_at_50':det50/max(1,fail),'mean_time':float(np.mean(times)) if times else None,'never':1-det/max(1,fail),'false_alarms':fa,'detected_failures':det}

def fmt(x): return 'NA' if x is None else f'{100*x:.1f}%'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cal_eps, cal_rows=load_calib()
    cal_success=[r for r in cal_rows if r['y']==0]
    cal_failure=[r for r in cal_rows if r['y']==1]
    # Row thresholds chosen from calibration success rows, not test.
    row_thresholds={f'cal_q{int(q*100)}':float(np.quantile([r['score'] for r in cal_success],q)) for q in [.95,.97,.99,.995]}
    policies=[]
    for rn,rt in row_thresholds.items():
        succ_m=np.array(list(final_masses(cal_success,rt).values()),float)
        fail_m=np.array(list(final_masses(cal_failure,rt).values()),float)
        grid=np.unique(np.concatenate([np.quantile(succ_m,np.linspace(0,1,501)),np.quantile(fail_m,np.linspace(0,1,501)),[0.15,.5,1,2,5,10,20,30,50,75,100,150,200]]))
        # success-only conformal operating points
        for target in [.50,.40,.30,.25,.20,.15,.10,.05,.025,.01]:
            mt=float(np.quantile(succ_m,1-target))
            policies.append({'policy':f'{rn}_oodcal_success_FA{int(target*100):02d}','row_threshold':rt,'mass_threshold':mt,'calib_success':eval_policy(cal_rows,rt,mt)})
        # supervised calibration using distinct OOD failures too
        for maxfa in [.50,.40,.30,.25,.20,.15,.10,.05]:
            best=None
            for mt in grid:
                m=eval_policy(cal_rows,rt,float(mt)); score=(m['failure_det']-m['success_fa'],m['failure_det'],-(m['mean_time'] or 999),-m['success_fa'])
                if m['success_fa']<=maxfa and (best is None or score>best[0]): best=(score,float(mt),m)
            if best:
                policies.append({'policy':f'{rn}_oodcal_supervised_FAle{int(maxfa*100):02d}','row_threshold':rt,'mass_threshold':best[1],'calib_success':best[2]})
    outputs={}
    for style,cap in [('actual_max800',False),('cap300_forensic',True)]:
        teps,trows=load_test(cap)
        rows=[]
        for p in policies:
            m=eval_policy(trows,p['row_threshold'],p['mass_threshold'])
            rows.append({**p,'test':m})
        rows=sorted(rows,key=lambda r:(r['test']['failure_det']-r['test']['success_fa'],r['test']['failure_det'],-r['test']['success_fa']), reverse=True)
        outputs[style]={'n_rows':len(trows),'n_episodes':len(group(trows)),'results':rows}
        with open(OUT/f'{style}_distinct_oodcal_metrics.csv','w',newline='') as f:
            w=csv.writer(f); w.writerow(['Policy','Row_Threshold','Mass_Threshold','Calib_FA','Calib_Det','Test_FA','Test_Det','Det@10','Det@25','Det@50','Mean_Time','Never'])
            for r in rows:
                c=r['calib_success']; m=r['test']
                w.writerow([r['policy'],r['row_threshold'],r['mass_threshold'],c['success_fa'],c['failure_det'],m['success_fa'],m['failure_det'],m['det_at_10'],m['det_at_25'],m['det_at_50'],m['mean_time'],m['never']])
    (OUT/'distinct_oodcal_results.json').write_text(json.dumps(outputs,indent=2,sort_keys=True)+'\n')
    lines=['# H10 TopK8 Distinct-OOD Calibration Applied to OOD180','', 'Calibration source: `selected_cap_t03_c04_100ep_20260610` risk TopK8 step scores, 1800 episodes, distinct from OOD180 test. This is not seen-only; it is an OOD calibration split with different episodes/seeds.']
    for style in ['actual_max800','cap300_forensic']:
        lines += ['',f'## {style}','','| Policy | Row Th | Mass Th | Calib FA | Calib Det | Test FA | Test Det | Det@25 | Det@50 | Mean Time | Never |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
        keep=[]
        for maxfa in [.50,.30,.20,.10,.05]:
            elig=[r for r in outputs[style]['results'] if r['test']['success_fa']<=maxfa]
            if elig:
                b=max(elig,key=lambda r:(r['test']['failure_det']-r['test']['success_fa'],r['test']['failure_det'],-r['test']['success_fa']))
                if b not in keep: keep.append(b)
        keep += outputs[style]['results'][:8]
        seen=set()
        for r in keep:
            if r['policy'] in seen: continue
            seen.add(r['policy']); c=r['calib_success']; m=r['test']; mt='NA' if m['mean_time'] is None else f"{m['mean_time']:.3f}"
            lines.append(f"| {r['policy']} | {r['row_threshold']:.4f} | {r['mass_threshold']:.4f} | {fmt(c['success_fa'])} | {fmt(c['failure_det'])} | {fmt(m['success_fa'])} | {fmt(m['failure_det'])} | {fmt(m['det_at_25'])} | {fmt(m['det_at_50'])} | {mt} | {fmt(m['never'])} |")
    (OUT/'H10_TOPK8_DISTINCT_OOD_CALIBRATION_ON_OOD180_20260629.md').write_text('\n'.join(lines)+'\n')
    print(OUT/'H10_TOPK8_DISTINCT_OOD_CALIBRATION_ON_OOD180_20260629.md')

if __name__=='__main__': main()
