---
title: "Active visual exploration and next-best-view control for unknown object approach reach and scan"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23 inclusive; 2026 preprints counted only if publicly available by 2026-03-23."
---

# Active visual exploration and next-best-view control for unknown object approach reach and scan

## Scope
This subtopic covers robot-guided active perception methods that choose new camera viewpoints, and in some cases touch or reorientation actions, to reduce uncertainty about a previously unseen rigid object or object-centric scene region so the robot can scan, approach, touch, or grasp it. The boundary includes eye-in-hand RGB/RGB-D scanning, object-centric next-best-view (NBV) planning, active neural-field reconstruction, visuo-haptic completion, and active view selection for occluded target grasping; it excludes passive single-shot perception, large-scale navigation-only exploration, and manipulation papers that do not actively choose views or information-gathering actions [S1,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S20].

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The shortlist-level quantitative claims in this note are now mostly re-checked from primary PDF text, but several secondary efficiency and robustness comparisons remain at the synthesis-summary level.

### Re-checked Claims
- ActNeRF: 14% PSNR gain, 20% F-score gain, and 71% manipulation-success gain (`verified-primary-pdf`).
- PB-NBV: the primary paper text supports the current qualitative claim that it attains the highest point-cloud coverage with low computational time among its compared methods (`verified-primary-pdf`).
- VISO-Grasp: 87.5% target-oriented grasping success with the fewest grasp attempts (`verified-primary-pdf`).
- Act-VH: the paper supports the current qualitative claim that visuo-haptic completion improves grasp success on novel objects (`verified-primary-pdf`).

### Still Pending
- Non-shortlist efficiency and optimization-overhead comparisons remain partially audited.
- Some one-shot or diffusion-based view-planning comparisons remain synthesis-level interpretations rather than table-level re-checks.

## Inclusion Criteria
- Papers from 2021-03-23 through 2026-03-23 on active object or object-centric scene perception where the robot selects viewpoints or sensing actions online or in one-shot form to improve belief over unknown geometry, occupancy, semantics, grasp affordance, or neural implicit state [S1,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S20].
- Systems with an explicit downstream robotic purpose such as 3D reconstruction, object scanning, target-oriented grasping, or physically touching/reorienting the object to reveal hidden surfaces [S1,S4,S6,S7,S9,S11,S14].
- Primary sources were prioritized: arXiv pages, official conference or journal pages, official project pages, and official publication pages [S1,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S20].

## Exclusion Criteria
- Passive grasp detection, passive shape completion, or pose estimation papers without active viewpoint or sensing-action choice.
- Navigation-scale active mapping and frontier exploration where the main target is whole-scene coverage rather than approaching or scanning a previously unseen object [inference from the source set; contrast object-centric papers such as S4,S7,S10,S14 with scene-scale methods cited but not centered here].
- Inspection papers that assume a fully known CAD model and optimize coverage only for known geometry, except when used as historical precursors before 2021 [S16,S17].
- Dynamic-object, deformable-object, or articulated-object manipulation papers unless the active perception loop is still centered on building an object belief for a mostly static target.

## Problem Formulations
- Iterative NBV for unknown-object reconstruction: choose the next camera pose from a partial explicit or implicit object model to maximize expected information gain, surface coverage, or uncertainty reduction under motion cost [S3,S4,S5,S8,S13].
- One-shot view planning: predict a set of views and a shortest connecting path at once from an initial sparse observation, point cloud, or even a single RGB image, then reconstruct after data capture [S9,S10,S12,S15].
- Interactive visuo-haptic exploration: choose where to touch, poke, or reorient the object based on uncertainty in the current visual belief so hidden surfaces become observable [S1,S6,S11].
- Target-oriented active grasping under occlusion: choose views that reveal target grasp affordances or spatial relationships well enough to execute a grasp on an unseen or heavily occluded object [S7,S14].
- Semantic-targeted active implicit reconstruction: bias exploration toward objects of interest rather than uniform scene coverage, using semantics and uncertainty jointly in the utility [S20].

