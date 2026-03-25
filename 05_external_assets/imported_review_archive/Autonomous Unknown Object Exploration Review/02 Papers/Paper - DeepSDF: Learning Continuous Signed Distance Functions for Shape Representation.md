---
title: "DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation"
authors: "Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, Steven Lovegrove"
year: 2019
venue: "CVPR 2019"
url: "https://arxiv.org/abs/1901.05103"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation

## Metadata
- Authors: Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, Steven Lovegrove
- Year: 2019
- Venue: CVPR 2019
- Primary URL: https://arxiv.org/abs/1901.05103
- Abstract source: arxiv_api

## Abstract
> Computer graphics, 3D computer vision and robotics communities have produced multiple approaches to representing 3D geometry for rendering and reconstruction. These provide trade-offs across fidelity, efficiency and compression capabilities. In this work, we introduce DeepSDF, a learned continuous Signed Distance Function (SDF) representation of a class of shapes that enables high quality shape representation, interpolation and completion from partial and noisy 3D input data. DeepSDF, like its classical counterpart, represents a shape's surface by a continuous volumetric field: the magnitude of a point in the field represents the distance to the surface boundary and the sign indicates whether the region is inside (-) or outside (+) of the shape, hence our representation implicitly encodes a shape's boundary as the zero-level-set of the learned function while explicitly representing the classification of space as being part of the shapes interior or not. While classical SDF's both in analytical or discretized voxel form typically represent the surface of a single shape, DeepSDF can represent an entire class of shapes. Furthermore, we show state-of-the-art performance for learned 3D shape representation and completion while reducing the model size by an order of magnitude compared with previous work.

## Why It Matters
- Provided the continuous signed-distance representation later adapted by tactile and robotic object-centric mapping papers such as TouchSDF and several neural field approaches.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
