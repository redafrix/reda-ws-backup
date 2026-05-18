# Stage 7 — Rollout Analysis (Object T0, 10 episodes)

- Timestamp: 2026-05-15 (Gemini)
- Task: *"pick up the alphabet soup and place it in the basket"*

## Success Metrics

| Metric | A_passive (Baseline) | B_deliberation (Rater) |
|---|---:|---:|
| Success Rate | **100%** | **100%** |
| Avg Steps (Success) | **162.2** | 233.5 |
| Avg Total Reward | 1.0 | 1.0 |

## Uncertainty & Seed Selection

| Metric | A_passive | B_deliberation |
|---|---:|---:|
| Mean Uncertainty | 1.31 | **1.15** |
| Min Uncertainty | 0.57 | **0.14** |
| Max Uncertainty | 1.93 | 2.35 |
| Seed 0 Avg Uncertainty | 1.29 | **1.10** |

### B_deliberation Seed Distribution
- **Seed 0:** 208 (44%)
- **Seed 1:** 44 (9%)
- **Seed 2:** 63 (13%)
- **Seed 3:** 105 (22%)
- **Seed 4:** 53 (11%)

## Key Observations

1. **Both modes achieved 100% success rate.** For this relatively simple task, SimVLA is highly robust once norm stats are loaded.
2. **B_deliberation is slower but lower uncertainty.** The rater-enabled mode took ~70 more steps on average than the baseline. This suggests the rater might be selecting seeds that are "safer" or more conservative, leading to more deliberate but slower progress.
3. **The Rater is active.** In B_deliberation, the model chose a non-zero seed 56% of the time. Seed 3 was particularly popular after Seed 0.
4. **Lower Mean Uncertainty.** B_deliberation successfully reduced the mean uncertainty from 1.31 to 1.15, and hit a much lower minimum uncertainty (0.14 vs 0.57).

## Conclusion

The deliberation mode successfully reduces predicted error (uncertainty) during the rollout, although for this specific task, it resulted in longer episode lengths. The 100% success rate across 20 episodes confirms the environment and model integration is stable.
