---
title: "Reinforcement learning for unknown object exploration touch and manipulation"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23, including 2026 preprints available by 2026-03-23."
---

# Reinforcement learning for unknown object exploration touch and manipulation

## Scope
This subtopic covers reinforcement-learning-centered methods that use tactile, force, proprioceptive, or visuo-tactile observations to choose probing, contact-establishment, correction, or manipulation actions for previously unseen or partially unknown rigid objects under partial observability. Included methods are model-free, model-based, actor-critic, world-model, curiosity-driven, or hybrid RL systems in which a learned policy is a core part of the closed loop for exploration-to-contact or contact-rich manipulation. The boundary excludes pure tactile perception or reconstruction papers without a learned action policy, pure imitation-learning systems without an RL component, known-object-only deployment that depends on object-specific models at test time, and deformable-object work unless it is used only as adjacent context.

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The note's active-touch anchors are now re-checked, but the broader RL branch still contains many quantitative claims that need a second pass beyond the shortlist.

### Re-checked Claims
- AcTExplore: 95.97% average IoU coverage on unseen YCB objects (`verified-primary-pdf`).
- Tactile Gym 2.0 benchmark framing with three sensors and three tasks is re-checked (`verified-primary-pdf`).

### Still Pending
- Curiosity-driven tSLAM timing claims, tactile pushing gains, and several dexterous-RL results were not yet table-re-audited.
- World-model and reflexive-control numbers in the 2025-2026 branch remain pending a second pass.

## Inclusion Criteria
- Primary-source papers, official project pages, or official conference and journal records within the requested window where the main contribution is an RL or hybrid RL policy for tactile or visuo-tactile exploration or manipulation.
- Methods that explicitly target unknown or unseen object geometry, unseen environments, unseen object configurations, or contact-rich tasks where touch resolves partial observability.
- Benchmark and representation papers were included when they are explicitly designed to support RL or planning with tactile feedback in this subtopic, such as Tactile Gym 2.0, Visuo-Tactile Transformers, and OmniVTA.
- Real-robot and simulation results were both included when the paper makes a substantive claim about unknown-object generalization, sim-to-real transfer, or tactile closed-loop autonomy.

## Exclusion Criteria
- Pure tactile localization, reconstruction, or state-estimation papers without a learned exploration or manipulation policy in the action loop.
- Pure behavior cloning or imitation-learning papers without reinforcement learning, residual RL, or an RL-trained local policy.
- Methods that require a known CAD model, known object identity, or per-object policy specialization at deployment unless used only as background or boundary-setting context.
- Vision-only manipulation, generic force-control papers without unknown-object exploration or manipulation, and deformable-object-only manipulation papers.

## Problem Formulations
- Tactile insertion as an episodic policy that alternates between insertion attempts and pose-correction actions for objects of unknown geometry.
- Touch-only active exploration of an unknown object's surface or shape, where the policy selects informative contacts under a limited touch budget.
- Goal-conditioned tactile pushing without vision, where a model-free or model-based policy must drive an unknown object to a target pose under disturbances.
- Bimanual tactile manipulation of unseen objects, including bi-pushing, bi-reorienting, and bi-gathering, with coordination learned from simulation and transferred to hardware.
- Blind or visuo-tactile dexterous in-hand manipulation, where tactile sensing compensates for missing or unreliable global visual state.
- Two-stage localize-then-execute pipelines, where high-level vision or a VLM identifies the object or region of interest and a reusable local tactile policy performs the contact-rich phase.
- World-model-based contact-rich manipulation, where short-horizon tactile dynamics are predicted explicitly and used for action selection plus reflexive correction.

