#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,random,time,sys,os
from collections import defaultdict
from pathlib import Path
import numpy as np, torch, torch.nn as nn
REDA_WS=Path(os.environ.get('REDA_WS', '/media/rootalkhatib/My Passport/reda_ws')); sys.path.insert(0,str(REDA_WS/'asynchvla_ws/src'))
from features_stage6.build_features import build_seed_stats, feature_vector, is_simvla_type
from rater_stage6.common_metrics import all_candidate_metrics, simvla_only_metrics
from rater_stage6.models import MLPRegressor, ContextGatedActionFixed, PerStepHead, HeteroscedasticHead
DATA_ROOT=REDA_WS/'asynchvla_ws/data/processed_stage5'; CKROOT=REDA_WS/'asynchvla_ws/outputs/checkpoints/stage6'; RROOT=REDA_WS/'asynchvla_ws/outputs/reports/stage6'
VARIANTS={
 'action_only_baseline':('A0_action_flat','mlp','mixed'),
 'context_only_baseline':('A1_context','mlp','mixed'),
 'full_old_baseline':('A2_full_old','mlp','mixed'),
 'full_engineered_mlp':('M2_engineered','mlp_big','mixed'),
 'seed_relative_rater':('M4_seed_relative','mlp_big','mixed'),
 'seed_relative_pairwise':('M4_seed_relative','mlp_big_pairwise','mixed'),
 'context_gated_action':('M3_gated_base','gated','mixed'),
 'per_step_error_head':('M4_seed_relative','perstep','mixed'),
 'heteroscedastic_head':('M4_seed_relative','hetero','mixed'),
 'heteroscedastic_simvla_focused':('M4_seed_relative','hetero','simvla_focused'),
 'seed_relative_simvla_focused':('M4_seed_relative','mlp_big_pairwise','simvla_focused'),
 'full_engineered_simvla_focused':('M2_engineered','mlp_big','simvla_focused'),
}
def load_part(split,part):
    p=DATA_ROOT/split/f'multiseed_candidate_{part}.pt'
    return torch.load(p,map_location='cpu')['candidates'] if p.exists() else []
def subset_train(rows, setting):
    if setting!='simvla_focused': return rows
    sim=[r for r in rows if is_simvla_type(r['candidate_type'])]; other=[r for r in rows if not is_simvla_type(r['candidate_type'])]
    rng=random.Random(42); rng.shuffle(other); return sim+other[:len(sim)]
def build_matrix(rows, mode, seed_stats):
    xs=[feature_vector(r,mode,seed_stats) for r in rows]
    y=torch.tensor([float(r['true_chunk_l2_error']) for r in rows],dtype=torch.float32)
    ystep=torch.stack([r['true_per_step_l2_error'].float() for r in rows])
    return torch.stack(xs),y,ystep
def standardize(xtr,*xs):
    mu=xtr.mean(0,keepdim=True); sd=xtr.std(0,keepdim=True).clamp_min(1e-6); return [(x-mu)/sd for x in (xtr,*xs)],mu,sd
def model_for(kind,in_dim,context_dim=968):
    if kind=='mlp': return MLPRegressor(in_dim,hidden=256,depth=2).train()
    if kind in ('mlp_big','mlp_big_pairwise'): return MLPRegressor(in_dim,hidden=384,depth=3).train()
    if kind=='gated': return ContextGatedActionFixed(context_dim, in_dim-context_dim, hidden=384).train()
    if kind=='perstep': return PerStepHead(in_dim,hidden=384).train()
    if kind=='hetero': return HeteroscedasticHead(in_dim,hidden=384).train()
    raise KeyError(kind)
def predict(model,kind,x):
    with torch.no_grad():
        out=model(x)
        if kind=='perstep': return out.mean(1), out
        if kind=='hetero':
            mean,logvar=out; return mean + 0.0*torch.exp(0.5*logvar), None
        return out.squeeze(-1) if out.ndim>1 else out, None
def pairwise_loss_for_batch(pred, rows):
    by=defaultdict(list)
    for i,r in enumerate(rows):
        if is_simvla_type(r['candidate_type']): by[r['context_id']].append(i)
    losses=[]
    for inds in by.values():
        if len(inds)<2: continue
        for a in range(len(inds)):
            for b in range(a+1,len(inds)):
                i,j=inds[a],inds[b]
                ti,tj=rows[i]['true_chunk_l2_error'],rows[j]['true_chunk_l2_error']
                if abs(ti-tj)<1e-8: continue
                sign=1.0 if ti<tj else -1.0
                losses.append(torch.relu(0.02 - sign*(pred[j]-pred[i])))
    return torch.stack(losses).mean() if losses else pred.sum()*0
