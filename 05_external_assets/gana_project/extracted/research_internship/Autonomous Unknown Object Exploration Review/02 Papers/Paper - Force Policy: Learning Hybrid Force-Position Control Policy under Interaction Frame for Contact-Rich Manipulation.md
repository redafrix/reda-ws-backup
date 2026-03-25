---
title: "Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation"
authors: "Hongjie Fang, Shirun Tang, Mingyu Mei, Haoxiang Qin, Zihao He, Jingjing Chen, Ying Feng, Chenxi Wang, Wanxi Liu, Zaixing He, Cewu Lu, Shiquan Wang"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2602.22088"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

## Metadata
- Authors: Hongjie Fang, Shirun Tang, Mingyu Mei, Haoxiang Qin, Zihao He, Jingjing Chen, Ying Feng, Chenxi Wang, Wanxi Liu, Zaixing He, Cewu Lu, Shiquan Wang
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2602.22088
- Abstract source: html_meta
- Abstract matched title: [2602.22088] Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

## Abstract
> Contact-rich manipulation demands human-like integration of perception and force feedback: vision should guide task progress, while high-frequency interaction control must stabilize contact under uncertainty. Existing learning-based policies often entangle these roles in a monolithic network, trading off global generalization against stable local refinement, while control-centric approaches typically assume a known task structure or learn only controller parameters rather than the structure itself. In this paper, we formalize a physically grounded interaction frame, an instantaneous local basis that decouples force regulation from motion execution, and propose a method to recover it from demonstrations. Based on this, we address both issues by proposing Force Policy, a global-local vision-force policy in which a global policy guides free-space actions using vision, and upon contact, a high-frequency local policy with force feedback estimates the interaction frame and executes hybrid force-position control for stable interaction. Real-world experiments across diverse contact-rich tasks show consistent gains over strong baselines, with more robust contact establishment, more accurate force regulation, and reliable generalization to novel objects with varied geometries and physical properties, ultimately improving both contact stability and execution quality. Project page: https://force-policy.github.io/

## Why It Matters
- Introduces an interaction-frame representation recovered from physical response and uses it to split global vision guidance from high-frequency force regulation, directly targeting stable contact under geometric and physical variation.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
