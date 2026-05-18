#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
DATA = REDA_WS / "asynchvla_ws/data/debug/candidate_debug.pt"
CKPT = REDA_WS / "asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt"
REPORT = REDA_WS / "asynchvla_ws/outputs/reports/debug_calibration_report.md"

class MLP(nn.Module):
    def __init__(self, in_dim: int):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(in_dim,256), nn.ReLU(), nn.Dropout(0.05), nn.Linear(256,128), nn.ReLU(), nn.Linear(128,1), nn.Softplus())
    def forward(self,x): return self.net(x).squeeze(-1)

def features(rows):
    return torch.stack([torch.cat([r["pooled_vlm_features"].float().flatten(), r["proprio"].float().flatten(), r["candidate_action_normalized"].float().flatten()]) for r in rows])

def risk(y, u):
    order=np.argsort(u)
    return [(c, float(np.mean(y[order[:max(1,int(round(len(y)*c)))]]))) for c in [0.10,0.25,0.50,0.75,1.00]]

def main():
    payload=torch.load(DATA,map_location="cpu")
    rows=payload["candidates"]
    ckpt=torch.load(CKPT,map_location="cpu")
    val_ctx=set(ckpt["split"]["val_contexts"])
    val=[r for r in rows if r["context_id"] in val_ctx]
    model_info=ckpt["models"]["full"]
    x=(features(val)-model_info["input_mean"])/model_info["input_std"]
    y=np.array([r["true_chunk_l2_error"] for r in val], dtype=np.float32)
    model=MLP(model_info["input_dim"])
    model.load_state_dict(model_info["state_dict"])
    model.eval()
    with torch.no_grad(): pred=model(x).numpy()
    residual=y-pred
    eta=max(0.0, float(np.quantile(residual,0.90)))
    calibrated=pred+eta
    coverage=float(np.mean(y <= calibrated))
    by_type=defaultdict(list)
    for r, yy, pp, cc in zip(val,y,pred,calibrated):
        by_type[r["candidate_type"]].append((yy,pp,cc))
    type_lines=[]
    for typ, vals in sorted(by_type.items()):
        arr=np.array(vals)
        cov=float(np.mean(arr[:,0] <= arr[:,2]))
        type_lines.append(f"- `{typ}`: n=`{len(vals)}`, coverage=`{cov:.4f}`, mean_true=`{float(arr[:,0].mean()):.6f}`, mean_pred=`{float(arr[:,1].mean()):.6f}`, mean_calibrated=`{float(arr[:,2].mean()):.6f}`")
    results={"calibration_rows":len(val),"calibration_contexts":len(val_ctx),"eta_90":eta,"empirical_coverage":coverage,"mean_predicted_error":float(pred.mean()),"mean_calibrated_uncertainty":float(calibrated.mean()),"risk_coverage_before":risk(y,pred),"risk_coverage_after":risk(y,calibrated)}
    lines=["# Debug Calibration Report","",f"- Dataset: `{DATA}`",f"- Checkpoint: `{CKPT}`",f"- Calibration split size rows: `{len(val)}`",f"- Calibration split contexts: `{len(val_ctx)}`",f"- Method: conformal residual correction, `calibrated_uncertainty = predicted_error + eta`.","","## Summary JSON","","```json",json.dumps(results,indent=2),"```","","## Coverage Per Candidate Type","",*type_lines]
    REPORT.write_text("\n".join(lines)+"\n")
    print("calibration_debug: OK")
    print(json.dumps(results, indent=2))
    print("report", REPORT)
if __name__=="__main__": main()
