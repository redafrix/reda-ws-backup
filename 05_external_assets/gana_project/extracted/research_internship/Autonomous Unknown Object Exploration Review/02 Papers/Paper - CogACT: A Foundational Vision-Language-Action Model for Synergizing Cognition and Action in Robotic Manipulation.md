---
title: "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation"
authors: "Qixiu Li et al."
year: 2024
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2411.19650"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

## Metadata
- Authors: Qixiu Li et al.
- Year: 2024
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2411.19650
- Abstract source: arxiv_api

## Abstract
> The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low tasks success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a omponentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrates the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real work shows that our model not only significantly surpasses existing VLAs in task performance and but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA which has similar model size (7B) with ours by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## Why It Matters
- A representative diffusion-action VLA that directly tackles the weakness of quantized action heads and shows large gains on unseen objects, backgrounds, and new robots [S17].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
