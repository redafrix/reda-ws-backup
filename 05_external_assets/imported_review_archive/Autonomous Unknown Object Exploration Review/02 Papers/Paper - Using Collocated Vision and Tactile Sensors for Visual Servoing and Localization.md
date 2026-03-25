---
title: "Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization"
authors: "Arkadeep Narayan Chaudhury, Timothy Man, Wenzhen Yuan, Christopher G. Atkeson"
year: 2022
venue: "IEEE Robotics and Automation Letters"
url: "https://arxiv.org/abs/2204.11686"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization

## Metadata
- Authors: Arkadeep Narayan Chaudhury, Timothy Man, Wenzhen Yuan, Christopher G. Atkeson
- Year: 2022
- Venue: IEEE Robotics and Automation Letters
- Primary URL: https://arxiv.org/abs/2204.11686
- Abstract source: html_meta
- Abstract matched title: [2204.11686] Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization

## Abstract
> Coordinating proximity and tactile imaging by collocating cameras with tactile sensors can 1) provide useful information before contact such as object pose estimates and visually servo a robot to a target with reduced occlusion and higher resolution compared to head-mounted or external depth cameras, 2) simplify the contact point and pose estimation problems and help tactile sensing avoid erroneous matches when a surface does not have significant texture or has repetitive texture with many possible matches, and 3) use tactile imaging to further refine contact point and object pose estimation. We demonstrate our results with objects that have more surface texture than most objects in standard manipulation datasets. We learn that optic flow needs to be integrated over a substantial amount of camera travel to be useful in predicting movement direction. Most importantly, we also learn that state of the art vision algorithms do not do a good job localizing tactile images on object models, unless a reasonable prior can be provided from collocated cameras.

## Why It Matters
- A canonical pre-contact and post-contact fusion paper: collocated cameras give better priors for servoing and tactile localization, showing why camera-touch geometry should be designed together.

## Mentioned In
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
