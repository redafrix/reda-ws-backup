# ACE + RND Combined FIPER Quadrant Analysis Report

This report combines Random Network Distillation (RND) novelty detection and Action Chunk Entropy (ACE) policy uncertainty to analyze robot decisions.

## Quadrant Definitions (at conformal `q95` thresholds)
- **normal_confident** (RND low, ACE low): In-distribution state, policy is confident.
- **ood_confident** (RND high, ACE low): Out-of-distribution state, but policy is highly consistent.
- **action_uncertain** (RND low, ACE high): In-distribution state, but policy is bifurcated/uncertain.
- **fiper_alarm** (RND high, ACE high): Out-of-distribution state and policy is uncertain (highest risk).

## Quadrant Distribution across Splits
| Split | Count | Normal Confident (%) | OOD Confident (%) | Action Uncertain (%) | FIPER Alarm (%) |
|---|---|---|---|---|---|
| `success_test` | 1268 | 91.48% | 5.84% | 1.66% | 1.03% |
| `ood_suite_success_test` | 755 | 0.00% | 34.30% | 0.00% | 65.70% |
| `failure_eval_all` | 3400 | 27.94% | 7.35% | 5.68% | 59.03% |
| `failure_eval_early` | 1700 | 32.59% | 25.35% | 0.88% | 41.18% |
| `failure_eval_late` | 850 | 26.94% | 4.24% | 6.00% | 62.82% |
| `failure_eval_near_end` | 850 | 26.71% | 6.12% | 7.06% | 60.12% |

## FIPER Alarm Complementarity Analysis (Failure Episodes)
Out of 3400 failure timesteps:
- **Both alarms trigger (FIPER Alarm)**: 2007 timesteps (59.03%)
- **Only RND triggers (OOD Confident)**: 250 timesteps (7.35%)
- **Only ACE triggers (Action Uncertain)**: 193 timesteps (5.68%)
- **Neither triggers (Missed failures)**: 950 timesteps (27.94%)

## Key Questions Answered
- **Does ACE add information beyond RND?**
  - Yes. In failure episodes, ACE flags 193 timesteps (5.68%) that RND misses (Action Uncertain quadrant).
- **Are failures mostly RND-high/ACE-low, ACE-high/RND-low, or both?**
  - In this dataset, failures are mostly both RND-high and ACE-high (59.03%), or RND-high/ACE-low (7.35%).
- **Does ACE help catch cases RND misses?**
  - Yes, it catches the 5.68% of failure steps where RND is below threshold.
- **Does RND catch cases ACE misses?**
  - Yes, RND catches 7.35% of failure steps where the policy is consistent (low ACE) but the state/action is anomalous.