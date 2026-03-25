---
title: "Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry"
authors: "Siyuan Dong, Devesh K. Jha, Diego Romeres, Sangwoon Kim, Daniel Nikovski, Alberto Rodriguez"
year: 2021
venue: "ICRA 2021"
url: "https://arxiv.org/abs/2104.01167"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry

## Metadata
- Authors: Siyuan Dong, Devesh K. Jha, Diego Romeres, Sangwoon Kim, Daniel Nikovski, Alberto Rodriguez
- Year: 2021
- Venue: ICRA 2021
- Primary URL: https://arxiv.org/abs/2104.01167
- Abstract source: html_meta
- Abstract matched title: [2104.01167] Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry

## Abstract
> Object insertion is a classic contact-rich manipulation task. The task remains challenging, especially when considering general objects of unknown geometry, which significantly limits the ability to understand the contact configuration between the object and the environment. We study the problem of aligning the object and environment with a tactile-based feedback insertion policy. The insertion process is modeled as an episodic policy that iterates between insertion attempts followed by pose corrections. We explore different mechanisms to learn such a policy based on Reinforcement Learning. The key contribution of this paper is to demonstrate that it is possible to learn a tactile insertion policy that generalizes across different object geometries, and an ablation study of the key design choices for the learning agent: 1) the type of learning scheme: supervised vs. reinforcement learning; 2) the type of learning schedule: unguided vs. curriculum learning; 3) the type of sensing modality: force/torque (F/T) vs. tactile; and 4) the type of tactile representation: tactile RGB vs. tactile flow. We show that the optimal configuration of the learning agent (RL + curriculum + tactile flow) exposed to 4 training objects yields an insertion policy that inserts 4 novel objects with over 85.0% success rate and within 3~4 attempts. Comparisons between F/T and tactile sensing, shows that while an F/T-based policy learns more efficiently, a tactile-based policy provides better generalization.

## Why It Matters
- A direct early-window unknown-object RL result: tactile insertion is formulated as a correction policy that generalizes to novel geometries.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
