---
title: "Touch begins where vision ends: Generalizable policies for contact-rich manipulation"
authors: "Zifan Zhao, Siddhant Haldar, Jinda Cui, Lerrel Pinto, Raunaq Bhirangi"
year: 2025
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2506.13762"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Touch begins where vision ends: Generalizable policies for contact-rich manipulation

## Metadata
- Authors: Zifan Zhao, Siddhant Haldar, Jinda Cui, Lerrel Pinto, Raunaq Bhirangi
- Year: 2025
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2506.13762
- Abstract source: html_meta
- Abstract matched title: [2506.13762] Touch begins where vision ends: Generalizable policies for contact-rich manipulation

## Abstract
> Data-driven approaches struggle with precise manipulation; imitation learning requires many hard-to-obtain demonstrations, while reinforcement learning yields brittle, non-generalizable policies. We introduce VisuoTactile Local (ViTaL) policy learning, a framework that solves fine-grained manipulation tasks by decomposing them into two phases: a reaching phase, where a vision-language model (VLM) enables scene-level reasoning to localize the object of interest, and a local interaction phase, where a reusable, scene-agnostic ViTaL policy performs contact-rich manipulation using egocentric vision and tactile sensing. This approach is motivated by the observation that while scene context varies, the low-level interaction remains consistent across task instances. By training local policies once in a canonical setting, they can generalize via a localize-then-execute strategy. ViTaL achieves around 90% success on contact-rich tasks in unseen environments and is robust to distractors. ViTaL's effectiveness stems from three key insights: (1) foundation models for segmentation enable training robust visual encoders via behavior cloning; (2) these encoders improve the generalizability of policies learned using residual RL; and (3) tactile sensing significantly boosts performance in contact-rich tasks. Ablation studies validate each of these insights, and we demonstrate that ViTaL integrates well with high-level VLMs, enabling robust, reusable low-level skills. Results and videos are available at https://vitalprecise.github.io.

## Why It Matters
- Captures the 2025 shift toward reusable local tactile policies that generalize across unseen environments when combined with high-level visual localization.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
