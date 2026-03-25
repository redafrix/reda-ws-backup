---
title: "Direction Matters: Learning Force Direction Enables Sim-to-Real Contact-Rich Manipulation"
authors: "Yifei Yang, Anzhe Chen, Zhenjie Zhu, Kechun Xu, Yunxuan Mao, Yufei Wei, Lu Chen, Rong Xiong, Yue Wang"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2602.14174"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Direction Matters: Learning Force Direction Enables Sim-to-Real Contact-Rich Manipulation

## Metadata
- Authors: Yifei Yang, Anzhe Chen, Zhenjie Zhu, Kechun Xu, Yunxuan Mao, Yufei Wei, Lu Chen, Rong Xiong, Yue Wang
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2602.14174
- Abstract source: arxiv_api

## Abstract
> Sim-to-real transfer for contact-rich manipulation remains challenging due to the inherent discrepancy in contact dynamics. While existing methods often rely on costly real-world data or utilize blind compliance through fixed controllers, we propose a framework that leverages expert-designed controller logic for transfer. Inspired by the success of privileged supervision in kinematic tasks, we employ a human-designed finite state machine based position/force controller in simulation to provide privileged guidance. The resulting policy is trained to predict the end-effector pose, contact state, and crucially the desired contact force direction. Unlike force magnitudes, which are highly sensitive to simulation inaccuracies, force directions encode high-level task geometry and remain robust across the sim-to-real gap. At deployment, these predictions configure a force-aware admittance controller. By combining the policy's directional intent with a constant, low-cost manually tuned force magnitude, the system generates adaptive, task-aligned compliance. This tuning is lightweight, typically requiring only a single scalar per contact state. We provide theoretical analysis for stability and robustness to disturbances. Experiments on four real-world tasks, i.e., microwave opening, peg-in-hole, whiteboard wiping, and door opening, demonstrate that our approach significantly outperforms strong baselines in both success rate and robustness. Videos are available at: https://yifei-y.github.io/project-pages/DirectionMatters/.

## Why It Matters
- Shifts the prediction target from brittle force magnitude to task-geometry-linked force direction, then uses the result to configure a force-aware admittance controller for robust sim-to-real transfer.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
