# FIPER Training Report

## 1. Thresholds
RND q95: 0.036420
ACE q95: -341.129398

## 2. Success False Alarm Rates (q95)
- RND: 0.0400
- ACE: 0.0385
- OR:  0.0640
- AND: 0.0144

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_all | 0.2306 | 0.3097 | 0.3562 | 0.1840 |
| failure_eval_early | 0.1091 | 0.0596 | 0.1315 | 0.0371 |
| failure_eval_mid | 0.2486 | 0.3522 | 0.3928 | 0.2080 |
| failure_eval_late | 0.3160 | 0.4746 | 0.5075 | 0.2831 |
| failure_eval_near_end | 0.3200 | 0.4741 | 0.5084 | 0.2857 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.1870 | 0.3706 | 0.6381 | 0.7885 | 0.1399 |
| ACE | 0.3005 | 0.0437 | 0.4231 | 0.7692 | 0.1346 |
| OR | 0.1704 | 0.3776 | 0.7098 | 0.8881 | 0.0717 |
| AND | 0.3430 | 0.0192 | 0.2780 | 0.5769 | 0.3094 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 1.0000
- shuffled_timestep_order: 0.6338
- reversed_timestep_order: 0.4023
- scaled_x2_clipped: 0.1824
- gripper_flipped: 0.8072
- repeated_first_action: 0.0556
- gaussian_noise_low: 0.0402
- gaussian_noise_medium: 0.0760
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
