---
{
  "session_id": "ood-generalization-20260504",
  "task": "Implement and evaluate OOD generalization improvements (Exp 04-07) for TDQC Calibrator.",
  "created": "2026-05-04T11:25:50.698Z",
  "updated": "2026-05-06T07:34:02.501Z",
  "status": "completed",
  "workflow_mode": "standard",
  "design_document": "/home/redafrix/tests/intern_ship_research/docs/maestro/plans/ood_generalization_design.md",
  "implementation_plan": null,
  "current_phase": 3,
  "total_phases": 8,
  "execution_mode": null,
  "execution_backend": "native",
  "current_batch": null,
  "task_complexity": "complex",
  "token_usage": {
    "total_input": 0,
    "total_output": 0,
    "total_cached": 0,
    "by_agent": {}
  },
  "phases": [
    {
      "id": 1,
      "name": "ood_prep",
      "status": "completed",
      "agents": [
        "coder"
      ],
      "parallel": false,
      "started": "2026-05-04T11:25:50.698Z",
      "completed": "2026-05-04T11:29:27.494Z",
      "blocked_by": [],
      "files_created": [
        "core/phase2_tdqc/build_dataset_v7_22d.py",
        "data/v7_22d/v7_22d_train.pt",
        "data/v7_22d/v7_22d_val.pt",
        "data/v7_22d/v7_22d_test.pt",
        "data/v7_22d/v7_22d_ood.pt"
      ],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [],
      "downstream_context": {
        "key_interfaces_introduced": [
          "core/phase2_tdqc/build_dataset_v7_22d.py script for generating 22D features."
        ],
        "patterns_established": [
          "Concatenation of raw features with their temporal deltas."
        ],
        "integration_points": [
          "The 22D dataset is saved in data/v7_22d/. Use these for Exp04.",
          "tdqc_model.py needs to be updated for 22D input and InstanceNorm1d."
        ],
        "assumptions": [
          "Deltas for t=0 are exactly zero.",
          "Features [0:11] are raw, [11:22] are deltas."
        ],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0,
      "requires_reconciliation": false
    },
    {
      "id": 2,
      "name": "dataset_gen",
      "status": "pending",
      "agents": [
        "generalist"
      ],
      "parallel": false,
      "started": null,
      "completed": null,
      "blocked_by": [
        1
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [
        "data/v7/v7_22d_train.pt",
        "data/v7/v7_22d_val.pt",
        "data/v7/v7_22d_test.pt",
        "data/v7/v7_22d_ood_test.pt"
      ],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    },
    {
      "id": 3,
      "name": "exp04_setup",
      "status": "in_progress",
      "agents": [
        "coder"
      ],
      "parallel": false,
      "started": "2026-05-04T11:29:27.494Z",
      "completed": null,
      "blocked_by": [
        2
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [
        "experiments/v7_exp04_delta_instnorm/code/phase2_tdqc/tdqc_model.py"
      ],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    },
    {
      "id": 4,
      "name": "exp04_train",
      "status": "pending",
      "agents": [
        "generalist"
      ],
      "parallel": false,
      "started": null,
      "completed": null,
      "blocked_by": [
        3
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [
        "experiments/v7_exp04_delta_instnorm/runs/best.pt"
      ],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    },
    {
      "id": 5,
      "name": "exp04_eval",
      "status": "pending",
      "agents": [
        "tester"
      ],
      "parallel": false,
      "started": null,
      "completed": null,
      "blocked_by": [
        4
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [
        "experiments/v7_exp04_delta_instnorm/analysis/eval_results_standard.txt",
        "experiments/v7_exp04_delta_instnorm/analysis/eval_results_ood.txt"
      ],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    },
    {
      "id": 6,
      "name": "exp05_dann",
      "status": "pending",
      "agents": [
        "coder"
      ],
      "parallel": false,
      "started": null,
      "completed": null,
      "blocked_by": [
        5
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    },
    {
      "id": 7,
      "name": "exp06_contrastive",
      "status": "pending",
      "agents": [
        "coder"
      ],
      "parallel": false,
      "started": null,
      "completed": null,
      "blocked_by": [
        6
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    },
    {
      "id": 8,
      "name": "exp07_custom",
      "status": "pending",
      "agents": [
        "coder"
      ],
      "parallel": false,
      "started": null,
      "completed": null,
      "blocked_by": [
        7
      ],
      "files_created": [],
      "files_modified": [],
      "files_deleted": [],
      "planned_files": [],
      "downstream_context": {
        "key_interfaces_introduced": [],
        "patterns_established": [],
        "integration_points": [],
        "assumptions": [],
        "warnings": []
      },
      "errors": [],
      "retry_count": 0
    }
  ]
}
---
# Implement and evaluate OOD generalization improvements (Exp 04-07) for TDQC Calibrator. Orchestration Log
