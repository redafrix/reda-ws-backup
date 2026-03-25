---
title: "CLIPort: What and Where Pathways for Robotic Manipulation"
authors: "Mohit Shridhar, Lucas Manuelli, Dieter Fox"
year: 2021
venue: "Conference on Robot Learning"
url: "https://arxiv.org/abs/2109.12098"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# CLIPort: What and Where Pathways for Robotic Manipulation

## Metadata
- Authors: Mohit Shridhar, Lucas Manuelli, Dieter Fox
- Year: 2021
- Venue: Conference on Robot Learning
- Primary URL: https://arxiv.org/abs/2109.12098
- Abstract source: arxiv_api

## Abstract
> How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP with the spatial precision (where) of Transporter . Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## Why It Matters
- A key early bridge from internet-scale vision-language pretraining into robot manipulation: it combines CLIP semantics with Transporter-style spatial precision and directly targets novel goals and object concepts [S1].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
