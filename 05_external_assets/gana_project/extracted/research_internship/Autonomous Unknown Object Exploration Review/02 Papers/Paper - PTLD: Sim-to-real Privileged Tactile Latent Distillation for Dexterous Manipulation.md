---
title: "PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation"
authors: "Rosy Chen, Mustafa Mukadam, Michael Kaess, Tingfan Wu, Francois R. Hogan, Jitendra Malik, Akash Sharma"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2603.04531"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation

## Metadata
- Authors: Rosy Chen, Mustafa Mukadam, Michael Kaess, Tingfan Wu, Francois R. Hogan, Jitendra Malik, Akash Sharma
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2603.04531
- Abstract source: html_meta
- Abstract matched title: [2603.04531] PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation

## Abstract
> Tactile dexterous manipulation is essential to automating complex household tasks, yet learning effective control policies remains a challenge. While recent work has relied on imitation learning, obtaining high quality demonstrations for multi-fingered hands via robot teleoperation or kinesthetic teaching is prohibitive. Alternatively, with reinforcement we can learn skills in simulation, but fast and realistic simulation of tactile observations is challenging. To bridge this gap, we introduce PTLD: sim-to-real Privileged Tactile Latent Distillation, a novel approach to learning tactile manipulation skills without requiring tactile simulation. Instead of simulating tactile sensors or relying purely on proprioceptive policies to transfer zero-shot sim-to-real, our key idea is to leverage privileged sensors in the real world to collect real-world tactile policy data. This data is then used to distill a robust state estimator that operates on tactile input. We demonstrate from our experiments that PTLD can be used to improve proprioceptive manipulation policies trained in simulation significantly by incorporating tactile sensing. On the benchmark in-hand rotation task, PTLD achieves a 182% improvement over a proprioception only policy. We also show that PTLD enables learning the challenging task of tactile in-hand reorientation where we see a 57% improvement in the number of goals reached over using proprioception alone. Website: https://akashsharma02.github.io/ptld-website/.

## Why It Matters
- Shows a practical 2026 alternative to tactile simulation by distilling tactile state estimation from privileged real-world data into sim-trained manipulation policies.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
