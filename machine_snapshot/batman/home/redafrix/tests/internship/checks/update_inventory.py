import json
from datetime import datetime

inventory_path = 'fiper_ws/experiment_catalog/inventory.json'

with open(inventory_path, 'r') as f:
    data = json.load(f)

# Define the 8 structured entries to add
new_entries = [
    {
        "name": "h10_goal_object_risk_proof_20260608",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608",
        "date": "2026-06-08",
        "type": "online_eval",
        "suite": "libero_goal_object",
        "tasks": [3, 6, 8],
        "policies": ["original_simvla", "modified_simvla", "original_h10_risk_base", "modified_h10_risk_topk8"],
        "episode_counts": {
            "Task 3": {
                "original_simvla": 100,
                "modified_simvla": 100,
                "original_h10_risk_base": 100,
                "modified_h10_risk_topk8": 100
            },
            "Task 6": {
                "original_simvla": 100,
                "modified_simvla": 100,
                "original_h10_risk_base": 100,
                "modified_h10_risk_topk8": 100
            },
            "Task 8": {
                "modified_simvla": 5,
                "modified_h10_risk_topk8": 2
            }
        },
        "trust_verdict": "PARTIAL_TRUST (Task 3/6 trusted, Task 8 incomplete and untrustworthy)",
        "caveats": "Task 8 runs are incomplete and were aborted early by KeyboardInterrupt. Tasks 3/6 are seen-task/unseen-seed, not zero-shot generalization.",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md"
        ]
    },
    {
        "name": "h10_goal_object_topk8_aggressive_task3_20260608",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608",
        "date": "2026-06-08",
        "type": "online_eval",
        "suite": "libero_goal_object",
        "tasks": [3, 6],
        "policies": ["modified_h10_risk_topk8"],
        "episode_counts": {
            "Task 3": 100,
            "Task 6": 100
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Aggressive gating (T=0.3) leads to over-activity (1.04% query mods in Task 3, 22.98% query mods in Task 6). Task 3 has 29 mods, Task 6 has 443 mods. Causes 14 regressions on Task 6.",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md"
        ]
    },
    {
        "name": "h10_goal_object_task6_old_topk8_aggressive_20260608",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608",
        "date": "2026-06-08",
        "type": "online_eval",
        "suite": "libero_goal_object",
        "tasks": [6],
        "policies": ["modified_h10_risk_topk8"],
        "episode_counts": {
            "Task 6": 100
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Ablation run using old Dean detector (hash 0ea8e943). Threshold T=0.3. Succeeded in rescuing 13 and causing 10 regressions (+3 net gain).",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md"
        ]
    },
    {
        "name": "h10_ood_goal_object_and_swap_20260608",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608",
        "date": "2026-06-08",
        "type": "online_eval",
        "suite": "libero_goal_swap",
        "tasks": [3, 6, 8],
        "policies": ["original_simvla", "modified_simvla", "risk_topk8"],
        "episode_counts": {
            "Task 3": 100,
            "Task 6": 100,
            "Task 8": 100
        },
        "trust_verdict": "DO_NOT_TRUST",
        "caveats": "OOD goal-swap failed completely, resulting in -2 net success (8/300 baseline vs 6/300 risk). Triggered panic interventions on impossible tasks. Full-suite goal-swap was not run, only tasks 3/6/8.",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/OOD_GOAL_SWAP_FINAL_PAIRED_ANALYSIS_20260609.md"
        ]
    },
    {
        "name": "h10_risk_aware_forensic_sanity_audit_steps_1_to_8",
        "host": "batman",
        "absolute_path": "/home/redafrix/tests/internship/checks",
        "date": "2026-06-09",
        "type": "report",
        "suite": "N/A",
        "tasks": [],
        "policies": [],
        "episode_counts": 0,
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Audit reports verifying the mechanical and scientific validity of the H10 campaigns.",
        "source_report_paths": [
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md",
            "/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP8_LIBERO_PRO_SUITE_IDENTITY_20260609.md"
        ]
    },
    {
        "name": "workspace_experiment_catalog_reports",
        "host": "batman",
        "absolute_path": "/home/redafrix/tests/internship/fiper_ws/experiment_catalog",
        "date": "2026-06-09",
        "type": "report",
        "suite": "N/A",
        "tasks": [],
        "policies": [],
        "episode_counts": 0,
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Canonical catalog reports of all experiments, datasets, and hosts.",
        "source_report_paths": [
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/README.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/KEY_RESULTS.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/TRUSTED_RESULTS_SUMMARY.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/MASTER_EXPERIMENT_INDEX.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/DATASET_MAP.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/HOST_WORKSPACE_MAP.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/SYNC_STATUS.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/MODEL_AND_SUITE_IDENTITY.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/FORENSIC_AUDIT_MAP.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md",
            "/home/redafrix/tests/internship/fiper_ws/experiment_catalog/SAM_WORKSPACE_SCAN_20260609.md"
        ]
    },
    {
        "name": "dean_data_collection_roots",
        "host": "dean",
        "absolute_path": "/home/dean/fiper_goal_object_collection_20260605",
        "date": "2026-06-05",
        "type": "dataset",
        "suite": "libero_goal_object",
        "tasks": [],
        "policies": [],
        "episode_counts": {
            "exact_200": 200,
            "continuous_100000": 20154
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Goal-object production dataset. exact_200 is frozen; continuous is ongoing collection.",
        "source_report_paths": []
    },
    {
        "name": "sam_discovered_roots",
        "host": "sam",
        "absolute_path": "/home/rootalkhatib/test/reda_ws/fiper_ws",
        "date": "2026-06-09",
        "type": "archive",
        "suite": "libero_10_with_milk / libero_goal_swap",
        "tasks": [7, 8],
        "policies": ["baseline_simvla", "riskaware_actionmod_v2_strict"],
        "episode_counts": {
            "baseline_simvla_libero10_milk_task7": 100,
            "baseline_same_seed_4worker_task7": 450,
            "baseline_same_seed_4worker_task8": 429,
            "riskaware_4worker_task7": 450,
            "riskaware_4worker_task8": 429
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Historical raw evaluation results and reports stored on Sam.",
        "source_report_paths": [
            "/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/reports/SAM_WORKSPACE_SCAN_20260609.md"
        ]
    }
]

# Append or replace the entries
# Let's make sure we don't duplicate them if run multiple times. We can remove entries by name if they exist.
existing_names = [e["name"] for e in new_entries]
data["entries"] = [e for e in data["entries"] if e.get("name") not in existing_names]
data["entries"].extend(new_entries)

# Update generated_at
data["generated_at"] = datetime.now().isoformat()

with open(inventory_path, 'w') as f:
    json.dump(data, f, indent=2)

print("SUCCESS: Updated inventory.json with new structured entries")
