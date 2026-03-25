---
title: "CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation"
authors: "Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2601.15541"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation

## Metadata
- Authors: Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2601.15541
- Abstract source: arxiv_api

## Abstract
> We propose a CompliantVLA-adaptor that augments the state-of-the-art Vision-Language-Action (VLA) models with vision-language model (VLM)-informed context-aware variable impedance control (VIC) to improve the safety and effectiveness of contact-rich robotic manipulation tasks. Existing VLA systems (e.g., RDT, Pi0.5, OpenVLA-oft) typically output position, but lack force-aware adaptation, leading to unsafe or failed interactions in physical tasks involving contact, compliance, or uncertainty. In the proposed CompliantVLA-adaptor, a VLM interprets task context from images and natural language to adapt the stiffness and damping parameters of a VIC controller. These parameters are further regulated using real-time force/torque feedback to ensure interaction forces remain within safe thresholds. We demonstrate that our method outperforms the VLA baselines on a suite of complex contact-rich tasks, both in simulation and the real world, with improved success rates and reduced force violations. This work presents a promising path towards a safe foundation model for physical contact-rich manipulation. We release our code, prompts, and force-torque-impedance-scenario context datasets at https://sites.google.com/view/compliantvla.

## Why It Matters
- Adds a distinct compliance-aware VLA branch, showing that explicit compliance augmentation can materially improve contact-rich task success.
- Provides a complementary 2026 direction in which compliance rather than tactile sensing or force sensing is the adaptation target, and it reports a measurable success-rate improvement on contact-rich tasks.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
