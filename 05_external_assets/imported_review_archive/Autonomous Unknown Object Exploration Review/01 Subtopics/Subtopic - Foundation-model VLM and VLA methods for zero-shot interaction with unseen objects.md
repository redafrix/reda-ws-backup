---
title: "Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects"
tags:
  - research-review
  - subtopic
  - unknown-object-exploration
date: 2026-03-23
time_window: "2021-03-23 to 2026-03-23 inclusive; 2026 preprints counted only if publicly available by 2026-03-23."
---

# Foundation-model VLM and VLA methods for zero-shot interaction with unseen objects

## Scope
This subtopic covers robot manipulation methods that use large pretrained vision-language models, vision-language-action models, diffusion or flow-based generalist policies, or closely related hierarchical VLM-to-control stacks to reason about and physically interact with previously unseen objects with little or no object-specific supervision. The boundary includes end-to-end VLAs, cross-embodiment generalist policies, and hierarchical systems that use foundation-model semantics or spatial reasoning to guide manipulation; it excludes classical task-specific grasping or imitation systems without foundation-model pretraining, pure perception-only VLMs, and navigation-only agents without substantive object interaction [S1,S2,S4,S5,S6,S7,S12,S13,S16,S18,S19,S21,S22,S23,S24,S25].

## Claim Status
> [!info] Verification state
> Overall status: `partial-quantitative-audit`
> Summary: The most important foundation-model numbers affecting the synthesis are now re-checked, and the 2026 contact-aware VLA branch is materially more complete than before, but several long-tail benchmark breakdowns remain pending.

### Re-checked Claims
- OpenVLA: 16.5 percentage-point gain over RT-2-X across 29 evaluation tasks (`verified-primary-pdf`).
- OG-VLA: over 40% relative improvement on unseen-environment benchmarks (`verified-primary-pdf`).
- VISTA: novel-scenario performance improves from 14% to 69% with world-model guidance (`verified-primary-abstract`).
- ForceVLA, ForceVLA2, HapticVLA, TacVLA, TaF-VLA, and CompliantVLA-adaptor headline numbers were re-checked from the primary abstracts (`verified-primary-abstract`).

### Downgraded Claims
- Gemini Robotics keeps only abstract-supported qualitative robustness wording; the earlier stronger quantitative comparison was removed.

### Still Pending
- FD-VLA is now included as a real missing 2026 paper, but its main contribution is currently treated as abstract-backed qualitative evidence rather than a single headline number.
- Some pi0, pi0.5, and embodiment-specific benchmark breakdowns remain summary-level rather than table-level re-checks.
- Novelty phrases such as 'state of the art' remain author claims unless explicitly re-audited.

## Inclusion Criteria
- Primary-source papers or official project pages published in the requested window that report robot manipulation on unseen objects, unseen scenes, unseen instructions, unseen backgrounds, or new robot embodiments using foundation-model-style vision-language or vision-language-action methods [S2,S5,S7,S12,S13,S16,S17,S18,S19,S20,S21,S22,S23,S24,S25].
- Methods were included if they either act end-to-end as a VLA or use a foundation-model planner or spatial reasoner to generate robot-relevant affordances, trajectories, subgoals, or low-level action guidance for object interaction [S2,S4,S5,S6,S18,S19,S21,S22,S23].
- Cross-embodiment pretraining, data-scaling, and open-source generalist policy work were included when the paper directly supports rapid adaptation or zero-shot transfer to new objects or environments [S7,S9,S12,S13,S16,S18,S19,S20,S24,S25].

## Exclusion Criteria
- Pure vision-language perception papers that detect or describe unseen objects but do not close the loop to robot action.
- Classical manipulation systems that generalize to novel instances but do not substantially rely on pretrained VLM/VLA/foundation-model components, except when cited as historical precursors before 2021 [S26,S27].
- Navigation-only embodied agents, whole-body humanoid locomotion papers, or language-only planning papers without substantive manipulator interaction.
- Papers whose evidence is limited to in-distribution imitation without explicit claims or experiments on unseen objects, scenes, instructions, or embodiments.

