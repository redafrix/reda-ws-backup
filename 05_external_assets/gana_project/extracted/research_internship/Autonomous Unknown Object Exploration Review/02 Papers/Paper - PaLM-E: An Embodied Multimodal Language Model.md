---
title: "PaLM-E: An Embodied Multimodal Language Model"
authors: "Danny Driess et al."
year: 2023
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2303.03378"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# PaLM-E: An Embodied Multimodal Language Model

## Metadata
- Authors: Danny Driess et al.
- Year: 2023
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2303.03378
- Abstract source: html_meta
- Abstract matched title: [2303.03378] PaLM-E: An Embodied Multimodal Language Model

## Abstract
> Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world, e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings. We train these encodings end-to-end, in conjunction with a pre-trained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, and captioning. Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, and further, exhibits positive transfer: the model benefits from diverse joint training across internet-scale language, vision, and visual-language domains. Our largest model, PaLM-E-562B with 562B parameters, in addition to being trained on robotics tasks, is a visual-language generalist with state-of-the-art performance on OK-VQA, and retains generalist language capabilities with increasing scale.

## Why It Matters
- Introduced the embodied multimodal language-model idea: continuous robot observations can be injected into a general language model, enabling positive transfer across robotics and internet-scale multimodal tasks [S4].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
