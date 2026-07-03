# Stage 9 VLM Label Audit Report

This audit uses VLM output only as a disagreement detector. It does not replace simulator metrics or same-state counterfactual evidence.

## Summary

- Results: `640`
- Suspicious labels: `481`
- Status counts: `{'ok': 640}`
- Model counts: `{'Qwen/Qwen3-VL-2B-Instruct': 320, 'Qwen/Qwen2.5-VL-3B-Instruct': 320}`
- Category counts: `{'bad_no_raw_local_bad': 80, 'bad_terminal_alt_only': 160, 'bad_terminal_timeout': 80, 'bad_with_local_good_progress': 80, 'ambiguous_random': 80, 'good_strong_random': 80, 'validated_bad_random': 80}`

## Behavior By Current Label

- `AMBIGUOUS`: `{'bad': 80}`
- `GOOD_STRONG`: `{'good': 55, 'bad': 25}`
- `VALIDATED_BAD`: `{'bad': 478, 'missing': 2}`

## Suggested Action By Current Label

- `AMBIGUOUS`: `{'downgrade_to_ambiguous': 69, 'upgrade_to_review': 11}`
- `GOOD_STRONG`: `{'keep': 59, 'downgrade_to_ambiguous': 20, 'upgrade_to_review': 1}`
- `VALIDATED_BAD`: `{'manual_review': 309, 'keep': 104, 'downgrade_to_ambiguous': 8, 'missing': 2, 'upgrade_to_review': 57}`

## Suspicious By Category

- `ambiguous_random`: `80`
- `bad_no_raw_local_bad`: `80`
- `bad_terminal_alt_only`: `110`
- `bad_terminal_timeout`: `77`
- `bad_with_local_good_progress`: `80`
- `good_strong_random`: `25`
- `validated_bad_random`: `29`

## Top Suspicious Examples

