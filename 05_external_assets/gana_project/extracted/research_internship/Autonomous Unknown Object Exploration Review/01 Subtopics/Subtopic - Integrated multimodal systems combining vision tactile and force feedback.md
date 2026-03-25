---
title: "Integrated multimodal systems combining vision tactile and force feedback"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23, including 2026 preprints available by 2026-03-23."
---

# Integrated multimodal systems combining vision tactile and force feedback

## Scope
This subtopic covers robotic systems that explicitly fuse camera sensing with tactile sensing, force-torque feedback, and/or robot proprioception to improve autonomous reaching, touching, scanning, pushing, grasping, in-hand manipulation, or contact-rich execution on unknown or previously unseen objects. The focus is on closed-loop systems where the multimodal estimate changes the robot's next action, controller, or stopping decision. The boundary excludes pure vision-only manipulation, pure tactile-only exploration unless used only as precursor context, offline representation learning without embodied closed-loop evaluation, and systems that depend on a fixed CAD model or object-specific template library at deployment unless they are used only to clarify historical influences.

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The note's strongest multimodal anchor numbers are now re-checked, and the visuo-tactile world-model branch is now explicitly abstract-verified, but several transparent-object and dataset-scale claims still need a second paper-by-paper pass.

### Re-checked Claims
- NeuralFeels: 81% F-score, 4.7 mm pose drift, 2.3 mm with known CAD, and up to 94% better tracking under heavy occlusion (`verified-primary-pdf`).
- ForceVLA: 23.2% average task-success improvement and up to 80% plug-insertion success (`verified-primary-abstract`).
- TacVLA: 20% on disassembly, 60% on in-box picking, and 2.1x under visual occlusion (`verified-primary-abstract`).
- HapticVLA: 86.7% mean real-world success without inference-time tactile sensing (`verified-primary-abstract`).
- Visuo-Tactile World Models: 33% better object permanence, 29% better compliance with motion laws, and up to 35% higher zero-shot real-robot success (`verified-primary-abstract`).

### Still Pending
- Transparent-object grasping gains and some dense-clutter pose-estimation gains remain to be re-audited.
- OmniVTA scale claims remain primary-source summaries rather than table-level re-checks.

## Inclusion Criteria
- Primary papers, official proceedings pages, or official project pages published or available within the requested window whose system explicitly combines camera sensing with tactile, force-torque, or proprioceptive feedback.
- Systems with embodied evaluation on unknown, unseen, transparent, cluttered, or otherwise perception-challenging objects where multimodal fusion changes estimation, planning, control, or policy execution online.
- Manipulation and exploration settings including visual servoing before contact, tactile refinement after contact, active touch for shape or pose estimation, non-prehensile pushing, in-hand manipulation, or contact-rich task execution.

## Exclusion Criteria
- Vision-only systems, even if they handle unknown objects well, unless they are used only as baselines inside a multimodal paper.
- Pure tactile-only or pure force-only systems within 2021-2026, except when cited as historical precursors for active touch, tactile servoing, or uncertainty-driven exploration.
- Offline multimodal representation papers without autonomous robot-loop evaluation on reach, touch, scan, or manipulation tasks.
- Methods that require object-specific CAD models, pre-rendered tactile databases, or fixed instance-level templates at deployment as a central assumption, unless cited only to define the boundary.

## Problem Formulations
- Pre-contact visual approach followed by post-contact tactile or force refinement, where vision gets the robot near the object and touch resolves the final pose or contact ambiguity.
- Active visuo-tactile pose estimation of unknown objects in clutter, often with decluttering actions selected before tactile probing.
- Uncertainty-driven visuo-haptic shape completion, where the robot uses a camera to build an initial shape hypothesis and chooses the next touch to reduce occluded-region uncertainty.
- Closed-loop visuo-tactile SLAM or tracking of unknown in-hand objects, jointly estimating pose and shape while the object moves and becomes visually occluded.
- Multimodal parameter inference during non-prehensile interaction, such as pushing while fusing vision, touch, and proprioception to infer object properties or control target pose.
- Contact-rich policy learning or world modeling, where fused vision-tactile-proprioceptive streams support insertion, wiping, fluid handling, or other tasks that require online contact-state reasoning.