## Sensing Modalities
- RGB-only sensing is common in neural-rendering and one-shot methods such as NeU-NBV, PRV, DM-OSVP, and VISO-Grasp [S5,S10,S12,S14].
- RGB-D or point-cloud sensing remains common in explicit NBV and visuo-haptic methods such as Act-VH, GMC, PB-NBV, and STAIR [S1,S8,S13,S20].
- Touch or contact sensing is used as an active information source in Act-VH, Poking, and ActNeRF, often alongside force closure or contact-event detection through the manipulator [S1,S6,S11].
- Robot proprioception, known camera poses, and pose re-estimation after interaction are important for closing the loop in ActNeRF and related manipulation-aware systems [S11].
- Foundation-model or language-conditioned semantic signals appear in the 2025 VISO-Grasp system, where they support spatial reasoning and object-centric active view planning [S14].

## Action Space And Robot Setup
- Most systems use a single manipulator or camera rig to move an RGB or RGB-D sensor around a tabletop object, with candidate viewpoints sampled on a sphere, hemisphere, or reachable free-space manifold [S3,S4,S5,S8,S10,S12,S13].
- Eye-in-hand setups are explicit in papers such as the RA-L 2022 uncertainty-guided NeRF policy, which uses a mobile robot with an arm-held camera, and in ActNeRF with a Franka manipulator [S3,S11].
- The action space can include more than camera motion: Act-VH chooses touch locations, Poking performs object-discovery pokes, and ActNeRF chooses between a visual action and a grasp-and-reorient action [S1,S6,S11].
- For grasping in clutter, ACE-NBV and VISO-Grasp use object-centric observation moves that seek views aligned with grasp affordances or target visibility constraints before attempting the grasp [S7,S14].
- One-shot methods reduce repeated online replanning by predicting all needed views and then optimizing a global path through them [S9,S10,S12].

## Method Families
- Probabilistic explicit-map NBV: iterative selection from partial voxel maps using coverage, entropy, or information gain, often with motion-cost terms [S8,S13,S17].
- Implicit or neural-field NBV: uncertainty is estimated from occupancy fields or radiance fields, and the next view is selected to reduce rendering or geometric uncertainty [S3,S4,S5,S20].
- One-shot/global view planning: supervised prediction of all views at once, sometimes with set-covering labels, predicted view counts, or diffusion-generated geometric priors [S9,S10,S12,S15].
- Visuo-haptic interactive exploration: the robot chooses touches, pokes, or reorientation actions to reveal hidden object surfaces [S1,S6,S11].
- Task-aware active grasping: the utility is defined by target grasp affordance, visibility, or target-aware spatial reasoning rather than pure surface coverage [S7,S14].

## Representative System Pipelines
- Act-VH
  - pipeline: Partial point cloud -> implicit surface reconstruction with uncertainty -> choose highest-uncertainty touch location -> execute touch and fuse new information -> use improved shape for grasping.
  - source ids: S1; S2
- NeU-NBV
  - pipeline: Collected RGB images -> image-based neural rendering with uncertainty estimation -> evaluate candidate views in a mapless way -> move camera to the most uncertain informative view -> iterate under a measurement budget.
  - source ids: S5; S21
- OSVP and PRV line
  - pipeline: Initial sparse observation or partial point cloud -> predict required number of views or directly predict a view set -> compute globally shortest path through the set -> collect all views -> reconstruct with an implicit model or NeRF.
  - source ids: S9; S10; S15
- ActNeRF
  - pipeline: Partial NeRF ensemble -> estimate uncertainty and action feasibility -> choose either a visual observation action or a grasp-and-reorient action -> reacquire pose after reorientation -> continue until model quality is good enough for manipulation.
  - source ids: S11
- VISO-Grasp
  - pipeline: Foundation-model-assisted object-centric spatial belief -> active view planning to resolve target invisibility and occlusion -> multi-view uncertainty-aware grasp fusion -> execute 6-DoF target grasp with sequential replanning if needed.
  - source ids: S14

