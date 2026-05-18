# Stage 9 Pilot Collection Report

Three pilot passes were run. v1 used strict no-object-progress labels and collapsed to BAD. v2/v3 added approach-progress evidence and collapsed to GOOD. This proves mechanics work but labels are not yet valid for final data.

```json
[
  {
    "num_samples": 72,
    "label_counts": {
      "BAD": 72
    },
    "out_dir": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual",
    "suites": [
      "libero_object_with_mug",
      "libero_spatial_with_mug",
      "libero_goal_with_mug"
    ],
    "task_ids": [
      0,
      1
    ],
    "states_per_task": 3,
    "simvla_seeds": [
      0,
      1,
      2,
      3
    ],
    "horizon": 10,
    "history_k": 4
  },
  {
    "num_samples": 72,
    "label_counts": {
      "GOOD": 72
    },
    "out_dir": "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual_v2",
    "suites": [
      "libero_object_with_mug",
      "libero_spatial_with_mug",
      "libero_goal_with_mug"
    ],
    "task_ids": [
      0,
      1
    ],
    "states_per_task": 3,
    "simvla_seeds": [
      0,
      1,
      2,
      3
    ],
    "horizon": 20,
    "history_k": 4
  },
  {
    "num_samples": 96,
    "label_counts": {
      "GOOD": 96
    },
    "out_dir": "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/later_state_counterfactual_v1",
    "suites": [
      "libero_object_with_mug",
      "libero_spatial_with_mug",
      "libero_goal_with_mug"
    ],
    "task_ids": [
      0
    ],
    "states_per_task": 8,
    "simvla_seeds": [
      0,
      1,
      2,
      3
    ],
    "horizon": 20,
    "history_k": 4
  }
]
```
