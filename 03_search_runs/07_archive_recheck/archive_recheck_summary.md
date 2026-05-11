# Archive Recheck Summary

Date: 2026-03-23

## Goal

Re-audit the archived `Autonomous Unknown Object Exploration Review` corpus from Gana and identify useful papers that were not retained in the active final set, with special attention to reinforcement-learning-centered and hybrid contact-policy papers.

## Main Result

Yes, there are still useful papers in the archived corpus that should not be ignored.

The strongest missed papers are not random extras. They mostly fall into two useful branches:

- local tactile or visuo-tactile policies for unknown geometry and contact correction
- hybrid pipelines where global vision localizes the target and a local RL or world-model policy handles the final contact-rich phase

## Strongest Missed Papers

### Best RL or Hybrid-RL Misses

1. `Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry`  
   Why it matters: one of the clearest early direct RL papers on unseen geometry. It treats insertion as repeated attempt-plus-correction and reports over 85 percent success on 4 novel objects with tactile flow.

2. `Touch begins where vision ends: Generalizable policies for contact-rich manipulation`  
   Why it matters: very relevant hybrid design. A global vision-language stage localizes, then a reusable local visuo-tactile policy with residual RL handles the contact-rich part. This matches your internship logic well.

3. `OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation`  
   Why it matters: strong 2026 world-model direction with visuo-tactile data at larger scale and explicit reflexive tactile correction. More frontier-heavy, but important.

4. `Visuo-Tactile Transformers for Manipulation`  
   Why it matters: useful for the model-based RL and representation-learning branch, though less direct than the three above.

### Strong Non-RL Misses Still Worth Keeping

5. `Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole`  
   Why it matters: not RL, but one of the cleanest tactile-guided unseen-geometry papers in the archive.

6. `Active Visuo-Haptic Object Shape Completion`  
   Why it matters: uncertainty-driven active touch that improves downstream grasping on novel objects.

7. `FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback`  
   Why it matters: strong closed-loop vision-plus-touch localization and reconstruction on unseen objects.

## Useful But Not Priority Additions

- `Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects`
- `Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch`
- `Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation`

These are useful, but less aligned with the current first benchmark:

- curiosity-driven exploration is more about reconstruction than task execution
- Tactile Gym 2.0 is more benchmark/infrastructure than direct solution
- the dexterous force-based sim-to-real paper is strong, but more about multi-finger tactile manipulation than your simpler arm benchmark

## Already Covered Elsewhere

These were in the archive but are already represented in the active workspace or active queue:

- `AcTExplore`
- `Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing`
- `OG-VLA`
- `Scaling World Model for Hierarchical Manipulation Policies`
- `GeneralVLA`
- `VISO-Grasp`

## Recommended Next Action

If the goal is to strengthen the active reading set without polluting it, the best additions from the archive are:

1. `Tactile-RL for Insertion`
2. `Touch begins where vision ends`
3. `Touch2Insert`
4. `OmniVTA`
5. `Active Visuo-Haptic Object Shape Completion`

## Source Archive

- `05_external_assets/imported_review_archive/Autonomous Unknown Object Exploration Review`
