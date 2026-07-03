#!/usr/bin/env python3
from pathlib import Path
import json
import statistics

BASE_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609/runs")
Q95_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610/runs")


def load(path: Path) -> dict[int, dict]:
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(errors="ignore").splitlines():
        if line.strip():
            row = json.loads(line)
            out[int(row["reset_seed"])] = row
    return out


def summarize_rows(rows: list[dict]) -> tuple[int, int, float]:
    if not rows:
        return 0, 0, 0.0
    return (
        len(rows),
        sum(bool(row.get("success")) for row in rows),
        statistics.mean(int(row.get("num_steps", row.get("steps", 0)) or 0) for row in rows),
    )


totals = {
    "original": [],
    "modified": [],
    "q95": [],
}
paired_rescues = []
paired_regressions = []
task_rows = []
mod_queries = 0
total_queries = 0
action_mods = 0
mod_eps = 0

for task in range(18):
    original = load(BASE_ROOT / f"task{task}/original_simvla/simvla_only/episode_summaries.jsonl")
    modified = load(BASE_ROOT / f"task{task}/modified_simvla/simvla_only/episode_summaries.jsonl")
    q95 = load(Q95_ROOT / f"task{task}/modified_h10_risk_topk8/risk_topk8/episode_summaries.jsonl")
    totals["original"].extend(original.values())
    totals["modified"].extend(modified.values())
    totals["q95"].extend(q95.values())

    rescues = []
    regressions = []
    both_success = both_failure = 0
    common = sorted(set(modified) & set(q95))
    for seed in common:
        bs = bool(modified[seed].get("success"))
        rs = bool(q95[seed].get("success"))
        if (not bs) and rs:
            rescues.append(seed)
            paired_rescues.append((task, seed))
        elif bs and (not rs):
            regressions.append(seed)
            paired_regressions.append((task, seed))
        elif bs and rs:
            both_success += 1
        else:
            both_failure += 1

    task_rows.append(
        {
            "task": task,
            "original": f"{sum(bool(v.get('success')) for v in original.values())}/{len(original)}",
            "modified": f"{sum(bool(v.get('success')) for v in modified.values())}/{len(modified)}",
            "q95": f"{sum(bool(v.get('success')) for v in q95.values())}/{len(q95)}",
            "rescues": len(rescues),
            "regressions": len(regressions),
            "net": len(rescues) - len(regressions),
            "both_success": both_success,
            "both_failure": both_failure,
        }
    )

    for row in q95.values():
        mods = int(row.get("action_modifications_count", row.get("modification_count", 0)) or 0)
        action_mods += mods
        mod_eps += int(mods > 0)
        total_queries += int(row.get("num_queries", 0) or 0)
    step_path = Q95_ROOT / f"task{task}/modified_h10_risk_topk8/risk_topk8/step_scores_risk_topk8.jsonl"
    if step_path.exists():
        for line in step_path.read_text(errors="ignore").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if int(row.get("selected_candidate_index", row.get("selected_idx", 0)) or 0) != 0:
                mod_queries += 1

print("GLOBAL")
for name, rows in totals.items():
    n, s, mean_steps = summarize_rows(rows)
    print(name, n, s, f"{100*s/n:.2f}%" if n else "NA", f"mean_steps={mean_steps:.2f}")
print("PAIRED_Q95_VS_MODIFIED", len(paired_rescues), paired_rescues, len(paired_regressions), paired_regressions, "net", len(paired_rescues) - len(paired_regressions))
print("MODIFICATIONS", "episode_mods", action_mods, "mod_eps", mod_eps, "num_queries_sum", total_queries, "step_modified_queries", mod_queries)
print("TASKS")
for row in task_rows:
    print(json.dumps(row, sort_keys=True))
