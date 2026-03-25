---
title: "Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23 inclusive; includes 2026 preprints publicly available by 2026-03-23."
---

# Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor

## Scope
Methods in which a single robot manipulator actively acquires observations with a manipulator-mounted sensor, or tightly coupled in-hand sensing on that manipulator, to reconstruct an unknown object or local object geometry for downstream approach, grasping, placement, or manipulation. Core scope includes eye-in-hand RGB or RGB-D scanning, wrist-camera plus tactile in-hand reconstruction, active tactile exploration, TSDF or point-cloud fusion, neural implicit SDF or occupancy models, NeRF-like object models, and emerging Gaussian-splatting object representations. Borderline systems that require fixed external cameras, multi-camera arrays, mobile-base scene mapping, or passive one-shot reconstruction are treated as adjacent rather than core.

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The strongest reconstruction and reconstruction-for-manipulation headline numbers in this note have now been re-checked from primary sources, but several adjacent geometry and transparent-object claims still need a second table-focused pass.

### Re-checked Claims
- AcTExplore: 95.97% average IoU coverage on unseen YCB objects while training on primitive shapes (`verified-primary-pdf`).
- NeuralFeels: 81% final F-score, 4.7 mm pose drift, 2.3 mm with known CAD, and up to 94% tracking improvement under heavy occlusion (`verified-primary-pdf`).
- ActNeRF: 14% PSNR gain, 20% F-score gain, and 71% task-success gain (`verified-primary-pdf`).
- Act-VH: real-robot grasp success after five touches rises from 30% to 80%, which supports the note's weaker claim that active visuo-haptic completion improves downstream grasping (`verified-primary-pdf`).

### Still Pending
- Dex-NeRF transparent-object grasp numbers were not re-audited in this pass.
- Some Gaussian-splatting and planning-ready geometry claims remain evidence-grounded summaries rather than table-level re-checks.

## Inclusion Criteria
- Papers and systems published or publicly available in the requested window that reconstruct unknown object geometry, partial geometry, or object-centric maps through iterative sensing.
- Single-manipulator setups with a hand-eye or wrist-mounted visual sensor, fingertip vision-based tactile sensing, or tightly coupled visual-tactile in-hand sensing on the same manipulator.
- Representations used for downstream robotic decisions, including TSDF, fused point clouds or surfels, implicit SDF or occupancy fields, radiance fields, Gaussian primitives, and touch-conditioned latent shape models.
- Works evaluated on robotic reconstruction, exploration, grasping, placement, tracking, or manipulation tasks where the reconstruction materially affects decisions.

## Exclusion Criteria
- Whole-scene mapping papers without an object-centric manipulation target were excluded or only used for background influence.
- Systems depending on fixed external cameras or multi-camera arrays were treated as adjacent rather than core; for example, See-Then-Grasp and Dex-NeRF inform the design space but do not satisfy the strict single manipulator-mounted sensor boundary.
- Pure category-level shape completion, passive single-view reconstruction, or grasping methods that do not build an explicit or implicit object model were excluded.
- Multi-arm systems, mobile-platform-only scanners, and non-robotic 3D reconstruction papers were excluded.

## Problem Formulations
- Active next-best-view scanning of a tabletop object with an eye-in-hand camera to maximize surface coverage or reduce model uncertainty.
- In-hand visuo-tactile SLAM, where the robot jointly estimates object pose and local geometry while the object moves relative to the fingers.
- Active tactile exploration, where sparse contacts are sequenced to cover unknown object surfaces under limited sensor footprint and action budget.
- Reconstruction-for-manipulation, where the learned object model is only required to be good enough for grasp selection, constrained placement, pose tracking, or downstream approach planning rather than full watertight scanning.
- Lifelong object model accumulation and reuse, where a robot improves future manipulation of re-encountered objects by reusing a previously reconstructed representation.
- High-fidelity automated digitization, where a robot arm actively plans viewpoints to produce photorealistic and geometrically accurate object assets.

## Sensing Modalities
- Item
  - modality: Hand-eye or wrist-mounted RGB-D
  - details: Used for active scanning, segmentation-backed object tracking, and dense geometric fusion in systems such as the lifelong TSDF pipeline and BundleSDF.
- Item
  - modality: Hand-eye or wrist-mounted RGB
  - details: Used in NeRF-based and photorealistic reconstruction pipelines such as ActNeRF and Auto3R, often with known robot kinematics to recover camera poses.
