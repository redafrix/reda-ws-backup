# Autonomous Unknown Object Exploration Report

Time window: 2021-03-23 to 2026-03-23

## Table of Contents
1. [Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor](#active-3d-reconstruction-scanning-and-object-centric-mapping-with-a-single-manipulator-mounted-sensor)
2. [Active visual exploration and next-best-view control for unknown object approach reach and scan](#active-visual-exploration-and-next-best-view-control-for-unknown-object-approach-reach-and-scan)
3. [Benchmarks datasets evaluation protocols and open research gaps](#benchmarks-datasets-evaluation-protocols-and-open-research-gaps)
4. [Force feedback impedance control contour following and compliant contact exploration](#force-feedback-impedance-control-contour-following-and-compliant-contact-exploration)
5. [Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects](#foundation-model-vlm-and-vla-methods-for-zero-shot-interaction-with-unseen-objects)
6. [Integrated multimodal systems combining vision tactile and force feedback](#integrated-multimodal-systems-combining-vision-tactile-and-force-feedback)
7. [Reinforcement learning for unknown object exploration touch and manipulation](#reinforcement-learning-for-unknown-object-exploration-touch-and-manipulation)
8. [Tactile-guided reaching contact localization and active haptic exploration of unknown objects](#tactile-guided-reaching-contact-localization-and-active-haptic-exploration-of-unknown-objects)

## Active 3D reconstruction scanning and object-centric mapping with a single manipulator-mounted sensor

### Subproblem Definition
Methods in which a single robot manipulator actively acquires observations with a manipulator-mounted sensor, or tightly coupled in-hand sensing on that manipulator, to reconstruct an unknown object or local object geometry for downstream approach, grasping, placement, or manipulation. Core scope includes eye-in-hand RGB or RGB-D scanning, wrist-camera plus tactile in-hand reconstruction, active tactile exploration, TSDF or point-cloud fusion, neural implicit SDF or occupancy models, NeRF-like object models, and emerging Gaussian-splatting object representations. Borderline systems that require fixed external cameras, multi-camera arrays, mobile-base scene mapping, or passive one-shot reconstruction are treated as adjacent rather than core.

### Problem Formulations
- Active next-best-view scanning of a tabletop object with an eye-in-hand camera to maximize surface coverage or reduce model uncertainty.
- In-hand visuo-tactile SLAM, where the robot jointly estimates object pose and local geometry while the object moves relative to the fingers.
- Active tactile exploration, where sparse contacts are sequenced to cover unknown object surfaces under limited sensor footprint and action budget.
- Reconstruction-for-manipulation, where the learned object model is only required to be good enough for grasp selection, constrained placement, pose tracking, or downstream approach planning rather than full watertight scanning.
- Lifelong object model accumulation and reuse, where a robot improves future manipulation of re-encountered objects by reusing a previously reconstructed representation.
- High-fidelity automated digitization, where a robot arm actively plans viewpoints to produce photorealistic and geometrically accurate object assets.

### Sensing Modalities
- Hand-eye or wrist-mounted RGB-D | details: Used for active scanning, segmentation-backed object tracking, and dense geometric fusion in systems such as the lifelong TSDF pipeline and BundleSDF.
- Hand-eye or wrist-mounted RGB | details: Used in NeRF-based and photorealistic reconstruction pipelines such as ActNeRF and Auto3R, often with known robot kinematics to recover camera poses.
- Vision-based tactile sensors | details: DIGIT, GelSight, or related optical tactile sensors provide local depth or contact geometry in FingerSLAM, VTacO, TouchSDF, Touch2Shape, and tactile-informed Gaussian methods.
- Proprioception and hand kinematics | details: Robot joint states, finger kinematics, and grasp state are used to register touch observations, maintain pose graphs, and constrain active exploration trajectories.
- Semantic masks or object segmentation | details: Object-centric visual pipelines often assume object masks, first-frame segmentation, or known target isolation before reconstruction or planning.
- Rendered uncertainty signals | details: Many active methods convert model uncertainty, entropy, or expected information gain into action scores for view selection, reorientation, or stopping.

### Action Space And Robot Setup
- The dominant embodiment is a fixed-base single arm observing a tabletop object with a hand-eye or wrist-mounted camera.
- A second cluster uses multi-fingered hands or grippers with fingertip tactile sensors and a wrist camera for in-hand reconstruction.
- Common actions are viewpoint changes over a reachable hemisphere, local pose optimization for next-best-view, contact probing over uncertain surface regions, in-hand object rotation, and occasional grasp-and-reorient steps that preserve the single-manipulator assumption.
- Inference from sources: the most capable systems use mixed action spaces rather than pure camera motion, because a single arm cannot expose bottoms or self-occluded surfaces by view motion alone.

### Method Families
- TSDF and explicit fusion with model reuse | representative methods: ['Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation'] | strength: Fast, manipulation-oriented, and directly usable for collision checking and pose tracking. | weakness: Typically lower fidelity and more sensitive to partial observability than newer neural representations.
- Visuo-tactile pose-graph reconstruction | representative methods: ['FingerSLAM', 'Visual-Tactile Sensing for In-Hand Object Reconstruction', 'NeuralFeels'] | strength: Can recover hidden local geometry during contact and remains useful under visual occlusion. | weakness: Coverage grows slowly, calibration is demanding, and local tactile observations must be registered accurately.
- Active tactile exploration | representative methods: ['AcTExplore', 'Touch2Shape'] | strength: Well matched to local surface discovery where camera views are insufficient. | weakness: Action efficiency and sim-to-real transfer are still limiting factors.
- Neural implicit object fields | representative methods: ['BundleSDF', 'TouchSDF', 'NeuralFeels'] | strength: Compact continuous geometry with better surface interpolation than raw volumetric grids. | weakness: Online optimization, pose drift, and extraction of planning-ready collision geometry remain costly.
- NeRF-based active reconstruction for manipulation | representative methods: ['ActNeRF', 'Auto3R'] | strength: High photorealism and uncertainty maps that naturally support next-best-view scoring. | weakness: Training cost, pose dependence, and incomplete access to hidden surfaces without physical reorientation.
- Gaussian-splatting object reconstruction | representative methods: ['Snap-it, Tap-it, Splat-it', 'ObjSplat'] | strength: Faster rendering and increasingly geometry-aware active planning. | weakness: Still early for robotic deployment, with limited standardized manipulation evaluation.

### Representative System Pipelines
- Item | system: Lu et al. lifelong TSDF reuse | pipeline: Segment object from RGB-D observations, fuse an object TSDF online, track pose with a particle-filter variant, store the model in an object memory, then reuse and register that model when the object reappears to reduce future active perception burden.
- Item | system: FingerSLAM | pipeline: Combine wrist-camera observations with fingertip tactile images in a factor graph, use odometry plus loop closure to estimate object pose, and stitch local tactile point clouds into a growing object surface model.
- Item | system: VTacO / VTacOH | pipeline: Train in the VT-Sim environment, infer rigid or deformable object geometry from visual-tactile hand interaction, and transfer the learned reconstruction model to real-world in-hand cases.
- Item | system: BundleSDF | pipeline: Use segmented RGB-D video to jointly optimize object pose and a neural object field, maintain memory frames and object detections, then recover a mesh and stable 6-DoF tracking for previously unknown objects.
- Item | system: AcTExplore | pipeline: Use reinforcement learning to select tactile probing motions that maximize reconstruction progress under a limited step budget, integrating each new contact into a growing surface estimate.
- Item | system: NeuralFeels | pipeline: Fuse vision, touch, and proprioception into an online neural field plus pose graph during in-hand manipulation, continuously refining both object geometry and object pose under occlusion.
- Item | system: ActNeRF / Auto3R | pipeline: Render uncertainty from a partially learned object radiance field, choose either a new visual viewpoint or a reorientation-enabled observation, retrain the object model incrementally, and use the resulting geometry for downstream manipulation or asset creation.

### Evaluation Tasks
- Unknown object surface reconstruction from active views.
- In-hand pose tracking plus geometry reconstruction under occlusion.
- Active tactile exploration under a limited number of touches or time steps.
- Object model reuse across repeated pick-and-place or constrained placement episodes.
- Transparent or reflective object grasping where the learned object model drives a downstream planner.
- Photorealistic robot-arm scanning and digitization of real objects.

### Common Metrics
- Chamfer Distance and related point-to-surface reconstruction error metrics.
- F-score for reconstructed surfaces or depth-based surface agreement.
- IoU or surface coverage metrics for exploration completeness.
- PSNR and novel-view rendering quality for NeRF-like methods.
- Pose error or drift, typically in millimeters or degrees, for in-hand tracking systems.
- Grasp success rate or task success rate when reconstruction feeds manipulation.
- Number of views, path length, or number of tactile contacts required to reach a target quality.

### Best Reported Capabilities
- AcTExplore reports 95.97% average IoU coverage on unseen YCB objects after being trained only on primitive shapes, showing that active tactile exploration can generalize beyond its training object set.
- NeuralFeels reports 81% final reconstruction F-score, 4.7 mm pose drift, and up to 94% tracking improvement under heavy occlusion across 70 real experiments, showing that online visuo-tactile neural fields can stay stable during in-hand interaction.
- ActNeRF reports 14% higher PSNR, 20% higher surface F-score, and 71% higher downstream task success than its comparison methods in simulated tabletop manipulation with reorientation actions.
- Auto3R demonstrates robot-arm deployment for automated scanning of real objects, including non-Lambertian and specular objects, and positions data-driven uncertainty prediction as a practical way to reduce human scan planning effort.
- Adjacent but influential evidence: Dex-NeRF achieves 90% and 100% physical grasp success in transparent-object settings using radiance-field geometry for grasp planning, showing that object-centric neural fields can directly support manipulation even when visual geometry is difficult.

### Failure Modes And Limitations
- Single-arm eye-in-hand systems struggle to observe bottoms, back sides, and narrow concavities without reorientation or contact.
- Visual-only neural fields remain brittle under pose error, poor segmentation, specular highlights, and transparent materials.
- Tactile systems acquire geometry slowly because each contact only reveals a local patch; policy quality matters as much as representation quality.
- Most evaluations use isolated tabletop objects or already-grasped objects rather than cluttered scenes with distractors and contact-rich uncertainty.
- Planning-ready geometry extraction is still a weak point for NeRF and Gaussian methods; many papers show attractive reconstructions but limited evidence on collision-safe deployment.
- Reproducibility is uneven because real systems depend on calibration, tactile sensor fabrication, object handling skills, and robot-specific control stacks.

### Representative Papers 2021 2026
- Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation | authors: Shiyang Lu, Rui Wang, Yinglong Miao, Chaitanya Mitash, Kostas E. Bekris | year: 2022 | venue: ICRA 2022 | url: https://arxiv.org/abs/2109.13910 | why it matters: A clean in-scope baseline for explicit object-centric mapping with a single manipulation system: it uses TSDF object models, tracks them online, and reuses them later to reduce future perception effort.
- FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback | authors: Jialiang Zhao, Maria Bauza, Edward H. Adelson | year: 2023 | venue: ICRA 2023 | url: https://arxiv.org/abs/2303.07997 | why it matters: One of the clearest demonstrations that a wrist camera plus fingertip tactile sensing can jointly localize and reconstruct unknown in-hand objects in a closed loop.
- Visual-Tactile Sensing for In-Hand Object Reconstruction | authors: Wenqiang Xu, Zhenjun Yu, Han Xue, Ruolin Ye, Siqiong Yao, Cewu Lu | year: 2023 | venue: CVPR 2023 | url: https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Visual-Tactile_Sensing_for_In-Hand_Object_Reconstruction_CVPR_2023_paper.html | why it matters: Introduces VTacO and VTacOH plus the VT-Sim environment, making visual-tactile in-hand reconstruction more reproducible and extending the scope to deformable objects.
- BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects | authors: Bowen Wen, Jonathan Tremblay, Valts Blukis, Stephen Tyree, Thomas Muller, Alex Evans, Dieter Fox, Jan Kautz, Stan Birchfield | year: 2023 | venue: CVPR 2023 | url: https://research.nvidia.com/publication/2023-06_bundlesdf-neural-6-dof-tracking-and-3d-reconstruction-unknown-objects | why it matters: A major step for object-centric neural fields in robotics: it couples unknown-object tracking with reconstruction from RGB-D video and provides a practical bridge from object videos to usable object meshes.
- AcTExplore: Active Tactile Exploration on Unknown Objects | authors: Amir-Hossein Shahidzadeh, Seong Jong Yoo, Pavan Mantripragada, Chahat Deep Singh, Cornelia Fermuller, Yiannis Aloimonos | year: 2024 | venue: ICRA 2024 | url: https://prg.cs.umd.edu/AcTExplore | why it matters: A representative active tactile exploration paper that explicitly optimizes probing actions for reconstruction quality and demonstrates strong generalization to unseen YCB objects.
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | authors: Sudharshan Suresh, Tzu-Yu Chiu, Ivan F. Garcia, Yashraj Narang, Michael R. Walter, Aaron M. Johnson, Animesh Garg [author list condensed in available source materials] | year: 2024 | venue: Science Robotics | url: https://github.com/facebookresearch/neuralfeels | why it matters: Pushes beyond static reconstruction into online in-hand perception, showing that a neural field can be maintained live during manipulation using vision, touch, and proprioception.
- TouchSDF: A DeepSDF Approach for 3D Shape Reconstruction using Vision-Based Tactile Sensing | authors: Mauro Comi, Yijiong Lin, Alex Church, Alessio Tonioni, Laurence Aitchison, Nathan F. Lepora | year: 2023 | venue: Touch Processing Workshop 2023 / arXiv | url: https://arxiv.org/abs/2311.12602 | why it matters: A clear example of bringing continuous SDF representations into tactile robotics, using local touch-derived point clouds to infer a global object shape.
- Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions | authors: Saptarshi Dasgupta, Akshat Gupta, Shreshth Tuli, Rohan Paul | year: 2024 | venue: arXiv preprint; accepted poster in ICRA 2024 RoboNeRF workshop | url: https://arxiv.org/abs/2404.01812 | why it matters: Directly targets the single-manipulator setting by allowing both visual view changes and physical reorientation actions, and shows that object-centric radiance fields can support downstream manipulation.
- Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces | authors: Mauro Comi, Alessio Tonioni, Max Yang, Jonathan Tremblay, Valts Blukis, Yijiong Lin, Nathan F. Lepora, Laurence Aitchison | year: 2025 | venue: Google Research publication page / arXiv preprint | url: https://arxiv.org/abs/2403.20275 | why it matters: An important frontier paper showing how touch can regularize Gaussian splatting for glossy or reflective objects where purely visual reconstructions are unreliable.
- Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction | authors: Yuanbo Wang, Zhaoxuan Zhang, Jiajin Qiu, Dilong Sun, Zhengyu Meng, Xiaopeng Wei, Xin Yang | year: 2025 | venue: CVPR 2025 | url: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html | why it matters: Marks the shift from reconstructing after touch to using a learned latent shape prior for both reconstruction and active touch policy learning.
- Auto3R: Automated 3D Reconstruction and Scanning via Data-driven Uncertainty Quantification | authors: Chentao Shen, Sizhe Zheng, Bingqian Wu, Yaohua Feng, Yuanchen Fei, Mingyu Mei, Hanwen Jiang, Xiangru Huang | year: 2025 | venue: arXiv preprint | url: https://arxiv.org/abs/2512.04528 | why it matters: A strong recent example of arm-mounted active scanning driven by learned uncertainty prediction, with explicit attention to real robot digitization and hard materials.

### 2026 Preprints
- ObjSplat: Geometry-Aware Gaussian Surfels for Active Object Reconstruction | authors: Yuetao Li, Zhizhou Jia, Yu Zhang, Qun Hao, Shaohui Zhang | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.06997 | why it matters: A very recent signal that active robotic reconstruction is moving toward geometry-aware Gaussian object models and multi-step next-best-path planning, which could be attractive for future manipulator-mounted scanners because Gaussian rendering is faster than classic NeRF training.

### Seminal Precursors Pre 2021
- KinectFusion: Real-Time Dense Surface Mapping and Tracking | authors: Richard A. Newcombe, Shahram Izadi, Otmar Hilliges, David Molyneaux, David Kim, Andrew J. Davison, Pushmeet Kohli, Jamie Shotton, Steve Hodges, Andrew Fitzgibbon | year: 2011 | venue: ISMAR 2011 | url: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/ismar_2011.pdf | why it matters: Established real-time dense TSDF-style fusion as a practical robot mapping primitive; later object-centric TSDF pipelines inherit this explicit volumetric mindset.
- Manipulator and Object Tracking for In-Hand 3D Object Modeling | authors: Michael Krainin, Peter Henry, Xiaofeng Ren, Dieter Fox | year: 2011 | venue: The International Journal of Robotics Research | url: https://rse-lab.cs.washington.edu/projects/3d-in-hand/ | why it matters: A foundational manipulator-centric object modeling paper: it jointly reasons about the robot hand and the object while building 3D models from in-hand sensing.
- Autonomous Generation of Complete 3D Object Models Using Next Best View Manipulation Planning | authors: Michael Krainin, Brian Curless, Dieter Fox | year: 2011 | venue: ICRA 2011 | url: https://ai.cs.washington.edu/www/media/papers/nbv-icra-11-final.pdf | why it matters: A direct precursor to modern active object scanning with manipulators: it formalized next-best-view and re-grasp planning to complete object models.
- DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation | authors: Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, Steven Lovegrove | year: 2019 | venue: CVPR 2019 | url: https://arxiv.org/abs/1901.05103 | why it matters: Provided the continuous signed-distance representation later adapted by tactile and robotic object-centric mapping papers such as TouchSDF and several neural field approaches.
- NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | authors: Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, Ren Ng | year: 2020 | venue: ECCV 2020 | url: https://arxiv.org/abs/2003.08934 | why it matters: Introduced the radiance-field representation that later enabled object-centric active reconstruction and reconstruction-for-manipulation pipelines such as Dex-NeRF, ActNeRF, and Auto3R.

### Trends 2021 To 2026
- 2021-2022: object-centric robotic reconstruction is still dominated by explicit models and task-facing pipelines, with TSDF reuse and specialized NeRF pipelines for hard perception cases such as transparent objects.
- 2023: the field shifts toward object-level neural representations and stronger multimodal fusion, especially visuo-tactile in-hand reconstruction and joint tracking plus reconstruction.
- 2024: active uncertainty-driven loops become more explicit; tactile exploration and manipulator-aware NeRF planning both use model uncertainty to choose actions rather than just fusing passively collected data.
- 2025: diffusion and Gaussian-based object models start to matter, especially when touch is needed for local detail or when faster rendering is valuable for active planning.
- Early 2026: preprints indicate a move toward geometry-aware Gaussian surfels and multi-step path planning, suggesting that the next phase may combine real-time rendering with stronger geometric guarantees.
- Inference from sources: the center of gravity is moving from generic full reconstruction toward task-sufficient object models that can be built quickly, updated online, and directly queried by a manipulation planner.

### Datasets And Benchmarks
- YCB object set and unseen YCB evaluation | role: Widely used for active tactile exploration and unknown-object manipulation; AcTExplore reports quantitative generalization on unseen YCB objects.
- VT-Sim | role: Simulation environment introduced by VTacO for rigid and deformable hand-object visual-tactile reconstruction, with released codes, models, datasets, and simulation tools.
- HO3D, YCBInEOAT, and BEHAVE | role: Object tracking and reconstruction benchmarks used by BundleSDF to evaluate unknown-object tracking and neural reconstruction.
- FeelSight | role: Dataset released with NeuralFeels, supporting real-world visuo-tactile in-hand perception studies.
- Transparent-object datasets from Dex-NeRF | role: Adjacent but influential benchmarks showing how reconstructed neural object models can enable manipulation of visually difficult transparent objects.
- Task-specific real robot scans | role: Many recent systems, including Auto3R and TouchSDF, rely on internal real-robot test sets rather than a shared benchmark; this remains a weakness of the subtopic.

### Research Gaps
- A shared benchmark that jointly measures scan quality, action cost, stopping efficiency, and downstream manipulation benefit is still missing.
- Most systems do not handle cluttered multi-object scenes where the target object is partially blocked before scanning begins.
- Stopping criteria are often heuristic; calibrated uncertainty that predicts task success remains underdeveloped.
- Single-arm full-coverage reconstruction without external cameras or handovers remains fundamentally hard and still lacks strong general solutions.
- Many neural methods reconstruct attractive geometry but do not expose robust collision models, grasp affordances, or contact-stable local surface estimates in a planner-friendly form.
- Tactile exploration still suffers from slow coverage, policy transfer issues, and limited public data diversity.
- Reflective, transparent, and deformable objects remain split across separate subliteratures instead of being handled by one unified active mapping stack.

### Opportunities For Single Manipulator Systems
- Use a two-layer representation: maintain a fast explicit occupancy or TSDF shell for planning and safety, while refining only the target object with an implicit or Gaussian model where uncertainty is high.
- Treat contact as a sparse but high-value sensing action rather than a fallback; touch should be invoked only for occluded, reflective, or manipulation-critical regions.
- Exploit object memory and model reuse aggressively, because repeated household and warehouse objects make one-shot full rescanning unnecessary.
- Plan for task-sufficient reconstruction instead of full watertight models, for example by focusing on graspable rims, support surfaces, insertion features, or collision-critical envelopes.
- Combine view planning and reorientation planning in one action space, since a single arm's main limitation is not sensing quality but inaccessible viewpoints.
- Adopt faster Gaussian or hybrid field renderers only if they are coupled to geometry-aware uncertainty, otherwise they risk improving appearance more than manipulation usefulness.

### Sources
- Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation | url: https://arxiv.org/abs/2109.13910 | type: primary paper | notes: Abstract, authors, TSDF representation, and lifelong object-memory framing.
- dblp record for Online Object Model Reconstruction and Reuse for Lifelong Improvement of Robot Manipulation | url: https://dblp.org/rec/conf/icra/LuWMMB22 | type: bibliographic record | notes: Venue and page numbers for ICRA 2022.
- FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback | url: https://arxiv.org/abs/2303.07997 | type: primary paper | notes: Abstract, authors, wrist-camera plus tactile setup, and real-world evaluation summary.
- dblp record for FingerSLAM | url: https://dblp.org/rec/conf/icra/ZhaoBA23 | type: bibliographic record | notes: Venue and page numbers for ICRA 2023.
- Visual-Tactile Sensing for In-Hand Object Reconstruction | url: https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Visual-Tactile_Sensing_for_In-Hand_Object_Reconstruction_CVPR_2023_paper.html | type: primary paper | notes: Official CVPR page with authors, abstract, and VT-Sim/VTacO framing.
- BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects | url: https://research.nvidia.com/publication/2023-06_bundlesdf-neural-6-dof-tracking-and-3d-reconstruction-unknown-objects | type: official publication page | notes: Authors, publication date, venue, and project link.
- AcTExplore project page | url: https://prg.cs.umd.edu/AcTExplore | type: official project page | notes: ICRA 2024 venue, abstract, code, and reported tactile exploration results.
- AcTExplore arXiv / PDF entry | url: https://prg.cs.umd.edu/research/AcTExplore_files/AcTExplore.pdf | type: paper PDF | notes: Project PDF used for quantitative details.
- NeuralFeels official repository | url: https://github.com/facebookresearch/neuralfeels | type: official repository | notes: Paper title, Science Robotics venue, code, dataset, and model links.
- TouchSDF project page | url: https://touchsdf.github.io/ | type: official project page | notes: Authors, task framing, code link, and tactile-to-DeepSDF pipeline description.
- TouchSDF arXiv page | url: https://arxiv.org/abs/2311.12602 | type: primary paper | notes: Abstract and arXiv metadata.
- ActNeRF project page | url: https://actnerf.github.io/ | type: official project page | notes: Core source for task setup, action space, reported gains, and comparison to ActiveNeRF.
- ActNeRF arXiv page | url: https://arxiv.org/abs/2404.01812 | type: primary paper | notes: Abstract and authors.
- ActiveNeRF: Learning where to See with Uncertainty Estimation | url: https://arxiv.org/abs/2209.08546 | type: background paper | notes: Used to trace uncertainty-driven active NeRF influence cited directly by ActNeRF.
- Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces | url: https://arxiv.org/abs/2403.20275 | type: primary paper | notes: Abstract and authors for tactile-informed Gaussian reconstruction.
- Google Research page for Snap-it, Tap-it, Splat-it | url: https://research.google/pubs/snap-it-tap-it-splat-it-tactile-informed-3d-gaussian-splatting-for-reconstructing-challenging-surfaces/ | type: official publication page | notes: High-level summary and publication-year context.
- Touch2Shape official CVPR 2025 page | url: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html | type: primary paper | notes: Authors, venue, abstract, and exploration-plus-reconstruction framing.
- Auto3R arXiv page | url: https://arxiv.org/abs/2512.04528 | type: primary paper | notes: Authors, abstract, and explicit robot-arm deployment claim.
- ObjSplat arXiv page | url: https://arxiv.org/abs/2601.06997 | type: primary paper | notes: Authors, abstract, Gaussian surfels, and next-best-path planning.
- Dex-NeRF: Using a Neural Radiance Field to Grasp Transparent Objects | url: https://proceedings.mlr.press/v164/ichnowski22a.html | type: primary paper | notes: Used as adjacent evidence linking radiance-field object reconstruction to downstream manipulation.
- See-Then-Grasp: Object Full 3D Reconstruction via Two-Stage Active Robotic Reconstruction Using Single Manipulator | url: https://www.mdpi.com/2076-3417/15/1/272 | type: adjacent boundary paper | notes: Used to sharpen the exclusion boundary because it relies on a fixed external camera in the second stage.
- KinectFusion: Real-Time Dense Surface Mapping and Tracking | url: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/ismar_2011.pdf | type: primary precursor paper | notes: Foundational dense fusion precursor for explicit object mapping.
- Robotic In-Hand 3D Object Modeling | url: https://rse-lab.cs.washington.edu/projects/3d-in-hand/ | type: official project page | notes: Project page linking the 2011 IJRR and ICRA precursors for in-hand modeling and next-best-view planning.
- Autonomous Generation of Complete 3D Object Models Using Next Best View Manipulation Planning | url: https://ai.cs.washington.edu/www/media/papers/nbv-icra-11-final.pdf | type: primary precursor paper | notes: Manipulator-based next-best-view planning precursor.
- DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation | url: https://arxiv.org/abs/1901.05103 | type: primary precursor paper | notes: Continuous SDF representation precursor.
- NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | url: https://arxiv.org/abs/2003.08934 | type: primary precursor paper | notes: Radiance-field representation precursor for active object-centric NeRF methods.

## Active visual exploration and next-best-view control for unknown object approach reach and scan

### Subproblem Definition
This subtopic covers robot-guided active perception methods that choose new camera viewpoints, and in some cases touch or reorientation actions, to reduce uncertainty about a previously unseen rigid object or object-centric scene region so the robot can scan, approach, touch, or grasp it. The boundary includes eye-in-hand RGB/RGB-D scanning, object-centric next-best-view (NBV) planning, active neural-field reconstruction, visuo-haptic completion, and active view selection for occluded target grasping; it excludes passive single-shot perception, large-scale navigation-only exploration, and manipulation papers that do not actively choose views or information-gathering actions [S1,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S20].

### Problem Formulations
- Iterative NBV for unknown-object reconstruction: choose the next camera pose from a partial explicit or implicit object model to maximize expected information gain, surface coverage, or uncertainty reduction under motion cost [S3,S4,S5,S8,S13].
- One-shot view planning: predict a set of views and a shortest connecting path at once from an initial sparse observation, point cloud, or even a single RGB image, then reconstruct after data capture [S9,S10,S12,S15].
- Interactive visuo-haptic exploration: choose where to touch, poke, or reorient the object based on uncertainty in the current visual belief so hidden surfaces become observable [S1,S6,S11].
- Target-oriented active grasping under occlusion: choose views that reveal target grasp affordances or spatial relationships well enough to execute a grasp on an unseen or heavily occluded object [S7,S14].
- Semantic-targeted active implicit reconstruction: bias exploration toward objects of interest rather than uniform scene coverage, using semantics and uncertainty jointly in the utility [S20].

### Sensing Modalities
- RGB-only sensing is common in neural-rendering and one-shot methods such as NeU-NBV, PRV, DM-OSVP, and VISO-Grasp [S5,S10,S12,S14].
- RGB-D or point-cloud sensing remains common in explicit NBV and visuo-haptic methods such as Act-VH, GMC, PB-NBV, and STAIR [S1,S8,S13,S20].
- Touch or contact sensing is used as an active information source in Act-VH, Poking, and ActNeRF, often alongside force closure or contact-event detection through the manipulator [S1,S6,S11].
- Robot proprioception, known camera poses, and pose re-estimation after interaction are important for closing the loop in ActNeRF and related manipulation-aware systems [S11].
- Foundation-model or language-conditioned semantic signals appear in the 2025 VISO-Grasp system, where they support spatial reasoning and object-centric active view planning [S14].

### Action Space And Robot Setup
- Most systems use a single manipulator or camera rig to move an RGB or RGB-D sensor around a tabletop object, with candidate viewpoints sampled on a sphere, hemisphere, or reachable free-space manifold [S3,S4,S5,S8,S10,S12,S13].
- Eye-in-hand setups are explicit in papers such as the RA-L 2022 uncertainty-guided NeRF policy, which uses a mobile robot with an arm-held camera, and in ActNeRF with a Franka manipulator [S3,S11].
- The action space can include more than camera motion: Act-VH chooses touch locations, Poking performs object-discovery pokes, and ActNeRF chooses between a visual action and a grasp-and-reorient action [S1,S6,S11].
- For grasping in clutter, ACE-NBV and VISO-Grasp use object-centric observation moves that seek views aligned with grasp affordances or target visibility constraints before attempting the grasp [S7,S14].
- One-shot methods reduce repeated online replanning by predicting all needed views and then optimizing a global path through them [S9,S10,S12].

### Method Families
- Probabilistic explicit-map NBV: iterative selection from partial voxel maps using coverage, entropy, or information gain, often with motion-cost terms [S8,S13,S17].
- Implicit or neural-field NBV: uncertainty is estimated from occupancy fields or radiance fields, and the next view is selected to reduce rendering or geometric uncertainty [S3,S4,S5,S20].
- One-shot/global view planning: supervised prediction of all views at once, sometimes with set-covering labels, predicted view counts, or diffusion-generated geometric priors [S9,S10,S12,S15].
- Visuo-haptic interactive exploration: the robot chooses touches, pokes, or reorientation actions to reveal hidden object surfaces [S1,S6,S11].
- Task-aware active grasping: the utility is defined by target grasp affordance, visibility, or target-aware spatial reasoning rather than pure surface coverage [S7,S14].

### Representative System Pipelines
- Act-VH | pipeline: Partial point cloud -> implicit surface reconstruction with uncertainty -> choose highest-uncertainty touch location -> execute touch and fuse new information -> use improved shape for grasping. | source ids: ['S1', 'S2']
- NeU-NBV | pipeline: Collected RGB images -> image-based neural rendering with uncertainty estimation -> evaluate candidate views in a mapless way -> move camera to the most uncertain informative view -> iterate under a measurement budget. | source ids: ['S5', 'S21']
- OSVP and PRV line | pipeline: Initial sparse observation or partial point cloud -> predict required number of views or directly predict a view set -> compute globally shortest path through the set -> collect all views -> reconstruct with an implicit model or NeRF. | source ids: ['S9', 'S10', 'S15']
- ActNeRF | pipeline: Partial NeRF ensemble -> estimate uncertainty and action feasibility -> choose either a visual observation action or a grasp-and-reorient action -> reacquire pose after reorientation -> continue until model quality is good enough for manipulation. | source ids: ['S11']
- VISO-Grasp | pipeline: Foundation-model-assisted object-centric spatial belief -> active view planning to resolve target invisibility and occlusion -> multi-view uncertainty-aware grasp fusion -> execute 6-DoF target grasp with sequential replanning if needed. | source ids: ['S14']

### Evaluation Tasks
- Unknown object 3D reconstruction or shape completion in simulation and on real robots [S1,S3,S4,S5,S8,S9,S10,S12,S13].
- Measurement-efficient scanning: reaching a reconstruction-quality or coverage target with fewer views, shorter paths, or lower planning time [S8,S9,S10,S12,S13].
- Interactive object discovery or completion through poking, touching, or reorientation [S1,S6,S11].
- Downstream grasping of previously unseen or occluded targets after active sensing [S1,S6,S7,S11,S14].
- Semantic-targeted active reconstruction in scenes containing objects of interest rather than uniform scene coverage [S20].

### Common Metrics
- Surface coverage or point-cloud coverage for unknown-object scan completeness [S8,S13,S16,S17].
- Reconstruction accuracy metrics such as F-score, geometry quality, or point-cloud/shape accuracy [S1,S4,S11].
- Novel-view or rendering metrics such as PSNR for neural-field models [S10,S11].
- Movement cost, travel distance, path length, planning time, or total computational time [S8,S10,S12,S13].
- Task success metrics such as grasp success rate, target-oriented grasp success, and number of grasp attempts [S1,S7,S11,S14].

### Best Reported Capabilities
- ActNeRF reports improvements of 14% in PSNR, 20% in F-score, and 71% in manipulation success for unseen orientations over its compared methods, showing that active view choice plus reorientation can directly benefit downstream manipulation [S11].
- PB-NBV reports the highest point-cloud coverage with low computational time among its compared frameworks in simulation, with supporting real-world feasibility experiments [S13].
- Act-VH reports better reconstruction than five baselines and significantly higher grasp success than the best reconstruction baseline on all 10 tested novel objects [S1,S2].
- PRV reports good reconstruction quality with significantly reduced movement cost and planning time compared to baselines, showing the value of predicting how many views are needed instead of scanning blindly [S10].
- VISO-Grasp reports 87.5% target-oriented grasping success with the fewest grasp attempts in real-world experiments under severe occlusion and invisibility constraints [S14].

### Failure Modes And Limitations
- Greedy iterative NBV can waste late-stage views on tiny residual regions and still leave holes or sparse surfaces, which motivated the shift toward global optimization and one-shot planning [S8].
- Visual-only neural or diffusion-based planners can struggle when the prior geometry is wrong, incomplete, or scale-ambiguous; DM-OSVP explicitly notes missing scale information and performance inadequacies in a test case, and it reports nontrivial generation and optimization overhead [S12].
- Purely visual exploration cannot reveal hidden support or bottom surfaces unless the object is touched or reoriented, which is exactly the limitation ActNeRF addresses [S11].
- Semantic-targeted methods can depend strongly on label quality; STAIR identifies accurate semantic labels as an assumption and noisy semantics as an open issue [S20].
- Inference from the source set: robustness to transparent, reflective, deformable, or dynamic objects remains weakly evidenced because most experiments use rigid tabletop objects with controlled sensing conditions [S1,S3,S4,S5,S8,S9,S10,S11,S12,S13,S14].

### Representative Papers 2021 2026
- Active Visuo-Haptic Object Shape Completion | authors: Lukas Rustler, Jens Lundell, Jan Kristof Behrens, Ville Kyrki, Matej Hoffmann | year: 2022 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2203.09149 | why it matters: A clean example of uncertainty-driven active touch: it uses visual shape uncertainty to choose where to touch an unseen object and shows downstream grasp gains on novel objects [S1,S2].
- Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields | authors: Soomin Lee, Le Chen, Jiahao Wang, Alexander Liniger, Suryansh Kumar, Fisher Yu | year: 2022 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2209.08409 | why it matters: One of the first robot-vision papers to formulate object NBV directly on a NeRF-style implicit representation with a ray-based uncertainty estimator [S3].
- Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization | authors: Dongyu Yan, Jianheng Liu, Fengyu Quan, Haoyao Chen, Mengmeng Fu | year: 2023 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2303.16739 | why it matters: Shows a continuous-manifold NBV optimizer over an implicit occupancy field, avoiding finite candidate-view selection and strengthening the implicit-reconstruction branch [S4].
- NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering | authors: Liren Jin, Xieyuanli Chen, Julius Rueckin, Marija Popovic | year: 2023 | venue: IROS 2023 | url: https://arxiv.org/abs/2303.01284 | why it matters: A mapless RGB-camera NBV planner using uncertainty in image-based neural rendering, important for active scanning without explicit maps [S5,S21].
- Perceiving Unseen 3D Objects by Poking the Objects | authors: Linghao Chen, Yunzhou Song, Hujun Bao, Xiaowei Zhou | year: 2023 | venue: ICRA 2023 | url: https://zju3dv.github.io/poking_perception/ | why it matters: Pushes the topic beyond passive view choice by using poking to discover and reconstruct unseen objects for later recognition and grasping [S6].
- Affordance-Driven Next-Best-View Planning for Robotic Grasping | authors: Xuechao Zhang, Dong Wang, Sun Han, Weichuang Li, Bin Zhao, Zhigang Wang, Xiaoming Duan, Chongrong Fang, Xuelong Li, Jianping He | year: 2023 | venue: Conference on Robot Learning | url: https://proceedings.mlr.press/v229/zhang23i.html | why it matters: Directly optimizes viewpoints for target grasp affordance under occlusion, making the downstream task itself the NBV objective [S7].
- Active Implicit Reconstruction Using One-Shot View Planning | authors: Hao Hu, Sicong Pan, Liren Jin, Marija Popovic, Maren Bennewitz | year: 2024 | venue: ICRA 2024 | url: https://arxiv.org/abs/2310.00685 | why it matters: Represents the transition from greedy iterative NBV to one-shot view-set prediction with implicit completion of small missing surfaces [S9].
- How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF? | authors: Sicong Pan, Liren Jin, Hao Hu, Marija Popovic, Maren Bennewitz | year: 2024 | venue: ICRA 2024 | url: https://www.hrl.uni-bonn.de/publications/2023/how-many-views-are-needed-to-reconstruct-an-unknown-object-using-nerf | why it matters: Turns active scanning into a budgeted planning problem by predicting the required number of views from object complexity, then optimizing the global view path [S10].
- Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions | authors: Saptarshi Dasgupta, Akshat Gupta, Shreshth Tuli, Rohan Paul | year: 2024 | venue: arXiv preprint; ICRA 2024 RoboNeRF workshop poster | url: https://arxiv.org/abs/2404.01812 | why it matters: Makes the active perception loop manipulation-aware by letting the robot decide between looking and physically reorienting the object [S11].
- Exploiting Priors from 3D Diffusion Models for RGB-Based One-Shot View Planning | authors: Sicong Pan, Liren Jin, Xuying Huang, Cyrill Stachniss, Marija Popovic, Maren Bennewitz | year: 2024 | venue: IROS 2024 | url: https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/pan2024iros.pdf | why it matters: Uses a single RGB image plus a diffusion-generated mesh prior to plan object-specific views, showing how generative priors can seed active scanning without depth [S12].
- PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects | authors: Zhizhou Jia, Yuetao Li, Qun Hao, Shaohui Zhang | year: 2025 | venue: IEEE Robotics and Automation Letters | url: https://pure.bit.edu.cn/en/publications/pb-nbv-efficient-projection-based-next-best-view-planning-framewo | why it matters: Emphasizes practical efficiency by replacing heavy ray-casting with projection-based quality evaluation while preserving strong coverage performance [S13].
- VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility | authors: Yitian Shi, Di Wen, Guanqi Chen, Edgar Welte, Sheng Liu, Kunyu Peng, Rainer Stiefelhagen, Rania Rayyes | year: 2025 | venue: IROS 2025 | url: https://arxiv.org/abs/2503.12609 | why it matters: A strong 2025 example of unifying active view planning, object-centric spatial belief, and target-aware 6-DoF grasping in severely occluded clutter [S14].

### Seminal Precursors Pre 2021
- A surface-based Next-Best-View approach for automated 3D model completion of unknown objects | authors: Simon Kriegel, Tim Bodenmueller, Michael Suppa, Gerd Hirzinger | year: 2011 | venue: ICRA 2011 | url: https://ieeexplore.ieee.org/document/5979947/ | why it matters: A classic object-model completion paper for unknown objects; it anchors the explicit-surface NBV tradition later extended by probabilistic and global-coverage methods [S16].
- An Adaptable, Probabilistic, Next-Best View Algorithm for Reconstruction of Unknown 3-D Objects | authors: Jeff Daudelin, Mark Campbell | year: 2017 | venue: IEEE Robotics and Automation Letters | url: https://ieeexplore.ieee.org/document/7835670 | why it matters: A widely cited probabilistic NBV baseline for unknown 3D objects, explicitly referenced by later non-model-based and global-coverage planners [S8,S17].
- Active Object Reconstruction Using a Guided View Planner | authors: Xin Yang, Yuanbo Wang, Yaru Wang, Baocai Yin, Qiang Zhang, Xiaopeng Wei, Hongbo Fu | year: 2018 | venue: IJCAI 2018 | url: https://www.ijcai.org/proceedings/2018/689 | why it matters: One of the clearer pre-2021 learning-based active reconstruction papers: it jointly reasons about view planning and 3D reconstruction from view sequences [S18].
- Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control | authors: Fereshteh Sadeghi, Alexander Toshev, Eric Jang, Sergey Levine | year: 2018 | venue: CVPR 2018 | url: https://research.google/pubs/sim2real-viewpoint-invariant-visual-servoing-by-recurrent-control/ | why it matters: Important for the approach/reach branch: it showed servoing to previously unseen objects from novel viewpoints without classical calibration-heavy visual servoing [S19].

### Trends 2021 To 2026
- 2022: active uncertainty estimation moved from explicit maps and touch heuristics into implicit representations and NeRF-style models, while visuo-haptic methods showed that pure vision is often not enough for downstream grasp reliability [S1,S3].
- 2023: the field diversified into continuous-manifold implicit NBV optimization, mapless RGB neural-rendering NBV, interactive poking-based discovery, and affordance-driven grasp-oriented view planning [S4,S5,S6,S7].
- 2024: one-shot planning became more prominent, with view-count prediction, implicit completion, semantic targeting, and diffusion priors all used to reduce online replanning and wasted camera motion [S9,S10,S12,S20].
- 2024 also strengthened manipulation-aware active perception: ActNeRF explicitly chooses between visual observations and reorientation actions instead of treating NBV as a purely visual problem [S11].
- 2025: there is clearer pressure toward operational efficiency and task integration, visible in PB-NBV's computational simplification and VISO-Grasp's direct integration of active views with target grasp execution in clutter [S13,S14].
- [uncertain] No clearly in-scope 2026 preprint tightly matching this subtopic was found in the searched primary-source set by 2026-03-23, so the 2026 part of the trend is currently an absence signal rather than a new paper cluster.

### Datasets And Benchmarks
- ShapeNet appears repeatedly in the reconstruction line, including PRV-related work and STAIR references [S10,S20].
- DM-OSVP relies on One-2-3-45++, which is trained on Objaverse, although Objaverse there is a prior-training source rather than the direct evaluation benchmark [S12].
- Many papers mix synthetic object sets with small real-world tabletop experiments instead of sharing a standard benchmark: this is explicit in Act-VH, GMC, Active Implicit Reconstruction, NeU-NBV, PRV, DM-OSVP, and PB-NBV [S1,S4,S5,S8,S10,S12,S13].
- ActNeRF evaluates in a simulated Franka tabletop environment with benchmark objects [S11].
- Inference from the source set: there is still no single community-standard benchmark that jointly measures active unknown-object scanning, motion efficiency, and downstream reach/grasp performance across papers [S1,S4,S5,S7,S8,S10,S11,S12,S13,S14].

### Research Gaps
- Inference from the source set: the field still lacks a common benchmark that forces a method to trade off view count, path length, scan quality, and downstream reach/grasp success in one protocol [S1,S4,S5,S7,S8,S10,S11,S12,S13,S14].
- A major open problem is unified action selection across view motion, touch, reorientation, and grasp execution; most papers optimize only one or two of these action types together [S1,S6,S7,S11,S14].
- Real-time performance remains an issue for neural-field and diffusion-prior methods, especially when geometry priors must be generated or optimized online [S12].
- Object-scale assumptions remain narrow; transparent, reflective, deformable, articulated, or highly cluttered scenes are still weakly covered by the source set [S1,S3,S4,S5,S8,S10,S11,S12,S13,S14].
- Stopping criteria and uncertainty calibration remain inconsistent across papers, which makes operational guarantees for 'scan enough and then act' systems weak [S3,S5,S10,S11,S20].

### Opportunities For Single Manipulator Systems
- A practical near-term stack for one arm is an eye-in-hand RGB-D or RGB camera with an object-centric uncertainty representation, a PB-NBV- or PRV-style motion-efficient view planner, and an optional single touch or flip action when uncertainty concentrates on support or bottom surfaces [S10,S11,S13].
- If compute is limited, explicit-map planners such as GMC or PB-NBV look more practical than diffusion-heavy or repeatedly retrained neural-field planners, while still matching the user's 'unknown object scan' setting well [S8,S13].
- If the downstream task is grasping in occlusion, ACE-NBV and VISO-Grasp suggest that the view utility should be task-conditioned on grasp affordance or target visibility rather than on uniform reconstruction quality alone [S7,S14].
- If only RGB is available, the Bonn one-shot line is especially promising because it shows a progression from fixed-pattern view-count prediction to object-specific RGB-only planning using diffusion priors [S10,S12].
- Inference from the source set: the most promising single-manipulator direction is a hybrid controller that begins with cheap global planning, then escalates to one or two manipulation actions only when the uncertainty map indicates hidden task-critical surfaces [S10,S11,S13,S14].

### Sources
- Active Visuo-Haptic Object Shape Completion | id: S1 | url: https://arxiv.org/abs/2203.09149 | type: arXiv page | notes: Abstract, authors, journal reference, and key results for Act-VH.
- Active Visuo-Haptic Object Shape Completion | id: S2 | url: https://research.fi/en/results/publication/0388789222 | type: official publication metadata page | notes: Venue, year, pages, DOI for the RA-L publication.
- Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields | id: S3 | url: https://arxiv.org/abs/2209.08409 | type: arXiv page | notes: Robot with arm-held camera, ray-based NeRF uncertainty, accepted RA-L 2022.
- Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization | id: S4 | url: https://arxiv.org/abs/2303.16739 | type: arXiv page | notes: Continuous-manifold NBV over implicit occupancy fields.
- NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering | id: S5 | url: https://arxiv.org/abs/2303.01284 | type: arXiv page | notes: Mapless RGB-camera NBV planning with neural-rendering uncertainty.
- Perceiving Unseen 3D Objects by Poking the Objects | id: S6 | url: https://zju3dv.github.io/poking_perception/ | type: official project page | notes: ICRA 2023 project page with abstract, code link, and citation block.
- Affordance-Driven Next-Best-View Planning for Robotic Grasping | id: S7 | url: https://proceedings.mlr.press/v229/zhang23i.html | type: official conference proceedings page | notes: CoRL 2023 paper page with abstract and bibliographic metadata.
- A global generalized maximum coverage-based solution to the non-model-based view planning problem for object reconstruction | id: S8 | url: https://www.sciencedirect.com/science/article/abs/pii/S1077314222001631 | type: official journal abstract page | notes: CVIU 2023 abstract, highlights, movement-cost trade-off, and code statement.
- Active Implicit Reconstruction Using One-Shot View Planning | id: S9 | url: https://arxiv.org/abs/2310.00685 | type: arXiv page | notes: ICRA 2024 one-shot view planning with implicit completion.
- How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF? | id: S10 | url: https://www.hrl.uni-bonn.de/publications/2023/how-many-views-are-needed-to-reconstruct-an-unknown-object-using-nerf | type: official project/publication page | notes: ICRA 2024 PRV paper with authors, DOI, and code link.
- Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions | id: S11 | url: https://arxiv.org/abs/2404.01812 | type: arXiv page | notes: ActNeRF abstract and quantitative results for visual plus reorientation actions.
- Exploiting Priors from 3D Diffusion Models for RGB-Based One-Shot View Planning | id: S12 | url: https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/pan2024iros.pdf | type: official paper PDF | notes: IROS 2024 PDF with authors, method details, failure case, and code link.
- PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects | id: S13 | url: https://pure.bit.edu.cn/en/publications/pb-nbv-efficient-projection-based-next-best-view-planning-framewo | type: official university publication page | notes: RA-L 2025 abstract, DOI, efficiency claim, and open-source statement.
- VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility | id: S14 | url: https://arxiv.org/abs/2503.12609 | type: arXiv page | notes: IROS 2025 paper with real-world success rate and code link.
- Sicong Pan publications page | id: S15 | url: https://psc0628.github.io/publications | type: author publication page | notes: Used to trace the SCVP, global max-flow, and one-shot planning lineage.
- A surface-based Next-Best-View approach for automated 3D model completion of unknown objects | id: S16 | url: https://ieeexplore.ieee.org/document/5979947/ | type: official IEEE page | notes: Pre-2021 precursor in explicit unknown-object model completion.
- An Adaptable, Probabilistic, Next-Best View Algorithm for Reconstruction of Unknown 3-D Objects | id: S17 | url: https://ieeexplore.ieee.org/document/7835670 | type: official IEEE page | notes: Pre-2021 probabilistic NBV precursor cited by later object-reconstruction work.
- Active Object Reconstruction Using a Guided View Planner | id: S18 | url: https://www.ijcai.org/proceedings/2018/689 | type: official conference proceedings page | notes: Pre-2021 learning-based active reconstruction precursor.
- Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control | id: S19 | url: https://research.google/pubs/sim2real-viewpoint-invariant-visual-servoing-by-recurrent-control/ | type: official publication page | notes: Pre-2021 active visual control precursor for unseen-object reaching.
- STAIR: Semantic-Targeted Active Implicit Reconstruction | id: S20 | url: https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/jin2024iros.pdf | type: official paper PDF | notes: Used for semantic-targeted active reconstruction, limitations, and influence mapping.
- NeU-NBV repository | id: S21 | url: https://github.com/dmar-bonn/neu-nbv | type: official code repository | notes: Confirms IROS 2023 acceptance, abstract, datasets, and code availability.

## Benchmarks datasets evaluation protocols and open research gaps

### Subproblem Definition
This subtopic reviews the public datasets, challenge tasks, benchmark suites, evaluation protocols, and unresolved benchmarking problems used to study autonomous interaction with unknown objects. The boundary includes object-centric active perception, tactile and force-based exploration, open-vocabulary and generalist manipulation benchmarks that explicitly test generalization to new objects or scenes, and sim-to-real evaluation frameworks. It excludes pure navigation benchmarks, static perception-only datasets with no interaction loop, and broad robot-learning corpora that do not materially inform evaluation of unknown-object interaction [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S19,S20,S21,S22].

### Problem Formulations
- Unknown-object shape acquisition: evaluate how efficiently a robot can reconstruct or cover an unseen object's geometry from views, touches, or both, often under a limited interaction budget [S2,S3,S19,S22].
- Target-oriented interaction under occlusion: benchmark whether active sensing leads to better grasping or retrieval of a previously unseen target in clutter or partial visibility [S4,S20,S21].
- Generalizable manipulation across object variation: define task families where policies must transfer across new instances, shapes, materials, and kinematic layouts rather than memorizing a fixed asset set [S5,S7,S10,S13].
- Open-vocabulary mobile manipulation: evaluate an end-to-end loop that must find, grasp, and place novel objects in novel homes from language instructions [S4,S24].
- Lifelong and multitask transfer: benchmark how well a learner reuses declarative and procedural knowledge as tasks accumulate, rather than only measuring single-task success [S7,S13].
- Sim-first proxy evaluation: test whether a simulated benchmark predicts real-world policy ranking and failure modes closely enough to reduce costly physical evaluation [S9,S12].
- Force-aware and tactile interaction: benchmark policies on contact-rich tasks where success depends on local force regulation, tactile interpretation, and safe control around uncertain geometry [S1,S2,S11,S14].

### Sensing Modalities
- RGB and RGB-D cameras remain the dominant benchmark inputs for active view planning, mobile manipulation, and generalist policy suites [S4,S5,S9,S10,S12,S13,S20,S21,S22].
- Optical tactile sensing is central in Tactile Gym 2.0 and AnyTouch 2, where DIGIT-, GelSight-, DigiTac-, and TacTip-style sensors are benchmarked or unified under shared evaluation tasks [S1,S14].
- Force and proprioceptive streams become first-class benchmark inputs in contact-rich work such as ForceVLA2 and in visuo-tactile reconstruction systems such as NeuralFeels [S2,S11].
- Point clouds, segmentation masks, and depth are explicitly supported in ManiSkill2, RLBench-derived styles of evaluation, and many object-centric reconstruction benchmarks [S5,S16,S22].
- Language instructions are integral in HomeRobot OVMM, VLABench, Open X-Embodiment, DROID, MobileManiBench, and RoboCasa365, reflecting the shift toward instruction-conditioned manipulation [S4,S6,S8,S10,S12,S13].
- Multi-view synchronized sensing is increasingly benchmarked, especially in DROID, MobileManiBench, ForceVLA2, and tactile foundation-model datasets [S8,S11,S12,S14].

### Action Space And Robot Setup
- Single-arm tabletop manipulation is still the default physical setup for active reconstruction and tactile exploration benchmarks, including Tactile Gym 2.0, Act-VH, AcTExplore, and many NBV papers [S1,S3,S19,S22].
- Eye-in-hand sensor motion is common when the benchmark measures view efficiency, surface coverage, or contact selection rather than only final task success [S2,S19,S22].
- Mobile manipulation appears as a distinct benchmark regime in HomeRobot OVMM, SIMPLER common setups, MobileManiBench, and RoboCasa365, where navigation and manipulation are evaluated together [S4,S9,S12,S13,S24].
- Benchmark action spaces increasingly mix Cartesian motion, gripper control, controller modes, and force-conditioned actions rather than plain end-effector deltas [S5,S9,S11,S12].
- Modern suites explicitly compare embodiments, for example Open X-Embodiment across 22 robots and MobileManiBench across two mobile platforms with different end-effectors [S6,S12].

### Method Families
- Shared physical-object and object-set benchmarks, such as YCB-backed unseen-object evaluations, anchor reproducible cross-lab comparison for rigid-object interaction [S3,S15,S19].
- Task-suite simulators such as ManiSkill2, LIBERO, RLBench, and RoboCasa365 package many task families under common APIs and reporting rules [S5,S7,S13,S16].
- Large-scale real-robot corpora such as Open X-Embodiment and DROID supply heterogeneous trajectories for pretraining and transfer evaluation across robots, scenes, and skills [S6,S8].
- Proxy-evaluation frameworks such as SIMPLER focus on ranking policies reproducibly in simulation while preserving real-world behavior trends [S9].
- Object-centric active perception benchmarks concentrate on coverage, uncertainty reduction, or downstream grasp gains on unknown objects [S2,S3,S19,S20,S21,S22].
- Tactile and force-aware datasets benchmark dynamic contact understanding, safe controller behavior, and contact-rich manipulation quality [S1,S2,S11,S14].
- Reasoning-heavy VLA benchmarks such as VLABench, MobileManiBench, and RoboCasa365 stress instruction following, long-horizon planning, and generalization under object and scene variation [S10,S12,S13].

### Representative System Pipelines
- Tactile Gym 2.0 | pipeline: Simulated optical tactile observations from TacTip, DIGIT, or DigiTac -> train RL or imitation policy on edge following, surface following, or pushing -> deploy on a low-cost 4-DoF real robot -> compare transfer performance across sensor types. | source ids: ['S1']
- NeuralFeels and FeelSight | pipeline: Vision + touch + proprioception -> online neural field and pose graph update -> evaluate reconstruction F-score, pose drift, and occlusion robustness on 70 released experiments -> use the result as a visuo-tactile perception benchmark. | source ids: ['S2']
- HomeRobot OVMM | pipeline: Language instruction + household scene observation -> navigate to find a novel object -> grasp it -> transport and place it on the target receptacle -> measure end-to-end sim and real success under open-vocabulary household variation. | source ids: ['S4', 'S24']
- SIMPLER | pipeline: Take a real-world manipulation policy -> match simulation visuals and control through texture matching and system identification -> run paired sim-and-real evaluations on common setups -> test whether simulation predicts real ranking and failure modes. | source ids: ['S9']
- MobileManiBench | pipeline: Generate large numbers of mobile-manipulation trajectories in Isaac Sim with synchronized multi-view sensing and rich annotations -> benchmark VLA models across objects, scenes, skills, and embodiments -> analyze data efficiency and generalization before real-world deployment. | source ids: ['S12']
- ForceVLA2 | pipeline: Multi-view images + task prompt + proprioception + force signals -> force-aware VLA predicts action chunks and hybrid force-position behavior -> evaluate across five contact-rich tasks with overload and stability failure modes explicitly considered. | source ids: ['S11']

### Evaluation Tasks
- Object pushing, edge following, and surface following for tactile sim-to-real comparison [S1].
- Unknown-object reconstruction and active tactile coverage on unseen objects, often using YCB instances or similar rigid assets [S2,S3,S19,S22].
- Target-oriented active grasping and 6-DoF grasp execution under clutter, invisibility, or occlusion [S20,S21].
- Open-vocabulary mobile manipulation in homes, including finding, grasping, transporting, and placing novel objects [S4,S24].
- Generalizable single-arm, dual-arm, mobile-base, rigid-body, and soft-body manipulation task families under a unified simulator interface [S5].
- Lifelong robot learning across growing task streams, where order, transfer, and forgetting matter in addition to success [S7].
- Cross-embodiment policy training and transfer over large real-robot datasets with many skills and scenes [S6,S8].
- Contact-rich tasks such as wiping, pressing, assembling, opening, closing, pulling, and pushing under force constraints [S11,S12,S13].
- Long-horizon language-conditioned reasoning tasks that require world knowledge, implicit intent understanding, and multi-step execution [S10].
- Sim-and-real paired evaluation to check whether simulator results predict real behavior across distribution shifts [S9].

### Common Metrics
- Task success rate remains the dominant metric across mobile manipulation, contact-rich manipulation, and multitask suites [S4,S5,S7,S9,S10,S11,S12,S13].
- Coverage and geometry metrics such as IoU, F-score, Chamfer-style reconstruction accuracy, or surface coverage are standard in active unknown-object exploration benchmarks [S2,S3,S19,S22].
- Pose drift or pose-estimation error is reported in visuo-tactile object understanding benchmarks such as NeuralFeels [S2].
- Budget-efficiency metrics such as number of views, touches, trajectory length, interaction steps, or planning time are used when the benchmark emphasizes efficient exploration rather than only end-state success [S3,S19,S22].
- Transfer metrics such as forward transfer, robustness to task ordering, and forgetting are central in lifelong suites like LIBERO [S7].
- Generalization metrics include performance on unseen objects, unseen scenes, new embodiments, and varied object instances [S3,S5,S6,S8,S12,S13].
- Simulation-to-real agreement or correlation is itself an evaluation target in SIMPLER, not just a background assumption [S9].
- Safety-oriented metrics such as overload reduction, unstable-contact reduction, or force-tracking quality are becoming more common in force-aware benchmarks [S11].
- Data-centric reporting such as number of trajectories, demonstrations, objects, tasks, scenes, and hours of interaction is heavily used to characterize benchmark scale and diversity [S6,S8,S11,S12,S13,S14].

### Best Reported Capabilities
- AcTExplore reports an average 95.97% IoU coverage on unseen YCB objects despite training on primitive shapes, showing that active tactile reconstruction benchmarks can already support strong unseen-object coverage in controlled settings [S3].
- NeuralFeels reports final reconstruction F-scores of 81%, average pose drift of 4.7 mm, and up to 94% tracking improvement over vision-only under heavy occlusion, demonstrating meaningful benchmark progress for visuo-tactile unknown-object perception [S2].
- Open X-Embodiment shows positive transfer across a 22-robot, 527-skill standardized dataset mixture, which is strong evidence that benchmark scale can improve cross-platform manipulation capability [S6].
- DROID demonstrates that large in-the-wild data diversity can improve policy performance and generalization relative to narrower real-world datasets [S8].
- SIMPLER provides evidence that benchmarked simulation can track real-world policy behavior strongly enough to be useful for scalable model comparison, which is a capability claim about evaluation methodology rather than task performance alone [S9].
- ForceVLA2 reports large gains over pi0 and pi0.5 across five contact-rich tasks while reducing arm overload and unstable contact, indicating that force-aware evaluation suites can expose capability gaps missed by position-only metrics [S11].
- RoboCasa365 scales benchmark diversity to 365 tasks across 2,500 kitchen environments with both human and synthetic demonstrations, enabling systematic studies of what drives generalization in household manipulation [S13].

### Failure Modes And Limitations
- Benchmark fragmentation is still severe: object-centric active exploration papers, tactile suites, generalist policy benchmarks, and mobile-manipulation challenges often report incompatible metrics and stopping rules [S1,S2,S3,S4,S5,S7,S9,S10,S11,S12,S13,S19,S20,S21,S22].
- Real-world evidence is thin relative to simulator scale. HomeRobot explicitly reports only 20% real-world baseline success, underscoring how much harder open-world evaluation remains than simulation-heavy benchmark results suggest [S4].
- Many benchmark suites still over-represent rigid household objects and under-represent deformable, transparent, reflective, slippery, or fragile unknown objects [S1,S3,S5,S13,S14,S18].
- Coverage-style metrics do not necessarily predict downstream utility; a benchmark can reward reconstruction quality without testing whether the robot can then grasp, insert, open, or safely manipulate the object [S2,S3,S19,S22].
- Large data benchmarks such as Open X-Embodiment and DROID broaden scale and diversity, but they do not by themselves solve standardized unknown-object evaluation because tasks, hardware, and annotations remain heterogeneous [S6,S8].
- Reasoning-heavy VLA benchmarks expose brittleness in current models, but many remain simulation-first and do not yet establish strong sim-to-real validity for unknown-object interaction [S10,S12,S13].
- Force and tactile benchmarks are improving quickly, yet dynamic contact data and public force-rich evaluation corpora remain much smaller and less standardized than RGB-centric resources [S1,S2,S11,S14].

### Representative Papers 2021 2026
- Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch | authors: Yijiong Lin, John Lloyd, Alex Church, Nathan F. Lepora | year: 2022 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2207.10763 | why it matters: A rare benchmark-first paper in tactile manipulation: it standardizes three tactile sensors, three physically interactive tasks, and sim-to-real comparison on accessible hardware [S1].
- ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills | authors: Jiayuan Gu, Fanbo Xiang, Xuanlin Li, Zhan Ling, Xiqiang Liu, Tongzhou Mu, Yihe Tang, Stone Tao, Xinyue Wei, Yunchao Yao, Xiaodi Yuan, Pengwei Xie, Zhiao Huang, Rui Chen, Hao Su | year: 2023 | venue: ICLR 2023 | url: https://arxiv.org/abs/2302.04659 | why it matters: It made unified interfaces and evaluation protocols a first-class benchmark contribution, covering 20 task families, 2000+ object models, and multiple manipulation regimes [S5].
- HomeRobot: Open-Vocabulary Mobile Manipulation | authors: Sriram Yenamandra, Arjun Ramachandran, Karmesh Yadav, Oleksandr Maksymets, Raghavendra Bura, Aaron Gokaslan, Manuela Veloso, Abhinav Gupta, Devendra Singh Chaplot | year: 2023 | venue: arXiv preprint | url: https://arxiv.org/abs/2306.11565 | why it matters: It turned unknown-object interaction into an end-to-end household benchmark with both simulation and real-world components instead of isolated grasp or perception tests [S4,S24].
- LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | authors: Bo Liu, Suraj Nair, Yuzhe Qin, Chelsea Finn, Sergey Levine, Li Fei-Fei, Jiajun Wu, Yuke Zhu | year: 2023 | venue: NeurIPS 2023 Datasets and Benchmarks Track | url: https://arxiv.org/abs/2306.03310 | why it matters: It shifted evaluation from static multitask scores to transfer, task ordering, and forgetting, which are important once unknown-object interaction is studied as continual skill accumulation [S7].
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models | authors: Open X-Embodiment Collaboration | year: 2023 | venue: ICRA 2024 | url: https://arxiv.org/abs/2310.08864 | why it matters: It standardized a heterogeneous real-robot data mixture across 22 robots and 527 skills, making cross-embodiment evaluation and transfer a mainstream benchmark topic [S6].
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | authors: Sudharshan Suresh, Shubham Chitnis, Ria Doshi, Russ Tedrake, Alberto Rodriguez, Phillip Isola, Edward Adelson, Pulkit Agrawal, Lerrel Pinto, Devendra Chaplot, Shuran Song, Saptarshi Das | year: 2024 | venue: Science Robotics | url: https://arxiv.org/abs/2312.13469 | why it matters: It released FeelSight and made visuo-tactile benchmarking more concrete by reporting reconstruction, pose-drift, and heavy-occlusion tracking metrics on a public evaluation set [S2].
- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | authors: Alexander Khazatsky and collaborators | year: 2024 | venue: RSS 2024 | url: https://arxiv.org/abs/2403.12945 | why it matters: It expanded real-world benchmark diversity to 76k trajectories over 564 scenes and 84 tasks, directly targeting the scene and task narrowness of prior robot datasets [S8].
- Evaluating Real-World Robot Manipulation Policies in Simulation | authors: Xuanlin Li, Tsung-Yen Yang, Quan Vuong, Ben Eysenbach, Karl Pertsch, Sergey Levine and collaborators | year: 2024 | venue: CoRL 2024 [uncertain] | url: https://arxiv.org/abs/2405.05941 | why it matters: It reframed benchmark design around reproducible policy verification, showing that a well-matched simulator can correlate strongly with real-world manipulation outcomes [S9].
- VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks | authors: Shiduo Zhang, Zhe Xu, Peiju Liu, Xiaopeng Yu, Yuan Li, Qinghui Gao, Zhaoye Fei, Zhangyue Yin, Zuxuan Wu, Yu-Gang Jiang, Xipeng Qiu | year: 2024 | venue: arXiv preprint | url: https://arxiv.org/abs/2412.18194 | why it matters: It argues that current benchmarks under-test world knowledge, implicit intent, and long-horizon reasoning, then operationalizes those pressures in 100 task categories with 2000+ objects [S10].
- VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility | authors: Yitian Shi, Di Wen, Guanqi Chen, Edgar Welte, Sheng Liu, Kunyu Peng, Rainer Stiefelhagen, Rania Rayyes | year: 2025 | venue: IROS 2025 | url: https://arxiv.org/abs/2503.12609 | why it matters: A strong object-centric benchmark paper for unknown-object interaction because it couples active perception, severe occlusion, and downstream 6-DoF grasp success in one protocol [S21].

### 2026 Preprints
- MobileManiBench: Simplifying Model Verification for Mobile Manipulation | authors: Wenbo Wang, Fangyun Wei, QiXiu Li, Xi Chen, Yaobo Liang, Chang Xu, Jiaolong Yang, Baining Guo | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.05233 | why it matters: Introduces a large-scale mobile-manipulation benchmark with 630 objects, 20 categories, 100+ tasks, 100 scenes, and 300K trajectories, directly targeting evaluation of VLA generalization before deployment [S12].
- AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception | authors: Xiaoyu Li, Jiale Li, Zijian Lei, Yuyang Li, Yue Wang, Ruihan Gao and collaborators [uncertain] | year: 2026 | venue: ICLR 2026 / arXiv preprint [uncertain] | url: https://arxiv.org/abs/2602.09617 | why it matters: Pairs a new large-scale dynamic tactile dataset, ToucHD, with cross-sensor representation learning, pushing tactile benchmark design beyond static touch and small single-sensor datasets [S14].
- RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | authors: Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu | year: 2026 | venue: ICLR 2026 / arXiv preprint | url: https://arxiv.org/abs/2603.04356 | why it matters: It greatly scales systematic household evaluation to 365 tasks across 2,500 kitchen environments and explicitly studies what kinds of diversity matter for generalization [S13].
- ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | authors: Yang Li, Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, Yunsong Zhou, Jia Zeng, Ce Hao, Jieji Ren, Qiaojun Yu, Cewu Lu, Yu Qiao, Jiangmiao Pang | year: 2026 | venue: CVPR 2026 / arXiv preprint | url: https://arxiv.org/abs/2603.15169 | why it matters: Adds an explicitly force-aware evaluation dataset and benchmark protocol for five contact-rich tasks, which is important because most VLA benchmarks still under-measure physical interaction quality [S11].

### Seminal Precursors Pre 2021
- The YCB Object and Model Set: Towards Common Benchmarks for Manipulation Research | authors: Berk Calli, Arjun Singh, Aaron Walsman, Siddhartha Srinivasa, Pieter Abbeel, Aaron M. Dollar | year: 2015 | venue: ICAR 2015 | url: https://ieeexplore.ieee.org/document/7251504 | why it matters: It provided the shared physical object set and community benchmark portal that many unknown-object interaction papers still rely on for cross-paper comparability [S15].
- RLBench: The Robot Learning Benchmark & Learning Environment | authors: Stephen James, Zicong Ma, David Rovick Arrojo, Andrew J. Davison | year: 2019 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/1909.12271 | why it matters: It established the template of a large, extensible manipulation task suite with demonstrations and multimodal observations, which later benchmark families continue to extend [S16].
- SAPIEN: A SimulAted Part-based Interactive ENvironment | authors: Fanbo Xiang, Zexiang Xu, Yunzhu Li, Ruichu Wang, Jiajun Wu, Dieter Fox, Hao Su | year: 2020 | venue: CVPR 2020 | url: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf | why it matters: It introduced the simulatable PartNet-Mobility asset base and interaction environment that later generalizable-manipulation benchmarks build on [S18].
- TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors | authors: Shaoxiong Wang, Mike Lambeta, Po-Wei Chou, Roberto Calandra | year: 2020 | venue: arXiv preprint | url: https://arxiv.org/abs/2012.08456 | why it matters: It helped make tactile benchmarking scalable by providing an open tactile simulator instead of requiring custom proprietary tactile environments [S17].
- BEHAVIOR: Benchmark for Everyday Household Activities in Virtual, Interactive, and Ecological Environments | authors: Sanjana Srivastava and collaborators | year: 2021 | venue: arXiv preprint | url: https://arxiv.org/abs/2108.03332 | why it matters: Although broader than unknown-object interaction, it established the importance of realistic household activity definitions and evaluation protocols that later mobile-manipulation benchmarks inherit [S23].

### Trends 2021 To 2026
- 2021-2022: the field still leaned on shared object sets and simulator-centered task suites, while tactile benchmarking focused on accessible sim-to-real transfer and standardized sensor comparison [S1,S15,S16,S17,S23].
- 2023: benchmark design broadened from single-task success to unified protocols for generalization, transfer, and open-vocabulary interaction, visible in ManiSkill2, HomeRobot OVMM, LIBERO, Open X-Embodiment, and AcTExplore [S3,S4,S5,S6,S7].
- 2024: large real-world datasets and evaluation-proxy frameworks became central, with DROID scaling in-the-wild diversity and SIMPLER explicitly testing whether simulation can stand in for real evaluation [S8,S9].
- Late 2024 to 2025: evaluation pressure shifted toward reasoning, occlusion, and task-conditioned active perception, as seen in VLABench and VISO-Grasp [S10,S21].
- 2026: benchmark scale and modality diversity continue to grow, with MobileManiBench and RoboCasa365 expanding task breadth while AnyTouch 2 and ForceVLA2 push dynamic tactile and force-aware evaluation forward [S11,S12,S13,S14].
- Across the whole period, the strongest trend is from isolated, method-specific evaluation toward benchmark ecosystems that try to measure transfer, reproducibility, and deployment relevance together rather than separately [S5,S6,S7,S8,S9,S10,S12,S13].

### Datasets And Benchmarks
- YCB remains the most visible shared physical object set for unknown rigid-object interaction and is still used in unseen-object tactile exploration papers such as AcTExplore [S3,S15].
- Tactile Gym 2.0 is the clearest reusable tactile benchmark suite in this topic, with object pushing, edge following, and surface following across three tactile sensors and sim-to-real validation [S1].
- FeelSight, released with NeuralFeels, provides a 70-experiment visuo-tactile evaluation dataset that directly targets in-hand perception of novel objects under occlusion [S2].
- HomeRobot OVMM defines an end-to-end open-vocabulary household benchmark for novel-object retrieval and placement, with both simulation and real-world components [S4,S24].
- ManiSkill2 is a benchmark suite rather than a single dataset; its significance is the unified evaluation protocol spanning 20 task families, 2000+ object models, and 4M+ demonstration frames [S5].
- Open X-Embodiment is the largest standardized cross-embodiment real-robot data mixture in this source set, covering 22 robots and 527 skills, and it shapes how foundation-model papers report transfer [S6].
- LIBERO contributes four task suites and 130 tasks for studying forward transfer, forgetting, and task-order sensitivity in lifelong manipulation [S7].
- DROID expands large-scale real-world evaluation with 76k trajectories, 564 scenes, and 84 tasks collected in the wild across many operators and geographies [S8].
- SIMPLER is a benchmark methodology and environment family for comparing real-world policies in simulation with explicit sim-real correlation as the goal [S9].
- VLABench introduces 100 reasoning-heavy language-conditioned task categories and 2000+ objects to stress capabilities that standard manipulation suites under-test [S10].
- ForceVLA2-Dataset, MobileManiBench, RoboCasa365, and ToucHD/AnyTouch 2 are the main 2026 additions in this review, respectively strengthening force-aware evaluation, mobile manipulation verification, large-scale household benchmarking, and dynamic tactile data [S11,S12,S13,S14].
- Foundational pre-2021 infrastructure still matters: RLBench for large task suites, PartNet-Mobility through SAPIEN for articulated assets, and TACTO for scalable tactile simulation [S16,S17,S18].

### Research Gaps
- The community still lacks a single benchmark that jointly measures exploration efficiency, geometric uncertainty reduction, downstream task success, and interaction safety on unseen objects [S2,S3,S4,S9,S11,S19,S20,S21,S22].
- Instance-level held-out splits are common, but category-level, material-level, and morphology-level out-of-distribution protocols are still weak or inconsistent across suites [S3,S5,S6,S8,S10,S12,S13].
- There is no broadly accepted metric that links reconstruction or coverage quality to actual manipulation utility; good shape metrics do not automatically imply grasp or contact success [S2,S3,S19,S22].
- Tactile and force benchmarks are still much smaller and less standardized than RGB-centric benchmarks, especially for dynamic contacts, slipping, variable friction, and multi-contact interaction [S1,S11,S14].
- Benchmarks rarely stress transparent, reflective, deformable, fragile, articulated-with-soft-components, or liquid-filled unknown objects, even though these are common deployment failures [S5,S13,S14,S18].
- Real-world evaluation remains expensive and sparse, which is why SIMPLER exists; but the field still needs broader evidence that simulator rankings generalize across more embodiments and task families [S4,S9,S12,S13].
- Foundation-model benchmarks emphasize task breadth and reasoning, yet often under-measure low-level contact quality, force safety, calibration drift, and physically grounded stopping criteria [S10,S11,S12,S13].
- Cross-benchmark comparability is poor because object assets, budget definitions, controller assumptions, and reporting conventions differ substantially [S1,S3,S4,S5,S7,S9,S10,S11,S12,S13,S21,S22].
- Benchmark papers seldom evaluate a full autonomy loop from initial discovery to final task completion with interruption handling, recovery behavior, and operator-free execution [S4,S20,S21].
- Inference from the source set: the strongest open opportunity is not merely larger datasets, but benchmark protocols that force methods to trade off information gain, safety, time, compute, and final task value under matched conditions [S8,S9,S10,S11,S12,S13].

### Opportunities For Single Manipulator Systems
- A practical benchmark target for one arm is a unified tabletop protocol that starts with partial RGB-D observation, allows a small budget of active views and touches, and ends with a grasp, insertion, or placement success metric on unseen rigid objects [S2,S3,S19,S20,S21,S22].
- Single-arm systems can benefit from combining the reproducibility of ManiSkill2-style unified interfaces with YCB-based physical evaluation so that simulation and real tests share object identities and task APIs [S5,S15].
- For low-cost hardware, Tactile Gym 2.0 suggests that one dense optical fingertip plus a wrist camera is enough to build a meaningful benchmark around surface following, guarded contact, and uncertainty reduction [S1].
- For perception-heavy single-arm manipulation, FeelSight and AcTExplore point to a useful benchmark niche: few-touch correction of visual uncertainty on previously unseen objects, measured by both geometry and downstream task success [S2,S3].
- For contact-rich single-arm tasks, ForceVLA2 shows that force-aware metrics should be added early instead of treated as optional diagnostics, especially for wiping, pressing, and assembly-like behaviors [S11].
- Inference from the source set: the best near-term opportunity is a benchmark that is smaller than RoboCasa365 or Open X-Embodiment but more integrated than current object-centric papers, namely a single-arm unknown-object suite with matched sim-real assets, explicit action budgets, force limits, and final-task success labels [S4,S5,S9,S11,S13,S15].

### Sources
- Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch | id: S1 | url: https://arxiv.org/abs/2207.10763 | type: arXiv page | notes: Primary source for tactile benchmark scope, task list, sensor list, and sim-to-real framing.
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | id: S2 | url: https://arxiv.org/abs/2312.13469 | type: arXiv page | notes: Primary source for FeelSight, 70-experiment evaluation set, F-score, pose drift, and occlusion claims.
- AcTExplore: Active Tactile Exploration of Unknown Objects | id: S3 | url: https://arxiv.org/abs/2310.08745 | type: arXiv page | notes: Primary source for unknown-object tactile exploration benchmark details and 95.97% IoU on unseen YCB objects.
- HomeRobot: Open-Vocabulary Mobile Manipulation | id: S4 | url: https://arxiv.org/abs/2306.11565 | type: arXiv page | notes: Primary source for OVMM benchmark framing and 20% real-world baseline success.
- ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills | id: S5 | url: https://arxiv.org/abs/2302.04659 | type: arXiv page | notes: Primary source for unified evaluation protocol, 20 task families, 2000+ object models, and 4M+ frames.
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models | id: S6 | url: https://arxiv.org/abs/2310.08864 | type: arXiv page | notes: Primary source for 22 robots, 527 skills, standardized data formats, and positive-transfer claims.
- LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | id: S7 | url: https://arxiv.org/abs/2306.03310 | type: arXiv page | notes: Primary source for four task suites, 130 tasks, forward transfer, and forgetting-related evaluation.
- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | id: S8 | url: https://arxiv.org/abs/2403.12945 | type: arXiv page | notes: Primary source for 76k trajectories, 564 scenes, 84 tasks, and in-the-wild dataset design.
- Evaluating Real-World Robot Manipulation Policies in Simulation | id: S9 | url: https://arxiv.org/abs/2405.05941 | type: arXiv page | notes: Primary source for SIMPLER and sim-real correlation claims.
- VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks | id: S10 | url: https://arxiv.org/abs/2412.18194 | type: arXiv page | notes: Primary source for 100 task categories, 2000+ objects, and reasoning-heavy benchmark design.
- ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | id: S11 | url: https://arxiv.org/abs/2603.15169 | type: arXiv page | notes: Primary source for ForceVLA2-Dataset, five contact-rich tasks, and force-aware evaluation claims.
- MobileManiBench: Simplifying Model Verification for Mobile Manipulation | id: S12 | url: https://arxiv.org/abs/2602.05233 | type: arXiv page | notes: Primary source for 630 objects, 20 categories, 100 scenes, 100+ tasks, and 300K trajectories.
- RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | id: S13 | url: https://arxiv.org/abs/2603.04356 | type: arXiv page | notes: Primary source for 365 tasks, 2,500 kitchen environments, and systematic evaluation framing.
- AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception | id: S14 | url: https://arxiv.org/abs/2602.09617 | type: arXiv page | notes: Primary source for ToucHD and the shift toward dynamic tactile benchmark datasets.
- The YCB Object and Model Set: Towards Common Benchmarks for Manipulation Research | id: S15 | url: https://ieeexplore.ieee.org/document/7251504 | type: official IEEE page | notes: Primary precursor for common object sets and benchmark protocols in manipulation.
- RLBench: The Robot Learning Benchmark & Learning Environment | id: S16 | url: https://arxiv.org/abs/1909.12271 | type: arXiv page | notes: Primary precursor for large manipulation task suites with demonstrations and multimodal observations.
- TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors | id: S17 | url: https://arxiv.org/abs/2012.08456 | type: arXiv page | notes: Primary precursor for tactile simulation infrastructure.
- SAPIEN: A SimulAted Part-based Interactive ENvironment | id: S18 | url: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf | type: official conference PDF | notes: Primary precursor for PartNet-Mobility-backed articulated-object simulation.
- Active Visuo-Haptic Object Shape Completion | id: S19 | url: https://arxiv.org/abs/2203.09149 | type: arXiv page | notes: Primary source for object-centric active visuo-haptic evaluation on unknown objects.
- Affordance-Driven Next-Best-View Planning for Robotic Grasping | id: S20 | url: https://proceedings.mlr.press/v229/zhang23i.html | type: official conference proceedings page | notes: Primary source for task-conditioned active view-planning evaluation toward grasping.
- VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility | id: S21 | url: https://arxiv.org/abs/2503.12609 | type: arXiv page | notes: Primary source for active-view-plus-grasp benchmark claims under clutter and invisibility.
- PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects | id: S22 | url: https://pure.bit.edu.cn/en/publications/pb-nbv-efficient-projection-based-next-best-view-planning-framewo | type: official university publication page | notes: Primary source for practical, efficiency-oriented unknown-object NBV evaluation.
- BEHAVIOR: Benchmark for Everyday Household Activities in Virtual, Interactive, and Ecological Environments | id: S23 | url: https://arxiv.org/abs/2108.03332 | type: arXiv page | notes: Primary precursor for realistic household activity definitions and evaluation.
- NeurIPS 2023 HomeRobot: Open Vocabulary Mobile Manipulation (OVMM) Challenge | id: S24 | url: https://aihabitat.org/challenge/2023_homerobot_ovmm/ | type: official challenge page | notes: Official benchmark page for OVMM challenge framing and evaluation context.

## Force feedback impedance control contour following and compliant contact exploration

### Subproblem Definition
This subtopic covers robot methods that deliberately maintain or exploit physical contact to trace surfaces, follow contours, reconstruct local geometry, or complete contact-rich manipulation on unknown or partially unknown objects. Included methods use force/torque sensing, tactile sensing, proprioception, compliance, admittance or impedance control, hybrid force-position control, or learned equivalents that explicitly regulate contact while exploring or manipulating geometry. The boundary excludes vision-only geometry exploration, non-contact inspection, and generic assembly papers that do not use contact feedback to regulate exploration, contour following, or safe interaction with uncertain geometry.

### Problem Formulations
- Surface following or edge following with regulation of contact pose, normal force, or shear during continuous motion.
- Dynamic contour following in which the object moves and the controller must both track motion and continue tactile exploration.
- Active tactile exploration for contour or shape reconstruction under local geometric uncertainty.
- Tool-mediated surface following, wiping, polishing, or scraping where the contact state and applied force must be inferred and stabilized.
- Force-guided contact establishment and force-limited insertion or assembly under pose uncertainty.
- Learning compliant or variable-impedance behaviors from demonstrations for stable force regulation in unknown environments.
- Modern multimodal policies that split long-horizon vision guidance from high-rate force-aware local interaction control.

### Sensing Modalities
- Wrist or end-effector force/torque sensing, sometimes estimated rather than directly measured, is central in FORGE, Force Policy, Direction Matters, ForceVLA2, and compliant force-control papers.
- High-resolution optical tactile sensing is dominant in the Bristol tactile-servoing line: TacTip, DIGIT, and DigiTac are used for edge following, surface following, object tracking, and pushing.
- Shear-sensitive tactile perception is explicitly used in pose-and-shear tactile servoing and in dynamic contour following, where shear minimization stabilizes contact.
- Vision is typically used for task context, object localization, or long-horizon guidance rather than fine local regulation in the more recent multimodal papers.
- Proprioception and Cartesian pose history are used broadly for controller state, contact-state estimation, and switching logic.
- Specialized contact sensors also appear, such as whisker-inspired tactile sensors for contour reconstruction and proximity+tactile sensing for tool-use transfer.

### Action Space And Robot Setup
- Most systems use a single 6- or 7-DoF arm with either a wrist F/T sensor, a tactile fingertip, or a tool instrumented with tactile or proximity sensing.
- Tactile Gym 2.0 deliberately lowers the hardware barrier by using a low-cost 4-DoF desktop arm for sim-to-real edge following, surface following, and object pushing.
- Pose-and-shear tactile servoing and dynamic contour following use Cartesian velocity control in SE(3) with closed-loop tactile state estimation.
- Force-aware manipulation papers typically command Cartesian pose deltas together with force targets, controller modes, or admittance/impedance parameters.
- Tool-use transfer uses a Franka arm and multimodal sensing to adapt surface-following behaviors across brushes, a broom, and a sponge.
- Some papers include dual-arm setups or bimanual variants, but the dominant embodiment in this subtopic is still a single manipulator performing local contact exploration.

### Method Families
- Classical and adaptive compliant control: impedance, admittance, and hybrid force-position control remain the base layer for safe sustained contact.
- Tactile servoing: optical tactile or whisker sensing is turned into local pose, shear, or contact-point estimates that drive continuous surface-following control.
- Sim-to-real tactile learning: simulation environments such as Tactile Gym 2.0 train policies for edge following and surface following before transferring them to real hardware.
- Demonstration-driven compliance learning: human demonstrations are used to infer variable impedance or optimal task frames for contact-rich control.
- Active exploration under uncertainty: the robot chooses informative next contacts to reduce reconstruction uncertainty while limiting contact risk.
- Multimodal force-aware policy learning: newer work separates global vision reasoning from high-rate local force control and often introduces explicit force-aware prompts, interaction frames, or force-direction predictions.

### Representative System Pipelines
- Tactile Gym 2.0: train deep RL policies in simulation on tactile images for edge following and surface following, translate tactile imagery across sensor domains, then transfer policies directly to real sensors and a desktop robot without task-specific fine-tuning.
- Tac-VGNN and follow-on tactile servoing: infer local pose and depth from tactile marker motion and Voronoi features, then drive a tactile servo controller that follows surfaces more smoothly than earlier discrete schemes.
- Pose-and-shear tactile servoing plus dynamic contour following: estimate both contact pose and shear, filter the state in SE(3), use shear-minimizing tracking during object motion, and switch into tactile exploration modes to continue contour following.
- Few-shot tool-use transfer: pre-train in simulation to recognize contact states, then fine-tune with a small number of human demonstrations so a single-arm robot can follow new surfaces with diverse tools and adapt to incline changes or mild deformability.
- FORGE: learn force-threshold-conditioned policies in simulation under dynamics randomization, deploy on real contact-rich tasks, predict task success online, and tune allowable force automatically for uncertain forceful interactions.
- Proactive tactile exploration: start from a minimal visual prior, fit and refine a mesh from sequential contacts, choose the next touch to reduce uncertainty while lowering contact-failure risk, and update the reconstruction iteratively.
- Direction Matters and Force Policy: use vision for task progress in free space, then switch to force-aware local control where the policy predicts force direction, contact state, or an interaction frame that configures admittance or hybrid force-position control.
- ForceVLA2: fuse multi-view vision, language, proprioception, and force prompts, then output action chunks, force objectives, control modes, and task progress for closed-loop hybrid force-position manipulation.

### Evaluation Tasks
- Edge following and surface following on rigid objects.
- Dynamic contour following and moving-object tracking.
- Object pushing and non-prehensile manipulation under sustained contact.
- Shape or contour reconstruction from tactile contact sequences.
- Tool-mediated surface following, wiping, painting, pressing, and scraping.
- Peg insertion, nut threading, gear meshing, snap-fit insertion, and related force-sensitive assembly tasks.
- Door opening, microwave opening, articulated-object manipulation, and retrieval under contact.
- Single-arm and occasional dual-arm contact-rich tasks with disturbances or geometric shifts.

### Common Metrics
- Task success rate or completion rate.
- Contour-following or tracking accuracy in millimeters.
- Force tracking error, force regulation quality, or compliance stability.
- Tactile pose-estimation error, depth error, or contact-state accuracy.
- Shape or contour reconstruction error, sometimes reported as sub-millimeter geometric accuracy.
- Robustness under disturbances, geometric shifts, or unseen objects and tools.
- Safety-related metrics such as force-threshold violations, overload events, or safety stops.
- Data efficiency metrics such as number of demonstrations or sim-to-real transfer without additional fine-tuning.

### Best Reported Capabilities
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

### Failure Modes And Limitations
- Sim-to-real mismatch in contact dynamics remains a core failure mode, especially for force magnitude prediction, frictional transitions, and contact transients.
- Many controllers still require manually chosen force magnitudes, phase thresholds, or switching logic even when the force direction or interaction frame is learned.
- Local tactile exploration can lose contact on high-curvature or sharp surfaces, enter tangential slip, or get trapped in local exploration minima.
- Most experiments are local and task-specific; few systems autonomously explore an entire unknown object in clutter or with broad material variation.
- Benchmarking is fragmented: Tactile Gym 2.0 is reusable, but many later systems use bespoke task suites that make direct comparison difficult.
- Whole-object reconstruction from contact remains slow because tactile information is local and contact placement must trade off information gain against safety.
- Reproducibility is uneven: some influential project pages exist without mature code or data releases as of 2026-03-23.
- The newest 2026 multimodal force-aware policies are promising but still limited to small real-robot task suites and curated perturbation settings.

### Representative Papers 2021 2026
- Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch | authors: Yijiong Lin, John Lloyd, Alex Church, Nathan F. Lepora | year: 2022 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2207.10763 | why it matters: Established the most reusable benchmark-style platform in this subtopic, with sim-to-real edge following and surface following across TacTip, DIGIT, and DigiTac sensors on accessible hardware.
- Tac-VGNN: A Voronoi Graph Neural Network for Pose-Based Tactile Servoing | authors: Wei Fan, Max Yang, Yunbo Xing, Nathan F. Lepora, Dandan Zhang | year: 2023 | venue: ICRA 2023 | url: https://arxiv.org/abs/2303.02708 | why it matters: Pushed tactile servoing toward smoother continuous surface following by improving pose estimation from tactile marker motion and explicitly showing better real surface-following performance.
- A pose and shear-based tactile robotic system for object tracking, surface following and object pushing | authors: John Lloyd, Nathan Lepora | year: 2023 | venue: Preprint | url: https://arxiv.org/abs/2306.08560 | why it matters: Extended local tactile state from pose alone to pose plus shear, enabling smoother continuous control and a broader set of sustained-contact behaviors including object tracking and surface following.
- Learning compliant dynamical system from human demonstrations for stable force control in unknown environments | authors: Jiayun Fu, Haotian Huang, Zhehao Jin, Andong Liu, Wen-An Zhang, Li Yu, Weiyong Si, Chenguang Yang | year: 2024 | venue: Robotics and Computer-Integrated Manufacturing | url: https://www.sciencedirect.com/science/article/pii/S0736584523001448 | why it matters: Represents the human-demonstration lineage for variable compliance, showing how force error and environment stiffness cues can be transferred into stable force control on UR5 single- and dual-arm tasks in unknown environments.
- Tactile control for object tracking and dynamic contour following | authors: Kirsty Aquilina, David A. W. Barton, Nathan F. Lepora | year: 2024 | venue: Robotics and Autonomous Systems | url: https://doi.org/10.1016/j.robot.2024.104710 | why it matters: One of the clearest demonstrations that tactile contour following can operate on moving objects, using a switching controller that fuses shear-based tracking with tactile exploration.
- Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks | authors: Ali Mousavi Mohammadi, Maxim Vochten, Erwin Aertbelien, Joris De Schutter | year: 2026 | venue: Robotics and Autonomous Systems | url: https://arxiv.org/abs/2404.01900 | why it matters: Formalized a data-driven way to recover the task frame from recorded motion and wrench demonstrations, directly supporting surface following and other force-constrained tasks without manual frame engineering.
- FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty | authors: Michael Noseworthy, Bingjie Tang, Bowen Wen, Ankur Handa, Chad Kessens, Nicholas Roy, Dieter Fox, Fabio Ramos, Yashraj Narang, Iretiayo Akinola | year: 2025 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2408.04587 | why it matters: Brought explicit force-threshold conditioning and success prediction into sim-to-real contact-rich manipulation, enabling safer exploration of uncertain forceful interactions such as snap-fit insertion.
- Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing | authors: Marina Y. Aoyama, Sethu Vijayakumar, Tetsuya Narita | year: 2025 | venue: IEEE Robotics and Automation Letters | url: https://sony.github.io/tool-use-few-shot-transfer/ | why it matters: Shows that tool-mediated surface following can generalize across tools with only a few human demonstrations when multimodal contact-state sensing is combined with sim pre-training.
- Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors | authors: Paris Oikonomou, George Retsinas, Petros Maragos, Costas S. Tzafestas | year: 2025 | venue: Preprint | url: https://arxiv.org/abs/2505.11975 | why it matters: Captures the exploration side of the subtopic by planning informative contacts to reduce shape uncertainty while explicitly lowering the risk of failed or unsafe contacts.
- Whisker-based Active Tactile Perception for Contour Reconstruction | authors: Yixuan Dang, Qinyang Xu, Yu Zhang, Xiangtong Yao, Liding Zhang, Zhenshan Bing, Florian Roehrbein, Alois Knoll | year: 2025 | venue: Preprint | url: https://arxiv.org/abs/2507.23305 | why it matters: Demonstrates a lightweight active-touch route to contour following, with a dedicated contact-localization pipeline and active pose regulation for sub-millimeter contour reconstruction.
- ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | authors: Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Cewu Lu, Wenqiang Zhang | year: 2025 | venue: NeurIPS 2025 / arXiv | url: https://arxiv.org/abs/2505.22159 | why it matters: A clearly relevant 2025 precursor to the force-aware VLA branch, introducing six-axis force as a first-class input inside the action model and releasing a five-task force-rich dataset.

### 2026 Preprints
- Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation | authors: Hongjie Fang, Shirun Tang, Mingyu Mei, Haoxiang Qin, Zihao He, Jingjing Chen, Ying Feng, Chenxi Wang, Wanxi Liu, Zaixing He, Cewu Lu, Shiquan Wang | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.22088 | why it matters: Introduces an interaction-frame representation recovered from physical response and uses it to split global vision guidance from high-frequency force regulation, directly targeting stable contact under geometric and physical variation.
- Direction Matters: Learning Force Direction Enables Sim-to-Real Contact-Rich Manipulation | authors: Yifei Yang, Anzhe Chen, Zhenjie Zhu, Kechun Xu, Yunxuan Mao, Yufei Wei, Lu Chen, Rong Xiong, Yue Wang | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.14174 | why it matters: Shifts the prediction target from brittle force magnitude to task-geometry-linked force direction, then uses the result to configure a force-aware admittance controller for robust sim-to-real transfer.
- ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | authors: Yang Li, Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, Yunsong Zhou, Jia Zeng, Ce Hao, Jieji Ren, Qiaojun Yu, Cewu Lu, Yu Qiao, Jiangmiao Pang | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.15169 | why it matters: Represents the strongest early-2026 move toward force-aware VLA systems, combining force prompts, multimodal fusion, hybrid control outputs, and a new dataset over five real contact-rich tasks.
- FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation | authors: Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.02142 | why it matters: Introduces force distillation as a way to keep force-aware reasoning inside a VLA without requiring physical force sensors at inference time.
- CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation | authors: Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.15541 | why it matters: Adds a distinct compliance-aware VLA branch, showing that explicit compliance augmentation can materially improve contact-rich task success.

### Seminal Precursors Pre 2021
- Impedance Control: An Approach to Manipulation: Part I-Theory | authors: Neville Hogan | year: 1985 | venue: Journal of Dynamic Systems, Measurement, and Control | url: https://newmanlab.mit.edu/wp-content/uploads/2017/09/1985-impedance-control-an-approach-to-manipulation-part-I-theory.pdf | why it matters: The foundational statement that manipulation requires controlling interaction dynamics rather than position or force alone; this remains the conceptual basis for nearly all compliant-contact work in the subtopic.
- Dynamic hybrid position/force control of robot manipulators-on-line estimation of unknown constraint | authors: Tsuneo Yoshikawa, Akio Sudou | year: 1993 | venue: IEEE Transactions on Robotics and Automation | url: https://ieeexplore.ieee.org/document/238286/ | why it matters: A classic hybrid position/force-control precursor for following unknown constraint surfaces while regulating contact, directly informing later task-frame and hybrid force-position formulations.
- Sensor-based 3-D autonomous surface-following control | authors: Anibal Ollero, Alfonso Garcia-Cerezo | year: 1996 | venue: Mathematics and Computers in Simulation | url: https://www.sciencedirect.com/science/article/pii/0378475495000909 | why it matters: An early autonomous surface-following paper that made the problem formulation explicit and distinguished adaptive sensor-based following from preprogrammed point-to-point tracking.
- Finger contact sensing and the application in dexterous hand manipulation | authors: Hongbin Liu, Kien Cuong Nguyen, Veronique Perdereau, Joao Bimbo, Junghwan Back, Matthew Godden, Lakmal D. Seneviratne, Kaspar Althoefer | year: 2015 | venue: Autonomous Robots | url: https://www.shadowrobot.com/wp-content/uploads/2022/04/Finger-Contact-Sensing-and-the-Application-in-Dexterous-Hand-Manipulation-Matthew-Godden-Co-Author-2015.pdf | why it matters: Showed how fingertip contact location and local force information can support surface following and exploration of unknown objects, bridging classical force control and modern tactile servoing.
- Active sensorimotor control for tactile exploration | authors: Nathan Lepora, Uriel Martinez-Hernandez, Maria Evans, Tony J. Prescott | year: 2017 | venue: Robotics and Autonomous Systems | url: https://www.sciencedirect.com/science/article/abs/pii/S0921889016303086 | why it matters: Established the active-touch action-perception loop for contour following of unknown objects, strongly influencing the later Bristol tactile-servoing and contour-following systems.

### Trends 2021 To 2026
- The field moved from local tactile servoing and surface following toward more complete force-aware manipulation pipelines that combine contact control with higher-level planning.
- There is a clear transition from fixed or manually tuned compliant controllers toward learned interaction structure: task frames, interaction frames, contact states, force directions, and multimodal force prompts.
- Static rigid-surface experiments are giving way to moving objects, articulated objects, variable inclination, mild deformability, and explicit disturbance tests.
- Sim-to-real methods improved substantially, especially through tactile simulators, dynamics randomization, and policy decompositions that reserve force for high-rate local control.
- Tool-mediated contact tasks became more prominent, reflecting real application needs such as wiping, polishing, and scraping rather than only direct fingertip contour following.
- Despite progress, evaluation remains fragmented and local: benchmarked, whole-object autonomous contact exploration in clutter still lags behind progress in curated task suites.

### Datasets And Benchmarks
- Tactile Gym 2.0 is the most reusable benchmark-style resource in this niche, with open sim-to-real tasks for edge following, surface following, and object pushing across multiple tactile sensors.
- The Tactile Gym 2.0 project page and repository make it possible to compare tactile sensors and policies on broadly similar contact tasks, which is unusual for this literature.
- ForceVLA2 introduces a 1,000-trajectory dataset over five contact-rich tasks with images, prompts, proprioception, and force signals, but the project page states that code and dataset were still coming soon as of 2026-03-23.
- Few-shot tool-use transfer, Direction Matters, FORGE, Proactive Tactile Exploration, and Whisker-based Active Tactile Perception all use custom task suites rather than shared public benchmarks.
- Overall, benchmark maturity is moderate for local tactile following and low for general unknown-object exploration with force-aware compliant contact.

### Research Gaps
- Whole-object autonomous exploration with compliant contact is still underdeveloped; most work follows a local contour or task surface rather than building complete object understanding.
- Shared real-world benchmarks for force-aware exploration are scarce, making it hard to compare exploration efficiency, safety, and generalization across labs.
- The field still lacks strong methods for highly deformable, fragile, or mixed-material surfaces where local geometry and safe force envelopes change rapidly.
- Contact-state estimation and controller switching remain brittle around discontinuities such as edges, holes, corners, and sudden friction changes.
- Many systems need manual force magnitudes or task-specific tuning; learning safe magnitudes online remains much less mature than learning direction or contact phase.
- Closed-loop integration of visual global geometry with tactile or force local exploration remains limited, especially for cluttered multi-object scenes.
- Reproducibility is constrained by specialized tactile hardware, limited open datasets, and incomplete releases for several high-profile 2025-2026 systems.

### Opportunities For Single Manipulator Systems
- A single arm with an eye-in-hand camera and wrist F/T sensor can already exploit the strongest current ideas: global visual targeting, explicit force-threshold safety, and local admittance or hybrid force-position regulation.
- If tactile hardware is available, the most practical near-term path is to pair a simple tactile servoing controller with a reusable simulator such as Tactile Gym 2.0 and then adapt on real surfaces.
- For tool-mediated tasks, the strongest opportunity is to learn contact-state abstractions or force directions rather than raw force magnitudes, because those signals appear more transferable across geometry changes.
- Minimal-visual-prior plus proactive tactile exploration is promising for unknown objects when the goal is not full dexterity but safe surface discovery for grasping, wiping, or inspection.
- Interaction-frame or task-frame representations are especially attractive for single-arm systems because they reduce controller design complexity and make force regulation more geometry-aware.
- A practical research stack for one manipulator is: visual object hypothesis, guarded contact with force threshold, local frame estimation, compliant contour following or probing, uncertainty-based next-touch selection, and explicit stopping when either task success or shape-confidence criteria are met.

### Sources
- Tactile Gym 2.0 project page | url: https://sites.google.com/view/tactile-gym-2 | type: official project page | year: 2022 | notes: Source for benchmark tasks, supported tactile sensors, sim-to-real transfer claims, and code availability.
- Tactile Gym 2.0 arXiv page | url: https://arxiv.org/abs/2207.10763 | type: arXiv abstract page | year: 2022 | notes: Primary paper source for edge following and surface following benchmark formulation.
- Tac-VGNN arXiv page | url: https://arxiv.org/abs/2303.02708 | type: arXiv abstract page | year: 2023 | notes: Source for pose-based tactile servoing and reported depth-estimation improvement with smoother real surface following.
- Pose and shear-based tactile robotic system arXiv page | url: https://arxiv.org/abs/2306.08560 | type: arXiv abstract page | year: 2023 | notes: Primary source for continuous tactile object tracking, surface following, and object pushing.
- Pose and shear-based tactile robotic system Zenodo record | url: https://zenodo.org/records/7835928 | type: official preprint record | year: 2023 | notes: Supplementary primary source with metadata and downloadable preprint.
- Tactile control for object tracking and dynamic contour following | url: https://doi.org/10.1016/j.robot.2024.104710 | type: journal DOI page | year: 2024 | notes: Primary publication record for dynamic contour following, moving-object tracking accuracy, and switching-controller design.
- University of Bristol publication record for dynamic contour following | url: https://research-information.bris.ac.uk/en/publications/tactile-control-for-object-tracking-and-dynamic-contour-following/ | type: official university publication page | year: 2024 | notes: Source for bibliographic metadata and abstract text.
- Learning compliant dynamical system from human demonstrations for stable force control in unknown environments | url: https://www.sciencedirect.com/science/article/pii/S0736584523001448 | type: official journal page | year: 2024 | notes: Primary source for human-demonstration-based variable compliance in unknown environments.
- Automatic Derivation of an Optimal Task Frame for Learning and Controlling Contact-Rich Tasks | url: https://arxiv.org/abs/2404.01900 | type: arXiv abstract page | year: 2024 | notes: Source for task-frame derivation from motion and wrench data, including validation on surface following.
- FORGE arXiv page | url: https://arxiv.org/abs/2408.04587 | type: arXiv abstract page | year: 2024 | notes: Primary source for force-threshold-conditioned exploration, success prediction, and robust contact-rich manipulation under uncertainty.
- FORGE project page | url: https://noseworm.github.io/forge/ | type: official project page | year: 2025 | notes: Source for task descriptions, project media, and emphasis on uncertain forceful interactions such as snap-fit insertion.
- Few-shot transfer of tool-use skills using human demonstrations with proximity and tactile sensing | url: https://sony.github.io/tool-use-few-shot-transfer/ | type: official project page | year: 2025 | notes: Primary source for multimodal tool-use surface-following transfer, adaptation to deformable surfaces, and few-shot demonstration requirements.
- Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors | url: https://arxiv.org/abs/2505.11975 | type: arXiv abstract page | year: 2025 | notes: Primary source for uncertainty-driven tactile contact selection and iterative shape reconstruction.
- Whisker-based Active Tactile Perception for Contour Reconstruction | url: https://arxiv.org/abs/2507.23305 | type: arXiv abstract page | year: 2025 | notes: Primary source for active whisker-based contour following and sub-millimeter contour reconstruction.
- Direction Matters project page | url: https://yifei-y.github.io/project-pages/DirectionMatters/ | type: official project page | year: 2026 | notes: Source for task list, force-aware admittance-control interpretation, robustness claims, and code availability.
- Direction Matters arXiv page | url: https://arxiv.org/abs/2602.14174 | type: arXiv abstract page | year: 2026 | notes: Primary source for learning force direction and sim-to-real contact-rich manipulation.
- Force Policy arXiv page | url: https://arxiv.org/abs/2602.22088 | type: arXiv abstract page | year: 2026 | notes: Primary source for interaction-frame-based hybrid force-position control policy learning.
- Force Policy project page | url: https://force-policy.github.io/ | type: official project page | year: 2026 | notes: Source for interaction-frame explanation, task descriptions, force-control evaluation, and code-coming-soon status.
- ForceVLA2 arXiv page | url: https://arxiv.org/abs/2603.15169 | type: arXiv abstract page | year: 2026 | notes: Primary source for the force-aware VLA formulation, dataset size, task coverage, and reported gains over pi0 and pi0.5.
- ForceVLA2 project page | url: https://sites.google.com/view/force-vla2/home | type: official project page | year: 2026 | notes: Source for control outputs, dataset description, real-task set, and code-and-dataset-coming-soon status.
- FD-VLA arXiv page | url: https://arxiv.org/abs/2602.02142 | type: arXiv abstract page | year: 2026 | notes: Primary source for force-token distillation and the claim that distilled force can outperform direct force sensing in physical experiments.
- CompliantVLA-adaptor arXiv page | url: https://arxiv.org/abs/2601.15541 | type: arXiv abstract page | year: 2026 | notes: Primary source for compliance augmentation in VLAs and the reported success-rate improvement from 9.86% to 17.29% on contact-rich tasks.
- Impedance Control: An Approach to Manipulation: Part I-Theory | url: https://newmanlab.mit.edu/wp-content/uploads/2017/09/1985-impedance-control-an-approach-to-manipulation-part-I-theory.pdf | type: paper PDF | year: 1985 | notes: Foundational precursor for compliant interaction control.
- Dynamic hybrid position/force control of robot manipulators-on-line estimation of unknown constraint | url: https://ieeexplore.ieee.org/document/238286/ | type: official journal page | year: 1993 | notes: Foundational precursor for hybrid position-force control on unknown constraints.
- Sensor-based 3-D autonomous surface-following control | url: https://www.sciencedirect.com/science/article/pii/0378475495000909 | type: official journal page | year: 1996 | notes: Foundational precursor for autonomous sensor-based surface following.
- Finger contact sensing and the application in dexterous hand manipulation | url: https://www.shadowrobot.com/wp-content/uploads/2022/04/Finger-Contact-Sensing-and-the-Application-in-Dexterous-Hand-Manipulation-Matthew-Godden-Co-Author-2015.pdf | type: paper PDF | year: 2015 | notes: Precursor linking fingertip contact sensing to surface following and manipulation.
- Active sensorimotor control for tactile exploration | url: https://www.sciencedirect.com/science/article/abs/pii/S0921889016303086 | type: official journal page | year: 2017 | notes: Precursor for active contour following and tactile action-perception loops on unknown objects.
- ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | url: https://arxiv.org/abs/2505.22159 | type: arXiv abstract page | year: 2025 | notes: Primary source for the 2025 force-aware VLA precursor, including the 23.2% average gain over pi0-based baselines and ForceVLA-Data across five contact-rich tasks.

## Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects

### Subproblem Definition
This subtopic covers robot manipulation methods that use large pretrained vision-language models, vision-language-action models, diffusion or flow-based generalist policies, or closely related hierarchical VLM-to-control stacks to reason about and physically interact with previously unseen objects with little or no object-specific supervision. The boundary includes end-to-end VLAs, cross-embodiment generalist policies, and hierarchical systems that use foundation-model semantics or spatial reasoning to guide manipulation; it excludes classical task-specific grasping or imitation systems without foundation-model pretraining, pure perception-only VLMs, and navigation-only agents without substantive object interaction [S1,S2,S4,S5,S6,S7,S12,S13,S16,S18,S19,S21,S22,S23,S24,S25].

### Problem Formulations
- Open-vocabulary tabletop manipulation: given RGB observations and a natural-language command, the robot must identify and manipulate a target object that was not explicitly modeled per instance, often under distractors or changed layouts [S1,S5,S12,S13,S20].
- Long-horizon household or mobile-manipulation tasks in novel homes or rooms: the policy must chain subskills such as picking, placing, opening, wiping, or sorting in environments absent from training [S2,S17,S18,S19].
- Cross-embodiment generalist pretraining plus rapid adaptation: a large policy is pretrained on heterogeneous robot data, then transferred to a new arm, camera arrangement, or action space with little task-specific data [S7,S11,S12,S13,S16,S19,S24,S25].
- Zero-shot or few-shot trajectory synthesis from foundation-model reasoning: a VLM or LLM predicts affordances, 3D paths, goal images, or value maps that a lower-level controller follows to manipulate previously unseen objects [S6,S21,S22,S23].
- 3D-aware VLA control: multi-view RGB-D or spatial encodings are used to improve robustness to unseen object poses, layouts, and backgrounds while retaining language grounding [S20,S21,S22,S23].
- Dexterous or bimanual generalist control: foundation policies extend beyond single-arm pick-and-place to box assembly, laundry folding, bag packing, and other high-dimensional tasks while preserving transfer to unseen objects or scenes [S16,S17,S18,S19,S25].

### Sensing Modalities
- RGB vision is the dominant modality, typically from one or more external cameras and often an egocentric or wrist camera; this is the standard input route for RT-1, RT-2, Octo, OpenVLA, pi0, pi0.5, Gemini Robotics, and most spatial VLA variants [S3,S5,S12,S13,S16,S18,S19,S20].
- Natural-language task instructions are universal across the subtopic and often provide the only explicit object specification, enabling open-vocabulary or relational object selection [S1,S2,S5,S6,S12,S17,S18,S19,S20,S21,S22,S23,S25].
- Robot proprioception and state tokens are common in embodied multimodal models and generalist policies, especially PaLM-E, pi0, pi0.5, Gemini Robotics, and RDT-1B [S4,S16,S18,S19,S25].
- RGB-D, point clouds, or multi-view spatial observations become more important in the 2025-2026 branch, particularly OG-VLA, GeneralVLA, VISTA, and Gemini Robotics-ER-style embodied reasoning [S19,S21,S22,S23].
- Goal images are still used in the generalist-policy lineage, especially Octo, as an alternative or complement to language prompts [S12].
- Inference from the source set: tactile and force sensing are not a central ingredient in the main zero-shot unseen-object foundation-model literature through 2026-03-23; most evidence is still vision-language dominant [S5,S12,S13,S16,S17,S18,S19,S20,S21,S22,S23,S25].

### Action Space And Robot Setup
- Most systems operate a single 6- or 7-DoF arm with a parallel-jaw gripper in tabletop or bench-top scenes, outputting end-effector translation, rotation, and gripper commands either as discrete tokens or short continuous action chunks [S1,S3,S5,S12,S13,S20,S21].
- Cross-embodiment work broadens this to multiple arm types and camera layouts; Open X-Embodiment spans 22 embodiments, Octo evaluates across 9 platforms, and OpenVLA supports multiple robots out of the box before parameter-efficient adaptation [S7,S12,S13,S14].
- Mobile manipulators appear in SayCan, pi0, pi0.5, and Gemini Robotics, where language-conditioned policies must combine arm motion with navigation or repositioning to complete household tasks [S2,S16,S17,S18,S19].
- Bimanual and highly dexterous setups become prominent in the pi0, Gemini Robotics, and RDT-1B line, which explicitly target dual-arm manipulation and complex contact-rich object handling [S16,S18,S19,S25].
- Hierarchical methods often do not emit motor torques directly; instead they predict language options, 3D paths, canonical goal images, or value maps that a lower-level controller or policy executes [S2,S6,S21,S22,S23].

### Method Families
- Semantic-plus-spatial grounding policies: CLIPort combines CLIP semantics with Transporter-style spatial reasoning, while SpatialVLA and OG-VLA inject stronger spatial encodings or canonical 3D views into the VLA stack [S1,S20,S21].
- Planner-executor foundation stacks: SayCan, VoxPoser, GeneralVLA, and VISTA use a high-level LLM/VLM or world model to produce feasible skill sequences, value maps, or goal images that lower-level control follows [S2,S6,S22,S23].
- End-to-end tokenized VLAs: RT-2, RT-2-X, and OpenVLA adapt a large VLM or VLM-like backbone to output robot actions directly, usually as discrete action tokens [S5,S7,S13,S14].
- Open-source generalist policy pretraining: Open X-Embodiment, Octo, and OpenVLA emphasize heterogeneous robot data mixtures and practical fine-tuning to new tasks, sensors, and embodiments [S7,S12,S13,S14].
- Diffusion or flow-based action generation: CogACT uses a diffusion action transformer, pi0 and pi0.5 use flow matching, and RDT-1B extends diffusion-based foundation modeling to bimanual manipulation [S16,S17,S18,S25].
- Self-improving or rapidly adaptable foundation agents: RoboCat and Gemini Robotics emphasize fast adaptation to novel tasks and embodiments and, in RoboCat's case, self-generated data for additional training rounds [S11,S19].

### Representative System Pipelines
- RT-2 and OpenVLA pipeline: start from a pretrained VLM backbone, add robot observation and language tokens, discretize actions into tokens, decode tokens back to Cartesian or gripper actions, and close the loop online on the robot [S5,S13,S14].
- Open X plus Octo pipeline: aggregate cross-lab robot trajectories into a standardized data mixture, pretrain a transformer policy across embodiments, then fine-tune to a new platform with language or goal-image conditioning and modest compute [S7,S12].
- pi0 and pi0.5 pipeline: keep a pretrained VLM backbone for semantics, attach a continuous generative action expert based on flow matching, co-train on heterogeneous robot and semantic data, then optionally specialize for long-horizon tasks in new homes [S16,S18].
- CogACT and RDT-1B pipeline: use a VLM or multimodal transformer for perception and task context, then hand off to a diffusion-based action module that models multi-step continuous actions and better handles multimodal manipulation outcomes [S17,S25].
- VoxPoser, GeneralVLA, VISTA, and OG-VLA pipeline: use a foundation model to infer affordances, spatial constraints, 3D paths, or visual subgoals over the current scene, then execute with a lower-level policy or planner that updates after each observation [S6,S21,S22,S23].

### Evaluation Tasks
- Single-step pick-and-place, reorientation, and relational placement tasks on unseen household objects or unseen object combinations [S1,S5,S12,S13,S20,S21].
- Language-conditioned multi-object tasks with distractors, unseen backgrounds, changed object sizes or shapes, and unseen target-object categories [S5,S13,S14,S15,S20].
- Long-horizon chores such as table cleaning, room cleanup, drawer manipulation, sorting, and multi-stage household tasks in previously unseen homes or scenes [S2,S17,S18,S19].
- Dexterous or bimanual tasks such as folding laundry, assembling boxes, bag packing, and other high-dimensional manipulation routines [S16,S18,S19,S25].
- Cross-robot or cross-setup transfer tasks in which a pretrained policy is adapted to a new arm, camera arrangement, or embodiment with a few demonstrations or short fine-tuning [S11,S12,S13,S19,S20,S25].
- Benchmark-style stress tests that vary camera pose, lighting, confounding objects, unseen objects, and instruction phrasing to probe failure under OOD shifts [S15,S21,S23].

### Common Metrics
- Episode or task success rate is the dominant metric, usually averaged over many tasks, scenes, or robot embodiments [S5,S12,S13,S15,S16,S17,S18,S19,S20,S21,S23,S24,S25].
- OOD generalization success is frequently broken down by novel object, novel background, novel instruction, novel pose, or novel environment conditions [S5,S13,S15,S18,S19,S20,S21,S23,S25].
- Cross-embodiment adaptation is often quantified by post-fine-tuning success rate versus the number of demonstrations, hours of training, or parameter-efficiency method used [S11,S12,S13,S19,S20,S24,S25].
- Some papers report relative or absolute gains over baselines such as RT-2-X, Octo, Diffusion Policy, or VoxPoser rather than only raw success [S13,S17,S19,S21,S22,S23].
- A smaller but important secondary set of metrics includes training throughput, GPU memory, inference efficiency, or evaluation latency, reflecting the engineering cost of deploying large VLAs [S13,S24].

### Best Reported Capabilities
- RT-2 provides one of the clearest early demonstrations that web-pretrained semantics can improve robot control on novel objects and semantic reasoning tasks such as selecting the smallest item or an improvised tool [S5].
- OpenVLA reports a 16.5 percentage-point absolute success-rate gain over RT-2-X across 29 tasks and multiple robot embodiments, with especially strong gains on multi-object, language-grounded fine-tuning tasks relative to Diffusion Policy [S13,S14].
- pi0 shows that a VLM-backed continuous action generator can pretrain across single-arm, dual-arm, and mobile-manipulation data and then execute zero-shot or fine-tuned dexterous tasks such as folding laundry and assembling boxes [S16].
- pi0.5 extends that line to open-world household generalization, reporting 10 to 15 minute kitchen and bedroom cleanup behaviors in new homes not present in training [S18].
- Gemini Robotics reports robustness to variations in object types and positions, handling unseen environments, and following diverse open-vocabulary instructions; those claims are directly stated in the abstract, while stronger quantitative comparisons need paper-level table verification before being treated as settled [S19].
- ForceVLA reports a 23.2% average task-success improvement over strong pi0-based baselines and up to 80% success on plug insertion, showing that force can be treated as a first-class modality inside a VLA stack rather than as a separate post-hoc controller [S26].
- HapticVLA reports an 86.7% mean real-world success rate while removing inference-time tactile sensing, showing that contact-aware behavior can be distilled into a VLA without keeping tactile hardware in the deployment loop [S27].
- TacVLA reports average improvements of 20% on disassembly, 60% on in-box picking, and 2.1x under visual occlusion, which makes it a strong 2026 example of explicit tactile-token fusion inside a VLA [S28].
- ForceVLA2 reports 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks, with gains reaching 35.0% even on fragile-object behaviors where overload and instability matter, strengthening the case for hybrid force-position outputs inside the VLA stack.
- CompliantVLA-adaptor reports that compliance augmentation raises overall success on contact-rich tasks from 9.86% to 17.29%, showing that explicit compliance is becoming a measurable adaptation axis for VLAs rather than a pure controller-side heuristic.
- CogACT shows that replacing simple action quantization with a specialized diffusion action module substantially improves success and generalization to unseen objects and backgrounds over OpenVLA-scale models [S17].
- OG-VLA reports over 40% relative improvements on unseen-environment benchmarks while retaining strong seen-setting performance, indicating that explicit 3D spatial normalization materially helps object generalization [S21].
- RDT-1B brings the same foundation-model story to bimanual manipulation, with reported zero-shot generalization to unseen objects and scenes and new-skill acquisition from only 1 to 5 demonstrations [S25].

### Failure Modes And Limitations
- Even strong VLAs remain brittle under systematic OOD shifts in lighting, camera viewpoint, confounding objects, unseen objects, and instruction mutations; VLATest makes this limitation explicit across seven representative models [S15].
- OpenVLA's own project page shows that open models still lag larger co-trained systems such as RT-2-X on hard semantic tasks that require internet knowledge not preserved during pure robot-action fine-tuning [S14].
- Most evaluations still center on rigid household objects in controlled labs or curated homes, so performance on transparent, reflective, deformable, articulated, or strongly contact-rich objects remains weakly evidenced [S13,S15,S18,S19,S21,S25].
- Purely 2D image-based VLAs struggle with spatial invariance and camera-pose sensitivity, which directly motivated SpatialVLA, OG-VLA, and other 3D-aware extensions [S20,S21].
- Large diffusion- or flow-based policies improve dexterity but raise deployment costs in data, compute, and latency, which is why later work emphasizes efficient training and action representations [S16,S18,S24,S25].
- Cross-embodiment transfer still usually needs some adaptation data or calibration of action spaces, so truly plug-and-play zero-shot deployment on a novel robot is not yet routine [S7,S12,S13,S19,S24].

### Representative Papers 2021 2026
- CLIPort: What and Where Pathways for Robotic Manipulation | authors: Mohit Shridhar, Lucas Manuelli, Dieter Fox | year: 2021 | venue: Conference on Robot Learning | url: https://arxiv.org/abs/2109.12098 | why it matters: A key early bridge from internet-scale vision-language pretraining into robot manipulation: it combines CLIP semantics with Transporter-style spatial precision and directly targets novel goals and object concepts [S1].
- Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | authors: Michael Ahn et al. | year: 2022 | venue: arXiv preprint / SayCan project | url: https://arxiv.org/abs/2204.01691 | why it matters: Established the influential hierarchical pattern in which a large language model proposes semantically appropriate steps while grounded robot value functions filter for embodiment-feasible actions [S2].
- RT-1: Robotics Transformer for Real-World Control at Scale | authors: Anthony Brohan et al. | year: 2023 | venue: Robotics: Science and Systems | url: https://arxiv.org/abs/2212.06817 | why it matters: RT-1 showed that scaling real-robot data and transformer capacity can produce a single action model with promising task and scene generalization, setting up the later VLA transition [S3].
- PaLM-E: An Embodied Multimodal Language Model | authors: Danny Driess et al. | year: 2023 | venue: arXiv preprint | url: https://arxiv.org/abs/2303.03378 | why it matters: Introduced the embodied multimodal language-model idea: continuous robot observations can be injected into a general language model, enabling positive transfer across robotics and internet-scale multimodal tasks [S4].
- RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | authors: Anthony Brohan et al. | year: 2023 | venue: Conference on Robot Learning | url: https://arxiv.org/abs/2307.15818 | why it matters: The paper that crystallized the VLA paradigm: actions are expressed as tokens inside a VLM-style training objective, leading to improved novel-object generalization and emergent semantic reasoning [S5].
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models | authors: Open X-Embodiment Collaboration et al. | year: 2023 | venue: ICRA 2024 / arXiv | url: https://arxiv.org/abs/2310.08864 | why it matters: Made cross-embodiment robot foundation-model research practical by standardizing 1M-plus trajectories from many labs and demonstrating positive transfer with RT-X models [S7].
- RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation | authors: Yuxiang Zhou et al. | year: 2023 | venue: Transactions on Machine Learning Research | url: https://deepmind.google/research/publications/35829/ | why it matters: Important for showing that a foundation manipulation agent can adapt to novel tasks and embodiments with 100 to 1000 examples and can bootstrap itself with self-generated data [S11].
- Octo: An Open-Source Generalist Robot Policy | authors: Octo Model Team et al. | year: 2024 | venue: Robotics: Science and Systems | url: https://arxiv.org/abs/2405.12213 | why it matters: A widely used open baseline for generalist manipulation: it proved that Open-X-scale pretraining could be packaged into a practical open-source policy that adapts to new setups within hours [S12].
- OpenVLA: An Open-Source Vision-Language-Action Model | authors: Moo Jin Kim et al. | year: 2024 | venue: arXiv preprint | url: https://arxiv.org/abs/2406.09246 | why it matters: OpenVLA is the main open-source end-to-end VLA reference point: it outperformed RT-2-X on a broad benchmark while releasing checkpoints, code, and practical fine-tuning recipes [S13,S14].
- $\pi_0$: A Vision-Language-Action Flow Model for General Robot Control | authors: Kevin Black et al. | year: 2024 | venue: RSS 2025 / arXiv | url: https://arxiv.org/abs/2410.24164 | why it matters: Marked a shift from discrete token heads toward continuous flow-based action generation, enabling higher-frequency and more dexterous generalist control across multiple embodiments [S16].
- CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | authors: Qixiu Li et al. | year: 2024 | venue: arXiv preprint | url: https://arxiv.org/abs/2411.19650 | why it matters: A representative diffusion-action VLA that directly tackles the weakness of quantized action heads and shows large gains on unseen objects, backgrounds, and new robots [S17].
- $\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization | authors: Physical Intelligence Team et al. | year: 2025 | venue: preprint / technical report | url: https://arxiv.org/abs/2504.16054 | why it matters: One of the strongest open-world generalization claims in the period: long-horizon mobile-manipulation behaviors in entirely new homes using heterogeneous co-training [S18].
- Gemini Robotics: Bringing AI into the Physical World | authors: Gemini Robotics Team et al. | year: 2025 | venue: arXiv technical report | url: https://arxiv.org/abs/2503.20020 | why it matters: Pushes the frontier toward broadly general, interactive, and dexterous robot foundation models with explicit claims on unseen objects, unseen environments, and novel embodiment adaptation [S19].
- OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model | authors: Ishika Singh, Ankit Goyal, Stan Birchfield, Dieter Fox, Animesh Garg, Valts Blukis | year: 2025 | venue: ICRA 2026 submission / arXiv | url: https://arxiv.org/abs/2506.01196 | why it matters: Representative of the 3D-aware branch that explicitly addresses camera-pose sensitivity and spatial-layout robustness for unseen scenes and objects [S21].
- Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation | authors: Haonan Chen, Jingxiang Guo, Bangjun Wang, Tianrui Zhang, Xuchuan Huang, Boren Zheng, Yiwen Hou, Chenrui Tie, Jiajun Deng, Lin Shao | year: 2025 | venue: arXiv preprint | url: https://arxiv.org/abs/2506.23919 | why it matters: A directly relevant 2025 world-model paper that uses image-generative VLMs to synthesize desired goal states, derive target object pose, and enable object-centric zero-shot manipulation with training-free low-level control.
- ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | authors: Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Cewu Lu, Wenqiang Zhang | year: 2025 | venue: NeurIPS 2025 / arXiv | url: https://arxiv.org/abs/2505.22159 | why it matters: A missing but clearly in-scope 2025 bridge between VLA and force-aware contact control: it adds a force-aware mixture-of-experts module and a five-task force dataset, showing concrete gains on contact-rich manipulation [S26].

### 2026 Preprints
- A Pragmatic VLA Foundation Model | authors: Wei Wu et al. | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.18692 | why it matters: LingBot-VLA emphasizes scale, efficiency, open access, and broad cross-platform generalization, making it a strong 2026 data-scaling and reproducibility point [S24].
- GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning | authors: Guoqing Ma, Siheng Wang, Zeyu Zhang, Shan Yu, Hao Tang | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.04315 | why it matters: A clean hierarchical zero-shot manipulation paper: it uses affordance segmentation, 3D planning, and a low-level 3D-aware controller to generate demonstrations and solve novel tasks without real-robot training data [S22].
- Scaling World Model for Hierarchical Manipulation Policies | authors: Qian Long et al. | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.10983 | why it matters: VISTA explicitly addresses OOD brittleness in VLAs by inserting a world-model planner that generates visual subgoals, boosting novel-scenario performance from 14% to 69% in the reported setup [S23].
- TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation | authors: Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li, Jiaming Jiang, Chenxi Xiao, Ziyuan Jiao | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.20321 | why it matters: Adds a physically grounded tactile-force alignment branch to the VLA literature, with a 10-million-sample tactile-force dataset and explicit grounding of tactile tokens in interaction forces [S29].
- TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation | authors: Kaidi Zhang, Heng Zhang, Zhengtong Xu, Zhiyuan Zhang, Md Rakibul Islam Prince, Xiang Li, Xiaojing Han, Yuhao Zhou, Arash Ajoudani, Yu She | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.12665 | why it matters: A clearly in-scope March 2026 multimodal VLA paper that activates tactile tokens only during contact and reports strong gains under occlusion and fine-grained manipulation [S28].
- HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing | authors: Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov, Ogunwoye Faith Ouwatobi, Marcelino Fernando, Artem Asanov, Ziang Guo, Dzmitry Tsetserukou | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.15257 | why it matters: A notable March 2026 branch showing that tactile-aware behavior can be distilled offline and deployed without inference-time tactile hardware while still outperforming baseline VLAs on contact-rich manipulation [S27].
- FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation | authors: Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.02142 | why it matters: Adds a distinct 2026 force-aware path that distills force into a latent token and explicitly argues that the distilled token can outperform direct force sensing in physical experiments, which broadens the design space beyond hardware-force-at-inference.
- ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | authors: Yang Li, Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, Yunsong Zhou, Jia Zeng, Ce Hao, Jieji Ren, Qiaojun Yu, Cewu Lu, Yu Qiao, Jiangmiao Pang | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.15169 | why it matters: Pushes the force-aware VLA line toward full hybrid force-position outputs and reports strong average gains across five real contact-rich tasks, making it a directly relevant 2026 continuation of ForceVLA.
- CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation | authors: Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.15541 | why it matters: Provides a complementary 2026 direction in which compliance rather than tactile sensing or force sensing is the adaptation target, and it reports a measurable success-rate improvement on contact-rich tasks.

### Seminal Precursors Pre 2021
- Transporter Networks: Rearranging the Visual World for Robotic Manipulation | authors: Andy Zeng et al. | year: 2020 | venue: Conference on Robot Learning | url: https://arxiv.org/abs/2010.14406 | why it matters: Transporter Networks supplied the spatial-manipulation backbone later reused by CLIPort and influenced the broader idea that robust visual correspondence is critical for unseen-object manipulation [S26].
- Learning Transferable Visual Models From Natural Language Supervision | authors: Alec Radford et al. | year: 2021 | venue: ICML 2021; preprint posted before the review window | url: https://arxiv.org/abs/2103.00020 | why it matters: CLIP is the core semantic precursor for open-vocabulary manipulation: CLIPort depends on it directly, and later VLA work inherits the broader recipe of web-scale vision-language pretraining [S27,S1].

### Trends 2021 To 2026
- 2021-2022 emphasized semantic grounding on top of task-specific manipulation backbones, with CLIPort and SayCan combining pretrained language or vision-language priors with more classical manipulation structures [S1,S2].
- 2023 shifted the center of gravity toward embodied multimodal transformers and true VLAs: PaLM-E, RT-2, Open X-Embodiment, and RoboCat all argue that large-scale pretraining and heterogeneous data are the path to generalization [S4,S5,S7,S11].
- 2024 made the area operationally accessible through open-source generalist policies and datasets such as Octo, OpenVLA, DROID, and benchmark-style evaluation frameworks such as VLATest [S9,S12,S13,S15].
- Late 2024 through 2025 saw a move from discrete action tokenization toward continuous generative action heads and more dexterous embodiments, especially in CogACT, pi0, pi0.5, Gemini Robotics, and RDT-1B [S16,S17,S18,S19,S25].
- 2025-2026 increasingly treats spatial understanding as the bottleneck, producing SpatialVLA, OG-VLA, GeneralVLA, and VISTA, all of which add 3D structure, visual subgoals, or explicit trajectory intermediates to improve OOD manipulation on unseen objects [S20,S21,S22,S23].
- A parallel 2025-2026 branch treats contact awareness as the next major frontier inside VLAs themselves: ForceVLA, FD-VLA, ForceVLA2, HapticVLA, TacVLA, TaF-VLA, and CompliantVLA-adaptor all add force, tactile, or compliance structure directly into the policy stack rather than relegating it entirely to a downstream controller.
- Across the whole window, the field moves from closed internal systems toward partially open ecosystems, but robustness lags behind capability demos: open checkpoints and benchmarks improved substantially, yet dependable zero-shot operation in truly messy environments is still unresolved [S7,S12,S13,S15,S18,S19,S24].

### Datasets And Benchmarks
- Open X-Embodiment is the central pretraining corpus for this literature: the collaboration reports 1M-plus real robot trajectories from 22 embodiments and uses them to train RT-X models that transfer across platforms [S7].
- BridgeData V2 remains an important open-vocabulary manipulation dataset for scaling single-arm policies, with 60,096 trajectories across 24 environments on a low-cost robot [S8].
- DROID broadens real-world diversity with 76k trajectories, 564 scenes, and 84 tasks gathered by distributed operators, and it is explicitly used as a transfer or fine-tuning domain in later VLA work [S9,S14].
- LIBERO is a standard benchmark for multi-task and lifelong transfer in manipulation, with 130 tasks generated across several suites; it is commonly used to test whether pretrained VLAs adapt efficiently [S10].
- VLATest is the clearest stress-testing benchmark for this subtopic because it systematically perturbs unseen objects, lighting, confounders, camera pose, and instruction phrasing rather than reporting only hand-picked demos [S15].
- Arnold and Colosseum are important 2025 evaluation suites for 3D-aware VLAs such as OG-VLA, focusing on unseen environments and spatial generalization [S21].
- SimplerEnv is widely used as a reproducible simulation proxy for real-robot policy evaluation on common setups such as Google Robot and WidowX+Bridge, and it is part of the open evaluation stack around newer VLA models [S20,S21].

### Research Gaps
- Robustness under realistic OOD shift remains the main gap: current VLAs still degrade under clutter, camera changes, lighting shifts, instruction variation, and harder unseen objects [S15].
- 3D spatial grounding is still not solved by default 2D VLAs, which is why multiple 2025-2026 papers add point clouds, orthographic views, explicit action grids, or visual subgoals [S20,S21,S22,S23].
- Open-world semantics and open-world control do not align perfectly: OpenVLA, for example, is competitive on robot-specific OOD tasks but weaker than RT-2-X on internet-knowledge-heavy semantic generalization [S14].
- Data efficiency is still poor for the strongest models; many results depend on enormous cross-embodiment datasets or expensive curation, even when downstream adaptation is data-efficient [S7,S9,S18,S19,S24].
- The literature under-covers tactile, force, deformable-object, and transparent-object interaction, which means the present zero-shot story is strongest for vision-dominant rigid-object manipulation [S13,S18,S19,S25].
- Evaluation standards remain fragmented: benchmark diversity is improving, but many papers still publish custom task suites that make direct comparison difficult [S15,S21,S24].

### Opportunities For Single Manipulator Systems
- A single-arm system with one static RGB camera plus a wrist camera is now a realistic target platform for open-source VLAs such as OpenVLA and Octo, especially when paired with DROID, BridgeData V2, or LIBERO-style fine-tuning [S8,S9,S10,S12,S13,S14].
- For tasks involving unseen objects and language grounding, OpenVLA is a strong default backbone because it is open, supports LoRA fine-tuning on consumer hardware, and performs well in multi-object, multi-instruction settings [S13,S14].
- If the application is especially sensitive to object pose variation or scene geometry, 3D-aware add-ons from SpatialVLA or OG-VLA are promising because they directly target spatial invariance rather than relying on 2D image tokens alone [S20,S21].
- For longer-horizon tasks, the most promising architecture for a single manipulator is likely hierarchical: pair a high-level VLM or world model that reasons about subgoals with a lower-level VLA that handles short-horizon control, following the SayCan, VoxPoser, GeneralVLA, and VISTA pattern [S2,S6,S22,S23].
- Inference from the source set: the best near-term path is not to seek full zero-shot autonomy on arbitrary objects, but to combine broad pretrained semantics with modest task-domain adaptation and stronger 3D perception on a simple single-arm platform [S13,S15,S20,S21,S23].

### Sources
- CLIPort: What and Where Pathways for Robotic Manipulation | url: https://arxiv.org/abs/2109.12098 | type: arXiv abstract page | year: 2021 | notes: Primary source for CLIP-based semantic grounding with Transporter-style spatial manipulation.
- Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | url: https://arxiv.org/abs/2204.01691 | type: arXiv abstract page | year: 2022 | notes: Primary source for the SayCan hierarchical grounding formulation.
- RT-1: Robotics Transformer for Real-World Control at Scale | url: https://arxiv.org/abs/2212.06817 | type: arXiv abstract page | year: 2022 | notes: Primary source for large-scale real-robot transformer control and scaling claims.
- PaLM-E: An Embodied Multimodal Language Model | url: https://arxiv.org/abs/2303.03378 | type: arXiv abstract page | year: 2023 | notes: Primary source for embodied multimodal language modeling and positive-transfer claims.
- RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | url: https://arxiv.org/abs/2307.15818 | type: arXiv abstract page | year: 2023 | notes: Primary source for the VLA formulation, tokenized actions, novel-object generalization, and semantic reasoning claims.
- VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | url: https://arxiv.org/abs/2307.05973 | type: arXiv abstract page | year: 2023 | notes: Primary source for zero-shot trajectory synthesis through VLM-grounded 3D value maps.
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models | url: https://arxiv.org/abs/2310.08864 | type: arXiv abstract page | year: 2023 | notes: Primary source for cross-embodiment dataset scale, RT-X, and positive-transfer claims.
- BridgeData V2: A Dataset for Robot Learning at Scale | url: https://arxiv.org/abs/2308.12952 | type: arXiv abstract page | year: 2023 | notes: Primary source for BridgeData V2 size, diversity, and open-vocabulary multi-task suitability.
- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | url: https://arxiv.org/abs/2403.12945 | type: arXiv abstract page | year: 2024 | notes: Primary source for DROID dataset size, scene diversity, and task count.
- LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | url: https://arxiv.org/abs/2306.03310 | type: arXiv abstract page | year: 2023 | notes: Primary source for the LIBERO benchmark and its 130-task lifelong-learning suites.
- RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation | url: https://deepmind.google/research/publications/35829/ | type: official publication page | year: 2023 | notes: Primary source for self-improvement and 100-1000 example adaptation claims.
- Octo: An Open-Source Generalist Robot Policy | url: https://arxiv.org/abs/2405.12213 | type: arXiv abstract page | year: 2024 | notes: Primary source for 800k-trajectory Open-X pretraining and rapid adaptation to new setups.
- OpenVLA: An Open-Source Vision-Language-Action Model | url: https://arxiv.org/abs/2406.09246 | type: arXiv abstract page | year: 2024 | notes: Primary source for OpenVLA architecture, benchmark numbers, and fine-tuning claims.
- OpenVLA project page | url: https://openvla.github.io/ | type: official project page | year: 2024 | notes: Primary source for detailed OOD task breakdowns, videos, and open-source release details.
- VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation | url: https://arxiv.org/abs/2409.12894 | type: arXiv abstract page | year: 2024 | notes: Primary source for robustness findings under confounders, unseen objects, camera pose, lighting, and instruction mutations.
- $\pi_0$: A Vision-Language-Action Flow Model for General Robot Control | url: https://arxiv.org/abs/2410.24164 | type: arXiv abstract page | year: 2024 | notes: Primary source for flow-matching continuous generalist control across multiple embodiments.
- CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | url: https://arxiv.org/abs/2411.19650 | type: arXiv abstract page | year: 2024 | notes: Primary source for the diffusion action transformer and unseen-object/background generalization claims.
- $\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization | url: https://arxiv.org/abs/2504.16054 | type: paper PDF | year: 2025 | notes: Primary source for heterogeneous co-training and long-horizon cleanup in entirely new homes.
- Gemini Robotics: Bringing AI into the Physical World | url: https://arxiv.org/abs/2503.20020 | type: arXiv abstract page | year: 2025 | notes: Primary source for generality, dexterity, unseen-object robustness, and new-embodiment adaptation claims.
- SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | url: https://spatialvla.github.io/ | type: official project page | year: 2025 | notes: Primary source for zero-shot spatial evaluation summaries, 3D position encoding, and adaptation claims.
- OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model | url: https://arxiv.org/abs/2506.01196 | type: arXiv abstract page | year: 2025 | notes: Primary source for canonical orthographic-view generation and unseen-environment benchmark gains.
- Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation | url: https://arxiv.org/abs/2506.23919 | type: arXiv abstract page | year: 2025 | notes: Primary source for the object-centric world-model branch that generates goal images, derives target object pose, and uses reflection-through-synthesis for zero-shot manipulation.
- GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning | url: https://arxiv.org/abs/2602.04315 | type: arXiv abstract page | year: 2026 | notes: Primary source for hierarchical zero-shot manipulation with affordance segmentation and 3D trajectory planning.
- Scaling World Model for Hierarchical Manipulation Policies | url: https://arxiv.org/abs/2602.10983 | type: arXiv abstract page | year: 2026 | notes: Primary source for world-model-generated goal images and reported OOD gains from 14% to 69%.
- A Pragmatic VLA Foundation Model | url: https://arxiv.org/abs/2601.18692 | type: arXiv abstract page | year: 2026 | notes: Primary source for LingBot-VLA scale, efficiency, and open benchmark positioning.
- RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation | url: https://arxiv.org/abs/2410.07864 | type: arXiv abstract page | year: 2024 | notes: Primary source for bimanual diffusion-based foundation modeling, unseen-object generalization, and few-shot adaptation.
- Transporter Networks: Rearranging the Visual World for Robotic Manipulation | url: https://arxiv.org/abs/2010.14406 | type: arXiv abstract page | year: 2020 | notes: Foundational precursor for spatially structured visual manipulation policies.
- Learning Transferable Visual Models From Natural Language Supervision | url: https://arxiv.org/abs/2103.00020 | type: arXiv abstract page | year: 2021 | notes: Foundational precursor for zero-shot vision-language semantics used throughout the later VLM/VLA literature.
- ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | url: https://arxiv.org/abs/2505.22159 | type: arXiv abstract page | year: 2025 | notes: Primary source for the force-aware VLA branch, including the 23.2% average gain over pi0-based baselines, the five-task ForceVLA-Data dataset, and up to 80% plug-insertion success.
- FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation | url: https://arxiv.org/abs/2602.02142 | type: arXiv abstract page | year: 2026 | notes: Primary source for force-token distillation, inference without physical force sensors, and the claim that distilled force can outperform direct force sensing in physical experiments.
- ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | url: https://arxiv.org/abs/2603.15169 | type: arXiv abstract page | year: 2026 | notes: Primary source for hybrid force-position VLA outputs and the reported 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks.
- CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation | url: https://arxiv.org/abs/2601.15541 | type: arXiv abstract page | year: 2026 | notes: Primary source for compliance augmentation of VLAs and the reported overall success-rate increase from 9.86% to 17.29% on contact-rich tasks.
- HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing | url: https://arxiv.org/abs/2603.15257 | type: arXiv abstract page | year: 2026 | notes: Primary source for tactile-distilled VLA control without inference-time tactile sensing, including the reported 86.7% mean real-world success rate.
- TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation | url: https://arxiv.org/abs/2603.12665 | type: arXiv abstract page | year: 2026 | notes: Primary source for contact-aware tactile-token gating in VLAs and the reported 20%, 60%, and 2.1x gains on contact-rich manipulation settings.
- TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation | url: https://arxiv.org/abs/2601.20321 | type: arXiv abstract page | year: 2026 | notes: Primary source for tactile-force alignment, TaF-Dataset with over 10 million synchronized observations, and force-grounded tactile tokenization.

## Integrated multimodal systems combining vision tactile and force feedback

### Subproblem Definition
This subtopic covers robotic systems that explicitly fuse camera sensing with tactile sensing, force-torque feedback, and/or robot proprioception to improve autonomous reaching, touching, scanning, pushing, grasping, in-hand manipulation, or contact-rich execution on unknown or previously unseen objects. The focus is on closed-loop systems where the multimodal estimate changes the robot's next action, controller, or stopping decision. The boundary excludes pure vision-only manipulation, pure tactile-only exploration unless used only as precursor context, offline representation learning without embodied closed-loop evaluation, and systems that depend on a fixed CAD model or object-specific template library at deployment unless they are used only to clarify historical influences.

### Problem Formulations
- Pre-contact visual approach followed by post-contact tactile or force refinement, where vision gets the robot near the object and touch resolves the final pose or contact ambiguity.
- Active visuo-tactile pose estimation of unknown objects in clutter, often with decluttering actions selected before tactile probing.
- Uncertainty-driven visuo-haptic shape completion, where the robot uses a camera to build an initial shape hypothesis and chooses the next touch to reduce occluded-region uncertainty.
- Closed-loop visuo-tactile SLAM or tracking of unknown in-hand objects, jointly estimating pose and shape while the object moves and becomes visually occluded.
- Multimodal parameter inference during non-prehensile interaction, such as pushing while fusing vision, touch, and proprioception to infer object properties or control target pose.
- Contact-rich policy learning or world modeling, where fused vision-tactile-proprioceptive streams support insertion, wiping, fluid handling, or other tasks that require online contact-state reasoning.

### Sensing Modalities
- RGB and RGB-D cameras are used from wrist-mounted, end-effector-mounted, or external viewpoints to provide coarse object pose, segmentation, scene context, or pre-contact servoing cues.
- Dense vision-based tactile sensors such as GelSight, DIGIT, GelSlim, and flexible optical tactile pads dominate the tactile side because they provide local contact geometry, slip, and shear as image-like observations.
- Wrist force-torque sensors and force-regulated controllers appear in some systems, especially pivoting, pushing, and precision assembly, but are less common than vision-based tactile sensing in the current literature.
- Robot proprioception, including joint states, gripper width, end-effector pose, and motion history, is used almost everywhere to register tactile readings in a common frame and to stabilize control.
- Several systems treat tactile images as local point clouds, local surface normals, slip/shear fields, or latent contact states rather than as raw images only.
- Recent 2025-2026 systems additionally model synchronized video, tactile, and action trajectories as a world-model dataset for predicting short-horizon contact evolution.

### Action Space And Robot Setup
- Single-arm setups with parallel grippers or tactile fingertips use vision for coarse positioning and tactile contact for local servo correction, transparent-object poking, or shape completion.
- Dexterous or multi-fingered hands with wrist cameras perform in-hand reorientation, rotation, or reconstruction while fusing tactile observations from multiple fingertips with global vision.
- Two-robot or bimanual systems appear in dense-clutter decluttering and in fine-grained manipulation, where one arm stabilizes or clears the scene and the other performs the multimodal contact-rich action.
- Non-prehensile setups include pushing and pivoting, where the action space mixes end-effector motion, gripper width, or force profile control with tactile or force-based feedback.
- Portable visuo-tactile grippers and low-cost flexible tactile hardware are increasingly used for data collection and imitation learning on insertion, fluid transfer, wiping, and reorientation tasks.
- Most embodiments are tabletop manipulators with one object or one target contact region at a time, not mobile manipulators operating in large unstructured workspaces.

### Method Families
- Collocated vision-tactile servoing: use a camera mounted near the tactile contact point to improve pre-contact localization and then use tactile sensing to refine contact and pose after touch.
- Active visuo-tactile interactive perception: combine visual scene understanding, action selection, and tactile probing to localize unknown objects in clutter or under ambiguity.
- Uncertainty-driven visuo-haptic reconstruction: estimate a partial shape from vision, choose the next exploratory touch using uncertainty, and feed the result back into grasping or manipulation.
- Graph-based and neural-field visuo-tactile tracking: jointly estimate unknown object pose and shape during in-hand manipulation, often under severe visual occlusion.
- Hybrid visuo-force or visuo-tactile control: split the task into a coarse vision stage and a fine tactile/force stage for pushing, pivoting, insertion, or orientation control.
- Representation-learning and world-model systems: learn fused visuo-tactile-proprioceptive representations or predictive contact models that improve long-horizon contact-rich policies.

### Representative System Pipelines
- Collocated visual approach and tactile refinement | pipeline: Collocated camera estimates pre-contact pose or approach direction -> robot visually servos toward object -> tactile contact provides local correction of contact point and pose -> controller updates the final motion or grasp. | examples: ['Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization', 'Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping']
- Active clutter-aware visuo-tactile perception | pipeline: RGB-D scene parsing -> declutter graph or active-view selection -> autonomous removal or probing action -> tactile and visual pose update with information-gain-driven touch selection -> target-object pose estimate for downstream manipulation. | examples: ['Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter']
- Visuo-tactile object tracking and reconstruction | pipeline: Wrist/global vision plus fingertip tactile streams -> factor graph or neural-field object model -> pose and shape update under occlusion -> reconstruction stitched over time -> manipulation continues with updated estimate. | examples: ['FingerSLAM', 'NeuralFeels', 'ViTaSCOPE']
- Uncertainty-driven visuo-haptic shape completion | pipeline: Initial camera point cloud -> implicit shape model with uncertainty -> next-best touch selected on high-uncertainty region -> touch and empty-space constraints fused back into model -> improved grasp or manipulation plan. | examples: ['Active Visuo-Haptic Object Shape Completion', 'Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation']
- Policy or world-model based contact-rich manipulation | pipeline: Synchronized video, tactile, and proprioceptive data -> fused latent or 3D multimodal representation -> policy or world model predicts contact-relevant future state -> high-frequency controller or diffusion policy executes action -> tactile mismatch triggers correction. | examples: ['3D-ViTac', 'Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception', 'Visuo-Tactile World Models', 'OmniVTA']

### Evaluation Tasks
- Visual servoing and localization immediately before and after first contact.
- Transparent-object grasping under poor depth cues and strong background or lighting variation.
- Unknown-object pose estimation in dense clutter with decluttering and tactile refinement.
- Unknown-object 3D shape completion or reconstruction for better grasp planning.
- In-hand pose and shape tracking of unseen objects under severe visual occlusion.
- Non-prehensile object pushing or pivoting to a target pose using tactile, force, and proprioceptive feedback.
- Fine-grained contact-rich tasks such as insertion, wiping, fluid transfer, and reorientation where vision-only control is brittle.
- Zero-shot or low-shot transfer to unseen objects, altered geometries, or disturbed execution conditions.

### Common Metrics
- Pose-estimation error, pose drift, or target-pose accuracy in millimeters and degrees.
- Shape reconstruction metrics such as F-score, IoU, point-cloud quality, or uncertainty reduction over successive touches.
- Task success rate for grasping, insertion, pushing, rotation, assembly, wiping, or other manipulation outcomes.
- Improvement relative to vision-only, tactile-only, or single-stage baselines.
- Number of touches, exploration steps, interaction time, or data-efficiency in low-demo and low-epoch regimes.
- Robustness under visual occlusion, transparency, human disturbance, unseen object geometry, or out-of-distribution conditions.
- Physical plausibility metrics in world-model papers, such as object permanence or compliance with motion laws.
- In some force-sensitive tasks, stability or force-regulation quality rather than geometric accuracy alone.

### Best Reported Capabilities
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

### Failure Modes And Limitations
- Many systems still require carefully calibrated tactile hardware and tight camera-sensor extrinsics, making reproduction and deployment harder than vision-only baselines.
- Evidence is concentrated in rigid-object tabletop settings; deformable objects, heavy clutter without prior decluttering, and open-world scene variability remain weakly covered.
- Several methods need deliberate first contact or stable holding conditions, so failures can occur before multimodal fusion can help.
- Local tactile geometry is often ambiguous on smooth, symmetric, or weakly featured objects, especially without a strong visual prior.
- Force-torque sensing is used less systematically than vision-based tactile sensing, so explicit force-aware manipulation remains less mature than visuo-tactile pose and shape estimation.
- Task generalization is often demonstrated on unseen objects within a narrow task family rather than on broad manipulation repertoires.
- World-model and policy-learning systems are promising but still depend on large data collection pipelines, simulation fidelity, or custom hardware that few labs can replicate quickly.

### Representative Papers 2021 2026
- Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization | authors: Arkadeep Narayan Chaudhury, Timothy Man, Wenzhen Yuan, Christopher G. Atkeson | year: 2022 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2204.11686 | why it matters: A canonical pre-contact and post-contact fusion paper: collocated cameras give better priors for servoing and tactile localization, showing why camera-touch geometry should be designed together.
- Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter | authors: Prajval Kumar Murali, Anirvan Dutta, Michael Gentner, Etienne Burdet, Ravinder Dahiya, Mohsen Kaboli | year: 2022 | venue: IEEE Robotics and Automation Letters / ICRA 2022 | url: https://arxiv.org/abs/2202.02207 | why it matters: A representative closed-loop clutter pipeline that combines decluttering actions, active vision, and active touch to estimate the pose of unknown objects more accurately than active vision alone.
- Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping | authors: Jiaqi Jiang, Guanqun Cao, Aaron Butterworth, Thanh-Toan Do, Shan Luo | year: 2022 | venue: arXiv preprint | url: https://arxiv.org/abs/2208.09743 | why it matters: Shows an especially clear multimodal use case: vision proposes a safe poke region on a hard-to-see transparent object, and tactile sensing provides the local geometry needed for successful grasping.
- FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback | authors: Jialiang Zhao, Maria Bauza, Edward H. Adelson | year: 2023 | venue: ICRA 2023 | url: https://arxiv.org/abs/2303.07997 | why it matters: One of the clearest SLAM-style formulations in this subtopic, fusing wrist vision and fingertip touch for 6-DoF localization and reconstruction of unseen in-hand objects.
- Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation | authors: Lukas Rustler, Jiri Matas, Matej Hoffmann | year: 2023 | venue: IROS 2023 | url: https://arxiv.org/abs/2303.04700 | why it matters: Turns multimodal shape completion into a practical manipulation pipeline by selecting uncertainty-reducing touches and demonstrating improved real-robot grasp success.
- Push to know! -- Visuo-Tactile based Active Object Parameter Inference with Dual Differentiable Filtering | authors: Anirvan Dutta, Etienne Burdet, Mohsen Kaboli | year: 2023 | venue: IROS 2023 | url: https://arxiv.org/abs/2308.01001 | why it matters: Extends the subtopic beyond geometry alone by using active pushing with vision and tactile feedback to infer physical object parameters and choose informative exploratory pushes.
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | authors: Sudharshan Suresh, Haozhi Qi, Tingfan Wu, Taosha Fan, Luis Pineda, Mike Lambeta, Jitendra Malik, Mrinal Kalakrishnan, Roberto Calandra, Michael Kaess, Joseph Ortiz, Mustafa Mukadam | year: 2024 | venue: Science Robotics | url: https://arxiv.org/abs/2312.13469 | why it matters: A strong state-of-the-art example of online multimodal implicit perception: neural fields and pose-graph optimization let touch disambiguate severe visual occlusions during in-hand manipulation.
- 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing | authors: Binghao Huang, Yixuan Wang, Xinyi Yang, Yiyue Luo, Yunzhu Li | year: 2025 | venue: CoRL proceedings | url: https://proceedings.mlr.press/v270/huang25e.html | why it matters: Represents the shift from pure estimation to full manipulation policies, fusing tactile and visual observations in a shared 3D space for fine-grained, force-sensitive bimanual skills.
- ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | authors: Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Cewu Lu, Wenqiang Zhang | year: 2025 | venue: NeurIPS 2025 / arXiv | url: https://arxiv.org/abs/2505.22159 | why it matters: A directly relevant multimodal-control paper that makes six-axis force a first-class modality inside a VLA pipeline, rather than leaving contact adaptation to a separate controller.
- Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception | authors: Bowen Deng, Yijiong Lin, Max Yang, Nathan F. Lepora | year: 2025 | venue: IEEE Robotics and Automation Letters | url: https://research-information.bris.ac.uk/en/publications/coarse-to-fine-robotic-pushing-using-touch-vision-and-propriocept/ | why it matters: A clean hybrid-control example: vision handles the coarse phase, tactile and proprioceptive feedback handle the fine phase, and the multimodal split enables orientation control that single-stage pushing cannot achieve.
- ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation | authors: Jayjun Lee, Nima Fazeli | year: 2025 | venue: RSS 2025 | url: https://www.roboticsproceedings.org/rss21/p054.html | why it matters: Pushes beyond object pose to simultaneous estimation of in-hand pose and extrinsic contact, which is central for dexterous manipulation in contact-rich environments.
- Visuo-Tactile World Models | authors: Carolina Higuera, Sergio Arnaud, Byron Boots, Mustafa Mukadam, Francois Robert Hogan, Franziska Meier | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.06001 | why it matters: Shows how visuo-tactile fusion can be elevated from local estimation to predictive planning, with tactile grounding improving both physical fidelity and downstream real-robot success.
- OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | authors: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.19201 | why it matters: Combines large-scale visuo-tactile data, predictive contact modeling, a contact-aware policy, and a reflexive tactile controller, making it one of the strongest 2026 end-to-end multimodal systems in scope.
- TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation | authors: Kaidi Zhang, Heng Zhang, Zhengtong Xu, Zhiyuan Zhang, Md Rakibul Islam Prince, Xiang Li, Xiaojing Han, Yuhao Zhou, Arash Ajoudani, Yu She | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.12665 | why it matters: A March 2026 multimodal VLA paper that uses contact-aware tactile-token gating, directly targeting occlusion and fine-grained manipulation rather than only visual semantic grounding.
- HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing | authors: Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov, Ogunwoye Faith Ouwatobi, Marcelino Fernando, Artem Asanov, Ziang Guo, Dzmitry Tsetserukou | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.15257 | why it matters: Important because it explores a different multimodal design point: using tactile feedback during training and distillation, but not requiring tactile hardware at inference.
- TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation | authors: Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li, Jiaming Jiang, Chenxi Xiao, Ziyuan Jiao | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.20321 | why it matters: A relevant 2026 multimodal paper that argues tactile data should be aligned to physical force rather than treated as another visual texture, pushing multimodal fusion in a more physically grounded direction.

### 2026 Preprints
- Visuo-Tactile World Models | authors: Carolina Higuera, Sergio Arnaud, Byron Boots, Mustafa Mukadam, Francois Robert Hogan, Franziska Meier | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2602.06001 | why it matters: Introduces multi-task visuo-tactile world models that improve physical plausibility and planning under contact, directly addressing failure modes of vision-only predictive models.
- OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | authors: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.19201 | why it matters: Extends the world-model direction with a much larger visuo-tactile-action dataset and an explicit 60 Hz reflexive tactile correction loop, while reporting generalization to unseen objects and geometries.

### Seminal Precursors Pre 2021
- Localizing a polyhedral object in a robot hand by integrating visual and tactile data | authors: Mohammad Boshra, Hong Zhang | year: 2000 | venue: Pattern Recognition | url: https://www.sciencedirect.com/science/article/abs/pii/S003132039900059X | why it matters: An early direct formulation of camera-touch fusion for in-hand object localization; modern visuo-tactile pose estimators still solve the same ambiguity problem in richer sensing regimes.
- "Touching to See" and "Seeing to Feel": Robotic Cross-modal Sensory Data Generation for Visual-Tactile Perception | authors: Jet-Tsyn Lee, Danushka Bollegala, Shan Luo | year: 2019 | venue: ICRA 2019 | url: https://arxiv.org/abs/1902.06273 | why it matters: Popularized cross-modal visual-tactile reasoning and dataset generation, which later multimodal policy and representation papers build on.
- Visuo-Haptic Grasping of Unknown Objects based on Gaussian Process Implicit Surfaces and Deep Learning | authors: Simon Ottenhaus, Daniel Renninghoff, Raphael Grimm, Fabio Ferreira, Tamim Asfour | year: 2019 | venue: Humanoids 2019 | url: https://h2t.iar.kit.edu/pdf/Ottenhaus2019.pdf | why it matters: A direct precursor for later unknown-object visuo-haptic pipelines: it fuses visual and tactile exploration into a grasp-selection loop for previously unseen objects.
- Active Tactile Object Exploration with Gaussian Processes | authors: Zhengkun Yi, Roberto Calandra, Filipe Veiga, Herke van Hoof, Tucker Hermans, Yilei Zhang, Jan Peters | year: 2016 | venue: IROS 2016 | url: https://is.mpg.de/ps/publications/yieatal16 | why it matters: Established uncertainty-driven next-touch planning on object surfaces, which directly influences later active visuo-haptic shape-completion pipelines.
- Exploratory Tactile Servoing With Active Touch | authors: Nathan F. Lepora, Kirsty Aquilina, Luke P. Cramphorn | year: 2017 | venue: IEEE Robotics and Automation Letters | url: https://research-information.bris.ac.uk/en/datasets/exploratory-tactile-servoing-with-active-touch/ | why it matters: A key precursor for modern closed-loop contact control: tactile sensing is not just perception but a driver of motion, which later multimodal pipelines extend with vision and force information.

### Trends 2021 To 2026
- The field shifts from local multimodal correction modules, such as visual servoing plus tactile refinement, toward end-to-end systems that keep multimodal fusion active throughout the task.
- Unknown-object handling increasingly moves from single rigid objects in simple scenes toward harder settings such as dense clutter, transparency, occlusion, and long-horizon contact-rich tasks, although coverage is still uneven.
- Representations progress from explicit local point clouds and Gaussian-process surfaces to neural fields, contact fields, shared 3D point spaces, and world-model latents.
- Vision-based tactile sensors become the dominant contact modality because they provide geometry, slip, and shear with low cost and high spatial resolution, while explicit force-torque sensing remains more niche.
- Data availability improves materially: FeelSight, Touch in the Wild, and OmniViTac-style datasets mark a move from tiny lab-specific collections to broader multimodal corpora.
- The strongest recent systems increasingly combine coarse global vision with fine tactile or force-sensitive control, rather than trying to solve the entire task from one modality or one control regime.
- Despite this progress, the field still lacks a standard benchmark that jointly measures uncertainty reduction, action efficiency, and downstream manipulation success on unseen objects.

### Datasets And Benchmarks
- FeelSight, released with NeuralFeels, contains 70 real-world and simulation rotation sequences with ground-truth object meshes and tracking, and is explicitly positioned as a visuo-tactile benchmark step.
- FingerSLAM is trained on real-world data from 20 objects and evaluated on 6 unseen objects, making it a small but concrete unknown-object benchmark for in-hand visuo-tactile localization and reconstruction.
- Active Visuo-Haptic Object Shape Completion and Efficient Visuo-Haptic Object Shape Completion rely on real and simulated shape-completion data, and the latter explicitly releases data and code for reproduction.
- Transparent-object work builds custom benchmarks rather than using a standard suite: Where Shall I Touch? creates a large-scale realistic synthetic dataset for transparent-object poking, and Visual-tactile Fusion for Transparent Object Grasping creates a multi-scene synthetic grasping dataset.
- Touch in the Wild contributes a much larger demonstration corpus, with over 2,700 demonstrations across 43 manipulation tasks in 12 environments and more than 2.6 million visuo-tactile pairs.
- OmniVTA introduces the OmniViTac visuo-tactile-action dataset with 21,000+ trajectories across 86 tasks and 100+ objects organized into six interaction patterns.
- There is still no single accepted benchmark that spans unknown-object pose estimation, active touch efficiency, force-sensitive execution, and downstream task success under one evaluation protocol.

### Research Gaps
- A unified benchmark for unknown-object multimodal manipulation is still missing, especially one that spans perception accuracy, sample efficiency, and downstream task performance.
- Explicit fusion with true force-torque sensing is less developed than fusion with vision-based tactile sensing, so force-aware control remains underrepresented relative to pose and shape estimation.
- The field still lacks convincing evaluations in severe clutter, articulation, deformability, or multi-object interactions without simplifications such as decluttering first.
- Most learning-based systems report strong gains but do not always isolate which part of the multimodal stack provides the improvement: sensor placement, representation, controller split, or dataset scale.
- Contact establishment itself is often treated as solved; fewer systems address safe search, first contact, and retreat within one end-to-end loop.
- Simulation-to-real transfer for tactile and force-sensitive policies remains a bottleneck, especially when sensor mechanics, contact friction, and object compliance differ from training assumptions.
- There is room for tighter integration between uncertainty-aware geometric estimators and modern policy or world-model approaches, rather than treating estimation and control as largely separate stages.

### Opportunities For Single Manipulator Systems
- A strong near-term architecture is a wrist RGB-D or RGB camera paired with one or two dense tactile pads and the robot's native proprioception, using vision for coarse approach and tactile sensing only for the last contact-critical phase.
- Transparent and reflective object handling is an especially attractive niche because multimodal gains there are already large and easier to justify than general all-object manipulation.
- Uncertainty-driven visuo-haptic shape completion offers a practical alternative to large policy models for single-arm systems that only need a few informative touches before grasping.
- Coarse-to-fine control is promising for single manipulators because it keeps the vision and tactile/force roles clean: vision handles global alignment, while contact sensing handles the final pose or force regulation.
- Portable visuo-tactile data collection, as in Touch in the Wild, suggests that single-arm systems could now acquire task-specific multimodal data at much lower cost than older dexterous-hand setups.
- The best application targets are semi-structured industrial or lab tasks such as connector insertion, transparent-container handling, precise wiping, and pushing or alignment of unknown rigid parts, where the final centimeters and final newtons matter more than broad semantic reasoning.

### Sources
- Using Collocated Vision and Tactile Sensors for Visual Servoing and Localization | url: https://arxiv.org/abs/2204.11686 | source type: primary paper | why used: Used for the collocated camera-tactile sensor setup, RA-L venue, and the pre-contact visual servo plus post-contact tactile refinement formulation.
- Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter | url: https://arxiv.org/abs/2202.02207 | source type: primary paper | why used: Used for the declutter graph pipeline, active vision plus active touch formulation, and the up to 36% pose-accuracy improvement claim.
- Where Shall I Touch? Vision-Guided Tactile Poking for Transparent Object Grasping | url: https://arxiv.org/abs/2208.09743 | source type: primary paper | why used: Used for the transparent-object grasping pipeline and the 38.9% to 85.2% grasp-success improvement claim.
- Visual-tactile Fusion for Transparent Object Grasping in Complex Backgrounds | url: https://arxiv.org/abs/2211.16693 | source type: primary paper | why used: Used for the transparent-object visual-tactile fusion framework, synthetic dataset note, and the 36.7% grasp-success and 34% classification improvements.
- Active Visuo-Haptic Object Shape Completion | url: https://arxiv.org/abs/2203.09149 | source type: primary paper | why used: Used for the uncertainty-driven active visuo-haptic reconstruction formulation and its RA-L 2022 venue.
- FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback | url: https://arxiv.org/abs/2303.07997 | source type: primary paper | why used: Used for the factor-graph visuo-tactile localization and reconstruction pipeline, 20-train and 6-unseen object split, and ICRA 2023 venue.
- Efficient Visuo-Haptic Object Shape Completion for Robot Manipulation | url: https://arxiv.org/abs/2303.04700 | source type: primary paper | why used: Used for the closed-loop shape-completion pipeline, public code and data note, IROS 2023 venue, and grasp-success numbers after exploratory touches.
- Push to know! -- Visuo-Tactile based Active Object Parameter Inference with Dual Differentiable Filtering | url: https://arxiv.org/abs/2308.01001 | source type: primary paper | why used: Used for the active pushing formulation, next-best exploratory push idea, and IROS 2023 acceptance.
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | url: https://arxiv.org/abs/2312.13469 | source type: primary paper | why used: Used for the neural-field formulation and the quantitative F-score, pose drift, and occlusion-improvement claims.
- NeuralFeels official project page | url: https://suddhu.github.io/neural-feels/ | source type: official project page | why used: Used for the Science Robotics venue, code availability, and FeelSight dataset description.
- 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing | url: https://proceedings.mlr.press/v270/huang25e.html | source type: official proceedings page | why used: Used for the CoRL proceedings entry, unified 3D multimodal representation description, and the claim that it outperforms vision-only policies on fine-grained tasks.
- 3D-ViTac official project page | url: https://binghao-huang.github.io/3D-ViTac/ | source type: official project page | why used: Used for method code and hardware resources, fine-grained task descriptions, and single-arm and bimanual manipulation examples.
- Coarse-to-Fine Robotic Pushing Using Touch, Vision and Proprioception | url: https://research-information.bris.ac.uk/en/publications/coarse-to-fine-robotic-pushing-using-touch-vision-and-propriocept/ | source type: official university publication page | why used: Used for the multi-stage coarse-to-fine formulation, RA-L 2025 venue, and the explicit role split between vision and tactile feedback.
- ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation | url: https://www.roboticsproceedings.org/rss21/p054.html | source type: official proceedings page | why used: Used for the RSS 2025 venue and the in-hand pose plus extrinsic-contact estimation formulation.
- ViTaSCOPE official project page | url: https://jayjunlee.github.io/vitascope/ | source type: official project page | why used: Used for the contact-field description, sim-to-real claim, and code-coming-soon reproducibility note.
- Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper | url: https://arxiv.org/abs/2507.15062 | source type: primary paper | why used: Used for the portable visuo-tactile gripper, cross-attention pretraining setup, and the low-demo, low-epoch manipulation claims.
- Touch in the Wild official project page | url: https://binghao-huang.github.io/touch_in_the_wild/ | source type: official project page | why used: Used for the NeurIPS 2025 project status, code and dataset links, 2,700 demonstrations, 43 tasks, 12 environments, and 2.6 million visuo-tactile pairs.
- Visuo-Tactile World Models | url: https://arxiv.org/abs/2602.06001 | source type: primary paper | why used: Used for the 2026 world-model formulation and the 33%, 29%, and up to 35% improvement claims.
- OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | url: https://arxiv.org/abs/2603.19201 | source type: primary paper | why used: Used for the OmniViTac dataset size, the four-module world-model pipeline, unseen-object generalization claim, and 60 Hz reflexive controller.
- OmniVTA official project page | url: https://mrsecant.github.io/OmniVTA/ | source type: official project page | why used: Used for task categories, real-robot examples, code and data-collection links, and qualitative evidence about adaptive fusion under perturbations.
- Localizing a polyhedral object in a robot hand by integrating visual and tactile data | url: https://www.sciencedirect.com/science/article/abs/pii/S003132039900059X | source type: primary paper | why used: Used as an early precursor for direct visual-tactile localization of grasped objects.
- "Touching to See" and "Seeing to Feel": Robotic Cross-modal Sensory Data Generation for Visual-Tactile Perception | url: https://arxiv.org/abs/1902.06273 | source type: primary paper | why used: Used as a precursor for cross-modal visual-tactile reasoning and data generation.
- Visuo-Haptic Grasping of Unknown Objects based on Gaussian Process Implicit Surfaces and Deep Learning | url: https://h2t.iar.kit.edu/pdf/Ottenhaus2019.pdf | source type: primary paper PDF | why used: Used as a precursor for unknown-object visuo-haptic grasping pipelines that integrate sensing, exploration, and grasp selection.
- Active Tactile Object Exploration with Gaussian Processes | url: https://is.mpg.de/ps/publications/yieatal16 | source type: official publication page | why used: Used as a precursor for uncertainty-driven next-touch planning and GP-based surface modeling.
- Exploratory Tactile Servoing With Active Touch | url: https://research-information.bris.ac.uk/en/datasets/exploratory-tactile-servoing-with-active-touch/ | source type: official dataset/publication page | why used: Used as a precursor for closed-loop tactile perception-and-control during exploration.
- ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | url: https://arxiv.org/abs/2505.22159 | source type: arXiv abstract page | why used: Used to cover the 2025 force-aware multimodal VLA branch, including the 23.2% average gain over pi0-based baselines and the five-task ForceVLA-Data dataset.
- TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation | url: https://arxiv.org/abs/2603.12665 | source type: arXiv abstract page | why used: Used to cover the March 2026 tactile-token VLA branch, including the reported 20%, 60%, and 2.1x improvements under contact-rich and occluded settings.
- HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing | url: https://arxiv.org/abs/2603.15257 | source type: arXiv abstract page | why used: Used to capture the distilled tactile-aware VLA branch and the reported 86.7% mean real-world success rate without inference-time tactile sensing.
- TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation | url: https://arxiv.org/abs/2601.20321 | source type: arXiv abstract page | why used: Used to cover physically grounded tactile-force alignment, the TaF-Dataset scale, and the force-aware multimodal VLA branch in early 2026.

## Reinforcement learning for unknown object exploration touch and manipulation

### Subproblem Definition
This subtopic covers reinforcement-learning-centered methods that use tactile, force, proprioceptive, or visuo-tactile observations to choose probing, contact-establishment, correction, or manipulation actions for previously unseen or partially unknown rigid objects under partial observability. Included methods are model-free, model-based, actor-critic, world-model, curiosity-driven, or hybrid RL systems in which a learned policy is a core part of the closed loop for exploration-to-contact or contact-rich manipulation. The boundary excludes pure tactile perception or reconstruction papers without a learned action policy, pure imitation-learning systems without an RL component, known-object-only deployment that depends on object-specific models at test time, and deformable-object work unless it is used only as adjacent context.

### Problem Formulations
- Tactile insertion as an episodic policy that alternates between insertion attempts and pose-correction actions for objects of unknown geometry.
- Touch-only active exploration of an unknown object's surface or shape, where the policy selects informative contacts under a limited touch budget.
- Goal-conditioned tactile pushing without vision, where a model-free or model-based policy must drive an unknown object to a target pose under disturbances.
- Bimanual tactile manipulation of unseen objects, including bi-pushing, bi-reorienting, and bi-gathering, with coordination learned from simulation and transferred to hardware.
- Blind or visuo-tactile dexterous in-hand manipulation, where tactile sensing compensates for missing or unreliable global visual state.
- Two-stage localize-then-execute pipelines, where high-level vision or a VLM identifies the object or region of interest and a reusable local tactile policy performs the contact-rich phase.
- World-model-based contact-rich manipulation, where short-horizon tactile dynamics are predicted explicitly and used for action selection plus reflexive correction.

### Sensing Modalities
- High-resolution optical tactile sensing is dominant, especially TacTip, DIGIT, DigiTac, GelSight-style tactile images, and tactile-flow representations derived from image sequences.
- Proprioception is used nearly everywhere for finger joint state, hand pose, end-effector pose, or object-relative control.
- Force-torque or torque-like signals appear in insertion, force-regulated grasping, and 2026 dexterous manipulation work, either via wrist F/T sensing or current-to-torque calibration.
- Vision is often fused with touch rather than replacing it: examples include vision-based rewards in See to Touch, egocentric vision in ViTaL, visual attention in VTT, and visuo-tactile world modeling in OmniVTA.
- Several systems are intentionally touch-first or touch-only after contact, especially Tactile-RL for Insertion, tactile pushing, tSLAM, AcTExplore, TacGNN, and some dexterous in-hand policies.
- The dominant sensing pattern is multimodal partial observability: vision gives coarse scene context, while touch and proprioception resolve the final local contact state.

### Action Space And Robot Setup
- Single-arm insertion systems usually choose between insertion attempts and small pose-correction motions, often with tactile images or tactile flow as observations.
- Single-arm tabletop systems in Tactile Gym 2.0 and tactile pushing operate with Cartesian motion commands for edge following, surface following, and pushing-to-goal tasks.
- Bimanual systems such as Bi-Touch use two industrial robot arms, each with a tactile fingertip, and learn coordinated motions for object transport and reorientation.
- Dexterous in-hand systems use anthropomorphic hands such as ADROIT, Allegro, or five-finger research hands, typically commanding joint-level actions or higher-level reorientation objectives.
- Hybrid local-policy systems such as ViTaL separate global reaching from local contact execution, so the local action space is intentionally robot-centered and scene-agnostic.
- 2026 dexterous sim-to-real work extends the action space toward explicit force-tracking and reorientation commands, not only pose control.

### Method Families
- Model-free deep RL: actor-critic or policy-gradient methods for tactile insertion, pushing, bimanual manipulation, and dexterous in-hand policies.
- Model-based RL and planning: tactile predictive models or learned multimodal latent dynamics used for control, as in Manipulation by Feel, VTT, and OmniVTA.
- Curiosity-driven or intrinsic-motivation exploration: policies that explicitly seek informative touches for unknown-object reconstruction, such as tSLAM and AcTExplore.
- Hybrid RL with structured priors: curriculum learning, residual RL, behavior-cloned visual encoders, or reactive tactile controllers combined with a learned policy.
- Sim-to-real tactile RL: policies trained in simulation and transferred through tactile image translation, dynamics randomization, latent distillation, or tactile-specific simulation models.
- World-model and latent-distillation approaches: newer methods that learn predictive visuo-tactile dynamics or tactile state estimators to improve sample efficiency and generalization.

### Representative System Pipelines
- Curriculum tactile insertion | pipeline: Tactile image or tactile flow after failed insertion -> policy predicts pose correction -> new insertion attempt -> repeat until insertion succeeds or attempt budget is exhausted. | examples: ['Tactile-RL for Insertion']
- Sim-to-real tactile pushing | pipeline: Current tactile observation plus goal state -> model-free or model-based RL policy -> Cartesian pushing action -> updated tactile observation and object displacement -> repeat. | examples: ['Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing']
- Bimanual tactile coordination | pipeline: Two tactile fingertip streams plus arm proprioception -> deep RL policy with goal-update mechanism -> synchronized dual-arm actions -> real-world tactile sim-to-real transfer. | examples: ['Bi-Touch']
- Unknown-object active touch reconstruction | pipeline: Current tactile history or partial shape estimate -> exploration policy with intrinsic reward -> next touch location or motion -> shape update -> repeat until coverage target. | examples: ['Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects', 'AcTExplore']
- Vision-guided local tactile policy | pipeline: Global visual localization or visual reward construction -> local tactile or visuo-tactile policy optimization -> contact-rich execution on the robot -> optional residual RL adaptation. | examples: ['See to Touch', 'Touch begins where vision ends']
- Predictive visuo-tactile contact control | pipeline: Visuo-tactile encoder -> short-horizon world model predicts contact evolution -> action policy proposes next manipulation action -> reflexive tactile controller corrects mismatch at high frequency. | examples: ['Visuo-Tactile Transformers for Manipulation', 'OmniVTA']

### Evaluation Tasks
- Generalization to unknown-geometry insertion objects and novel peg or receptacle shapes.
- Goal-directed tactile pushing of unseen objects to target poses under disturbances.
- Edge following and surface following with tactile RL benchmarks.
- Touch-only or touch-dominant reconstruction of unknown object surfaces under a fixed exploration budget.
- Bimanual unseen-object bi-pushing, bi-reorienting, and bi-gathering.
- Blind or visuo-tactile dexterous tasks such as peg pick-and-place, bowl unstacking, slender-object flipping, in-hand rotation, reorientation, wiping, and assembly.

### Common Metrics
- Task success rate, often on held-out objects, held-out environments, or held-out object configurations.
- Attempts to success or average number of corrective actions before insertion or task completion.
- Coverage or reconstruction quality metrics such as IoU and F-score for exploration-oriented methods.
- Trajectory quality metrics such as pushing path length, cumulative reward, return, or time to completion.
- Robustness under perturbations, large disturbances, distractors, or sim-to-real transfer without fine-tuning.
- Task-specific dexterous metrics such as number of goals reached, state-prediction RMSE, or force-tracking quality.

### Best Reported Capabilities
- Tactile-RL for Insertion reports that the best learned agent configuration, RL plus curriculum plus tactile flow, inserts 4 novel objects with over 85.0% success rate within 3 to 4 attempts.
- AcTExplore reports 95.97% average IoU coverage on unseen YCB objects while being trained only on primitive shapes, which is one of the strongest unknown-object active-touch reconstruction results in this period.
- Curiosity-driven tSLAM reports reconstruction of objects of varying complexity within 6 seconds of interaction and cross-dataset transfer from 3D Warehouse training objects to ContactDB test objects.
- See to Touch reports 73% success across six challenging dexterous tasks on a four-fingered Allegro hand, with 108% higher performance than policies using tactile and vision rewards together and 135% higher than policies without tactile observations.
- ViTaL reports around 90% success on contact-rich tasks in unseen environments and explicitly claims robustness to distractors using a reusable local tactile policy plus residual RL.
- PTLD reports a 182% improvement over a proprioception-only policy on benchmark in-hand rotation and a 57% improvement in goals reached for tactile in-hand reorientation.
- OmniVTA introduces a 21,000-plus trajectory visuo-tactile-action dataset spanning 86 tasks and 100-plus objects, then reports better real-robot generalization to unseen objects and geometric configurations than prior baselines.
- Closing the Reality Gap demonstrates zero-shot sim-to-real dexterous tactile manipulation with controllable grasp-force tracking and object reorientation on a five-finger hand trained entirely in simulation.

### Failure Modes And Limitations
- Most systems remain restricted to rigid single-object or fixture-based laboratory tasks, with weak evidence in cluttered or open-world scenes.
- Touch remains highly local, so policies often need careful contact initialization, repeated corrections, or a preceding visual localization stage.
- Sim-to-real transfer is still fragile: Bi-Touch explicitly reports unwanted squeezing in one task, and many methods depend on tactile image translation, privileged information, or extensive calibration.
- Generalization claims are usually across small held-out object sets or geometry families rather than broad household-object diversity.
- RL sample efficiency is still a bottleneck, which is why curricula, pretrained encoders, model-based latents, and world models appear repeatedly.
- Benchmark fragmentation makes comparisons difficult because insertion, pushing, dexterous in-hand tasks, and active exploration are usually evaluated on different custom suites.
- Several recent 2026 systems promise public code or data but had not fully released all assets by 2026-03-23, limiting immediate external verification.

### Representative Papers 2021 2026
- Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry | authors: Siyuan Dong, Devesh K. Jha, Diego Romeres, Sangwoon Kim, Daniel Nikovski, Alberto Rodriguez | year: 2021 | venue: ICRA 2021 | url: https://arxiv.org/abs/2104.01167 | why it matters: A direct early-window unknown-object RL result: tactile insertion is formulated as a correction policy that generalizes to novel geometries.
- Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch | authors: Yijiong Lin, John Lloyd, Alex Church, Nathan F. Lepora | year: 2022 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2207.10763 | why it matters: The main benchmark and software substrate for tactile RL in this period, covering object pushing, edge following, and surface following with sim-to-real transfer.
- Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects | authors: Yujie Lu, Jianren Wang, Vikash Kumar | year: 2022 | venue: arXiv preprint | url: https://arxiv.org/abs/2204.00035 | why it matters: A clear curiosity-driven exploration paper for touch-only reconstruction of unknown objects, with explicit cross-dataset generalization.
- Visuo-Tactile Transformers for Manipulation | authors: Yizhou Chen, Andrea Sipos, Mark Van der Merwe, Nima Fazeli | year: 2022 | venue: CoRL 2022 | url: https://arxiv.org/abs/2210.00121 | why it matters: Represents the model-based RL branch: it learns multimodal latents for planning and helps establish visuo-tactile representation learning as part of RL policy design.
- Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing | authors: Max Yang, Yijiong Lin, Alex Church, John Lloyd, Dandan Zhang, David A. W. Barton, Nathan F. Lepora | year: 2023 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2307.14272 | why it matters: Provides a rare direct comparison between model-based and model-free tactile RL while demonstrating generalization to unseen objects and pushing scenarios without domain randomization.
- Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning | authors: Yijiong Lin, Alex Church, Max Yang, Haoran Li, John Lloyd, Dandan Zhang, Nathan F. Lepora | year: 2023 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/2307.06423 | why it matters: Extends tactile RL from single-arm tasks to coordinated dual-arm manipulation and tests robustness on unseen real objects under perturbations.
- See to Touch: Learning Tactile Dexterity through Visual Incentives | authors: Irmak Guzey, Yinlong Dai, Ben Evans, Soumith Chintala, Lerrel Pinto | year: 2023 | venue: arXiv preprint | url: https://arxiv.org/abs/2309.12300 | why it matters: Shows that online RL with visually derived rewards can train tactile dexterity directly on a real robot across multiple contact-rich tasks.
- AcTExplore: Active Tactile Exploration of Unknown Objects | authors: Amir-Hossein Shahidzadeh, Seong Jong Yoo, Pavan Mantripragada, Chahat Deep Singh, Cornelia Fermuller, Yiannis Aloimonos | year: 2024 | venue: ICRA 2024 | url: https://arxiv.org/abs/2310.08745 | why it matters: One of the strongest RL exploration results for unknown objects, targeting large-scale active tactile reconstruction rather than only local correction.
- Touch begins where vision ends: Generalizable policies for contact-rich manipulation | authors: Zifan Zhao, Siddhant Haldar, Jinda Cui, Lerrel Pinto, Raunaq Bhirangi | year: 2025 | venue: arXiv preprint | url: https://arxiv.org/abs/2506.13762 | why it matters: Captures the 2025 shift toward reusable local tactile policies that generalize across unseen environments when combined with high-level visual localization.
- OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | authors: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.19201 | why it matters: A major step toward world-model-based visuo-tactile control, pairing a large dataset with predictive contact modeling and reflexive closed-loop correction.

### 2026 Preprints
- Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation | authors: Haoyu Dong, Zhengmao He, Yang Li, Zhibin Li, Xinyu Yi, Zhe Zhao | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2601.02778 | why it matters: Uses an asymmetric actor-critic PPO pipeline with dense tactile feedback and torque sensing to achieve zero-shot sim-to-real force tracking and reorientation.
- PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation | authors: Rosy Chen, Mustafa Mukadam, Michael Kaess, Tingfan Wu, Francois R. Hogan, Jitendra Malik, Akash Sharma | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.04531 | why it matters: Shows a practical 2026 alternative to tactile simulation by distilling tactile state estimation from privileged real-world data into sim-trained manipulation policies.
- OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | authors: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.19201 | why it matters: Represents the world-model branch of the field and expands benchmark scale with a large visuo-tactile-action dataset spanning many contact-rich tasks.

### Seminal Precursors Pre 2021
- Active Tactile Object Exploration with Gaussian Processes | authors: Zhengkun Yi, Roberto Calandra, Filipe Veiga, Herke van Hoof, Tucker Hermans, Yilei Zhang, Jan Peters | year: 2016 | venue: IROS 2016 | url: https://flipveiga.github.io/publication/yi2016active/ | why it matters: A foundational uncertainty-reduction formulation for choosing the next touch on an unknown object surface.
- Exploratory Tactile Servoing With Active Touch | authors: Nathan F. Lepora, Kirsty Aquilina, Luke P. Cramphorn | year: 2017 | venue: IEEE Robotics and Automation Letters | url: https://research-information.bris.ac.uk/ws/files/102887809/Nathan_Lepora_Exploratory_tactile_servoing_with_active_touch.pdf | why it matters: Establishes the action-perception loop for tactile exploration and strongly influences later tactile RL benchmarks for contour and surface following.
- Manipulation by Feel: Touch-Based Control with Deep Predictive Models | authors: Stephen Tian, Frederik Ebert, Dinesh Jayaraman, Mayur Mudigonda, Chelsea Finn, Roberto Calandra, Sergey Levine | year: 2019 | venue: ICRA 2019 | url: https://arxiv.org/abs/1903.04128 | why it matters: A key model-based precursor that learns tactile dynamics and uses tactile MPC, directly anticipating later model-based tactile RL and world-model work.
- On Policy Learning Robust to Irreversible Events: An Application to Robotic In-Hand Manipulation | authors: Pietro Falco, Abdallah Attawia, Matteo Saveriano, Dongheui Lee | year: 2019 | venue: IEEE Robotics and Automation Letters | url: https://arxiv.org/abs/1911.08927 | why it matters: An early hybrid architecture combining reinforcement learning with tactile reactive control to prevent slip and irreversible failures during in-hand manipulation.

### Trends 2021 To 2026
- The field shifts from narrow single-task tactile RL policies toward reusable local contact policies and broader contact-rich manipulation suites.
- Pure tactile observation is increasingly fused with vision, force, or torque rather than used alone, especially when policies must generalize beyond one canonical setup.
- Method design moves from mostly model-free RL toward hybrid pipelines that combine pretrained encoders, curricula, residual RL, predictive latents, or world models.
- Unknown-object claims become stronger over time: early papers often generalize across held-out geometries, while later papers claim transfer to unseen objects, unseen environments, and unseen geometric configurations.
- Sim-to-real remains central throughout the window, but the mechanism evolves from image translation and randomization toward latent distillation and explicit tactile dynamics modeling.
- Benchmark scale improves by 2026, but the field still lacks a universally adopted end-to-end benchmark spanning exploration efficiency, contact safety, and downstream manipulation success.

### Datasets And Benchmarks
- Tactile Gym 2.0 is the main reusable benchmark platform in this subtopic, with object pushing, edge following, and surface following tasks plus open-source simulation and hardware transfer support.
- The Tactile-RL for Insertion study uses a train-versus-novel-object protocol over unknown insertion geometries and is one of the earliest direct unknown-object RL evaluations in the requested window.
- Bi-Touch extends the benchmark ecosystem to dual-arm tasks with bi-pushing, bi-reorienting, and bi-gathering, although it is less standardized across labs than Tactile Gym itself.
- Curiosity-driven tSLAM explicitly trains on 3D Warehouse objects and tests on ContactDB objects, which is one of the clearest cross-dataset generalization checks in touch-only exploration.
- AcTExplore evaluates on unseen YCB objects and provides a strong reconstruction benchmark for active tactile exploration.
- OmniViTac, introduced with OmniVTA in 2026, is the largest benchmark-style dataset in this review: 21,000-plus trajectories, 86 tasks, and 100-plus objects across six interaction patterns.

### Research Gaps
- There is still no common benchmark that jointly measures exploration efficiency, task success, safety, and generalization for unknown-object tactile RL.
- Most papers separate reaching, contact establishment, and contact-rich execution; unified end-to-end policies that safely bridge all phases remain rare.
- Long-horizon partial observability is under-addressed: touch is local, but only a few papers use explicit belief updates or world models strong enough for broad open-world behavior.
- Generalization claims are often limited to small geometry families, so scaling to diverse household objects, clutter, and articulated parts is still unresolved.
- Sim-to-real remains expensive because high-quality tactile simulation and hardware calibration are difficult; 2026 distillation approaches help, but they are still early.
- Few methods report contact safety, object damage, or energy-aware interaction metrics, even though those matter directly for autonomous unknown-object exploration.

### Opportunities For Single Manipulator Systems
- A single manipulator with one tactile fingertip or a tactile parallel-jaw gripper can already target the strongest demonstrated use cases: unknown-geometry insertion, contact-aware pushing, guarded local exploration, and local correction after visual localization.
- The most practical architecture is a two-stage stack: global wrist or eye-in-hand vision to localize the candidate object or receptacle, then a local tactile policy trained in simulation and adapted with residual RL or latent distillation.
- For systems without expensive tactile simulation, PTLD-style privileged latent distillation is promising because it reduces dependence on accurate simulated tactile images.
- For exploration tasks, AcTExplore-style active probing and Tactile Gym-style surface-following tasks suggest a feasible path to single-arm next-best-touch systems that build partial geometry before grasping or insertion.
- For manipulation tasks, tactile flow and short-horizon predictive models appear especially promising because they encode local contact evolution with less global-scene complexity than full VLA systems.
- A strong near-term single-arm research stack would combine tactile flow or tactile images, proprioception, an insertion or probing curriculum, a reusable local contact policy, and explicit stopping rules based on confidence or touch budget.

### Sources
- Tactile-RL for Insertion: Generalization to Objects of Unknown Geometry | url: https://arxiv.org/abs/2104.01167 | source type: primary paper | why used: Used for the unknown-geometry tactile insertion formulation, RL plus curriculum plus tactile-flow result, and over-85-percent success claim.
- Tactile-RL for Insertion project page | url: https://sites.google.com/view/tactileinsertion | source type: official project page | why used: Used for the ICRA 2021 venue metadata and project-level description of novel-object evaluation.
- Tactile Gym 2.0: Sim-to-real Deep Reinforcement Learning for Comparing Low-cost High-Resolution Robot Touch | url: https://arxiv.org/abs/2207.10763 | source type: primary paper | why used: Used for benchmark tasks, supported sensors, and the sim-to-real tactile RL benchmark framing.
- Tactile Gym 2.0 project page | url: https://sites.google.com/view/tactile-gym-2 | source type: official project page | why used: Used for code availability, RA-L metadata, and confirmation of the benchmark's open-source role.
- Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects | url: https://arxiv.org/abs/2204.00035 | source type: primary paper | why used: Used for curiosity-driven touch-only exploration, 6-second reconstruction claim, and 3D Warehouse to ContactDB generalization.
- Visuo-Tactile Transformers for Manipulation | url: https://arxiv.org/abs/2210.00121 | source type: primary paper | why used: Used for the model-based RL and planning representation-learning branch and CoRL 2022 acceptance.
- Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning | url: https://arxiv.org/abs/2307.06423 | source type: primary paper | why used: Used for bimanual tasks, unseen-object perturbation evaluation, RA-L venue, and code availability note.
- Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing | url: https://arxiv.org/abs/2307.14272 | source type: primary paper | why used: Used for the model-based versus model-free comparison, unseen-object generalization claim, and tactile pushing formulation.
- Tactile RL pushing project page | url: https://sites.google.com/view/tactile-rl-pushing/ | source type: official project page | why used: Used for code and video availability on the tactile pushing system.
- See to Touch: Learning Tactile Dexterity through Visual Incentives | url: https://arxiv.org/abs/2309.12300 | source type: primary paper | why used: Used for the TAVI framework, six-task real-robot evaluation, and 73-percent success plus relative-improvement claims.
- See to Touch project page | url: https://see-to-touch.github.io/ | source type: official project page | why used: Used for task list, videos, and code availability.
- AcTExplore: Active Tactile Exploration of Unknown Objects | url: https://arxiv.org/abs/2310.08745 | source type: primary paper | why used: Used for RL-driven unknown-object exploration and the 95.97-percent unseen-YCB IoU coverage result.
- AcTExplore project page | url: https://prg.cs.umd.edu/AcTExplore | source type: official project page | why used: Used for code availability and project-level description.
- Touch begins where vision ends: Generalizable policies for contact-rich manipulation | url: https://arxiv.org/abs/2506.13762 | source type: primary paper | why used: Used for the ViTaL formulation, residual-RL generalization claims, and around-90-percent success in unseen environments.
- ViTaL project page | url: https://vitalprecise.github.io/ | source type: official project page | why used: Used for videos and project-level explanation of the localize-then-execute pipeline.
- OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | url: https://arxiv.org/abs/2603.19201 | source type: primary paper | why used: Used for the world-model architecture, OmniViTac dataset scale, unseen-object generalization claims, and release statement.
- Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation | url: https://arxiv.org/abs/2601.02778 | source type: primary paper | why used: Used for the 2026 actor-critic tactile sim-to-real dexterous manipulation direction and zero-shot transfer claim.
- PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation | url: https://arxiv.org/abs/2603.04531 | source type: primary paper | why used: Used for latent distillation, 182-percent and 57-percent improvement claims, and the no-tactile-simulation transfer strategy.
- Active Tactile Object Exploration with Gaussian Processes | url: https://flipveiga.github.io/publication/yi2016active/ | source type: primary paper page | why used: Used as a foundational pre-2021 precursor for uncertainty-driven next-touch planning.
- Exploratory Tactile Servoing With Active Touch | url: https://research-information.bris.ac.uk/ws/files/102887809/Nathan_Lepora_Exploratory_tactile_servoing_with_active_touch.pdf | source type: primary paper PDF | why used: Used as a foundational pre-2021 precursor for tactile action-perception loops.
- Manipulation by Feel: Touch-Based Control with Deep Predictive Models | url: https://arxiv.org/abs/1903.04128 | source type: primary paper | why used: Used as a pre-2021 precursor for model-based tactile control and predictive tactile dynamics.
- On Policy Learning Robust to Irreversible Events: An Application to Robotic In-Hand Manipulation | url: https://arxiv.org/abs/1911.08927 | source type: primary paper | why used: Used as a pre-2021 precursor for combining RL with tactile reactive control to avoid slip and failures.

## Tactile-guided reaching contact localization and active haptic exploration of unknown objects

### Subproblem Definition
This subtopic covers methods that use tactile sensing, usually together with proprioception and sometimes vision, to localize unknown rigid object surfaces, salient contact features, object pose, or extrinsic contact locations while the robot is interacting with the object. Included systems close the loop by choosing informative touches, sliding or rotating over the surface, or using the localized contact geometry to drive a downstream reach, insertion, or contact-rich manipulation behavior on previously unseen objects. The boundary excludes pure tactile classification, grasp-stability prediction without geometric localization, deformable-object exploration, and methods that require a fully known object-specific codebook or CAD model at deployment unless they are cited only as adjacent background.

### Problem Formulations
- Online joint estimation of unknown object shape and pose from a stream of tactile contacts during planar pushing or in-hand interaction.
- Closed-loop unknown-object 6-DoF localization and 3D reconstruction from visuo-tactile feedback with loop closure or pose-graph optimization.
- Active tactile exploration for surface coverage or reconstruction, where the policy chooses the next touch to maximize coverage or reduce uncertainty.
- Extrinsic contact localization on a grasped object, where touch and motion cues are used to infer where the environment contacts the object.
- One-shot or few-shot tactile localization from local geometry followed by a downstream reach, insertion, or contact-rich manipulation action on unseen geometry.

### Sensing Modalities
- Dense vision-based tactile sensors such as GelSight, DIGIT, and GelSlim-style fingertips dominate the literature because they provide local surface geometry as images or point clouds.
- Robot kinematics and proprioception are used nearly everywhere to transform local contacts into object-frame or world-frame constraints.
- RGB or RGB-D wrist or external cameras are fused with touch in FingerSLAM, NeuralFeels, and ViTaSCOPE to stabilize global pose estimates under partial occlusion.
- Some systems are touch-only, including Tactile SLAM in planar pushing, curiosity-driven tSLAM, AcTExplore, TacLoc, and Touch2Insert after contact is made.
- Force, shear, and motion-consistency cues appear indirectly through tactile image sequences, distributed tactile motion, or shear-field modeling rather than as standalone force-torque pipelines.

### Action Space And Robot Setup
- Planar pushing along an unknown contour with a tactile probe or pusher for simultaneous mapping and pose estimation.
- Anthropomorphic or multi-fingered hands that slide, roll, and re-contact the object to collect local tactile depth maps.
- In-hand exploration with one or more tactile fingertips plus a wrist camera, often on dexterous hands holding a single object.
- Bimanual setups where one hand stabilizes the object and the other performs active tactile exploration to refine pose.
- Single-contact probing followed by registration-guided insertion in peg-hole or connector tasks.
- Robot embodiments are mostly research manipulators with rigid grippers or dexterous hands in highly instrumented tabletop scenes rather than mobile or cluttered field robots.

### Method Families
- SLAM-style geometric inference: joint pose-shape estimation with GPIS, factor graphs, loop closure, or fixed-lag smoothing.
- Learned active exploration: reinforcement learning or curiosity-driven policies that choose where to touch next for maximal information gain or coverage.
- Visuo-tactile neural representations: neural fields, implicit SDFs, and dense fusion networks that use touch to correct occluded visual pose estimates.
- Registration-centric localization: one-shot or incremental partial-to-full registration between tactile point clouds and unknown or minimally parameterized object models.
- Task-oriented contact exploitation: using localized tactile geometry to drive insertion or other contact-rich skills after one or a few touches.

### Representative System Pipelines
- SLAM-style tactile mapping | pipeline: Tactile contact stream -> local surface estimate -> factor-graph pose update -> nonparametric shape update -> repeat during pushing or exploration. | examples: ['Tactile SLAM', 'FingerSLAM']
- RL-driven active surface coverage | pipeline: Current tactile map or tactile-history state -> exploration policy -> next fingertip motion -> new local tactile depth -> fused surface reconstruction. | examples: ['Curiosity-Driven Self-supervised Tactile Exploration', 'AcTExplore', 'Object Pose Estimation through Dexterous Touch']
- Visuo-tactile implicit tracking | pipeline: Vision segmentation and tactile depth estimation -> online neural object field -> pose-graph or optimization backend -> improved pose/contact estimate under occlusion. | examples: ['NeuralFeels', 'ViTaSCOPE']
- Registration for downstream control | pipeline: One or few tactile contacts -> partial geometry reconstruction -> registration against object or task geometry -> direct control action such as insertion. | examples: ['TacLoc', 'Touch2Insert']

### Evaluation Tasks
- Unknown-object shape reconstruction from tactile-only exploration.
- 6-DoF pose estimation of unseen in-hand objects.
- Extrinsic contact localization on grasped objects under occlusion.
- Active exploration efficiency, measured by how quickly coverage or useful pose features are acquired.
- Downstream contact-rich execution such as peg or connector insertion after tactile localization.

### Common Metrics
- Surface reconstruction quality: IoU coverage, F-score, point-cloud or mesh accuracy.
- Pose-estimation quality: translation drift, pose-estimation accuracy in millimeters, and sometimes rotation error.
- Task success: insertion success rate or completion of downstream manipulation objective.
- Exploration efficiency: number of contacts, interaction time, or reaching adequate reconstruction within a short horizon.
- Generalization split quality: performance on unseen objects or cross-dataset transfer.

### Best Reported Capabilities
- AcTExplore reports 95.97% average IoU coverage on unseen YCB objects while training only on primitive shapes, showing strong object-agnostic surface coverage from active touch.
- NeuralFeels reports 81% final reconstruction F-score, 4.7 mm average pose drift, 2.3 mm with known CAD models, and up to 94% tracking improvement over vision-only baselines under heavy occlusion.
- FingerSLAM demonstrates real-world visuo-tactile 6-DoF localization and reconstruction on 6 unseen objects after training on data from 20 objects.
- Curiosity-driven tSLAM reports reconstruction of objects of varying complexity within 6 seconds of touch-only interaction and cross-dataset transfer from 3D Warehouse training to ContactDB testing.
- Touch2Insert reports sub-millimeter pose estimation accuracy in simulation for all tested connectors and an 86.7% average real-robot insertion success rate across three diverse connectors.

### Failure Modes And Limitations
- Most systems remain restricted to single-object, rigid-object, or in-hand settings with controlled contact and limited clutter.
- Dense tactile sensing provides only local geometry, so global localization is ambiguous without repeated contact, loop closure, or auxiliary vision.
- Active exploration policies are often trained in simulation and evaluated on relatively small object sets; scaling to larger shape diversity and contact conditions remains unclear.
- Methods that reconstruct shape online can be slow or contact-budget limited, making them hard to deploy for time-critical reaching tasks.
- Registration-based approaches depend on informative local geometry; symmetric or weakly distinctive contacts remain ambiguous.
- Downstream task success is still demonstrated on narrow families such as handheld unknown objects or a few connector types rather than broad open-world manipulation.

### Representative Papers 2021 2026
- Tactile SLAM: Real-time inference of shape and pose from planar pushing | authors: Sudharshan Suresh, Maria Bauza, Kuan-Ting Yu, Joshua G. Mangelson, Alberto Rodriguez, Michael Kaess | year: 2021 | venue: ICRA 2021 | url: https://arxiv.org/abs/2011.07044 | why it matters: A clean SLAM formulation for unknown-object tactile exploration: GPIS-based shape updates alternate with factor-graph pose estimation during planar pushing.
- Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects | authors: Yujie Lu, Jianren Wang, Vikash Kumar | year: 2022 | venue: arXiv preprint | url: https://arxiv.org/abs/2204.00035 | why it matters: Shifts the field toward learned active touch policies for unknown-object reconstruction, with touch-only exploration and cross-dataset generalization.
- FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback | authors: Jialiang Zhao, Maria Bauza, Edward H. Adelson | year: 2023 | venue: ICRA 2023 | url: https://arxiv.org/abs/2303.07997 | why it matters: A representative visuo-tactile pose-graph system for unseen in-hand objects, combining fingertip tactile sensing, vision, loop closure, and incremental reconstruction.
- AcTExplore: Active Tactile Exploration of Unknown Objects | authors: Amir-Hossein Shahidzadeh, Seong Jong Yoo, Pavan Mantripragada, Chahat Deep Singh, Cornelia Fermuller, Yiannis Aloimonos | year: 2024 | venue: ICRA 2024 | url: https://arxiv.org/abs/2310.08745 | why it matters: A strong object-agnostic active exploration result: RL-driven tactile motion obtains very high unseen-object surface coverage while trained only on primitive shapes.
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | authors: Sudharshan Suresh, Haozhi Qi, Tingfan Wu, Taosha Fan, Luis Pineda, Mike Lambeta, Jitendra Malik, Mrinal Kalakrishnan, Roberto Calandra, Michael Kaess, Joseph Ortiz, Mustafa Mukadam | year: 2024 | venue: Science Robotics | url: https://arxiv.org/abs/2312.13469 | why it matters: Shows online neural-field tracking and reconstruction of novel in-hand objects, with tactile input substantially improving performance under severe visual occlusion.
- Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors | authors: Paris Oikonomou, George Retsinas, Petros Maragos, Costas S. Tzafestas | year: 2025 | venue: arXiv preprint | url: https://arxiv.org/abs/2505.11975 | why it matters: Emphasizes explicit uncertainty reduction and safe next-touch planning for shape reconstruction when only minimal visual priors are available.
- ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation | authors: Jayjun Lee, Nima Fazeli | year: 2025 | venue: RSS 2025 | url: https://arxiv.org/abs/2506.12239 | why it matters: Moves beyond object pose alone to simultaneous estimation of in-hand pose and extrinsic contact fields with a visuo-tactile implicit representation.
- Object Pose Estimation through Dexterous Touch | authors: Amir-Hossein Shahidzadeh, Jiyue Zhu, Kezhou Chen, Sha Yi, Cornelia Fermuller, Yiannis Aloimonos, Xiaolong Wang | year: 2025 | venue: arXiv preprint | url: https://arxiv.org/abs/2509.13591 | why it matters: Uses active bimanual tactile exploration to find pose-critical surface features without prior object geometry, which is directly aligned with uncertainty-reducing tactile localization.
- Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole | authors: Masaru Yajima, Yuma Shin, Rei Kawakami, Asako Kanezaki, Kei Ota | year: 2026 | venue: ICRA 2026 | url: https://arxiv.org/abs/2603.03627 | why it matters: A direct tactile-guided reaching result: one tactile contact is used to reconstruct local cross-sections, estimate relative pose in zero shot, and execute insertion on unseen connectors.
- TacLoc: Global Tactile Localization on Objects from a Registration Perspective | authors: Zirui Zhang, Boyang Zhang, Fumin Zhang, Huan Yin | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.10565 | why it matters: Represents the registration-based direction of the field: dense tactile point clouds and normals are used for object pose localization without rendered tactile data or pre-trained object-specific models.

### 2026 Preprints
- Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole | authors: Masaru Yajima, Yuma Shin, Rei Kawakami, Asako Kanezaki, Kei Ota | year: 2026 | venue: ICRA 2026 / arXiv preprint | url: https://arxiv.org/abs/2603.03627 | why it matters: Shows a concrete transition from tactile localization to controlled reaching: a single tactile interaction estimates relative peg-hole pose on unseen connector geometries.
- TacLoc: Global Tactile Localization on Objects from a Registration Perspective | authors: Zirui Zhang, Boyang Zhang, Fumin Zhang, Huan Yin | year: 2026 | venue: arXiv preprint | url: https://arxiv.org/abs/2603.10565 | why it matters: Pushes tactile localization toward more object-agnostic registration by removing the need for rendered tactile databases or per-object pretrained models.

### Seminal Precursors Pre 2021
- Localizing a polyhedral object in a robot hand by integrating visual and tactile data | authors: Mohammad Boshra, Hong Zhang | year: 2000 | venue: Pattern Recognition | url: https://www.sciencedirect.com/science/article/abs/pii/S003132039900059X | why it matters: An early vision-touch localization formulation that already treats tactile data as the key to resolving occlusion and depth ambiguity during object localization in hand.
- Correcting pose estimates during tactile exploration of object shape: a neuro-robotic study | authors: Claudius Strub, Florentin Worgotter, Helge J. Ritter, Yulia Sandamirskaya | year: 2014 | venue: ICDL-EpiRob 2014 | url: https://ieeexplore.ieee.org/document/6982950/ | why it matters: Directly frames tactile exploration as jointly learning shape while correcting pose drift, which is conceptually very close to later tactile-SLAM formulations.
- Active Tactile Object Exploration with Gaussian Processes | authors: Zhengkun Yi, Roberto Calandra, Filipe Veiga, Herke van Hoof, Tucker Hermans, Yilei Zhang, Jan Peters | year: 2016 | venue: IROS 2016 | url: https://flipveiga.github.io/publication/yi2016active/ | why it matters: A foundational uncertainty-driven next-touch method: the Gaussian-process surface model explicitly chooses exploration actions to reduce geometric uncertainty.
- Exploratory Tactile Servoing With Active Touch | authors: Nathan F. Lepora, Kirsty Aquilina, Luke P. Cramphorn | year: 2017 | venue: IEEE Robotics and Automation Letters | url: https://research-information.bris.ac.uk/ws/files/102887809/Nathan_Lepora_Exploratory_tactile_servoing_with_active_touch.pdf | why it matters: Establishes the idea that tactile perception and control should be closed in the loop so the robot actively moves to maintain and improve contact information.

### Trends 2021 To 2026
- The field moves from tactile-only geometric inference in constrained settings toward multimodal visuo-tactile tracking that explicitly handles heavy visual occlusion.
- Active exploration becomes more learned: curiosity and RL increasingly replace fixed probing strategies, especially for large unknown surfaces.
- Representations shift from explicit local geometric models such as GPIS and stitched point clouds toward neural fields, implicit surfaces, and registration pipelines.
- Recent work increasingly targets object-agnostic deployment, explicitly criticizing object-specific rendered databases or pre-trained codebooks.
- There is a gradual move from pure reconstruction toward task-conditioned use of localized contact geometry, especially insertion and extrinsic contact reasoning.
- Benchmarking is improving, but the subtopic still lacks a single accepted end-to-end benchmark covering localization, exploration efficiency, and downstream manipulation success on unseen objects.

### Datasets And Benchmarks
- YCB object evaluations are common for unseen-object surface coverage or tactile localization, including AcTExplore and TacLoc.
- Curiosity-driven tSLAM reports training on 3D Warehouse objects and testing on ContactDB objects, giving one of the few explicit cross-dataset generalization checks.
- NeuralFeels releases the FeelSight dataset with 70 experiments in simulation and the real world, explicitly positioning it as a benchmarking step for visuo-tactile in-hand perception.
- FingerSLAM uses a real-world dataset collected on 20 objects and evaluates on 6 unseen objects.
- Adjacent known-object localization work contributes reusable benchmarks too, notably YCB-Slide from MidasTouch, but these are not full unknown-object exploration benchmarks.
- The literature still lacks a standard benchmark that jointly measures next-touch efficiency, uncertainty reduction, and downstream success on previously unseen objects.

### Research Gaps
- Standardized benchmarks for unknown-object tactile localization that combine geometry accuracy, uncertainty reduction, and downstream task success are still missing.
- Most methods assume rigid, isolated objects and stable contact; clutter, slip, articulation, and deformability remain underexplored.
- The community lacks strong comparisons between learned exploration policies and explicit information-gain or uncertainty-reduction planners under matched conditions.
- Global ambiguity from local tactile geometry is still a core failure mode for symmetric or low-feature surfaces.
- Real-time performance under strict contact budgets is underreported, which matters for practical reaching and manipulation pipelines.
- Few methods integrate tactile exploration with grasp acquisition and retreat planning in one unified loop for a single manipulator.
- 2026 work suggests a move toward registration-based object-agnostic localization, but robust large-scale real-world validation is still limited.

### Opportunities For Single Manipulator Systems
- A practical near-term architecture is a wrist RGB-D camera plus one dense fingertip tactile sensor, with tactile updates used only when vision becomes occluded or uncertain.
- Registration-based first-touch localization, as seen in TacLoc and Touch2Insert, looks promising for single-arm reaching, insertion, button pressing, and edge finding because it can convert a small number of contacts into an immediate geometric correction.
- Uncertainty-aware next-best-touch planners using minimal visual priors appear attractive for one-arm systems because they avoid the data and training burden of large RL policies while still exploiting tactile geometry.
- SLAM-like backends remain useful when repeated contacts are available; a single manipulator can reuse FingerSLAM and NeuralFeels ideas with a simpler object-centric factor graph or neural SDF.
- The best experimental target for a single manipulator is likely unknown rigid household or industrial parts in semi-structured scenes, where touch can resolve the final few millimeters of pose uncertainty that vision leaves behind.

### Sources
- Tactile SLAM: Real-time inference of shape and pose from planar pushing | url: https://arxiv.org/abs/2011.07044 | source type: primary paper | why used: Used for the SLAM-style unknown-object mapping formulation, ICRA 2021 venue, and planar-pushing setup.
- Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects | url: https://arxiv.org/abs/2204.00035 | source type: primary paper | why used: Used for touch-only active exploration, 6-second reconstruction claim, and 3D Warehouse to ContactDB generalization.
- FingerSLAM: Closed-loop Unknown Object Localization and Reconstruction from Visuo-tactile Feedback | url: https://arxiv.org/abs/2303.07997 | source type: primary paper | why used: Used for unseen-object in-hand localization and reconstruction, factor graph, loop closure, and object counts.
- AcTExplore: Active Tactile Exploration of Unknown Objects | url: https://arxiv.org/abs/2310.08745 | source type: primary paper | why used: Used for active exploration method description and ICRA 2024 acceptance.
- AcTExplore official project page | url: https://prg.cs.umd.edu/AcTExplore | source type: official project page | why used: Used for code availability and the 95.97% IoU coverage claim on unseen YCB objects.
- Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation | url: https://arxiv.org/abs/2312.13469 | source type: primary paper | why used: Used for neural-field formulation, quantitative reconstruction and pose-drift numbers, and FeelSight dataset release.
- NeuralFeels official project page | url: https://suddhu.github.io/neural-feels/ | source type: official project page | why used: Used for Science Robotics venue, code availability, dataset availability, and benchmark-positioning statements.
- Proactive tactile exploration for object-agnostic shape reconstruction from minimal visual priors | url: https://arxiv.org/abs/2505.11975 | source type: primary paper | why used: Used for explicit uncertainty-minimization and minimal-visual-prior active exploration claims.
- ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation | url: https://arxiv.org/abs/2506.12239 | source type: primary paper | why used: Used for simultaneous in-hand pose and extrinsic contact estimation and RSS 2025 acceptance.
- ViTaSCOPE official project page | url: https://jayjunlee.github.io/vitascope/ | source type: official project page | why used: Used for RSS 2025 venue confirmation and code-coming-soon reproducibility note.
- Object Pose Estimation through Dexterous Touch | url: https://arxiv.org/abs/2509.13591 | source type: primary paper | why used: Used for active bimanual tactile exploration without prior object geometry.
- TacLoc: Global Tactile Localization on Objects from a Registration Perspective | url: https://arxiv.org/abs/2603.10565 | source type: primary paper | why used: Used for 2026 registration-based object-agnostic tactile localization and YCB evaluation.
- Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole | url: https://arxiv.org/abs/2603.03627 | source type: primary paper | why used: Used for 2026 tactile-guided insertion, zero-shot claim, sub-millimeter simulation accuracy, and 86.7% real success rate.
- Tac2Pose: Tactile Object Pose Estimation from the First Touch | url: https://arxiv.org/abs/2204.11701 | source type: primary paper | why used: Used only to define the boundary between known-object tactile localization and the unknown-object focus of this review.
- MidasTouch: Monte-Carlo inference over distributions across sliding touch | url: https://arxiv.org/abs/2210.14210 | source type: primary paper | why used: Used only as adjacent context for global tactile localization that still relies on per-object codebooks.
- Localizing a polyhedral object in a robot hand by integrating visual and tactile data | url: https://www.sciencedirect.com/science/article/abs/pii/S003132039900059X | source type: primary paper | why used: Used as an early precursor for tactile-visual localization under occlusion.
- Correcting pose estimates during tactile exploration of object shape: a neuro-robotic study | url: https://ieeexplore.ieee.org/document/6982950/ | source type: primary paper | why used: Used as a precursor for joint tactile shape learning and pose-drift correction.
- Active Tactile Object Exploration with Gaussian Processes | url: https://flipveiga.github.io/publication/yi2016active/ | source type: official paper page | why used: Used as a precursor for uncertainty-driven next-touch planning over object surfaces.
- Exploratory Tactile Servoing With Active Touch | url: https://research-information.bris.ac.uk/ws/files/102887809/Nathan_Lepora_Exploratory_tactile_servoing_with_active_touch.pdf | source type: primary paper PDF | why used: Used as a precursor for closed-loop tactile perception-and-control during exploration.