def train_variant(split, variant, epochs=120, quick=False):
    mode,kind,setting=VARIANTS[variant]; parts={p:load_part(split,p) for p in ['train','calib','test_id','test_ood']}; train_rows=subset_train(parts['train'],setting)
    all_seed_rows=[]
    for rs in parts.values(): all_seed_rows.extend(rs)
    seed_stats=build_seed_stats(all_seed_rows)
    xtr,ytr,ystep_tr=build_matrix(train_rows,mode,seed_stats); xcal,ycal,ystep_cal=build_matrix(parts['calib'],mode,seed_stats)
    (xtrn,xcaln),mu,sd=standardize(xtr,xcal); m=model_for(kind,xtr.shape[1]); opt=torch.optim.AdamW(m.parameters(),lr=2e-3,weight_decay=1e-4); hub=nn.HuberLoss(delta=.25); best=(1e9,None,0)
    batch=512 if not quick else 256; epochs=40 if quick else epochs; t0=time.time()
    for ep in range(1,epochs+1):
        perm=torch.randperm(len(xtrn)); m.train()
        for st in range(0,len(perm),batch):
            ix=perm[st:st+batch]; out=m(xtrn[ix])
            if kind=='perstep': pred=out.mean(1); loss=hub(out,ystep_tr[ix])+hub(pred,ytr[ix])
            elif kind=='hetero':
                mean,logvar=out; var=torch.exp(logvar).clamp_min(1e-4); loss=(0.5*((ytr[ix]-mean)**2/var+logvar)).mean()
            else: pred=out.squeeze(-1) if out.ndim>1 else out; loss=hub(pred,ytr[ix])
            if 'pairwise' in kind:
                pred_for_pair=out.squeeze(-1) if out.ndim>1 else out; loss=loss+0.25*pairwise_loss_for_batch(pred_for_pair,[train_rows[int(i)] for i in ix])
            opt.zero_grad(); loss.backward(); opt.step()
        pred,_=predict(m,kind,xcaln); vl=float(hub(pred,ycal))
        if vl<best[0]: best=(vl,{k:v.detach().clone() for k,v in m.state_dict().items()},ep)
    m.load_state_dict(best[1]); m.eval(); metrics={}; predictions={}
    for part,rows in parts.items():
        if not rows: continue
        x,y,ys=build_matrix(rows,mode,seed_stats); xn=(x-mu)/sd; pred,per=predict(m,kind,xn); pp=pred.detach().cpu().numpy().tolist()
        metrics[part]={'all_candidate':all_candidate_metrics(rows,pp),'simvla_only':simvla_only_metrics(rows,pp)}
        predictions[part]=[{'context_id':r['context_id'],'candidate_type':r['candidate_type'],'true':float(r['true_chunk_l2_error']),'pred':float(p)} for r,p in zip(rows,pp)]
    ckdir=CKROOT/split/variant; ckdir.mkdir(parents=True,exist_ok=True); torch.save({'state_dict':m.state_dict(),'feature_mode':mode,'kind':kind,'setting':setting,'input_mean':mu,'input_std':sd,'input_dim':xtr.shape[1],'best_epoch':best[2]}, ckdir/'model.pt'); (ckdir/'predictions.json').write_text(json.dumps(predictions))
    return {'variant':variant,'feature_mode':mode,'model_kind':kind,'train_setting':setting,'train_rows':len(train_rows),'input_dim':int(xtr.shape[1]),'best_epoch':best[2],'best_calib_loss':best[0],'train_time_sec':time.time()-t0,'metrics':metrics}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--split',default='holdout_libero_object'); ap.add_argument('--variants',nargs='*',default=list(VARIANTS)); ap.add_argument('--quick',action='store_true'); ap.add_argument('--epochs',type=int,default=120); ap.add_argument('--out-prefix',default=None); args=ap.parse_args()
    RROOT.mkdir(parents=True,exist_ok=True); results=[]
    for v in args.variants:
        print('TRAIN',args.split,v,flush=True); results.append(train_variant(args.split,v,args.epochs,args.quick))
    out={'split':args.split,'results':results}; prefix=args.out_prefix or f'stage6_pilot_{args.split}'
    (RROOT/f'{prefix}.json').write_text(json.dumps(out,indent=2))
    lines=['# Stage 6 Experiments: '+args.split,'','```json',json.dumps(out,indent=2),'```']; (RROOT/f'{prefix}.md').write_text('\n'.join(lines)+'\n')
    print('wrote',RROOT/f'{prefix}.md')
if __name__=='__main__': main()
