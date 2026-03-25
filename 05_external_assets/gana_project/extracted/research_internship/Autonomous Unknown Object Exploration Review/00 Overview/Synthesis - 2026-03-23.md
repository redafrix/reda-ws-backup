---
title: Synthesis - Autonomous Unknown Object Exploration
tags:
  - research-review
  - synthesis
  - robotics
  - manipulation
date: 2026-03-23
time_window: 2021-03-23 to 2026-03-23
---

# Synthesis

## Scope

This synthesis covers the eight validated subtopic reviews in this vault:
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan]]
- [[Subtopic - Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor]]
- [[Subtopic - Tactile-guided reaching contact localization and active haptic exploration of unknown objects]]
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback]]
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps]]

## Verification Status

This note is a synthesis layer, not a list of independently proven theorems.
- Concrete paper facts in the vault come from primary sources where possible.
- Novelty wording such as "first" should be treated as an author claim unless explicitly re-audited.
- The conclusions below are evidence-grounded inferences across the audited paper set.
- See [[Verification Audit - 2026-03-23]] for the current audit status and remaining gaps.

## Executive Summary

The strongest state-of-the-art pattern is not a single monolithic policy. It is a staged autonomy loop:
- active vision or object-centric mapping narrows uncertainty,
- sparse touch or force-controlled contact resolves the remaining geometry,
- then a local controller or task policy executes the final contact-rich behavior.

Pure vision is now strong enough for efficient approach, next-best-view planning, and some occlusion-aware grasping, but it is still weak on hidden support surfaces, reflective or transparent regions, and the final millimeters of alignment. That gap is exactly where visuo-tactile and force-aware systems still matter most.

The most credible near-term route for one manipulator is therefore hybrid:
- use vision for global search, target selection, and view planning;
- use touch or force only when uncertainty concentrates on task-critical geometry;
- stop when the model is task-sufficient, not when it is globally complete.

Foundation-model and VLA methods are now relevant, but mainly for semantic grounding, task conditioning, and long-horizon sequencing. They are not yet a drop-in replacement for local contact estimation, compliant control, or uncertainty-aware surface exploration.

## What Changed From 2021 To 2026

From 2021 to roughly 2023, object-centric active perception was still dominated by explicit maps, tactile SLAM formulations, and task-specific servoing. By 2024, the field moved toward neural object fields, uncertainty-driven action selection, active tactile probing, and one-shot or globally optimized view planning. By 2025 and early 2026, three changes became clear:
- more methods optimize for task-conditioned object understanding rather than uniform reconstruction;
- more systems combine modalities instead of trusting a single sensor;
- more papers claim unseen-object or unseen-environment transfer, but the evidence is still mostly in curated tabletop or household settings.

Representative anchor papers for that transition are [[Paper - Active Visuo-Haptic Object Shape Completion]], [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]], [[Paper - Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions|ActNeRF]], [[Paper - VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility]], [[Paper - OpenVLA: An Open-Source Vision-Language-Action Model]], and [[Paper - Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation]].

## Main Conclusions

1. Task-sufficient object models are overtaking full reconstruction.
For manipulation, the literature increasingly stops once the robot knows the graspable rim, collision-critical envelope, insertion feature, contact frame, or support surface. Full watertight scanning with one arm is still expensive and often unnecessary.

2. Active touch is most valuable as a sparse corrective action.
The best tactile papers do not use touch everywhere. They use it where vision is occluded, ambiguous, reflective, or locally precision-critical. That is the strongest design pattern for your stated use case.

3. Local contact control remains a separate competency.
Even with stronger VLA and VLM systems, force direction, interaction-frame estimation, admittance or impedance regulation, and tactile servoing are still handled by dedicated local loops. The data supports keeping that separation.

4. Multimodal fusion matters most in hard cases.
The clearest win regions are heavy occlusion, in-hand tracking, transparent objects, precise insertion, contour following, and other tasks where geometry must be corrected online.

5. Benchmarking is still behind capability claims.
There is still no accepted benchmark that jointly measures action budget, uncertainty reduction, force safety, and final task success on unknown objects with a single manipulator.

## Recommended System Stack For Your Use Case

If the target is one robot manipulator that must autonomously reach, touch, contour, or scan unseen static objects, the most defensible stack from the current literature is:

### Perception Layer
- wrist or eye-in-hand RGB-D if possible; RGB if not
- object-centric uncertainty map or explicit occupancy shell for safe planning
- optional lightweight 3D-aware VLA or VLM module for semantic target selection, not for direct contact control

### Active Exploration Layer
- motion-efficient view planner in the style of [[Paper - PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects]] or the Bonn one-shot view-planning line
- explicit escalation from viewing to touching only when uncertainty remains on task-critical surfaces
- reorientation as a first-class action, because one arm cannot see or touch all relevant surfaces from camera motion alone

### Contact Layer
- one dense fingertip tactile sensor or a reliable wrist force-torque sensor
- guarded contact, then local registration or tactile localization in the style of [[Paper - Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole]], [[Paper - TacLoc: Global Tactile Localization on Objects from a Registration Perspective]], or [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]]
- interaction-frame or force-direction estimation before full contact-rich execution

### Control Layer
- hybrid force-position or admittance controller for the last-contact phase
- optionally an RL local policy only for short-horizon corrective behaviors, not for the entire autonomy loop
- explicit stopping rules based on confidence, touch budget, or downstream task readiness

## Where VLA Methods Actually Help

The evidence in this corpus suggests that VLA methods help most in:
- open-vocabulary target selection,
- semantic disambiguation among distractors,
- long-horizon subgoal sequencing,
- generating coarse visual or spatial priors before contact.

They help less in:
- final alignment,
- force-safe contact establishment,
- contour following,
- precise insertion,
- uncertainty-calibrated local geometry estimation.

That makes a hybrid architecture more credible than a pure end-to-end VLA stack for research on unknown-object touch and scan.

## Research Gaps That Still Matter

- No standard benchmark ties reconstruction quality to manipulation value under matched action budgets.
- Clutter, articulation, deformability, transparency, and force safety are still mostly split across separate subliteratures.
- End-to-end loops that cover first detection, active sensing, guarded contact, local correction, and final manipulation are still rare.
- Sim-to-real transfer for tactile and force-sensitive policies is improving, but still fragile.
- Benchmark suites for VLAs under-contact are much weaker than their language and scene-generalization benchmarks.

## Recommended Reading Order

If the goal is a practical single-arm research program, the fastest path through the vault is:
- [[Subtopic - Active visual exploration and next-best-view control for unknown object approach reach and scan]]
- [[Subtopic - Tactile-guided reaching contact localization and active haptic exploration of unknown objects]]
- [[Subtopic - Force feedback impedance control contour following and compliant contact exploration]]
- [[Subtopic - Integrated multimodal systems combining vision tactile and force feedback]]
- [[Subtopic - Reinforcement learning for unknown object exploration touch and manipulation]]
- [[Subtopic - Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects]]
- [[Subtopic - Benchmarks datasets evaluation protocols and open research gaps]]

## Shortlist

If I had to pick a compact shortlist for your exact problem, I would start with:
- [[Paper - Active Visuo-Haptic Object Shape Completion]]
- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]]
- [[Paper - VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility]]
- [[Paper - Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole]]
- [[Paper - TacLoc: Global Tactile Localization on Objects from a Registration Perspective]]
- [[Paper - PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects]]
- [[Paper - OpenVLA: An Open-Source Vision-Language-Action Model]]
- [[Paper - OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model]]
- [[Paper - Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation]]
- [[Paper - Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch]]
