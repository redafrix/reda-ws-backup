---
title: "ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills"
authors: "Jiayuan Gu, Fanbo Xiang, Xuanlin Li, Zhan Ling, Xiqiang Liu, Tongzhou Mu, Yihe Tang, Stone Tao, Xinyue Wei, Yunchao Yao, Xiaodi Yuan, Pengwei Xie, Zhiao Huang, Rui Chen, Hao Su"
year: 2023
venue: "ICLR 2023"
url: "https://arxiv.org/abs/2302.04659"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills

## Metadata
- Authors: Jiayuan Gu, Fanbo Xiang, Xuanlin Li, Zhan Ling, Xiqiang Liu, Tongzhou Mu, Yihe Tang, Stone Tao, Xinyue Wei, Yunchao Yao, Xiaodi Yuan, Pengwei Xie, Zhiao Huang, Rui Chen, Hao Su
- Year: 2023
- Venue: ICLR 2023
- Primary URL: https://arxiv.org/abs/2302.04659
- Abstract source: html_meta
- Abstract matched title: [2302.04659] ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills

## Abstract
> Generalizable manipulation skills, which can be composed to tackle long-horizon and complex daily chores, are one of the cornerstones of Embodied AI. However, existing benchmarks, mostly composed of a suite of simulatable environments, are insufficient to push cutting-edge research works because they lack object-level topological and geometric variations, are not based on fully dynamic simulation, or are short of native support for multiple types of manipulation tasks. To this end, we present ManiSkill2, the next generation of the SAPIEN ManiSkill benchmark, to address critical pain points often encountered by researchers when using benchmarks for generalizable manipulation skills. ManiSkill2 includes 20 manipulation task families with 2000+ object models and 4M+ demonstration frames, which cover stationary/mobile-base, single/dual-arm, and rigid/soft-body manipulation tasks with 2D/3D-input data simulated by fully dynamic engines. It defines a unified interface and evaluation protocol to support a wide range of algorithms (e.g., classic sense-plan-act, RL, IL), visual observations (point cloud, RGBD), and controllers (e.g., action type and parameterization). Moreover, it empowers fast visual input learning algorithms so that a CNN-based policy can collect samples at about 2000 FPS with 1 GPU and 16 processes on a regular workstation. It implements a render server infrastructure to allow sharing rendering resources across all environments, thereby significantly reducing memory usage. We open-source all codes of our benchmark (simulator, environments, and baselines) and host an online challenge open to interdisciplinary researchers.

## Why It Matters
- It made unified interfaces and evaluation protocols a first-class benchmark contribution, covering 20 task families, 2000+ object models, and multiple manipulation regimes [S5].

## Mentioned In
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
