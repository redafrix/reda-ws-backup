---
title: Negative and Rejected Ideas
created: 2026-06-02
tags:
  - fiper/negative-results
---

# Negative and Rejected Ideas

This project tried many directions. The goal of this note is not to list every minor run, but to preserve the important decision evidence.

## Capacity Scaling

Larger transformer variants were expected to help, but they did not. They tended to overfit early and increase false alarms. Smaller variants were not clearly better.

## Dynamic Thresholds

Step-varying and history-varying thresholds were plausible because success episodes sometimes recover after a risk spike. In practice they did not beat the selected static conformal mass policy enough to justify replacing it.

## Official Expert Actions

Official expert demonstrations were useful as a source of intuition, but not as a final detector component.

| Test | Positive | Failure mode |
|---|---|---|
| action normality | false alarms decreased | recall collapsed |
| autoencoder veto | OOD FA very low | failure detection collapsed |
| action encoder pretraining | mechanically worked | did not beat existing model |

## ACE Subsampling

Reducing ACE to first 4 candidates every 2 steps lowered OOD false alarms, but it hurt early detection too much. For a real-time safety monitor, detecting failures late is often not useful.

## Chunk Execution

Full action chunk execution was surprisingly strong on Task7, but it changes the control policy itself. It is not the same scientific question as risk-aware first-action receding horizon, so it was paused and not selected as the main FIPER risk-aware story.
