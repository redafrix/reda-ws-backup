# Stage 9 Label Learnability Smoke

Status: blocked / not meaningful.

Reason: the latest real SimVLA pilot has label distribution `{'GOOD': 96}`. A BAD-vs-GOOD classifier cannot be trained or evaluated above random when only one class is present.

Decision: do not run final model training or final collection until label diversity is repaired.
