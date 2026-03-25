---
title: "Visuo-Haptic Grasping of Unknown Objects based on Gaussian Process Implicit Surfaces and Deep Learning"
authors: "Simon Ottenhaus, Daniel Renninghoff, Raphael Grimm, Fabio Ferreira, Tamim Asfour"
year: 2019
venue: "Humanoids 2019"
url: "https://h2t.iar.kit.edu/pdf/Ottenhaus2019.pdf"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Visuo-Haptic Grasping of Unknown Objects based on Gaussian Process Implicit Surfaces and Deep Learning

## Metadata
- Authors: Simon Ottenhaus, Daniel Renninghoff, Raphael Grimm, Fabio Ferreira, Tamim Asfour
- Year: 2019
- Venue: Humanoids 2019
- Primary URL: https://h2t.iar.kit.edu/pdf/Ottenhaus2019.pdf
- Abstract source: openalex

## Abstract
> Grasping unknown objects is a challenging task for humanoid robots, as planning and execution have to cope with noisy sensor data. This work presents a framework, which integrates sensing, planning and acting in one visuo-haptic grasping pipeline. Visual and tactile perception are fused using Gaussian Process Implicit Surfaces to estimate the object surface. Two grasp planners then generate grasp candidates, which are used to train a neural network to determine the best grasp. The main contribution of this work is the introduction of a discriminative deep neural network for scoring grasp hypotheses for underactuated humanoid hands. The pipeline delivers full 6D grasp poses for multi-fingered humanoid hands but it is not limited to any specific gripper. The pipeline is trained and evaluated in simulation, based on objects from the YCB and KIT object sets, resulting in a 95 % success rate regarding force-closure. To prove the validity of the proposed approach, the pipeline is executed on the humanoid robot ARMAR-6 in experiments with eight non-trivial objects using an underactuated five finger hand.

## Why It Matters
- A direct precursor for later unknown-object visuo-haptic pipelines: it fuses visual and tactile exploration into a grasp-selection loop for previously unseen objects.

## Mentioned In
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
