---
title: "Force feedback impedance control contour following and compliant contact exploration"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23, including 2026 preprints available by 2026-03-23."
---

# Force feedback impedance control contour following and compliant contact exploration

## Scope
This subtopic covers robot methods that deliberately maintain or exploit physical contact to trace surfaces, follow contours, reconstruct local geometry, or complete contact-rich manipulation on unknown or partially unknown objects. Included methods use force/torque sensing, tactile sensing, proprioception, compliance, admittance or impedance control, hybrid force-position control, or learned equivalents that explicitly regulate contact while exploring or manipulating geometry. The boundary excludes vision-only geometry exploration, non-contact inspection, and generic assembly papers that do not use contact feedback to regulate exploration, contour following, or safe interaction with uncertain geometry.

## Claim Status
> [!info] Verification state
> Overall status: `early-quantitative-audit`
> Summary: This note now has multiple verified 2025-2026 force-aware VLA anchors, but the broader local-control literature still needs a heavier table-by-table pass than the shortlist required.

### Re-checked Claims
- ForceVLA: 23.2% average task-success improvement over strong pi0-based baselines and up to 80% success on plug insertion (`verified-primary-abstract`).
- ForceVLA2: 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks, with gains still reaching 35.0% on fragile-object tasks (`verified-primary-abstract`).
- CompliantVLA-adaptor: overall success on contact-rich tasks improves from 9.86% to 17.29% with compliance augmentation (`verified-primary-abstract`).
- Tactile Gym 2.0 benchmark framing for edge following, surface following, and object pushing is re-checked (`verified-primary-pdf`).

### Still Pending
- Force Policy remains qualitative-only because the local PDF extraction failed in this pass.
- Several contour-following, tool-use, and force-regulation accuracy numbers remain to be re-audited from the original tables.

## Inclusion Criteria
- Papers and system demonstrations in the requested window that use force, torque, tactile, proximity, and/or proprioceptive feedback to maintain sustained contact with unknown or partially unknown geometry.
- Methods with explicit impedance, admittance, hybrid force-position, variable compliance, or learned force-aware control for contour following, surface following, shape reconstruction, wiping, opening, insertion, or similar contact-rich tasks.
- Primary-source records were prioritized: arXiv abstract pages, official publisher pages, official conference or journal records, and official project pages.

## Exclusion Criteria
- Vision-only object exploration, grasp planning, or mapping without closed-loop contact regulation.
- Purely theoretical force-control papers with no clear tie to surface tracing, compliant exploration, or safe manipulation of uncertain geometry.
- General contact-rich manipulation papers that treat force only as an auxiliary signal but do not make contact maintenance, contour following, or compliant exploration a substantive part of the method.
- Mobile navigation, aerial or underwater path-following, and non-manipulation settings unless the paper directly addresses tactile or force-based contour following.

## Problem Formulations
- Surface following or edge following with regulation of contact pose, normal force, or shear during continuous motion.
- Dynamic contour following in which the object moves and the controller must both track motion and continue tactile exploration.
- Active tactile exploration for contour or shape reconstruction under local geometric uncertainty.
- Tool-mediated surface following, wiping, polishing, or scraping where the contact state and applied force must be inferred and stabilized.
- Force-guided contact establishment and force-limited insertion or assembly under pose uncertainty.
- Learning compliant or variable-impedance behaviors from demonstrations for stable force regulation in unknown environments.
- Modern multimodal policies that split long-horizon vision guidance from high-rate force-aware local interaction control.

## Sensing Modalities
- Wrist or end-effector force/torque sensing, sometimes estimated rather than directly measured, is central in FORGE, Force Policy, Direction Matters, ForceVLA2, and compliant force-control papers.
- High-resolution optical tactile sensing is dominant in the Bristol tactile-servoing line: TacTip, DIGIT, and DigiTac are used for edge following, surface following, object tracking, and pushing.
- Shear-sensitive tactile perception is explicitly used in pose-and-shear tactile servoing and in dynamic contour following, where shear minimization stabilizes contact.
- Vision is typically used for task context, object localization, or long-horizon guidance rather than fine local regulation in the more recent multimodal papers.
- Proprioception and Cartesian pose history are used broadly for controller state, contact-state estimation, and switching logic.
- Specialized contact sensors also appear, such as whisker-inspired tactile sensors for contour reconstruction and proximity+tactile sensing for tool-use transfer.

