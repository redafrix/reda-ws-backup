from __future__ import annotations
import numpy as np


def residual_eta(pred, true, q=0.9):
    pred=np.asarray(pred,dtype=float); true=np.asarray(true,dtype=float)
    if len(pred)==0: return None
    return float(np.quantile(true-pred, q))


def affine_fit(pred, true):
    pred=np.asarray(pred,dtype=float); true=np.asarray(true,dtype=float)
    if len(pred)<2 or np.std(pred)<1e-9: return (1.0, residual_eta(pred,true,0.5) or 0.0)
    a,b=np.polyfit(pred,true,1)
    return float(a), float(b)


def binned_residual(pred, true, bins=5, q=0.9):
    pred=np.asarray(pred,dtype=float); true=np.asarray(true,dtype=float)
    if len(pred)==0: return []
    edges=np.quantile(pred, np.linspace(0,1,bins+1))
    out=[]
    global_eta=residual_eta(pred,true,q) or 0.0
    for i in range(bins):
        lo,hi=edges[i],edges[i+1]
        mask=(pred>=lo) & ((pred<=hi) if i==bins-1 else (pred<hi))
        eta=residual_eta(pred[mask], true[mask], q) if mask.any() else global_eta
        out.append({'bin':i,'lo':float(lo),'hi':float(hi),'eta':float(eta if eta is not None else global_eta),'n':int(mask.sum())})
    return out
