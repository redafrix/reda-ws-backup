---
title: "OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation"
authors: "Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2603.19201"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation

## Metadata
- Authors: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding
- Year: 2026
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2603.19201
- Abstract source: html_meta
- Abstract matched title: [2603.19201] OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation

## Abstract
> Contact-rich manipulation tasks, such as wiping and assembly, require accurate perception of contact forces, friction changes, and state transitions that cannot be reliably inferred from vision alone. Despite growing interest in visuo-tactile manipulation, progress is constrained by two persistent limitations: existing datasets are small in scale and narrow in task coverage, and current methods treat tactile signals as passive observations rather than using them to model contact dynamics or enable closed-loop control explicitly. In this paper, we present \textbf{OmniViTac}, a large-scale visuo-tactile-action dataset comprising $21{,}000+$ trajectories across $86$ tasks and $100+$ objects, organized into six physics-grounded interaction patterns. Building on this dataset, we propose \textbf{OmniVTA}, a world-model-based visuo-tactile manipulation framework that integrates four tightly coupled modules: a self-supervised tactile encoder, a two-stream visuo-tactile world model for predicting short-horizon contact evolution, a contact-aware fusion policy for action generation, and a 60Hz reflexive controller that corrects deviations between predicted and observed tactile signals in a closed loop. Real-robot experiments across all six interaction categories show that OmniVTA outperforms existing methods and generalizes well to unseen objects and geometric configurations, confirming the value of combining predictive contact modeling with high-frequency tactile feedback for contact-rich manipulation. All data, models, and code will be made publicly available on the project website at https://mrsecant.github.io/OmniVTA.

## Why It Matters
- Combines large-scale visuo-tactile data, predictive contact modeling, a contact-aware policy, and a reflexive tactile controller, making it one of the strongest 2026 end-to-end multimodal systems in scope.
- Extends the world-model direction with a much larger visuo-tactile-action dataset and an explicit 60 Hz reflexive tactile correction loop, while reporting generalization to unseen objects and geometries.
- A major step toward world-model-based visuo-tactile control, pairing a large dataset with predictive contact modeling and reflexive closed-loop correction.
- Represents the world-model branch of the field and expands benchmark scale with a large visuo-tactile-action dataset spanning many contact-rich tasks.

## Mentioned In
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
