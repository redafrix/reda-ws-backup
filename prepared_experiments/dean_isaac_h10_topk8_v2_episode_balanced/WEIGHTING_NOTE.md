# Minibatch Weighting Detail

For the desired full-dataset objective, define raw scientific row weights:

- success row from episode i: `w_raw = 0.5 / (N_success_episodes * T_i)`
- failure row from episode i: `w_raw = 0.5 / (N_failure_episodes * T_i)`

Across the full training split, `sum(w_raw) = 1`.

For ordinary uniformly shuffled mini-batches, use a mean-one multiplier so the stochastic gradient is an unbiased estimate of the full weighted objective and the loss scale stays comparable to ordinary mean BCE:

`row_multiplier = N_train_rows * w_raw`

Then for each mini-batch:

`query_bce = binary_cross_entropy_with_logits(logits, labels, reduction="none")`

`loss = mean(query_bce * row_multiplier)`

Do NOT divide by the sum of weights inside each mini-batch. A random batch-dependent denominator changes the stochastic objective. Do NOT use the old V1 `pos_weight` simultaneously.

For the frozen V1 train split:

- `N_train_rows = 52825`
- `N_success_episodes = 2736`
- `N_failure_episodes = 64`

The implementation must still compute these values from the actual frozen arrays and assert that they match before training.