from __future__ import annotations
import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss


def coverage(pred, true, eta):
    pred=np.asarray(pred,dtype=float); true=np.asarray(true,dtype=float)
    bound=pred+float(eta)
    return {'n':int(len(pred)),'coverage':float(np.mean(true<=bound)) if len(pred) else None,'mean_width':float(np.mean(bound-pred)) if len(pred) else None,'median_width':float(np.median(bound-pred)) if len(pred) else None,'mean_true':float(np.mean(true)) if len(pred) else None,'mean_pred':float(np.mean(pred)) if len(pred) else None}


def risk_thresholds(score, true):
    score=np.asarray(score,dtype=float); true=np.asarray(true,dtype=float)
    rows=[]
    for accept in [0.9,0.75,0.5,0.25]:
        thr=float(np.quantile(score, accept))
        mask=score<=thr
        rows.append({'accept_rate':accept,'threshold':thr,'accepted_n':int(mask.sum()),'rejected_n':int((~mask).sum()),'accepted_mean_true':float(true[mask].mean()) if mask.any() else None,'rejected_mean_true':float(true[~mask].mean()) if (~mask).any() else None})
    return rows


def bad_action_metrics(score,true,quantile=0.7):
    score=np.asarray(score,dtype=float); true=np.asarray(true,dtype=float)
    y=(true>=np.quantile(true,quantile)).astype(int)
    if len(set(y.tolist()))<2 or np.std(score)<1e-9: return {'auroc':None,'auprc':None,'brier':None}
    s=(score-score.min())/(score.max()-score.min()+1e-9)
    return {'auroc':float(roc_auc_score(y,score)),'auprc':float(average_precision_score(y,score)),'brier':float(brier_score_loss(y,s))}
