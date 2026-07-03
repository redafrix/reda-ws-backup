#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import h5py

REDA_WS=Path("/media/rootalkhatib/My Passport/reda_ws")
ROOTS=[
    REDA_WS/"intern_ship_ws/ood_data",
    REDA_WS/"intern_ship_ws/assets/data",
    REDA_WS/"intern_ship_ws/outputs/eval",
    REDA_WS/"intern_ship_ws/simvla",
    REDA_WS/"intern_ship_ws/tdqc",
]
REPORT=REDA_WS/"asynchvla_ws/outputs/reports/ood_expert_data_search.md"
OOD_HINTS=("ood","unseen","novel","heldout","held_out","out_of_distribution")

def has_ood_hint(path: Path) -> bool:
    # Match path tokens, not arbitrary substrings; avoids false positives like "wooden" containing "ood".
    text = str(path).lower().replace("-", "_")
    tokens = []
    for part in Path(text).parts:
        tokens.extend([tok for tok in part.replace(".", "_").split("_") if tok])
    joined = "_".join(tokens)
    return ("ood" in tokens or "unseen" in tokens or "novel" in tokens or "heldout" in tokens or "held_out" in joined or "out_of_distribution" in joined)

def h5_summary(path:Path):
    info={"path":str(path),"size_bytes":path.stat().st_size,"has_expert_actions":False,"has_images":False,"has_proprio":False,"keys":[],"shapes":{},"error":None}
    try:
        with h5py.File(path,"r") as f:
            info["keys"]=list(f.keys())
            demo=None
            if "data" in f and len(f["data"].keys())>0:
                dk=sorted(f["data"].keys())[0]; demo=f["data"][dk]; base=f"data/{dk}"
            else:
                demo=f; base=""
            def has(k): return k in demo
            checks=["actions","obs/agentview_rgb","obs/eye_in_hand_rgb","obs/ee_pos","obs/ee_ori","obs/gripper_states","obs/joint_states"]
            for k in checks:
                if has(k):
                    d=demo[k]; info["shapes"][f"{base}/{k}" if base else k]=list(d.shape)
            info["has_expert_actions"]="actions" in demo
            info["has_images"]=("obs/agentview_rgb" in demo) or ("obs/eye_in_hand_rgb" in demo)
            info["has_proprio"]=("obs/ee_pos" in demo and "obs/gripper_states" in demo) or ("robot_states" in demo)
    except Exception as e:
        info["error"]=repr(e)
    return info

def main():
    all_h5=[]; hinted=[]; npz_pt=[]
    for root in ROOTS:
        if not root.exists(): continue
        for p in root.rglob("*"):
            if not p.is_file(): continue
            low=str(p).lower()
            if p.suffix.lower() in (".hdf5",".h5"):
                all_h5.append(p)
                if has_ood_hint(p): hinted.append(p)
            elif p.suffix.lower() in (".pt",".npz",".pkl",".json",".csv") and has_ood_hint(p):
                npz_pt.append(p)
    hinted_summaries=[h5_summary(p) for p in sorted(set(hinted))[:100]]
    usable=[s for s in hinted_summaries if s["has_expert_actions"] and s["has_images"] and s["has_proprio"]]
    # Also report if any separate ood_data HDF5 exists even without name hint.
    ood_root_h5=[p for p in all_h5 if "intern_ship_ws/ood_data" in str(p)]
    for p in ood_root_h5:
        if p not in hinted:
            s=h5_summary(p); hinted_summaries.append(s)
            if s["has_expert_actions"] and s["has_images"] and s["has_proprio"]: usable.append(s)
    lines=["# OOD Expert Data Search","",f"- Roots searched: `{[str(r) for r in ROOTS]}`",f"- Total HDF5/H5 files found under roots: `{len(all_h5)}`",f"- HDF5/H5 files with OOD/unseen/novel hints: `{len(hinted)}`",f"- OOD-hint non-HDF5 metadata/artifacts found: `{len(npz_pt)}`",f"- Usable raw OOD expert demos found: `{len(usable)}`",""]
    if usable:
        lines += ["## Usable Raw OOD Expert Demonstrations",""]
        for s in usable:
            lines += [f"- `{s['path']}` size=`{s['size_bytes']}` shapes=`{s['shapes']}`"]
    else:
        lines += ["True OOD action-error evaluation is blocked because no OOD expert-action demonstrations were found.",""]
    lines += ["## HDF5/H5 OOD-Hint Inspection", "", "```json", json.dumps(hinted_summaries[:50], indent=2), "```", "", "## OOD-Hint Non-HDF5 Files", ""]
    for p in sorted(npz_pt)[:100]: lines.append(f"- `{p}` size=`{p.stat().st_size}`")
    REPORT.write_text("\n".join(lines)+"\n")
    print("ood_search: OK")
    print("total_h5", len(all_h5))
    print("hinted_h5", len(hinted))
    print("usable", len(usable))
    print("report", REPORT)
if __name__=="__main__": main()