- Item
  - modality: Vision-based tactile sensors
  - details: DIGIT, GelSight, or related optical tactile sensors provide local depth or contact geometry in FingerSLAM, VTacO, TouchSDF, Touch2Shape, and tactile-informed Gaussian methods.
- Item
  - modality: Proprioception and hand kinematics
  - details: Robot joint states, finger kinematics, and grasp state are used to register touch observations, maintain pose graphs, and constrain active exploration trajectories.
- Item
  - modality: Semantic masks or object segmentation
  - details: Object-centric visual pipelines often assume object masks, first-frame segmentation, or known target isolation before reconstruction or planning.
- Item
  - modality: Rendered uncertainty signals
  - details: Many active methods convert model uncertainty, entropy, or expected information gain into action scores for view selection, reorientation, or stopping.

## Action Space And Robot Setup
- The dominant embodiment is a fixed-base single arm observing a tabletop object with a hand-eye or wrist-mounted camera.
- A second cluster uses multi-fingered hands or grippers with fingertip tactile sensors and a wrist camera for in-hand reconstruction.
- Common actions are viewpoint changes over a reachable hemisphere, local pose optimization for next-best-view, contact probing over uncertain surface regions, in-hand object rotation, and occasional grasp-and-reorient steps that preserve the single-manipulator assumption.
- Inference from sources: the most capable systems use mixed action spaces rather than pure camera motion, because a single arm cannot expose bottoms or self-occluded surfaces by view motion alone.

## Method Families
- Item
  - family: TSDF and explicit fusion with model reuse
  - representative methods: Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation
  - strength: Fast, manipulation-oriented, and directly usable for collision checking and pose tracking.
  - weakness: Typically lower fidelity and more sensitive to partial observability than newer neural representations.
- Item
  - family: Visuo-tactile pose-graph reconstruction
  - representative methods: FingerSLAM; Visual-Tactile Sensing for In-Hand Object Reconstruction; NeuralFeels
  - strength: Can recover hidden local geometry during contact and remains useful under visual occlusion.
  - weakness: Coverage grows slowly, calibration is demanding, and local tactile observations must be registered accurately.
- Item
  - family: Active tactile exploration
  - representative methods: AcTExplore; Touch2Shape
  - strength: Well matched to local surface discovery where camera views are insufficient.
  - weakness: Action efficiency and sim-to-real transfer are still limiting factors.
- Item
  - family: Neural implicit object fields
  - representative methods: BundleSDF; TouchSDF; NeuralFeels
  - strength: Compact continuous geometry with better surface interpolation than raw volumetric grids.
  - weakness: Online optimization, pose drift, and extraction of planning-ready collision geometry remain costly.
- Item
  - family: NeRF-based active reconstruction for manipulation
  - representative methods: ActNeRF; Auto3R
  - strength: High photorealism and uncertainty maps that naturally support next-best-view scoring.
  - weakness: Training cost, pose dependence, and incomplete access to hidden surfaces without physical reorientation.
- Item
  - family: Gaussian-splatting object reconstruction
  - representative methods: Snap-it, Tap-it, Splat-it; ObjSplat
  - strength: Faster rendering and increasingly geometry-aware active planning.
  - weakness: Still early for robotic deployment, with limited standardized manipulation evaluation.

## Representative System Pipelines
- Segment object from RGB-D observations, fuse an object TSDF online, track pose with a particle-filter variant, store the model in an object memory, then reuse and register that model when the object reappears to reduce future active perception burden.
  - system: Lu et al. lifelong TSDF reuse
  - pipeline: Segment object from RGB-D observations, fuse an object TSDF online, track pose with a particle-filter variant, store the model in an object memory, then reuse and register that model when the object reappears to reduce future active perception burden.
- Combine wrist-camera observations with fingertip tactile images in a factor graph, use odometry plus loop closure to estimate object pose, and stitch local tactile point clouds into a growing object surface model.
  - system: FingerSLAM
  - pipeline: Combine wrist-camera observations with fingertip tactile images in a factor graph, use odometry plus loop closure to estimate object pose, and stitch local tactile point clouds into a growing object surface model.
- Train in the VT-Sim environment, infer rigid or deformable object geometry from visual-tactile hand interaction, and transfer the learned reconstruction model to real-world in-hand cases.
  - system: VTacO / VTacOH
  - pipeline: Train in the VT-Sim environment, infer rigid or deformable object geometry from visual-tactile hand interaction, and transfer the learned reconstruction model to real-world in-hand cases.
