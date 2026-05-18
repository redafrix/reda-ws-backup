# Stage 5 SimVLA-only calibration: holdout_libero_object

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
| global_residual | test_id | 1250 | 0.914 | 0.973 |
| global_residual | test_ood | 1250 | 0.907 | 0.973 |
| simvla_only_residual | test_id | 1250 | 0.809 | 0.725 |
| simvla_only_residual | test_ood | 1250 | 0.822 | 0.725 |
| simvla_only_binned | test_id | 1250 | 0.804 | 0.722 |
| simvla_only_binned | test_ood | 1250 | 0.822 | 0.712 |

## Calib q values

```json
{
  "global_residual": {
    "q_calib": 0.4866520166397095,
    "mean_width": 0.973304033279419
  },
  "simvla_only_residual": {
    "q_calib": 0.36236047744750977,
    "mean_width": 0.7247209548950195
  },
  "simvla_only_binned": {
    "q_calib": null,
    "bins": [
      {
        "lo": 0.23288175463676453,
        "hi": 1.4460258483886719,
        "n": 313,
        "q": 0.39363837242126465
      },
      {
        "lo": 1.4460258483886719,
        "hi": 1.8371388912200928,
        "n": 312,
        "q": 0.3390653133392334
      },
      {
        "lo": 1.8371388912200928,
        "hi": 2.57389897108078,
        "n": 312,
        "q": 0.34180498123168945
      },
      {
        "lo": 2.57389897108078,
        "hi": 4.344550609588623,
        "n": 313,
        "q": 0.3601255416870117
      }
    ]
  }
}
```

## Full JSON

```json
{
  "split_name": "holdout_libero_object",
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
      "q_calib": 0.4866520166397095,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.9136,
          "mean_width": 0.973304033279419
        },
        "test_ood": {
          "n": 1250,
          "empirical_coverage": 0.9072,
          "mean_width": 0.973304033279419
        }
      },
      "mean_width": 0.973304033279419
    },
    "simvla_only_residual": {
      "q_calib": 0.36236047744750977,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.8088,
          "mean_width": 0.7247209548950195
        },
        "test_ood": {
          "n": 1250,
          "empirical_coverage": 0.8216,
          "mean_width": 0.7247209548950195
        }
      },
      "mean_width": 0.7247209548950195
    },
    "simvla_only_binned": {
      "q_calib": null,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.804,
          "mean_width": 0.7217982376098633,
          "bin_assignment_counts": [
            451,
            523,
            171,
            105
          ]
        },
        "test_ood": {
          "n": 1250,
          "empirical_coverage": 0.8224,
          "mean_width": 0.7120286392211914,
          "bin_assignment_counts": [
            339,
            499,
            327,
            85
          ]
        }
      },
      "bins": [
        {
          "lo": 0.23288175463676453,
          "hi": 1.4460258483886719,
          "n": 313,
          "q": 0.39363837242126465
        },
        {
          "lo": 1.4460258483886719,
          "hi": 1.8371388912200928,
          "n": 312,
          "q": 0.3390653133392334
        },
        {
          "lo": 1.8371388912200928,
          "hi": 2.57389897108078,
          "n": 312,
          "q": 0.34180498123168945
        },
        {
          "lo": 2.57389897108078,
          "hi": 4.344550609588623,
          "n": 313,
          "q": 0.3601255416870117
        }
      ]
    }
  }
}
```
