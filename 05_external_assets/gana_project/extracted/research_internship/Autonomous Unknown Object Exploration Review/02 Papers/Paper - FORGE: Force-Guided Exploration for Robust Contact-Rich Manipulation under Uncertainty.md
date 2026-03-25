---
title: "FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty"
authors: "Michael Noseworthy, Bingjie Tang, Bowen Wen, Ankur Handa, Chad Kessens, Nicholas Roy, Dieter Fox, Fabio Ramos, Yashraj Narang, Iretiayo Akinola"
year: 2025
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2408.04587"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty

## Metadata
- Authors: Michael Noseworthy, Bingjie Tang, Bowen Wen, Ankur Handa, Chad Kessens, Nicholas Roy, Dieter Fox, Fabio Ramos, Yashraj Narang, Iretiayo Akinola
- Year: 2025
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2408.04587
- Abstract source: html_meta
- Abstract matched title: [2408.04587] FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty

## Abstract
> We present FORGE, a method for sim-to-real transfer of force-aware manipulation policies in the presence of significant pose uncertainty. During simulation-based policy learning, FORGE combines a force threshold mechanism with a dynamics randomization scheme to enable robust transfer of the learned policies to the real robot. At deployment, FORGE policies, conditioned on a maximum allowable force, adaptively perform contact-rich tasks while avoiding aggressive and unsafe behaviour, regardless of the controller gains. Additionally, FORGE policies predict task success, enabling efficient termination and autonomous tuning of the force threshold. We show that FORGE can be used to learn a variety of robust contact-rich policies, including the forceful insertion of snap-fit connectors. We further demonstrate the multistage assembly of a planetary gear system, which requires success across three assembly tasks: nut threading, insertion, and gear meshing. Project website can be accessed at https://noseworm.github.io/forge/.

## Why It Matters
- Brought explicit force-threshold conditioning and success prediction into sim-to-real contact-rich manipulation, enabling safer exploration of uncertain forceful interactions such as snap-fit insertion.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
