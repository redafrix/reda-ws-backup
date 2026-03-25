---
title: "Affordance-Driven Next-Best-View Planning for Robotic Grasping"
authors: "Xuechao Zhang, Dong Wang, Sun Han, Weichuang Li, Bin Zhao, Zhigang Wang, Xiaoming Duan, Chongrong Fang, Xuelong Li, Jianping He"
year: 2023
venue: "Conference on Robot Learning"
url: "https://proceedings.mlr.press/v229/zhang23i.html"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Affordance-Driven Next-Best-View Planning for Robotic Grasping

## Metadata
- Authors: Xuechao Zhang, Dong Wang, Sun Han, Weichuang Li, Bin Zhao, Zhigang Wang, Xiaoming Duan, Chongrong Fang, Xuelong Li, Jianping He
- Year: 2023
- Venue: Conference on Robot Learning
- Primary URL: https://proceedings.mlr.press/v229/zhang23i.html
- Abstract source: pmlr_html

## Abstract
> Grasping occluded objects in cluttered environments is an essential component in complex robotic manipulation tasks. In this paper, we introduce an AffordanCE-driven Next-Best-View planning policy (ACE-NBV) that tries to find a feasible grasp for target object via continuously observing scenes from new viewpoints. This policy is motivated by the observation that the grasp affordances of an occluded object can be better-measured under the view when the view-direction are the same as the grasp view. Specifically, our method leverages the paradigm of novel view imagery to predict the grasps affordances under previously unobserved view, and select next observation view based on the highest imagined grasp quality of the target object. The experimental results in simulation and on a real robot demonstrate the effectiveness of the proposed affordance-driven next-best-view planning policy. Project page: https://sszxc.net/ace-nbv/.

## Why It Matters
- Directly optimizes viewpoints for target grasp affordance under occlusion, making the downstream task itself the NBV objective [S7].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
