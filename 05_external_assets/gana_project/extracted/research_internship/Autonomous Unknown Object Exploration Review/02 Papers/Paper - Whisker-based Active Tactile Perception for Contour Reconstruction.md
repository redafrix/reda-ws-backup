---
title: "Whisker-based Active Tactile Perception for Contour Reconstruction"
authors: "Yixuan Dang, Qinyang Xu, Yu Zhang, Xiangtong Yao, Liding Zhang, Zhenshan Bing, Florian Roehrbein, Alois Knoll"
year: 2025
venue: "Preprint"
url: "https://arxiv.org/abs/2507.23305"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Whisker-based Active Tactile Perception for Contour Reconstruction

## Metadata
- Authors: Yixuan Dang, Qinyang Xu, Yu Zhang, Xiangtong Yao, Liding Zhang, Zhenshan Bing, Florian Roehrbein, Alois Knoll
- Year: 2025
- Venue: Preprint
- Primary URL: https://arxiv.org/abs/2507.23305
- Abstract source: html_meta
- Abstract matched title: [2507.23305] Whisker-based Active Tactile Perception for Contour Reconstruction

## Abstract
> Perception using whisker-inspired tactile sensors currently faces a major challenge: the lack of active control in robots based on direct contact information from the whisker. To accurately reconstruct object contours, it is crucial for the whisker sensor to continuously follow and maintain an appropriate relative touch pose on the surface. This is especially important for localization based on tip contact, which has a low tolerance for sharp surfaces and must avoid slipping into tangential contact. In this paper, we first construct a magnetically transduced whisker sensor featuring a compact and robust suspension system composed of three flexible spiral arms. We develop a method that leverages a characterized whisker deflection profile to directly extract the tip contact position using gradient descent, with a Bayesian filter applied to reduce fluctuations. We then propose an active motion control policy to maintain the optimal relative pose of the whisker sensor against the object surface. A B-Spline curve is employed to predict the local surface curvature and determine the sensor orientation. Results demonstrate that our algorithm can effectively track objects and reconstruct contours with sub-millimeter accuracy. Finally, we validate the method in simulations and real-world experiments where a robot arm drives the whisker sensor to follow the surfaces of three different objects.

## Why It Matters
- Demonstrates a lightweight active-touch route to contour following, with a dedicated contact-localization pipeline and active pose regulation for sub-millimeter contour reconstruction.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
