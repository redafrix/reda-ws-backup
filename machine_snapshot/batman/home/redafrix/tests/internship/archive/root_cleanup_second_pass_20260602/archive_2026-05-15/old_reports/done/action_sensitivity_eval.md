# Action Sensitivity Evaluation

- Dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`
- Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt`
- Held-out validation contexts: `40`

## Results JSON

```json
{
  "validation_contexts": 40,
  "validation_rows": 240,
  "type_summary": {
    "expert_action": {
      "n": 40,
      "mean_pred_uncertainty": 0.07516987659037114,
      "mean_true_error": 0.0
    },
    "simvla_seed0": {
      "n": 40,
      "mean_pred_uncertainty": 1.7163172960281372,
      "mean_true_error": 1.6784774482250213
    },
    "perturb_small": {
      "n": 40,
      "mean_pred_uncertainty": 0.14503278099000455,
      "mean_true_error": 0.25085412003099916
    },
    "perturb_large": {
      "n": 40,
      "mean_pred_uncertainty": 1.4033871360123158,
      "mean_true_error": 1.8994492262601852
    },
    "same_task_far": {
      "n": 40,
      "mean_pred_uncertainty": 0.847804456949234,
      "mean_true_error": 0.811363835260272
    },
    "other_demo_or_other_task": {
      "n": 40,
      "mean_pred_uncertainty": 0.9974087877199054,
      "mean_true_error": 0.9964550018310547
    }
  },
  "ranking_matrix_pred_less_probability": {
    "expert_action": {
      "expert_action": null,
      "perturb_small": 0.9,
      "same_task_far": 1.0,
      "other_demo_or_other_task": 0.975,
      "simvla_seed0": 1.0,
      "perturb_large": 1.0
    },
    "perturb_small": {
      "expert_action": 0.1,
      "perturb_small": null,
      "same_task_far": 0.975,
      "other_demo_or_other_task": 1.0,
      "simvla_seed0": 1.0,
      "perturb_large": 1.0
    },
    "same_task_far": {
      "expert_action": 0.0,
      "perturb_small": 0.025,
      "same_task_far": null,
      "other_demo_or_other_task": 0.6,
      "simvla_seed0": 0.975,
      "perturb_large": 0.95
    },
    "other_demo_or_other_task": {
      "expert_action": 0.025,
      "perturb_small": 0.0,
      "same_task_far": 0.4,
      "other_demo_or_other_task": null,
      "simvla_seed0": 0.925,
      "perturb_large": 0.775
    },
    "simvla_seed0": {
      "expert_action": 0.0,
      "perturb_small": 0.0,
      "same_task_far": 0.025,
      "other_demo_or_other_task": 0.075,
      "simvla_seed0": null,
      "perturb_large": 0.25
    },
    "perturb_large": {
      "expert_action": 0.0,
      "perturb_small": 0.0,
      "same_task_far": 0.05,
      "other_demo_or_other_task": 0.225,
      "simvla_seed0": 0.75,
      "perturb_large": null
    }
  },
  "num_failures_recorded": 1,
  "first_failures": [
    {
      "context_id": "ctx_000012",
      "case": "expert_not_below_other_task",
      "expert_pred": 0.05721167474985123,
      "other_pred": 0.055512167513370514,
      "task": "close the top drawer of the cabinet"
    }
  ],
  "appears_to_ignore_actions": false
}
```
