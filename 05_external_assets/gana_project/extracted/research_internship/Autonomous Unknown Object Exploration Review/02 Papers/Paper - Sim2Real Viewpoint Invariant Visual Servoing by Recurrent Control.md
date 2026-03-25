---
title: "Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control"
authors: "Fereshteh Sadeghi, Alexander Toshev, Eric Jang, Sergey Levine"
year: 2018
venue: "CVPR 2018"
url: "https://research.google/pubs/sim2real-viewpoint-invariant-visual-servoing-by-recurrent-control/"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control

## Metadata
- Authors: Fereshteh Sadeghi, Alexander Toshev, Eric Jang, Sergey Levine
- Year: 2018
- Venue: CVPR 2018
- Primary URL: https://research.google/pubs/sim2real-viewpoint-invariant-visual-servoing-by-recurrent-control/
- Abstract source: html_body

## Abstract
> Humans are remarkably proficient at controlling their limbs and tools from a wide range of viewpoints. In robotics, this ability is referred to as visual servoing: moving a tool or end-point to a desired location using primarily visual feedback. In this paper, we propose learning viewpoint invariant visual servoing skills in a robot manipulation task. We train a deep recurrent controller that can automatically determine which actions move the end-effector of a robotic arm to a desired object. This problem is fundamentally ambiguous: under severe variation in viewpoint, it may be impossible to determine the actions in a single feedforward operation. Instead, our visual servoing approach uses its memory of past movements to understand how the actions affect the robot motion from the current viewpoint, correcting mistakes and gradually moving closer to the target. This ability is in stark contrast to previous visual servoing methods, which assume known dynamics or require a calibration phase. We learn our recurrent controller using simulated data, synthetic demonstrations and reinforcement learning. We then describe how the resulting model can be transferred to a real-world robot by disentangling perception from control and only adapting the visual layers. The adapted model can servo to previously unseen objects from novel viewpoints on a real-world Kuka IIWA robotic arm. For supplementary videos, see: \href{https://www.youtube.com/watch?v=oLgM2Bnb7fo}{https://www.youtube.com/watch?v=oLgM2Bnb7fo}

## Why It Matters
- Important for the approach/reach branch: it showed servoing to previously unseen objects from novel viewpoints without classical calibration-heavy visual servoing [S19].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
