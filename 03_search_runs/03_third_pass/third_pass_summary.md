# Third Pass Summary

## What This Pass Added

This pass finally surfaced several direct papers on:

- unknown-object manipulation
- category-level or object-agnostic manipulation
- no-object-model pick-and-place
- modern visuo-tactile perception

The best new direct hits were:

- `Manipulation of unknown objects via contact configuration regulation`
- `Self-Supervised Learning for Precise Pick-and-Place Without Object Model`
- `kPAM 2.0: Feedback Control for Category-Level Robotic Manipulation`
- `Learn to grasp unknown objects in robotic manipulation`
- `Attribute-Based Robotic Grasping With Data-Efficient Adaptation`

## Main Interpretation

The literature is now clustering into five useful branches for your internship:

1. Active tactile or visuo-tactile exploration
2. Unknown-object manipulation without explicit prior object models
3. Contact-rich or tactile servoing control
4. Generalization-oriented manipulation at category level
5. Large policy models such as VLA or RT-style systems

## What Still Looks Weak

- explicitly simple `reaching` to unseen objects as the main benchmark
- papers that vary only one factor first, like color then shape
- work that is exactly your supervisor's minimal task formulation, as opposed to grasping, pushing, or broader manipulation

This likely means your task is a synthesis problem:

- take methods from active exploration
- take baselines from unknown-object manipulation
- take control ideas from tactile servoing or contact-rich manipulation
- define a simpler reach-or-touch benchmark than much of the existing literature uses

## Current Best Reading Order

Start with [working_shortlist.csv](./working_shortlist.csv):

- first read the `read-first` papers
- then read the `read-next` papers
- use the `survey` entries only to map the field, not as your main technical basis

## Best Next Move

The search is now strong enough that the next highest-value step is no longer broad search.

It should be:

1. read the `read-first` shortlist
2. extract method assumptions and limitations
3. identify which branch is the best starting solution for your internship
