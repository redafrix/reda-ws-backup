# Four-Task Same-Seed Deployment Results

This summary records the paired comparison audited on 2026-06-02.

## Compared Policies

- Baseline: vanilla SimVLA, first-action-only receding horizon.
- Risk-aware: SimVLA plus `v2_018_transformer_k16` risk detector using `risk_filtered_lowest_score_candidate_v2_strict_margin`.

Both policies were compared by `reset_seed` in the same episode order for every worker.

## Per-Task Results

| Host | Worker / task | Episodes | Baseline success | Risk-aware success | Delta | Recoveries | Regressions |
|---|---|---:|---:|---:|---:|---:|---:|
| Sam | `sam_w0_seen_task7` (`libero_10_with_milk/task7`) | 450 | 244 / 450 = 54.2% | 281 / 450 = 62.4% | +8.2 pts | 80 | 43 |
| Sam | `sam_w1_ood_task8` (`libero_10_with_milk/task8`) | 429 | 210 / 429 = 49.0% | 213 / 429 = 49.7% | +0.7 pts | 81 | 78 |
| Bob | `bob_w0_fold00_seen_butter_t2` (`libero_object_with_mug/task2`) | 450 | 172 / 450 = 38.2% | 184 / 450 = 40.9% | +2.7 pts | 31 | 19 |
| Bob | `bob_w1_fold00_unseen_alphabet_soup_t0` (`libero_object_with_mug/task0`) | 552 | 395 / 552 = 71.6% | 399 / 552 = 72.3% | +0.7 pts | 14 | 10 |

## Global Result

| Metric | Baseline | Risk-aware |
|---|---:|---:|
| Paired episodes | 1881 | 1881 |
| Successes | 1021 | 1077 |
| Success rate | 54.3% | 57.3% |
| Net delta | | +3.0 pts |

## Verification Checks

- Same reset seed order: yes for all four workers.
- Paired seeds: 1881 / 1881.
- Risk-aware errors: 0.
- Baseline errors: 0.
- Risk-aware seed collisions: 0.
- Risk-aware main-vs-ACE seed collisions: 0.
- No active Bob/Sam rollout processes remained at audit time.

## Action Modification Statistics

| Worker | Total modifications | Mean / episode | Median / episode | Max / episode |
|---|---:|---:|---:|---:|
| `sam_w0_seen_task7` | 7779 | 17.29 | 15 | 89 |
| `sam_w1_ood_task8` | 384 | 0.90 | 0 | 7 |
| `bob_w0_fold00_seen_butter_t2` | 4403 | 9.78 | 5 | 91 |
| `bob_w1_fold00_unseen_alphabet_soup_t0` | 5159 | 9.35 | 2 | 77 |

## Same-Seed Caveat

The comparison is exact for environment reset seeds and episode pairing.

The baseline also reuses the risk-aware main action sampling seeds when the risk-aware seed trace has rows for the corresponding timestep. If a baseline episode continues longer than the risk-aware episode, fallback main action seeds are generated for the remaining timesteps.

Fallback totals observed:

| Worker | Episodes with fallback | Total fallback timesteps | Max fallback in one episode |
|---|---:|---:|---:|
| `sam_w0_seen_task7` | 213 | 6805 | 96 |
| `sam_w1_ood_task8` | 151 | 4136 | 75 |
| `bob_w0_fold00_seen_butter_t2` | 87 | 3270 | 128 |
| `bob_w1_fold00_unseen_alphabet_soup_t0` | 80 | 1891 | 147 |

This does not invalidate the reset-seed paired comparison, but it means the baseline is not guaranteed to replay the exact same action-sampling seed for every timestep after the matching risk-aware trace ends.

## Interpretation

The risk-aware policy improves global success rate by 3.0 percentage points. The strongest result is on `libero_10_with_milk/task7`, where it adds 8.2 points. The other three tasks show smaller gains. The policy recovers many failures but also creates regressions, especially on task8.
