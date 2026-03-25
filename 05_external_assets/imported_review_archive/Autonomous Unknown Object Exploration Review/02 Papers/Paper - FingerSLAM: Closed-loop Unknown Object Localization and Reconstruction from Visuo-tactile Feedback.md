---
title: "FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback"
authors: "Jialiang Zhao, Maria Bauza, Edward H. Adelson"
year: 2023
venue: "ICRA 2023"
url: "https://arxiv.org/abs/2303.07997"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback

## Metadata
- Authors: Jialiang Zhao, Maria Bauza, Edward H. Adelson
- Year: 2023
- Venue: ICRA 2023
- Primary URL: https://arxiv.org/abs/2303.07997
- Abstract source: html_meta
- Abstract matched title: [2303.07997] FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback

## Abstract
> In this paper, we address the problem of using visuo-tactile feedback for 6-DoF localization and 3D reconstruction of unknown in-hand objects. We propose FingerSLAM, a closed-loop factor graph-based pose estimator that combines local tactile sensing at finger-tip and global vision sensing from a wrist-mount camera. FingerSLAM is constructed with two constituent pose estimators: a multi-pass refined tactile-based pose estimator that captures movements from detailed local textures, and a single-pass vision-based pose estimator that predicts from a global view of the object. We also design a loop closure mechanism that actively matches current vision and tactile images to previously stored key-frames to reduce accumulated error. FingerSLAM incorporates the two sensing modalities of tactile and vision, as well as the loop closure mechanism with a factor graph-based optimization framework. Such a framework produces an optimized pose estimation solution that is more accurate than the standalone estimators. The estimated poses are then used to reconstruct the shape of the unknown object incrementally by stitching the local point clouds recovered from tactile images. We train our system on real-world data collected with 20 objects. We demonstrate reliable visuo-tactile pose estimation and shape reconstruction through quantitative and qualitative real-world evaluations on 6 objects that are unseen during training.

## Why It Matters
- One of the clearest demonstrations that a wrist camera plus fingertip tactile sensing can jointly localize and reconstruct unknown in-hand objects in a closed loop.
- One of the clearest SLAM-style formulations in this subtopic, fusing wrist vision and fingertip touch for 6-DoF localization and reconstruction of unseen in-hand objects.
- A representative visuo-tactile pose-graph system for unseen in-hand objects, combining fingertip tactile sensing, vision, loop closure, and incremental reconstruction.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
- [[Subtopic - Tactile-guided reaching contact localization and active haptic exploration of unknown objects|Tactile-guided reaching contact localization and active haptic exploration of unknown objects]]