## Problem Formulations
- Open-vocabulary tabletop manipulation: given RGB observations and a natural-language command, the robot must identify and manipulate a target object that was not explicitly modeled per instance, often under distractors or changed layouts [S1,S5,S12,S13,S20].
- Long-horizon household or mobile-manipulation tasks in novel homes or rooms: the policy must chain subskills such as picking, placing, opening, wiping, or sorting in environments absent from training [S2,S17,S18,S19].
- Cross-embodiment generalist pretraining plus rapid adaptation: a large policy is pretrained on heterogeneous robot data, then transferred to a new arm, camera arrangement, or action space with little task-specific data [S7,S11,S12,S13,S16,S19,S24,S25].
- Zero-shot or few-shot trajectory synthesis from foundation-model reasoning: a VLM or LLM predicts affordances, 3D paths, goal images, or value maps that a lower-level controller follows to manipulate previously unseen objects [S6,S21,S22,S23].
- 3D-aware VLA control: multi-view RGB-D or spatial encodings are used to improve robustness to unseen object poses, layouts, and backgrounds while retaining language grounding [S20,S21,S22,S23].
- Dexterous or bimanual generalist control: foundation policies extend beyond single-arm pick-and-place to box assembly, laundry folding, bag packing, and other high-dimensional tasks while preserving transfer to unseen objects or scenes [S16,S17,S18,S19,S25].

## Sensing Modalities
- RGB vision is the dominant modality, typically from one or more external cameras and often an egocentric or wrist camera; this is the standard input route for RT-1, RT-2, Octo, OpenVLA, pi0, pi0.5, Gemini Robotics, and most spatial VLA variants [S3,S5,S12,S13,S16,S18,S19,S20].
- Natural-language task instructions are universal across the subtopic and often provide the only explicit object specification, enabling open-vocabulary or relational object selection [S1,S2,S5,S6,S12,S17,S18,S19,S20,S21,S22,S23,S25].
- Robot proprioception and state tokens are common in embodied multimodal models and generalist policies, especially PaLM-E, pi0, pi0.5, Gemini Robotics, and RDT-1B [S4,S16,S18,S19,S25].
- RGB-D, point clouds, or multi-view spatial observations become more important in the 2025-2026 branch, particularly OG-VLA, GeneralVLA, VISTA, and Gemini Robotics-ER-style embodied reasoning [S19,S21,S22,S23].
- Goal images are still used in the generalist-policy lineage, especially Octo, as an alternative or complement to language prompts [S12].
- Inference from the source set: tactile and force sensing are not a central ingredient in the main zero-shot unseen-object foundation-model literature through 2026-03-23; most evidence is still vision-language dominant [S5,S12,S13,S16,S17,S18,S19,S20,S21,S22,S23,S25].

## Action Space And Robot Setup
- Most systems operate a single 6- or 7-DoF arm with a parallel-jaw gripper in tabletop or bench-top scenes, outputting end-effector translation, rotation, and gripper commands either as discrete tokens or short continuous action chunks [S1,S3,S5,S12,S13,S20,S21].
- Cross-embodiment work broadens this to multiple arm types and camera layouts; Open X-Embodiment spans 22 embodiments, Octo evaluates across 9 platforms, and OpenVLA supports multiple robots out of the box before parameter-efficient adaptation [S7,S12,S13,S14].
- Mobile manipulators appear in SayCan, pi0, pi0.5, and Gemini Robotics, where language-conditioned policies must combine arm motion with navigation or repositioning to complete household tasks [S2,S16,S17,S18,S19].
- Bimanual and highly dexterous setups become prominent in the pi0, Gemini Robotics, and RDT-1B line, which explicitly target dual-arm manipulation and complex contact-rich object handling [S16,S18,S19,S25].
- Hierarchical methods often do not emit motor torques directly; instead they predict language options, 3D paths, canonical goal images, or value maps that a lower-level controller or policy executes [S2,S6,S21,S22,S23].

## Method Families
- Semantic-plus-spatial grounding policies: CLIPort combines CLIP semantics with Transporter-style spatial reasoning, while SpatialVLA and OG-VLA inject stronger spatial encodings or canonical 3D views into the VLA stack [S1,S20,S21].
- Planner-executor foundation stacks: SayCan, VoxPoser, GeneralVLA, and VISTA use a high-level LLM/VLM or world model to produce feasible skill sequences, value maps, or goal images that lower-level control follows [S2,S6,S22,S23].
- End-to-end tokenized VLAs: RT-2, RT-2-X, and OpenVLA adapt a large VLM or VLM-like backbone to output robot actions directly, usually as discrete action tokens [S5,S7,S13,S14].
- Open-source generalist policy pretraining: Open X-Embodiment, Octo, and OpenVLA emphasize heterogeneous robot data mixtures and practical fine-tuning to new tasks, sensors, and embodiments [S7,S12,S13,S14].
- Diffusion or flow-based action generation: CogACT uses a diffusion action transformer, pi0 and pi0.5 use flow matching, and RDT-1B extends diffusion-based foundation modeling to bimanual manipulation [S16,S17,S18,S25].
- Self-improving or rapidly adaptable foundation agents: RoboCat and Gemini Robotics emphasize fast adaptation to novel tasks and embodiments and, in RoboCat's case, self-generated data for additional training rounds [S11,S19].