## Action Space And Robot Setup
- Most systems use a single 6- or 7-DoF arm with either a wrist F/T sensor, a tactile fingertip, or a tool instrumented with tactile or proximity sensing.
- Tactile Gym 2.0 deliberately lowers the hardware barrier by using a low-cost 4-DoF desktop arm for sim-to-real edge following, surface following, and object pushing.
- Pose-and-shear tactile servoing and dynamic contour following use Cartesian velocity control in SE(3) with closed-loop tactile state estimation.
- Force-aware manipulation papers typically command Cartesian pose deltas together with force targets, controller modes, or admittance/impedance parameters.
- Tool-use transfer uses a Franka arm and multimodal sensing to adapt surface-following behaviors across brushes, a broom, and a sponge.
- Some papers include dual-arm setups or bimanual variants, but the dominant embodiment in this subtopic is still a single manipulator performing local contact exploration.

## Method Families
- Classical and adaptive compliant control: impedance, admittance, and hybrid force-position control remain the base layer for safe sustained contact.
- Tactile servoing: optical tactile or whisker sensing is turned into local pose, shear, or contact-point estimates that drive continuous surface-following control.
- Sim-to-real tactile learning: simulation environments such as Tactile Gym 2.0 train policies for edge following and surface following before transferring them to real hardware.
- Demonstration-driven compliance learning: human demonstrations are used to infer variable impedance or optimal task frames for contact-rich control.
- Active exploration under uncertainty: the robot chooses informative next contacts to reduce reconstruction uncertainty while limiting contact risk.
- Multimodal force-aware policy learning: newer work separates global vision reasoning from high-rate local force control and often introduces explicit force-aware prompts, interaction frames, or force-direction predictions.

## Representative System Pipelines
- Tactile Gym 2.0: train deep RL policies in simulation on tactile images for edge following and surface following, translate tactile imagery across sensor domains, then transfer policies directly to real sensors and a desktop robot without task-specific fine-tuning.
- Tac-VGNN and follow-on tactile servoing: infer local pose and depth from tactile marker motion and Voronoi features, then drive a tactile servo controller that follows surfaces more smoothly than earlier discrete schemes.
- Pose-and-shear tactile servoing plus dynamic contour following: estimate both contact pose and shear, filter the state in SE(3), use shear-minimizing tracking during object motion, and switch into tactile exploration modes to continue contour following.
- Few-shot tool-use transfer: pre-train in simulation to recognize contact states, then fine-tune with a small number of human demonstrations so a single-arm robot can follow new surfaces with diverse tools and adapt to incline changes or mild deformability.
- FORGE: learn force-threshold-conditioned policies in simulation under dynamics randomization, deploy on real contact-rich tasks, predict task success online, and tune allowable force automatically for uncertain forceful interactions.
- Proactive tactile exploration: start from a minimal visual prior, fit and refine a mesh from sequential contacts, choose the next touch to reduce uncertainty while lowering contact-failure risk, and update the reconstruction iteratively.
- Direction Matters and Force Policy: use vision for task progress in free space, then switch to force-aware local control where the policy predicts force direction, contact state, or an interaction frame that configures admittance or hybrid force-position control.
- ForceVLA2: fuse multi-view vision, language, proprioception, and force prompts, then output action chunks, force objectives, control modes, and task progress for closed-loop hybrid force-position manipulation.

## Evaluation Tasks
- Edge following and surface following on rigid objects.
- Dynamic contour following and moving-object tracking.
- Object pushing and non-prehensile manipulation under sustained contact.
- Shape or contour reconstruction from tactile contact sequences.
- Tool-mediated surface following, wiping, painting, pressing, and scraping.
- Peg insertion, nut threading, gear meshing, snap-fit insertion, and related force-sensitive assembly tasks.
- Door opening, microwave opening, articulated-object manipulation, and retrieval under contact.
- Single-arm and occasional dual-arm contact-rich tasks with disturbances or geometric shifts.

## Common Metrics
- Task success rate or completion rate.
- Contour-following or tracking accuracy in millimeters.
- Force tracking error, force regulation quality, or compliance stability.
- Tactile pose-estimation error, depth error, or contact-state accuracy.
- Shape or contour reconstruction error, sometimes reported as sub-millimeter geometric accuracy.
- Robustness under disturbances, geometric shifts, or unseen objects and tools.
- Safety-related metrics such as force-threshold violations, overload events, or safety stops.
- Data efficiency metrics such as number of demonstrations or sim-to-real transfer without additional fine-tuning.

