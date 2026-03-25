---
title: "TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation"
authors: "Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li, Jiaming Jiang, Chenxi Xiao, Ziyuan Jiao"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2601.20321"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation

## Metadata
- Authors: Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li, Jiaming Jiang, Chenxi Xiao, Ziyuan Jiao
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2601.20321
- Abstract source: html_meta
- Abstract matched title: [2601.20321] TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation

## Abstract
> Vision-Language-Action (VLA) models have recently emerged as powerful generalists for robotic manipulation. However, due to their predominant reliance on visual modalities, they fundamentally lack the physical intuition required for contact-rich tasks that require precise force regulation and physical reasoning. Existing attempts to incorporate vision-based tactile sensing into VLA models typically treat tactile inputs as auxiliary visual textures, thereby overlooking the underlying correlation between surface deformation and interaction dynamics. To bridge this gap, we propose a paradigm shift from tactile-vision alignment to tactile-force alignment. Here, we introduce TaF-VLA, a framework that explicitly grounds high-dimensional tactile observations in physical interaction forces. To facilitate this, we develop an automated tactile-force data acquisition device and curate the TaF-Dataset, comprising over 10 million synchronized tactile observations, 6-axis force/torque, and matrix force map. To align sequential tactile observations with interaction forces, the central component of our approach is the Tactile-Force Adapter (TaF-Adapter), a tactile sensor encoder that extracts discretized latent information for encoding tactile observations. This mechanism ensures that the learned representations capture history-dependent, noise-insensitive physical dynamics rather than static visual textures. Finally, we integrate this force-aligned encoder into a VLA backbone. Extensive real-world experiments demonstrate that TaF-VLA policy significantly outperforms state-of-the-art tactile-vision-aligned and vision-only baselines on contact-rich tasks, verifying its ability to achieve robust, force-aware manipulation through cross-modal physical reasoning.

## Why It Matters
- Adds a physically grounded tactile-force alignment branch to the VLA literature, with a 10-million-sample tactile-force dataset and explicit grounding of tactile tokens in interaction forces [S29].
- A relevant 2026 multimodal paper that argues tactile data should be aligned to physical force rather than treated as another visual texture, pushing multimodal fusion in a more physically grounded direction.

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
