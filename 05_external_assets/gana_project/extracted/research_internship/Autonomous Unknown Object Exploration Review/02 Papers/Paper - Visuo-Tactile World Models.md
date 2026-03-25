---
title: "Visuo-Tactile World Models"
authors: "Carolina Higuera, Sergio Arnaud, Byron Boots, Mustafa Mukadam, Francois Robert Hogan, Franziska Meier"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2602.06001"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Visuo-Tactile World Models

## Metadata
- Authors: Carolina Higuera, Sergio Arnaud, Byron Boots, Mustafa Mukadam, Francois Robert Hogan, Franziska Meier
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2602.06001
- Abstract source: html_meta
- Abstract matched title: [2602.06001] Visuo-Tactile World Models

## Abstract
> We introduce multi-task Visuo-Tactile World Models (VT-WM), which capture the physics of contact through touch reasoning. By complementing vision with tactile sensing, VT-WM better understands robot-object interactions in contact-rich tasks, avoiding common failure modes of vision-only models under occlusion or ambiguous contact states, such as objects disappearing, teleporting, or moving in ways that violate basic physics. Trained across a set of contact-rich manipulation tasks, VT-WM improves physical fidelity in imagination, achieving 33% better performance at maintaining object permanence and 29% better compliance with the laws of motion in autoregressive rollouts. Moreover, experiments show that grounding in contact dynamics also translates to planning. In zero-shot real-robot experiments, VT-WM achieves up to 35% higher success rates, with the largest gains in multi-step, contact-rich tasks. Finally, VT-WM demonstrates significant downstream versatility, effectively adapting its learned contact dynamics to a novel task and achieving reliable planning success with only a limited set of demonstrations.

## Why It Matters
- Shows how visuo-tactile fusion can be elevated from local estimation to predictive planning, with tactile grounding improving both physical fidelity and downstream real-robot success.
- Introduces multi-task visuo-tactile world models that improve physical plausibility and planning under contact, directly addressing failure modes of vision-only predictive models.

## Mentioned In
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
