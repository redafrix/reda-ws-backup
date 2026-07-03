---
title: Next Steps
created: 2026-06-02
tags:
  - fiper/next
---

# Next Steps

## Main Technical Problem

The current risk-aware policy helps, but it creates too many regressions. The best next work should target intervention quality rather than just offline detector score.

## Recommended Next Experiments

1. **Intervention lockout:** prevent repeated interventions after a stable low-risk period.
2. **Dynamic margin:** require larger risk improvement when main risk is not extreme.
3. **Candidate diversity filter:** only switch action if candidate risk improves and action does not deviate too violently.
4. **Fast scoring optimization:** reduce the 8.68x runtime overhead by batching all candidate chunks in one model forward pass.
5. **Uncertainty feature selection:** use Dean uncertainty features with top-K or late-fusion, not raw 98D by default.
6. **Regression review videos:** inspect paired regressions to see whether the risk-aware action causes timeout, wrong object, or motion inefficiency.

## Decision Summary

Keep `v2_018_transformer_k16` as the main selected baseline. The real-time same-seed result is positive enough to justify continued work, but not strong enough to claim the monitor is deployment-ready.
