# FIPER Training Report

## 1. Thresholds
RND q95: 0.033358
ACE q95: -342.326879

## 2. Success False Alarm Rates (q95)
- success_test_seen RND: 0.0621
- success_test_seen ACE: 0.0580
- success_test_seen OR:  0.0995
- success_test_seen AND: 0.0206
- success_test_ood RND: 0.2781
- success_test_ood ACE: 0.1150
- success_test_ood OR:  0.3405
- success_test_ood AND: 0.0525

## 3. Failure Detection Summary (q95)
| Split | RND | ACE | OR | AND |
|---|---|---|---|---|
| failure_eval_seen | 0.2803 | 0.2906 | 0.3895 | 0.1814 |
| failure_eval_ood | 0.4754 | 0.4082 | 0.5785 | 0.3051 |
| failure_eval_ood_late | 0.6133 | 0.7288 | 0.8046 | 0.5375 |
| failure_eval_ood_near_end | 0.6291 | 0.7440 | 0.8200 | 0.5531 |

## 4. Early Detection Performance (q95)
| Signal | Mean Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|
| RND | 0.1437 | 0.3840 | 0.8480 | 0.9600 | 0.0240 |
| ACE | 0.2156 | 0.0000 | 0.7920 | 0.9920 | 0.0000 |
| OR | 0.1202 | 0.3840 | 0.9440 | 1.0000 | 0.0000 |
| AND | 0.2752 | 0.0000 | 0.4880 | 0.8080 | 0.1520 |

## 5. Corrupted-Action Sanity (RND q95)
- zero: 0.0000
- random_uniform: 1.0000
- shuffled_timestep_order: 0.7850
- reversed_timestep_order: 0.6416
- scaled_x2_clipped: 0.7511
- gripper_flipped: 0.9918
- repeated_first_action: 0.1760
- gaussian_noise_low: 0.0636
- gaussian_noise_medium: 0.3853
- gaussian_noise_high: 1.0000

## 6. Audit Verdicts
EARLY_FAILURE_DETECTION_USEFUL = YES
RND_ADDS_VALUE_BEYOND_ACE = NO
ACE_ADDS_VALUE_BEYOND_RND = YES
ACE_IS_PRIMARY_EARLY_SIGNAL = NO
SUCCESS_ROW_FALSE_ALARM_UNDER_15PCT = YES
CORRUPTED_ACTION_SANITY_REVIEW_REQUIRED = YES
READY_FOR_NEXT_EXPERIMENT_REVIEW_REQUIRED = YES
