import json
import os
import numpy as np

base_dir = "asynchvla_ws/outputs/reports/stage7/scan"
results = []
if os.path.exists(base_dir):
    for f in sorted(os.listdir(base_dir)):
        if f.endswith(".json"):
            with open(os.path.join(base_dir, f)) as f_in:
                data = json.load(f_in)
                eps = data.get("episodes", [])
                successes = [e for e in eps if e.get("success")]
                success_rate = len(successes) / len(eps) if eps else 0
                all_steps = [e.get("steps", 0) for e in eps]
                
                all_unc = []
                for e in eps:
                    trace = e.get("trace", [])
                    for t in trace:
                        if t.get("kind") == "replan":
                            scores = t.get("scores", [])
                            if scores:
                                all_unc.extend(scores)
                
                results.append({
                    "suite": data.get("task_suite", "unknown"),
                    "task_id": data.get("task_id", -1),
                    "task_name": data.get("task_language", "unknown"),
                    "success_rate": success_rate,
                    "avg_steps": float(np.mean(all_steps)) if all_steps else 0,
                    "avg_uncertainty": float(np.mean(all_unc)) if all_unc else 0,
                    "max_uncertainty": float(np.max(all_unc)) if all_unc else 0
                })

report_json = "asynchvla_ws/outputs/reports/stage7/stage7_hard_task_scan.json"
with open(report_json, "w") as f:
    json.dump(results, f, indent=2)

report_md = "asynchvla_ws/outputs/reports/stage7/stage7_hard_task_scan.md"
with open(report_md, "w") as f:
    f.write("# Stage 7 — Hard Task Scan\n\n")
    f.write("| Suite | Task ID | Name | Success | Avg Steps | Avg Unc | Max Unc |\n")
    f.write("|---|---|---|---|---|---|---|\n")
    for r in results:
        f.write(f"| {r['suite']} | {r['task_id']} | {r['task_name']} | {r['success_rate']*100}% | {r['avg_steps']:.1f} | {r['avg_uncertainty']:.3f} | {r['max_uncertainty']:.3f} |\n")

print(f"Report written to {report_md}")
