# Stage 9 VLM Label Audit Report

This audit uses VLM output only as a disagreement detector. It does not replace simulator metrics or same-state counterfactual evidence.

## Summary

- Results: `320`
- Suspicious labels: `312`
- Status counts: `{'ok': 320}`
- Model counts: `{'Qwen/Qwen3-VL-2B-Instruct': 160, 'Qwen/Qwen2.5-VL-3B-Instruct': 160}`
- Category counts: `{'bad_no_raw_local_bad': 40, 'bad_terminal_alt_only': 80, 'bad_terminal_timeout': 40, 'bad_with_local_good_progress': 40, 'ambiguous_random': 40, 'good_strong_random': 40, 'validated_bad_random': 40}`

## Behavior By Current Label

- `AMBIGUOUS`: `{'bad': 40}`
- `GOOD_STRONG`: `{'bad': 40}`
- `VALIDATED_BAD`: `{'good': 160, 'bad': 80}`

## Suggested Action By Current Label

- `AMBIGUOUS`: `{'keep': 22, 'downgrade_to_ambiguous': 18}`
- `GOOD_STRONG`: `{'downgrade_to_ambiguous': 15, 'keep': 25}`
- `VALIDATED_BAD`: `{'keep': 207, 'manual_review': 1, 'upgrade_to_review': 1, 'downgrade_to_ambiguous': 31}`

## Suspicious By Category

- `ambiguous_random`: `36`
- `bad_no_raw_local_bad`: `40`
- `bad_terminal_alt_only`: `78`
- `bad_terminal_timeout`: `40`
- `bad_with_local_good_progress`: `40`
- `good_strong_random`: `40`
- `validated_bad_random`: `38`

## Top Suspicious Examples