- Use segmented RGB-D video to jointly optimize object pose and a neural object field, maintain memory frames and object detections, then recover a mesh and stable 6-DoF tracking for previously unknown objects.
  - system: BundleSDF
  - pipeline: Use segmented RGB-D video to jointly optimize object pose and a neural object field, maintain memory frames and object detections, then recover a mesh and stable 6-DoF tracking for previously unknown objects.
- Use reinforcement learning to select tactile probing motions that maximize reconstruction progress under a limited step budget, integrating each new contact into a growing surface estimate.
  - system: AcTExplore
  - pipeline: Use reinforcement learning to select tactile probing motions that maximize reconstruction progress under a limited step budget, integrating each new contact into a growing surface estimate.
- Fuse vision, touch, and proprioception into an online neural field plus pose graph during in-hand manipulation, continuously refining both object geometry and object pose under occlusion.
  - system: NeuralFeels
  - pipeline: Fuse vision, touch, and proprioception into an online neural field plus pose graph during in-hand manipulation, continuously refining both object geometry and object pose under occlusion.
- Render uncertainty from a partially learned object radiance field, choose either a new visual viewpoint or a reorientation-enabled observation, retrain the object model incrementally, and use the resulting geometry for downstream manipulation or asset creation.
  - system: ActNeRF / Auto3R
  - pipeline: Render uncertainty from a partially learned object radiance field, choose either a new visual viewpoint or a reorientation-enabled observation, retrain the object model incrementally, and use the resulting geometry for downstream manipulation or asset creation.

## Evaluation Tasks
- Unknown object surface reconstruction from active views.
- In-hand pose tracking plus geometry reconstruction under occlusion.
- Active tactile exploration under a limited number of touches or time steps.
- Object model reuse across repeated pick-and-place or constrained placement episodes.
- Transparent or reflective object grasping where the learned object model drives a downstream planner.
- Photorealistic robot-arm scanning and digitization of real objects.

## Common Metrics
- Chamfer Distance and related point-to-surface reconstruction error metrics.
- F-score for reconstructed surfaces or depth-based surface agreement.
- IoU or surface coverage metrics for exploration completeness.
- PSNR and novel-view rendering quality for NeRF-like methods.
- Pose error or drift, typically in millimeters or degrees, for in-hand tracking systems.
- Grasp success rate or task success rate when reconstruction feeds manipulation.
- Number of views, path length, or number of tactile contacts required to reach a target quality.

## Best Reported Capabilities
- AcTExplore reports 95.97% average IoU coverage on unseen YCB objects after being trained only on primitive shapes, showing that active tactile exploration can generalize beyond its training object set.
- NeuralFeels reports 81% final reconstruction F-score, 4.7 mm pose drift, and up to 94% tracking improvement under heavy occlusion across 70 real experiments, showing that online visuo-tactile neural fields can stay stable during in-hand interaction.
- ActNeRF reports 14% higher PSNR, 20% higher surface F-score, and 71% higher downstream task success than its comparison methods in simulated tabletop manipulation with reorientation actions.
- Auto3R demonstrates robot-arm deployment for automated scanning of real objects, including non-Lambertian and specular objects, and positions data-driven uncertainty prediction as a practical way to reduce human scan planning effort.
- Adjacent but influential evidence: Dex-NeRF achieves 90% and 100% physical grasp success in transparent-object settings using radiance-field geometry for grasp planning, showing that object-centric neural fields can directly support manipulation even when visual geometry is difficult.

## Failure Modes And Limitations
- Single-arm eye-in-hand systems struggle to observe bottoms, back sides, and narrow concavities without reorientation or contact.
- Visual-only neural fields remain brittle under pose error, poor segmentation, specular highlights, and transparent materials.
- Tactile systems acquire geometry slowly because each contact only reveals a local patch; policy quality matters as much as representation quality.
- Most evaluations use isolated tabletop objects or already-grasped objects rather than cluttered scenes with distractors and contact-rich uncertainty.
- Planning-ready geometry extraction is still a weak point for NeRF and Gaussian methods; many papers show attractive reconstructions but limited evidence on collision-safe deployment.
- Reproducibility is uneven because real systems depend on calibration, tactile sensor fabrication, object handling skills, and robot-specific control stacks.

