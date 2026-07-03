# ACE Success vs Failure Comparison Report

This report analyzes the Action Chunk Entropy (ACE) and diversity metrics calculated from the 64 unexecuted candidate action chunks.

## ACE Conformal Thresholds
- Calibrated on successful training and calibration episodes:
  - **q90**: -161.1047
  - **q95**: -155.7420
  - **q99**: -137.9771

## Overall Comparison: Success vs Failure
| Metric | Success Mean (Std) | Failure Mean (Std) | Late Failure Mean (Std) |
|---|---|---|---|
| **ACE (Gaussian Entropy)** | -193.4394 (22.3192) | -139.4645 (34.2802) | -128.5291 (32.5499) |
| **Mean Pairwise Distance** | 1.2942 (0.4195) | 2.5459 (1.0911) | 2.9658 (1.1396) |
| **Action Std Mean** | 0.0940 (0.0303) | 0.1838 (0.0813) | 0.2152 (0.0852) |
| **Gripper Std** | 0.0059 (0.0035) | 0.0950 (0.1496) | 0.1171 (0.1703) |
| **Translation Std** | 0.0862 (0.0429) | 0.1893 (0.0878) | 0.2258 (0.0956) |
| **Rotation Std** | 0.1312 (0.0345) | 0.2079 (0.0819) | 0.2373 (0.0887) |
| **Near-Duplicate Pairs** | 0.0 (0.0) | 0.0 (0.0) | 0.0 (0.0) |
| **Effective Diversity** | 64.00 (0.00) | 64.00 (0.00) | 64.00 (0.00) |

## Temporal Analysis: ACE Over Episode Progress
| Episode Progress | Mean ACE Score | Mean Pairwise Distance | Mean Effective Diversity | Count |
|---|---|---|---|---|
| 0.0-0.25 | -171.2931 | 1.6785 | 64.00 | 7096 |
| 0.25-0.5 | -155.2378 | 2.1034 | 64.00 | 4145 |
| 0.5-0.75 | -144.6150 | 2.4437 | 64.00 | 3958 |
| 0.75-1.0 | -138.3441 | 2.7381 | 64.00 | 7267 |

## Key Questions Answered
- **Are the 64 chunks actually different?**
  - Yes. The mean pairwise distance across success rows is 1.2942, with an average of 64.00 unique trajectory clusters out of 64.
- **Is ACE higher in failure episodes?**
  - Let's compare: Success Mean ACE is -193.4394 vs Failure Mean ACE of -139.4645.
- **Does ACE increase near failure/timeout?**
  - Early failure ACE is -161.7085 vs Late failure ACE of -128.5291.
- **Is SimVLA stochastic or mostly deterministic from the same state?**
  - The policy shows significant stochasticity from the same state when different seeds are used, as indicated by the high mean pairwise distance and entropy values.
- **Does ACE alone separate success/failure?**
  - We will analyze this by looking at overlap in the distributions and evaluating classification metrics in the diagnostic supervised section.