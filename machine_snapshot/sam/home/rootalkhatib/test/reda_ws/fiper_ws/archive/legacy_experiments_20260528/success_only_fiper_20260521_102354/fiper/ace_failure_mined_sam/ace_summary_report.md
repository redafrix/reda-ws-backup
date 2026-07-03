# Action Chunk Entropy (ACE) Summary Report

- **Total Groups Analyzed**: 128
- **Candidate counts per group (Min/Mean/Max)**: 64 / 64.0 / 64
- **ACE Score (Min/Mean/Max)**: -215.7487 / -172.0639 / -88.4886

## ACE Score by Group Risk Type (Stage 9 V2)

| Group Type | Group Count | Mean ACE Score | ACE Range (Min - Max) |
|---|---|---|---|
| action_specific_mixed | 1 | -135.1820 | -135.1820 - -135.1820 |
| all_risky_state_context_candidate | 19 | -142.0818 | -169.0346 - -88.4886 |
| all_safe_or_weak_safe | 108 | -177.6800 | -215.7487 - -115.5589 |

## Top 20 Highest ACE Groups (Most Action-Uncertain)

| State ID | Candidates | ACE Score | Group Type | Risk Range (Min - Max) |
|---|---|---|---|---|
| libero_spatial_with_mug_t1_r2_pseed2_window014_state | 64 | -88.4886 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t0_r4_pseed4_window009_state | 64 | -92.0911 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t0_r6_pseed6_window011_state | 64 | -95.6795 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t2_r1_pseed1_window007_state | 64 | -115.5589 | all_safe_or_weak_safe | 0.22 - 0.27 |
| libero_spatial_with_mug_t0_r6_pseed6_window013_state | 64 | -124.8424 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t0_r3_pseed3_window006_state | 64 | -129.5392 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r0_pseed0_window006_state | 64 | -134.4934 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r6_pseed6_window009_state | 64 | -135.1820 | action_specific_mixed | 0.14 - 0.85 |
| libero_spatial_with_mug_t0_r1_pseed1_window014_state | 64 | -137.2216 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t0_r7_pseed7_window006_state | 64 | -137.3117 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r6_pseed6_window014_state | 64 | -138.0224 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t3_r6_pseed6_window008_state | 64 | -138.3642 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r2_pseed2_window006_state | 64 | -139.7678 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r4_pseed4_window014_state | 64 | -143.4624 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t1_r2_pseed2_window011_state | 64 | -146.0615 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t0_r5_pseed5_window006_state | 64 | -146.3300 | all_safe_or_weak_safe | 0.22 - 0.22 |
| libero_spatial_with_mug_t0_r1_pseed1_window011_state | 64 | -147.5474 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t1_r1_pseed1_window006_state | 64 | -148.5863 | all_safe_or_weak_safe | 0.27 - 0.27 |
| libero_spatial_with_mug_t1_r3_pseed3_window013_state | 64 | -150.0688 | all_risky_state_context_candidate | 0.85 - 0.85 |
| libero_spatial_with_mug_t1_r7_pseed7_window006_state | 64 | -150.7802 | all_safe_or_weak_safe | 0.27 - 0.27 |

## Correlation Analysis Summary

By inspecting the ACE scores across different group types:
- **High ACE** indicates the policy's multi-seed action chunks are highly diverse (entropy/variance is high).
- **Low ACE** suggests the policy is very consistent across random seeds.
We observe that:
  - **action_specific_mixed** (Mean ACE: -135.1820): Indicates bifurcation states where different seeds lead to different outcomes (success or failure).
  - **all_risky_state_context_candidate** (Mean ACE: -142.0818): Represents other risk configurations.
  - **all_safe_or_weak_safe** (Mean ACE: -177.6800): Represents states where the policy confidently outputs successful actions.