## Representative Papers
- [[Paper - Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation|Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation]] (2022, ICRA 2022)
- [[Paper - FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback|FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback]] (2023, ICRA 2023)
- [[Paper - Visual-Tactile Sensing for In-Hand Object Reconstruction|Visual-Tactile Sensing for In-Hand Object Reconstruction]] (2023, CVPR 2023)
- [[Paper - BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects|BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects]] (2023, CVPR 2023)
- [[Paper - AcTExplore: Active Tactile Exploration on Unknown Objects|AcTExplore: Active Tactile Exploration on Unknown Objects]] (2024, ICRA 2024)
- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation|Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]] (2024, Science Robotics)
- [[Paper - TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing|TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing]] (2023, Touch Processing Workshop 2023 / arXiv)
- [[Paper - Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions|Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions]] (2024, arXiv preprint; accepted poster in ICRA 2024 RoboNeRF workshop)
- [[Paper - Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces|Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces]] (2025, Google Research publication page / arXiv preprint)
- [[Paper - Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction|Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction]] (2025, CVPR 2025)
- [[Paper - Auto3R: Automated 3D Reconstruction and Scanning via Data-driven Uncertainty Quantification|Auto3R: Automated 3D Reconstruction and Scanning via Data-driven Uncertainty Quantification]] (2025, arXiv preprint)

## Trends 2021 To 2026
- 2021-2022: object-centric robotic reconstruction is still dominated by explicit models and task-facing pipelines, with TSDF reuse and specialized NeRF pipelines for hard perception cases such as transparent objects.
- 2023: the field shifts toward object-level neural representations and stronger multimodal fusion, especially visuo-tactile in-hand reconstruction and joint tracking plus reconstruction.
- 2024: active uncertainty-driven loops become more explicit; tactile exploration and manipulator-aware NeRF planning both use model uncertainty to choose actions rather than just fusing passively collected data.
- 2025: diffusion and Gaussian-based object models start to matter, especially when touch is needed for local detail or when faster rendering is valuable for active planning.
- Early 2026: preprints indicate a move toward geometry-aware Gaussian surfels and multi-step path planning, suggesting that the next phase may combine real-time rendering with stronger geometric guarantees.
- Inference from sources: the center of gravity is moving from generic full reconstruction toward task-sufficient object models that can be built quickly, updated online, and directly queried by a manipulation planner.

## Research Gaps
- A shared benchmark that jointly measures scan quality, action cost, stopping efficiency, and downstream manipulation benefit is still missing.
- Most systems do not handle cluttered multi-object scenes where the target object is partially blocked before scanning begins.
- Stopping criteria are often heuristic; calibrated uncertainty that predicts task success remains underdeveloped.
- Single-arm full-coverage reconstruction without external cameras or handovers remains fundamentally hard and still lacks strong general solutions.
- Many neural methods reconstruct attractive geometry but do not expose robust collision models, grasp affordances, or contact-stable local surface estimates in a planner-friendly form.
- Tactile exploration still suffers from slow coverage, policy transfer issues, and limited public data diversity.
- Reflective, transparent, and deformable objects remain split across separate subliteratures instead of being handled by one unified active mapping stack.

## Opportunities For Single Manipulator Systems
- Use a two-layer representation: maintain a fast explicit occupancy or TSDF shell for planning and safety, while refining only the target object with an implicit or Gaussian model where uncertainty is high.
- Treat contact as a sparse but high-value sensing action rather than a fallback; touch should be invoked only for occluded, reflective, or manipulation-critical regions.
- Exploit object memory and model reuse aggressively, because repeated household and warehouse objects make one-shot full rescanning unnecessary.
- Plan for task-sufficient reconstruction instead of full watertight models, for example by focusing on graspable rims, support surfaces, insertion features, or collision-critical envelopes.
- Combine view planning and reorientation planning in one action space, since a single arm's main limitation is not sensing quality but inaccessible viewpoints.
- Adopt faster Gaussian or hybrid field renderers only if they are coupled to geometry-aware uncertainty, otherwise they risk improving appearance more than manipulation usefulness.

