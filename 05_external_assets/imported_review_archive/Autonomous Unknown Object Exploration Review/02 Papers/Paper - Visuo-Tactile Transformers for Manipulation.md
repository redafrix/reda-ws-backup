---
title: "Visuo-Tactile Transformers for Manipulation"
authors: "Yizhou Chen, Andrea Sipos, Mark Van der Merwe, Nima Fazeli"
year: 2022
venue: "CoRL 2022"
url: "https://arxiv.org/abs/2210.00121"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Visuo-Tactile Transformers for Manipulation

## Metadata
- Authors: Yizhou Chen, Andrea Sipos, Mark Van der Merwe, Nima Fazeli
- Year: 2022
- Venue: CoRL 2022
- Primary URL: https://arxiv.org/abs/2210.00121
- Abstract source: html_meta
- Abstract matched title: [2210.00121] Visuo-Tactile Transformers for Manipulation

## Abstract
> Learning representations in the joint domain of vision and touch can improve manipulation dexterity, robustness, and sample-complexity by exploiting mutual information and complementary cues. Here, we present Visuo-Tactile Transformers (VTTs), a novel multimodal representation learning approach suited for model-based reinforcement learning and planning. Our approach extends the Visual Transformer \cite{dosovitskiy2021image} to handle visuo-tactile feedback. Specifically, VTT uses tactile feedback together with self and cross-modal attention to build latent heatmap representations that focus attention on important task features in the visual domain. We demonstrate the efficacy of VTT for representation learning with a comparative evaluation against baselines on four simulated robot tasks and one real world block pushing task. We conduct an ablation study over the components of VTT to highlight the importance of cross-modality in representation learning.

## Why It Matters
- Represents the model-based RL branch: it learns multimodal latents for planning and helps establish visuo-tactile representation learning as part of RL policy design.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
