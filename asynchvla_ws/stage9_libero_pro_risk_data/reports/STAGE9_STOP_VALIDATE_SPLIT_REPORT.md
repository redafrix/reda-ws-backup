# Stage 9 Stop, Validate, Split Report

Generated: `2026-05-19T09:40:18`

## Executive Summary

- Collection was stopped gracefully: the watchdogs were stopped and Bob's in-flight chunk was allowed to finish before validation.
- Frozen dataset root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710`
- Freeze manifest/output directory: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940`
- Total samples: `37632`
- Total same-state groups: `4704`
- Total chunks with JSONL: `147`
- Incomplete chunks: `0`
- Corrupt JSONL rows: `0`
- DATASET_READY_FOR_TRAINING = YES

## Stop Status

- Bob process check after stop: `no matching process`
- Sam process check after stop: `no matching process`
- No hard kill was used for the Bob collector; the final chunk completed and was analyzed after the watchdog had been stopped.

## Freeze Snapshot

- Dataset root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710`
- Freeze directory: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940`
- Chunk manifest: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/chunk_manifest.json`
- Validation summary: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/validation_summary.json`
- Corrected label suggestions: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/corrected_label_suggestions.jsonl`
- Random review samples: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/random_review_samples.jsonl`

## Label Counts

| key | count |
|---|---:|
| `GOOD_STRONG` | 17930 |
| `AMBIGUOUS` | 9025 |
| `VALIDATED_BAD` | 6914 |
| `GOOD_WEAK` | 3763 |

## Raw Label Counts

| key | count |
|---|---:|
| `AMBIGUOUS` | 11082 |
| `GOOD_WEAK` | 9010 |
| `BAD` | 8773 |
| `GOOD_STRONG` | 8767 |

## VALIDATED_BAD Subtype Counts

| key | count |
|---|---:|
| `state_context` | 4044 |
| `action_specific` | 2870 |

## VALIDATED_BAD Reason Counts

| key | count |
|---|---:|
| `no_progress_strong` | 4694 |
| `repeated_same_state_failure_tail_no_progress` | 4120 |
| `terminal_failure_with_successful_same_state_alternative` | 2870 |
| `target_object_dropped` | 260 |
| `large_object_height_drop` | 113 |
| `target_object_moved_away_from_goal` | 1 |

## Task Counts

| key | count |
|---|---:|
| `libero_goal_with_mug_task0` | 1024 |
| `libero_goal_with_mug_task1` | 1024 |
| `libero_goal_with_mug_task2` | 1024 |
| `libero_goal_with_mug_task3` | 1024 |
| `libero_goal_with_mug_task4` | 1024 |
| `libero_goal_with_mug_task5` | 1024 |
| `libero_goal_with_mug_task6` | 1024 |
| `libero_object_with_mug_task0` | 1024 |
| `libero_object_with_mug_task1` | 1024 |
| `libero_object_with_mug_task2` | 1024 |
| `libero_object_with_mug_task3` | 1024 |
| `libero_object_with_mug_task4` | 1024 |
| `libero_object_with_mug_task5` | 1024 |
| `libero_object_with_mug_task6` | 1024 |
| `libero_object_with_mug_task7` | 1024 |
| `libero_object_with_mug_task8` | 1024 |
| `libero_object_with_mug_task9` | 1024 |
| `libero_spatial_with_mug_task0` | 1024 |
| `libero_spatial_with_mug_task1` | 1024 |
| `libero_spatial_with_mug_task2` | 1024 |
| `libero_spatial_with_mug_task3` | 1024 |
| `libero_spatial_with_mug_task4` | 1024 |
| `libero_spatial_with_mug_task5` | 1024 |
| `libero_spatial_with_mug_task6` | 1024 |
| `libero_spatial_with_mug_task7` | 1024 |
| `libero_spatial_with_mug_task8` | 1024 |
| `libero_spatial_with_mug_task9` | 1024 |
| `libero_10_with_mug_task0` | 768 |
| `libero_10_with_mug_task1` | 768 |
| `libero_10_with_mug_task2` | 768 |
| `libero_10_with_mug_task3` | 768 |
| `libero_10_with_mug_task4` | 768 |
| `libero_10_with_mug_task5` | 768 |
| `libero_10_with_mug_task6` | 768 |
| `libero_10_with_mug_task7` | 768 |
| `libero_10_with_mug_task8` | 768 |
| `libero_10_with_mug_task9` | 768 |
| `libero_goal_with_mug_task7` | 768 |
| `libero_goal_with_mug_task8` | 768 |
| `libero_goal_with_mug_task9` | 768 |

