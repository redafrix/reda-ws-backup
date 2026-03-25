---
title: "OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model"
authors: "Ishika Singh, Ankit Goyal, Stan Birchfield, Dieter Fox, Animesh Garg, Valts Blukis"
year: 2025
venue: "ICRA 2026 submission / arXiv"
url: "https://arxiv.org/abs/2506.01196"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model

## Metadata
- Authors: Ishika Singh, Ankit Goyal, Stan Birchfield, Dieter Fox, Animesh Garg, Valts Blukis
- Year: 2025
- Venue: ICRA 2026 submission / arXiv
- Primary URL: https://arxiv.org/abs/2506.01196
- Abstract source: html_meta
- Abstract matched title: [2506.01196] OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model

## Abstract
> We introduce OG-VLA, a novel architecture and learning framework that combines the generalization strengths of Vision Language Action models (VLAs) with the robustness of 3D-aware policies. We address the challenge of mapping natural language instructions and one or more RGBD observations to quasi-static robot actions. 3D-aware robot policies achieve state-of-the-art performance on precise robot manipulation tasks, but struggle with generalization to unseen instructions, scenes, and objects. On the other hand, VLAs excel at generalizing across instructions and scenes, but can be sensitive to camera and robot pose variations. We leverage prior knowledge embedded in language and vision foundation models to improve generalization of 3D-aware keyframe policies. OG-VLA unprojects input observations from diverse views into a point cloud which is then rendered from canonical orthographic views, ensuring input view invariance and consistency between input and output spaces. These canonical views are processed with a vision backbone, a Large Language Model (LLM), and an image diffusion model to generate images that encode the next position and orientation of the end-effector on the input scene. Evaluations on the Arnold and Colosseum benchmarks demonstrate state-of-the-art generalization to unseen environments, with over 40% relative improvements while maintaining robust performance in seen settings. We also show real-world adaption in 3 to 5 demonstrations along with strong generalization. Videos and resources at https://og-vla.github.io/

## Why It Matters
- Representative of the 3D-aware branch that explicitly addresses camera-pose sensitivity and spatial-layout robustness for unseen scenes and objects [S21].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
