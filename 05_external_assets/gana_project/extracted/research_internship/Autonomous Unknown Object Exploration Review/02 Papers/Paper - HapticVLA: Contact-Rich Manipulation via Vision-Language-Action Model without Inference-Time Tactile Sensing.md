---
title: "HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing"
authors: "Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov, Ogunwoye Faith Ouwatobi, Marcelino Fernando, Artem Asanov, Ziang Guo, Dzmitry Tsetserukou"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2603.15257"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing

## Metadata
- Authors: Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov, Ogunwoye Faith Ouwatobi, Marcelino Fernando, Artem Asanov, Ziang Guo, Dzmitry Tsetserukou
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2603.15257
- Abstract source: html_meta
- Abstract matched title: [2603.15257] HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing

## Abstract
> Tactile sensing is a crucial capability for Vision-Language-Action (VLA) architectures, as it enables dexterous and safe manipulation in contact-rich tasks. However, reliance on dedicated tactile hardware increases cost and reduces reproducibility across robotic platforms. We argue that tactile-aware manipulation can be learned offline and deployed without direct haptic feedback at inference. To this end, we present HapticVLA, which proceeds in two tightly coupled stages: Safety-Aware Reward-Weighted Flow Matching (SA-RWFM) and Tactile Distillation (TD). SA-RWFM trains a flow-matching action expert that incorporates precomputed, safety-aware tactile rewards penalizing excessive grasping force and suboptimal grasping trajectories. TD further transfers this tactile-aware capability into a conventional VLA: we distill a compact tactile token from the SA-RWFM teacher and train a student VLA to predict that token from vision and state modalities, enabling tactile-aware action generation at inference without requiring on-board tactile sensors. This design preserves contact-rich tactile-aware reasoning within VLA while removing the need for on-board tactile sensors during deployment. On real-world experiments, HapticVLA achieves a mean success rate of 86.7%, consistently outperforming baseline VLAs - including versions provided with direct tactile feedback during inference.

## Why It Matters
- A notable March 2026 branch showing that tactile-aware behavior can be distilled offline and deployed without inference-time tactile hardware while still outperforming baseline VLAs on contact-rich manipulation [S27].
- Important because it explores a different multimodal design point: using tactile feedback during training and distillation, but not requiring tactile hardware at inference.

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
