#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

REDA_WS=Path("/media/rootalkhatib/My Passport/reda_ws")
DATA=REDA_WS/"asynchvla_ws/data/debug/candidate_debug.pt"
CKPT=REDA_WS/"asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt"
REPORT=REDA_WS/"asynchvla_ws/outputs/reports/action_sensitivity_eval.md"
TYPES=["expert_action","perturb_small","same_task_far","other_demo_or_other_task","simvla_seed0","perturb_large"]

class MLP(nn.Module):
    def __init__(self,in_dim:int):
        super().__init__(); self.net=nn.Sequential(nn.Linear(in_dim,256),nn.ReLU(),nn.Dropout(0.05),nn.Linear(256,128),nn.ReLU(),nn.Linear(128,1),nn.Softplus())
    def forward(self,x): return self.net(x).squeeze(-1)

def features(rows):
    return torch.stack([torch.cat([r["pooled_vlm_features"].float().flatten(),r["proprio"].float().flatten(),r["candidate_action_normalized"].float().flatten()]) for r in rows])

def main():
    payload=torch.load(DATA,map_location="cpu"); rows=payload["candidates"]
    ckpt=torch.load(CKPT,map_location="cpu"); val_ctx=set(ckpt["split"]["val_contexts"])
    val=[r for r in rows if r["context_id"] in val_ctx]
    mi=ckpt["models"]["full"]; x=(features(val)-mi["input_mean"])/mi["input_std"]
    model=MLP(mi["input_dim"]); model.load_state_dict(mi["state_dict"]); model.eval()
    with torch.no_grad(): preds=model(x).numpy()
    by_type=defaultdict(list); by_ctx=defaultdict(dict)
    for r,p in zip(val,preds):
        rec={"pred":float(p),"true":float(r["true_chunk_l2_error"]),"context_id":r["context_id"],"task":r["task_name"]}
        by_type[r["candidate_type"]].append(rec); by_ctx[r["context_id"]][r["candidate_type"]]=rec
    type_summary={}
    for typ, vals in by_type.items():
        type_summary[typ]={"n":len(vals),"mean_pred_uncertainty":float(np.mean([v["pred"] for v in vals])),"mean_true_error":float(np.mean([v["true"] for v in vals]))}
    matrix={}
    for a in TYPES:
        matrix[a]={}
        for b in TYPES:
            total=ok=0
            for d in by_ctx.values():
                if a in d and b in d and a!=b:
                    total+=1; ok+=int(d[a]["pred"] < d[b]["pred"])
            matrix[a][b]=None if total==0 or a==b else ok/total
    failures=[]
    for ctx,d in by_ctx.items():
        if "expert_action" in d and "perturb_large" in d and d["expert_action"]["pred"] >= d["perturb_large"]["pred"]:
            failures.append({"context_id":ctx,"case":"expert_not_below_large","expert_pred":d["expert_action"]["pred"],"large_pred":d["perturb_large"]["pred"],"task":d["expert_action"]["task"]})
        if "expert_action" in d and "other_demo_or_other_task" in d and d["expert_action"]["pred"] >= d["other_demo_or_other_task"]["pred"]:
            failures.append({"context_id":ctx,"case":"expert_not_below_other_task","expert_pred":d["expert_action"]["pred"],"other_pred":d["other_demo_or_other_task"]["pred"],"task":d["expert_action"]["task"]})
    action_ignored = type_summary.get("expert_action",{}).get("mean_pred_uncertainty",0) >= type_summary.get("perturb_large",{}).get("mean_pred_uncertainty",0)
    results={"validation_contexts":len(val_ctx),"validation_rows":len(val),"type_summary":type_summary,"ranking_matrix_pred_less_probability":matrix,"num_failures_recorded":len(failures),"first_failures":failures[:10],"appears_to_ignore_actions":bool(action_ignored)}
    lines=["# Action Sensitivity Evaluation","",f"- Dataset: `{DATA}`",f"- Checkpoint: `{CKPT}`",f"- Held-out validation contexts: `{len(val_ctx)}`","","## Results JSON","","```json",json.dumps(results,indent=2),"```"]
    REPORT.write_text("\n".join(lines)+"\n")
    print("action_sensitivity_eval: OK")
    print(json.dumps(results,indent=2))
    print("report",REPORT)
if __name__=="__main__": main()
