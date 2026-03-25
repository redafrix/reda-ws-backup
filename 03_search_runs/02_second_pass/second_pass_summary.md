# Second Pass Summary

## What Changed

The second pass improved coverage mainly through:

- citation expansion from the strongest direct seeds
- venue-based search in RSS and CoRL
- a targeted attempt at the weak `reaching-touch-scan` bucket

The best additions did **not** come from raw reaching keywords.
They came from:

- `AcTExplore` citation expansion
- tactile/control references
- RSS and CoRL venue sweeps

## Best New Additions

- `ViTract: Robust Object Shape Perception via Active Visuo-Tactile Interaction`
- `Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control`
- `Controlling Contact-Rich Manipulation Under Partial Observability`
- `A visuo-tactile control framework for manipulation and exploration of unknown objects`
- `A Control Framework for Tactile Servoing`
- `SimNet: Enabling Robust Unknown Object Manipulation from Pure Synthetic Data via Stereo`
- `Vision-driven Compliant Manipulation for Reliable High-Precision Assembly Tasks`

## Main Conclusions From This Round

1. The contact/tactile branch is now much stronger than the reaching branch.
2. The classical-control branch is becoming more concrete and useful.
3. There is a real cluster around:
   - tactile servoing
   - visuo-tactile exploration
   - contact-rich manipulation under uncertainty
4. The direct `reaching unseen object` retrieval problem is still weak with naive keyword search.

## What This Means For The Research Direction

The field is giving stronger support for a path like:

- active perception or exploration
- contact confirmation
- uncertainty-aware control or policy selection
- generalization to unknown object geometry or surface properties

This is stronger than a narrow search for only `reaching unseen object`, which seems too specific for how many papers are titled.

## Updated Weakest Gap

Still missing:

- papers explicitly framing the task as `reach or approach an unseen object`
- controlled generalization studies where only one factor changes first, such as color then shape
- papers that use a simple reaching benchmark as the main evaluation for unseen-object transfer

## Best Next Moves

1. Run a venue sweep specifically for:
   - `ICRA`
   - `IROS`
   - `CoRL`
   using terms like:
   - `unknown object`
   - `generalization`
   - `reaching`
   - `contact`
   - `tactile`
2. Expand from these newly added papers:
   - `ViTract`
   - `SimNet`
   - `Controlling Contact-Rich Manipulation Under Partial Observability`
   - `Vision-driven Compliant Manipulation for Reliable High-Precision Assembly Tasks`
3. Use the installed `research` skill after this venue pass, not before
   - by then the seed set is strong enough to generate a useful deep-research outline