- `libero_10_with_mug_t2_r0_pTRANSPORT_s120_state_seed17` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t2_r0_pTRANSPORT_s120_state_seed17.jpg`
- `libero_10_with_mug_t3_r0_pTRANSPORT_s120_state_seed6` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t3_r0_pTRANSPORT_s120_state_seed6.jpg`
- `libero_10_with_mug_t3_r7_pTRANSPORT_s120_state_seed12` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t3_r7_pTRANSPORT_s120_state_seed12.jpg`
- `libero_10_with_mug_t4_r0_pSTUCK_OR_NO_PROGRESS_s120_state_seed7` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t4_r0_pSTUCK_OR_NO_PROGRESS_s120_state_seed7.jpg`
- `libero_10_with_mug_t5_r0_pTRANSPORT_s136_state_seed9` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t5_r0_pTRANSPORT_s136_state_seed9.jpg`
- `libero_10_with_mug_t6_r0_pTRANSPORT_s136_state_seed13` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t6_r0_pTRANSPORT_s136_state_seed13.jpg`
- `libero_10_with_mug_t6_r0_pTRANSPORT_s136_state_seed22` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t6_r0_pTRANSPORT_s136_state_seed22.jpg`
- `libero_10_with_mug_t7_r3_pSTUCK_OR_NO_PROGRESS_s120_state_seed12` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_10_with_mug_t7_r3_pSTUCK_OR_NO_PROGRESS_s120_state_seed12.jpg`
- `libero_goal_with_mug_t0_r3_pSTUCK_OR_NO_PROGRESS_s58_state_seed14` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t0_r3_pSTUCK_OR_NO_PROGRESS_s58_state_seed14.jpg`
- `libero_goal_with_mug_t0_r3_pSTUCK_OR_NO_PROGRESS_s58_state_seed31` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t0_r3_pSTUCK_OR_NO_PROGRESS_s58_state_seed31.jpg`
- `libero_goal_with_mug_t6_r4_pSTUCK_OR_NO_PROGRESS_s52_state_seed14` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t6_r4_pSTUCK_OR_NO_PROGRESS_s52_state_seed14.jpg`
- `libero_goal_with_mug_t6_r7_pPLACE_OR_GOAL_s26_state_seed1` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t6_r7_pPLACE_OR_GOAL_s26_state_seed1.jpg`
- `libero_goal_with_mug_t9_r7_pSTUCK_OR_NO_PROGRESS_s53_state_seed11` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t9_r7_pSTUCK_OR_NO_PROGRESS_s53_state_seed11.jpg`
- `libero_goal_with_mug_t9_r7_pTRANSPORT_s143_state_seed17` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_goal_with_mug_t9_r7_pTRANSPORT_s143_state_seed17.jpg`
- `libero_object_with_mug_t3_r5_pSTUCK_OR_NO_PROGRESS_s136_state_seed7` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t3_r5_pSTUCK_OR_NO_PROGRESS_s136_state_seed7.jpg`
- `libero_object_with_mug_t4_r2_pGRASP_OR_LIFT_s104_state_seed6` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t4_r2_pGRASP_OR_LIFT_s104_state_seed6.jpg`
- `libero_object_with_mug_t4_r5_pGRASP_OR_LIFT_s71_state_seed2` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t4_r5_pGRASP_OR_LIFT_s71_state_seed2.jpg`
- `libero_object_with_mug_t5_r2_pNEAR_GRASP_s37_state_seed29` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t5_r2_pNEAR_GRASP_s37_state_seed29.jpg`
- `libero_object_with_mug_t6_r6_pSTUCK_OR_NO_PROGRESS_s54_state_seed22` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t6_r6_pSTUCK_OR_NO_PROGRESS_s54_state_seed22.jpg`
- `libero_object_with_mug_t7_r0_pTRANSPORT_s92_state_seed5` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t7_r0_pTRANSPORT_s92_state_seed5.jpg`
- `libero_object_with_mug_t9_r0_pGRASP_OR_LIFT_s72_state_seed10` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t9_r0_pGRASP_OR_LIFT_s72_state_seed10.jpg`
- `libero_object_with_mug_t9_r1_pGRASP_OR_LIFT_s66_state_seed26` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t9_r1_pGRASP_OR_LIFT_s66_state_seed26.jpg`
- `libero_object_with_mug_t9_r4_pGRASP_OR_LIFT_s71_state_seed19` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t9_r4_pGRASP_OR_LIFT_s71_state_seed19.jpg`
- `libero_object_with_mug_t9_r7_pGRASP_OR_LIFT_s67_state_seed14` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_object_with_mug_t9_r7_pGRASP_OR_LIFT_s67_state_seed14.jpg`
- `libero_spatial_with_mug_t0_r7_pSTUCK_OR_NO_PROGRESS_s120_state_seed12` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_spatial_with_mug_t0_r7_pSTUCK_OR_NO_PROGRESS_s120_state_seed12.jpg`
- `libero_spatial_with_mug_t4_r7_pSTUCK_OR_NO_PROGRESS_s60_state_seed22` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_spatial_with_mug_t4_r7_pSTUCK_OR_NO_PROGRESS_s60_state_seed22.jpg`
- `libero_spatial_with_mug_t6_r5_pTRANSPORT_s102_state_seed4` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_spatial_with_mug_t6_r5_pTRANSPORT_s102_state_seed4.jpg`
- `libero_spatial_with_mug_t7_r4_pTRANSPORT_s136_state_seed13` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_spatial_with_mug_t7_r4_pTRANSPORT_s136_state_seed13.jpg`
- `libero_spatial_with_mug_t7_r4_pTRANSPORT_s136_state_seed14` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_spatial_with_mug_t7_r4_pTRANSPORT_s136_state_seed14.jpg`
- `libero_spatial_with_mug_t7_r4_pTRANSPORT_s136_state_seed27` `bad_no_raw_local_bad` label=`VALIDATED_BAD` behavior=`good` action=`keep` failure=`none` conf=`0.95` sheet=`asynchvla_ws/stage9_libero_pro_risk_data/vlm_audit/stage9_vlm_audit_20260519_blind/sheets/bad_no_raw_local_bad/libero_spatial_with_mug_t7_r4_pTRANSPORT_s136_state_seed27.jpg`

## Decision

Any sample flagged here should be rechecked with simulator metrics and, if possible, replay video. VLM disagreement alone should downgrade to review, not create a final GOOD or BAD label.