## Best Reported Capabilities
- Dynamic contour following can follow moving objects with sub-millimeter accuracy over an approximately 72 mm range across five tested velocities in 2D, according to Aquilina et al. 2024.
- Whisker-based active tactile perception reports sub-millimeter contour-reconstruction accuracy while maintaining stable surface following on three objects in both simulation and real experiments.
- Tac-VGNN reports a 28.57% improvement in vertical-depth pose estimation over a vanilla GNN baseline and smoother real surface-following trajectories.
- Few-shot transfer of tool-use skills demonstrates surface following across tools with different geometry and physical properties, plus adaptation to changing inclination, deformable surfaces, and external disturbances.
- FORGE shows that force-threshold-conditioned policies can safely perform uncertain forceful tasks such as snap-fit insertion while also predicting task success for efficient stopping and automatic threshold tuning.
- ForceVLA reports a 23.2% average task-success improvement over strong pi0-based baselines and up to 80% success on plug insertion, making it an important 2025 precursor to the force-aware VLA line rather than a 2026-only story.
- Direction Matters demonstrates strong real-world robustness on microwave opening, peg-in-hole, whiteboard wiping, and door opening by predicting force direction rather than force magnitude.
- ForceVLA2 reports 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks, with gains still reaching 35.0% on fragile-object tasks where contact stability matters most.
- CompliantVLA-adaptor reports that compliance augmentation improves overall success on contact-rich tasks from 9.86% to 17.29%, making compliance an explicit VLA adaptation axis rather than only a downstream controller knob.
- FD-VLA argues that a distilled force token can outperform direct force sensing in physical experiments, widening the force-aware VLA design space beyond hardware-force-at-inference.

## Failure Modes And Limitations
- Sim-to-real mismatch in contact dynamics remains a core failure mode, especially for force magnitude prediction, frictional transitions, and contact transients.
- Many controllers still require manually chosen force magnitudes, phase thresholds, or switching logic even when the force direction or interaction frame is learned.
- Local tactile exploration can lose contact on high-curvature or sharp surfaces, enter tangential slip, or get trapped in local exploration minima.
- Most experiments are local and task-specific; few systems autonomously explore an entire unknown object in clutter or with broad material variation.
- Benchmarking is fragmented: Tactile Gym 2.0 is reusable, but many later systems use bespoke task suites that make direct comparison difficult.
- Whole-object reconstruction from contact remains slow because tactile information is local and contact placement must trade off information gain against safety.
- Reproducibility is uneven: some influential project pages exist without mature code or data releases as of 2026-03-23.
- The newest 2026 multimodal force-aware policies are promising but still limited to small real-robot task suites and curated perturbation settings.

