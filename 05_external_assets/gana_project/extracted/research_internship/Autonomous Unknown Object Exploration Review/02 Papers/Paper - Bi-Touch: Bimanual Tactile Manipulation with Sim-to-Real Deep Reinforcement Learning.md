---
title: "Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning"
authors: "Yijiong Lin, Alex Church, Max Yang, Haoran Li, John Lloyd, Dandan Zhang, Nathan F. Lepora"
year: 2023
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2307.06423"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning

## Metadata
- Authors: Yijiong Lin, Alex Church, Max Yang, Haoran Li, John Lloyd, Dandan Zhang, Nathan F. Lepora
- Year: 2023
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2307.06423
- Abstract source: arxiv_api

## Abstract
> Bimanual manipulation with tactile feedback will be key to human-level robot dexterity. However, this topic is less explored than single-arm settings, partly due to the availability of suitable hardware along with the complexity of designing effective controllers for tasks with relatively large state-action spaces. Here we introduce a dual-arm tactile robotic system (Bi-Touch) based on the Tactile Gym 2.0 setup that integrates two affordable industrial-level robot arms with low-cost high-resolution tactile sensors (TacTips). We present a suite of bimanual manipulation tasks tailored towards tactile feedback: bi-pushing, bi-reorienting and bi-gathering. To learn effective policies, we introduce appropriate reward functions for these tasks and propose a novel goal-update mechanism with deep reinforcement learning. We also apply these policies to real-world settings with a tactile sim-to-real approach. Our analysis highlights and addresses some challenges met during the sim-to-real application, e.g. the learned policy tended to squeeze an object in the bi-reorienting task due to the sim-to-real gap. Finally, we demonstrate the generalizability and robustness of this system by experimenting with different unseen objects with applied perturbations in the real world. Code and videos are available at https://sites.google.com/view/bi-touch/.

## Why It Matters
- Extends tactile RL from single-arm tasks to coordinated dual-arm manipulation and tests robustness on unseen real objects under perturbations.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
