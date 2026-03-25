---
title: "Tactile-guided reaching contact localization and active haptic exploration of unknown objects"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23, including 2026 preprints available by 2026-03-23."
---

# Tactile-guided reaching contact localization and active haptic exploration of unknown objects

## Scope
This subtopic covers methods that use tactile sensing, usually together with proprioception and sometimes vision, to localize unknown rigid object surfaces, salient contact features, object pose, or extrinsic contact locations while the robot is interacting with the object. Included systems close the loop by choosing informative touches, sliding or rotating over the surface, or using the localized contact geometry to drive a downstream reach, insertion, or contact-rich manipulation behavior on previously unseen objects. The boundary excludes pure tactile classification, grasp-stability prediction without geometric localization, deformable-object exploration, and methods that require a fully known object-specific codebook or CAD model at deployment unless they are cited only as adjacent background.

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The main quantitative claims that make this note important to your use case are now re-checked, but some secondary tactile-localization results remain pending.

### Re-checked Claims
- AcTExplore: 95.97% average IoU coverage on unseen YCB objects (`verified-primary-pdf`).
- NeuralFeels: 81% final reconstruction F-score, 4.7 mm pose drift, 2.3 mm with known CAD, and up to 94% better tracking under occlusion (`verified-primary-pdf`).
- Touch2Insert: sub-millimeter simulation pose estimation and 86.7% average real-robot insertion success (`verified-primary-pdf`).
- TacLoc is re-checked as a YCB-evaluated registration-based tactile-localization paper, but no headline numeric gain is currently relied on in the synthesis (`verified-primary-abstract`).

### Still Pending
- Curiosity-driven tSLAM timing and transfer numbers still need a stricter table-focused pass.
- Additional localization and extrinsic-contact metrics outside the shortlist remain partially audited.

## Inclusion Criteria
- Primary papers or official project pages within the window whose main contribution is tactile or visuo-tactile localization, pose estimation, surface reconstruction, extrinsic contact localization, or active touch planning for unknown or previously unseen rigid objects.
- Methods that explicitly reduce pose or surface uncertainty through touch, choose next-touch actions, or use localized tactile geometry to guide a controlled reach or insertion behavior.
- Real-robot or simulation studies are included when the paper states unknown-object or unseen-object evaluation, or when the method is clearly designed for object-agnostic deployment.

## Exclusion Criteria
- Pure tactile object recognition, texture recognition, grasp quality prediction, or contact classification without geometric localization or exploration.
- Deformable-object exploration, whole-body skin contact monitoring, and non-manipulation haptics.
- Known-object tactile localization papers such as Tac2Pose and MidasTouch are only used as boundary-setting context because they rely on object-specific geometry or codebooks at deployment rather than unknown-object generalization.

## Problem Formulations
- Online joint estimation of unknown object shape and pose from a stream of tactile contacts during planar pushing or in-hand interaction.
- Closed-loop unknown-object 6-DoF localization and 3D reconstruction from visuo-tactile feedback with loop closure or pose-graph optimization.
- Active tactile exploration for surface coverage or reconstruction, where the policy chooses the next touch to maximize coverage or reduce uncertainty.
- Extrinsic contact localization on a grasped object, where touch and motion cues are used to infer where the environment contacts the object.
- One-shot or few-shot tactile localization from local geometry followed by a downstream reach, insertion, or contact-rich manipulation action on unseen geometry.

## Sensing Modalities
- Dense vision-based tactile sensors such as GelSight, DIGIT, and GelSlim-style fingertips dominate the literature because they provide local surface geometry as images or point clouds.
- Robot kinematics and proprioception are used nearly everywhere to transform local contacts into object-frame or world-frame constraints.
- RGB or RGB-D wrist or external cameras are fused with touch in FingerSLAM, NeuralFeels, and ViTaSCOPE to stabilize global pose estimates under partial occlusion.
- Some systems are touch-only, including Tactile SLAM in planar pushing, curiosity-driven tSLAM, AcTExplore, TacLoc, and Touch2Insert after contact is made.
- Force, shear, and motion-consistency cues appear indirectly through tactile image sequences, distributed tactile motion, or shear-field modeling rather than as standalone force-torque pipelines.