## Sensing Modalities
- High-resolution optical tactile sensing is dominant, especially TacTip, DIGIT, DigiTac, GelSight-style tactile images, and tactile-flow representations derived from image sequences.
- Proprioception is used nearly everywhere for finger joint state, hand pose, end-effector pose, or object-relative control.
- Force-torque or torque-like signals appear in insertion, force-regulated grasping, and 2026 dexterous manipulation work, either via wrist F/T sensing or current-to-torque calibration.
- Vision is often fused with touch rather than replacing it: examples include vision-based rewards in See to Touch, egocentric vision in ViTaL, visual attention in VTT, and visuo-tactile world modeling in OmniVTA.
- Several systems are intentionally touch-first or touch-only after contact, especially Tactile-RL for Insertion, tactile pushing, tSLAM, AcTExplore, TacGNN, and some dexterous in-hand policies.
- The dominant sensing pattern is multimodal partial observability: vision gives coarse scene context, while touch and proprioception resolve the final local contact state.

## Action Space And Robot Setup
- Single-arm insertion systems usually choose between insertion attempts and small pose-correction motions, often with tactile images or tactile flow as observations.
- Single-arm tabletop systems in Tactile Gym 2.0 and tactile pushing operate with Cartesian motion commands for edge following, surface following, and pushing-to-goal tasks.
- Bimanual systems such as Bi-Touch use two industrial robot arms, each with a tactile fingertip, and learn coordinated motions for object transport and reorientation.
- Dexterous in-hand systems use anthropomorphic hands such as ADROIT, Allegro, or five-finger research hands, typically commanding joint-level actions or higher-level reorientation objectives.
- Hybrid local-policy systems such as ViTaL separate global reaching from local contact execution, so the local action space is intentionally robot-centered and scene-agnostic.
- 2026 dexterous sim-to-real work extends the action space toward explicit force-tracking and reorientation commands, not only pose control.

## Method Families
- Model-free deep RL: actor-critic or policy-gradient methods for tactile insertion, pushing, bimanual manipulation, and dexterous in-hand policies.
- Model-based RL and planning: tactile predictive models or learned multimodal latent dynamics used for control, as in Manipulation by Feel, VTT, and OmniVTA.
- Curiosity-driven or intrinsic-motivation exploration: policies that explicitly seek informative touches for unknown-object reconstruction, such as tSLAM and AcTExplore.
- Hybrid RL with structured priors: curriculum learning, residual RL, behavior-cloned visual encoders, or reactive tactile controllers combined with a learned policy.
- Sim-to-real tactile RL: policies trained in simulation and transferred through tactile image translation, dynamics randomization, latent distillation, or tactile-specific simulation models.
- World-model and latent-distillation approaches: newer methods that learn predictive visuo-tactile dynamics or tactile state estimators to improve sample efficiency and generalization.

## Representative System Pipelines
- Curriculum tactile insertion
  - pipeline: Tactile image or tactile flow after failed insertion -> policy predicts pose correction -> new insertion attempt -> repeat until insertion succeeds or attempt budget is exhausted.
  - examples: Tactile-RL for Insertion
- Sim-to-real tactile pushing
  - pipeline: Current tactile observation plus goal state -> model-free or model-based RL policy -> Cartesian pushing action -> updated tactile observation and object displacement -> repeat.
  - examples: Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing
- Bimanual tactile coordination
  - pipeline: Two tactile fingertip streams plus arm proprioception -> deep RL policy with goal-update mechanism -> synchronized dual-arm actions -> real-world tactile sim-to-real transfer.
  - examples: Bi-Touch
- Unknown-object active touch reconstruction
  - pipeline: Current tactile history or partial shape estimate -> exploration policy with intrinsic reward -> next touch location or motion -> shape update -> repeat until coverage target.
  - examples: Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects; AcTExplore
- Vision-guided local tactile policy
  - pipeline: Global visual localization or visual reward construction -> local tactile or visuo-tactile policy optimization -> contact-rich execution on the robot -> optional residual RL adaptation.
  - examples: See to Touch; Touch begins where vision ends
- Predictive visuo-tactile contact control
  - pipeline: Visuo-tactile encoder -> short-horizon world model predicts contact evolution -> action policy proposes next manipulation action -> reflexive tactile controller corrects mismatch at high frequency.
  - examples: Visuo-Tactile Transformers for Manipulation; OmniVTA

