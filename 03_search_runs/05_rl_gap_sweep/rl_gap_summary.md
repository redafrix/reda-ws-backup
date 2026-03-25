# RL Gap Sweep

Date: 2026-03-23

## Why This Sweep Was Needed

The earlier literature passes over-weighted:

- category-level manipulation
- VLA grounding
- tactile exploration
- object-model-free manipulation

They under-weighted RL papers using older or different language, especially:

- visual servoing
- active vision
- query-object reaching
- recurrent control
- targeted grasping

That is why an on-target RL paper was missed even though it matches the internship well.

## Most Important Missed Paper

### Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control

This is the strongest missed paper for the current internship question.

Why:

- it is explicitly about **reaching** a visually indicated object
- it uses **camera input**
- it uses a **reinforcement learning objective**
- it transfers to **previously unseen objects**
- it tests **novel viewpoints**

Primary-source support:

- the CVPR paper states that the arm must reach objects using monocular camera observations from an arbitrary viewpoint
- the paper further states that the model can reach previously unseen objects from novel viewpoints on a real Kuka IIWA arm

## Strong RL Additions

1. `Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control`
   Best direct RL match to the reaching-on-unseen-objects problem.

2. `Distributed Reinforcement Learning of Targeted Grasping with Active Vision for Mobile Manipulators`
   Strong RL paper on targeted grasping of unseen objects with active vision.

3. `HACMan`
   Strong RL paper for unseen-category non-prehensile manipulation with zero-shot transfer.

4. `Multi-Stage Reinforcement Learning for Non-Prehensile Manipulation`
   RL paper that explicitly says previous methods often learn one skill such as reach or push, then demonstrates unseen-shape transfer.

5. `Sim2Real Manipulation on Unknown Objects with Tactile-based Reinforcement Learning`
   Best touch-heavy RL addition if the project later depends on tactile sensing.

## Search Terms That Should Stay In The Workflow

Add these query families permanently:

- `visual servoing reinforcement learning unseen objects`
- `query object reaching robot reinforcement learning`
- `active vision targeted grasping unseen objects RL`
- `non-prehensile manipulation unseen objects RL`
- `goal-conditioned reinforcement learning object reaching robot`
- `sim2real robotic manipulation unseen objects reinforcement learning`

## Recommendation

Do not immediately promote all RL additions into the final must-read graph.

Promote in this order:

1. `Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control`
2. `Distributed Reinforcement Learning of Targeted Grasping with Active Vision for Mobile Manipulators`
3. `HACMan`

The first one is the most likely paper the user had in mind.