## Representative System Pipelines
- RT-2 and OpenVLA pipeline: start from a pretrained VLM backbone, add robot observation and language tokens, discretize actions into tokens, decode tokens back to Cartesian or gripper actions, and close the loop online on the robot [S5,S13,S14].
- Open X plus Octo pipeline: aggregate cross-lab robot trajectories into a standardized data mixture, pretrain a transformer policy across embodiments, then fine-tune to a new platform with language or goal-image conditioning and modest compute [S7,S12].
- pi0 and pi0.5 pipeline: keep a pretrained VLM backbone for semantics, attach a continuous generative action expert based on flow matching, co-train on heterogeneous robot and semantic data, then optionally specialize for long-horizon tasks in new homes [S16,S18].
- CogACT and RDT-1B pipeline: use a VLM or multimodal transformer for perception and task context, then hand off to a diffusion-based action module that models multi-step continuous actions and better handles multimodal manipulation outcomes [S17,S25].
- VoxPoser, GeneralVLA, VISTA, and OG-VLA pipeline: use a foundation model to infer affordances, spatial constraints, 3D paths, or visual subgoals over the current scene, then execute with a lower-level policy or planner that updates after each observation [S6,S21,S22,S23].

## Evaluation Tasks
- Single-step pick-and-place, reorientation, and relational placement tasks on unseen household objects or unseen object combinations [S1,S5,S12,S13,S20,S21].
- Language-conditioned multi-object tasks with distractors, unseen backgrounds, changed object sizes or shapes, and unseen target-object categories [S5,S13,S14,S15,S20].
- Long-horizon chores such as table cleaning, room cleanup, drawer manipulation, sorting, and multi-stage household tasks in previously unseen homes or scenes [S2,S17,S18,S19].
- Dexterous or bimanual tasks such as folding laundry, assembling boxes, bag packing, and other high-dimensional manipulation routines [S16,S18,S19,S25].
- Cross-robot or cross-setup transfer tasks in which a pretrained policy is adapted to a new arm, camera arrangement, or embodiment with a few demonstrations or short fine-tuning [S11,S12,S13,S19,S20,S25].
- Benchmark-style stress tests that vary camera pose, lighting, confounding objects, unseen objects, and instruction phrasing to probe failure under OOD shifts [S15,S21,S23].

## Common Metrics
- Episode or task success rate is the dominant metric, usually averaged over many tasks, scenes, or robot embodiments [S5,S12,S13,S15,S16,S17,S18,S19,S20,S21,S23,S24,S25].
- OOD generalization success is frequently broken down by novel object, novel background, novel instruction, novel pose, or novel environment conditions [S5,S13,S15,S18,S19,S20,S21,S23,S25].
- Cross-embodiment adaptation is often quantified by post-fine-tuning success rate versus the number of demonstrations, hours of training, or parameter-efficiency method used [S11,S12,S13,S19,S20,S24,S25].
- Some papers report relative or absolute gains over baselines such as RT-2-X, Octo, Diffusion Policy, or VoxPoser rather than only raw success [S13,S17,S19,S21,S22,S23].
- A smaller but important secondary set of metrics includes training throughput, GPU memory, inference efficiency, or evaluation latency, reflecting the engineering cost of deploying large VLAs [S13,S24].

## Best Reported Capabilities
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

## Failure Modes And Limitations
- Even strong VLAs remain brittle under systematic OOD shifts in lighting, camera viewpoint, confounding objects, unseen objects, and instruction mutations; VLATest makes this limitation explicit across seven representative models [S15].
- OpenVLA's own project page shows that open models still lag larger co-trained systems such as RT-2-X on hard semantic tasks that require internet knowledge not preserved during pure robot-action fine-tuning [S14].
- Most evaluations still center on rigid household objects in controlled labs or curated homes, so performance on transparent, reflective, deformable, articulated, or strongly contact-rich objects remains weakly evidenced [S13,S15,S18,S19,S21,S25].
- Purely 2D image-based VLAs struggle with spatial invariance and camera-pose sensitivity, which directly motivated SpatialVLA, OG-VLA, and other 3D-aware extensions [S20,S21].
- Large diffusion- or flow-based policies improve dexterity but raise deployment costs in data, compute, and latency, which is why later work emphasizes efficient training and action representations [S16,S18,S24,S25].
- Cross-embodiment transfer still usually needs some adaptation data or calibration of action spaces, so truly plug-and-play zero-shot deployment on a novel robot is not yet routine [S7,S12,S13,S19,S24].