## Phase Counts

| key | count |
|---|---:|
| `STUCK_OR_NO_PROGRESS` | 15472 |
| `TRANSPORT` | 14968 |
| `PLACE_OR_GOAL` | 4568 |
| `NEAR_GRASP` | 1496 |
| `GRASP_OR_LIFT` | 1080 |
| `APPROACH` | 48 |

## Perturbation Counts

| key | count |
|---|---:|
| `instruction_or_goal` | 17152 |
| `initial_position` | 10240 |
| `object` | 10240 |

## Trace Completeness

| key | count |
|---|---:|
| `terminal_before_horizon` | 26602 |
| `full_horizon` | 11030 |

## Frame Path Count Distribution

| key | count |
|---|---:|
| `0` | 37632 |

## Integrity And Label Checks

| check | result |
|---|---:|
| `allowed_labels_only` | `True` |
| `chunks_complete` | `True` |
| `h40_trace_complete_or_terminal_before_h` | `True` |
| `has_good_strong` | `True` |
| `has_validated_bad` | `True` |
| `json_parse_clean` | `True` |
| `label_evidence_present` | `True` |
| `no_duplicate_sample_ids` | `True` |
| `no_eef_away_only_validated_bad` | `True` |
| `no_suspicious_good_or_bad` | `True` |
| `no_unknown_validated_bad` | `True` |
| `same_state_comparison_present` | `True` |
| `same_state_groups_complete` | `True` |
| `training_eligible_samples` | `24844` |

- Duplicate sample IDs: `0`
- Missing sample IDs: `0`
- Same-state group issues: `0`
- Suspicious GOOD_STRONG / VALIDATED_BAD samples: `0`
- All suspicious samples across all labels: `0`

## Correctness Audit

- `VALIDATED_BAD` was required to have a known subtype, non-empty strong reason, terminal-failure evidence, trace evidence, same-state comparison, and no EEF-away-only reason.
- `GOOD_STRONG` was required to have terminal-success evidence and label evidence.
- Parent episode failure/timeout was checked as metadata only; parent-only reasons were treated as invalid.
- Same-state groups were required to contain eight real SimVLA seed candidates with matching comparison metadata.
- Suspicious strong labels were assigned corrected suggestions to `AMBIGUOUS`; no label was upgraded to BAD during this audit.

## Random Review Sample