## Action Space And Robot Setup
- Planar pushing along an unknown contour with a tactile probe or pusher for simultaneous mapping and pose estimation.
- Anthropomorphic or multi-fingered hands that slide, roll, and re-contact the object to collect local tactile depth maps.
- In-hand exploration with one or more tactile fingertips plus a wrist camera, often on dexterous hands holding a single object.
- Bimanual setups where one hand stabilizes the object and the other performs active tactile exploration to refine pose.
- Single-contact probing followed by registration-guided insertion in peg-hole or connector tasks.
- Robot embodiments are mostly research manipulators with rigid grippers or dexterous hands in highly instrumented tabletop scenes rather than mobile or cluttered field robots.

## Method Families
- SLAM-style geometric inference: joint pose-shape estimation with GPIS, factor graphs, loop closure, or fixed-lag smoothing.
- Learned active exploration: reinforcement learning or curiosity-driven policies that choose where to touch next for maximal information gain or coverage.
- Visuo-tactile neural representations: neural fields, implicit SDFs, and dense fusion networks that use touch to correct occluded visual pose estimates.
- Registration-centric localization: one-shot or incremental partial-to-full registration between tactile point clouds and unknown or minimally parameterized object models.
- Task-oriented contact exploitation: using localized tactile geometry to drive insertion or other contact-rich skills after one or a few touches.

## Representative System Pipelines
- SLAM-style tactile mapping
  - pipeline: Tactile contact stream -> local surface estimate -> factor-graph pose update -> nonparametric shape update -> repeat during pushing or exploration.
  - examples: Tactile SLAM; FingerSLAM
- RL-driven active surface coverage
  - pipeline: Current tactile map or tactile-history state -> exploration policy -> next fingertip motion -> new local tactile depth -> fused surface reconstruction.
  - examples: Curiosity-Driven Self-supervised Tactile Exploration; AcTExplore; Object Pose Estimation through Dexterous Touch
- Visuo-tactile implicit tracking
  - pipeline: Vision segmentation and tactile depth estimation -> online neural object field -> pose-graph or optimization backend -> improved pose/contact estimate under occlusion.
  - examples: NeuralFeels; ViTaSCOPE
- Registration for downstream control
  - pipeline: One or few tactile contacts -> partial geometry reconstruction -> registration against object or task geometry -> direct control action such as insertion.
  - examples: TacLoc; Touch2Insert

## Evaluation Tasks
- Unknown-object shape reconstruction from tactile-only exploration.
- 6-DoF pose estimation of unseen in-hand objects.
- Extrinsic contact localization on grasped objects under occlusion.
- Active exploration efficiency, measured by how quickly coverage or useful pose features are acquired.
- Downstream contact-rich execution such as peg or connector insertion after tactile localization.

## Common Metrics
- Surface reconstruction quality: IoU coverage, F-score, point-cloud or mesh accuracy.
- Pose-estimation quality: translation drift, pose-estimation accuracy in millimeters, and sometimes rotation error.
- Task success: insertion success rate or completion of downstream manipulation objective.
- Exploration efficiency: number of contacts, interaction time, or reaching adequate reconstruction within a short horizon.
- Generalization split quality: performance on unseen objects or cross-dataset transfer.

## Best Reported Capabilities
- AcTExplore reports 95.97% average IoU coverage on unseen YCB objects while training only on primitive shapes, showing strong object-agnostic surface coverage from active touch.
- NeuralFeels reports 81% final reconstruction F-score, 4.7 mm average pose drift, 2.3 mm with known CAD models, and up to 94% tracking improvement over vision-only baselines under heavy occlusion.
- FingerSLAM demonstrates real-world visuo-tactile 6-DoF localization and reconstruction on 6 unseen objects after training on data from 20 objects.
- Curiosity-driven tSLAM reports reconstruction of objects of varying complexity within 6 seconds of touch-only interaction and cross-dataset transfer from 3D Warehouse training to ContactDB testing.
- Touch2Insert reports sub-millimeter pose estimation accuracy in simulation for all tested connectors and an 86.7% average real-robot insertion success rate across three diverse connectors.

