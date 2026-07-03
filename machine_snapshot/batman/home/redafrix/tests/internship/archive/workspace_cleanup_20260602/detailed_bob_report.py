import json
from collections import Counter

with open("bob_results.json", "r") as f:
    bob_results = json.load(f)

suite_stats = {}
for r in bob_results:
    suite = r["suite_name"]
    if suite not in suite_stats:
        suite_stats[suite] = {"pass": 0, "fail": 0, "errors": Counter()}
    if r["status"] == "PASS":
        suite_stats[suite]["pass"] += 1
    else:
        suite_stats[suite]["fail"] += 1
        suite_stats[suite]["errors"][r["error_type"]] += 1

print(f"{'Suite':<40} | {'Pass':<5} | {'Fail':<5} | {'Errors'}")
print("-" * 80)
for suite, stats in sorted(suite_stats.items()):
    err_str = ", ".join([f"{k}: {v}" for k, v in stats["errors"].items()])
    print(f"{suite:<40} | {stats['pass']:<5} | {stats['fail']:<5} | {err_str}")
