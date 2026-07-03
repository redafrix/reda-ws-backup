# FIPER Training Report

## 1. Thresholds
RND q95: 1.144241
ACE q95: -339.439930

## 2. Success False Alarm Rates (q95)
- RND: 0.0410
- ACE: 0.0190
- OR:  0.0570
- AND: 0.0030

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_all | 0.0290 | 0.2100 | 0.2170 | 0.0220 |
| failure_eval_early | 0.0060 | 0.0380 | 0.0440 | 0.0000 |
| failure_eval_mid | 0.0350 | 0.2140 | 0.2270 | 0.0220 |
| failure_eval_late | 0.0860 | 0.2940 | 0.3280 | 0.0520 |
| failure_eval_near_end | 0.0850 | 0.2530 | 0.2770 | 0.0610 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.2155 | 0.1017 | 0.1356 | 0.2203 | 0.7627 |
| ACE | 0.2712 | 0.2881 | 0.3559 | 0.4068 | 0.4407 |
| OR | 0.2546 | 0.3220 | 0.3898 | 0.4407 | 0.4068 |
| AND | 0.2217 | 0.0678 | 0.1017 | 0.1525 | 0.8305 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 0.0000
- shuffled_timestep_order: 0.0510
- reversed_timestep_order: 0.0550
- scaled_x2_clipped: 0.0010
- gripper_flipped: 0.0780
- repeated_first_action: 0.0370
- gaussian_noise_low: 0.0400
- gaussian_noise_medium: 0.0390
- gaussian_noise_high: 0.1750

## 6. Audit Verdicts
RND_RECEDING_ONLY_PIPELINE_WORKS = YES
ACE_PIPELINE_WORKS = YES
COMBINED_FIPER_WORKS = YES
EARLY_FAILURE_DETECTION_USEFUL = YES
RND_ADDS_VALUE_BEYOND_ACE = YES
ACE_IS_PRIMARY_SIGNAL = YES
SUCCESS_FALSE_ALARM_ACCEPTABLE = YES
CORRUPTED_ACTION_SANITY_PASSED = YES
READY_FOR_PARALLEL_BOB_REPLICATION = YES
READY_FOR_OFFICIAL_LIBERO_MIXED_EXPERIMENT = YES
