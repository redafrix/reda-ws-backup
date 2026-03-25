---
title: "Benchmarks datasets evaluation protocols and open research gaps"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23 inclusive; 2026 preprints counted only if publicly available by 2026-03-23."
---

# Benchmarks datasets evaluation protocols and open research gaps

## Scope
This subtopic reviews the public datasets, challenge tasks, benchmark suites, evaluation protocols, and unresolved benchmarking problems used to study autonomous interaction with unknown objects. The boundary includes object-centric active perception, tactile and force-based exploration, open-vocabulary and generalist manipulation benchmarks that explicitly test generalization to new objects or scenes, and sim-to-real evaluation frameworks. It excludes pure navigation benchmarks, static perception-only datasets with no interaction loop, and broad robot-learning corpora that do not materially inform evaluation of unknown-object interaction [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S19,S20,S21,S22].

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The benchmark note now has re-checked anchor metrics for active touch, visuo-tactile perception, and the main VLA benchmark claims, but several benchmark-scale and force-aware suite numbers still need a second pass.

### Re-checked Claims
- AcTExplore: 95.97% average IoU coverage on unseen YCB objects (`verified-primary-pdf`).
- NeuralFeels: 81% F-score, 4.7 mm pose drift, and up to 94% better tracking under heavy occlusion (`verified-primary-pdf`).
- OpenVLA: 16.5 percentage-point gain over RT-2-X across 29 tasks (`verified-primary-pdf`).
- Tactile Gym 2.0: three optical tactile sensors and three physically interactive tasks are supported (`verified-primary-pdf`).

### Still Pending
- ForceVLA2 benchmark gains were not yet table-verified in this pass.
- Some benchmark-scale counts such as environment or task totals remain primary-source summaries rather than table-by-table re-checks.

## Inclusion Criteria
- Primary-source papers, official benchmark pages, official project pages, and official proceedings pages from 2021-03-23 through 2026-03-23 that define or materially shape evaluation of autonomous interaction with previously unseen or poorly modeled objects [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S19,S20,S21,S22,S23,S24].
- Benchmarks that evaluate active sensing, tactile exploration, contact-rich interaction, open-vocabulary object manipulation, or generalizable robot manipulation under object, scene, or embodiment variation [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14].
- Precursors before 2021 were included only when they clearly underpin current benchmark design, shared object sets, tactile simulation, or task-suite construction [S15,S16,S17,S18].

## Exclusion Criteria
- Vision-only object datasets with no robotic action loop, unless they are directly used as benchmark assets for interaction papers.
- Benchmarks centered on mobile navigation or scene exploration rather than manipulating, touching, grasping, opening, or reconstructing unknown objects.
- Purely synthetic evaluation papers with no benchmark contribution, no dataset release, and no reusable protocol.
- Large robot-learning datasets that are useful for pretraining but provide little evidence about unknown-object interaction unless they also define reusable evaluation settings or transfer claims [contrast S6,S8,S9,S12 with broader benchmark-centered sources such as S4,S5,S7,S10,S11,S13].

## Problem Formulations
- Unknown-object shape acquisition: evaluate how efficiently a robot can reconstruct or cover an unseen object's geometry from views, touches, or both, often under a limited interaction budget [S2,S3,S19,S22].
- Target-oriented interaction under occlusion: benchmark whether active sensing leads to better grasping or retrieval of a previously unseen target in clutter or partial visibility [S4,S20,S21].
- Generalizable manipulation across object variation: define task families where policies must transfer across new instances, shapes, materials, and kinematic layouts rather than memorizing a fixed asset set [S5,S7,S10,S13].
- Open-vocabulary mobile manipulation: evaluate an end-to-end loop that must find, grasp, and place novel objects in novel homes from language instructions [S4,S24].
- Lifelong and multitask transfer: benchmark how well a learner reuses declarative and procedural knowledge as tasks accumulate, rather than only measuring single-task success [S7,S13].
- Sim-first proxy evaluation: test whether a simulated benchmark predicts real-world policy ranking and failure modes closely enough to reduce costly physical evaluation [S9,S12].
- Force-aware and tactile interaction: benchmark policies on contact-rich tasks where success depends on local force regulation, tactile interpretation, and safe control around uncertain geometry [S1,S2,S11,S14].

