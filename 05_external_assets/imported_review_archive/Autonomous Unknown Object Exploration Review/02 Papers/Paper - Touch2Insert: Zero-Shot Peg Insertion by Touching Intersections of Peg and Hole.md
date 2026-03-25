---
title: "Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole"
authors: "Masaru Yajima, Yuma Shin, Rei Kawakami, Asako Kanezaki, Kei Ota"
year: 2026
venue: "ICRA 2026"
url: "https://arxiv.org/abs/2603.03627"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole

## Metadata
- Authors: Masaru Yajima, Yuma Shin, Rei Kawakami, Asako Kanezaki, Kei Ota
- Year: 2026
- Venue: ICRA 2026
- Primary URL: https://arxiv.org/abs/2603.03627
- Abstract source: html_meta
- Abstract matched title: [2603.03627] Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole

## Abstract
> Reliable insertion of industrial connectors remains a central challenge in robotics, requiring sub-millimeter precision under uncertainty and often without full visual access. Vision-based approaches struggle with occlusion and limited generalization, while learning-based policies frequently fail to transfer to unseen geometries. To address these limitations, we leverage tactile sensing, which captures local surface geometry at the point of contact and thus provides reliable information even under occlusion and across novel connector shapes. Building on this capability, we present \emph{Touch2Insert}, a tactile-based framework for arbitrary peg insertion. Our method reconstructs cross-sectional geometry from high-resolution tactile images and estimates the relative pose of the hole with respect to the peg in a zero-shot manner. By aligning reconstructed shapes through registration, the framework enables insertion from a single contact without task-specific training. To evaluate its performance, we conducted experiments with three diverse connectors in both simulation and real-robot settings. The results indicate that Touch2Insert achieved sub-millimeter pose estimation accuracy for all connectors in simulation, and attained an average success rate of 86.7\% on the real robot, thereby confirming the robustness and generalizability of tactile sensing for real-world robotic connector insertion.

## Why It Matters
- A direct tactile-guided reaching result: one tactile contact is used to reconstruct local cross-sections, estimate relative pose in zero shot, and execute insertion on unseen connectors.
- Shows a concrete transition from tactile localization to controlled reaching: a single tactile interaction estimates relative peg-hole pose on unseen connector geometries.

## Mentioned In
- [[Subtopic - Tactile-guided reaching contact localization and active haptic exploration of unknown objects|Tactile-guided reaching contact localization and active haptic exploration of unknown objects]]
