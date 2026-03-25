---
title: "Active Visuo-Haptic Object Shape Completion"
authors: "Lukas Rustler, Jens Lundell, Jan Kristof Behrens, Ville Kyrki, Matej Hoffmann"
year: 2022
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2203.09149"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Active Visuo-Haptic Object Shape Completion

## Metadata
- Authors: Lukas Rustler, Jens Lundell, Jan Kristof Behrens, Ville Kyrki, Matej Hoffmann
- Year: 2022
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2203.09149
- Abstract source: arxiv_api

## Abstract
> Recent advancements in object shape completion have enabled impressive object reconstructions using only visual input. However, due to self-occlusion, the reconstructions have high uncertainty in the occluded object parts, which negatively impacts the performance of downstream robotic tasks such as grasping. In this work, we propose an active visuo-haptic shape completion method called Act-VH that actively computes where to touch the objects based on the reconstruction uncertainty. Act-VH reconstructs objects from point clouds and calculates the reconstruction uncertainty using IGR, a recent state-of-the-art implicit surface deep neural network. We experimentally evaluate the reconstruction accuracy of Act-VH against five baselines in simulation and in the real world. We also propose a new simulation environment for this purpose. The results show that Act-VH outperforms all baselines and that an uncertainty-driven haptic exploration policy leads to higher reconstruction accuracy than a random policy and a policy driven by Gaussian Process Implicit Surfaces. As a final experiment, we evaluate Act-VH and the best reconstruction baseline on grasping 10 novel objects. The results show that Act-VH reaches a significantly higher grasp success rate than the baseline on all objects. Together, this work opens up the door for using active visuo-haptic shape completion in more complex cluttered scenes.

## Why It Matters
- A clean example of uncertainty-driven active touch: it uses visual shape uncertainty to choose where to touch an unseen object and shows downstream grasp gains on novel objects [S1,S2].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
