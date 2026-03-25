---
title: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models"
authors: "Open X-Embodiment Collaboration"
year: 2023
venue: "ICRA 2024"
url: "https://arxiv.org/abs/2310.08864"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Open X-Embodiment: Robotic Learning Datasets and RT-X Models

## Metadata
- Authors: Open X-Embodiment Collaboration
- Year: 2023
- Venue: ICRA 2024
- Primary URL: https://arxiv.org/abs/2310.08864
- Abstract source: arxiv_api

## Abstract
> Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## Why It Matters
- It standardized a heterogeneous real-robot data mixture across 22 robots and 527 skills, making cross-embodiment evaluation and transfer a mainstream benchmark topic [S6].
- Made cross-embodiment robot foundation-model research practical by standardizing 1M-plus trajectories from many labs and demonstrating positive transfer with RT-X models [S7].

## Mentioned In
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
