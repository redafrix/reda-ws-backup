---
title: "Transporter Networks: Rearranging the Visual World for Robotic Manipulation"
authors: "Andy Zeng et al."
year: 2020
venue: "Conference on Robot Learning"
url: "https://arxiv.org/abs/2010.14406"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Transporter Networks: Rearranging the Visual World for Robotic Manipulation

## Metadata
- Authors: Andy Zeng et al.
- Year: 2020
- Venue: Conference on Robot Learning
- Primary URL: https://arxiv.org/abs/2010.14406
- Abstract source: arxiv_api

## Abstract
> Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## Why It Matters
- Transporter Networks supplied the spatial-manipulation backbone later reused by CLIPort and influenced the broader idea that robust visual correspondence is critical for unseen-object manipulation [S26].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