## Sensing Modalities
- RGB and RGB-D cameras remain the dominant benchmark inputs for active view planning, mobile manipulation, and generalist policy suites [S4,S5,S9,S10,S12,S13,S20,S21,S22].
- Optical tactile sensing is central in Tactile Gym 2.0 and AnyTouch 2, where DIGIT-, GelSight-, DigiTac-, and TacTip-style sensors are benchmarked or unified under shared evaluation tasks [S1,S14].
- Force and proprioceptive streams become first-class benchmark inputs in contact-rich work such as ForceVLA2 and in visuo-tactile reconstruction systems such as NeuralFeels [S2,S11].
- Point clouds, segmentation masks, and depth are explicitly supported in ManiSkill2, RLBench-derived styles of evaluation, and many object-centric reconstruction benchmarks [S5,S16,S22].
- Language instructions are integral in HomeRobot OVMM, VLABench, Open X-Embodiment, DROID, MobileManiBench, and RoboCasa365, reflecting the shift toward instruction-conditioned manipulation [S4,S6,S8,S10,S12,S13].
- Multi-view synchronized sensing is increasingly benchmarked, especially in DROID, MobileManiBench, ForceVLA2, and tactile foundation-model datasets [S8,S11,S12,S14].

## Action Space And Robot Setup
- Single-arm tabletop manipulation is still the default physical setup for active reconstruction and tactile exploration benchmarks, including Tactile Gym 2.0, Act-VH, AcTExplore, and many NBV papers [S1,S3,S19,S22].
- Eye-in-hand sensor motion is common when the benchmark measures view efficiency, surface coverage, or contact selection rather than only final task success [S2,S19,S22].
- Mobile manipulation appears as a distinct benchmark regime in HomeRobot OVMM, SIMPLER common setups, MobileManiBench, and RoboCasa365, where navigation and manipulation are evaluated together [S4,S9,S12,S13,S24].
- Benchmark action spaces increasingly mix Cartesian motion, gripper control, controller modes, and force-conditioned actions rather than plain end-effector deltas [S5,S9,S11,S12].
- Modern suites explicitly compare embodiments, for example Open X-Embodiment across 22 robots and MobileManiBench across two mobile platforms with different end-effectors [S6,S12].

## Method Families
- Shared physical-object and object-set benchmarks, such as YCB-backed unseen-object evaluations, anchor reproducible cross-lab comparison for rigid-object interaction [S3,S15,S19].
- Task-suite simulators such as ManiSkill2, LIBERO, RLBench, and RoboCasa365 package many task families under common APIs and reporting rules [S5,S7,S13,S16].
- Large-scale real-robot corpora such as Open X-Embodiment and DROID supply heterogeneous trajectories for pretraining and transfer evaluation across robots, scenes, and skills [S6,S8].
- Proxy-evaluation frameworks such as SIMPLER focus on ranking policies reproducibly in simulation while preserving real-world behavior trends [S9].
- Object-centric active perception benchmarks concentrate on coverage, uncertainty reduction, or downstream grasp gains on unknown objects [S2,S3,S19,S20,S21,S22].
- Tactile and force-aware datasets benchmark dynamic contact understanding, safe controller behavior, and contact-rich manipulation quality [S1,S2,S11,S14].
- Reasoning-heavy VLA benchmarks such as VLABench, MobileManiBench, and RoboCasa365 stress instruction following, long-horizon planning, and generalization under object and scene variation [S10,S12,S13].

## Representative System Pipelines
- Tactile Gym 2.0
  - pipeline: Simulated optical tactile observations from TacTip, DIGIT, or DigiTac -> train RL or imitation policy on edge following, surface following, or pushing -> deploy on a low-cost 4-DoF real robot -> compare transfer performance across sensor types.
  - source ids: S1
- NeuralFeels and FeelSight
  - pipeline: Vision + touch + proprioception -> online neural field and pose graph update -> evaluate reconstruction F-score, pose drift, and occlusion robustness on 70 released experiments -> use the result as a visuo-tactile perception benchmark.
  - source ids: S2
- HomeRobot OVMM
  - pipeline: Language instruction + household scene observation -> navigate to find a novel object -> grasp it -> transport and place it on the target receptacle -> measure end-to-end sim and real success under open-vocabulary household variation.
  - source ids: S4; S24
- SIMPLER
  - pipeline: Take a real-world manipulation policy -> match simulation visuals and control through texture matching and system identification -> run paired sim-and-real evaluations on common setups -> test whether simulation predicts real ranking and failure modes.
  - source ids: S9
