# FIPER Archive

Created: 2026-05-28

This archive keeps rejected, legacy, smoke, and outdated data/experiment
artifacts without deleting them.

Current active baseline remains at top level:

- `current_baseline/`
- `configs/current_baseline_v2_018_transformer_k16.json`
- `data/frozen/fiper_sweep_eternal_20260527_combined/`
- `data/manifests/fiper_sweep_eternal_20260527_combined/`
- `experiments/prepared_20260527/`
- `experiments/clean_temporal_nextgen_v2_full_all_20260527/`
- `experiments/transformer_k16_online_policy_sweep_20260528/`
- `experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528/`
- `experiments/transformer_capacity_history_sweep_fold00_v1_20260528/`
- `experiments/transformer_capacity_history_small_sweep_fold00_v1_20260528/`

Do not train from archived `20260526` snapshots unless deliberately reproducing
old results. The current split/data generation is based on the 20260527 combined
dataset.
