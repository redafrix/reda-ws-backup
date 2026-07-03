# Current FIPER Sweep Analysis Report

Generated: 2026-05-26 10:32:45

## Inputs

- `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/instance_A/fiper_receding_samples.jsonl`
- `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_eternal/instance_B/fiper_receding_samples.jsonl`

## Dataset

- Raw rows: 319730
- Used rows: 319730
- Excluded rows: 0
- Corrupt rows: 0
- Missing required rows: 0
- Episodes: 1961
- Episodes by outcome: `{'success': 1594, 'failure_or_timeout': 367}`
- Episode length avg/min/max: 163.04 / 67 / 300

## Schema Checks

- ACE candidate count distribution: `{8: 319730}`
- Main chunk shape distribution: `{'(10, 7)': 319730}`
- Executed action shape distribution: `{'(7,)': 319730}`
- ACE replay violations: 0
- First-action mismatches: 0 / 319730
- Unique main seeds: 319703
- Duplicate main seeds: 27
- Unique ACE seeds: 2556341
- Duplicate ACE seeds: 1499

## Splits

- Episodes by split: `{'failure_eval_all': 367, 'success_train': 1113, 'success_calib': 238, 'success_test_id': 243}`

Train/eval was not run. Re-run with `--run-train-eval` after freezing data.
