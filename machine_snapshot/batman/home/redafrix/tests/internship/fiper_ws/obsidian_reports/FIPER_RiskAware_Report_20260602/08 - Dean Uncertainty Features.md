---
title: Dean Uncertainty Features
created: 2026-06-02
tags:
  - fiper/uncertainty
  - dean
---

# Dean Uncertainty Features

Dean collected a newer dataset using a modified SimVLA checkpoint that exposes 49 uncertainty features plus 49 deltas, for 98 additional features per timestep.

## Datasets

| Split | Episodes used | Successes | Failures | Purpose |
|---|---:|---:|---:|---|
| all-tasks random | 4191 | 3405 | 786 | test if uncertainty helps when all tasks are seen |
| last-2-taskids OOD | 4191 total pool | 3405 | 786 | hold out last task ids for cleaner OOD |

## Initial Results

![[assets/dean_uncertainty_features.png]]

| Split | Variant | FA | Detection | Det@25 | Det@50 | Decision |
|---|---|---:|---:|---:|---:|---|
| all-tasks random | base | 14.2% | 95.8% | 54.0% | 89.0% | strong |
| all-tasks random | unc_raw | 16.8% | 97.5% | 67.1% | 87.8% | better early detection, worse FA |
| OOD last2 | base | 26.0% | 86.0% | 39.8% | 78.5% | baseline |
| OOD last2 | unc_raw | 28.9% | 84.9% | 35.5% | 83.9% | not better overall |

## Interpretation

The uncertainty features contain signal, especially for early detection on seen splits, but raw 98D concatenation is not automatically better. The next useful direction is feature selection, regularization, or late fusion rather than blindly adding all uncertainty dimensions.
