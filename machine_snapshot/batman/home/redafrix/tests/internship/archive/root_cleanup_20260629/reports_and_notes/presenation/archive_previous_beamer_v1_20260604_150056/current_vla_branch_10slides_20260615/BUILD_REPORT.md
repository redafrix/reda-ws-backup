# VLA Branch 10-Slide Presentation Build Report

## Output

- `main.tex`
- `main.pdf`
- `rendered_slides/contact_sheet.png`
- `rendered_slides/slide-01.png` through `slide-10.png`

## Source Material Used

- Visual style from `../internship_first_presentation/presentation.tex`.
- SimVLA architecture images from `../internship_second_presentation-20260615T125536Z-3-001/internship_second_presentation/assets/`.
- Risk-aware numbers and selected-cap results from the consolidated Obsidian report `FIPER Risk-Aware SimVLA - Full Report.md`.

## Slide Order

1. Title and VLA branch scope.
2. Target problem: unseen-object manipulation.
3. VLA motivation and uncertainty limitation.
4. Original SimVLA architecture.
5. Modified SimVLA uncertainty head.
6. FIPER direction: score to action selection.
7. Offline detector results.
8. Online progression: basic risk-aware -> uncertainty -> H10 -> threshold 0.3 -> selected-cap.
9. Selected-cap mechanism and best online result.
10. VLA branch synthesis.

## Verification

- PDF compiles successfully with `pdflatex`.
- Exactly 10 slides rendered.
- Contact sheet generated.
- Main quantitative claims checked against the consolidated report:
  - historical four-task basic risk-aware: +56 net successes over 1,881 paired episodes.
  - Dean Task0 uncertainty risk: 39/100 vs 34/100 modified SimVLA.
  - Task6 H10 threshold 0.3: 62/100 vs 57/100.
  - Bob OOD threshold 0.3: 1,713/1,800 vs 1,718/1,800.
  - Dean selected-cap: 1,741/1,800 vs 1,726/1,800, 38 rescues / 23 regressions, net +15.