- MobileManiBench
  - pipeline: Generate large numbers of mobile-manipulation trajectories in Isaac Sim with synchronized multi-view sensing and rich annotations -> benchmark VLA models across objects, scenes, skills, and embodiments -> analyze data efficiency and generalization before real-world deployment.
  - source ids: S12
- ForceVLA2
  - pipeline: Multi-view images + task prompt + proprioception + force signals -> force-aware VLA predicts action chunks and hybrid force-position behavior -> evaluate across five contact-rich tasks with overload and stability failure modes explicitly considered.
  - source ids: S11

## Evaluation Tasks
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

## Common Metrics
- Task success rate remains the dominant metric across mobile manipulation, contact-rich manipulation, and multitask suites [S4,S5,S7,S9,S10,S11,S12,S13].
- Coverage and geometry metrics such as IoU, F-score, Chamfer-style reconstruction accuracy, or surface coverage are standard in active unknown-object exploration benchmarks [S2,S3,S19,S22].
- Pose drift or pose-estimation error is reported in visuo-tactile object understanding benchmarks such as NeuralFeels [S2].
- Budget-efficiency metrics such as number of views, touches, trajectory length, interaction steps, or planning time are used when the benchmark emphasizes efficient exploration rather than only end-state success [S3,S19,S22].
- Transfer metrics such as forward transfer, robustness to task ordering, and forgetting are central in lifelong suites like LIBERO [S7].
- Generalization metrics include performance on unseen objects, unseen scenes, new embodiments, and varied object instances [S3,S5,S6,S8,S12,S13].
- Simulation-to-real agreement or correlation is itself an evaluation target in SIMPLER, not just a background assumption [S9].
- Safety-oriented metrics such as overload reduction, unstable-contact reduction, or force-tracking quality are becoming more common in force-aware benchmarks [S11].
- Data-centric reporting such as number of trajectories, demonstrations, objects, tasks, scenes, and hours of interaction is heavily used to characterize benchmark scale and diversity [S6,S8,S11,S12,S13,S14].

## Best Reported Capabilities
- AcTExplore reports an average 95.97% IoU coverage on unseen YCB objects despite training on primitive shapes, showing that active tactile reconstruction benchmarks can already support strong unseen-object coverage in controlled settings [S3].
- NeuralFeels reports final reconstruction F-scores of 81%, average pose drift of 4.7 mm, and up to 94% tracking improvement over vision-only under heavy occlusion, demonstrating meaningful benchmark progress for visuo-tactile unknown-object perception [S2].
- Open X-Embodiment shows positive transfer across a 22-robot, 527-skill standardized dataset mixture, which is strong evidence that benchmark scale can improve cross-platform manipulation capability [S6].
- DROID demonstrates that large in-the-wild data diversity can improve policy performance and generalization relative to narrower real-world datasets [S8].
- SIMPLER provides evidence that benchmarked simulation can track real-world policy behavior strongly enough to be useful for scalable model comparison, which is a capability claim about evaluation methodology rather than task performance alone [S9].
- ForceVLA2 reports large gains over pi0 and pi0.5 across five contact-rich tasks while reducing arm overload and unstable contact, indicating that force-aware evaluation suites can expose capability gaps missed by position-only metrics [S11].
- RoboCasa365 scales benchmark diversity to 365 tasks across 2,500 kitchen environments with both human and synthetic demonstrations, enabling systematic studies of what drives generalization in household manipulation [S13].

## Failure Modes And Limitations
- Benchmark fragmentation is still severe: object-centric active exploration papers, tactile suites, generalist policy benchmarks, and mobile-manipulation challenges often report incompatible metrics and stopping rules [S1,S2,S3,S4,S5,S7,S9,S10,S11,S12,S13,S19,S20,S21,S22].
- Real-world evidence is thin relative to simulator scale. HomeRobot explicitly reports only 20% real-world baseline success, underscoring how much harder open-world evaluation remains than simulation-heavy benchmark results suggest [S4].
- Many benchmark suites still over-represent rigid household objects and under-represent deformable, transparent, reflective, slippery, or fragile unknown objects [S1,S3,S5,S13,S14,S18].
- Coverage-style metrics do not necessarily predict downstream utility; a benchmark can reward reconstruction quality without testing whether the robot can then grasp, insert, open, or safely manipulate the object [S2,S3,S19,S22].
- Large data benchmarks such as Open X-Embodiment and DROID broaden scale and diversity, but they do not by themselves solve standardized unknown-object evaluation because tasks, hardware, and annotations remain heterogeneous [S6,S8].
- Reasoning-heavy VLA benchmarks expose brittleness in current models, but many remain simulation-first and do not yet establish strong sim-to-real validity for unknown-object interaction [S10,S12,S13].
- Force and tactile benchmarks are improving quickly, yet dynamic contact data and public force-rich evaluation corpora remain much smaller and less standardized than RGB-centric resources [S1,S2,S11,S14].

