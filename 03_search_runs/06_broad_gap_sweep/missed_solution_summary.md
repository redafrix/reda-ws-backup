# Broad Gap Sweep

Date: 2026-03-23

## Why This Sweep Was Needed

The RL-only sweep found one real miss, but the broader issue is that earlier searches underweighted several method families:

- visual servoing
- active vision for targeted object reaching or grasping
- 3D-aware VLAs
- hierarchical world-model methods
- object-centric zero-shot planning methods
- older language-conditioned manipulation baselines

That means the current 10-paper must-read set is good, but it is not yet a complete view of all plausible solution families.

## Most Important Misses By Family

### 1. Camera-first reaching

- `Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control`

Why:
- closest direct match to the simplest benchmark
- camera-first
- robot arm reaching
- unseen objects
- novel viewpoints

This is the strongest single missed paper overall.

### 2. Active vision for unseen targets

- `Distributed Reinforcement Learning of Targeted Grasping with Active Vision for Mobile Manipulators`
- `VISO-Grasp`

Why:
- both explicitly use additional sensing actions to resolve target ambiguity
- both are still object-directed rather than generic exploration papers

### 3. Stronger 3D-aware VLA branch

- `OG-VLA`
- `Scaling World Model for Hierarchical Manipulation Policies`
- `Goal-VLA`
- `GeneralVLA`

Why:
- these are strong recent papers that address the same generalization bottleneck as ObjectVLA from different angles
- they are not all must-read immediately, but they are too relevant to ignore

### 4. Older but important baseline families

- `CLIPort`
- `VoxPoser`

Why:
- both are major solution templates for open-set or language-grounded manipulation
- both can still inform a clean internship direction even if they are not your final method

## What This Changes

The current must-read set is still valid, but it is now clear that there are at least three more families we had not represented well enough:

1. `visual servoing and active vision`
2. `3D-aware and hierarchical VLA`
3. `language-to-planning / open-set manipulation baselines`

## Promotion Order

If we promote any of these into the active reading queue, the best order is:

1. `Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control`
2. `OG-VLA`
3. `Scaling World Model for Hierarchical Manipulation Policies`
4. `Distributed Reinforcement Learning of Targeted Grasping with Active Vision for Mobile Manipulators`
5. `Goal-VLA`
6. `GeneralVLA`

## Important Clarification

These are **candidate additions** and **missed solution families**.

They are not automatically part of the final must-read graph yet, because adding all of them immediately would dilute the current clean reading set again.