## Evaluation Tasks
- Generalization to unknown-geometry insertion objects and novel peg or receptacle shapes.
- Goal-directed tactile pushing of unseen objects to target poses under disturbances.
- Edge following and surface following with tactile RL benchmarks.
- Touch-only or touch-dominant reconstruction of unknown object surfaces under a fixed exploration budget.
- Bimanual unseen-object bi-pushing, bi-reorienting, and bi-gathering.
- Blind or visuo-tactile dexterous tasks such as peg pick-and-place, bowl unstacking, slender-object flipping, in-hand rotation, reorientation, wiping, and assembly.

## Common Metrics
- Task success rate, often on held-out objects, held-out environments, or held-out object configurations.
- Attempts to success or average number of corrective actions before insertion or task completion.
- Coverage or reconstruction quality metrics such as IoU and F-score for exploration-oriented methods.
- Trajectory quality metrics such as pushing path length, cumulative reward, return, or time to completion.
- Robustness under perturbations, large disturbances, distractors, or sim-to-real transfer without fine-tuning.
- Task-specific dexterous metrics such as number of goals reached, state-prediction RMSE, or force-tracking quality.

## Best Reported Capabilities
- Tactile-RL for Insertion reports that the best learned agent configuration, RL plus curriculum plus tactile flow, inserts 4 novel objects with over 85.0% success rate within 3 to 4 attempts.
- AcTExplore reports 95.97% average IoU coverage on unseen YCB objects while being trained only on primitive shapes, which is one of the strongest unknown-object active-touch reconstruction results in this period.
- Curiosity-driven tSLAM reports reconstruction of objects of varying complexity within 6 seconds of interaction and cross-dataset transfer from 3D Warehouse training objects to ContactDB test objects.
- See to Touch reports 73% success across six challenging dexterous tasks on a four-fingered Allegro hand, with 108% higher performance than policies using tactile and vision rewards together and 135% higher than policies without tactile observations.
- ViTaL reports around 90% success on contact-rich tasks in unseen environments and explicitly claims robustness to distractors using a reusable local tactile policy plus residual RL.
- PTLD reports a 182% improvement over a proprioception-only policy on benchmark in-hand rotation and a 57% improvement in goals reached for tactile in-hand reorientation.
- OmniVTA introduces a 21,000-plus trajectory visuo-tactile-action dataset spanning 86 tasks and 100-plus objects, then reports better real-robot generalization to unseen objects and geometric configurations than prior baselines.
- Closing the Reality Gap demonstrates zero-shot sim-to-real dexterous tactile manipulation with controllable grasp-force tracking and object reorientation on a five-finger hand trained entirely in simulation.

## Failure Modes And Limitations
- Most systems remain restricted to rigid single-object or fixture-based laboratory tasks, with weak evidence in cluttered or open-world scenes.
- Touch remains highly local, so policies often need careful contact initialization, repeated corrections, or a preceding visual localization stage.
- Sim-to-real transfer is still fragile: Bi-Touch explicitly reports unwanted squeezing in one task, and many methods depend on tactile image translation, privileged information, or extensive calibration.
- Generalization claims are usually across small held-out object sets or geometry families rather than broad household-object diversity.
- RL sample efficiency is still a bottleneck, which is why curricula, pretrained encoders, model-based latents, and world models appear repeatedly.
- Benchmark fragmentation makes comparisons difficult because insertion, pushing, dexterous in-hand tasks, and active exploration are usually evaluated on different custom suites.
- Several recent 2026 systems promise public code or data but had not fully released all assets by 2026-03-23, limiting immediate external verification.