## Representative Papers
- [[Paper - Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch|Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch]] (2022, IEEE Robotics and Automation Letters)
- [[Paper - ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills|ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills]] (2023, ICLR 2023)
- [[Paper - HomeRobot: Open-Vocabulary Mobile Manipulation|HomeRobot: Open-Vocabulary Mobile Manipulation]] (2023, arXiv preprint)
- [[Paper - LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning|LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning]] (2023, NeurIPS 2023 Datasets and Benchmarks Track)
- [[Paper - Open X-Embodiment: Robotic Learning Datasets and RT-X Models|Open X-Embodiment: Robotic Learning Datasets and RT-X Models]] (2023, ICRA 2024)
- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation|Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]] (2024, Science Robotics)
- [[Paper - DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset|DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset]] (2024, RSS 2024)
- [[Paper - Evaluating Real-World Robot Manipulation Policies in Simulation|Evaluating Real-World Robot Manipulation Policies in Simulation]] (2024, CoRL 2024 [uncertain])
- [[Paper - VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks|VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks]] (2024, arXiv preprint)
- [[Paper - VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility|VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility]] (2025, IROS 2025)

## Trends 2021 To 2026
- 2021-2022: the field still leaned on shared object sets and simulator-centered task suites, while tactile benchmarking focused on accessible sim-to-real transfer and standardized sensor comparison [S1,S15,S16,S17,S23].
- 2023: benchmark design broadened from single-task success to unified protocols for generalization, transfer, and open-vocabulary interaction, visible in ManiSkill2, HomeRobot OVMM, LIBERO, Open X-Embodiment, and AcTExplore [S3,S4,S5,S6,S7].
- 2024: large real-world datasets and evaluation-proxy frameworks became central, with DROID scaling in-the-wild diversity and SIMPLER explicitly testing whether simulation can stand in for real evaluation [S8,S9].
- Late 2024 to 2025: evaluation pressure shifted toward reasoning, occlusion, and task-conditioned active perception, as seen in VLABench and VISO-Grasp [S10,S21].
- 2026: benchmark scale and modality diversity continue to grow, with MobileManiBench and RoboCasa365 expanding task breadth while AnyTouch 2 and ForceVLA2 push dynamic tactile and force-aware evaluation forward [S11,S12,S13,S14].
- Across the whole period, the strongest trend is from isolated, method-specific evaluation toward benchmark ecosystems that try to measure transfer, reproducibility, and deployment relevance together rather than separately [S5,S6,S7,S8,S9,S10,S12,S13].

## Research Gaps
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

## Opportunities For Single Manipulator Systems
- A practical benchmark target for one arm is a unified tabletop protocol that starts with partial RGB-D observation, allows a small budget of active views and touches, and ends with a grasp, insertion, or placement success metric on unseen rigid objects [S2,S3,S19,S20,S21,S22].
- Single-arm systems can benefit from combining the reproducibility of ManiSkill2-style unified interfaces with YCB-based physical evaluation so that simulation and real tests share object identities and task APIs [S5,S15].
- For low-cost hardware, Tactile Gym 2.0 suggests that one dense optical fingertip plus a wrist camera is enough to build a meaningful benchmark around surface following, guarded contact, and uncertainty reduction [S1].
- For perception-heavy single-arm manipulation, FeelSight and AcTExplore point to a useful benchmark niche: few-touch correction of visual uncertainty on previously unseen objects, measured by both geometry and downstream task success [S2,S3].
- For contact-rich single-arm tasks, ForceVLA2 shows that force-aware metrics should be added early instead of treated as optional diagnostics, especially for wiping, pressing, and assembly-like behaviors [S11].
- Inference from the source set: the best near-term opportunity is a benchmark that is smaller than RoboCasa365 or Open X-Embodiment but more integrated than current object-centric papers, namely a single-arm unknown-object suite with matched sim-real assets, explicit action budgets, force limits, and final-task success labels [S4,S5,S9,S11,S13,S15].

