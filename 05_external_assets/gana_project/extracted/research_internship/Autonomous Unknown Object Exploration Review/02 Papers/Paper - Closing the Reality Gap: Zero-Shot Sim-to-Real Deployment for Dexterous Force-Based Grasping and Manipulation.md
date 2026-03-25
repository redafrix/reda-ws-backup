---
title: "Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation"
authors: "Haoyu Dong, Zhengmao He, Yang Li, Zhibin Li, Xinyu Yi, Zhe Zhao"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2601.02778"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation

## Metadata
- Authors: Haoyu Dong, Zhengmao He, Yang Li, Zhibin Li, Xinyu Yi, Zhe Zhao
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2601.02778
- Abstract source: arxiv_api

## Abstract
> Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities, but training control policies that can directly deploy on real hardware remains difficult due to contact-rich physics and imperfect actuation. We close this gap with a practical sim-to-real reinforcement learning (RL) framework that utilizes dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling to bridge the actuation gaps with randomization of non-ideal effects such as backlash, torque-speed saturation. Using an asymmetric actor-critic PPO pipeline trained entirely in simulation, our policies deploy directly to a five-finger hand. The resulting policies demonstrated two essential skills: (1) command-based, controllable grasp force tracking, and (2) reorientation of objects in the hand, both of which were robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with effective sensing/actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## Why It Matters
- Uses an asymmetric actor-critic PPO pipeline with dense tactile feedback and torque sensing to achieve zero-shot sim-to-real force tracking and reorientation.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