## Evaluation Tasks
- Unknown object 3D reconstruction or shape completion in simulation and on real robots [S1,S3,S4,S5,S8,S9,S10,S12,S13].
- Measurement-efficient scanning: reaching a reconstruction-quality or coverage target with fewer views, shorter paths, or lower planning time [S8,S9,S10,S12,S13].
- Interactive object discovery or completion through poking, touching, or reorientation [S1,S6,S11].
- Downstream grasping of previously unseen or occluded targets after active sensing [S1,S6,S7,S11,S14].
- Semantic-targeted active reconstruction in scenes containing objects of interest rather than uniform scene coverage [S20].

## Common Metrics
- Surface coverage or point-cloud coverage for unknown-object scan completeness [S8,S13,S16,S17].
- Reconstruction accuracy metrics such as F-score, geometry quality, or point-cloud/shape accuracy [S1,S4,S11].
- Novel-view or rendering metrics such as PSNR for neural-field models [S10,S11].
- Movement cost, travel distance, path length, planning time, or total computational time [S8,S10,S12,S13].
- Task success metrics such as grasp success rate, target-oriented grasp success, and number of grasp attempts [S1,S7,S11,S14].

## Best Reported Capabilities
- ActNeRF reports improvements of 14% in PSNR, 20% in F-score, and 71% in manipulation success for unseen orientations over its compared methods, showing that active view choice plus reorientation can directly benefit downstream manipulation [S11].
- PB-NBV reports the highest point-cloud coverage with low computational time among its compared frameworks in simulation, with supporting real-world feasibility experiments [S13].
- Act-VH reports better reconstruction than five baselines and significantly higher grasp success than the best reconstruction baseline on all 10 tested novel objects [S1,S2].
- PRV reports good reconstruction quality with significantly reduced movement cost and planning time compared to baselines, showing the value of predicting how many views are needed instead of scanning blindly [S10].
- VISO-Grasp reports 87.5% target-oriented grasping success with the fewest grasp attempts in real-world experiments under severe occlusion and invisibility constraints [S14].

## Failure Modes And Limitations
- Greedy iterative NBV can waste late-stage views on tiny residual regions and still leave holes or sparse surfaces, which motivated the shift toward global optimization and one-shot planning [S8].
- Visual-only neural or diffusion-based planners can struggle when the prior geometry is wrong, incomplete, or scale-ambiguous; DM-OSVP explicitly notes missing scale information and performance inadequacies in a test case, and it reports nontrivial generation and optimization overhead [S12].
- Purely visual exploration cannot reveal hidden support or bottom surfaces unless the object is touched or reoriented, which is exactly the limitation ActNeRF addresses [S11].
- Semantic-targeted methods can depend strongly on label quality; STAIR identifies accurate semantic labels as an assumption and noisy semantics as an open issue [S20].
- Inference from the source set: robustness to transparent, reflective, deformable, or dynamic objects remains weakly evidenced because most experiments use rigid tabletop objects with controlled sensing conditions [S1,S3,S4,S5,S8,S9,S10,S11,S12,S13,S14].

## Representative Papers
- [[Paper - Active Visuo-Haptic Object Shape Completion|Active Visuo-Haptic Object Shape Completion]] (2022, IEEE Robotics and Automation Letters)
- [[Paper - Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields|Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields]] (2022, IEEE Robotics and Automation Letters)
- [[Paper - Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization|Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization]] (2023, IEEE Robotics and Automation Letters)
- [[Paper - NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering|NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering]] (2023, IROS 2023)
- [[Paper - Perceiving Unseen 3D Objects by Poking the Objects|Perceiving Unseen 3D Objects by Poking the Objects]] (2023, ICRA 2023)
- [[Paper - Affordance-Driven Next-Best-View Planning for Robotic Grasping|Affordance-Driven Next-Best-View Planning for Robotic Grasping]] (2023, Conference on Robot Learning)
- [[Paper - Active Implicit Reconstruction Using One-Shot View Planning|Active Implicit Reconstruction Using One-Shot View Planning]] (2024, ICRA 2024)
- [[Paper - How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF?|How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF?]] (2024, ICRA 2024)
- [[Paper - Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions|Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions]] (2024, arXiv preprint; ICRA 2024 RoboNeRF workshop poster)
- [[Paper - Exploiting Priors from 3D Diffusion Models for RGB-Based One-Shot View Planning|Exploiting Priors from 3D Diffusion Models for RGB-Based One-Shot View Planning]] (2024, IROS 2024)
- [[Paper - PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects|PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects]] (2025, IEEE Robotics and Automation Letters)
- [[Paper - VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility|VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility]] (2025, IROS 2025)

