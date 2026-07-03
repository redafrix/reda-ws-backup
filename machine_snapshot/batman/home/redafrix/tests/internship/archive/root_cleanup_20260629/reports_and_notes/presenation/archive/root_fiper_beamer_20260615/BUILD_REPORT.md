# Presentation Build Report (BUILD_REPORT.md)

This report documents the compilation and verification of the Beamer presentation for the SimVLA Risk Detection task.

---

## 1. Output Files and Paths

All files have been compiled and generated in the target directory:
`/home/redafrix/tests/internship/presenation`

*   **LaTeX Source:** [main.tex](file:///home/redafrix/tests/internship/presenation/main.tex)
*   **PDF Presentation:** [main.pdf](file:///home/redafrix/tests/internship/presenation/main.pdf)
*   **PNG Slide Directory:** [rendered_slides/](file:///home/redafrix/tests/internship/presenation/rendered_slides/) containing `slide-01.png` through `slide-09.png`
*   **Contact Sheet:** [rendered_slides/contact_sheet.png](file:///home/redafrix/tests/internship/presenation/rendered_slides/contact_sheet.png)

---

## 2. Compilation and Validation Workflow

1.  **LaTeX Compilation (Two-Pass):**
    ```bash
    pdflatex -halt-on-error main.tex
    pdflatex -halt-on-error main.tex
    ```
2.  **PNG Slide Rendering (180 DPI):**
    ```bash
    rm -rf rendered_slides
    mkdir -p rendered_slides
    pdftoppm -png -r 180 main.pdf rendered_slides/slide
    ```
3.  **Contact Sheet Montage:**
    ```bash
    montage rendered_slides/slide-*.png -tile 2x5 -geometry 567x319+10+10 rendered_slides/contact_sheet.png
    ```
4.  **Verification Script Executed:**
    ```bash
    ./check_presentation.py
    ```

---

## 3. Reference Source Tracking

The presentation content is verified against and aligned with:
1.  `/home/redafrix/tests/internship/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py`
2.  `/home/redafrix/tests/internship/fiper_ws/realtime_deployment/scripts/collect_fiper_uncertainty_receding_dean_v1.py`
3.  `/home/redafrix/tests/internship/fiper_ws/reports/dean_topk8_fusion_policy_v1_20260602/DEAN_TOPK8_FUSION_POLICY_REPORT.md`
4.  `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`

---

## 4. Ground Truth Verification

### A. Dimensions and Routing
*   **History = 16 x 21:** Each history step contains 8D robot proprioception + 7D executed action + 6D action disagreement metrics (calculated via `compute_ace_metrics`).
*   **Static Base Input = 43D:** Consists of 28D action chunk stats + 7D current action disagreement + 8D current robot proprioception.
*   **Static with Uncertainty = 51D:** Base input (43D) + 8 selected uncertainty signals (51D total).
*   **Routing:** Slide 4 (Architecture) routes the History 16 x 21 and Candidate action to the Temporal Transformer, whereas the Static features 51D (with the 8 selected uncertainty signals) go exclusively to the Static Network, avoiding the Transformer.

### B. Real-time Decision Protocol
*   **Isolated Main Action:** The main SimVLA action is generated alone.
*   **Alternative Actions:** 8 alternative actions are generated separately.
*   **Score and Select:** The detector scores all 9 options and selects an alternative only if its risk margin exceeds a calibrated threshold.

### C. Historical Baseline Note (RND)
*   **Random Network Distillation (RND):** Random Network Distillation was tested as a novelty baseline, but it is not part of the final selected pipeline. It operates by comparing a fixed random network and a trained predictor network, where high prediction error signals that the current state/observation is unfamiliar. On the slides, it is represented strictly as a tiny badge: `"Earlier test: RND novelty signal"`.

---

## 5. Slide-by-Slide Outline

1.  **Slide 1 — Title:** "Risk Detection for SimVLA: From FIPER to Uncertainty Signals".
2.  **Slide 2 — Original FIPER + ACE:** Explains candidate-action disagreement (ACE) and points out that original FIPER calculates risk only around the current action.
3.  **Slide 3 — What I changed:** Two-row visual comparison showing original FIPER's current state risk scoring vs my detector's history + uncertainty scoring. Features a tiny badge: `"Earlier test: RND novelty signal"`.
4.  **Slide 4 — Architecture:** Two-branch flow diagram with clean, readable labels showing "History 16 x 21", "Candidate action", and "Static features 51D".
5.  **Slide 5 — Data collection:** Data collection flow from rollout to training labels, detailing action chunks and disagreement variation.
6.  **Slide 6 — Real-time decision:** Logic flowchart explaining generation of the main action alone, alternative generation, scoring, and selection.
7.  **Slide 7 — Uncertainty signals:** Diagram detailing raw signals (49 raw + 49 changes) down to 8 selected uncertainty signals, categorized into 4 families.
8.  **Slide 8 — Offline data results:** Dual side-by-side tables ("Seen tasks" and "Held-out tasks") showing false alarms, failures detected, and early detection metrics. Stacked headers prevent clipping.
9.  **Slide 9 — Simulator tests + checks:** Success/Intervention metrics table under "same initial situations" and remaining tasks.

---

## 6. Validation Checklist

*   **SLIDE_COUNT = 9**
*   **LANGUAGE_ENGLISH_PASS = YES**
*   **RND_IS_ONLY_SMALL_BADGE = YES**
*   **ACE_EXPLAINED_ONCE = YES**
*   **ARCHITECTURE_LABELS_READABLE = YES**
*   **SLIDE_8_NOT_CUT = YES**
*   **VISUAL_VALIDATION_PASS = YES**