## Representative Papers
- [[Paper - CLIPort: What and Where Pathways for Robotic Manipulation|CLIPort: What and Where Pathways for Robotic Manipulation]] (2021, Conference on Robot Learning)
- [[Paper - Do As I Can, Not As I Say: Grounding Language in Robotic Affordances|Do As I Can, Not As I Say: Grounding Language in Robotic Affordances]] (2022, arXiv preprint / SayCan project)
- [[Paper - RT-1: Robotics Transformer for Real-World Control at Scale|RT-1: Robotics Transformer for Real-World Control at Scale]] (2023, Robotics: Science and Systems)
- [[Paper - PaLM-E: An Embodied Multimodal Language Model|PaLM-E: An Embodied Multimodal Language Model]] (2023, arXiv preprint)
- [[Paper - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control|RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control]] (2023, Conference on Robot Learning)
- [[Paper - Open X-Embodiment: Robotic Learning Datasets and RT-X Models|Open X-Embodiment: Robotic Learning Datasets and RT-X Models]] (2023, ICRA 2024 / arXiv)
- [[Paper - RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation|RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation]] (2023, Transactions on Machine Learning Research)
- [[Paper - Octo: An Open-Source Generalist Robot Policy|Octo: An Open-Source Generalist Robot Policy]] (2024, Robotics: Science and Systems)
- [[Paper - OpenVLA: An Open-Source Vision-Language-Action Model|OpenVLA: An Open-Source Vision-Language-Action Model]] (2024, arXiv preprint)
- [[Paper - $\pi_0$: A Vision-Language-Action Flow Model for General Robot Control|$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control]] (2024, RSS 2025 / arXiv)
- [[Paper - CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation|CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation]] (2024, arXiv preprint)
- [[Paper - $\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization|$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization]] (2025, preprint / technical report)
- [[Paper - Gemini Robotics: Bringing AI into the Physical World|Gemini Robotics: Bringing AI into the Physical World]] (2025, arXiv technical report)
- [[Paper - OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model|OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model]] (2025, ICRA 2026 submission / arXiv)
- [[Paper - Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation|Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation]] (2025, arXiv preprint)
- [[Paper - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation|ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (2025, NeurIPS 2025 / arXiv)

## Trends 2021 To 2026
- 2021-2022 emphasized semantic grounding on top of task-specific manipulation backbones, with CLIPort and SayCan combining pretrained language or vision-language priors with more classical manipulation structures [S1,S2].
- 2023 shifted the center of gravity toward embodied multimodal transformers and true VLAs: PaLM-E, RT-2, Open X-Embodiment, and RoboCat all argue that large-scale pretraining and heterogeneous data are the path to generalization [S4,S5,S7,S11].
- 2024 made the area operationally accessible through open-source generalist policies and datasets such as Octo, OpenVLA, DROID, and benchmark-style evaluation frameworks such as VLATest [S9,S12,S13,S15].
- Late 2024 through 2025 saw a move from discrete action tokenization toward continuous generative action heads and more dexterous embodiments, especially in CogACT, pi0, pi0.5, Gemini Robotics, and RDT-1B [S16,S17,S18,S19,S25].
- 2025-2026 increasingly treats spatial understanding as the bottleneck, producing SpatialVLA, OG-VLA, GeneralVLA, and VISTA, all of which add 3D structure, visual subgoals, or explicit trajectory intermediates to improve OOD manipulation on unseen objects [S20,S21,S22,S23].
- A parallel 2025-2026 branch treats contact awareness as the next major frontier inside VLAs themselves: ForceVLA, FD-VLA, ForceVLA2, HapticVLA, TacVLA, TaF-VLA, and CompliantVLA-adaptor all add force, tactile, or compliance structure directly into the policy stack rather than relegating it entirely to a downstream controller.
- Across the whole window, the field moves from closed internal systems toward partially open ecosystems, but robustness lags behind capability demos: open checkpoints and benchmarks improved substantially, yet dependable zero-shot operation in truly messy environments is still unresolved [S7,S12,S13,S15,S18,S19,S24].

## Research Gaps
- Robustness under realistic OOD shift remains the main gap: current VLAs still degrade under clutter, camera changes, lighting shifts, instruction variation, and harder unseen objects [S15].
- 3D spatial grounding is still not solved by default 2D VLAs, which is why multiple 2025-2026 papers add point clouds, orthographic views, explicit action grids, or visual subgoals [S20,S21,S22,S23].
- Open-world semantics and open-world control do not align perfectly: OpenVLA, for example, is competitive on robot-specific OOD tasks but weaker than RT-2-X on internet-knowledge-heavy semantic generalization [S14].
- Data efficiency is still poor for the strongest models; many results depend on enormous cross-embodiment datasets or expensive curation, even when downstream adaptation is data-efficient [S7,S9,S18,S19,S24].
- The literature under-covers tactile, force, deformable-object, and transparent-object interaction, which means the present zero-shot story is strongest for vision-dominant rigid-object manipulation [S13,S18,S19,S25].
- Evaluation standards remain fragmented: benchmark diversity is improving, but many papers still publish custom task suites that make direct comparison difficult [S15,S21,S24].

## Opportunities For Single Manipulator Systems
- A single-arm system with one static RGB camera plus a wrist camera is now a realistic target platform for open-source VLAs such as OpenVLA and Octo, especially when paired with DROID, BridgeData V2, or LIBERO-style fine-tuning [S8,S9,S10,S12,S13,S14].
- For tasks involving unseen objects and language grounding, OpenVLA is a strong default backbone because it is open, supports LoRA fine-tuning on consumer hardware, and performs well in multi-object, multi-instruction settings [S13,S14].
- If the application is especially sensitive to object pose variation or scene geometry, 3D-aware add-ons from SpatialVLA or OG-VLA are promising because they directly target spatial invariance rather than relying on 2D image tokens alone [S20,S21].
- For longer-horizon tasks, the most promising architecture for a single manipulator is likely hierarchical: pair a high-level VLM or world model that reasons about subgoals with a lower-level VLA that handles short-horizon control, following the SayCan, VoxPoser, GeneralVLA, and VISTA pattern [S2,S6,S22,S23].
- Inference from the source set: the best near-term path is not to seek full zero-shot autonomy on arbitrary objects, but to combine broad pretrained semantics with modest task-domain adaptation and stronger 3D perception on a simple single-arm platform [S13,S15,S20,S21,S23].

## Sources
- [CLIPort: What and Where Pathways for Robotic Manipulation](https://arxiv.org/abs/2109.12098) | type: arXiv abstract page | year: 2021 | notes: Primary source for CLIP-based semantic grounding with Transporter-style spatial manipulation.
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | type: arXiv abstract page | year: 2022 | notes: Primary source for the SayCan hierarchical grounding formulation.
- [RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817) | type: arXiv abstract page | year: 2022 | notes: Primary source for large-scale real-robot transformer control and scaling claims.
- [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378) | type: arXiv abstract page | year: 2023 | notes: Primary source for embodied multimodal language modeling and positive-transfer claims.
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | type: arXiv abstract page | year: 2023 | notes: Primary source for the VLA formulation, tokenized actions, novel-object generalization, and semantic reasoning claims.
- [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973) | type: arXiv abstract page | year: 2023 | notes: Primary source for zero-shot trajectory synthesis through VLM-grounded 3D value maps.
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) | type: arXiv abstract page | year: 2023 | notes: Primary source for cross-embodiment dataset scale, RT-X, and positive-transfer claims.
- [BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952) | type: arXiv abstract page | year: 2023 | notes: Primary source for BridgeData V2 size, diversity, and open-vocabulary multi-task suitability.
- [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945) | type: arXiv abstract page | year: 2024 | notes: Primary source for DROID dataset size, scene diversity, and task count.
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | type: arXiv abstract page | year: 2023 | notes: Primary source for the LIBERO benchmark and its 130-task lifelong-learning suites.
- [RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation](https://deepmind.google/research/publications/35829/) | type: official publication page | year: 2023 | notes: Primary source for self-improvement and 100-1000 example adaptation claims.
- [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) | type: arXiv abstract page | year: 2024 | notes: Primary source for 800k-trajectory Open-X pretraining and rapid adaptation to new setups.
- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | type: arXiv abstract page | year: 2024 | notes: Primary source for OpenVLA architecture, benchmark numbers, and fine-tuning claims.
- [OpenVLA project page](https://openvla.github.io/) | type: official project page | year: 2024 | notes: Primary source for detailed OOD task breakdowns, videos, and open-source release details.
- [VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2409.12894) | type: arXiv abstract page | year: 2024 | notes: Primary source for robustness findings under confounders, unseen objects, camera pose, lighting, and instruction mutations.
- [$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) | type: arXiv abstract page | year: 2024 | notes: Primary source for flow-matching continuous generalist control across multiple embodiments.
- [CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation](https://arxiv.org/abs/2411.19650) | type: arXiv abstract page | year: 2024 | notes: Primary source for the diffusion action transformer and unseen-object/background generalization claims.
- [$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | type: paper PDF | year: 2025 | notes: Primary source for heterogeneous co-training and long-horizon cleanup in entirely new homes.
- [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020) | type: arXiv abstract page | year: 2025 | notes: Primary source for generality, dexterity, unseen-object robustness, and new-embodiment adaptation claims.
- [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](https://spatialvla.github.io/) | type: official project page | year: 2025 | notes: Primary source for zero-shot spatial evaluation summaries, 3D position encoding, and adaptation claims.
- [OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model](https://arxiv.org/abs/2506.01196) | type: arXiv abstract page | year: 2025 | notes: Primary source for canonical orthographic-view generation and unseen-environment benchmark gains.
- [Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation](https://arxiv.org/abs/2506.23919) | type: arXiv abstract page | year: 2025 | notes: Primary source for the object-centric world-model branch that generates goal images, derives target object pose, and uses reflection-through-synthesis for zero-shot manipulation.
- [GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning](https://arxiv.org/abs/2602.04315) | type: arXiv abstract page | year: 2026 | notes: Primary source for hierarchical zero-shot manipulation with affordance segmentation and 3D trajectory planning.
- [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/abs/2602.10983) | type: arXiv abstract page | year: 2026 | notes: Primary source for world-model-generated goal images and reported OOD gains from 14% to 69%.
- [A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692) | type: arXiv abstract page | year: 2026 | notes: Primary source for LingBot-VLA scale, efficiency, and open benchmark positioning.
- [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864) | type: arXiv abstract page | year: 2024 | notes: Primary source for bimanual diffusion-based foundation modeling, unseen-object generalization, and few-shot adaptation.
- [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://arxiv.org/abs/2010.14406) | type: arXiv abstract page | year: 2020 | notes: Foundational precursor for spatially structured visual manipulation policies.
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | type: arXiv abstract page | year: 2021 | notes: Foundational precursor for zero-shot vision-language semantics used throughout the later VLM/VLA literature.
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://arxiv.org/abs/2505.22159) | type: arXiv abstract page | year: 2025 | notes: Primary source for the force-aware VLA branch, including the 23.2% average gain over pi0-based baselines, the five-task ForceVLA-Data dataset, and up to 80% plug-insertion success.
- [FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2602.02142) | type: arXiv abstract page | year: 2026 | notes: Primary source for force-token distillation, inference without physical force sensors, and the claim that distilled force can outperform direct force sensing in physical experiments.
- [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://arxiv.org/abs/2603.15169) | type: arXiv abstract page | year: 2026 | notes: Primary source for hybrid force-position VLA outputs and the reported 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks.
- [CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation](https://arxiv.org/abs/2601.15541) | type: arXiv abstract page | year: 2026 | notes: Primary source for compliance augmentation of VLAs and the reported overall success-rate increase from 9.86% to 17.29% on contact-rich tasks.
- [HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing](https://arxiv.org/abs/2603.15257) | type: arXiv abstract page | year: 2026 | notes: Primary source for tactile-distilled VLA control without inference-time tactile sensing, including the reported 86.7% mean real-world success rate.
- [TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation](https://arxiv.org/abs/2603.12665) | type: arXiv abstract page | year: 2026 | notes: Primary source for contact-aware tactile-token gating in VLAs and the reported 20%, 60%, and 2.1x gains on contact-rich manipulation settings.
- [TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321) | type: arXiv abstract page | year: 2026 | notes: Primary source for tactile-force alignment, TaF-Dataset with over 10 million synchronized observations, and force-grounded tactile tokenization.