| label | sample_id | task | phase | seed | reasons | terminal_success | terminal_failure | trace_len |
|---|---|---|---|---:|---|---:|---:|---:|
| `AMBIGUOUS` | `libero_10_with_mug_t9_r1_pTRANSPORT_s136_state_seed8` | `libero_10_with_mug_task9` | `TRANSPORT` | `8` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_object_with_mug_t3_r2_pSTUCK_OR_NO_PROGRESS_s145_state_seed13` | `libero_object_with_mug_task3` | `STUCK_OR_NO_PROGRESS` | `13` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_object_with_mug_t8_r6_pTRANSPORT_s94_state_seed22` | `libero_object_with_mug_task8` | `TRANSPORT` | `22` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_goal_with_mug_t1_r2_pTRANSPORT_s120_state_seed12` | `libero_goal_with_mug_task1` | `TRANSPORT` | `12` | `terminal_outcome_ambiguous` | `False` | `True` | `40` |
| `AMBIGUOUS` | `libero_spatial_with_mug_t5_r6_pSTUCK_OR_NO_PROGRESS_s120_state_seed7` | `libero_spatial_with_mug_task5` | `STUCK_OR_NO_PROGRESS` | `7` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_10_with_mug_t7_r1_pSTUCK_OR_NO_PROGRESS_s136_state_seed23` | `libero_10_with_mug_task7` | `STUCK_OR_NO_PROGRESS` | `23` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_goal_with_mug_t5_r2_pTRANSPORT_s144_state_seed22` | `libero_goal_with_mug_task5` | `TRANSPORT` | `22` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_spatial_with_mug_t0_r1_pTRANSPORT_s120_state_seed11` | `libero_spatial_with_mug_task0` | `TRANSPORT` | `11` | `terminal_outcome_ambiguous` | `False` | `True` | `40` |
| `AMBIGUOUS` | `libero_spatial_with_mug_t4_r1_pTRANSPORT_s117_state_seed15` | `libero_spatial_with_mug_task4` | `TRANSPORT` | `15` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_object_with_mug_t1_r2_pTRANSPORT_s146_state_seed30` | `libero_object_with_mug_task1` | `TRANSPORT` | `30` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_10_with_mug_t9_r3_pSTUCK_OR_NO_PROGRESS_s136_state_seed14` | `libero_10_with_mug_task9` | `STUCK_OR_NO_PROGRESS` | `14` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `AMBIGUOUS` | `libero_goal_with_mug_t6_r0_pPLACE_OR_GOAL_s80_state_seed1` | `libero_goal_with_mug_task6` | `PLACE_OR_GOAL` | `1` | `terminal_outcome_ambiguous` | `False` | `True` | `1` |
| `GOOD_STRONG` | `libero_goal_with_mug_t7_r2_pTRANSPORT_s25_state_seed15` | `libero_goal_with_mug_task7` | `TRANSPORT` | `15` | `terminal_success_under_policy_continuation` | `True` | `False` | `40` |
| `GOOD_STRONG` | `libero_goal_with_mug_t4_r7_pPLACE_OR_GOAL_s86_state_seed2` | `libero_goal_with_mug_task4` | `PLACE_OR_GOAL` | `2` | `terminal_success_under_policy_continuation` | `True` | `False` | `6` |
| `GOOD_STRONG` | `libero_object_with_mug_t3_r2_pNEAR_GRASP_s46_state_seed18` | `libero_object_with_mug_task3` | `NEAR_GRASP` | `18` | `terminal_success_under_policy_continuation` | `True` | `False` | `40` |
| `GOOD_STRONG` | `libero_goal_with_mug_t5_r6_pTRANSPORT_s32_state_seed4` | `libero_goal_with_mug_task5` | `TRANSPORT` | `4` | `terminal_success_under_policy_continuation` | `True` | `False` | `40` |

## VALIDATED_BAD Examples

| sample_id | subtype | task | phase | reasons | terminal_failure | same-state summary |
|---|---|---|---|---|---:|---|
| `libero_10_with_mug_t6_r5_pTRANSPORT_s148_state_seed1` | `state_context` | `libero_10_with_mug_task6` | `TRANSPORT` | `no_progress_strong,repeated_same_state_failure_tail_no_progress` | `True` | `success_alt=False, fail_count=8/8` |
| `libero_10_with_mug_t8_r6_pSTUCK_OR_NO_PROGRESS_s148_state_seed20` | `state_context` | `libero_10_with_mug_task8` | `STUCK_OR_NO_PROGRESS` | `no_progress_strong,repeated_same_state_failure_tail_no_progress` | `True` | `success_alt=False, fail_count=8/8` |
| `libero_goal_with_mug_t0_r2_pSTUCK_OR_NO_PROGRESS_s159_state_seed3` | `state_context` | `libero_goal_with_mug_task0` | `STUCK_OR_NO_PROGRESS` | `no_progress_strong,repeated_same_state_failure_tail_no_progress` | `True` | `success_alt=False, fail_count=8/8` |
| `libero_spatial_with_mug_t7_r3_pSTUCK_OR_NO_PROGRESS_s60_state_seed12` | `action_specific` | `libero_spatial_with_mug_task7` | `STUCK_OR_NO_PROGRESS` | `no_progress_strong,terminal_failure_with_successful_same_state_alternative` | `True` | `success_alt=False, fail_count=6/8` |
| `libero_10_with_mug_t5_r4_pSTUCK_OR_NO_PROGRESS_s159_state_seed23` | `state_context` | `libero_10_with_mug_task5` | `STUCK_OR_NO_PROGRESS` | `no_progress_strong,repeated_same_state_failure_tail_no_progress` | `True` | `success_alt=False, fail_count=8/8` |
| `libero_10_with_mug_t3_r1_pSTUCK_OR_NO_PROGRESS_s159_state_seed5` | `state_context` | `libero_10_with_mug_task3` | `STUCK_OR_NO_PROGRESS` | `no_progress_strong,repeated_same_state_failure_tail_no_progress` | `True` | `success_alt=False, fail_count=8/8` |
| `libero_object_with_mug_t7_r4_pSTUCK_OR_NO_PROGRESS_s120_state_seed6` | `action_specific` | `libero_object_with_mug_task7` | `STUCK_OR_NO_PROGRESS` | `terminal_failure_with_successful_same_state_alternative` | `True` | `success_alt=True, fail_count=7/8` |
| `libero_goal_with_mug_t9_r5_pSTUCK_OR_NO_PROGRESS_s148_state_seed4` | `state_context` | `libero_goal_with_mug_task9` | `STUCK_OR_NO_PROGRESS` | `no_progress_strong,repeated_same_state_failure_tail_no_progress` | `True` | `success_alt=False, fail_count=8/8` |