## Representative Papers
- [[Paper - Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry|Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry]] (2021, ICRA 2021)
- [[Paper - Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch|Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch]] (2022, IEEE Robotics and Automation Letters)
- [[Paper - Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects|Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects]] (2022, arXiv preprint)
- [[Paper - Visuo-Tactile Transformers for Manipulation|Visuo-Tactile Transformers for Manipulation]] (2022, CoRL 2022)
- [[Paper - Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing|Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing]] (2023, IEEE Robotics and Automation Letters)
- [[Paper - Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning|Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning]] (2023, IEEE Robotics and Automation Letters)
- [[Paper - See to Touch: Learning Tactile Dexterity through Visual Incentives|See to Touch: Learning Tactile Dexterity through Visual Incentives]] (2023, arXiv preprint)
- [[Paper - AcTExplore: Active Tactile Exploration of Unknown Objects|AcTExplore: Active Tactile Exploration of Unknown Objects]] (2024, ICRA 2024)
- [[Paper - Touch begins where vision ends: Generalizable policies for contact-rich manipulation|Touch begins where vision ends: Generalizable policies for contact-rich manipulation]] (2025, arXiv preprint)
- [[Paper - OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation|OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation]] (2026, arXiv preprint)

## Trends 2021 To 2026
- The field shifts from narrow single-task tactile RL policies toward reusable local contact policies and broader contact-rich manipulation suites.
- Pure tactile observation is increasingly fused with vision, force, or torque rather than used alone, especially when policies must generalize beyond one canonical setup.
- Method design moves from mostly model-free RL toward hybrid pipelines that combine pretrained encoders, curricula, residual RL, predictive latents, or world models.
- Unknown-object claims become stronger over time: early papers often generalize across held-out geometries, while later papers claim transfer to unseen objects, unseen environments, and unseen geometric configurations.
- Sim-to-real remains central throughout the window, but the mechanism evolves from image translation and randomization toward latent distillation and explicit tactile dynamics modeling.
- Benchmark scale improves by 2026, but the field still lacks a universally adopted end-to-end benchmark spanning exploration efficiency, contact safety, and downstream manipulation success.

## Research Gaps
- There is still no common benchmark that jointly measures exploration efficiency, task success, safety, and generalization for unknown-object tactile RL.
- Most papers separate reaching, contact establishment, and contact-rich execution; unified end-to-end policies that safely bridge all phases remain rare.
- Long-horizon partial observability is under-addressed: touch is local, but only a few papers use explicit belief updates or world models strong enough for broad open-world behavior.
- Generalization claims are often limited to small geometry families, so scaling to diverse household objects, clutter, and articulated parts is still unresolved.
- Sim-to-real remains expensive because high-quality tactile simulation and hardware calibration are difficult; 2026 distillation approaches help, but they are still early.
- Few methods report contact safety, object damage, or energy-aware interaction metrics, even though those matter directly for autonomous unknown-object exploration.

## Opportunities For Single Manipulator Systems
- A single manipulator with one tactile fingertip or a tactile parallel-jaw gripper can already target the strongest demonstrated use cases: unknown-geometry insertion, contact-aware pushing, guarded local exploration, and local correction after visual localization.
- The most practical architecture is a two-stage stack: global wrist or eye-in-hand vision to localize the candidate object or receptacle, then a local tactile policy trained in simulation and adapted with residual RL or latent distillation.
- For systems without expensive tactile simulation, PTLD-style privileged latent distillation is promising because it reduces dependence on accurate simulated tactile images.
- For exploration tasks, AcTExplore-style active probing and Tactile Gym-style surface-following tasks suggest a feasible path to single-arm next-best-touch systems that build partial geometry before grasping or insertion.
- For manipulation tasks, tactile flow and short-horizon predictive models appear especially promising because they encode local contact evolution with less global-scene complexity than full VLA systems.
- A strong near-term single-arm research stack would combine tactile flow or tactile images, proprioception, an insertion or probing curriculum, a reusable local contact policy, and explicit stopping rules based on confidence or touch budget.