## Trends 2021 To 2026
- 2022: active uncertainty estimation moved from explicit maps and touch heuristics into implicit representations and NeRF-style models, while visuo-haptic methods showed that pure vision is often not enough for downstream grasp reliability [S1,S3].
- 2023: the field diversified into continuous-manifold implicit NBV optimization, mapless RGB neural-rendering NBV, interactive poking-based discovery, and affordance-driven grasp-oriented view planning [S4,S5,S6,S7].
- 2024: one-shot planning became more prominent, with view-count prediction, implicit completion, semantic targeting, and diffusion priors all used to reduce online replanning and wasted camera motion [S9,S10,S12,S20].
- 2024 also strengthened manipulation-aware active perception: ActNeRF explicitly chooses between visual observations and reorientation actions instead of treating NBV as a purely visual problem [S11].
- 2025: there is clearer pressure toward operational efficiency and task integration, visible in PB-NBV's computational simplification and VISO-Grasp's direct integration of active views with target grasp execution in clutter [S13,S14].
- [uncertain] No clearly in-scope 2026 preprint tightly matching this subtopic was found in the searched primary-source set by 2026-03-23, so the 2026 part of the trend is currently an absence signal rather than a new paper cluster.

## Research Gaps
- Inference from the source set: the field still lacks a common benchmark that forces a method to trade off view count, path length, scan quality, and downstream reach/grasp success in one protocol [S1,S4,S5,S7,S8,S10,S11,S12,S13,S14].
- A major open problem is unified action selection across view motion, touch, reorientation, and grasp execution; most papers optimize only one or two of these action types together [S1,S6,S7,S11,S14].
- Real-time performance remains an issue for neural-field and diffusion-prior methods, especially when geometry priors must be generated or optimized online [S12].
- Object-scale assumptions remain narrow; transparent, reflective, deformable, articulated, or highly cluttered scenes are still weakly covered by the source set [S1,S3,S4,S5,S8,S10,S11,S12,S13,S14].
- Stopping criteria and uncertainty calibration remain inconsistent across papers, which makes operational guarantees for 'scan enough and then act' systems weak [S3,S5,S10,S11,S20].

## Opportunities For Single Manipulator Systems
- A practical near-term stack for one arm is an eye-in-hand RGB-D or RGB camera with an object-centric uncertainty representation, a PB-NBV- or PRV-style motion-efficient view planner, and an optional single touch or flip action when uncertainty concentrates on support or bottom surfaces [S10,S11,S13].
- If compute is limited, explicit-map planners such as GMC or PB-NBV look more practical than diffusion-heavy or repeatedly retrained neural-field planners, while still matching the user's 'unknown object scan' setting well [S8,S13].
- If the downstream task is grasping in occlusion, ACE-NBV and VISO-Grasp suggest that the view utility should be task-conditioned on grasp affordance or target visibility rather than on uniform reconstruction quality alone [S7,S14].
- If only RGB is available, the Bonn one-shot line is especially promising because it shows a progression from fixed-pattern view-count prediction to object-specific RGB-only planning using diffusion priors [S10,S12].
- Inference from the source set: the most promising single-manipulator direction is a hybrid controller that begins with cheap global planning, then escalates to one or two manipulation actions only when the uncertainty map indicates hidden task-critical surfaces [S10,S11,S13,S14].

