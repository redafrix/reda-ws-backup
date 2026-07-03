#!/usr/bin/env python3
from pathlib import Path
import json

base = Path("/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_10ep_20260610/runs")
m10 = Path("/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_m10_10ep_20260610/runs")


def load(path: Path) -> dict[int, dict]:
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(errors="ignore").splitlines():
        if line.strip():
            row = json.loads(line)
            out[int(row["reset_seed"])] = row
    return out


print("task,baseline,m02,m10,m10_vs_base_net,m10_vs_m02_net,m10_mods,m10_mean_steps")
for task in range(18):
    baseline = load(base / f"task{task}/modified_simvla/simvla_only/episode_summaries.jsonl")
    m02 = load(base / f"task{task}/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl")
    current = load(m10 / f"task{task}/risk_topk8_selected_cap_m10/risk_topk8/episode_summaries.jsonl")
    if not current:
        continue

    common_base = sorted(set(baseline) & set(current))
    common_m02 = sorted(set(m02) & set(current))
    net_base = sum((not baseline[s]["success"]) and current[s]["success"] for s in common_base) - sum(
        baseline[s]["success"] and (not current[s]["success"]) for s in common_base
    )
    net_m02 = sum((not m02[s]["success"]) and current[s]["success"] for s in common_m02) - sum(
        m02[s]["success"] and (not current[s]["success"]) for s in common_m02
    )

    mods = sum(int(row.get("action_modifications_count", 0) or 0) for row in current.values())
    mean_steps = sum(int(row.get("num_steps", 0) or 0) for row in current.values()) / len(current)
    baseline_txt = f"{sum(bool(row.get('success')) for row in baseline.values())}/{len(baseline)}" if baseline else "NA"
    m02_txt = f"{sum(bool(row.get('success')) for row in m02.values())}/{len(m02)}" if m02 else "NA"
    current_txt = f"{sum(bool(row.get('success')) for row in current.values())}/{len(current)}"
    print(task, baseline_txt, m02_txt, current_txt, net_base, net_m02, mods, round(mean_steps, 1))
