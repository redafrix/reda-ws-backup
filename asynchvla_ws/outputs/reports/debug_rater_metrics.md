# Debug Rater Metrics

- Dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`
- Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt`
- Train contexts: `160`
- Validation contexts: `40`
- Train rows: `960`
- Validation rows: `240`
- Split rule: by `context_id`; no context appears in both train and validation.
- Target: chunk-level normalized action L2 error.
- Full input: pooled VLM features + proprio + candidate action.
- Context baseline input: pooled VLM features + proprio only.
- Action baseline input: candidate action only.
- Critical success condition met: `True`

## Metrics JSON

```json
{
  "full": {
    "pearson": 0.9247123003005981,
    "spearman": 0.9127852854049705,
    "auroc_top30_bad": 0.9372519841269841,
    "mse": 0.0844452902674675,
    "mae": 0.1540125012397766,
    "risk_coverage": [
      [
        0.1,
        0.07786501199007034
      ],
      [
        0.25,
        0.091851606965065
      ],
      [
        0.5,
        0.3230048716068268
      ],
      [
        0.75,
        0.6465259790420532
      ],
      [
        1.0,
        0.9394332766532898
      ]
    ],
    "expert_lt_perturb_large": 1.0,
    "expert_lt_other_task": 0.975,
    "expert_lt_same_task_far": 1.0,
    "expert_lt_simvla": 1.0,
    "simvla_pairwise_true_order_accuracy": 0.8625,
    "action_sensitivity_avg_pred_std_same_context": 0.6570668966730115
  },
  "context": {
    "pearson": 0.11169809848070145,
    "spearman": 0.08863473362012958,
    "auroc_top30_bad": 0.5337301587301587,
    "mse": 0.5634625554084778,
    "mae": 0.6299929022789001,
    "risk_coverage": [
      [
        0.1,
        0.8472843170166016
      ],
      [
        0.25,
        0.8600943088531494
      ],
      [
        0.5,
        0.8733155727386475
      ],
      [
        0.75,
        0.900708019733429
      ],
      [
        1.0,
        0.9394332766532898
      ]
    ],
    "expert_lt_perturb_large": 0.0,
    "expert_lt_other_task": 0.0,
    "expert_lt_same_task_far": 0.0,
    "expert_lt_simvla": 0.0,
    "simvla_pairwise_true_order_accuracy": 0.775,
    "action_sensitivity_avg_pred_std_same_context": 0.0
  },
  "action": {
    "pearson": 0.8275177478790283,
    "spearman": 0.7268669887076941,
    "auroc_top30_bad": 0.964905753968254,
    "mse": 0.17187699675559998,
    "mae": 0.2743626832962036,
    "risk_coverage": [
      [
        0.1,
        0.5096613764762878
      ],
      [
        0.25,
        0.396089106798172
      ],
      [
        0.5,
        0.47591277956962585
      ],
      [
        0.75,
        0.6212962865829468
      ],
      [
        1.0,
        0.9394332766532898
      ]
    ],
    "expert_lt_perturb_large": 0.975,
    "expert_lt_other_task": 0.475,
    "expert_lt_same_task_far": 0.725,
    "expert_lt_simvla": 1.0,
    "simvla_pairwise_true_order_accuracy": 0.91875,
    "action_sensitivity_avg_pred_std_same_context": 0.610025018480904
  }
}
```
