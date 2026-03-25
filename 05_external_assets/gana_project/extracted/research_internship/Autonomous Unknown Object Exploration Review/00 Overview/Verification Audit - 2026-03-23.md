---
title: Verification Audit - 2026-03-23
tags:
  - research-review
  - verification
  - audit
date: 2026-03-23
---

# Verification Audit

## Status

No, the vault should not be read as "100% verified" in the absolute sense.

What is now true:
- the corpus has been re-audited for high-impact numeric claims and recent 2025-2026 papers;
- the shortlist verification pass is now recorded in [[Shortlist Quantitative Verification - 2026-03-23]];
- unsupported wording was downgraded where the primary source did not directly support it;
- several real completeness gaps were added to the corpus, including [[Paper - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]], [[Paper - ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation]], [[Paper - FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation]], [[Paper - CompliantVLA-adaptor: Adapting Vision-Language-Action Model with Compliance Augmentation for Contact-Rich Tasks]], [[Paper - HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing]], [[Paper - TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation]], and [[Paper - TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation]];
- synthesis-level conclusions should be interpreted as evidence-grounded inferences across papers, not as directly quoted claims from any single source.

## Directly Re-checked Primary-Source Claims

- [[Paper - AcTExplore: Active Tactile Exploration on Unknown Objects|AcTExplore: Active Tactile Exploration on Unknown Objects]]
  Source: [AcTExplore primary PDF](https://prg.cs.umd.edu/research/AcTExplore_files/AcTExplore.pdf)
  Verified from primary PDF text: average 95.97% IoU coverage on unseen YCB objects while training on primitive shapes.

- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]]
  Source: [arXiv:2312.13469](https://arxiv.org/abs/2312.13469)
  Verified from primary PDF text: 81% reconstruction F-score, 4.7 mm pose drift, 2.3 mm with known CAD, and up to 94% better tracking under heavy occlusion.

- [[Paper - Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions|ActNeRF]]
  Source: [arXiv:2404.01812](https://arxiv.org/abs/2404.01812)
  Verified from primary PDF text: 14% PSNR gain, 20% F-score gain, and 71% manipulation-success gain.

- [[Paper - Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole]]
  Source: [arXiv:2603.03627](https://arxiv.org/abs/2603.03627)
  Verified from primary PDF text: sub-millimeter simulation pose estimation and 86.7% average real-robot insertion success.

- [[Paper - OpenVLA: An Open-Source Vision-Language-Action Model]]
  Source: [arXiv:2406.09246](https://arxiv.org/abs/2406.09246)
  Verified from primary PDF text: 16.5 percentage-point absolute gain over RT-2-X across 29 evaluation tasks.

- [[Paper - VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility]]
  Source: [arXiv:2503.12609](https://arxiv.org/abs/2503.12609)
  Verified from primary PDF text: 87.5% real-world target-oriented grasping success with the fewest grasp attempts.

- [[Paper - OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model]]
  Source: [arXiv:2506.01196](https://arxiv.org/abs/2506.01196)
  Verified from primary PDF text: over 40% relative improvements on unseen-environment benchmarks while maintaining robust seen-setting performance.

- [[Paper - PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects]]
  Source: [arXiv:2501.10663](https://arxiv.org/abs/2501.10663)
  Verified from primary PDF text: highest point-cloud coverage with low computational time among compared frameworks, plus real-world feasibility, supporting the current qualitative wording.

- [[Paper - Scaling World Model for Hierarchical Manipulation Policies]]
  Source: [arXiv:2602.10983](https://arxiv.org/abs/2602.10983)
  Verified from abstract: novel-scenario performance for the same-structured VLA improves from 14% to 69% with world-model guidance.

- [[Paper - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]]
  Source: [arXiv:2505.22159](https://arxiv.org/abs/2505.22159)
  Verified from abstract: 23.2% average task-success improvement over strong pi0-based baselines and up to 80% success on plug insertion.

- [[Paper - ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation]]
  Source: [arXiv:2603.15169](https://arxiv.org/abs/2603.15169)
  Verified from abstract: 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks, with gains still reaching 35.0% on fragile-object tasks.

- [[Paper - HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing]]
  Source: [arXiv:2603.15257](https://arxiv.org/abs/2603.15257)
  Verified from abstract: 86.7% mean real-world success rate while removing inference-time tactile sensing.

- [[Paper - TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation]]
  Source: [arXiv:2603.12665](https://arxiv.org/abs/2603.12665)
  Verified from abstract: average improvements of 20% on disassembly, 60% on in-box picking, and 2.1x under visual occlusion.

- [[Paper - TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation]]
  Source: [arXiv:2601.20321](https://arxiv.org/abs/2601.20321)
  Verified from abstract: a tactile-force-aligned VLA branch with a TaF-Dataset of over 10 million synchronized tactile observations, force/torque readings, and force maps.

- [[Paper - CompliantVLA-adaptor: Adapting Vision-Language-Action Model with Compliance Augmentation for Contact-Rich Tasks]]
  Source: [arXiv:2603.10572](https://arxiv.org/abs/2603.10572)
  Verified from abstract: overall success on contact-rich tasks improves from 9.86% to 17.29% with compliance augmentation.

- [[Paper - Visuo-Tactile World Models]]
  Source: [arXiv:2602.06001](https://arxiv.org/abs/2602.06001)
  Verified from abstract: 33% better object permanence, 29% better compliance with motion laws, and up to 35% higher zero-shot real-robot success.

- [[Paper - OpenVLA: An Open-Source Vision-Language-Action Model]]
  Source: [OpenVLA project page](https://openvla.github.io/)
  Verified from official project page: OpenVLA is presented as outperforming RT-1-X and Octo, and the page states it also outperforms RT-2-X on the authors' direct multi-platform evaluation while still lagging RT-2-X on harder internet-semantic tasks.

- [[Paper - Gemini Robotics: Bringing AI into the Physical World]]
  Source: [arXiv:2503.20020](https://arxiv.org/abs/2503.20020)
  Verified from abstract: robustness to variations in object types and positions, handling unseen environments, and following diverse open-vocabulary instructions.
  Not retained as settled fact: the earlier "more than doubles performance" wording was removed because I did not yet confirm that number directly from a primary-source results table.

- [[Paper - FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation]]
  Source: [arXiv:2602.02142](https://arxiv.org/abs/2602.02142)
  Verified from abstract: a force-distillation module can provide force-aware reasoning without inference-time force sensing, and the paper states that the distilled force token outperforms direct force sensing in physical experiments.

## Claims Still Treated As Lower Confidence

- Force Policy remains in the synthesis as a local-control anchor, but its current local PDF extraction failed, so I am not yet treating an exact quantitative headline from it as fully re-audited.
- TacLoc is verified as a relevant YCB-evaluated tactile-localization paper, but I am not yet relying on a headline numeric gain from it in the synthesis.
- Several multimodal subtopic numbers outside the shortlist still need a second table-focused pass, especially transparent-object grasping, visuo-tactile world-model, and some benchmark-scale claims.

## Interpretation Rules

- Concrete numbers should only be trusted as "fully re-audited" if they are listed in the section above or in [[Shortlist Quantitative Verification - 2026-03-23]].
- "First", "state of the art", and similar novelty phrases should be read as author claims unless the note explicitly says otherwise.
- The synthesis note is a cross-paper inference layer. It is evidence-grounded, but it is not a direct fact statement from any single primary source.

## Remaining Work

- Re-audit the strongest remaining numeric claims paper-by-paper from result tables, not just abstracts and project pages.
- Search for additional 2025-2026 papers in the multimodal force-aware VLA branch to make sure ForceVLA is not the only missing item that mattered.
- Add claim-status labels directly into the generated report so inference and direct fact are visually separated everywhere, not just in this audit note.
