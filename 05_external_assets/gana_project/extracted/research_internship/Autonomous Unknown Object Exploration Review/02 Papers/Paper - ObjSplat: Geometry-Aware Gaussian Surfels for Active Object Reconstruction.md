---
title: "ObjSplat: Geometry-Aware Gaussian Surfels for Active Object Reconstruction"
authors: "Yuetao Li, Zhizhou Jia, Yu Zhang, Qun Hao, Shaohui Zhang"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2601.06997"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# ObjSplat: Geometry-Aware Gaussian Surfels for Active Object Reconstruction

## Metadata
- Authors: Yuetao Li, Zhizhou Jia, Yu Zhang, Qun Hao, Shaohui Zhang
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2601.06997
- Abstract source: html_meta
- Abstract matched title: [2601.06997] ObjSplat: Geometry-Aware Gaussian Surfels for Active Object Reconstruction

## Abstract
> Autonomous high-fidelity object reconstruction is fundamental for creating digital assets and bridging the simulation-to-reality gap in robotics. We present ObjSplat, an active reconstruction framework that leverages Gaussian surfels as a unified representation to progressively reconstruct unknown objects with both photorealistic appearance and accurate geometry. Addressing the limitations of conventional opacity or depth-based cues, we introduce a geometry-aware viewpoint evaluation pipeline that explicitly models back-face visibility and occlusion-aware multi-view covisibility, reliably identifying under-reconstructed regions even on geometrically complex objects. Furthermore, to overcome the limitations of greedy planning strategies, ObjSplat employs a next-best-path (NBP) planner that performs multi-step lookahead on a dynamically constructed spatial graph. By jointly optimizing information gain and movement cost, this planner generates globally efficient trajectories. Extensive experiments in simulation and on real-world cultural artifacts demonstrate that ObjSplat produces physically consistent models within minutes, achieving superior reconstruction fidelity and surface completeness while significantly reducing scan time and path length compared to state-of-the-art approaches. Project page: https://li-yuetao.github.io/ObjSplat-page/ .

## Why It Matters
- A very recent signal that active robotic reconstruction is moving toward geometry-aware Gaussian object models and multi-step next-best-path planning, which could be attractive for future manipulator-mounted scanners because Gaussian rendering is faster than classic NeRF training.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