## GOOD_STRONG Examples

| sample_id | task | phase | reasons | terminal_success | reward_sum_H | trace_len |
|---|---|---|---|---:|---:|---:|
| `libero_goal_with_mug_t7_r2_pTRANSPORT_s25_state_seed15` | `libero_goal_with_mug_task7` | `TRANSPORT` | `terminal_success_under_policy_continuation` | `True` | `0.0` | `40` |
| `libero_goal_with_mug_t4_r7_pPLACE_OR_GOAL_s86_state_seed2` | `libero_goal_with_mug_task4` | `PLACE_OR_GOAL` | `terminal_success_under_policy_continuation` | `True` | `1.0` | `6` |
| `libero_object_with_mug_t3_r2_pNEAR_GRASP_s46_state_seed18` | `libero_object_with_mug_task3` | `NEAR_GRASP` | `terminal_success_under_policy_continuation` | `True` | `0.0` | `40` |
| `libero_goal_with_mug_t5_r6_pTRANSPORT_s32_state_seed4` | `libero_goal_with_mug_task5` | `TRANSPORT` | `terminal_success_under_policy_continuation` | `True` | `0.0` | `40` |
| `libero_spatial_with_mug_t1_r5_pTRANSPORT_s50_state_seed17` | `libero_spatial_with_mug_task1` | `TRANSPORT` | `terminal_success_under_policy_continuation` | `True` | `0.0` | `40` |
| `libero_goal_with_mug_t9_r0_pTRANSPORT_s112_state_seed7` | `libero_goal_with_mug_task9` | `TRANSPORT` | `terminal_success_under_policy_continuation` | `True` | `1.0` | `32` |
| `libero_object_with_mug_t8_r6_pNEAR_GRASP_s33_state_seed27` | `libero_object_with_mug_task8` | `NEAR_GRASP` | `terminal_success_under_policy_continuation` | `True` | `0.0` | `40` |
| `libero_spatial_with_mug_t8_r6_pTRANSPORT_s30_state_seed24` | `libero_spatial_with_mug_task8` | `TRANSPORT` | `terminal_success_under_policy_continuation` | `True` | `0.0` | `40` |

## Suspicious Samples

- None found by the strict audit.

## Splits

- Split directory: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/frozen/stage9_stop_validate_20260519_093940/splits`
- Unseen perturbation holdout: `initial_position`
- Unseen task holdouts: `['libero_10_with_mug_task8', 'libero_10_with_mug_task9', 'libero_goal_with_mug_task8', 'libero_goal_with_mug_task9', 'libero_object_with_mug_task8', 'libero_object_with_mug_task9', 'libero_spatial_with_mug_task8', 'libero_spatial_with_mug_task9']`
- Unseen seed holdouts: `[7, 15, 23, 31]`

| split | samples | GOOD_STRONG | VALIDATED_BAD | GOOD_WEAK | AMBIGUOUS |
|---|---:|---:|---:|---:|---:|
| `calib` | 2709 | 1337 | 518 | 185 | 669 |
| `test_seen_task` | 1806 | 762 | 344 | 190 | 510 |
| `test_unseen_perturbation` | 10240 | 6646 | 1521 | 211 | 1862 |
| `test_unseen_seed` | 2784 | 1055 | 678 | 268 | 783 |
| `test_unseen_task` | 5120 | 1707 | 1070 | 1034 | 1309 |
| `train` | 14973 | 6423 | 2783 | 1875 | 3892 |

## Blockers

- none

## Final Decision

DATASET_READY_FOR_TRAINING = YES

