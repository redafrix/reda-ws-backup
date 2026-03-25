---
title: "Active Implicit Reconstruction Using One-Shot View Planning"
authors: "Hao Hu, Sicong Pan, Liren Jin, Marija Popovic, Maren Bennewitz"
year: 2024
venue: "ICRA 2024"
url: "https://arxiv.org/abs/2310.00685"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Active Implicit Reconstruction Using One-Shot View Planning

## Metadata
- Authors: Hao Hu, Sicong Pan, Liren Jin, Marija Popovic, Maren Bennewitz
- Year: 2024
- Venue: ICRA 2024
- Primary URL: https://arxiv.org/abs/2310.00685
- Abstract source: arxiv_api

## Abstract
> Active object reconstruction using autonomous robots is gaining great interest. A primary goal in this task is to maximize the information of the object to be reconstructed, given limited on-board resources. Previous view planning methods exhibit inefficiency since they rely on an iterative paradigm based on explicit representations, consisting of (1) planning a path to the next-best view only; and (2) requiring a considerable number of less-gain views in terms of surface coverage. To address these limitations, we propose to integrate implicit representations into the One-Shot View Planning (OSVP). The key idea behind our approach is to use implicit representations to obtain the small missing surface areas instead of observing them with extra views. Therefore, we design a deep neural network, named OSVP, to directly predict a set of views given a dense point cloud refined from an initial sparse observation. To train our OSVP network, we generate supervision labels using dense point clouds refined by implicit representations and set covering optimization problems. Simulated experiments show that our method achieves sufficient reconstruction quality, outperforming several baselines under limited view and movement budgets. We further demonstrate the applicability of our approach in a real-world object reconstruction scenario.

## Why It Matters
- Represents the transition from greedy iterative NBV to one-shot view-set prediction with implicit completion of small missing surfaces [S9].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
