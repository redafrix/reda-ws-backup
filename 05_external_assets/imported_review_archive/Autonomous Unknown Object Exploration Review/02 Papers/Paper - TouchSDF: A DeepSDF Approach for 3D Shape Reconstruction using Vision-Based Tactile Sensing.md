---
title: "TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing"
authors: "Mauro Comi, Yijiong Lin, Alex Church, Alessio Tonioni, Laurence Aitchison, Nathan F. Lepora"
year: 2023
venue: "Touch Processing Workshop 2023 / arXiv"
url: "https://arxiv.org/abs/2311.12602"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing

## Metadata
- Authors: Mauro Comi, Yijiong Lin, Alex Church, Alessio Tonioni, Laurence Aitchison, Nathan F. Lepora
- Year: 2023
- Venue: Touch Processing Workshop 2023 / arXiv
- Primary URL: https://arxiv.org/abs/2311.12602
- Abstract source: html_meta
- Abstract matched title: [2311.12602] TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing

## Abstract
> Humans rely on their visual and tactile senses to develop a comprehensive 3D understanding of their physical environment. Recently, there has been a growing interest in exploring and manipulating objects using data-driven approaches that utilise high-resolution vision-based tactile sensors. However, 3D shape reconstruction using tactile sensing has lagged behind visual shape reconstruction because of limitations in existing techniques, including the inability to generalise over unseen shapes, the absence of real-world testing, and limited expressive capacity imposed by discrete representations. To address these challenges, we propose TouchSDF, a Deep Learning approach for tactile 3D shape reconstruction that leverages the rich information provided by a vision-based tactile sensor and the expressivity of the implicit neural representation DeepSDF. Our technique consists of two components: (1) a Convolutional Neural Network that maps tactile images into local meshes representing the surface at the touch location, and (2) an implicit neural function that predicts a signed distance function to extract the desired 3D shape. This combination allows TouchSDF to reconstruct smooth and continuous 3D shapes from tactile inputs in simulation and real-world settings, opening up research avenues for robust 3D-aware representations and improved multimodal perception in robotics. Code and supplementary material are available at: https://touchsdf.github.io/

## Why It Matters
- A clear example of bringing continuous SDF representations into tactile robotics, using local touch-derived point clouds to infer a global object shape.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
