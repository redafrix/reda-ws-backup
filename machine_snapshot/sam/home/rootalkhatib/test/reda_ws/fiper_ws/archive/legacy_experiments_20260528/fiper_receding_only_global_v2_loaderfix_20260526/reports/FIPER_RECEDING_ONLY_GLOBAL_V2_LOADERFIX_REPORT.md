# FIPER Training Report

## 1. Thresholds
RND q95: 0.035757
ACE q95: -341.129443

## 2. Success False Alarm Rates (q95)
- success_test_id RND: 0.0400
- success_test_id ACE: 0.0385
- success_test_id OR:  0.0635
- success_test_id AND: 0.0150

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_all | 0.2319 | 0.3097 | 0.3551 | 0.1865 |
| failure_eval_early | 0.1005 | 0.0569 | 0.1214 | 0.0359 |
| failure_eval_mid | 0.2509 | 0.3506 | 0.3912 | 0.2103 |
| failure_eval_late | 0.3253 | 0.4805 | 0.5164 | 0.2894 |
| failure_eval_near_end | 0.3301 | 0.4839 | 0.5212 | 0.2928 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.1783 | 0.3811 | 0.6503 | 0.7937 | 0.1416 |
| ACE | 0.3038 | 0.0402 | 0.4196 | 0.7692 | 0.1346 |
| OR | 0.1708 | 0.3881 | 0.7133 | 0.8916 | 0.0647 |
| AND | 0.3388 | 0.0210 | 0.2850 | 0.5927 | 0.3007 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 1.0000
- shuffled_timestep_order: 0.6366
- reversed_timestep_order: 0.4092
- scaled_x2_clipped: 0.1824
- gripper_flipped: 0.8353
- repeated_first_action: 0.0575
- gaussian_noise_low: 0.0403
- gaussian_noise_medium: 0.0772
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
