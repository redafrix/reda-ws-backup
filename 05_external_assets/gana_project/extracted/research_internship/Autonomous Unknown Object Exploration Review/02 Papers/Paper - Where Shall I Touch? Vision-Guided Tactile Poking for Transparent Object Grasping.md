---
title: "Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping"
authors: "Jiaqi Jiang, Guanqun Cao, Aaron Butterworth, Thanh-Toan Do, Shan Luo"
year: 2022
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2208.09743"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping

## Metadata
- Authors: Jiaqi Jiang, Guanqun Cao, Aaron Butterworth, Thanh-Toan Do, Shan Luo
- Year: 2022
- Venue: arXiv preprint
- Primary URL: https://arxiv.org/abs/2208.09743
- Abstract source: html_meta
- Abstract matched title: [2208.09743] Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping

## Abstract
> Picking up transparent objects is still a challenging task for robots. The visual properties of transparent objects such as reflection and refraction make the current grasping methods that rely on camera sensing fail to detect and localise them. However, humans can handle the transparent object well by first observing its coarse profile and then poking an area of interest to get a fine profile for grasping. Inspired by this, we propose a novel framework of vision-guided tactile poking for transparent objects grasping. In the proposed framework, a segmentation network is first used to predict the horizontal upper regions named as poking regions, where the robot can poke the object to obtain a good tactile reading while leading to minimal disturbance to the object's state. A poke is then performed with a high-resolution GelSight tactile sensor. Given the local profiles improved with the tactile reading, a heuristic grasp is planned for grasping the transparent object. To mitigate the limitations of real-world data collection and labelling for transparent objects, a large-scale realistic synthetic dataset was constructed. Extensive experiments demonstrate that our proposed segmentation network can predict the potential poking region with a high mean Average Precision (mAP) of 0.360, and the vision-guided tactile poking can enhance the grasping success rate significantly from 38.9% to 85.2%. Thanks to its simplicity, our proposed approach could also be adopted by other force or tactile sensors and could be used for grasping of other challenging objects. All the materials used in this paper are available at https://sites.google.com/view/tactilepoking.

## Why It Matters
- Shows an especially clear multimodal use case: vision proposes a safe poke region on a hard-to-see transparent object, and tactile sensing provides the local geometry needed for successful grasping.

## Mentioned In
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
