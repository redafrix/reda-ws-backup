---
title: "Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields"
authors: "Soomin Lee, Le Chen, Jiahao Wang, Alexander Liniger, Suryansh Kumar, Fisher Yu"
year: 2022
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2209.08409"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields

## Metadata
- Authors: Soomin Lee, Le Chen, Jiahao Wang, Alexander Liniger, Suryansh Kumar, Fisher Yu
- Year: 2022
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2209.08409
- Abstract source: html_meta
- Abstract matched title: [2209.08409] Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields

## Abstract
> In this paper, we tackle the problem of active robotic 3D reconstruction of an object. In particular, we study how a mobile robot with an arm-held camera can select a favorable number of views to recover an object's 3D shape efficiently. Contrary to the existing solution to this problem, we leverage the popular neural radiance fields-based object representation, which has recently shown impressive results for various computer vision tasks. However, it is not straightforward to directly reason about an object's explicit 3D geometric details using such a representation, making the next-best-view selection problem for dense 3D reconstruction challenging. This paper introduces a ray-based volumetric uncertainty estimator, which computes the entropy of the weight distribution of the color samples along each ray of the object's implicit neural representation. We show that it is possible to infer the uncertainty of the underlying 3D geometry given a novel view with the proposed estimator. We then present a next-best-view selection policy guided by the ray-based volumetric uncertainty in neural radiance fields-based representations. Encouraging experimental results on synthetic and real-world data suggest that the approach presented in this paper can enable a new research direction of using an implicit 3D object representation for the next-best-view problem in robot vision applications, distinguishing our approach from the existing approaches that rely on explicit 3D geometric modeling.

## Why It Matters
- One of the first robot-vision papers to formulate object NBV directly on a NeRF-style implicit representation with a ray-based uncertainty estimator [S3].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
