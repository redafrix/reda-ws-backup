---
title: Shortlist Quantitative Verification - 2026-03-23
tags:
  - research-review
  - verification
  - shortlist
date: 2026-03-23
---

# Shortlist Quantitative Verification

## Scope

This note records the status of the quantitative claims that most directly affect the shortlist and synthesis.

Status labels used here:
- `verified-primary-pdf`: the number or comparison was re-checked from primary PDF text, either from a local PDF-to-text extraction or from the primary PDF rendered in-browser.
- `verified-primary-abstract`: the number was re-checked from the paper's primary abstract page, but I have not yet tied it to a local results table in this vault.
- `qualitative-only`: the paper remains important for the shortlist or synthesis, but I am not currently relying on a numeric claim from it here.
- `downgraded`: earlier stronger wording was removed because the current audit did not support keeping it as a settled quantitative fact.

## Verified From Primary PDF Text

- [[Paper - Active Visuo-Haptic Object Shape Completion]]
  Status: `verified-primary-pdf`
  Verified claim: the paper reports that average real-robot grasp success after five touches rises from 30% to 80% for Act-VH, while the strongest reconstruction baseline remains lower.
  Use in vault: the synthesis and active-visual subtopic only retain the weaker and safer conclusion that active visuo-haptic completion materially improves downstream grasping on novel objects.

- [[Paper - AcTExplore: Active Tactile Exploration on Unknown Objects|AcTExplore: Active Tactile Exploration on Unknown Objects]]
  Status: `verified-primary-pdf`
  Verified claim: the paper reports an average 95.97% IoU coverage on unseen YCB objects while training on primitive shapes.
  Use in vault: retained as one of the strongest active-touch reconstruction numbers in the review.

- [[Paper - Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation]]
  Status: `verified-primary-pdf`
  Verified claims: 81% final reconstruction F-score, 4.7 mm average pose drift, 2.3 mm pose drift with known CAD models, and up to 94% better tracking than vision-only under heavy occlusion.
  Use in vault: retained without weakening.

- [[Paper - Uncertainty-aware Active Learning of NeRF-based Object Models for Robot Manipulators using Visual and Re-orientation Actions|ActNeRF]]
  Status: `verified-primary-pdf`
  Verified claims: 14% higher PSNR, 20% higher F-score, and 71% higher manipulation success relative to its compared method set.
  Use in vault: retained without weakening.

- [[Paper - VISO-Grasp: Vision-Language Informed Spatial Object-centric 6-DoF Active View Planning and Grasping in Clutter and Invisibility]]
  Status: `verified-primary-pdf`
  Verified claim: 87.5% target-oriented grasping success with the fewest grasp attempts in the reported real-world comparison.
  Use in vault: retained without weakening.

- [[Paper - Touch2Insert: Zero-Shot Peg Insertion by Touching Intersections of Peg and Hole]]
  Status: `verified-primary-pdf`
  Verified claims: sub-millimeter pose estimation accuracy in simulation across tested connectors and 86.7% average real-robot insertion success.
  Use in vault: retained without weakening.

- [[Paper - PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects]]
  Status: `verified-primary-pdf`
  Verified claim: the abstract and body text support the current qualitative wording that PB-NBV achieves the highest point-cloud coverage with low computational time among its compared frameworks, plus real-world feasibility.
  Use in vault: deliberately kept qualitative because the current synthesis does not need a single scalar headline number from PB-NBV.

- [[Paper - OpenVLA: An Open-Source Vision-Language-Action Model]]
  Status: `verified-primary-pdf`
  Verified claim: 16.5 percentage-point absolute success-rate gain over RT-2-X across 29 evaluation tasks.
  Use in vault: retained without weakening.

- [[Paper - OG-VLA: Orthographic Image Generation for 3D-Aware Vision-Language Action Model]]
  Status: `verified-primary-pdf`
  Verified claim: over 40% relative improvement on unseen-environment benchmarks while maintaining strong seen-setting performance.
  Use in vault: retained without weakening.

- [[Paper - Tactile Gym 2.0: Sim-to-Real Deep Reinforcement Learning for Comparing Low-Cost High-Resolution Robot Touch]]
  Status: `verified-primary-pdf`
  Verified claim: the benchmark extends to three optical tactile sensors and three physically interactive tasks: object pushing, edge following, and surface following.
  Use in vault: retained as benchmark framing, not as a SOTA performance claim.

## Verified From Primary Abstract Pages In The 2025-2026 Sweep

- [[Paper - Scaling World Model for Hierarchical Manipulation Policies]]
  Status: `verified-primary-abstract`
  Verified claim: world-model guidance improves the reported same-structured VLA's novel-scenario performance from 14% to 69%.

- [[Paper - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]]
  Status: `verified-primary-abstract`
  Verified claims: 23.2% average task-success improvement over strong pi0-based baselines and up to 80% success on plug insertion.

- [[Paper - ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation]]
  Status: `verified-primary-abstract`
  Verified claims: 48.0% average gains over pi0 and pi0.5 across five contact-rich tasks, with gains still reaching 35.0% on fragile-object behaviors.

- [[Paper - HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing]]
  Status: `verified-primary-abstract`
  Verified claim: 86.7% mean real-world success rate without inference-time tactile sensing.

- [[Paper - TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation]]
  Status: `verified-primary-abstract`
  Verified claims: average gains of 20% on disassembly, 60% on in-box picking, and 2.1x under visual occlusion.

- [[Paper - TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation]]
  Status: `verified-primary-abstract`
  Verified claim: TaF-Dataset contains over 10 million synchronized tactile observations, force-torque readings, and force maps.

- [[Paper - CompliantVLA-adaptor: Adapting Vision-Language-Action Model with Compliance Augmentation for Contact-Rich Tasks]]
  Status: `verified-primary-abstract`
  Verified claim: compliance augmentation improves overall success on contact-rich tasks from 9.86% to 17.29%.

- [[Paper - Visuo-Tactile World Models]]
  Status: `verified-primary-abstract`
  Verified claims: 33% better object permanence, 29% better compliance with motion laws, and up to 35% higher zero-shot real-robot success than vision-only alternatives.

- [[Paper - TacLoc: Global Tactile Localization on Objects from a Registration Perspective]]
  Status: `verified-primary-abstract`
  Verified claim: the paper is evaluated on the YCB dataset and demonstrated on real objects with two visual-tactile sensors.
  Use in vault: retained as a qualitative localization paper; no strong numeric headline from TacLoc is currently relied on in the synthesis.

## Downgraded Or Kept Qualitative

- [[Paper - Gemini Robotics: Bringing AI into the Physical World]]
  Status: `downgraded`
  Current state: the earlier stronger comparative wording was removed. The vault now retains only the abstract-supported qualitative claim that the system is robust to object variation, unseen environments, and diverse open-vocabulary instructions.

- [[Paper - Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation]]
  Status: `qualitative-only`
  Current state: the paper remains important to the synthesis as a local-control anchor, but the current local PDF extraction failed, so I am not treating an exact quantitative comparison from this paper as fully re-audited yet.

- [[Paper - FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation]]
  Status: `qualitative-only`
  Current state: the paper was added in the completeness sweep because it is a real missing 2026 branch, but the present audit uses it as abstract-backed qualitative evidence rather than as a settled headline number.

## Interpretation

- Claims listed as `verified-primary-pdf` are now strong enough to be treated as re-audited quantitative evidence in the vault.
- Claims listed as `verified-primary-abstract` are stronger than memory-based summaries but still below full table-level audit.
- Claims not listed here should still be treated as either synthesis-level inference or pending audit until they receive an explicit status label in a subtopic note.
