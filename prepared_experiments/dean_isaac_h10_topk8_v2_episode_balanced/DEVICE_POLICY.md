# Device Policy While HARD1000 Is Live

Priority 1 is not disturbing the live HARD1000 Isaac collection.

Agy must first inspect the exact promoted V1 trainer and recorded V1 device/backend. Do not guess.

Preferred execution while HARD1000 is live:

1. If the trainer supports CPU without scientific/code changes, run V2 on CPU with conservative process priority and limited CPU threads, leaving CUDA untouched.
2. If exact V1 execution requires CUDA, perform a read-only `nvidia-smi` capacity check and only run the small standalone risk-head process if there is clearly sufficient headroom. No second Isaac/Omniverse process is allowed.
3. If GPU headroom is uncertain, do not launch V2 on CUDA; use CPU if supported, otherwise stop and report `WAIT_FOR_HARD1000`.

Do not alter CUDA clocks, persistence mode, MIG, power limits, process affinity of HARD1000, or any Isaac process.

If CPU execution is used, record that backend in the V2 results so V1/V2 reproducibility metadata is explicit. The scientific change remains the loss/model-selection weighting; backend differences must be disclosed rather than hidden.
