import subprocess
import json
import os
import numpy as np
import sys

def run_task(suite, task_id):
    out_path = f"asynchvla_ws/outputs/reports/stage7/scan/scan_{suite}_task{task_id}.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    cmd = [
        "python3", "asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py",
        "--task-suite", suite,
        "--task-id", str(task_id),
        "--num-episodes", "2",
        "--max-steps", "600",
        "--modes", "A_passive",
        "--out", out_path
    ]
    
    print(f"Checking {suite} task {task_id}...", flush=True)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=1200) 
        if result.returncode != 0:
            print(f"Error running {suite} {task_id}: {result.stderr}", flush=True)
            return {"suite": suite, "task_id": task_id, "error": result.stderr}
    except Exception as e:
        print(f"Exception running {suite} {task_id}: {str(e)}", flush=True)
        return {"suite": suite, "task_id": task_id, "error": str(e)}

    if not os.path.exists(out_path):
        return {"suite": suite, "task_id": task_id, "error": "No output file"}

    with open(out_path) as f:
        data = json.load(f)
    
    eps = data.get("episodes", [])
    if not eps:
        return {"suite": suite, "task_id": task_id, "error": "No episodes in output"}
    
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

    return {
        "suite": suite,
        "task_id": task_id,
        "task_name": data.get("task_language", "unknown"),
        "success_rate": success_rate,
        "avg_steps": float(np.mean(all_steps)) if all_steps else 0,
        "avg_uncertainty": float(np.mean(all_unc)) if all_unc else 0,
        "max_uncertainty": float(np.max(all_unc)) if all_unc else 0,
        "num_episodes": len(eps)
    }

def main():
    suites = ["libero_spatial", "libero_goal", "libero_object", "libero_10"]
    results = []
    
    for suite in suites:
        for task_id in range(10):
            res = run_task(suite, task_id)
            results.append(res)
            
            if "error" not in res:
                print(f"  Result: {res['success_rate']*100}% success, {res['avg_steps']} steps, {res['avg_uncertainty']:.3f} unc", flush=True)
            else:
                print(f"  Skipped/Error: {res['error']}", flush=True)

    os.makedirs("asynchvla_ws/outputs/reports/stage7", exist_ok=True)
    with open("asynchvla_ws/outputs/reports/stage7/stage7_hard_task_scan.json", "w") as f:
        json.dump(results, f, indent=2)

    with open("asynchvla_ws/outputs/reports/stage7/stage7_hard_task_scan.md", "w") as f:
        f.write("# Stage 7 — Hard Task Scan\n\n")
        f.write("| Suite | Task ID | Name | Success | Avg Steps | Avg Unc | Max Unc |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        
        valid_results = [r for r in results if "error" not in r]
        for r in valid_results:
            f.write(f"| {r['suite']} | {r['task_id']} | {r['task_name']} | {r['success_rate']*100}% | {r['avg_steps']:.1f} | {r['avg_uncertainty']:.3f} | {r['max_uncertainty']:.3f} |\n")

    print("Scan complete.", flush=True)

if __name__ == "__main__":
    main()
