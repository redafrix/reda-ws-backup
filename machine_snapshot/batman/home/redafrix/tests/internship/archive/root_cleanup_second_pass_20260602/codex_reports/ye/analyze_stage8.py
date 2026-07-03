from __future__ import annotations
import json, re, math
from pathlib import Path
from statistics import mean
ROOT=Path('/home/redafrix/tests/internship/codex_reports/ye')
BOB=ROOT/'bob_bundle/asynchvla_ws/stage8_ultimate/reports'
SAM=ROOT/'sam_bundle/asynchvla_ws/stage8_ultimate/reports'

def parse_md_table(path):
    text=Path(path).read_text(errors='replace')
    rows=[]; header=None
    for line in text.splitlines():
        if not line.startswith('|'): continue
        cells=[c.strip().strip('`') for c in line.strip().strip('|').split('|')]
        if not cells: continue
        if all(set(c)<=set('-: ') for c in cells): continue
        if header is None and 'suite' in cells and 'mode' in cells:
            header=cells; continue
        if header and len(cells)==len(header):
            d=dict(zip(header,cells))
            rows.append(d)
    return rows

def num(x):
    try: return float(x)
    except: return math.nan

def rollout_summary(fname):
    rows=parse_md_table(BOB/fname)
    # keep first aggregate table until Episode Rows? parser also includes episode rows with different headers not because header fixed; ok
    # Weighted by episodes
    modes={}
    for r in rows:
        if 'success_rate' not in r: continue
        ep=num(r['episodes']); mode=r['mode']
        modes.setdefault(mode, {'episodes':0,'succ':0,'steps':0,'unc':0,'rejects':0,'tasks':0,'minsucc':1,'maxsucc':0})
        m=modes[mode]; m['episodes']+=ep; m['succ']+=ep*num(r['success_rate']); m['steps']+=ep*num(r['avg_steps']); m['unc']+=ep*num(r['avg_unc']); m['rejects']+=ep*num(r['avg_rejects']); m['tasks']+=1; m['minsucc']=min(m['minsucc'],num(r['success_rate'])); m['maxsucc']=max(m['maxsucc'],num(r['success_rate']))
    out={}
    for k,m in modes.items():
        ep=m['episodes'] or 1
        out[k]={'episodes':int(ep),'tasks':m['tasks'],'success_rate':m['succ']/ep,'avg_steps':m['steps']/ep,'avg_unc':m['unc']/ep,'avg_rejects':m['rejects']/ep,'min_task_success':m['minsucc'],'max_task_success':m['maxsucc']}
    # worst tasks for A passive
    worst=[]
    for r in rows:
        if r.get('mode')=='A_passive' and 'success_rate' in r:
            worst.append((num(r['success_rate']), num(r['avg_steps']), r.get('suite'), r.get('task'), r))
    worst=sorted(worst)[:10]
    best_delta=[]
    # compare modes by suite/task
    by={}
    for r in rows:
        if 'success_rate' in r:
            by.setdefault((r['suite'],r['task']),{})[r['mode']]=r
    for key,d in by.items():
        if 'A_passive' in d:
            a=d['A_passive']
            for mode in ['B_deliberation','C_random_seed','E_conservative_switch_proxy']:
                if mode in d:
                    best_delta.append((num(d[mode]['success_rate'])-num(a['success_rate']), num(a['avg_steps'])-num(d[mode]['avg_steps']), key, mode, d[mode], a))
    return out,worst,sorted(best_delta, reverse=True)[:10], sorted(best_delta)[:10]

def sim_metrics_from_json(path):
    d=json.loads(Path(path).read_text())
    results=d.get('results') or d.get('variants') or []
    out=[]
    for res in results:
        var=res.get('variant')
        for part in ['test_ood','test_id']:
            sm=((res.get('metrics') or {}).get(part) or {}).get('simvla_only')
            allm=((res.get('metrics') or {}).get(part) or {}).get('all_candidate')
            if sm:
                out.append({'split':d.get('split'), 'variant':var, 'part':part,
                    'pairwise':sm.get('pairwise_seed_ranking'), 'improve':sm.get('improvement_over_seed0'),
                    'pred_best':sm.get('predicted_best_mean_error'), 'seed0':sm.get('seed0_mean_error'),
                    'oracle':sm.get('oracle_best_mean_error'), 'auroc':sm.get('auroc_top30_worst'),
                    'spearman':sm.get('spearman'), 'all_auroc': allm.get('auroc_top30_bad') if allm else None})
    return out

def collect_models():
    rows=[]
    for p in SAM.glob('stage8_big_arch_*.json'):
        rows += sim_metrics_from_json(p)
    for p in SAM.glob('stage7_flowtrace_*.json'):
        for r in sim_metrics_from_json(p): r['source']='flowtrace'; rows.append(r)
    q=SAM/'stage8_quantile_head_results.json'
    if q.exists():
        d=json.loads(q.read_text())
        for split,arr in d.get('splits',{}).items():
            for res in arr:
                for part in ['test_ood','test_id']:
                    sm=((res.get('metrics') or {}).get(part) or {}).get('simvla_only')
                    if sm:
                        rows.append({'split':split,'variant':res.get('variant'),'part':part,'pairwise':sm.get('pairwise_seed_ranking'),'improve':sm.get('improvement_over_seed0'),'pred_best':sm.get('predicted_best_mean_error'),'seed0':sm.get('seed0_mean_error'),'oracle':sm.get('oracle_best_mean_error'),'auroc':sm.get('auroc_top30_worst'),'spearman':sm.get('spearman'),'source':'quantile'})
    return rows

def summarize_models(rows):
    # best per split-part by pairwise and by improvement
    best_pair={}; best_imp={}
    for r in rows:
        key=(r['split'],r['part'])
        if r.get('pairwise') is not None and (key not in best_pair or r['pairwise']>best_pair[key]['pairwise']): best_pair[key]=r
        if r.get('improve') is not None and (key not in best_imp or r['improve']>best_imp[key]['improve']): best_imp[key]=r
    return best_pair,best_imp

def calibration_summary():
    p=SAM/'stage8_calibration_real_q0.90.json'
    if not p.exists(): return []
    arr=json.loads(p.read_text())
    # select simvla evals, context_gated, methods
    rows=[]
    for r in arr:
        if r.get('eval','').endswith('simvla') and r.get('variant')=='context_gated_action':
            rows.append({k:r.get(k) for k in ['split','eval','method','n','coverage','mean_width','auroc','brier']})
    return rows

lib_sum,lib_worst,lib_best,lib_bad=rollout_summary('stage8_libero_pro_expanded_rollout_results.md')
hard_sum,hard_worst,hard_best,hard_bad=rollout_summary('stage8_normal_libero_hard_task_results.md')
models=collect_models(); bp,bi=summarize_models(models)
cal=calibration_summary()
summary={'libero_pro_mode_summary':lib_sum,'libero_pro_worst_A':lib_worst[:8], 'libero_pro_best_deltas':lib_best[:8], 'libero_pro_bad_deltas':lib_bad[:8], 'hard_mode_summary':hard_sum,'hard_worst_A':hard_worst[:8], 'hard_best_deltas':hard_best[:8], 'hard_bad_deltas':hard_bad[:8], 'best_pairwise':{str(k):v for k,v in bp.items()}, 'best_improvement':{str(k):v for k,v in bi.items()}, 'calibration_context_gated_q90_simvla':cal, 'model_row_count':len(models)}
(ROOT/'parsed_summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2)[:20000])