## Sources
- [Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry](https://arxiv.org/abs/2104.01167) | source type: primary paper | why used: Used for the unknown-geometry tactile insertion formulation, RL plus curriculum plus tactile-flow result, and over-85-percent success claim.
- [Tactile-RL for Insertion project page](https://sites.google.com/view/tactileinsertion) | source type: official project page | why used: Used for the ICRA 2021 venue metadata and project-level description of novel-object evaluation.
- [Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch](https://arxiv.org/abs/2207.10763) | source type: primary paper | why used: Used for benchmark tasks, supported sensors, and the sim-to-real tactile RL benchmark framing.
- [Tactile Gym 2.0 project page](https://sites.google.com/view/tactile-gym-2) | source type: official project page | why used: Used for code availability, RA-L metadata, and confirmation of the benchmark's open-source role.
- [Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects](https://arxiv.org/abs/2204.00035) | source type: primary paper | why used: Used for curiosity-driven touch-only exploration, 6-second reconstruction claim, and 3D Warehouse to ContactDB generalization.
- [Visuo-Tactile Transformers for Manipulation](https://arxiv.org/abs/2210.00121) | source type: primary paper | why used: Used for the model-based RL and planning representation-learning branch and CoRL 2022 acceptance.
- [Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning](https://arxiv.org/abs/2307.06423) | source type: primary paper | why used: Used for bimanual tasks, unseen-object perturbation evaluation, RA-L venue, and code availability note.
- [Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing](https://arxiv.org/abs/2307.14272) | source type: primary paper | why used: Used for the model-based versus model-free comparison, unseen-object generalization claim, and tactile pushing formulation.
- [Tactile RL pushing project page](https://sites.google.com/view/tactile-rl-pushing/) | source type: official project page | why used: Used for code and video availability on the tactile pushing system.
- [See to Touch: Learning Tactile Dexterity through Visual Incentives](https://arxiv.org/abs/2309.12300) | source type: primary paper | why used: Used for the TAVI framework, six-task real-robot evaluation, and 73-percent success plus relative-improvement claims.
- [See to Touch project page](https://see-to-touch.github.io/) | source type: official project page | why used: Used for task list, videos, and code availability.
- [AcTExplore: Active Tactile Exploration of Unknown Objects](https://arxiv.org/abs/2310.08745) | source type: primary paper | why used: Used for RL-driven unknown-object exploration and the 95.97-percent unseen-YCB IoU coverage result.
- [AcTExplore project page](https://prg.cs.umd.edu/AcTExplore) | source type: official project page | why used: Used for code availability and project-level description.
- [Touch begins where vision ends: Generalizable policies for contact-rich manipulation](https://arxiv.org/abs/2506.13762) | source type: primary paper | why used: Used for the ViTaL formulation, residual-RL generalization claims, and around-90-percent success in unseen environments.
- [ViTaL project page](https://vitalprecise.github.io/) | source type: official project page | why used: Used for videos and project-level explanation of the localize-then-execute pipeline.
- [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2603.19201) | source type: primary paper | why used: Used for the world-model architecture, OmniViTac dataset scale, unseen-object generalization claims, and release statement.
- [Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation](https://arxiv.org/abs/2601.02778) | source type: primary paper | why used: Used for the 2026 actor-critic tactile sim-to-real dexterous manipulation direction and zero-shot transfer claim.
- [PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation](https://arxiv.org/abs/2603.04531) | source type: primary paper | why used: Used for latent distillation, 182-percent and 57-percent improvement claims, and the no-tactile-simulation transfer strategy.
- [Active Tactile Object Exploration with Gaussian Processes](https://flipveiga.github.io/publication/yi2016active/) | source type: primary paper page | why used: Used as a foundational pre-2021 precursor for uncertainty-driven next-touch planning.
- [Exploratory Tactile Servoing With Active Touch](https://research-information.bris.ac.uk/ws/files/102887809/Nathan_Lepora_Exploratory_tactile_servoing_with_active_touch.pdf) | source type: primary paper PDF | why used: Used as a foundational pre-2021 precursor for tactile action-perception loops.
- [Manipulation by Feel: Touch-Based Control with Deep Predictive Models](https://arxiv.org/abs/1903.04128) | source type: primary paper | why used: Used as a pre-2021 precursor for model-based tactile control and predictive tactile dynamics.
- [On Policy Learning Robust to Irreversible Events: An Application to Robotic In-Hand Manipulation](https://arxiv.org/abs/1911.08927) | source type: primary paper | why used: Used as a pre-2021 precursor for combining RL with tactile reactive control to avoid slip and failures.
