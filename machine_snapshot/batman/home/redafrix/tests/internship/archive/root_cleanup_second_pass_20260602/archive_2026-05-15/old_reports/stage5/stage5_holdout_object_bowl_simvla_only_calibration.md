# Stage 5 SimVLA-only calibration: holdout_object_bowl

- alpha (miscoverage budget): 0.1
- target coverage: 0.90
- n_calib_all = 2500, n_calib_simvla = 1250

## Test sizes

| part | n_total | n_simvla |
| --- | ---: | ---: |
| test_id | 2500 | 1250 |
| test_ood | 2500 | 1250 |

## Coverage and width per scheme

| scheme | part | n | coverage | mean_width |
| --- | --- | ---: | ---: | ---: |
| global_residual | test_id | 1250 | 0.687 | 0.774 |
| global_residual | test_ood | 1250 | 0.869 | 0.774 |
| simvla_only_residual | test_id | 1250 | 0.654 | 0.683 |
| simvla_only_residual | test_ood | 1250 | 0.819 | 0.683 |
| simvla_only_binned | test_id | 1250 | 0.630 | 0.629 |
| simvla_only_binned | test_ood | 1250 | 0.796 | 0.657 |

## Calib q values

```json
{
  "global_residual": {
    "q_calib": 0.3872396945953369,
    "mean_width": 0.7744793891906738
  },
  "simvla_only_residual": {
    "q_calib": 0.3414916396141052,
    "mean_width": 0.6829832792282104
  },
  "simvla_only_binned": {
    "q_calib": null,
    "bins": [
      {
        "lo": 0.6734454035758972,
        "hi": 1.319790005683899,
        "n": 313,
        "q": 0.3568040132522583
      },
      {
        "lo": 1.319790005683899,
        "hi": 1.5040634274482727,
        "n": 312,
        "q": 0.4144202470779419
      },
      {
        "lo": 1.5040634274482727,
        "hi": 1.792603999376297,
        "n": 312,
        "q": 0.2979273796081543
      },
      {
        "lo": 1.792603999376297,
        "hi": 2.7188732624053955,
        "n": 313,
        "q": 0.2824680805206299
      }
    ]
  }
}
```

## Full JSON

```json
{
  "split_name": "holdout_object_bowl",
  "alpha": 0.1,
  "n_calib_all": 2500,
  "n_calib_simvla": 1250,
  "test_parts": {
    "test_id": {
      "n_total": 2500,
      "n_simvla": 1250
    },
    "test_ood": {
      "n_total": 2500,
      "n_simvla": 1250
    }
  },
  "schemes": {
    "global_residual": {
      "q_calib": 0.3872396945953369,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.6872,
          "mean_width": 0.7744793891906738
        },
        "test_ood": {
          "n": 1250,
          "empirical_coverage": 0.8688,
          "mean_width": 0.7744793891906738
        }
      },
      "mean_width": 0.7744793891906738
    },
    "simvla_only_residual": {
      "q_calib": 0.3414916396141052,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.6536,
          "mean_width": 0.6829832792282104
        },
        "test_ood": {
          "n": 1250,
          "empirical_coverage": 0.8192,
          "mean_width": 0.6829832792282104
        }
      },
      "mean_width": 0.6829832792282104
    },
    "simvla_only_binned": {
      "q_calib": null,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.6296,
          "mean_width": 0.6290658769607544,
          "bin_assignment_counts": [
            201,
            146,
            380,
            523
          ]
        },
        "test_ood": {
          "n": 1250,
          "empirical_coverage": 0.796,
          "mean_width": 0.6571876272201538,
          "bin_assignment_counts": [
            293,
            246,
            221,
            490
          ]
        }
      },
      "bins": [
        {
          "lo": 0.6734454035758972,
          "hi": 1.319790005683899,
          "n": 313,
          "q": 0.3568040132522583
        },
        {
          "lo": 1.319790005683899,
          "hi": 1.5040634274482727,
          "n": 312,
          "q": 0.4144202470779419
        },
        {
          "lo": 1.5040634274482727,
          "hi": 1.792603999376297,
          "n": 312,
          "q": 0.2979273796081543
        },
        {
          "lo": 1.792603999376297,
          "hi": 2.7188732624053955,
          "n": 313,
          "q": 0.2824680805206299
        }
      ]
    }
  }
}
```
