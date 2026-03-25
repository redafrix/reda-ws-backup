# World Models And pi*0.6 Sweep

Date: 2026-03-23

## Scope

This pass isolates the `world model` branch from the broader unseen-object literature.

For this internship, a world-model paper is useful if it does at least one of these:

- predicts future visual or physical states under robot actions
- plans through imagined intermediate states or goals
- uses an internal simulator or digital twin to improve manipulation
- improves manipulation on novel objects, scenes, or layouts through that predictive model

`pi*0.6` is included as an adjacent paper because it is recent, high-signal, and directly about improving a VLA from real experience with RL, even though it is not itself an explicit world-model paper.

## Ranked Shortlist

1. `PointWorld`
   Why it matters: probably the strongest direct new addition. It is a large pretrained 3D world model that predicts full-scene point flow and can drive MPC from a single in-the-wild RGB-D observation without demonstrations or post-training.

2. `Scaling World Model for Hierarchical Manipulation Policies`
   Why it matters: already in the main set, but it clearly belongs in the world-model branch. It uses a world model to generate visual subgoals before low-level execution.

3. `Goal-VLA`
   Why it matters: object-centric world model that imagines the desired future state, then controls toward it. Strong conceptual fit for unseen-object transfer.

4. `Act2Goal`
   Why it matters: strong recent paper on goal-conditioned world models plus multi-scale temporal control. The abstract explicitly claims zero-shot generalization to novel objects, layouts, and environments.

5. `Dream to Manipulate`
   Why it matters: compositional world model built as an explicit, manipulable reconstruction of the scene. Good fit if we care about low-data generalization and imagining new object configurations.

6. `pi*0.6: A VLA That Learns from Experience`
   Why it matters: not a world model, but a major recent RL-for-VLA paper. It shows how a strong VLA can improve from demonstrations, online corrections, and autonomous experience in the real world.

7. `GWM`
   Why it matters: 3D Gaussian world model that improves policy learning and supports model-based RL. Strong 3D representation paper, though the demonstrated real task is still simpler than our full target.

8. `Visuo-Tactile World Models`
   Why it matters: best contact-rich world-model addition if we later need touch to stabilize unseen-object behavior under occlusion or ambiguous contact.

9. `OmniVTA`
   Why it matters: already in the main set. It is the larger-scale, more system-heavy visuo-tactile world-model branch.

10. `iMoWM`
    Why it matters: efficient multimodal world model that predicts RGB, depth, and robot masks. Useful support paper, but less directly tied to unseen-object transfer than the top papers above.

11. `DayDreamer`
    Why it matters: foundational real-robot world-model RL baseline. Important background for understanding why model-based imagination helps, but less directly focused on unseen-object manipulation.

## Main Takeaways

- The world-model branch is real and now strong enough to deserve its own reading slice.
- The best additions for this internship are not generic world models. They are the ones that expose geometry, object structure, or contact in a way that helps transfer the same task to a new object.
- `PointWorld`, `Act2Goal`, and `Dream to Manipulate` were genuinely under-covered before this pass.
- `pi*0.6` should be read alongside the world-model papers because it addresses a nearby question: how to make a strong robot policy improve from deployment rather than only from static demonstrations.

## Promotion Recommendation

If only a few papers from this sweep should enter the main active reading stream, promote these first:

1. `PointWorld`
2. `Act2Goal`
3. `Dream to Manipulate`
4. `pi*0.6`

Then use these as support:

1. `GWM`
2. `Visuo-Tactile World Models`
3. `DayDreamer`
4. `iMoWM`

## Terms To Watch

- `World model`: predicts future states under actions.
- `MPC`: model-predictive control, meaning the robot simulates several action options and chooses the best one.
- `Point flow`: 3D motion of points in the scene, useful for predicting how objects will move.
- `Gaussian Splatting`: a 3D scene representation that approximates geometry and appearance with many small 3D blobs.
- `Object-centric`: represent the scene in terms of objects and their states rather than just raw pixels.
- `Latent planning`: planning in a compressed internal representation instead of in raw images.
- `Advantage conditioning`: tell a policy whether an action was better or worse than expected so it can learn from imperfect data.

## Sources

- [pi*0.6 official blog](https://www.physicalintelligence.company/blog/pistar06)
- [pi*0.6 PDF](https://www.physicalintelligence.company/download/pistar06.pdf)
- [PointWorld project page](https://point-world.github.io/)
- [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/abs/2602.10983)
- [Goal-VLA](https://arxiv.org/abs/2506.23919)
- [Act2Goal](https://arxiv.org/abs/2512.23541)
- [Dream to Manipulate project page](https://leobarcellona.github.io/DreamToManipulate/)
- [GWM project page](https://gaussian-world-model.github.io/)
- [Visuo-Tactile World Models](https://arxiv.org/abs/2602.06001)
- [OmniVTA](https://arxiv.org/abs/2603.19201)
- [iMoWM project page](https://xingyoujun.github.io/imowm/)
- [DayDreamer PMLR page](https://proceedings.mlr.press/v205/wu23c.html)
