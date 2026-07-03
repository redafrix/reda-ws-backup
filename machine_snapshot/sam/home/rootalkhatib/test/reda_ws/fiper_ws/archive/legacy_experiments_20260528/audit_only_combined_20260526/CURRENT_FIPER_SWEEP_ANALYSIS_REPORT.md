# Current FIPER Sweep Analysis Report

Generated: 2026-05-26 11:26:47

## Inputs

- `data/frozen/fiper_sweep_eternal_20260526_combined/sam_instance_A/fiper_receding_samples.jsonl`
- `data/frozen/fiper_sweep_eternal_20260526_combined/sam_instance_B/fiper_receding_samples.jsonl`
- `data/frozen/fiper_sweep_eternal_20260526_combined/bob_instance_A/fiper_receding_samples.jsonl`
- `data/frozen/fiper_sweep_eternal_20260526_combined/bob_instance_B/fiper_receding_samples.jsonl`

## Dataset

- Raw rows: 635921
- Used rows: 635921
- Excluded rows: 0
- Corrupt rows: 0
- Missing required rows: 0
- Episodes: 4221
- Episodes by outcome: `{'success': 3649, 'failure_or_timeout': 572}`
- Episode length avg/min/max: 150.66 / 66 / 300

## Schema Checks

- ACE candidate count distribution: `{8: 635921}`
- Main chunk shape distribution: `{'(10, 7)': 635921}`
- Executed action shape distribution: `{'(7,)': 635921}`
- ACE replay violations: 0
- First-action mismatches: 0 / 635921
- Unique main seeds: 635826
- Duplicate main seeds: 95
- Unique ACE seeds: 5081284
- Duplicate ACE seeds: 6084

## Splits

- Episodes by split: `{'failure_eval_all': 572, 'success_train': 2555, 'success_calib': 550, 'success_test_id': 544}`

Train/eval was not run. Re-run with `--run-train-eval` after freezing data.
