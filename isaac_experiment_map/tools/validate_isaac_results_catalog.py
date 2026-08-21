#!/usr/bin/env python3
"""Validator for Master Isaac Results Catalog & Analysis-Ready Tables.

Performs rigorous consistency, arithmetic, enum validity, quarantine exclusion,
and integrity checks across the full experimental catalog.
"""

from __future__ import annotations

import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

WORKSPACE = Path("/home/redafrix/tests/internship")
MAP_DIR = WORKSPACE / "isaac_experiment_map"
CATALOG_DIR = MAP_DIR / "catalog"
ANALYSIS_DIR = MAP_DIR / "analysis_ready"

VALID_STATUSES = {
    "valid", "historical_reference", "incomplete", "superseded",
    "quarantined_invalid", "development_only", "predeclared_not_executed"
}

VALID_CANONICALITIES = {
    "canonical_primary", "canonical_ablation", "canonical_baseline",
    "historical_reference", "noncanonical", "invalid"
}


def main() -> int:
    print("=== STARTING MASTER ISAAC RESULTS CATALOG VALIDATION ===")
    errors = []

    # 1. Validate experiments.jsonl
    exp_f = CATALOG_DIR / "experiments.jsonl"
    if not exp_f.exists():
        errors.append("Missing experiments.jsonl!")
        return 1

    experiments = [json.loads(l) for l in exp_f.read_text().splitlines() if l.strip()]
    print(f"Auditing {len(experiments)} experiment records in experiments.jsonl...")

    exp_ids = set()
    exp_keys = set()

    for e in experiments:
        eid = e["experiment_id"]
        ekey = e["experiment_key"]

        if eid in exp_ids:
            errors.append(f"Duplicate experiment_id: {eid}")
        exp_ids.add(eid)

        if ekey in exp_keys:
            errors.append(f"Duplicate experiment_key: {ekey}")
        exp_keys.add(ekey)

        # Enum checks
        if e["scientific_status"] not in VALID_STATUSES:
            errors.append(f"Invalid scientific_status '{e['scientific_status']}' in {eid}")
        if e["canonicality"] not in VALID_CANONICALITIES:
            errors.append(f"Invalid canonicality '{e['canonicality']}' in {eid}")

        # Quarantine check
        if e["scientific_status"] in ["quarantined_invalid", "development_only", "predeclared_not_executed"] and e["use_for_primary_results"]:
            errors.append(f"Quarantined/non-executable run {eid} has use_for_primary_results == True!")

        # Arithmetic check
        if e["episode_count"] is not None and e["episode_count"] > 0:
            succ = e.get("success_count", 0) or 0
            fail = e.get("failure_count", 0) or 0
            if succ + fail != e["episode_count"]:
                errors.append(f"Sum mismatch in {eid}: {succ} + {fail} != {e['episode_count']}")
            
            if e["success_rate"] is not None:
                exp_rate = succ / e["episode_count"]
                if abs(e["success_rate"] - exp_rate) > 1e-4:
                    errors.append(f"Success rate mismatch in {eid}: {e['success_rate']} != {exp_rate}")

    # 2. Validate paired_comparisons.csv
    paired_f = CATALOG_DIR / "paired_comparisons.csv"
    if not paired_f.exists():
        errors.append("Missing paired_comparisons.csv!")
    else:
        with paired_f.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                cid = row["comparison_id"]
                n_pairs = int(row["n_pairs"])
                a_succ = int(row["a_successes"])
                b_succ = int(row["b_successes"])
                s_to_s = int(row["both_success"])
                s_to_f = int(row["a_only_success"])
                f_to_s = int(row["b_only_success"])
                f_to_f = int(row["both_failure"])
                rescues = int(row["rescues_relative_to_a"])
                regressions = int(row["regressions_relative_to_a"])
                net = int(row["net_change"])

                if s_to_s + s_to_f + f_to_s + f_to_f != n_pairs:
                    errors.append(f"Matrix sum mismatch in {cid}: {s_to_s}+{s_to_f}+{f_to_s}+{f_to_f} != {n_pairs}")
                if s_to_s + s_to_f != a_succ:
                    errors.append(f"A successes mismatch in {cid}: {s_to_s}+{s_to_f} != {a_succ}")
                if s_to_s + f_to_s != b_succ:
                    errors.append(f"B successes mismatch in {cid}: {s_to_s}+{f_to_s} != {b_succ}")
                if rescues != f_to_s or regressions != s_to_f:
                    errors.append(f"Rescue/regression mismatch in {cid}")
                if net != rescues - regressions:
                    errors.append(f"Net rescue mismatch in {cid}: {net} != {rescues} - {regressions}")

    # 3. Validate ood400_episode_results.csv
    ep_f = ANALYSIS_DIR / "ood400_episode_results.csv"
    if not ep_f.exists():
        errors.append("Missing ood400_episode_results.csv!")
    else:
        with ep_f.open() as f:
            rows = list(csv.DictReader(f))
            if len(rows) != 1200:
                errors.append(f"Expected 1200 rows in ood400_episode_results.csv, got {len(rows)}")
            
            # Check variant counts
            var_counts = Counter(r["variant"] for r in rows)
            for v in ["baseline", "c090_primary", "q95_symmetric"]:
                if var_counts[v] != 400:
                    errors.append(f"Variant {v} has {var_counts[v]} rows (expected 400)")

    # 4. Validate ood400_decision_summary.csv
    dec_f = ANALYSIS_DIR / "ood400_decision_summary.csv"
    if not dec_f.exists():
        errors.append("Missing ood400_decision_summary.csv!")
    else:
        with dec_f.open() as f:
            dec_rows = list(csv.DictReader(f))
            if len(dec_rows) != 19514:
                errors.append(f"Expected 19514 rows in ood400_decision_summary.csv, got {len(dec_rows)}")

    # 5. Summary
    if errors:
        print(f"VALIDATION FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print("ALL CATALOG AND DATASET INTEGRITY CHECKS PASSED (0 errors)!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
