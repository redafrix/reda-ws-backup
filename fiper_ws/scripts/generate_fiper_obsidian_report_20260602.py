#!/usr/bin/env python3
from __future__ import annotations

import json
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian_reports" / "FIPER_RiskAware_Report_20260602"
ASSETS = VAULT / "assets"


def pct(v: float) -> str:
    return f"{v:.1f}%"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cleaned = textwrap.dedent(content).strip()
    normalized_lines = []
    for line in cleaned.splitlines():
        if line.startswith("        "):
            line = line[8:]
        normalized_lines.append(line.rstrip())
    path.write_text("\n".join(normalized_lines).strip() + "\n")


def bar_compare(path: Path, title: str, labels: list[str], series: dict[str, list[float]], ylabel: str = "%") -> None:
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(labels))
    width = 0.8 / max(1, len(series))
    for i, (name, values) in enumerate(series.items()):
        ax.bar(x - 0.4 + width / 2 + i * width, values, width, label=name)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.grid(axis="y", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def horizontal_delta(path: Path, title: str, labels: list[str], values: list[float], xlabel: str) -> None:
    fig, ax = plt.subplots(figsize=(10, 5.2))
    colors = ["#2ca25f" if v >= 0 else "#de2d26" for v in values]
    ax.barh(labels, values, color=colors)
    ax.axvline(0, color="#333", lw=1)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def grouped_stacked(path: Path, title: str, labels: list[str], recoveries: list[int], regressions: list[int]) -> None:
    fig, ax = plt.subplots(figsize=(10, 5.2))
    y = np.arange(len(labels))
    ax.barh(y, recoveries, color="#31a354", label="Recovered failures")
    ax.barh(y, [-v for v in regressions], color="#e34a33", label="Regressed successes")
    ax.axvline(0, color="#333", lw=1)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_title(title)
    ax.set_xlabel("Episode count")
    ax.grid(axis="x", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def line_or_bar(path: Path, title: str, labels: list[str], values: list[float], ylabel: str) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.bar(labels, values, color="#756bb1")
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def make_plots() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)

    bar_compare(
        ASSETS / "selected_detector_metrics.png",
        "Selected Offline Detector Policy: v2_018 Transformer k16",
        ["Seen FA", "OOD FA", "OOD Det", "Det@25", "Det@50"],
        {"rate": [15.4, 25.6, 95.2, 26.2, 85.7]},
    )

    ace_labels = ["baseline", "full8 every2", "first4 every1", "first4 every2"]
    bar_compare(
        ASSETS / "ace_sampling_ablation.png",
        "ACE Sampling Ablation on Fold 00",
        ace_labels,
        {
            "OOD FA": [25.6, 26.5, 28.0, 20.4],
            "Recall": [95.2, 92.9, 95.2, 95.2],
            "Det@25": [26.2, 19.0, 31.0, 14.3],
            "Det@50": [85.7, 83.3, 90.5, 81.0],
        },
    )

    realtime_labels = ["Task7 seen", "Task8 OOD", "Fold00 seen", "Fold00 unseen"]
    base = [54.2, 49.0, 38.2, 71.6]
    risk = [62.4, 49.7, 40.9, 72.3]
    bar_compare(
        ASSETS / "four_task_success_rates.png",
        "Real-Time Same-Seed Success Rates",
        realtime_labels,
        {"Baseline": base, "Risk-aware": risk},
    )
    horizontal_delta(
        ASSETS / "four_task_success_delta.png",
        "Risk-Aware Success-Rate Delta by Task",
        realtime_labels,
        [r - b for b, r in zip(base, risk)],
        "percentage points",
    )
    grouped_stacked(
        ASSETS / "recoveries_vs_regressions.png",
        "Paired Outcomes: Recoveries vs Regressions",
        realtime_labels,
        [80, 81, 31, 14],
        [43, 78, 19, 10],
    )
    bar_compare(
        ASSETS / "modification_stats.png",
        "Risk-Aware Action Modification Statistics",
        realtime_labels,
        {
            "Mean mods/episode": [17.29, 0.90, 9.78, 9.35],
            "Median mods/episode": [15.0, 0.0, 5.0, 2.0],
        },
        ylabel="modifications",
    )

    bar_compare(
        ASSETS / "task7_first_realtime.png",
        "First Task7 Real-Time Test",
        ["Success rate", "Recoveries", "Regressions"],
        {"Baseline": [58, 0, 0], "Risk-aware": [61, 25, 22]},
    )
    line_or_bar(
        ASSETS / "task7_timing_slowdown.png",
        "Task7 Runtime Cost",
        ["Baseline\nparallel", "Risk-aware\nparallel"],
        [3178 / 3600, 27570 / 3600],
        "hours",
    )

    bar_compare(
        ASSETS / "dean_uncertainty_features.png",
        "Dean Uncertainty Features: Base vs 98D Uncertainty",
        ["Seen FA", "Seen Det", "Seen Det@25", "OOD FA", "OOD Det", "OOD Det@50"],
        {
            "base": [14.2, 95.8, 54.0, 26.0, 86.0, 78.5],
            "unc_raw": [16.8, 97.5, 67.1, 28.9, 84.9, 83.9],
        },
    )

    bar_compare(
        ASSETS / "discarded_ideas_summary.png",
        "Why the Main Idea Survived",
        ["Capacity sweep", "Official AE AND", "Official pretrain", "Dynamic threshold", "ACE first4/2"],
        {
            "OOD FA": [28.0, 2.8, 28.4, 25.6, 20.4],
            "Recall": [95.2, 26.2, 95.2, 95.2, 95.2],
        },
    )


def frontmatter(title: str, tags: list[str]) -> str:
    tag_lines = "\n".join([f"  - {t}" for t in tags])
    return f"""---
title: {title}
created: 2026-06-02
tags:
{tag_lines}
---
"""


def make_notes() -> None:
    VAULT.mkdir(parents=True, exist_ok=True)
    (VAULT / ".obsidian").mkdir(exist_ok=True)
    write(VAULT / ".obsidian" / "app.json", '{"readableLineLength": false, "showLineNumber": true}')

    write(
        VAULT / "00 - FIPER Risk-Aware Report.md",
        frontmatter("FIPER Risk-Aware Report", ["fiper", "simvla", "risk-aware", "report"]) + """
        # FIPER Risk-Aware Report

        > [!abstract]
        > This vault summarizes the FIPER risk-aware SimVLA work so far. It focuses on the selected positive result: the `v2_018_transformer_k16` risk detector used online with `risk_filtered_lowest_score_candidate_v2_strict_margin`.

        ## Reading Order

        1. [[01 - Executive Summary]]
        2. [[02 - Data Collection and Splits]]
        3. [[03 - Architecture]]
        4. [[04 - Training and Calibration]]
        5. [[05 - Offline Experiments]]
        6. [[06 - Real-Time Deployment]]
        7. [[07 - Negative and Rejected Ideas]]
        8. [[08 - Dean Uncertainty Features]]
        9. [[09 - Glossary]]
        10. [[10 - Next Steps]]
        11. [[11 - Source Artifacts and Trust Checks]]

        ## Main Result

        The selected risk-aware policy improved the 4-task real-time same-seed success rate from **54.3%** to **57.3%** over **1881 paired episodes**. The strongest task-level gain was on `libero_10_with_milk/task7`: **54.2% -> 62.4%**.

        ![[assets/four_task_success_rates.png]]

        ## End-to-End Map

        ```mermaid
        graph TD
            A[SimVLA rollout data] --> B[FIPER receding samples]
            B --> C[Seen/OOD splits]
            C --> D[Train v2_018 transformer risk model]
            D --> E[Calibrate q95 + conformal mass]
            E --> F[Offline OOD/seen evaluation]
            F --> G[Real-time risk-aware SimVLA]
            G --> H[Same-seed baseline comparison]
            H --> I[Selected deployment evidence]
        ```
        """,
    )

    write(
        VAULT / "01 - Executive Summary.md",
        frontmatter("Executive Summary", ["fiper/summary", "risk-aware"]) + """
        # Executive Summary

        ## Selected Idea

        The selected idea is a temporal risk detector named `v2_018_transformer_k16`. It predicts whether the current SimVLA trajectory is entering failure risk. It is not a hard stop by itself. In real time, it is used as an action-selection helper: when the normal SimVLA action chunk looks risky and a candidate chunk looks clearly safer, the system executes the safer candidate.

        ## Why This Idea Was Kept

        Offline, the detector had the best practical balance we found:

        | Metric | Value |
        |---|---:|
        | Seen false alarm | 15.4% |
        | OOD false alarm | 25.6% |
        | OOD failure detection | 95.2% |
        | OOD Det@25 | 26.2% |
        | OOD Det@50 | 85.7% |
        | Mean detection time | 0.332 |

        ![[assets/selected_detector_metrics.png]]

        Real-time, it improved the 4-task same-seed comparison:

        | Metric | Baseline SimVLA | Risk-aware SimVLA |
        |---|---:|---:|
        | Paired episodes | 1881 | 1881 |
        | Successes | 1021 | 1077 |
        | Success rate | 54.3% | 57.3% |
        | Net gain | | +3.0 percentage points |

        ## Important Caveat

        The detector recovers failures but also causes regressions. The main engineering problem is no longer "can it help?" It can. The next problem is reducing harmful interventions while keeping the recoveries.

        ![[assets/recoveries_vs_regressions.png]]
        """,
    )

    write(
        VAULT / "02 - Data Collection and Splits.md",
        frontmatter("Data Collection and Splits", ["fiper/data", "splits"]) + """
        # Data Collection and Splits

        ## What Was Collected

        FIPER converts SimVLA rollouts into temporal training rows. Each row describes one timestep in a rollout:

        - current robot proprioception
        - previous executed actions
        - action chunk proposed by SimVLA
        - ACE candidate chunks
        - ACE metrics
        - episode outcome label, success or failure/timeout

        The current canonical FIPER combined dataset used for the selected baseline had **734,266 receding rows** after consolidation.

        ## What "Receding" Means

        SimVLA predicts a chunk of future actions, but the standard control loop executes only the first action, then queries SimVLA again at the next step. This is called receding-horizon control.

        ## Split Families Tried

        | Split family | Purpose | Train data | Eval data | Why it matters |
        |---|---|---|---|---|
        | `00_global_main` | General baseline | broad seen train/calib/val | general seen/OOD tests | used for `libero_10_with_milk/task7` real-time deployment |
        | `01_ood_task_8_9` | Task-id OOD | train without task 8/9 | task 8/9 held out | used for `libero_10_with_milk/task8` deployment |
        | `fold_00_holdout_alphabet_soup_bbq_sauce` | target-object OOD | excludes held-out objects | alphabet soup / BBQ sauce style object holdout | used for fold00 real-time seen/unseen object tasks |
        | capacity/history sweep fold00 | model size sanity check | fold00 split | fold00 OOD eval | tested if bigger/smaller transformer improves |
        | ACE sampling ablation fold00 | input-frequency ablation | fold00 split | fold00 OOD eval | tested if fewer ACE candidates improves false alarms |
        | Dean all-tasks random | uncertainty feature sanity | all tasks randomized | seen test | asks if uncertainty features help on in-distribution tasks |
        | Dean last-two task-id OOD | clean OOD with all episodes | last 2 task ids held out | OOD success/failure | asks if uncertainty features help on OOD task ids |

        ## Split Flow

        ```mermaid
        graph LR
            A[Collected episodes] --> B{Episode outcome}
            B --> S[Success episodes]
            B --> F[Failure/timeout episodes]
            S --> ST[success_train_seen]
            S --> SV[success_val_seen]
            S --> SC[success_calib_seen]
            S --> STE[success_test_seen or success_test_ood]
            F --> FT[failure_train_seen]
            F --> FV[failure_val_seen]
            F --> FTE[failure_test_seen or failure_eval_ood]
            SC --> Q[q95 row threshold]
            SV --> M[conformal mass threshold]
        ```

        ## Leakage Rules

        The selected detector must not use:

        - reward
        - success flag
        - future timesteps
        - visual object poses
        - task metadata as model input
        - OOD rows for training in OOD experiments
        """,
    )

    write(
        VAULT / "03 - Architecture.md",
        frontmatter("Architecture", ["fiper/model", "transformer"]) + """
        # Architecture

        ## Selected Model

        `v2_018_transformer_k16` is a sequence transformer risk model.

        | Parameter | Value |
        |---|---:|
        | history window | 16 timesteps |
        | sequence model | transformer encoder |
        | width | 128 |
        | layers | 3 |
        | heads | 4 |
        | dropout | 0.1 |
        | output | scalar risk score |

        ## Inputs

        The model receives three feature groups:

        1. **History tokens:** previous proprioception, previous executed actions, previous ACE metrics.
        2. **Action tokens:** current SimVLA candidate action chunk.
        3. **Static features:** action statistics, ACE metrics, current proprioception.

        ## Architecture Diagram

        ```mermaid
        graph TD
            H[History k=16<br/>proprio + action + ACE] --> HP[History projection]
            A[Current action chunk<br/>10 x 7] --> AP[Action projection]
            HP --> T[Transformer encoder<br/>3 layers, 4 heads]
            AP --> T
            T --> CLS[CLS sequence embedding]
            S[Static features<br/>action stats + ACE + proprio] --> SP[Static MLP]
            CLS --> C[Concat]
            SP --> C
            C --> HEAD[LayerNorm + MLP head]
            HEAD --> R[Risk score 0..1]
        ```

        ## Why A Temporal Model

        A single action can look risky in isolation, but failures often emerge from a sequence: repeated drift, unstable candidate chunks, or mismatch between action proposals and proprioceptive history. The transformer sees a short history window and can detect these temporal patterns.

        ## Output Meaning

        The output is a risk score. Higher score means the current state/action context resembles trajectories that later fail. It is not a calibrated probability of task failure by itself; it becomes actionable only after threshold calibration.
        """,
    )

    write(
        VAULT / "04 - Training and Calibration.md",
        frontmatter("Training and Calibration", ["fiper/training", "calibration"]) + """
        # Training and Calibration

        ## Training Objective

        The model is trained as a binary risk classifier:

        - label `0`: row comes from a successful episode
        - label `1`: row comes from a failure/timeout episode

        The practical objective is not only high accuracy. The detector must keep success false alarms low while detecting failures early enough to matter.

        ## Training Pipeline

        ```mermaid
        sequenceDiagram
            participant D as FIPER rows
            participant S as Split builder
            participant M as Transformer risk model
            participant C as Calibration
            participant E as Evaluation

            D->>S: materialize train / val / calib / test buckets
            S->>M: train on success_train_seen + failure_train_seen
            S->>M: early-stop on success_val_seen + failure_val_seen
            S->>C: estimate q95 on success_calib_seen
            S->>C: estimate conformal mass on success_val_seen
            C->>E: evaluate success false alarm and failure detection
        ```

        ## Calibration

        Two thresholds are used:

        | Threshold | Data used | Meaning |
        |---|---|---|
        | `q95` | `success_calib_seen` rows | row-level threshold; only the top 5% success-like risk scores should exceed it |
        | conformal mass | `success_val_seen` episodes | episode-level accumulated evidence threshold |

        The online alarm logic accumulates score excess above `q95`:

        $$
        mass_t = \\sum_{i=1}^{t} \\max(0, score_i - q95)
        $$

        An episode is flagged when `mass_t` exceeds the calibrated conformal mass threshold.

        ## Why Not Use Failures For Calibration

        Success-only calibration protects false alarm control: it asks "how much risk mass do successful episodes naturally generate?" Failures are used to train and validate the detector, but not to define the success false-alarm threshold.
        """,
    )

    write(
        VAULT / "05 - Offline Experiments.md",
        frontmatter("Offline Experiments", ["fiper/results", "offline"]) + """
        # Offline Experiments

        ## Selected Baseline Metrics

        ![[assets/selected_detector_metrics.png]]

        | Metric | Value |
        |---|---:|
        | Seen FA | 15.4% |
        | OOD FA | 25.6% |
        | OOD failure detection | 95.2% |
        | OOD Det@25 | 26.2% |
        | OOD Det@50 | 85.7% |
        | Mean detection time | 0.332 |

        ## ACE Sampling Ablation

        ![[assets/ace_sampling_ablation.png]]

        | Variant | Seen FA | OOD FA | Recall | Det@25 | Det@50 | Decision |
        |---|---:|---:|---:|---:|---:|---|
        | existing `v2_018` | 15.4% | 25.6% | 95.2% | 26.2% | 85.7% | selected |
        | full8 every 2 steps | 14.0% | 26.5% | 92.9% | 19.0% | 83.3% | rejected |
        | first4 every step | 15.4% | 28.0% | 95.2% | 31.0% | 90.5% | rejected: FA worse |
        | first4 every 2 steps | 14.0% | 20.4% | 95.2% | 14.3% | 81.0% | interesting but slower detection |

        ## Capacity and History Sweep

        Bigger transformers did not improve the final decision rule. Some large models overfit very early, often around epoch 1-2. Smaller models approached the baseline but did not reduce OOD false alarms enough.

        ## Official Expert Data Tests

        | Idea | Result | Decision |
        |---|---|---|
        | Gaussian/normality check on official actions | reduced false alarms but killed recall | rejected |
        | official action autoencoder as veto | OOD FA down to 2.8%, but failure detection down to 26.2% | rejected |
        | official action encoder pretraining | did not beat real existing `v2_018`; OOD FA increased 25.6% -> 28.4% | rejected |

        ![[assets/discarded_ideas_summary.png]]

        ## Dynamic Threshold Tests

        Step-dependent and history-dependent threshold variants did not improve enough over static conformal mass. The selected policy stayed `score_q95_mass_conformal_alpha_0.15`.
        """,
    )

    write(
        VAULT / "06 - Real-Time Deployment.md",
        frontmatter("Real-Time Deployment", ["fiper/deployment", "real-time"]) + """
        # Real-Time Deployment

        ## Deployment Policy

        The real-time policy tested on Bob/Sam was:

        `risk_filtered_lowest_score_candidate_v2_strict_margin`

        At each timestep:

        1. Sample the normal/main SimVLA action chunk.
        2. Sample 8 extra candidate chunks with unique random seeds.
        3. Compute ACE from the candidate set.
        4. Score main and candidate chunks with the risk detector.
        5. If strict margin rules pass, execute the lowest-risk candidate.
        6. Otherwise execute the normal main action.

        ```mermaid
        graph TD
            O[Current observation] --> M[Sample main SimVLA chunk]
            O --> C[Sample 8 candidate chunks]
            C --> ACE[Compute ACE metrics]
            M --> R[Risk detector]
            C --> R
            ACE --> R
            R --> D{Strict margin condition?}
            D -->|No| E[Execute main first action]
            D -->|Yes| F[Execute lowest-risk candidate first action]
            E --> N[Next env step]
            F --> N
        ```

        ## First Task7 Test

        ![[assets/task7_first_realtime.png]]

        | Metric | Baseline | Risk-aware |
        |---|---:|---:|
        | Episodes | 100 | 100 |
        | Success rate | 58.0% | 61.0% |
        | Recoveries | - | 25 |
        | Regressions | - | 22 |
        | Mean modifications / episode | - | 18.68 |

        Runtime cost was high:

        ![[assets/task7_timing_slowdown.png]]

        | Runtime metric | Baseline | Risk-aware |
        |---|---:|---:|
        | estimated parallel elapsed | 0.88 h | 7.66 h |
        | slowdown | | 8.68x |

        ## Four-Task Same-Seed Test

        ![[assets/four_task_success_rates.png]]

        | Task | Episodes | Baseline | Risk-aware | Delta |
        |---|---:|---:|---:|---:|
        | `libero_10_with_milk/task7` | 450 | 54.2% | 62.4% | +8.2 pts |
        | `libero_10_with_milk/task8` | 429 | 49.0% | 49.7% | +0.7 pts |
        | fold00 seen butter task2 | 450 | 38.2% | 40.9% | +2.7 pts |
        | fold00 unseen alphabet soup task0 | 552 | 71.6% | 72.3% | +0.7 pts |
        | **global** | **1881** | **54.3%** | **57.3%** | **+3.0 pts** |

        ![[assets/four_task_success_delta.png]]

        ## Recoveries and Regressions

        ![[assets/recoveries_vs_regressions.png]]

        | Task | Recoveries | Regressions |
        |---|---:|---:|
        | task7 seen | 80 | 43 |
        | task8 OOD | 81 | 78 |
        | fold00 seen butter | 31 | 19 |
        | fold00 unseen alphabet soup | 14 | 10 |

        ## Modification Rate

        ![[assets/modification_stats.png]]

        The modification rate matters because too many interventions can slow down or perturb a trajectory. The selected v2 strict policy is much less aggressive than the first v1 smoke, but it still creates regressions.

        ## Pairing Caveat

        The 4-task comparison is exact for reset seed order. The baseline also reused risk-aware main action seeds when available. If the baseline episode ran longer than the risk-aware episode, it generated fallback action sampling seeds after the risk-aware trace ended. This is a caveat for per-timestep action-seed equality, not for reset-seed pairing.
        """,
    )

    write(
        VAULT / "07 - Negative and Rejected Ideas.md",
        frontmatter("Negative and Rejected Ideas", ["fiper/negative-results"]) + """
        # Negative and Rejected Ideas

        This project tried many directions. The goal of this note is not to list every minor run, but to preserve the important decision evidence.

        ## Capacity Scaling

        Larger transformer variants were expected to help, but they did not. They tended to overfit early and increase false alarms. Smaller variants were not clearly better.

        ## Dynamic Thresholds

        Step-varying and history-varying thresholds were plausible because success episodes sometimes recover after a risk spike. In practice they did not beat the selected static conformal mass policy enough to justify replacing it.

        ## Official Expert Actions

        Official expert demonstrations were useful as a source of intuition, but not as a final detector component.

        | Test | Positive | Failure mode |
        |---|---|---|
        | action normality | false alarms decreased | recall collapsed |
        | autoencoder veto | OOD FA very low | failure detection collapsed |
        | action encoder pretraining | mechanically worked | did not beat existing model |

        ## ACE Subsampling

        Reducing ACE to first 4 candidates every 2 steps lowered OOD false alarms, but it hurt early detection too much. For a real-time safety monitor, detecting failures late is often not useful.

        ## Chunk Execution

        Full action chunk execution was surprisingly strong on Task7, but it changes the control policy itself. It is not the same scientific question as risk-aware first-action receding horizon, so it was paused and not selected as the main FIPER risk-aware story.
        """,
    )

    write(
        VAULT / "08 - Dean Uncertainty Features.md",
        frontmatter("Dean Uncertainty Features", ["fiper/uncertainty", "dean"]) + """
        # Dean Uncertainty Features

        Dean collected a newer dataset using a modified SimVLA checkpoint that exposes 49 uncertainty features plus 49 deltas, for 98 additional features per timestep.

        ## Datasets

        | Split | Episodes used | Successes | Failures | Purpose |
        |---|---:|---:|---:|---|
        | all-tasks random | 4191 | 3405 | 786 | test if uncertainty helps when all tasks are seen |
        | last-2-taskids OOD | 4191 total pool | 3405 | 786 | hold out last task ids for cleaner OOD |

        ## Initial Results

        ![[assets/dean_uncertainty_features.png]]

        | Split | Variant | FA | Detection | Det@25 | Det@50 | Decision |
        |---|---|---:|---:|---:|---:|---|
        | all-tasks random | base | 14.2% | 95.8% | 54.0% | 89.0% | strong |
        | all-tasks random | unc_raw | 16.8% | 97.5% | 67.1% | 87.8% | better early detection, worse FA |
        | OOD last2 | base | 26.0% | 86.0% | 39.8% | 78.5% | baseline |
        | OOD last2 | unc_raw | 28.9% | 84.9% | 35.5% | 83.9% | not better overall |

        ## Interpretation

        The uncertainty features contain signal, especially for early detection on seen splits, but raw 98D concatenation is not automatically better. The next useful direction is feature selection, regularization, or late fusion rather than blindly adding all uncertainty dimensions.
        """,
    )

    write(
        VAULT / "09 - Glossary.md",
        frontmatter("Glossary", ["fiper/glossary"]) + """
        # Glossary

        | Term | Meaning |
        |---|---|
        | FIPER | The monitoring dataset/pipeline built from receding SimVLA rollouts. It turns rollout timesteps into rows for training a risk detector. |
        | SimVLA | The vision-language-action model used to generate robot action chunks. |
        | VLA | Vision-language-action model: a model that uses images and language to output robot actions. |
        | action chunk | A short sequence of future robot actions predicted together. In this work, chunks are usually 10 actions of 7 dimensions. |
        | receding horizon | Execute only the first action of a predicted chunk, then re-query the model at the next timestep. |
        | ACE | Action Chunking Error / action candidate disagreement signal. It measures how much candidate chunks vary across sampled seeds. |
        | proprioception | Robot internal state, such as gripper pose/joint-related state, used as numeric input. |
        | risk score | Scalar detector output. Higher means the current trajectory/action resembles failure cases. |
        | false alarm | A success episode that the monitor flags as risky. Lower is better. |
        | failure detection | A failure episode that the monitor flags at least once. Higher is better. |
        | Det@25 | Fraction of failure episodes detected before 25% of the episode duration. |
        | Det@50 | Fraction of failure episodes detected before 50% of the episode duration. |
        | OOD | Out-of-distribution. Evaluation examples whose task, object, or perturbation was held out from training. |
        | seen | Data distribution allowed in training/calibration. |
        | fold | A train/test partition, often holding out particular objects or tasks. |
        | held-out object | Object category intentionally excluded from training to test generalization. |
        | calibration | Turning raw model scores into operational thresholds. |
        | q95 | 95th percentile of risk scores on success calibration rows. |
        | conformal mass | Episode-level accumulated risk evidence above q95. |
        | alpha | Conformal calibration parameter. Here `alpha=0.15` means the threshold is tuned to tolerate roughly 15% calibration false alarms. |
        | recovery | A paired seed where baseline failed but risk-aware succeeded. |
        | regression | A paired seed where baseline succeeded but risk-aware failed. |
        | same-seed comparison | Both methods run the same environment reset seeds in the same order. |
        | transformer | Sequence model using attention to combine information from multiple timesteps/tokens. |
        | attention head | One parallel attention mechanism inside a transformer layer. |
        | dropout | Training regularization that randomly zeroes activations to reduce overfitting. |
        | early stopping | Stop training when validation performance no longer improves. |
        | leakage | Any input or split mistake that gives the model information it should not have, such as reward, success label, future state, or OOD examples in training. |
        """,
    )

    write(
        VAULT / "10 - Next Steps.md",
        frontmatter("Next Steps", ["fiper/next"]) + """
        # Next Steps

        ## Main Technical Problem

        The current risk-aware policy helps, but it creates too many regressions. The best next work should target intervention quality rather than just offline detector score.

        ## Recommended Next Experiments

        1. **Intervention lockout:** prevent repeated interventions after a stable low-risk period.
        2. **Dynamic margin:** require larger risk improvement when main risk is not extreme.
        3. **Candidate diversity filter:** only switch action if candidate risk improves and action does not deviate too violently.
        4. **Fast scoring optimization:** reduce the 8.68x runtime overhead by batching all candidate chunks in one model forward pass.
        5. **Uncertainty feature selection:** use Dean uncertainty features with top-K or late-fusion, not raw 98D by default.
        6. **Regression review videos:** inspect paired regressions to see whether the risk-aware action causes timeout, wrong object, or motion inefficiency.

        ## Decision Summary

        Keep `v2_018_transformer_k16` as the main selected baseline. The real-time same-seed result is positive enough to justify continued work, but not strong enough to claim the monitor is deployment-ready.
        """,
    )

    write(
        VAULT / "11 - Source Artifacts and Trust Checks.md",
        frontmatter("Source Artifacts and Trust Checks", ["fiper/sources", "audit"]) + """
        # Source Artifacts and Trust Checks

        This note lists the local artifacts used to build the report. It is meant to make the numbers traceable for a future session.

        ## Main Source Reports

        | Artifact | Used for |
        |---|---|
        | `reports/FIPER_WS_CURRENT_BASELINE_AND_ORGANIZATION_REPORT_20260528.md` | selected baseline definition, offline metrics, split summary, rejected ideas |
        | `realtime_deployment/reports/REALTIME_TASK7_FINAL_CLEAN_AUDIT_AND_TIMING_REPORT_20260529.md` | first Task7 real-time baseline-vs-risk-aware result and timing |
        | `gana's_zip/riskaware_v2_018_repro_20260602.zip` | 4-task same-seed summary and reproducibility bundle |
        | `dean_uncertainty_work/outputs/all_tasks_random_v2/all_tasks_summary.csv` | Dean all-tasks random base vs uncertainty result |
        | `dean_uncertainty_work/outputs/ood_last2_taskids_v1/ood_last2_summary.csv` | Dean last-two-task-id OOD base vs uncertainty result |

        ## Generated Report Artifacts

        | Artifact | Purpose |
        |---|---|
        | `scripts/generate_fiper_obsidian_report_20260602.py` | regenerates this Obsidian report and all plots |
        | `obsidian_reports/FIPER_RiskAware_Report_20260602/assets/*.png` | report plots |
        | `obsidian_reports/FIPER_RiskAware_Report_20260602/*.md` | Obsidian notes |

        ## Trust Checks Already Encoded In The Story

        - The selected model passed feature hygiene audits: no reward, success flag, future timestep, object pose, or OOD leakage as model input.
        - The 4-task real-time comparison is same-reset-seed paired.
        - The selected policy is not claimed as deployment-ready because recoveries and regressions both occur.
        - Chunk-execution results are mentioned only as a separate finding, not as the main selected FIPER risk-aware result.

        ## Known Caveats

        - Some timing and same-action-seed details depend on logs generated on Bob/Sam. The report focuses on the final audited summaries rather than reconstructing every raw rollout.
        - Dean uncertainty features are promising but not yet selected as the main baseline. Raw 98D concatenation did not beat the base model overall on the OOD split.
        """,
    )


def main() -> None:
    make_plots()
    make_notes()
    print(VAULT)


if __name__ == "__main__":
    main()