## Sensing Modalities
- RGB and RGB-D cameras are used from wrist-mounted, end-effector-mounted, or external viewpoints to provide coarse object pose, segmentation, scene context, or pre-contact servoing cues.
- Dense vision-based tactile sensors such as GelSight, DIGIT, GelSlim, and flexible optical tactile pads dominate the tactile side because they provide local contact geometry, slip, and shear as image-like observations.
- Wrist force-torque sensors and force-regulated controllers appear in some systems, especially pivoting, pushing, and precision assembly, but are less common than vision-based tactile sensing in the current literature.
- Robot proprioception, including joint states, gripper width, end-effector pose, and motion history, is used almost everywhere to register tactile readings in a common frame and to stabilize control.
- Several systems treat tactile images as local point clouds, local surface normals, slip/shear fields, or latent contact states rather than as raw images only.
- Recent 2025-2026 systems additionally model synchronized video, tactile, and action trajectories as a world-model dataset for predicting short-horizon contact evolution.

## Action Space And Robot Setup
- Single-arm setups with parallel grippers or tactile fingertips use vision for coarse positioning and tactile contact for local servo correction, transparent-object poking, or shape completion.
- Dexterous or multi-fingered hands with wrist cameras perform in-hand reorientation, rotation, or reconstruction while fusing tactile observations from multiple fingertips with global vision.
- Two-robot or bimanual systems appear in dense-clutter decluttering and in fine-grained manipulation, where one arm stabilizes or clears the scene and the other performs the multimodal contact-rich action.
- Non-prehensile setups include pushing and pivoting, where the action space mixes end-effector motion, gripper width, or force profile control with tactile or force-based feedback.
- Portable visuo-tactile grippers and low-cost flexible tactile hardware are increasingly used for data collection and imitation learning on insertion, fluid transfer, wiping, and reorientation tasks.
- Most embodiments are tabletop manipulators with one object or one target contact region at a time, not mobile manipulators operating in large unstructured workspaces.

## Method Families
- Collocated vision-tactile servoing: use a camera mounted near the tactile contact point to improve pre-contact localization and then use tactile sensing to refine contact and pose after touch.
- Active visuo-tactile interactive perception: combine visual scene understanding, action selection, and tactile probing to localize unknown objects in clutter or under ambiguity.
- Uncertainty-driven visuo-haptic reconstruction: estimate a partial shape from vision, choose the next exploratory touch using uncertainty, and feed the result back into grasping or manipulation.
- Graph-based and neural-field visuo-tactile tracking: jointly estimate unknown object pose and shape during in-hand manipulation, often under severe visual occlusion.
- Hybrid visuo-force or visuo-tactile control: split the task into a coarse vision stage and a fine tactile/force stage for pushing, pivoting, insertion, or orientation control.
- Representation-learning and world-model systems: learn fused visuo-tactile-proprioceptive representations or predictive contact models that improve long-horizon contact-rich policies.

## Representative System Pipelines
- Collocated visual approach and tactile refinement
  - pipeline: Collocated camera estimates pre-contact pose or approach direction -> robot visually servos toward object -> tactile contact provides local correction of contact point and pose -> controller updates the final motion or grasp.
  - examples: Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization; Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping
- Active clutter-aware visuo-tactile perception
  - pipeline: RGB-D scene parsing -> declutter graph or active-view selection -> autonomous removal or probing action -> tactile and visual pose update with information-gain-driven touch selection -> target-object pose estimate for downstream manipulation.
  - examples: Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter
- Visuo-tactile object tracking and reconstruction
  - pipeline: Wrist/global vision plus fingertip tactile streams -> factor graph or neural-field object model -> pose and shape update under occlusion -> reconstruction stitched over time -> manipulation continues with updated estimate.
  - examples: FingerSLAM; NeuralFeels; ViTaSCOPE
- Uncertainty-driven visuo-haptic shape completion
  - pipeline: Initial camera point cloud -> implicit shape model with uncertainty -> next-best touch selected on high-uncertainty region -> touch and empty-space constraints fused back into model -> improved grasp or manipulation plan.
  - examples: Active Visuo-Haptic Object Shape Completion; Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation
- Policy or world-model based contact-rich manipulation
  - pipeline: Synchronized video, tactile, and proprioceptive data -> fused latent or 3D multimodal representation -> policy or world model predicts contact-relevant future state -> high-frequency controller or diffusion policy executes action -> tactile mismatch triggers correction.
  - examples: 3D-ViTac; Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception; Visuo-Tactile World Models; OmniVTA

## Evaluation Tasks
- Visual servoing and localization immediately before and after first contact.
- Transparent-object grasping under poor depth cues and strong background or lighting variation.
- Unknown-object pose estimation in dense clutter with decluttering and tactile refinement.
- Unknown-object 3D shape completion or reconstruction for better grasp planning.
- In-hand pose and shape tracking of unseen objects under severe visual occlusion.
- Non-prehensile object pushing or pivoting to a target pose using tactile, force, and proprioceptive feedback.
- Fine-grained contact-rich tasks such as insertion, wiping, fluid transfer, and reorientation where vision-only control is brittle.
- Zero-shot or low-shot transfer to unseen objects, altered geometries, or disturbed execution conditions.

## Common Metrics
- Pose-estimation error, pose drift, or target-pose accuracy in millimeters and degrees.
- Shape reconstruction metrics such as F-score, IoU, point-cloud quality, or uncertainty reduction over successive touches.
- Task success rate for grasping, insertion, pushing, rotation, assembly, wiping, or other manipulation outcomes.
- Improvement relative to vision-only, tactile-only, or single-stage baselines.
- Number of touches, exploration steps, interaction time, or data-efficiency in low-demo and low-epoch regimes.
- Robustness under visual occlusion, transparency, human disturbance, unseen object geometry, or out-of-distribution conditions.
- Physical plausibility metrics in world-model papers, such as object permanence or compliance with motion laws.
- In some force-sensitive tasks, stability or force-regulation quality rather than geometric accuracy alone.

## Best Reported Capabilities
- NeuralFeels reports final reconstruction F-scores of 81%, average pose drift of 4.7 mm, 2.3 mm with known CAD models, and up to 94% better tracking than vision-only methods under heavy visual occlusion.
- Where Shall I Touch? reports that vision-guided tactile poking raises transparent-object grasp success from 38.9% to 85.2%.
- Visual-tactile Fusion for Transparent Object Grasping in Complex Backgrounds reports a 36.7% grasp-success improvement over direct grasping and a 34% improvement in transparent-object classification accuracy.
- Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter reports up to 36% better pose accuracy than the active-vision baseline.
- Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation reports average real-robot grasp success increasing from 63.3% before exploratory touch to 70.4% after one touch and 82.7% after five touches.
- ForceVLA reports a 23.2% average task-success improvement over strong pi0-based baselines and up to 80% success on plug insertion, showing that explicit force sensing can materially strengthen multimodal VLA-style control on contact-rich tasks.
- TacVLA reports average gains of 20% on disassembly, 60% on in-box picking, and 2.1x under visual occlusion, showing that contact-aware tactile-token fusion can materially improve multimodal VLA performance in physically constrained tasks.
- HapticVLA reports 86.7% mean real-world success while removing inference-time tactile hardware, suggesting that part of the multimodal benefit can be distilled offline rather than sensed online at deployment.
- Visuo-Tactile World Models reports 33% better object permanence, 29% better compliance with motion laws in autoregressive rollouts, and up to 35% higher zero-shot real-robot success than vision-only alternatives.
- Touch in the Wild shows that with only 30 demonstrations a pretrained visuo-tactile representation can still disambiguate in-hand state and complete test-tube reorientation and insertion, whereas the non-pretrained policy fails.
- OmniVTA introduces a large-scale visuo-tactile-action dataset with 21,000+ trajectories over 86 tasks and 100+ objects and demonstrates real-robot generalization to unseen objects and geometric configurations with a 60 Hz reflexive controller in the loop.