## Failure Modes And Limitations
- Most systems remain restricted to single-object, rigid-object, or in-hand settings with controlled contact and limited clutter.
- Dense tactile sensing provides only local geometry, so global localization is ambiguous without repeated contact, loop closure, or auxiliary vision.
- Active exploration policies are often trained in simulation and evaluated on relatively small object sets; scaling to larger shape diversity and contact conditions remains unclear.
- Methods that reconstruct shape online can be slow or contact-budget limited, making them hard to deploy for time-critical reaching tasks.
- Registration-based approaches depend on informative local geometry; symmetric or weakly distinctive contacts remain ambiguous.
- Downstream task success is still demonstrated on narrow families such as handheld unknown objects or a few connector types rather than broad open-world manipulation.

## Representative Papers
- [[Paper - Tactile SLAM: Real-time inference of shape and pose from planar pushing|Tactile SLAM: Real-time inference of shape and pose from planar pushing]] (2021, ICRA 2021)
- [[Paper - Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects|Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects]] (2022, arXiv preprint)
- [[Paper - FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback|FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback]] (2023, ICRA 2023)
- [[Paper - AcTExplore: Active Tactile Exploration of Unknown Objects|AcTExplore: Active Tactile Exploration of Unknown Objects]] (2024, ICRA 2024)
- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation|Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]] (2024, Science Robotics)
- [[Paper - Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors|Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors]] (2025, arXiv preprint)
- [[Paper - ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation|ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation]] (2025, RSS 2025)
- [[Paper - Object Pose Estimation through Dexterous Touch|Object Pose Estimation through Dexterous Touch]] (2025, arXiv preprint)
- [[Paper - Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole|Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole]] (2026, ICRA 2026)
- [[Paper - TacLoc: Global Tactile Localization on Objects from a Registration Perspective|TacLoc: Global Tactile Localization on Objects from a Registration Perspective]] (2026, arXiv preprint)

## Trends 2021 To 2026
- The field moves from tactile-only geometric inference in constrained settings toward multimodal visuo-tactile tracking that explicitly handles heavy visual occlusion.
- Active exploration becomes more learned: curiosity and RL increasingly replace fixed probing strategies, especially for large unknown surfaces.
- Representations shift from explicit local geometric models such as GPIS and stitched point clouds toward neural fields, implicit surfaces, and registration pipelines.
- Recent work increasingly targets object-agnostic deployment, explicitly criticizing object-specific rendered databases or pre-trained codebooks.
- There is a gradual move from pure reconstruction toward task-conditioned use of localized contact geometry, especially insertion and extrinsic contact reasoning.
- Benchmarking is improving, but the subtopic still lacks a single accepted end-to-end benchmark covering localization, exploration efficiency, and downstream manipulation success on unseen objects.

## Research Gaps
- Standardized benchmarks for unknown-object tactile localization that combine geometry accuracy, uncertainty reduction, and downstream task success are still missing.
- Most methods assume rigid, isolated objects and stable contact; clutter, slip, articulation, and deformability remain underexplored.
- The community lacks strong comparisons between learned exploration policies and explicit information-gain or uncertainty-reduction planners under matched conditions.
- Global ambiguity from local tactile geometry is still a core failure mode for symmetric or low-feature surfaces.
- Real-time performance under strict contact budgets is underreported, which matters for practical reaching and manipulation pipelines.
- Few methods integrate tactile exploration with grasp acquisition and retreat planning in one unified loop for a single manipulator.
- 2026 work suggests a move toward registration-based object-agnostic localization, but robust large-scale real-world validation is still limited.

## Opportunities For Single Manipulator Systems
- A practical near-term architecture is a wrist RGB-D camera plus one dense fingertip tactile sensor, with tactile updates used only when vision becomes occluded or uncertain.
- Registration-based first-touch localization, as seen in TacLoc and Touch2Insert, looks promising for single-arm reaching, insertion, button pressing, and edge finding because it can convert a small number of contacts into an immediate geometric correction.
- Uncertainty-aware next-best-touch planners using minimal visual priors appear attractive for one-arm systems because they avoid the data and training burden of large RL policies while still exploiting tactile geometry.
- SLAM-like backends remain useful when repeated contacts are available; a single manipulator can reuse FingerSLAM and NeuralFeels ideas with a simpler object-centric factor graph or neural SDF.
- The best experimental target for a single manipulator is likely unknown rigid household or industrial parts in semi-structured scenes, where touch can resolve the final few millimeters of pose uncertainty that vision leaves behind.

