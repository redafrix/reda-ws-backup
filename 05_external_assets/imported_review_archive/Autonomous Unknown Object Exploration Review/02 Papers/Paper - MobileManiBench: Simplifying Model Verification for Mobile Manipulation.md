---
title: "MobileManiBench: Simplifying Model Verification for Mobile Manipulation"
authors: "Wenbo Wang, Fangyun Wei, QiXiu Li, Xi Chen, Yaobo Liang, Chang Xu, Jiaolong Yang, Baining Guo"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2602.05233"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# MobileManiBench: Simplifying Model Verification for Mobile Manipulation

## Metadata
- Authors: Wenbo Wang, Fangyun Wei, QiXiu Li, Xi Chen, Yaobo Liang, Chang Xu, Jiaolong Yang, Baining Guo
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2602.05233
- Abstract source: html_meta
- Abstract matched title: [2602.05233] MobileManiBench: Simplifying Model Verification for Mobile Manipulation

## Abstract
> Vision-language-action models have advanced robotic manipulation but remain constrained by reliance on the large, teleoperation-collected datasets dominated by the static, tabletop scenes. We propose a simulation-first framework to verify VLA architectures before real-world deployment and introduce MobileManiBench, a large-scale benchmark for mobile-based robotic manipulation. Built on NVIDIA Isaac Sim and powered by reinforcement learning, our pipeline autonomously generates diverse manipulation trajectories with rich annotations (language instructions, multi-view RGB-depth-segmentation images, synchronized object/robot states and actions). MobileManiBench features 2 mobile platforms (parallel-gripper and dexterous-hand robots), 2 synchronized cameras (head and right wrist), 630 objects in 20 categories, 5 skills (open, close, pull, push, pick) with over 100 tasks performed in 100 realistic scenes, yielding 300K trajectories. This design enables controlled, scalable studies of robot embodiments, sensing modalities, and policy architectures, accelerating research on data efficiency and generalization. We benchmark representative VLA models and report insights into perception, reasoning, and control in complex simulated environments.

## Why It Matters
- Introduces a large-scale mobile-manipulation benchmark with 630 objects, 20 categories, 100+ tasks, 100 scenes, and 300K trajectories, directly targeting evaluation of VLA generalization before deployment [S12].

## Mentioned In
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
