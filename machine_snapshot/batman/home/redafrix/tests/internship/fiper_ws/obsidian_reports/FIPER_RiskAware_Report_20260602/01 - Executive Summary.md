---
title: Executive Summary
created: 2026-06-02
tags:
  - fiper/summary
  - risk-aware
---

# Executive Summary

## Selected Idea

The selected idea is a temporal risk detector named `v2_018_transformer_k16`. It predicts whether the current SimVLA trajectory is entering failure risk. It is not a hard stop by itself. In real time, it is used as an action-selection helper: when the normal SimVLA action chunk looks risky and a candidate chunk looks clearly safer, the system executes the safer candidate.

## Why This Idea Was Kept

Offline, the detector had the best practical balance we found:

| Metric | Value |
|---|---:|
| Seen false alarm | 15.4% |
| OOD false alarm | 25.6% |
| OOD failure detection | 95.2% |
| OOD Det@25 | 26.2% |
| OOD Det@50 | 85.7% |
| Mean detection time | 0.332 |

![[assets/selected_detector_metrics.png]]

Real-time, it improved the 4-task same-seed comparison:

| Metric | Baseline SimVLA | Risk-aware SimVLA |
|---|---:|---:|
| Paired episodes | 1881 | 1881 |
| Successes | 1021 | 1077 |
| Success rate | 54.3% | 57.3% |
| Net gain | | +3.0 percentage points |

## Important Caveat

The detector recovers failures but also causes regressions. The main engineering problem is no longer "can it help?" It can. The next problem is reducing harmful interventions while keeping the recoveries.

![[assets/recoveries_vs_regressions.png]]
