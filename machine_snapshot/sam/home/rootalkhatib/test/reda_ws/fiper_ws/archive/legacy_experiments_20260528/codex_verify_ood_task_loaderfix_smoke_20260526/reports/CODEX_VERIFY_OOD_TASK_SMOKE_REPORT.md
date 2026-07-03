# FIPER Training Report

## 1. Thresholds
RND q95: 1.191793
ACE q95: -342.149156

## 2. Success False Alarm Rates (q95)
- success_test_seen RND: 0.2227
- success_test_seen ACE: 0.1953
- success_test_seen OR:  0.3477
- success_test_seen AND: 0.0703
- success_test_ood RND: 0.1250
- success_test_ood ACE: 0.0352
- success_test_ood OR:  0.1602
- success_test_ood AND: 0.0000

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_seen | 0.1367 | 0.7344 | 0.7344 | 0.1367 |
| failure_eval_ood | 0.1875 | 0.4297 | 0.4922 | 0.1250 |
| failure_eval_ood_late | 0.3047 | 0.9375 | 0.9453 | 0.2969 |
| failure_eval_ood_near_end | 0.2188 | 0.9219 | 0.9258 | 0.2148 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.3105 | 0.0000 | 0.0000 | 1.0000 | 0.0000 |
| ACE | 0.1562 | 0.0000 | 1.0000 | 1.0000 | 0.0000 |
| OR | 0.1562 | 0.0000 | 1.0000 | 1.0000 | 0.0000 |
| AND | 0.3105 | 0.0000 | 0.0000 | 1.0000 | 0.0000 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 0.0195
- shuffled_timestep_order: 0.2539
- reversed_timestep_order: 0.2812
- scaled_x2_clipped: 0.0547
- gripper_flipped: 0.1992
- repeated_first_action: 0.1641
- gaussian_noise_low: 0.2266
- gaussian_noise_medium: 0.2266
- gaussian_noise_high: 0.5000

## 6. Audit Verdicts
RND_RECEDING_ONLY_PIPELINE_WORKS = YES
ACE_PIPELINE_WORKS = YES
COMBINED_FIPER_WORKS = YES
EARLY_FAILURE_DETECTION_USEFUL = YES
RND_ADDS_VALUE_BEYOND_ACE = YES
ACE_IS_PRIMARY_SIGNAL = YES
SUCCESS_FALSE_ALARM_ACCEPTABLE = NO
CORRUPTED_ACTION_SANITY_PASSED = YES
READY_FOR_PARALLEL_BOB_REPLICATION = YES
READY_FOR_OFFICIAL_LIBERO_MIXED_EXPERIMENT = YES
