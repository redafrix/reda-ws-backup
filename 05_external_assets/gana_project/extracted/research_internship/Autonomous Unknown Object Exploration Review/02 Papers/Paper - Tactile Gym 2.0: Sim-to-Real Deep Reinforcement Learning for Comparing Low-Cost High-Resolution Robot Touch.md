---
title: "Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch"
authors: "Yijiong Lin, John Lloyd, Alex Church, Nathan F. Lepora"
year: 2022
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2207.10763"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch

## Metadata
- Authors: Yijiong Lin, John Lloyd, Alex Church, Nathan F. Lepora
- Year: 2022
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2207.10763
- Abstract source: html_meta
- Abstract matched title: [2207.10763] Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch

## Abstract
> High-resolution optical tactile sensors are increasingly used in robotic learning environments due to their ability to capture large amounts of data directly relating to agent-environment interaction. However, there is a high barrier of entry to research in this area due to the high cost of tactile robot platforms, specialised simulation software, and sim-to-real methods that lack generality across different sensors. In this letter we extend the Tactile Gym simulator to include three new optical tactile sensors (TacTip, DIGIT and DigiTac) of the two most popular types, Gelsight-style (image-shading based) and TacTip-style (marker based). We demonstrate that a single sim-to-real approach can be used with these three different sensors to achieve strong real-world performance despite the significant differences between real tactile images. Additionally, we lower the barrier of entry to the proposed tasks by adapting them to an inexpensive 4-DoF robot arm, further enabling the dissemination of this benchmark. We validate the extended environment on three physically-interactive tasks requiring a sense of touch: object pushing, edge following and surface following. The results of our experimental validation highlight some differences between these sensors, which may help future researchers select and customize the physical characteristics of tactile sensors for different manipulations scenarios.

## Why It Matters
- A rare benchmark-first paper in tactile manipulation: it standardizes three tactile sensors, three physically interactive tasks, and sim-to-real comparison on accessible hardware [S1].
- Established the most reusable benchmark-style platform in this subtopic, with sim-to-real edge following and surface following across TacTip, DIGIT, and DigiTac sensors on accessible hardware.
- The main benchmark and software substrate for tactile RL in this period, covering object pushing, edge following, and surface following with sim-to-real transfer.

## Mentioned In
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation|Reinforcement learning for unknown object exploration touch and manipulation]]
