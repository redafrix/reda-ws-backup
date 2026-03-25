---
title: "ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation"
authors: "Yang Li, Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, Yunsong Zhou, Jia Zeng, Ce Hao, Jieji Ren, Qiaojun Yu, Cewu Lu, Yu Qiao, Jiangmiao Pang"
year: 2026
venue: "CVPR 2026 / arXiv preprint"
url: "https://arxiv.org/abs/2603.15169"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

## Metadata
- Authors: Yang Li, Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, Yunsong Zhou, Jia Zeng, Ce Hao, Jieji Ren, Qiaojun Yu, Cewu Lu, Yu Qiao, Jiangmiao Pang
- Year: 2026
- Venue: CVPR 2026 / arXiv preprint
- Primary URL: https://arxiv.org/abs/2603.15169
- Abstract source: html_meta
- Abstract matched title: [2603.15169] ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

## Abstract
> Embodied intelligence for contact-rich manipulation has predominantly relied on position control, while explicit awareness and regulation of interaction forces remain under-explored, limiting stability, precision, and robustness in real-world tasks. We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness. ForceVLA2 introduces force-based prompts into the VLM expert to construct force-aware task concepts across stages, and employs a Cross-Scale Mixture-of-Experts (MoE) in the action expert to adaptively fuse these concepts with real-time interaction forces for closed-loop hybrid force-position regulation. To support learning and evaluation, we construct ForceVLA2-Dataset, containing 1,000 trajectories over 5 contact-rich tasks, including wiping, pressing, and assembling, with multi-view images, task prompts, proprioceptive state, and force signals. Extensive experiments show that ForceVLA2 substantially improves success rates and reliability in contact-rich manipulation, outperforming pi0 and pi0.5 by 48.0% and 35.0%, respectively, across the 5 tasks, and mitigating common failure modes such as arm overload and unstable contact, thereby actively advancing force-aware interactive physical intelligence in VLAs. The project page is available at https://sites.google.com/view/force-vla2/home.

## Why It Matters
- Adds an explicitly force-aware evaluation dataset and benchmark protocol for five contact-rich tasks, which is important because most VLA benchmarks still under-measure physical interaction quality [S11].
- Represents the strongest early-2026 move toward force-aware VLA systems, combining force prompts, multimodal fusion, hybrid control outputs, and a new dataset over five real contact-rich tasks.
- Pushes the force-aware VLA line toward full hybrid force-position outputs and reports strong average gains across five real contact-rich tasks, making it a directly relevant 2026 continuation of ForceVLA.

## Mentioned In
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