## Sources
- [Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation](https://arxiv.org/abs/2109.13910) | type: primary paper | notes: Abstract, authors, TSDF representation, and lifelong object-memory framing.
- [dblp record for Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation](https://dblp.org/rec/conf/icra/LuWMMB22) | type: bibliographic record | notes: Venue and page numbers for ICRA 2022.
- [FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback](https://arxiv.org/abs/2303.07997) | type: primary paper | notes: Abstract, authors, wrist-camera plus tactile setup, and real-world evaluation summary.
- [dblp record for FingerSLAM](https://dblp.org/rec/conf/icra/ZhaoBA23) | type: bibliographic record | notes: Venue and page numbers for ICRA 2023.
- [Visual-Tactile Sensing for In-Hand Object Reconstruction](https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Visual-Tactile_Sensing_for_In-Hand_Object_Reconstruction_CVPR_2023_paper.html) | type: primary paper | notes: Official CVPR page with authors, abstract, and VT-Sim/VTacO framing.
- [BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects](https://research.nvidia.com/publication/2023-06_bundlesdf-neural-6-dof-tracking-and-3d-reconstruction-unknown-objects) | type: official publication page | notes: Authors, publication date, venue, and project link.
- [AcTExplore project page](https://prg.cs.umd.edu/AcTExplore) | type: official project page | notes: ICRA 2024 venue, abstract, code, and reported tactile exploration results.
- [AcTExplore arXiv / PDF entry](https://prg.cs.umd.edu/research/AcTExplore_files/AcTExplore.pdf) | type: paper PDF | notes: Project PDF used for quantitative details.
- [NeuralFeels official repository](https://github.com/facebookresearch/neuralfeels) | type: official repository | notes: Paper title, Science Robotics venue, code, dataset, and model links.
- [TouchSDF project page](https://touchsdf.github.io/) | type: official project page | notes: Authors, task framing, code link, and tactile-to-DeepSDF pipeline description.
- [TouchSDF arXiv page](https://arxiv.org/abs/2311.12602) | type: primary paper | notes: Abstract and arXiv metadata.
- [ActNeRF project page](https://actnerf.github.io/) | type: official project page | notes: Core source for task setup, action space, reported gains, and comparison to ActiveNeRF.
- [ActNeRF arXiv page](https://arxiv.org/abs/2404.01812) | type: primary paper | notes: Abstract and authors.
- [ActiveNeRF: Learning where to See with Uncertainty Estimation](https://arxiv.org/abs/2209.08546) | type: background paper | notes: Used to trace uncertainty-driven active NeRF influence cited directly by ActNeRF.
- [Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces](https://arxiv.org/abs/2403.20275) | type: primary paper | notes: Abstract and authors for tactile-informed Gaussian reconstruction.
- [Google Research page for Snap-it, Tap-it, Splat-it](https://research.google/pubs/snap-it-tap-it-splat-it-tactile-informed-3d-gaussian-splatting-for-reconstructing-challenging-surfaces/) | type: official publication page | notes: High-level summary and publication-year context.
- [Touch2Shape official CVPR 2025 page](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html) | type: primary paper | notes: Authors, venue, abstract, and exploration-plus-reconstruction framing.
- [Auto3R arXiv page](https://arxiv.org/abs/2512.04528) | type: primary paper | notes: Authors, abstract, and explicit robot-arm deployment claim.
- [ObjSplat arXiv page](https://arxiv.org/abs/2601.06997) | type: primary paper | notes: Authors, abstract, Gaussian surfels, and next-best-path planning.
- [Dex-NeRF: Using a Neural Radiance Field to Grasp Transparent Objects](https://proceedings.mlr.press/v164/ichnowski22a.html) | type: primary paper | notes: Used as adjacent evidence linking radiance-field object reconstruction to downstream manipulation.
- [See-Then-Grasp: Object Full 3D Reconstruction via Two-Stage Active Robotic Reconstruction Using Single Manipulator](https://www.mdpi.com/2076-3417/15/1/272) | type: adjacent boundary paper | notes: Used to sharpen the exclusion boundary because it relies on a fixed external camera in the second stage.
- [KinectFusion: Real-Time Dense Surface Mapping and Tracking](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/ismar_2011.pdf) | type: primary precursor paper | notes: Foundational dense fusion precursor for explicit object mapping.
- [Robotic In-Hand 3D Object Modeling](https://rse-lab.cs.washington.edu/projects/3d-in-hand/) | type: official project page | notes: Project page linking the 2011 IJRR and ICRA precursors for in-hand modeling and next-best-view planning.
- [Autonomous Generation of Complete 3D Object Models Using Next Best View Manipulation Planning](https://ai.cs.washington.edu/www/media/papers/nbv-icra-11-final.pdf) | type: primary precursor paper | notes: Manipulator-based next-best-view planning precursor.
- [DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation](https://arxiv.org/abs/1901.05103) | type: primary precursor paper | notes: Continuous SDF representation precursor.
- [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934) | type: primary precursor paper | notes: Radiance-field representation precursor for active object-centric NeRF methods.
