---
title: "See to Touch: Learning Tactile Dexterity through Visual Incentives"
authors: "Irmak Guzey, Yinlong Dai, Ben Evans, Soumith Chintala, Lerrel Pinto"
year: 2023
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2309.12300"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# See to Touch: Learning Tactile Dexterity through Visual Incentives

## Metadata
- Authors: Irmak Guzey, Yinlong Dai, Ben Evans, Soumith Chintala, Lerrel Pinto
- Year: 2023
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2309.12300
- Abstract source: html_meta
- Abstract matched title: [2309.12300] See to Touch: Learning Tactile Dexterity through Visual Incentives

## Abstract
> Equipping multi-fingered robots with tactile sensing is crucial for achieving the precise, contact-rich, and dexterous manipulation that humans excel at. However, relying solely on tactile sensing fails to provide adequate cues for reasoning about objects' spatial configurations, limiting the ability to correct errors and adapt to changing situations. In this paper, we present Tactile Adaptation from Visual Incentives (TAVI), a new framework that enhances tactile-based dexterity by optimizing dexterous policies using vision-based rewards. First, we use a contrastive-based objective to learn visual representations. Next, we construct a reward function using these visual representations through optimal-transport based matching on one human demonstration. Finally, we use online reinforcement learning on our robot to optimize tactile-based policies that maximize the visual reward. On six challenging tasks, such as peg pick-and-place, unstacking bowls, and flipping slender objects, TAVI achieves a success rate of 73% using our four-fingered Allegro robot hand. The increase in performance is 108% higher than policies using tactile and vision-based rewards and 135% higher than policies without tactile observational input. Robot videos are best viewed on our project website: https://see-to-touch.github.io/.

## Why It Matters
- Shows that online RL with visually derived rewards can train tactile dexterity directly on a real robot across multiple contact-rich tasks.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
