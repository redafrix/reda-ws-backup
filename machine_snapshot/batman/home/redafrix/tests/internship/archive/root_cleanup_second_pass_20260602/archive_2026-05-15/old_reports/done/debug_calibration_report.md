# Debug Calibration Report

- Dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`
- Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/debug_rater/debug_rater.pt`
- Calibration split size rows: `240`
- Calibration split contexts: `40`
- Method: conformal residual correction, `calibrated_uncertainty = predicted_error + eta`.

## Summary JSON

```json
{
  "calibration_rows": 240,
  "calibration_contexts": 40,
  "eta_90": 0.32035860419273376,
  "empirical_coverage": 0.9,
  "mean_predicted_error": 0.864186704158783,
  "mean_calibrated_uncertainty": 1.1845453977584839,
  "risk_coverage_before": [
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
  "risk_coverage_after": [
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
  ]
}
```

## Coverage Per Candidate Type

- `expert_action`: n=`40`, coverage=`1.0000`, mean_true=`0.000000`, mean_pred=`0.075170`, mean_calibrated=`0.395528`
- `other_demo_or_other_task`: n=`40`, coverage=`0.9750`, mean_true=`0.996455`, mean_pred=`0.997409`, mean_calibrated=`1.317767`
- `perturb_large`: n=`40`, coverage=`0.4250`, mean_true=`1.899449`, mean_pred=`1.403387`, mean_calibrated=`1.723746`
- `perturb_small`: n=`40`, coverage=`1.0000`, mean_true=`0.250854`, mean_pred=`0.145033`, mean_calibrated=`0.465391`
- `same_task_far`: n=`40`, coverage=`1.0000`, mean_true=`0.811364`, mean_pred=`0.847804`, mean_calibrated=`1.168163`
- `simvla_seed0`: n=`40`, coverage=`1.0000`, mean_true=`1.678478`, mean_pred=`1.716317`, mean_calibrated=`2.036676`
