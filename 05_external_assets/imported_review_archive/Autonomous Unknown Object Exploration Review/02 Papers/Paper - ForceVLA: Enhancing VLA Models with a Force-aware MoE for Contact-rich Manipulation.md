---
title: "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation"
authors: "Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Cewu Lu, Wenqiang Zhang"
year: 2025
venue: "NeurIPS 2025 / arXiv"
url: "https://arxiv.org/abs/2505.22159"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

## Metadata
- Authors: Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Cewu Lu, Wenqiang Zhang
- Year: 2025
- Venue: NeurIPS 2025 / arXiv
- Primary URL: https://arxiv.org/abs/2505.22159
- Abstract source: html_meta
- Abstract matched title: [2505.22159] ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

## Abstract
> Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## Why It Matters
- A clearly relevant 2025 precursor to the force-aware VLA branch, introducing six-axis force as a first-class input inside the action model and releasing a five-task force-rich dataset.
- A missing but clearly in-scope 2025 bridge between VLA and force-aware contact control: it adds a force-aware mixture-of-experts module and a five-task force dataset, showing concrete gains on contact-rich manipulation [S26].
- A directly relevant multimodal-control paper that makes six-axis force a first-class modality inside a VLA pipeline, rather than leaving contact adaptation to a separate controller.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
