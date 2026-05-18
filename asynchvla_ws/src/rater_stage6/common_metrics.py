from __future__ import annotations
from collections import defaultdict
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import roc_auc_score

def is_simvla(t): return str(t).startswith('simvla_seed')

def safe_corr(fn, x, y):
    if len(x) < 3 or np.std(x) < 1e-9 or np.std(y) < 1e-9: return None
    return float(fn(x, y).statistic)

def risk_coverage(y, p):
    order=np.argsort(p); out=[]
    for c in [0.10,0.25,0.50,0.75,1.0]:
        n=max(1,int(round(len(y)*c))); keep=order[:n]
        out.append({'coverage':c,'mean_true_error':float(np.mean(y[keep]))})
    return out

def switch_proxy(rows, preds):
    y=np.array([r['true_chunk_l2_error'] for r in rows], dtype=float); p=np.array(preds,dtype=float)
    out=[]
    for rej in [0.10,0.25,0.50,0.75]:
        thr=np.quantile(p,1-rej); acc=p<=thr; rejmask=~acc
        out.append({'reject_rate':rej,'threshold':float(thr),'accepted_n':int(acc.sum()),'rejected_n':int(rejmask.sum()),'accepted_mean_error':float(y[acc].mean()) if acc.any() else None,'rejected_mean_error':float(y[rejmask].mean()) if rejmask.any() else None,'gap_rejected_minus_accepted':float(y[rejmask].mean()-y[acc].mean()) if acc.any() and rejmask.any() else None})
    return out

def all_candidate_metrics(rows, preds):
    y=np.array([r['true_chunk_l2_error'] for r in rows], dtype=float); p=np.array(preds,dtype=float)
    labels=(y>=np.quantile(y,.7)).astype(int) if len(y) else np.array([])
    by=defaultdict(dict)
    for r,pp in zip(rows,p): by[r['context_id']][r['candidate_type']] = (float(pp), float(r['true_chunk_l2_error']))
    def acc(a,b):
        n=o=0
        for d in by.values():
            if a in d and b in d:
                n+=1
                if d[a][0] < d[b][0]: o+=1
                elif d[a][0] == d[b][0]: o+=0.5
        return o/n if n else None
    stds=[np.std([v[0] for v in d.values()]) for d in by.values() if len(d)>1]
    return {'n':len(rows),'pearson':safe_corr(pearsonr,p,y),'spearman':safe_corr(spearmanr,p,y),'auroc_top30_bad':float(roc_auc_score(labels,p)) if len(set(labels.tolist()))==2 and np.std(p)>1e-9 else None,'mae':float(np.mean(np.abs(p-y))) if len(y) else None,'mse':float(np.mean((p-y)**2)) if len(y) else None,'expert_lt_perturb_large':acc('expert_action','perturb_large'),'expert_lt_other_task':acc('expert_action','other_demo_or_other_task'),'expert_lt_simvla_seed0':acc('expert_action','simvla_seed0'),'same_context_pred_std':float(np.mean(stds)) if stds else None,'risk_coverage':risk_coverage(y,p) if len(y) else []}

def simvla_only_metrics(rows, preds):
    pairs=[(r,float(pp)) for r,pp in zip(rows,preds) if is_simvla(r['candidate_type'])]
    if not pairs: return {'n':0}
    srows=[r for r,_ in pairs]; p=np.array([pp for _,pp in pairs]); y=np.array([r['true_chunk_l2_error'] for r in srows], dtype=float)
    labels=(y>=np.quantile(y,.7)).astype(int)
    by=defaultdict(list)
    for r,pp in pairs: by[r['context_id']].append((r,pp))
    pair_ok=pair_n=0; seed0=[]; predbest=[]; oracle=[]; random=[]
    rng=np.random.default_rng(0)
    for ctx,items in by.items():
        items=sorted(items, key=lambda x:x[0]['candidate_type'])
        true=np.array([it[0]['true_chunk_l2_error'] for it in items]); pred=np.array([it[1] for it in items])
        for i in range(len(items)):
            for j in range(i+1,len(items)):
                dt=true[i]-true[j]; dp=pred[i]-pred[j]
                if abs(dt)<1e-9: pair_ok += 0.5
                elif abs(dp)<1e-9: pair_ok += 0.5
                else: pair_ok += float(np.sign(dt)==np.sign(dp))
                pair_n += 1
        seed0.append(next((it[0]['true_chunk_l2_error'] for it in items if it[0]['candidate_type']=='simvla_seed0'), true[0]))
        predbest.append(true[int(np.argmin(pred))]); oracle.append(float(true.min())); random.append(float(true[rng.integers(0,len(true))]))
    return {'n':len(srows),'contexts':len(by),'pearson':safe_corr(pearsonr,p,y),'spearman':safe_corr(spearmanr,p,y),'auroc_top30_worst':float(roc_auc_score(labels,p)) if len(set(labels.tolist()))==2 and np.std(p)>1e-9 else None,'pairwise_seed_ranking':pair_ok/pair_n if pair_n else None,'predicted_best_mean_error':float(np.mean(predbest)),'seed0_mean_error':float(np.mean(seed0)),'random_seed_mean_error':float(np.mean(random)),'oracle_best_mean_error':float(np.mean(oracle)),'improvement_over_seed0':float(np.mean(seed0)-np.mean(predbest)),'gap_to_oracle':float(np.mean(predbest)-np.mean(oracle)),'risk_coverage':risk_coverage(y,p),'switch_proxy_all_simvla':switch_proxy(srows,p),'switch_proxy_seed0':switch_proxy([r for r in srows if r['candidate_type']=='simvla_seed0'], [pp for r,pp in pairs if r['candidate_type']=='simvla_seed0'])}
