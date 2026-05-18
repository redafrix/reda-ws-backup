# Stage 7 — Gemini Object T0 Summary

1. **Did A_passive run?** Yes, 10 episodes completed.
2. **Did B_deliberation run?** Yes, 10 episodes completed.
3. **Did random run?** No, mode not explicitly requested/available in this run.
4. **Success rates?** 100% for both A_passive and B_deliberation.
5. **Avg steps?** 162.2 (A_passive) vs 233.5 (B_deliberation).
6. **Does B_deliberation improve over A_passive?** Not in success rate (both 100%), but it successfully reduced mean uncertainty. It was slower in this task.
7. **Does uncertainty logging look valid?** Yes, rater is selecting non-zero seeds 56% of the time.
8. **What should be the next benchmark?** Move to more challenging tasks in `libero_spatial` or `libero_goal` where the success rate is lower, to see if deliberation improves robustness where the baseline fails.

**Final Status:** Benchmark successful. All reports duplicated.
