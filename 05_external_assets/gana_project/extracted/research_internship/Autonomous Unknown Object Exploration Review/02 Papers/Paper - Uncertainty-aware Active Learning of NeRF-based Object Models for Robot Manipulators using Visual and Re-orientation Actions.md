---
title: "Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions"
authors: "Saptarshi Dasgupta, Akshat Gupta, Shreshth Tuli, Rohan Paul"
year: 2024
venue: "arXiv preprint; accepted poster in ICRA 2024 RoboNeRF workshop"
url: "https://arxiv.org/abs/2404.01812"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions

## Metadata
- Authors: Saptarshi Dasgupta, Akshat Gupta, Shreshth Tuli, Rohan Paul
- Year: 2024
- Venue: arXiv preprint; accepted poster in ICRA 2024 RoboNeRF workshop
- Primary URL: https://arxiv.org/abs/2404.01812
- Abstract source: html_meta
- Abstract matched title: [2404.01812] Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions

## Abstract
> Manipulating unseen objects is challenging without a 3D representation, as objects generally have occluded surfaces. This requires physical interaction with objects to build their internal representations. This paper presents an approach that enables a robot to rapidly learn the complete 3D model of a given object for manipulation in unfamiliar orientations. We use an ensemble of partially constructed NeRF models to quantify model uncertainty to determine the next action (a visual or re-orientation action) by optimizing informativeness and feasibility. Further, our approach determines when and how to grasp and re-orient an object given its partial NeRF model and re-estimates the object pose to rectify misalignments introduced during the interaction. Experiments with a simulated Franka Emika Robot Manipulator operating in a tabletop environment with benchmark objects demonstrate an improvement of (i) 14% in visual reconstruction quality (PSNR), (ii) 20% in the geometric/depth reconstruction of the object surface (F-score) and (iii) 71% in the task success rate of manipulating objects a-priori unseen orientations/stable configurations in the scene; over current methods. The project page can be found here: https://actnerf.github.io.

## Why It Matters
- Directly targets the single-manipulator setting by allowing both visual view changes and physical reorientation actions, and shows that object-centric radiance fields can support downstream manipulation.
- Makes the active perception loop manipulation-aware by letting the robot decide between looking and physically reorienting the object [S11].

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
