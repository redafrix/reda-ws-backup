# Generalization-Focused Pass

Date: 2026-03-23

## Why This Pass Exists

The earlier passes found a useful literature set, but they still over-weighted active exploration and tactile exploration. After the task clarification, the first reading wave needed to be corrected.

The actual first-wave question is:

- same task
- new unseen object
- camera is mandatory
- touch is optional support

That means papers about category-level manipulation, open-world object grounding, no-object-model manipulation, and data-efficient adaptation should be read before tactile exploration papers.

## New First-Wave Additions

- `ObjectVLA`
- `GenDP`
- `Learning Category-Level Generalizable Object Manipulation Policy via Generative Adversarial Self-Imitation Learning from Demonstrations`
- `Open-World Object Manipulation using Pre-trained Vision-Language Models`
- `Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation`

## Main Correction

Use this priority order:

1. task generalization on unseen objects
2. category-level and open-world manipulation
3. sim-to-real or synthetic-data support
4. VLA baselines
5. tactile and active-exploration support

## What Stays Weak

Even after this correction, the exact minimal benchmark is still weak in the literature:

- simple reaching to unseen objects
- controlled one-factor shifts like color first and shape next
- touch-as-confirmation rather than full manipulation

That gap is still real. The likely internship contribution is to simplify the benchmark while borrowing representations or control logic from stronger manipulation papers.