## Sources
- [Tactile SLAM: Real-time inference of shape and pose from planar pushing](https://arxiv.org/abs/2011.07044) | source type: primary paper | why used: Used for the SLAM-style unknown-object mapping formulation, ICRA 2021 venue, and planar-pushing setup.
- [Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects](https://arxiv.org/abs/2204.00035) | source type: primary paper | why used: Used for touch-only active exploration, 6-second reconstruction claim, and 3D Warehouse to ContactDB generalization.
- [FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback](https://arxiv.org/abs/2303.07997) | source type: primary paper | why used: Used for unseen-object in-hand localization and reconstruction, factor graph, loop closure, and object counts.
- [AcTExplore: Active Tactile Exploration of Unknown Objects](https://arxiv.org/abs/2310.08745) | source type: primary paper | why used: Used for active exploration method description and ICRA 2024 acceptance.
- [AcTExplore official project page](https://prg.cs.umd.edu/AcTExplore) | source type: official project page | why used: Used for code availability and the 95.97% IoU coverage claim on unseen YCB objects.
- [Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation](https://arxiv.org/abs/2312.13469) | source type: primary paper | why used: Used for neural-field formulation, quantitative reconstruction and pose-drift numbers, and FeelSight dataset release.
- [NeuralFeels official project page](https://suddhu.github.io/neural-feels/) | source type: official project page | why used: Used for Science Robotics venue, code availability, dataset availability, and benchmark-positioning statements.
- [Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors](https://arxiv.org/abs/2505.11975) | source type: primary paper | why used: Used for explicit uncertainty-minimization and minimal-visual-prior active exploration claims.
- [ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation](https://arxiv.org/abs/2506.12239) | source type: primary paper | why used: Used for simultaneous in-hand pose and extrinsic contact estimation and RSS 2025 acceptance.
- [ViTaSCOPE official project page](https://jayjunlee.github.io/vitascope/) | source type: official project page | why used: Used for RSS 2025 venue confirmation and code-coming-soon reproducibility note.
- [Object Pose Estimation through Dexterous Touch](https://arxiv.org/abs/2509.13591) | source type: primary paper | why used: Used for active bimanual tactile exploration without prior object geometry.
- [TacLoc: Global Tactile Localization on Objects from a Registration Perspective](https://arxiv.org/abs/2603.10565) | source type: primary paper | why used: Used for 2026 registration-based object-agnostic tactile localization and YCB evaluation.
- [Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole](https://arxiv.org/abs/2603.03627) | source type: primary paper | why used: Used for 2026 tactile-guided insertion, zero-shot claim, sub-millimeter simulation accuracy, and 86.7% real success rate.
- [Tac2Pose: Tactile Object Pose Estimation from the First Touch](https://arxiv.org/abs/2204.11701) | source type: primary paper | why used: Used only to define the boundary between known-object tactile localization and the unknown-object focus of this review.
- [MidasTouch: Monte-Carlo inference over distributions across sliding touch](https://arxiv.org/abs/2210.14210) | source type: primary paper | why used: Used only as adjacent context for global tactile localization that still relies on per-object codebooks.
- [Localizing a polyhedral object in a robot hand by integrating visual and tactile data](https://www.sciencedirect.com/science/article/abs/pii/S003132039900059X) | source type: primary paper | why used: Used as an early precursor for tactile-visual localization under occlusion.
- [Correcting pose estimates during tactile exploration of object shape: a neuro-robotic study](https://ieeexplore.ieee.org/document/6982950/) | source type: primary paper | why used: Used as a precursor for joint tactile shape learning and pose-drift correction.
- [Active Tactile Object Exploration with Gaussian Processes](https://flipveiga.github.io/publication/yi2016active/) | source type: official paper page | why used: Used as a precursor for uncertainty-driven next-touch planning over object surfaces.
- [Exploratory Tactile Servoing With Active Touch](https://research-information.bris.ac.uk/ws/files/102887809/Nathan_Lepora_Exploratory_tactile_servoing_with_active_touch.pdf) | source type: primary paper PDF | why used: Used as a precursor for closed-loop tactile perception-and-control during exploration.
