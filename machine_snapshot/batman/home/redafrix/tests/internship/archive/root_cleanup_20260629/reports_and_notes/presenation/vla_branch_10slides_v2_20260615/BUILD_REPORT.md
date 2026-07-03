# VLA Branch Deck v2

## Deliverable

- `main.tex`: Beamer source.
- `main.pdf`: compiled 13-slide deck.
- `rendered_slides/`: PNG render of each slide for visual checking.
- `contact_sheet.png`: quick visual overview of all slides.

## Design Target

This version follows the first internship presentation template style: Beamer Madrid, dark blue title bars, minimal text, table/diagram-first slides, and no report-style paragraphs.

## Narrative Order

1. Goal: unseen-object manipulation.
2. Problem only: why unseen-object manipulation fails.
3. Existing solutions and limitations, including VLAs.
4. Why uncertainty is needed in a VLA.
5. Original SimVLA.
6. Modified SimVLA uncertainty head.
7. Results from the uncertainty-head idea before FIPER.
8. Original FIPER idea.
9. Our FIPER extension.
10. Best offline risk detector only.
11. Online evaluation architecture.
12. Selected-cap online result versus original SimVLA on the OOD suite.
13. Thank-you slide.

## Checked Facts Used

- SimVLA uncertainty-head first result from the second presentation: in-distribution AUC up to 0.9836 at step 100, but weak OOD AUC.
- Best offline FIPER extension: seen FA 15.0, seen detection 97.5, seen early 65.0; OOD FA 23.0, OOD detection 89.2, OOD early 37.6.
- Same-seed Bob OOD selected-cap versus basic/original SimVLA paper checkpoint: 1713/1800 vs 1668/1800, +45 successes, 1440 modifications.

## Verification

- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdfinfo main.pdf` reports 13 pages.
- `pdftoppm -png -r 140 main.pdf rendered_slides/slide`
- `contact_sheet.png` was generated and visually checked.
