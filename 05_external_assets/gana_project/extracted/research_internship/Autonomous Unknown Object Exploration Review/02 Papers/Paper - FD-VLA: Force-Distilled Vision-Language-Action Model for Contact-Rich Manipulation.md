---
title: "FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation"
authors: "Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2602.02142"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

## Metadata
- Authors: Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2602.02142
- Abstract source: html_meta
- Abstract matched title: [2602.02142] FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

## Abstract
> Force sensing is a crucial modality for Vision-Language-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks. We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors. The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and robot states, into a predicted force token aligned with the latent representation of actual force signals. During inference, this distilled force token is injected into the pretrained VLM, enabling force-aware reasoning while preserving the integrity of its vision-language semantics. This design provides two key benefits: first, it allows practical deployment across a wide range of robots that lack expensive or fragile force-torque sensors, thereby reducing hardware cost and complexity; second, the FDM introduces an additional force-vision-state fusion prior to the VLM, which improves cross-modal alignment and enhances perception-action robustness in contact-rich scenarios. Surprisingly, our physical experiments show that the distilled force token outperforms direct sensor force measurements as well as other baselines, which highlights the effectiveness of this force-distilled VLA approach.

## Why It Matters
- Introduces force distillation as a way to keep force-aware reasoning inside a VLA without requiring physical force sensors at inference time.
- Adds a distinct 2026 force-aware path that distills force into a latent token and explicitly argues that the distilled token can outperform direct force sensing in physical experiments, which broadens the design space beyond hardware-force-at-inference.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
