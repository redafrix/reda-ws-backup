---
title: "BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects"
authors: "Bowen Wen, Jonathan Tremblay, Valts Blukis, Stephen Tyree, Thomas Muller, Alex Evans, Dieter Fox, Jan Kautz, Stan Birchfield"
year: 2023
venue: "CVPR 2023"
url: "https://research.nvidia.com/publication/2023-06_bundlesdf-neural-6-dof-tracking-and-3d-reconstruction-unknown-objects"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects

## Metadata
- Authors: Bowen Wen, Jonathan Tremblay, Valts Blukis, Stephen Tyree, Thomas Muller, Alex Evans, Dieter Fox, Jan Kautz, Stan Birchfield
- Year: 2023
- Venue: CVPR 2023
- Primary URL: https://research.nvidia.com/publication/2023-06_bundlesdf-neural-6-dof-tracking-and-3d-reconstruction-unknown-objects
- Abstract source: openalex

## Abstract
> We present a near real-time (10Hz) method for 6-DoF tracking of an unknown object from a monocular RGBD video sequence, while simultaneously performing neural 3D reconstruction of the object. Our method works for arbi-trary rigid objects, even when visual texture is largely ab-sent. The object is assumed to be segmented in the first frame only. No additional information is required, and no assumption is made about the interaction agent. Key to our method is a Neural Object Field that is learned concurrently with a pose graph optimization process in order to robustly accumulate information into a consistent 3D representation capturing both geometry and appearance. A dynamic pool of posed memory frames is automatically main-tained to facilitate communication between these threads. Our approach handles challenging sequences with large pose changes, partial and full occlusion, untextured surfaces, and specular highlights. We show results on HO3D, YCBInEOAT, and BEHAVE datasets, demonstrating that our method significantly outperforms existing approaches. Project page: https://bundlesdf.github.io/

## Why It Matters
- A major step for object-centric neural fields in robotics: it couples unknown-object tracking with reconstruction from RGB-D video and provides a practical bridge from object videos to usable object meshes.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
