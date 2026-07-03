# FIPER Dataset Preparation Report

This report summarizes the data validation and selection results on Bob.

## Source Information
- **Source JSONL**: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`
- **Total Source Rows**: 1060884
- **Total Unique Source Episodes**: 4469
- **Corrupt Rows**: 0
- **NaN/Inf Rows (in checked sample)**: 0

## Selection Parameters
- **Seed**: `20260701`
- **Total Target Episodes**: ~900 (successes: 800, failures: up to 100)

## Selected Subset Statistics
- **Total Selected Episodes**: 900
- **Total Selected Rows**: 194643
- **Unique State Files Required**: 194643

## Destination Paths
- **Workspace Destination**: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/seen_goal_object_fiper_subset`
- **Generated Files**:
  - `selected_episodes.json`
  - `selected_rows.jsonl`
  - `state_transfer_manifest.txt`
  - `SPLIT_SUMMARY.md`
  - `PREP_REPORT.md`
  - `states/` (to be transferred from Sam)
