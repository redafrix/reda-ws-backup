# Action Chunk Entropy (ACE) Summary Report

- **Total Groups Analyzed**: 20
- **Candidate counts per group (Min/Mean/Max)**: 64 / 64.0 / 64
- **ACE Score (Min/Mean/Max)**: -180.7153 / -151.6331 / -121.7779

## ACE Score by Group Risk Type (Stage 9 V2)

| Group Type | Group Count | Mean ACE Score | ACE Range (Min - Max) |
|---|---|---|---|
| all_safe_or_weak_safe | 20 | -151.6331 | -180.7153 - -121.7779 |

## Top 20 Highest ACE Groups (Most Action-Uncertain)

| State ID | Candidates | ACE Score | Group Type | Risk Range (Min - Max) |
|---|---|---|---|---|
| libero_spatial_with_mug_t0_r13_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -121.7779 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r13_pSTUCK_OR_NO_PROGRESS_s119_state | 64 | -122.0901 | all_safe_or_weak_safe | 0.16 - 0.25 |
| libero_spatial_with_mug_t0_r13_pPLACE_OR_GOAL_s96_state | 64 | -129.5432 | all_safe_or_weak_safe | 0.06 - 0.30 |
| libero_spatial_with_mug_t0_r11_pSTUCK_OR_NO_PROGRESS_s119_state | 64 | -132.3340 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r11_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -134.5508 | all_safe_or_weak_safe | 0.24 - 0.25 |
| libero_spatial_with_mug_t0_r10_pPLACE_OR_GOAL_s74_state | 64 | -136.8420 | all_safe_or_weak_safe | 0.03 - 0.06 |
| libero_spatial_with_mug_t0_r0_pPLACE_OR_GOAL_s70_state | 64 | -137.3987 | all_safe_or_weak_safe | 0.00 - 0.07 |
| libero_spatial_with_mug_t0_r11_pPLACE_OR_GOAL_s80_state | 64 | -140.1682 | all_safe_or_weak_safe | 0.00 - 0.00 |
| libero_spatial_with_mug_t0_r11_pSTUCK_OR_NO_PROGRESS_s96_state | 64 | -142.5178 | all_safe_or_weak_safe | 0.00 - 0.31 |
| libero_spatial_with_mug_t0_r13_pTRANSPORT_s80_state | 64 | -144.4240 | all_safe_or_weak_safe | 0.00 - 0.00 |
| libero_spatial_with_mug_t0_r12_pPLACE_OR_GOAL_s76_state | 64 | -155.9324 | all_safe_or_weak_safe | 0.06 - 0.06 |
| libero_spatial_with_mug_t0_r0_pPLACE_OR_GOAL_s74_state | 64 | -157.8073 | all_safe_or_weak_safe | 0.03 - 0.06 |
| libero_spatial_with_mug_t0_r12_pPLACE_OR_GOAL_s32_state | 64 | -160.9054 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r10_pPLACE_OR_GOAL_s33_state | 64 | -162.2677 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r0_pTRANSPORT_s26_state | 64 | -168.8634 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r12_pSTUCK_OR_NO_PROGRESS_s57_state | 64 | -174.0613 | all_safe_or_weak_safe | 0.24 - 0.25 |
| libero_spatial_with_mug_t0_r10_pSTUCK_OR_NO_PROGRESS_s56_state | 64 | -175.6522 | all_safe_or_weak_safe | 0.03 - 0.28 |
| libero_spatial_with_mug_t0_r0_pSTUCK_OR_NO_PROGRESS_s54_state | 64 | -176.5904 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r10_pTRANSPORT_s49_state | 64 | -178.2203 | all_safe_or_weak_safe | 0.00 - 0.03 |
| libero_spatial_with_mug_t0_r12_pTRANSPORT_s51_state | 64 | -180.7153 | all_safe_or_weak_safe | 0.07 - 0.24 |

## Correlation Analysis Summary

By inspecting the ACE scores across different group types:
- **High ACE** indicates the policy's multi-seed action chunks are highly diverse (entropy/variance is high).
- **Low ACE** suggests the policy is very consistent across random seeds.
We observe that:
  - **all_safe_or_weak_safe** (Mean ACE: -151.6331): Represents states where the policy confidently outputs successful actions.
