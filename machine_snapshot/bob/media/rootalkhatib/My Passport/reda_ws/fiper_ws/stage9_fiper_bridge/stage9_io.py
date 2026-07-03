import json
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any

def read_jsonl(path: str) -> List[Dict[str, Any]]:
    rows = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def write_jsonl(path: str, rows: List[Dict[str, Any]]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")

def get_state_id(sample: Dict[str, Any]) -> str:
    meta = sample.get("metadata") or {}
    return str(meta.get("state_id") or sample.get("state_id") or sample.get("sample_id") or "unknown")

def group_by_state_id(rows: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    groups = defaultdict(list)
    for row in rows:
        sid = get_state_id(row)
        # Strip seed suffix if the sample_id was used as state_id
        if "_seed" in sid:
            sid = sid.split("_seed")[0]
        groups[sid].append(row)
    return dict(groups)

def summarize_stage9_v2_dataset(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    groups = group_by_state_id(rows)
    total_samples = len(rows)
    total_groups = len(groups)
    
    risk_bins = defaultdict(int)
    for row in rows:
        label = row.get("label") or {}
        risk_bin = label.get("risk_bin", "unknown")
        risk_bins[risk_bin] += 1
        
    group_sizes = [len(g) for g in groups.values()]
    avg_group_size = sum(group_sizes) / len(group_sizes) if group_sizes else 0
    
    return {
        "total_samples": total_samples,
        "total_groups": total_groups,
        "risk_bins": dict(risk_bins),
        "min_group_size": min(group_sizes) if group_sizes else 0,
        "max_group_size": max(group_sizes) if group_sizes else 0,
        "avg_group_size": avg_group_size
    }

def select_success_only_samples(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Selects samples that represent successful calibration anchors:
    1. Expert LIBERO demos (source = 'libero_expert_demonstration' or labeled as risk_anchor).
    2. Policy successes: outcome.success_within_H == True or outcome.success_after == True,
       or labeled with low risk (e.g., risk_score <= 0.35 and risk_bin in ['SAFE_STRONG', 'SAFE_WEAK']).
    """
    success_samples = []
    for row in rows:
        # Check source metadata
        meta = row.get("metadata") or {}
        is_expert = meta.get("source") == "libero_expert_demonstration" or "expert" in str(meta.get("source_hdf5", "")).lower()
        
        # Check outcome success
        outcome = row.get("outcome") or {}
        is_outcome_success = bool(outcome.get("success_within_H") or outcome.get("success_after") or outcome.get("success"))
        
        # Check labels from continuous v2
        label = row.get("label") or {}
        risk_score = label.get("risk_score")
        risk_bin = label.get("risk_bin")
        is_low_risk = risk_score is not None and risk_score <= 0.35
        
        if is_expert or is_outcome_success or (is_low_risk and risk_bin in ["SAFE_STRONG", "SAFE_WEAK"]):
            success_samples.append(row)
            
    return success_samples

def select_same_state_groups(rows: List[Dict[str, Any]], expected_size: int = 64) -> Dict[str, List[Dict[str, Any]]]:
    """
    Groups rows by state_id and returns only groups that have exactly expected_size members (or close to it).
    """
    groups = group_by_state_id(rows)
    return {sid: g for sid, g in groups.items() if len(g) == expected_size}
