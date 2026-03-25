---
title: "Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing"
authors: "Max Yang, Yijiong Lin, Alex Church, John Lloyd, Dandan Zhang, David A. W. Barton, Nathan F. Lepora"
year: 2023
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2307.14272"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing

## Metadata
- Authors: Max Yang, Yijiong Lin, Alex Church, John Lloyd, Dandan Zhang, David A. W. Barton, Nathan F. Lepora
- Year: 2023
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2307.14272
- Abstract source: html_meta
- Abstract matched title: [2307.14272] Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing

## Abstract
> Object pushing presents a key non-prehensile manipulation problem that is illustrative of more complex robotic manipulation tasks. While deep reinforcement learning (RL) methods have demonstrated impressive learning capabilities using visual input, a lack of tactile sensing limits their capability for fine and reliable control during manipulation. Here we propose a deep RL approach to object pushing using tactile sensing without visual input, namely tactile pushing. We present a goal-conditioned formulation that allows both model-free and model-based RL to obtain accurate policies for pushing an object to a goal. To achieve real-world performance, we adopt a sim-to-real approach. Our results demonstrate that it is possible to train on a single object and a limited sample of goals to produce precise and reliable policies that can generalize to a variety of unseen objects and pushing scenarios without domain randomization. We experiment with the trained agents in harsh pushing conditions, and show that with significantly more training samples, a model-free policy can outperform a model-based planner, generating shorter and more reliable pushing trajectories despite large disturbances. The simplicity of our training environment and effective real-world performance highlights the value of rich tactile information for fine manipulation. Code and videos are available at https://sites.google.com/view/tactile-rl-pushing/.

## Why It Matters
- Provides a rare direct comparison between model-based and model-free tactile RL while demonstrating generalization to unseen objects and pushing scenarios without domain randomization.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
