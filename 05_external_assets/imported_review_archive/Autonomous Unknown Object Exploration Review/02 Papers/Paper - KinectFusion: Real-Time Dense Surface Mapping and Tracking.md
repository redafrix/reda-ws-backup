---
title: "KinectFusion: Real-Time Dense Surface Mapping and Tracking"
authors: "Richard A. Newcombe, Shahram Izadi, Otmar Hilliges, David Molyneaux, David Kim, Andrew J. Davison, Pushmeet Kohli, Jamie Shotton, Steve Hodges, Andrew Fitzgibbon"
year: 2011
venue: "ISMAR 2011"
url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/ismar_2011.pdf"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# KinectFusion: Real-Time Dense Surface Mapping and Tracking

## Metadata
- Authors: Richard A. Newcombe, Shahram Izadi, Otmar Hilliges, David Molyneaux, David Kim, Andrew J. Davison, Pushmeet Kohli, Jamie Shotton, Steve Hodges, Andrew Fitzgibbon
- Year: 2011
- Venue: ISMAR 2011
- Primary URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/ismar_2011.pdf
- Abstract source: openalex
- Abstract matched title: KinectFusion: Real-time dense surface mapping and tracking

## Abstract
> We present a system for accurate real-time mapping of complex and arbitrary indoor scenes in variable lighting conditions, using only a moving low-cost depth camera and commodity graphics hardware. We fuse all of the depth data streamed from a Kinect sensor into a single global implicit surface model of the observed scene in real-time. The current sensor pose is simultaneously obtained by tracking the live depth frame relative to the global model using a coarse-to-fine iterative closest point (ICP) algorithm, which uses all of the observed depth data available. We demonstrate the advantages of tracking against the growing full surface model compared with frame-to-frame tracking, obtaining tracking and mapping results in constant time within room sized scenes with limited drift and high accuracy. We also show both qualitative and quantitative results relating to various aspects of our tracking and mapping system. Modelling of natural scenes, in real-time with only commodity sensor and GPU hardware, promises an exciting step forward in augmented reality (AR), in particular, it allows dense surfaces to be reconstructed in real-time, with a level of detail and robustness beyond any solution yet presented using passive computer vision.

## Why It Matters
- Established real-time dense TSDF-style fusion as a practical robot mapping primitive; later object-centric TSDF pipelines inherit this explicit volumetric mindset.

## Mentioned In
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor|Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
