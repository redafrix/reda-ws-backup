---
title: "Learning Transferable Visual Models From Natural Language Supervision"
authors: "Alec Radford et al."
year: 2021
venue: "ICML 2021; preprint posted before the review window"
url: "https://arxiv.org/abs/2103.00020"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Learning Transferable Visual Models From Natural Language Supervision

## Metadata
- Authors: Alec Radford et al.
- Year: 2021
- Venue: ICML 2021; preprint posted before the review window
- Primary URL: https://arxiv.org/abs/2103.00020
- Abstract source: arxiv_api

## Abstract
> State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

## Why It Matters
- CLIP is the core semantic precursor for open-vocabulary manipulation: CLIPort depends on it directly, and later VLA work inherits the broader recipe of web-scale vision-language pretraining [S27,S1].

## Mentioned In
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects|Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
