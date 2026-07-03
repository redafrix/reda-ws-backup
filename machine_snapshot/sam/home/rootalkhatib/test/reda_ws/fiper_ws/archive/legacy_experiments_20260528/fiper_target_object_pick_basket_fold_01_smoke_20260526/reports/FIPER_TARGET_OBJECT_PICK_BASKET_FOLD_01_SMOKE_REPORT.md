# FIPER Training Report

## 1. Thresholds
RND q95: 0.491808
ACE q95: -342.285971

## 2. Success False Alarm Rates (q95)
- success_test_seen RND: 0.0840
- success_test_seen ACE: 0.1007
- success_test_seen OR:  0.1740
- success_test_seen AND: 0.0107
- success_test_ood RND: 0.1067
- success_test_ood ACE: 0.0627
- success_test_ood OR:  0.1600
- success_test_ood AND: 0.0093

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_seen | 0.1007 | 0.1873 | 0.2267 | 0.0613 |
| failure_eval_ood | 0.1520 | 0.3727 | 0.4613 | 0.0633 |
| failure_eval_ood_late | 0.0673 | 0.6847 | 0.7013 | 0.0507 |
| failure_eval_ood_near_end | 0.0507 | 0.7200 | 0.7360 | 0.0347 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.1630 | 0.5000 | 0.6000 | 0.8000 | 0.1000 |
| ACE | 0.1940 | 0.0000 | 0.8000 | 1.0000 | 0.0000 |
| OR | 0.1050 | 0.5000 | 0.9000 | 1.0000 | 0.0000 |
| AND | 0.3758 | 0.0000 | 0.3000 | 0.6000 | 0.2000 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 0.9920
- shuffled_timestep_order: 0.1987
- reversed_timestep_order: 0.1900
- scaled_x2_clipped: 0.3473
- gripper_flipped: 0.3180
- repeated_first_action: 0.0873
- gaussian_noise_low: 0.0860
- gaussian_noise_medium: 0.1033
- gaussian_noise_high: 0.9973

## 6. Audit Verdicts
EARLY_FAILURE_DETECTION_USEFUL = YES
RND_ADDS_VALUE_BEYOND_ACE = NO
ACE_ADDS_VALUE_BEYOND_RND = YES
ACE_IS_PRIMARY_EARLY_SIGNAL = YES
SUCCESS_ROW_FALSE_ALARM_UNDER_15PCT = NO
CORRUPTED_ACTION_SANITY_REVIEW_REQUIRED = YES
READY_FOR_NEXT_EXPERIMENT_REVIEW_REQUIRED = YES
