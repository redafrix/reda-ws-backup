---
title: "Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing"
authors: "Marina Y. Aoyama, Sethu Vijayakumar, Tetsuya Narita"
year: 2025
venue: "IEEE Robotics and Automation Letters"
url: "https://sony.github.io/tool-use-few-shot-transfer/"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing

## Metadata
- Authors: Marina Y. Aoyama, Sethu Vijayakumar, Tetsuya Narita
- Year: 2025
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://sony.github.io/tool-use-few-shot-transfer/
- Abstract source: html_body

## Abstract
> Tools extend the manipulation abilities of robots, much like they do for humans. Despite human expertise in tool manipulation, teaching robots these skills faces challenges. The complexity arises from the interplay of two points of contact: one between the robot and the tool, and another between the tool and the environment. Tactile and proximity sensors play a crucial role in identifying these complex contacts. However, learning tool manipulation with a small amount of real-world data using these sensors remains challenging due to the large sim-to-real gap and sensor noise. To address this, we propose a few-shot tool-use skill transfer framework using multimodal sensing. The framework involves pre-training the base policy to capture contact states common in tool-use skills in simulation and fine-tuning it with human demonstrations collected in the real-world target domain to bridge the domain gap. We validate that this framework enables teaching surface-following tasks using tools with diverse physical and geometric properties with a small number of demonstrations on the Franka Emika robot arm. Our analysis suggests that the robot acquires new tool-use skills by transferring the ability to recognise tool-environment contact relationships from pre-trained to fine-tuned policies. Additionally, integrating proximity and tactile sensors enhances the identification of contact states and environmental geometry.

## Why It Matters
- Shows that tool-mediated surface following can generalize across tools with only a few human demonstrations when multimodal contact-state sensing is combined with sim pre-training.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
