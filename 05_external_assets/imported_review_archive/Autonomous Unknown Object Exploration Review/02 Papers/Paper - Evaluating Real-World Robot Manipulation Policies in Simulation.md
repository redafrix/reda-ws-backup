---
title: "Evaluating Real-World Robot Manipulation Policies in Simulation"
authors: "Xuanlin Li, Tsung-Yen Yang, Quan Vuong, Ben Eysenbach, Karl Pertsch, Sergey Levine and collaborators"
year: 2024
venue: "CoRL 2024 [uncertain]"
url: "https://arxiv.org/abs/2405.05941"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Evaluating Real-World Robot Manipulation Policies in Simulation

## Metadata
- Authors: Xuanlin Li, Tsung-Yen Yang, Quan Vuong, Ben Eysenbach, Karl Pertsch, Sergey Levine and collaborators
- Year: 2024
- Venue: CoRL 2024 [uncertain]
- Primary URL: https://arxiv.org/abs/2405.05941
- Abstract source: arxiv_api

## Abstract
> The field of robotics has made significant advances towards generalist robot manipulation policies. However, real-world evaluation of such policies is not scalable and faces reproducibility challenges, which are likely to worsen as policies broaden the spectrum of tasks they can perform. We identify control and visual disparities between real and simulated environments as key challenges for reliable simulated evaluation and propose approaches for mitigating these gaps without needing to craft full-fidelity digital twins of real-world environments. We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups. Through paired sim-and-real evaluations of manipulation policies, we demonstrate strong correlation between policy performance in SIMPLER environments and in the real world. Additionally, we find that SIMPLER evaluations accurately reflect real-world policy behavior modes such as sensitivity to various distribution shifts. We open-source all SIMPLER environments along with our workflow for creating new environments at https://simpler-env.github.io to facilitate research on general-purpose manipulation policies and simulated evaluation frameworks.

## Why It Matters
- It reframed benchmark design around reproducible policy verification, showing that a well-matched simulator can correlate strongly with real-world manipulation outcomes [S9].

## Mentioned In
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps|Benchmarks datasets evaluation protocols and open research gaps]]
