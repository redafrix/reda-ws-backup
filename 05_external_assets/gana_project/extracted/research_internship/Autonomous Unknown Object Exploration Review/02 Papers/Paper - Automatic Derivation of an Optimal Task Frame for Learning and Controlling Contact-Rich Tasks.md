---
title: "Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks"
authors: "Ali Mousavi Mohammadi, Maxim Vochten, Erwin Aertbelien, Joris De Schutter"
year: 2026
venue: "Robotics and Autonomous Systems"
url: "https://arxiv.org/abs/2404.01900"
tags:
  - paper
  - research-review
  - unknown-object-exploration
---

# Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks

## Metadata
- Authors: Ali Mousavi Mohammadi, Maxim Vochten, Erwin Aertbelien, Joris De Schutter
- Year: 2026
- Venue: Robotics and Autonomous Systems
- Primary URL: https://arxiv.org/abs/2404.01900
- Abstract source: arxiv_api

## Abstract
> In previous work on learning and controlling contact-rich tasks, the procedure for choosing a proper reference frame to express learned signals for the motion and the interaction wrench is often implicit, requires expert insight, or starts from proposed frame candidates. This article presents an automatic method to derive the optimal reference frame, referred to as optimal task frame, directly from the recorded motion and wrench data of the demonstration. Using screw theory, several origin and orientation candidates are generated that maximize decoupling in the data. These candidates are then processed probabilistically, without needing hyperparameters, to obtain the optimal task frame. Its origin and orientation are independently fixed to either the world or the robot tool. The method works regardless of whether the task involves translation, rotation, force, or moment, or any combination thereof. The method was validated for various tasks, including surface following and manipulation of articulated objects, showing good agreement between derived and assumed expert task frames. To validate the robot's performance, a constraint-based controller was designed based on the data expressed in the derived task frames. These experiments demonstrated the approach's effectiveness and versatility. The automatic task frame derivation approach supports learning methods to design controllers for a wide range of contact-rich tasks.

## Why It Matters
- Formalized a data-driven way to recover the task frame from recorded motion and wrench demonstrations, directly supporting surface following and other force-constrained tasks without manual frame engineering.

## Mentioned In
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration|Force feedback impedance control contour following and compliant contact exploration]]
