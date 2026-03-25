---
title: "RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation"
authors: "Yuxiang Zhou et al."
year: 2023
venue: "Transactions on Machine Learning Research"
url: "https://deepmind.google/research/publications/35829/"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation

## Metadata
- Authors: Yuxiang Zhou et al.
- Year: 2023
- Venue: Transactions on Machine Learning Research
- Primary URL: https://deepmind.google/research/publications/35829/
- Abstract source: html_meta
- Abstract matched title: RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation â Google DeepMind

## Abstract
> The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a foundation agent for robotic manipulation. This agent, named _RoboCat_, is a visual goal-conditioned decision transformer capable of consuming multi-embodiment action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100--1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## Why It Matters
- Important for showing that a foundation manipulation agent can adapt to novel tasks and embodiments with 100 to 1000 examples and can bootstrap itself with self-generated data [S11].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
