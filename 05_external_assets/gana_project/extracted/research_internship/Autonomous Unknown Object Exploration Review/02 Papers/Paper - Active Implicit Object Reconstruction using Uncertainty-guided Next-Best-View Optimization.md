---
title: "Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization"
authors: "Dongyu Yan, Jianheng Liu, Fengyu Quan, Haoyao Chen, Mengmeng Fu"
year: 2023
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2303.16739"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization

## Metadata
- Authors: Dongyu Yan, Jianheng Liu, Fengyu Quan, Haoyao Chen, Mengmeng Fu
- Year: 2023
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2303.16739
- Abstract source: arxiv_api

## Abstract
> Actively planning sensor views during object reconstruction is crucial for autonomous mobile robots. An effective method should be able to strike a balance between accuracy and efficiency. In this paper, we propose a seamless integration of the emerging implicit representation with the active reconstruction task. We build an implicit occupancy field as our geometry proxy. While training, the prior object bounding box is utilized as auxiliary information to generate clean and detailed reconstructions. To evaluate view uncertainty, we employ a sampling-based approach that directly extracts entropy from the reconstructed occupancy probability field as our measure of view information gain. This eliminates the need for additional uncertainty maps or learning. Unlike previous methods that compare view uncertainty within a finite set of candidates, we aim to find the next-best-view (NBV) on a continuous manifold. Leveraging the differentiability of the implicit representation, the NBV can be optimized directly by maximizing the view uncertainty using gradient descent. It significantly enhances the method's adaptability to different scenarios. Simulation and real-world experiments demonstrate that our approach effectively improves reconstruction accuracy and efficiency of view planning in active reconstruction tasks. The proposed system will open source at https://github.com/HITSZ-NRSL/ActiveImplicitRecon.git.

## Why It Matters
- Shows a continuous-manifold NBV optimizer over an implicit occupancy field, avoiding finite candidate-view selection and strengthening the implicit-reconstruction branch [S4].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
