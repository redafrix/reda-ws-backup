# Workspace Guide

This workspace is organized by function rather than by creation time.

## Folders

- `00_subjects/official_briefs/`
  - Official internship subject PDFs.

- `01_context/conversations/`
  - Context material such as prior assistant conversations.

- `02_search_strategy/`
  - The literature search plan, query matrix, and paper tracking template.

- `03_search_runs/01_first_pass/`
  - First-pass seed search outputs.

- `03_search_runs/02_second_pass/`
  - Second-pass expansion outputs.

- `03_search_runs/03_third_pass/`
  - Third-pass targeted search outputs and the current shortlist.

- `04_structured_research/`
  - Structured deep-research artifacts such as outlines and field schemas.

- `05_external_assets/gana_project/archive/`
  - The original zip archive received from Gana.

- `05_external_assets/gana_project/extracted/`
  - The extracted contents of Gana's project for inspection and reuse.

- `intern_ship_ws/`
  - The main implementation workspace for SimVLA and TDQC.
  - Contains `phase2_tdqc_standalone/` (Failure Detection model).
  - Contains `smolvla_phase2/` (Integration and training scripts).
  - Contains `models/` (SimVLA and SmolVLM weights).

## Fast Start

If you want to continue the paper search quickly:
...
3. Read `03_search_runs/03_third_pass/working_shortlist.csv`

If you want to work on implementation:
1. Enter `intern_ship_ws/`
2. Activate the environment: `source activate_simvla.sh`
3. See `intern_ship_ws/README.md` for technical details.
4. Final TDQC Model: `intern_ship_ws/phase2_tdqc_standalone/results/checkpoints/lstm_td0_final_polish_v2/best.pt`

## Current Best Files

- `02_search_strategy/literature_search_plan.md`
- `02_search_strategy/query_matrix.csv`
- `03_search_runs/03_third_pass/working_shortlist.csv`
- `04_structured_research/unseen-object-exploration/outline.yaml`
- `04_structured_research/unseen-object-exploration/fields.yaml`



1 /home/redafrix/envs/simvla/bin/python3.10 "/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/final_ranker.py"