- `libero_10_with_mug_t2_r7_pTRANSPORT_s120_state_seed12` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t2_r7_pTRANSPORT_s120_state_seed12.jpg`
- `libero_10_with_mug_t3_r0_pTRANSPORT_s120_state_seed17` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t3_r0_pTRANSPORT_s120_state_seed17.jpg`
- `libero_10_with_mug_t3_r3_pTRANSPORT_s120_state_seed3` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t3_r3_pTRANSPORT_s120_state_seed3.jpg`
- `libero_10_with_mug_t3_r7_pPLACE_OR_GOAL_s136_state_seed20` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t3_r7_pPLACE_OR_GOAL_s136_state_seed20.jpg`
- `libero_10_with_mug_t3_r7_pTRANSPORT_s120_state_seed7` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t3_r7_pTRANSPORT_s120_state_seed7.jpg`
- `libero_10_with_mug_t4_r7_pSTUCK_OR_NO_PROGRESS_s120_state_seed9` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`misplacement` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t4_r7_pSTUCK_OR_NO_PROGRESS_s120_state_seed9.jpg`
- `libero_10_with_mug_t5_r0_pTRANSPORT_s136_state_seed13` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`object_drop` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t5_r0_pTRANSPORT_s136_state_seed13.jpg`
- `libero_10_with_mug_t5_r6_pSTUCK_OR_NO_PROGRESS_s81_state_seed21` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`object_drop` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t5_r6_pSTUCK_OR_NO_PROGRESS_s81_state_seed21.jpg`
- `libero_10_with_mug_t6_r0_pTRANSPORT_s136_state_seed2` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`misplacement` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t6_r0_pTRANSPORT_s136_state_seed2.jpg`
- `libero_10_with_mug_t6_r5_pTRANSPORT_s120_state_seed17` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t6_r5_pTRANSPORT_s120_state_seed17.jpg`
- `libero_10_with_mug_t7_r3_pSTUCK_OR_NO_PROGRESS_s120_state_seed9` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_10_with_mug_t7_r3_pSTUCK_OR_NO_PROGRESS_s120_state_seed9.jpg`
- `libero_goal_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s49_state_seed5` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s49_state_seed5.jpg`
- `libero_goal_with_mug_t0_r3_pSTUCK_OR_NO_PROGRESS_s58_state_seed21` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t0_r3_pSTUCK_OR_NO_PROGRESS_s58_state_seed21.jpg`
- `libero_goal_with_mug_t3_r0_pSTUCK_OR_NO_PROGRESS_s136_state_seed7` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t3_r0_pSTUCK_OR_NO_PROGRESS_s136_state_seed7.jpg`
- `libero_goal_with_mug_t4_r3_pPLACE_OR_GOAL_s76_state_seed27` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`misplacement` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t4_r3_pPLACE_OR_GOAL_s76_state_seed27.jpg`
- `libero_goal_with_mug_t4_r3_pPLACE_OR_GOAL_s76_state_seed4` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`misplacement` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t4_r3_pPLACE_OR_GOAL_s76_state_seed4.jpg`
- `libero_goal_with_mug_t4_r3_pPLACE_OR_GOAL_s76_state_seed7` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`misplacement` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t4_r3_pPLACE_OR_GOAL_s76_state_seed7.jpg`
- `libero_goal_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s67_state_seed31` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`misplacement` conf=`0.9` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s67_state_seed31.jpg`
- `libero_goal_with_mug_t5_r2_pSTUCK_OR_NO_PROGRESS_s93_state_seed26` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t5_r2_pSTUCK_OR_NO_PROGRESS_s93_state_seed26.jpg`
- `libero_goal_with_mug_t6_r0_pPLACE_OR_GOAL_s28_state_seed19` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t6_r0_pPLACE_OR_GOAL_s28_state_seed19.jpg`
- `libero_goal_with_mug_t6_r4_pSTUCK_OR_NO_PROGRESS_s52_state_seed1` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t6_r4_pSTUCK_OR_NO_PROGRESS_s52_state_seed1.jpg`
- `libero_goal_with_mug_t6_r4_pSTUCK_OR_NO_PROGRESS_s52_state_seed15` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t6_r4_pSTUCK_OR_NO_PROGRESS_s52_state_seed15.jpg`
- `libero_goal_with_mug_t6_r7_pPLACE_OR_GOAL_s26_state_seed22` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t6_r7_pPLACE_OR_GOAL_s26_state_seed22.jpg`
- `libero_goal_with_mug_t9_r3_pSTUCK_OR_NO_PROGRESS_s44_state_seed13` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t9_r3_pSTUCK_OR_NO_PROGRESS_s44_state_seed13.jpg`
- `libero_goal_with_mug_t9_r7_pSTUCK_OR_NO_PROGRESS_s53_state_seed15` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t9_r7_pSTUCK_OR_NO_PROGRESS_s53_state_seed15.jpg`
- `libero_object_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s120_state_seed12` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_object_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s120_state_seed12.jpg`
- `libero_object_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s120_state_seed3` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure_with_successful_same_state_alternative` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_object_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s120_state_seed3.jpg`
- `libero_object_with_mug_t1_r4_pTRANSPORT_s136_state_seed31` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`object_drop` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_object_with_mug_t1_r4_pTRANSPORT_s136_state_seed31.jpg`
- `libero_object_with_mug_t1_r4_pTRANSPORT_s136_state_seed6` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`object_drop` conf=`0.9` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_object_with_mug_t1_r4_pTRANSPORT_s136_state_seed6.jpg`
- `libero_object_with_mug_t4_r5_pGRASP_OR_LIFT_s71_state_seed17` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`bad` action=`manual_review` failure=`terminal_failure` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519/sheets/bad_no_raw_local_bad/libero_object_with_mug_t4_r5_pGRASP_OR_LIFT_s71_state_seed17.jpg`

## Decision

Any sample flagged here should be rechecked with simulator metrics and, if possible, replay video. VLM disagreement alone should downgrade to review, not create a final GOOD or BAD label.
