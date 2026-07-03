import json

with open("bob_results.json", "r") as f:
    bob_results = json.load(f)

with open("sam_results.json", "r") as f:
    sam_results = json.load(f)

merged = bob_results + sam_results

with open("merged_smoke_test_results.json", "w") as f:
    json.dump(merged, f, indent=2)

# Summary
summary = {
    "Bob": {"total": len(bob_results), "pass": 0, "fail": 0, "errors": {}},
    "Sam": {"total": len(sam_results), "pass": 0, "fail": 0, "errors": {}}
}

for r in bob_results:
    if r["status"] == "PASS":
        summary["Bob"]["pass"] += 1
    else:
        summary["Bob"]["fail"] += 1
        etype = r.get("error_type", "UNKNOWN")
        summary["Bob"]["errors"][etype] = summary["Bob"]["errors"].get(etype, 0) + 1

for r in sam_results:
    if r["status"] == "PASS":
        summary["Sam"]["pass"] += 1
    else:
        summary["Sam"]["fail"] += 1
        etype = r.get("error_type", "UNKNOWN")
        summary["Sam"]["errors"][etype] = summary["Sam"]["errors"].get(etype, 0) + 1

print(json.dumps(summary, indent=2))
