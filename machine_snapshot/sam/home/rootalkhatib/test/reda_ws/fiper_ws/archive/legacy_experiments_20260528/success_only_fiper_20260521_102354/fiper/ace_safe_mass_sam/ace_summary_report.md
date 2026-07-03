# Action Chunk Entropy (ACE) Summary Report

- **Total Groups Analyzed**: 80
- **Candidate counts per group (Min/Mean/Max)**: 64 / 64.0 / 64
- **ACE Score (Min/Mean/Max)**: -181.7815 / -133.9203 / -62.2254

## ACE Score by Group Risk Type (Stage 9 V2)

| Group Type | Group Count | Mean ACE Score | ACE Range (Min - Max) |
|---|---|---|---|
| all_safe_or_weak_safe | 80 | -133.9203 | -181.7815 - -62.2254 |

## Top 20 Highest ACE Groups (Most Action-Uncertain)

| State ID | Candidates | ACE Score | Group Type | Risk Range (Min - Max) |
|---|---|---|---|---|
| libero_spatial_with_mug_t0_r5_pSTUCK_OR_NO_PROGRESS_s119_state | 64 | -62.2254 | all_safe_or_weak_safe | 0.16 - 0.25 |
| libero_spatial_with_mug_t0_r5_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -76.9483 | all_safe_or_weak_safe | 0.24 - 0.25 |
| libero_spatial_with_mug_t0_r6_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -77.8126 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r16_pTRANSPORT_s108_state | 64 | -80.6533 | all_safe_or_weak_safe | 0.27 - 0.27 |
| libero_spatial_with_mug_t0_r18_pSTUCK_OR_NO_PROGRESS_s119_state | 64 | -82.2583 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r14_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -88.9623 | all_safe_or_weak_safe | 0.24 - 0.25 |
| libero_spatial_with_mug_t0_r16_pTRANSPORT_s119_state | 64 | -89.4367 | all_safe_or_weak_safe | 0.27 - 0.27 |
| libero_spatial_with_mug_t0_r5_pPLACE_OR_GOAL_s96_state | 64 | -95.5567 | all_safe_or_weak_safe | 0.00 - 0.33 |
| libero_spatial_with_mug_t0_r18_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -97.8991 | all_safe_or_weak_safe | 0.07 - 0.27 |
| libero_spatial_with_mug_t0_r6_pSTUCK_OR_NO_PROGRESS_s80_state | 64 | -104.8788 | all_safe_or_weak_safe | 0.00 - 0.08 |
| libero_spatial_with_mug_t0_r17_pTRANSPORT_s80_state | 64 | -105.7569 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r17_pSTUCK_OR_NO_PROGRESS_s96_state | 64 | -106.2360 | all_safe_or_weak_safe | 0.23 - 0.25 |
| libero_spatial_with_mug_t0_r17_pSTUCK_OR_NO_PROGRESS_s119_state | 64 | -107.2360 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r18_pSTUCK_OR_NO_PROGRESS_s96_state | 64 | -107.8479 | all_safe_or_weak_safe | 0.00 - 0.31 |
| libero_spatial_with_mug_t0_r14_pSTUCK_OR_NO_PROGRESS_s119_state | 64 | -109.1923 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r16_pSTUCK_OR_NO_PROGRESS_s96_state | 64 | -111.3803 | all_safe_or_weak_safe | 0.23 - 0.25 |
| libero_spatial_with_mug_t0_r7_pSTUCK_OR_NO_PROGRESS_s96_state | 64 | -111.6898 | all_safe_or_weak_safe | 0.00 - 0.31 |
| libero_spatial_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s96_state | 64 | -112.2313 | all_safe_or_weak_safe | 0.22 - 0.25 |
| libero_spatial_with_mug_t0_r17_pSTUCK_OR_NO_PROGRESS_s108_state | 64 | -112.4700 | all_safe_or_weak_safe | 0.25 - 0.25 |
| libero_spatial_with_mug_t0_r4_pTRANSPORT_s119_state | 64 | -112.8355 | all_safe_or_weak_safe | 0.26 - 0.26 |

## Correlation Analysis Summary

By inspecting the ACE scores across different group types:
- **High ACE** indicates the policy's multi-seed action chunks are highly diverse (entropy/variance is high).
- **Low ACE** suggests the policy is very consistent across random seeds.
We observe that:
  - **all_safe_or_weak_safe** (Mean ACE: -133.9203): Represents states where the policy confidently outputs successful actions.
