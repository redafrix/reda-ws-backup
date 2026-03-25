---
title: "Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation"
authors: "Sudharshan Suresh, Tzu-Yu Chiu, Ivan F. Garcia, Yashraj Narang, Michael R. Walter, Aaron M. Johnson, Animesh Garg [author list condensed in available source materials]"
year: 2024
venue: "Science Robotics"
url: "https://github.com/facebookresearch/neuralfeels"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation

## Metadata
- Authors: Sudharshan Suresh, Tzu-Yu Chiu, Ivan F. Garcia, Yashraj Narang, Michael R. Walter, Aaron M. Johnson, Animesh Garg [author list condensed in available source materials]
- Year: 2024
- Venue: Science Robotics
- Primary URL: https://github.com/facebookresearch/neuralfeels
- Abstract source: openalex

## Abstract
> To achieve human-level dexterity, robots must infer spatial awareness from multimodal sensing to reason over contact interactions. During in-hand manipulation of novel objects, such spatial awareness involves estimating the object's pose and shape. The status quo for in-hand perception primarily employs vision, and restricts to tracking a priori known objects. Moreover, visual occlusion of objects in-hand is imminent during manipulation, preventing current systems to push beyond tasks without occlusion. We combine vision and touch sensing on a multi-fingered hand to estimate an object's pose and shape during in-hand manipulation. Our method, NeuralFeels, encodes object geometry by learning a neural field online and jointly tracks it by optimizing a pose graph problem. We study multimodal in-hand perception in simulation and the real-world, interacting with different objects via a proprioception-driven policy. Our experiments show final reconstruction F-scores of $81$% and average pose drifts of $4.7\,\text{mm}$, further reduced to $2.3\,\text{mm}$ with known CAD models. Additionally, we observe that under heavy visual occlusion we can achieve up to $94$% improvements in tracking compared to vision-only methods. Our results demonstrate that touch, at the very least, refines and, at the very best, disambiguates visual estimates during in-hand manipulation. We release our evaluation dataset of 70 experiments, FeelSight, as a step towards benchmarking in this domain. Our neural representation driven by multimodal sensing can serve as a perception backbone towards advancing robot dexterity. Videos can be found on our project website https://suddhu.github.io/neural-feels/

## Why It Matters
- Pushes beyond static reconstruction into online in-hand perception, showing that a neural field can be maintained live during manipulation using vision, touch, and proprioception.
- It released FeelSight and made visuo-tactile benchmarking more concrete by reporting reconstruction, pose-drift, and heavy-occlusion tracking metrics on a public evaluation set [S2].
- A strong state-of-the-art example of online multimodal implicit perception: neural fields and pose-graph optimization let touch disambiguate severe visual occlusions during in-hand manipulation.
- Shows online neural-field tracking and reconstruction of novel in-hand objects, with tactile input substantially improving performance under severe visual occlusion.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback|Integrated multimodal systems combining vision tactile and force feedback]]
- [[Subtopic - Tactile-guided reaching contact localization and active haptic exploration of unknown objects|Tactile-guided reaching contact localization and active haptic exploration of unknown objects]]
