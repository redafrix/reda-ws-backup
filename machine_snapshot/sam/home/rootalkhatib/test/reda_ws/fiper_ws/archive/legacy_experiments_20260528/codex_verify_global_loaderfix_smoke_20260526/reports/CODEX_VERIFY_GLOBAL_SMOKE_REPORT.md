# FIPER Training Report

## 1. Thresholds
RND q95: 2.105479
ACE q95: -341.798546

## 2. Success False Alarm Rates (q95)
- success_test_id RND: 0.0352
- success_test_id ACE: 0.1602
- success_test_id OR:  0.1953
- success_test_id AND: 0.0000

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_all | 0.0000 | 0.7070 | 0.7070 | 0.0000 |
| failure_eval_early | 0.0273 | 0.1172 | 0.1445 | 0.0000 |
| failure_eval_mid | 0.0000 | 0.7969 | 0.7969 | 0.0000 |
| failure_eval_late | 0.0000 | 0.5312 | 0.5312 | 0.0000 |
| failure_eval_near_end | 0.0156 | 0.4727 | 0.4727 | 0.0156 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| ACE | 0.1562 | 0.0000 | 1.0000 | 1.0000 | 0.0000 |
| OR | 0.1562 | 0.0000 | 1.0000 | 1.0000 | 0.0000 |
| AND | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 0.0000
- shuffled_timestep_order: 0.0352
- reversed_timestep_order: 0.0703
- scaled_x2_clipped: 0.0000
- gripper_flipped: 0.0547
- repeated_first_action: 0.0312
- gaussian_noise_low: 0.0352
- gaussian_noise_medium: 0.0391
- gaussian_noise_high: 0.1523

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