## Sources
- [Active Visuo-Haptic Object Shape Completion](https://arxiv.org/abs/2203.09149) | type: arXiv page | notes: Abstract, authors, journal reference, and key results for Act-VH.
- [Active Visuo-Haptic Object Shape Completion](https://research.fi/en/results/publication/0388789222) | type: official publication metadata page | notes: Venue, year, pages, DOI for the RA-L publication.
- [Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields](https://arxiv.org/abs/2209.08409) | type: arXiv page | notes: Robot with arm-held camera, ray-based NeRF uncertainty, accepted RA-L 2022.
- [Active Implicit Object Reconstruction using Uncertainty-guided Next-Best-View Optimization](https://arxiv.org/abs/2303.16739) | type: arXiv page | notes: Continuous-manifold NBV over implicit occupancy fields.
- [NeU-NBV: Next Best View Planning Using Uncertainty Estimation in Image-Based Neural Rendering](https://arxiv.org/abs/2303.01284) | type: arXiv page | notes: Mapless RGB-camera NBV planning with neural-rendering uncertainty.
- [Perceiving Unseen 3D Objects by Poking the Objects](https://zju3dv.github.io/poking_perception/) | type: official project page | notes: ICRA 2023 project page with abstract, code link, and citation block.
- [Affordance-Driven Next-Best-View Planning for Robotic Grasping](https://proceedings.mlr.press/v229/zhang23i.html) | type: official conference proceedings page | notes: CoRL 2023 paper page with abstract and bibliographic metadata.
- [A global generalized maximum coverage-based solution to the non-model-based view planning problem for object reconstruction](https://www.sciencedirect.com/science/article/abs/pii/S1077314222001631) | type: official journal abstract page | notes: CVIU 2023 abstract, highlights, movement-cost trade-off, and code statement.
- [Active Implicit Reconstruction Using One-Shot View Planning](https://arxiv.org/abs/2310.00685) | type: arXiv page | notes: ICRA 2024 one-shot view planning with implicit completion.
- [How Many Views Are Needed to Reconstruct an Unknown Object Using NeRF?](https://www.hrl.uni-bonn.de/publications/2023/how-many-views-are-needed-to-reconstruct-an-unknown-object-using-nerf) | type: official project/publication page | notes: ICRA 2024 PRV paper with authors, DOI, and code link.
- [Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions](https://arxiv.org/abs/2404.01812) | type: arXiv page | notes: ActNeRF abstract and quantitative results for visual plus reorientation actions.
- [Exploiting Priors from 3D Diffusion Models for RGB-Based One-Shot View Planning](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/pan2024iros.pdf) | type: official paper PDF | notes: IROS 2024 PDF with authors, method details, failure case, and code link.
- [PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects](https://pure.bit.edu.cn/en/publications/pb-nbv-efficient-projection-based-next-best-view-planning-framewo) | type: official university publication page | notes: RA-L 2025 abstract, DOI, efficiency claim, and open-source statement.
- [VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility](https://arxiv.org/abs/2503.12609) | type: arXiv page | notes: IROS 2025 paper with real-world success rate and code link.
- [Sicong Pan publications page](https://psc0628.github.io/publications) | type: author publication page | notes: Used to trace the SCVP, global max-flow, and one-shot planning lineage.
- [A surface-based Next-Best-View approach for automated 3D model completion of unknown objects](https://ieeexplore.ieee.org/document/5979947/) | type: official IEEE page | notes: Pre-2021 precursor in explicit unknown-object model completion.
- [An Adaptable, Probabilistic, Next-Best View Algorithm for Reconstruction of Unknown 3-D Objects](https://ieeexplore.ieee.org/document/7835670) | type: official IEEE page | notes: Pre-2021 probabilistic NBV precursor cited by later object-reconstruction work.
- [Active Object Reconstruction Using a Guided View Planner](https://www.ijcai.org/proceedings/2018/689) | type: official conference proceedings page | notes: Pre-2021 learning-based active reconstruction precursor.
- [Sim2Real Viewpoint Invariant Visual Servoing by Recurrent Control](https://research.google/pubs/sim2real-viewpoint-invariant-visual-servoing-by-recurrent-control/) | type: official publication page | notes: Pre-2021 active visual control precursor for unseen-object reaching.
- [STAIR: Semantic-Targeted Active Implicit Reconstruction](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/jin2024iros.pdf) | type: official paper PDF | notes: Used for semantic-targeted active reconstruction, limitations, and influence mapping.
- [NeU-NBV repository](https://github.com/dmar-bonn/neu-nbv) | type: official code repository | notes: Confirms IROS 2023 acceptance, abstract, datasets, and code availability.
