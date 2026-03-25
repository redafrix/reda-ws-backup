---
title: "How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF?"
authors: "Sicong Pan, Liren Jin, Hao Hu, Marija Popovic, Maren Bennewitz"
year: 2024
venue: "ICRA 2024"
url: "https://www.hrl.uni-bonn.de/publications/2023/how-many-views-are-needed-to-reconstruct-an-unknown-object-using-nerf"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF?

## Metadata
- Authors: Sicong Pan, Liren Jin, Hao Hu, Marija Popovic, Maren Bennewitz
- Year: 2024
- Venue: ICRA 2024
- Primary URL: https://www.hrl.uni-bonn.de/publications/2023/how-many-views-are-needed-to-reconstruct-an-unknown-object-using-nerf
- Abstract source: openalex

## Abstract
> Neural Radiance Fields (NeRFs) are gaining significant interest for online active object reconstruction due to their exceptional memory efficiency and requirement for only posed RGB inputs. Previous NeRF-based view planning methods exhibit computational inefficiency since they rely on an iterative paradigm, consisting of (1) retraining the NeRF when new images arrive; and (2) planning a path to the next best view only. To address these limitations, we propose a non-iterative pipeline based on the Prediction of the Required number of Views (PRV). The key idea behind our approach is that the required number of views to reconstruct an object depends on its complexity. Therefore, we design a deep neural network, named PRVNet, to predict the required number of views, allowing us to tailor the data acquisition based on the object complexity and plan a globally shortest path. To train our PRVNet, we generate supervision labels using the ShapeNet dataset. Simulated experiments show that our PRV-based view planning method outperforms baselines, achieving good reconstruction quality while significantly reducing movement cost and planning time. We further justify the generalization ability of our approach in a real-world experiment.

## Why It Matters
- Turns active scanning into a budgeted planning problem by predicting the required number of views from object complexity, then optimizing the global view path [S10].

## Mentioned In
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan|Active visual exploration and next-best-view control for unknown object approach reach and scan]]