## Failure Modes And Limitations
- Many systems still require carefully calibrated tactile hardware and tight camera-sensor extrinsics, making reproduction and deployment harder than vision-only baselines.
- Evidence is concentrated in rigid-object tabletop settings; deformable objects, heavy clutter without prior decluttering, and open-world scene variability remain weakly covered.
- Several methods need deliberate first contact or stable holding conditions, so failures can occur before multimodal fusion can help.
- Local tactile geometry is often ambiguous on smooth, symmetric, or weakly featured objects, especially without a strong visual prior.
- Force-torque sensing is used less systematically than vision-based tactile sensing, so explicit force-aware manipulation remains less mature than visuo-tactile pose and shape estimation.
- Task generalization is often demonstrated on unseen objects within a narrow task family rather than on broad manipulation repertoires.
- World-model and policy-learning systems are promising but still depend on large data collection pipelines, simulation fidelity, or custom hardware that few labs can replicate quickly.

## Representative Papers
- [[Paper - Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization|Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization]] (2022, IEEE Robotics and Automation Letters)
- [[Paper - Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter|Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter]] (2022, IEEE Robotics and Automation Letters / ICRA 2022)
- [[Paper - Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping|Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping]] (2022, arXiv preprint)
- [[Paper - FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback|FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback]] (2023, ICRA 2023)
- [[Paper - Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation|Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation]] (2023, IROS 2023)
- [[Paper - Push to know! -- Visuo-Tactile based Active Object Parameter Inference with Dual Differentiable Filtering|Push to know! -- Visuo-Tactile based Active Object Parameter Inference with Dual Differentiable Filtering]] (2023, IROS 2023)
- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation|Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]] (2024, Science Robotics)
- [[Paper - 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing|3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing]] (2025, CoRL proceedings)
- [[Paper - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation|ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (2025, NeurIPS 2025 / arXiv)
- [[Paper - Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception|Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception]] (2025, IEEE Robotics and Automation Letters)
- [[Paper - ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation|ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation]] (2025, RSS 2025)
- [[Paper - Visuo-Tactile World Models|Visuo-Tactile World Models]] (2026, arXiv preprint)
- [[Paper - OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation|OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation]] (2026, arXiv preprint)
- [[Paper - TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation|TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation]] (2026, arXiv preprint)
- [[Paper - HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing|HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing]] (2026, arXiv preprint)
- [[Paper - TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation|TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation]] (2026, arXiv preprint)

## Trends 2021 To 2026
- The field shifts from local multimodal correction modules, such as visual servoing plus tactile refinement, toward end-to-end systems that keep multimodal fusion active throughout the task.
- Unknown-object handling increasingly moves from single rigid objects in simple scenes toward harder settings such as dense clutter, transparency, occlusion, and long-horizon contact-rich tasks, although coverage is still uneven.
- Representations progress from explicit local point clouds and Gaussian-process surfaces to neural fields, contact fields, shared 3D point spaces, and world-model latents.
- Vision-based tactile sensors become the dominant contact modality because they provide geometry, slip, and shear with low cost and high spatial resolution, while explicit force-torque sensing remains more niche.
- Data availability improves materially: FeelSight, Touch in the Wild, and OmniViTac-style datasets mark a move from tiny lab-specific collections to broader multimodal corpora.
- The strongest recent systems increasingly combine coarse global vision with fine tactile or force-sensitive control, rather than trying to solve the entire task from one modality or one control regime.
- Despite this progress, the field still lacks a standard benchmark that jointly measures uncertainty reduction, action efficiency, and downstream manipulation success on unseen objects.

## Research Gaps
- A unified benchmark for unknown-object multimodal manipulation is still missing, especially one that spans perception accuracy, sample efficiency, and downstream task performance.
- Explicit fusion with true force-torque sensing is less developed than fusion with vision-based tactile sensing, so force-aware control remains underrepresented relative to pose and shape estimation.
- The field still lacks convincing evaluations in severe clutter, articulation, deformability, or multi-object interactions without simplifications such as decluttering first.
- Most learning-based systems report strong gains but do not always isolate which part of the multimodal stack provides the improvement: sensor placement, representation, controller split, or dataset scale.
- Contact establishment itself is often treated as solved; fewer systems address safe search, first contact, and retreat within one end-to-end loop.
- Simulation-to-real transfer for tactile and force-sensitive policies remains a bottleneck, especially when sensor mechanics, contact friction, and object compliance differ from training assumptions.
- There is room for tighter integration between uncertainty-aware geometric estimators and modern policy or world-model approaches, rather than treating estimation and control as largely separate stages.

## Opportunities For Single Manipulator Systems
- A strong near-term architecture is a wrist RGB-D or RGB camera paired with one or two dense tactile pads and the robot's native proprioception, using vision for coarse approach and tactile sensing only for the last contact-critical phase.
- Transparent and reflective object handling is an especially attractive niche because multimodal gains there are already large and easier to justify than general all-object manipulation.
- Uncertainty-driven visuo-haptic shape completion offers a practical alternative to large policy models for single-arm systems that only need a few informative touches before grasping.
- Coarse-to-fine control is promising for single manipulators because it keeps the vision and tactile/force roles clean: vision handles global alignment, while contact sensing handles the final pose or force regulation.
- Portable visuo-tactile data collection, as in Touch in the Wild, suggests that single-arm systems could now acquire task-specific multimodal data at much lower cost than older dexterous-hand setups.
- The best application targets are semi-structured industrial or lab tasks such as connector insertion, transparent-container handling, precise wiping, and pushing or alignment of unknown rigid parts, where the final centimeters and final newtons matter more than broad semantic reasoning.

## Sources
- [Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization](https://arxiv.org/abs/2204.11686) | source type: primary paper | why used: Used for the collocated camera-tactile sensor setup, RA-L venue, and the pre-contact visual servo plus post-contact tactile refinement formulation.
- [Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter](https://arxiv.org/abs/2202.02207) | source type: primary paper | why used: Used for the declutter graph pipeline, active vision plus active touch formulation, and the up to 36% pose-accuracy improvement claim.
- [Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping](https://arxiv.org/abs/2208.09743) | source type: primary paper | why used: Used for the transparent-object grasping pipeline and the 38.9% to 85.2% grasp-success improvement claim.
- [Visual-tactile Fusion for Transparent Object Grasping in Complex Backgrounds](https://arxiv.org/abs/2211.16693) | source type: primary paper | why used: Used for the transparent-object visual-tactile fusion framework, synthetic dataset note, and the 36.7% grasp-success and 34% classification improvements.
- [Active Visuo-Haptic Object Shape Completion](https://arxiv.org/abs/2203.09149) | source type: primary paper | why used: Used for the uncertainty-driven active visuo-haptic reconstruction formulation and its RA-L 2022 venue.
- [FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback](https://arxiv.org/abs/2303.07997) | source type: primary paper | why used: Used for the factor-graph visuo-tactile localization and reconstruction pipeline, 20-train and 6-unseen object split, and ICRA 2023 venue.
- [Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation](https://arxiv.org/abs/2303.04700) | source type: primary paper | why used: Used for the closed-loop shape-completion pipeline, public code and data note, IROS 2023 venue, and grasp-success numbers after exploratory touches.
- [Push to know! -- Visuo-Tactile based Active Object Parameter Inference with Dual Differentiable Filtering](https://arxiv.org/abs/2308.01001) | source type: primary paper | why used: Used for the active pushing formulation, next-best exploratory push idea, and IROS 2023 acceptance.
- [Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation](https://arxiv.org/abs/2312.13469) | source type: primary paper | why used: Used for the neural-field formulation and the quantitative F-score, pose drift, and occlusion-improvement claims.
- [NeuralFeels official project page](https://suddhu.github.io/neural-feels/) | source type: official project page | why used: Used for the Science Robotics venue, code availability, and FeelSight dataset description.
- [3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://proceedings.mlr.press/v270/huang25e.html) | source type: official proceedings page | why used: Used for the CoRL proceedings entry, unified 3D multimodal representation description, and the claim that it outperforms vision-only policies on fine-grained tasks.
- [3D-ViTac official project page](https://binghao-huang.github.io/3D-ViTac/) | source type: official project page | why used: Used for method code and hardware resources, fine-grained task descriptions, and single-arm and bimanual manipulation examples.
- [Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception](https://research-information.bris.ac.uk/en/publications/coarse-to-fine-robotic-pushing-using-touch-vision-and-propriocept/) | source type: official university publication page | why used: Used for the multi-stage coarse-to-fine formulation, RA-L 2025 venue, and the explicit role split between vision and tactile feedback.
- [ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation](https://www.roboticsproceedings.org/rss21/p054.html) | source type: official proceedings page | why used: Used for the RSS 2025 venue and the in-hand pose plus extrinsic-contact estimation formulation.
- [ViTaSCOPE official project page](https://jayjunlee.github.io/vitascope/) | source type: official project page | why used: Used for the contact-field description, sim-to-real claim, and code-coming-soon reproducibility note.
- [Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper](https://arxiv.org/abs/2507.15062) | source type: primary paper | why used: Used for the portable visuo-tactile gripper, cross-attention pretraining setup, and the low-demo, low-epoch manipulation claims.
- [Touch in the Wild official project page](https://binghao-huang.github.io/touch_in_the_wild/) | source type: official project page | why used: Used for the NeurIPS 2025 project status, code and dataset links, 2,700 demonstrations, 43 tasks, 12 environments, and 2.6 million visuo-tactile pairs.
- [Visuo-Tactile World Models](https://arxiv.org/abs/2602.06001) | source type: primary paper | why used: Used for the 2026 world-model formulation and the 33%, 29%, and up to 35% improvement claims.
- [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2603.19201) | source type: primary paper | why used: Used for the OmniViTac dataset size, the four-module world-model pipeline, unseen-object generalization claim, and 60 Hz reflexive controller.
- [OmniVTA official project page](https://mrsecant.github.io/OmniVTA/) | source type: official project page | why used: Used for task categories, real-robot examples, code and data-collection links, and qualitative evidence about adaptive fusion under perturbations.
- [Localizing a polyhedral object in a robot hand by integrating visual and tactile data](https://www.sciencedirect.com/science/article/abs/pii/S003132039900059X) | source type: primary paper | why used: Used as an early precursor for direct visual-tactile localization of grasped objects.
- ["Touching to See" and "Seeing to Feel": Robotic Cross-modal Sensory Data Generation for Visual-Tactile Perception](https://arxiv.org/abs/1902.06273) | source type: primary paper | why used: Used as a precursor for cross-modal visual-tactile reasoning and data generation.
- [Visuo-Haptic Grasping of Unknown Objects based on Gaussian Process Implicit Surfaces and Deep Learning](https://h2t.iar.kit.edu/pdf/Ottenhaus2019.pdf) | source type: primary paper PDF | why used: Used as a precursor for unknown-object visuo-haptic grasping pipelines that integrate sensing, exploration, and grasp selection.
- [Active Tactile Object Exploration with Gaussian Processes](https://is.mpg.de/ps/publications/yieatal16) | source type: official publication page | why used: Used as a precursor for uncertainty-driven next-touch planning and GP-based surface modeling.
- [Exploratory Tactile Servoing With Active Touch](https://research-information.bris.ac.uk/en/datasets/exploratory-tactile-servoing-with-active-touch/) | source type: official dataset/publication page | why used: Used as a precursor for closed-loop tactile perception-and-control during exploration.
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://arxiv.org/abs/2505.22159) | source type: arXiv abstract page | why used: Used to cover the 2025 force-aware multimodal VLA branch, including the 23.2% average gain over pi0-based baselines and the five-task ForceVLA-Data dataset.
- [TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation](https://arxiv.org/abs/2603.12665) | source type: arXiv abstract page | why used: Used to cover the March 2026 tactile-token VLA branch, including the reported 20%, 60%, and 2.1x improvements under contact-rich and occluded settings.
- [HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing](https://arxiv.org/abs/2603.15257) | source type: arXiv abstract page | why used: Used to capture the distilled tactile-aware VLA branch and the reported 86.7% mean real-world success rate without inference-time tactile sensing.
- [TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321) | source type: arXiv abstract page | why used: Used to cover physically grounded tactile-force alignment, the TaF-Dataset scale, and the force-aware multimodal VLA branch in early 2026.