## Representative Papers
- [[Paper - Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch|Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch]] (2022, IEEE Robotics and Automation Letters)
- [[Paper - Tac-VGNN: A Voronoi Graph Neural Network for Pose-Based Tactile Servoing|Tac-VGNN: A Voronoi Graph Neural Network for Pose-Based Tactile Servoing]] (2023, ICRA 2023)
- [[Paper - A pose and shear-based tactile robotic system for object tracking, surface following and object pushing|A pose and shear-based tactile robotic system for object tracking, surface following and object pushing]] (2023, Preprint)
- [[Paper - Learning compliant dynamical system from human demonstrations for stable force control in unknown environments|Learning compliant dynamical system from human demonstrations for stable force control in unknown environments]] (2024, Robotics and Computer-Integrated Manufacturing)
- [[Paper - Tactile control for object tracking and dynamic contour following|Tactile control for object tracking and dynamic contour following]] (2024, Robotics and Autonomous Systems)
- [[Paper - Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks|Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks]] (2026, Robotics and Autonomous Systems)
- [[Paper - FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty|FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty]] (2025, IEEE Robotics and Automation Letters)
- [[Paper - Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing|Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing]] (2025, IEEE Robotics and Automation Letters)
- [[Paper - Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors|Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors]] (2025, Preprint)
- [[Paper - Whisker-based Active Tactile Perception for Contour Reconstruction|Whisker-based Active Tactile Perception for Contour Reconstruction]] (2025, Preprint)
- [[Paper - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation|ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (2025, NeurIPS 2025 / arXiv)

## Trends 2021 To 2026
- The field moved from local tactile servoing and surface following toward more complete force-aware manipulation pipelines that combine contact control with higher-level planning.
- There is a clear transition from fixed or manually tuned compliant controllers toward learned interaction structure: task frames, interaction frames, contact states, force directions, and multimodal force prompts.
- Static rigid-surface experiments are giving way to moving objects, articulated objects, variable inclination, mild deformability, and explicit disturbance tests.
- Sim-to-real methods improved substantially, especially through tactile simulators, dynamics randomization, and policy decompositions that reserve force for high-rate local control.
- Tool-mediated contact tasks became more prominent, reflecting real application needs such as wiping, polishing, and scraping rather than only direct fingertip contour following.
- Despite progress, evaluation remains fragmented and local: benchmarked, whole-object autonomous contact exploration in clutter still lags behind progress in curated task suites.

## Research Gaps
- Whole-object autonomous exploration with compliant contact is still underdeveloped; most work follows a local contour or task surface rather than building complete object understanding.
- Shared real-world benchmarks for force-aware exploration are scarce, making it hard to compare exploration efficiency, safety, and generalization across labs.
- The field still lacks strong methods for highly deformable, fragile, or mixed-material surfaces where local geometry and safe force envelopes change rapidly.
- Contact-state estimation and controller switching remain brittle around discontinuities such as edges, holes, corners, and sudden friction changes.
- Many systems need manual force magnitudes or task-specific tuning; learning safe magnitudes online remains much less mature than learning direction or contact phase.
- Closed-loop integration of visual global geometry with tactile or force local exploration remains limited, especially for cluttered multi-object scenes.
- Reproducibility is constrained by specialized tactile hardware, limited open datasets, and incomplete releases for several high-profile 2025-2026 systems.

## Opportunities For Single Manipulator Systems
- A single arm with an eye-in-hand camera and wrist F/T sensor can already exploit the strongest current ideas: global visual targeting, explicit force-threshold safety, and local admittance or hybrid force-position regulation.
- If tactile hardware is available, the most practical near-term path is to pair a simple tactile servoing controller with a reusable simulator such as Tactile Gym 2.0 and then adapt on real surfaces.
- For tool-mediated tasks, the strongest opportunity is to learn contact-state abstractions or force directions rather than raw force magnitudes, because those signals appear more transferable across geometry changes.
- Minimal-visual-prior plus proactive tactile exploration is promising for unknown objects when the goal is not full dexterity but safe surface discovery for grasping, wiping, or inspection.
- Interaction-frame or task-frame representations are especially attractive for single-arm systems because they reduce controller design complexity and make force regulation more geometry-aware.
- A practical research stack for one manipulator is: visual object hypothesis, guarded contact with force threshold, local frame estimation, compliant contour following or probing, uncertainty-based next-touch selection, and explicit stopping when either task success or shape-confidence criteria are met.

## Sources
- [Tactile Gym 2.0 project page](https://sites.google.com/view/tactile-gym-2) | type: official project page | year: 2022 | notes: Source for benchmark tasks, supported tactile sensors, sim-to-real transfer claims, and code availability.
- [Tactile Gym 2.0 arXiv page](https://arxiv.org/abs/2207.10763) | type: arXiv abstract page | year: 2022 | notes: Primary paper source for edge following and surface following benchmark formulation.
- [Tac-VGNN arXiv page](https://arxiv.org/abs/2303.02708) | type: arXiv abstract page | year: 2023 | notes: Source for pose-based tactile servoing and reported depth-estimation improvement with smoother real surface following.
- [Pose and shear-based tactile robotic system arXiv page](https://arxiv.org/abs/2306.08560) | type: arXiv abstract page | year: 2023 | notes: Primary source for continuous tactile object tracking, surface following, and object pushing.
- [Pose and shear-based tactile robotic system Zenodo record](https://zenodo.org/records/7835928) | type: official preprint record | year: 2023 | notes: Supplementary primary source with metadata and downloadable preprint.
- [Tactile control for object tracking and dynamic contour following](https://doi.org/10.1016/j.robot.2024.104710) | type: journal DOI page | year: 2024 | notes: Primary publication record for dynamic contour following, moving-object tracking accuracy, and switching-controller design.
- [University of Bristol publication record for dynamic contour following](https://research-information.bris.ac.uk/en/publications/tactile-control-for-object-tracking-and-dynamic-contour-following/) | type: official university publication page | year: 2024 | notes: Source for bibliographic metadata and abstract text.
- [Learning compliant dynamical system from human demonstrations for stable force control in unknown environments](https://www.sciencedirect.com/science/article/pii/S0736584523001448) | type: official journal page | year: 2024 | notes: Primary source for human-demonstration-based variable compliance in unknown environments.
- [Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks](https://arxiv.org/abs/2404.01900) | type: arXiv abstract page | year: 2024 | notes: Source for task-frame derivation from motion and wrench data, including validation on surface following.
- [FORGE arXiv page](https://arxiv.org/abs/2408.04587) | type: arXiv abstract page | year: 2024 | notes: Primary source for force-threshold-conditioned exploration, success prediction, and robust contact-rich manipulation under uncertainty.
- [FORGE project page](https://noseworm.github.io/forge/) | type: official project page | year: 2025 | notes: Source for task descriptions, project media, and emphasis on uncertain forceful interactions such as snap-fit insertion.
- [Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing](https://sony.github.io/tool-use-few-shot-transfer/) | type: official project page | year: 2025 | notes: Primary source for multimodal tool-use surface-following transfer, adaptation to deformable surfaces, and few-shot demonstration requirements.
- [Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors](https://arxiv.org/abs/2505.11975) | type: arXiv abstract page | year: 2025 | notes: Primary source for uncertainty-driven tactile contact selection and iterative shape reconstruction.
- [Whisker-based Active Tactile Perception for Contour Reconstruction](https://arxiv.org/abs/2507.23305) | type: arXiv abstract page | year: 2025 | notes: Primary source for active whisker-based contour following and sub-millimeter contour reconstruction.
- [Direction Matters project page](https://yifei-y.github.io/project-pages/DirectionMatters/) | type: official project page | year: 2026 | notes: Source for task list, force-aware admittance-control interpretation, robustness claims, and code availability.
- [Direction Matters arXiv page](https://arxiv.org/abs/2602.14174) | type: arXiv abstract page | year: 2026 | notes: Primary source for learning force direction and sim-to-real contact-rich manipulation.
- [Force Policy arXiv page](https://arxiv.org/abs/2602.22088) | type: arXiv abstract page | year: 2026 | notes: Primary source for interaction-frame-based hybrid force-position control policy learning.
- [Force Policy project page](https://force-policy.github.io/) | type: official project page | year: 2026 | notes: Source for interaction-frame explanation, task descriptions, force-control evaluation, and code-coming-soon status.
- [ForceVLA2 arXiv page](https://arxiv.org/abs/2603.15169) | type: arXiv abstract page | year: 2026 | notes: Primary source for the force-aware VLA formulation, dataset size, task coverage, and reported gains over pi0 and pi0.5.
- [ForceVLA2 project page](https://sites.google.com/view/force-vla2/home) | type: official project page | year: 2026 | notes: Source for control outputs, dataset description, real-task set, and code-and-dataset-coming-soon status.
- [FD-VLA arXiv page](https://arxiv.org/abs/2602.02142) | type: arXiv abstract page | year: 2026 | notes: Primary source for force-token distillation and the claim that distilled force can outperform direct force sensing in physical experiments.
- [CompliantVLA-adaptor arXiv page](https://arxiv.org/abs/2601.15541) | type: arXiv abstract page | year: 2026 | notes: Primary source for compliance augmentation in VLAs and the reported success-rate improvement from 9.86% to 17.29% on contact-rich tasks.
- [Impedance Control: An Approach to Manipulation: Part I-Theory](https://newmanlab.mit.edu/wp-content/uploads/2017/09/1985-impedance-control-an-approach-to-manipulation-part-I-theory.pdf) | type: paper PDF | year: 1985 | notes: Foundational precursor for compliant interaction control.
- [Dynamic hybrid position/force control of robot manipulators-on-line estimation of unknown constraint](https://ieeexplore.ieee.org/document/238286/) | type: official journal page | year: 1993 | notes: Foundational precursor for hybrid position-force control on unknown constraints.
- [Sensor-based 3-D autonomous surface-following control](https://www.sciencedirect.com/science/article/pii/0378475495000909) | type: official journal page | year: 1996 | notes: Foundational precursor for autonomous sensor-based surface following.
- [Finger contact sensing and the application in dexterous hand manipulation](https://www.shadowrobot.com/wp-content/uploads/2022/04/Finger-Contact-Sensing-and-the-Application-in-Dexterous-Hand-Manipulation-Matthew-Godden-Co-Author-2015.pdf) | type: paper PDF | year: 2015 | notes: Precursor linking fingertip contact sensing to surface following and manipulation.
- [Active sensorimotor control for tactile exploration](https://www.sciencedirect.com/science/article/abs/pii/S0921889016303086) | type: official journal page | year: 2017 | notes: Precursor for active contour following and tactile action-perception loops on unknown objects.
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://arxiv.org/abs/2505.22159) | type: arXiv abstract page | year: 2025 | notes: Primary source for the 2025 force-aware VLA precursor, including the 23.2% average gain over pi0-based baselines and ForceVLA-Data across five contact-rich tasks.
