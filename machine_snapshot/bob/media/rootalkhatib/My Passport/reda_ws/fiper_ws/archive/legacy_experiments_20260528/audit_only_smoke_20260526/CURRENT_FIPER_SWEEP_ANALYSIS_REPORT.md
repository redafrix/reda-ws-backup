# Current FIPER Sweep Analysis Report

Generated: 2026-05-26 10:35:05

## Inputs

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/instance_A/fiper_receding_samples.jsonl`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/instance_B/fiper_receding_samples.jsonl`

## Dataset

- Raw rows: 316191
- Used rows: 316191
- Excluded rows: 0
- Corrupt rows: 0
- Missing required rows: 0
- Episodes: 2260
- Episodes by outcome: `{'success': 2055, 'failure_or_timeout': 205}`
- Episode length avg/min/max: 139.91 / 66 / 300

## Schema Checks

- ACE candidate count distribution: `{8: 316191}`
- Main chunk shape distribution: `{'(10, 7)': 316191}`
- Executed action shape distribution: `{'(7,)': 316191}`
- ACE replay violations: 0
- First-action mismatches: 0 / 316191
- Unique main seeds: 316163
- Duplicate main seeds: 28
- Unique ACE seeds: 2527959
- Duplicate ACE seeds: 1569

## Splits

- Episodes by split: `{'failure_eval_all': 205, 'success_train': 1442, 'success_calib': 312, 'success_test_id': 301}`

Train/eval was not run. Re-run with `--run-train-eval` after freezing data.