## Sources
- [Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch](https://arxiv.org/abs/2207.10763) | type: arXiv page | notes: Primary source for tactile benchmark scope, task list, sensor list, and sim-to-real framing.
- [Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation](https://arxiv.org/abs/2312.13469) | type: arXiv page | notes: Primary source for FeelSight, 70-experiment evaluation set, F-score, pose drift, and occlusion claims.
- [AcTExplore: Active Tactile Exploration of Unknown Objects](https://arxiv.org/abs/2310.08745) | type: arXiv page | notes: Primary source for unknown-object tactile exploration benchmark details and 95.97% IoU on unseen YCB objects.
- [HomeRobot: Open-Vocabulary Mobile Manipulation](https://arxiv.org/abs/2306.11565) | type: arXiv page | notes: Primary source for OVMM benchmark framing and 20% real-world baseline success.
- [ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659) | type: arXiv page | notes: Primary source for unified evaluation protocol, 20 task families, 2000+ object models, and 4M+ frames.
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) | type: arXiv page | notes: Primary source for 22 robots, 527 skills, standardized data formats, and positive-transfer claims.
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | type: arXiv page | notes: Primary source for four task suites, 130 tasks, forward transfer, and forgetting-related evaluation.
- [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945) | type: arXiv page | notes: Primary source for 76k trajectories, 564 scenes, 84 tasks, and in-the-wild dataset design.
- [Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941) | type: arXiv page | notes: Primary source for SIMPLER and sim-real correlation claims.
- [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://arxiv.org/abs/2412.18194) | type: arXiv page | notes: Primary source for 100 task categories, 2000+ objects, and reasoning-heavy benchmark design.
- [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://arxiv.org/abs/2603.15169) | type: arXiv page | notes: Primary source for ForceVLA2-Dataset, five contact-rich tasks, and force-aware evaluation claims.
- [MobileManiBench: Simplifying Model Verification for Mobile Manipulation](https://arxiv.org/abs/2602.05233) | type: arXiv page | notes: Primary source for 630 objects, 20 categories, 100 scenes, 100+ tasks, and 300K trajectories.
- [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356) | type: arXiv page | notes: Primary source for 365 tasks, 2,500 kitchen environments, and systematic evaluation framing.
- [AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception](https://arxiv.org/abs/2602.09617) | type: arXiv page | notes: Primary source for ToucHD and the shift toward dynamic tactile benchmark datasets.
- [The YCB Object and Model Set: Towards Common Benchmarks for Manipulation Research](https://ieeexplore.ieee.org/document/7251504) | type: official IEEE page | notes: Primary precursor for common object sets and benchmark protocols in manipulation.
- [RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271) | type: arXiv page | notes: Primary precursor for large manipulation task suites with demonstrations and multimodal observations.
- [TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors](https://arxiv.org/abs/2012.08456) | type: arXiv page | notes: Primary precursor for tactile simulation infrastructure.
- [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf) | type: official conference PDF | notes: Primary precursor for PartNet-Mobility-backed articulated-object simulation.
- [Active Visuo-Haptic Object Shape Completion](https://arxiv.org/abs/2203.09149) | type: arXiv page | notes: Primary source for object-centric active visuo-haptic evaluation on unknown objects.
- [Affordance-Driven Next-Best-View Planning for Robotic Grasping](https://proceedings.mlr.press/v229/zhang23i.html) | type: official conference proceedings page | notes: Primary source for task-conditioned active view-planning evaluation toward grasping.
- [VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility](https://arxiv.org/abs/2503.12609) | type: arXiv page | notes: Primary source for active-view-plus-grasp benchmark claims under clutter and invisibility.
- [PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects](https://pure.bit.edu.cn/en/publications/pb-nbv-efficient-projection-based-next-best-view-planning-framewo) | type: official university publication page | notes: Primary source for practical, efficiency-oriented unknown-object NBV evaluation.
- [BEHAVIOR: Benchmark for Everyday Household Activities in Virtual, Interactive, and Ecological Environments](https://arxiv.org/abs/2108.03332) | type: arXiv page | notes: Primary precursor for realistic household activity definitions and evaluation.
- [NeurIPS 2023 HomeRobot: Open Vocabulary Mobile Manipulation (OVMM) Challenge](https://aihabitat.org/challenge/2023_homerobot_ovmm/) | type: official challenge page | notes: Official benchmark page for OVMM challenge framing and evaluation context.
