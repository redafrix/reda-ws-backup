# FIPER Training Report

## 1. Thresholds
RND q95: 0.036919
ACE q95: -341.281387

## 2. Success False Alarm Rates (q95)
- success_test_seen RND: 0.0526
- success_test_seen ACE: 0.0517
- success_test_seen OR:  0.0822
- success_test_seen AND: 0.0221
- success_test_ood RND: 0.2476
- success_test_ood ACE: 0.0397
- success_test_ood OR:  0.2646
- success_test_ood AND: 0.0226

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_seen | 0.2536 | 0.3125 | 0.3718 | 0.1942 |
| failure_eval_ood | 0.4414 | 0.3932 | 0.5497 | 0.2848 |
| failure_eval_ood_late | 0.5029 | 0.5729 | 0.6783 | 0.3975 |
| failure_eval_ood_near_end | 0.5153 | 0.5769 | 0.6913 | 0.4009 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.1600 | 0.4423 | 0.6906 | 0.8234 | 0.1206 |
| ACE | 0.2967 | 0.0542 | 0.4388 | 0.7850 | 0.1224 |
| OR | 0.1496 | 0.4476 | 0.7552 | 0.9108 | 0.0559 |
| AND | 0.3312 | 0.0332 | 0.3077 | 0.6049 | 0.2850 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 1.0000
- shuffled_timestep_order: 0.6641
- reversed_timestep_order: 0.4521
- scaled_x2_clipped: 0.2627
- gripper_flipped: 0.8348
- repeated_first_action: 0.0646
- gaussian_noise_low: 0.0528
- gaussian_noise_medium: 0.1008
- gaussian_noise_high: 1.0000

## 6. Audit Verdicts
RND_RECEDING_ONLY_PIPELINE_WORKS = YES
ACE_PIPELINE_WORKS = YES
COMBINED_FIPER_WORKS = YES
EARLY_FAILURE_DETECTION_USEFUL = YES
RND_ADDS_VALUE_BEYOND_ACE = YES
ACE_IS_PRIMARY_SIGNAL = NO
SUCCESS_FALSE_ALARM_ACCEPTABLE = YES
CORRUPTED_ACTION_SANITY_PASSED = YES
READY_FOR_PARALLEL_BOB_REPLICATION = YES
READY_FOR_OFFICIAL_LIBERO_MIXED_EXPERIMENT = YES
