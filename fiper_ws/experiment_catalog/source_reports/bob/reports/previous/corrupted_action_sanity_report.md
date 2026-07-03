# Corrupted-Action Sanity Test Report

This report evaluates the sensitivity of the trained RND safety monitor to various types of action chunk corruptions.
We apply corruptions to the `success_test` action chunks and measure the alarm rate against the conformal `q95` threshold.

## Alarm Rates on Corrupted Actions
| Corruption Type | Mean RND Score | Alarm Rate @ q95 (%) | Sensitivity Status |
|---|---|---|---|
| `clean` | 0.000172 | 6.86% | Nominal (False Alarm) |
| `zero` | 0.033398 | 100.00% | SENSITIVE (Success) |
| `random` | 0.033850 | 100.00% | SENSITIVE (Success) |
| `shuffled` | 0.000616 | 66.96% | SENSITIVE (Success) |
| `reversed` | 0.000499 | 53.71% | SENSITIVE (Success) |
| `scaled` | 0.027345 | 100.00% | SENSITIVE (Success) |
| `gripper_flipped` | 0.035599 | 100.00% | SENSITIVE (Success) |
| `repeated_first` | 0.000221 | 18.14% | WEAK (Low sensitivity) |
| `noise_low` | 0.014814 | 100.00% | SENSITIVE (Success) |
| `noise_medium` | 0.031442 | 100.00% | SENSITIVE (Success) |
| `noise_high` | 0.037677 | 100.00% | SENSITIVE (Success) |

## Analysis of Results
- **Clean Success Chunks**: Alarms at approximately the false alarm rate target (~5%).
- **Severe Corruptions (Zero/Random)**: These represent completely out-of-distribution behaviors and should trigger near 100% alarms.
- **Structural Corruptions (Shuffled/Reversed/Repeated)**: These evaluate whether the model is sensitive to temporal ordering and structure, which is crucial for action-heavy risk detectors.
- **Noise Sensitivity**: Low noise should trigger fewer alarms, while high noise should trigger significant alarms, showing graceful scaling.