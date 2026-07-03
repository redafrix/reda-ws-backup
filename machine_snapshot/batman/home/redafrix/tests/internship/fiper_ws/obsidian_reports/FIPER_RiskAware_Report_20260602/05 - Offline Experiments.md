---
title: Offline Experiments
created: 2026-06-02
tags:
  - fiper/results
  - offline
---

# Offline Experiments

## Selected Baseline Metrics

![[assets/selected_detector_metrics.png]]

| Metric | Value |
|---|---:|
| Seen FA | 15.4% |
| OOD FA | 25.6% |
| OOD failure detection | 95.2% |
| OOD Det@25 | 26.2% |
| OOD Det@50 | 85.7% |
| Mean detection time | 0.332 |

## ACE Sampling Ablation

![[assets/ace_sampling_ablation.png]]

| Variant | Seen FA | OOD FA | Recall | Det@25 | Det@50 | Decision |
|---|---:|---:|---:|---:|---:|---|
| existing `v2_018` | 15.4% | 25.6% | 95.2% | 26.2% | 85.7% | selected |
| full8 every 2 steps | 14.0% | 26.5% | 92.9% | 19.0% | 83.3% | rejected |
| first4 every step | 15.4% | 28.0% | 95.2% | 31.0% | 90.5% | rejected: FA worse |
| first4 every 2 steps | 14.0% | 20.4% | 95.2% | 14.3% | 81.0% | interesting but slower detection |

## Capacity and History Sweep

Bigger transformers did not improve the final decision rule. Some large models overfit very early, often around epoch 1-2. Smaller models approached the baseline but did not reduce OOD false alarms enough.

## Official Expert Data Tests

| Idea | Result | Decision |
|---|---|---|
| Gaussian/normality check on official actions | reduced false alarms but killed recall | rejected |
| official action autoencoder as veto | OOD FA down to 2.8%, but failure detection down to 26.2% | rejected |
| official action encoder pretraining | did not beat real existing `v2_018`; OOD FA increased 25.6% -> 28.4% | rejected |

![[assets/discarded_ideas_summary.png]]

## Dynamic Threshold Tests

Step-dependent and history-dependent threshold variants did not improve enough over static conformal mass. The selected policy stayed `score_q95_mass_conformal_alpha_0.15`.
