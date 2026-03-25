---
title: "Octo: An Open-Source Generalist Robot Policy"
authors: "Octo Model Team et al."
year: 2024
venue: "Robotics: Science and Systems"
url: "https://arxiv.org/abs/2405.12213"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Octo: An Open-Source Generalist Robot Policy

## Metadata
- Authors: Octo Model Team et al.
- Year: 2024
- Venue: Robotics: Science and Systems
- Primary URL: https://arxiv.org/abs/2405.12213
- Abstract source: arxiv_api

## Abstract
> Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs. In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces. We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## Why It Matters
- A widely used open baseline for generalist manipulation: it proved that Open-X-scale pretraining could be packaged into a practical open-source policy that adapts to new setups within hours [S12].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
