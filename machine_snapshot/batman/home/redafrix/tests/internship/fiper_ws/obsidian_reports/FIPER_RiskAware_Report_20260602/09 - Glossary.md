---
title: Glossary
created: 2026-06-02
tags:
  - fiper/glossary
---

# Glossary

| Term | Meaning |
|---|---|
| FIPER | The monitoring dataset/pipeline built from receding SimVLA rollouts. It turns rollout timesteps into rows for training a risk detector. |
| SimVLA | The vision-language-action model used to generate robot action chunks. |
| VLA | Vision-language-action model: a model that uses images and language to output robot actions. |
| action chunk | A short sequence of future robot actions predicted together. In this work, chunks are usually 10 actions of 7 dimensions. |
| receding horizon | Execute only the first action of a predicted chunk, then re-query the model at the next timestep. |
| ACE | Action Chunking Error / action candidate disagreement signal. It measures how much candidate chunks vary across sampled seeds. |
| proprioception | Robot internal state, such as gripper pose/joint-related state, used as numeric input. |
| risk score | Scalar detector output. Higher means the current trajectory/action resembles failure cases. |
| false alarm | A success episode that the monitor flags as risky. Lower is better. |
| failure detection | A failure episode that the monitor flags at least once. Higher is better. |
| Det@25 | Fraction of failure episodes detected before 25% of the episode duration. |
| Det@50 | Fraction of failure episodes detected before 50% of the episode duration. |
| OOD | Out-of-distribution. Evaluation examples whose task, object, or perturbation was held out from training. |
| seen | Data distribution allowed in training/calibration. |
| fold | A train/test partition, often holding out particular objects or tasks. |
| held-out object | Object category intentionally excluded from training to test generalization. |
| calibration | Turning raw model scores into operational thresholds. |
| q95 | 95th percentile of risk scores on success calibration rows. |
| conformal mass | Episode-level accumulated risk evidence above q95. |
| alpha | Conformal calibration parameter. Here `alpha=0.15` means the threshold is tuned to tolerate roughly 15% calibration false alarms. |
| recovery | A paired seed where baseline failed but risk-aware succeeded. |
| regression | A paired seed where baseline succeeded but risk-aware failed. |
| same-seed comparison | Both methods run the same environment reset seeds in the same order. |
| transformer | Sequence model using attention to combine information from multiple timesteps/tokens. |
| attention head | One parallel attention mechanism inside a transformer layer. |
| dropout | Training regularization that randomly zeroes activations to reduce overfitting. |
| early stopping | Stop training when validation performance no longer improves. |
| leakage | Any input or split mistake that gives the model information it should not have, such as reward, success label, future state, or OOD examples in training. |
