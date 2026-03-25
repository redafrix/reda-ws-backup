---
title: "Manipulation by Feel: Touch-Based Control with Deep Predictive Models"
authors: "Stephen Tian, Frederik Ebert, Dinesh Jayaraman, Mayur Mudigonda, Chelsea Finn, Roberto Calandra, Sergey Levine"
year: 2019
venue: "ICRA 2019"
url: "https://arxiv.org/abs/1903.04128"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Manipulation by Feel: Touch-Based Control with Deep Predictive Models

## Metadata
- Authors: Stephen Tian, Frederik Ebert, Dinesh Jayaraman, Mayur Mudigonda, Chelsea Finn, Roberto Calandra, Sergey Levine
- Year: 2019
- Venue: ICRA 2019
- Primary URL: https://arxiv.org/abs/1903.04128
- Abstract source: html_meta
- Abstract matched title: [1903.04128] Manipulation by Feel: Touch-Based Control with Deep Predictive Models

## Abstract
> Touch sensing is widely acknowledged to be important for dexterous robotic manipulation, but exploiting tactile sensing for continuous, non-prehensile manipulation is challenging. General purpose control techniques that are able to effectively leverage tactile sensing as well as accurate physics models of contacts and forces remain largely elusive, and it is unclear how to even specify a desired behavior in terms of tactile percepts. In this paper, we take a step towards addressing these issues by combining high-resolution tactile sensing with data-driven modeling using deep neural network dynamics models. We propose deep tactile MPC, a framework for learning to perform tactile servoing from raw tactile sensor inputs, without manual supervision. We show that this method enables a robot equipped with a GelSight-style tactile sensor to manipulate a ball, analog stick, and 20-sided die, learning from unsupervised autonomous interaction and then using the learned tactile predictive model to reposition each object to user-specified configurations, indicated by a goal tactile reading. Videos, visualizations and the code are available here: https://sites.google.com/view/deeptactilempc

## Why It Matters
- A key model-based precursor that learns tactile dynamics and uses tactile MPC, directly anticipating later model-based tactile RL and world-model work.

## Mentioned In
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
