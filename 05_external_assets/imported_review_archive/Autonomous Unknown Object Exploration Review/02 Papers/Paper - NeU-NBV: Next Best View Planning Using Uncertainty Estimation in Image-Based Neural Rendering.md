---
title: "NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering"
authors: "Liren Jin, Xieyuanli Chen, Julius Rueckin, Marija Popovic"
year: 2023
venue: "IROS 2023"
url: "https://arxiv.org/abs/2303.01284"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering

## Metadata
- Authors: Liren Jin, Xieyuanli Chen, Julius Rueckin, Marija Popovic
- Year: 2023
- Venue: IROS 2023
- Primary URL: https://arxiv.org/abs/2303.01284
- Abstract source: html_meta
- Abstract matched title: [2303.01284] NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering

## Abstract
> Autonomous robotic tasks require actively perceiving the environment to achieve application-specific goals. In this paper, we address the problem of positioning an RGB camera to collect the most informative images to represent an unknown scene, given a limited measurement budget. We propose a novel mapless planning framework to iteratively plan the next best camera view based on collected image measurements. A key aspect of our approach is a new technique for uncertainty estimation in image-based neural rendering, which guides measurement acquisition at the most uncertain view among view candidates, thus maximising the information value during data collection. By incrementally adding new measurements into our image collection, our approach efficiently explores an unknown scene in a mapless manner. We show that our uncertainty estimation is generalisable and valuable for view planning in unknown scenes. Our planning experiments using synthetic and real-world data verify that our uncertainty-guided approach finds informative images leading to more accurate scene representations when compared against baselines.

## Why It Matters
- A mapless RGB-camera NBV planner using uncertainty in image-based neural rendering, important for active scanning without explicit maps [S5,S21].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
