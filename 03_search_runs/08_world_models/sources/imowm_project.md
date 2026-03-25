Arxiv 2025

[Chuanrui Zhang](https://xingyoujun.github.io/) <sup>1</sup>, Zhengxian Wu <sup>2</sup>, Guanxing Lu <sup>2</sup>, Yansong Tang <sup>2</sup>, [Ziwei Wang](https://ziweiwangthu.github.io/) <sup>1</sup>,

<sup>1</sup> Nanyang Technological University, <sup>2</sup> Tsinghua University

![architecture](https://xingyoujun.github.io/imowm/static/images/teaser.png)

architecture

<video controls=""><source src="https://xingyoujun.github.io/imowm/static/videos/video.mp4" type="video/mp4"></video>

## TL;DR

> [!success] Success
> We present iMoWM, an interactive multi-modal world model for robotic manipulation.

## Abstract

Learned world models hold significant potential for robotic manipulation, as they can serve as simulator for real-world interactions. While extensive progress has been made in 2D video-based world models, these approaches often lack geometric and spatial reasoning, which is essential for capturing the physical structure of the 3D world. To address this limitation, we introduce iMoWM, a novel interactive world model designed to generate color images, depth maps, and robot arm masks in an autoregressive manner conditioned on actions. To overcome the high computational cost associated with three-dimensional information, we propose MMTokenizer, which unifies multi-modal inputs into a compact token representation. This design enables iMoWM to leverage large-scale pretrained VideoGPT models while maintaining high efficiency and incorporating richer physical information. With its multi-modal representation, iMoWM not only improves the visual quality of future predictions but also serves as an effective simulator for model-based reinforcement learning (RL) and facilitates real-world imitation learning. Extensive experiments demonstrate the superiority of iMoWM across these tasks, showcasing the advantages of multi-modal world modeling for robotic manipulation.

## Architecture

![architecture](https://xingyoujun.github.io/imowm/static/images/pipeline.png)

Overview of iMoWM. Our method takes a color image as input and extracts the robot-arm mask. The metric depth map is obtained either from RGB-D camera observations or from our depth module. These inputs are then encoded into discrete tokens using the proposed MMTokenizer. By injecting action-conditioned slot tokens, the autoregressive transformer generates future tokens sequentially, which are finally decoded into multi-modal outputs.

## Comparisons with the State-of-the-art

We present qualitative comparisons with the following state-of-the-art models:

![SOTA comparisons](https://xingyoujun.github.io/imowm/static/images/compare.png)