---
title: "Exploratory Tactile Servoing With Active Touch"
authors: "Nathan F. Lepora, Kirsty Aquilina, Luke P. Cramphorn"
year: 2017
venue: "IEEE Robotics and Automation Letters"
url: "https://research-information.bris.ac.uk/en/datasets/exploratory-tactile-servoing-with-active-touch/"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Exploratory Tactile Servoing With Active Touch

## Metadata
- Authors: Nathan F. Lepora, Kirsty Aquilina, Luke P. Cramphorn
- Year: 2017
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://research-information.bris.ac.uk/en/datasets/exploratory-tactile-servoing-with-active-touch/
- Abstract source: openalex

## Abstract
> A key unsolved problem in tactile robotics is how to combine tactile perception and control to interact robustly and intelligently with the surroundings. Here, we focus on a prototypical task of tactile exploration over surface features such as edges or ridges, which is a principal exploratory procedure of humans to recognize object shape. Our methods were adapted from an approach for biomimetic active touch that perceives stimulus location and identity while controlling location to aid perception. With minor modification to the control policy, to rotate the sensor to maintain a relative orientation and move tangentially (tactile servoing), the method applies also to tactile exploration. Robust exploratory tactile servoing is then attained over various two-dimensional objects, ranging from the edge of a circular disk, a volute laminar, and circular or spiral ridges. Conceptually, the approach brings together active perception and haptic exploration as instantiations of a common active touch algorithm, and has potential to generalize to more complex tasks requiring the flexibility and robustness of human touch.

## Why It Matters
- A key precursor for modern closed-loop contact control: tactile sensing is not just perception but a driver of motion, which later multimodal pipelines extend with vision and force information.
- Establishes the action-perception loop for tactile exploration and strongly influences later tactile RL benchmarks for contour and surface following.
- Establishes the idea that tactile perception and control should be closed in the loop so the robot actively moves to maintain and improve contact information.

## Mentioned In
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
- [[Subtopic - Tactile-guided reaching contact localization and active haptic exploration of unknown objects|Tactile-guided reaching contact localization and active haptic exploration of unknown objects]]
