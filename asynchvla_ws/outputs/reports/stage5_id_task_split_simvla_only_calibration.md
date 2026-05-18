# Stage 5 SimVLA-only calibration: id_task_split

- alpha (miscoverage budget): 0.1
- target coverage: 0.90
- n_calib_all = 2500, n_calib_simvla = 1250

## Test sizes

| part | n_total | n_simvla |
| --- | ---: | ---: |
| test_id | 2500 | 1250 |

## Coverage and width per scheme

| scheme | part | n | coverage | mean_width |
| --- | --- | ---: | ---: | ---: |
| global_residual | test_id | 1250 | 0.863 | 1.039 |
| simvla_only_residual | test_id | 1250 | 0.779 | 0.820 |
| simvla_only_binned | test_id | 1250 | 0.768 | 0.857 |

## Calib q values

```json
{
  "global_residual": {
    "q_calib": 0.5193350315093994,
    "mean_width": 1.0386700630187988
  },
  "simvla_only_residual": {
    "q_calib": 0.40979576110839844,
    "mean_width": 0.8195915222167969
  },
  "simvla_only_binned": {
    "q_calib": null,
    "bins": [
      {
        "lo": 0.5180937051773071,
        "hi": 1.4060887098312378,
        "n": 313,
        "q": 0.49297448992729187
      },
      {
        "lo": 1.4060887098312378,
        "hi": 1.7217333316802979,
        "n": 312,
        "q": 0.4532341957092285
      },
      {
        "lo": 1.7217333316802979,
        "hi": 2.2274467945098877,
        "n": 312,
        "q": 0.4220874309539795
      },
      {
        "lo": 2.2274467945098877,
        "hi": 3.328244686126709,
        "n": 313,
        "q": 0.17766594886779785
      }
    ]
  }
}
```

## Full JSON

```json
{
  "split_name": "id_task_split",
  "alpha": 0.1,
  "n_calib_all": 2500,
  "n_calib_simvla": 1250,
  "test_parts": {
    "test_id": {
      "n_total": 2500,
      "n_simvla": 1250
    }
  },
  "schemes": {
    "global_residual": {
      "q_calib": 0.5193350315093994,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.8632,
          "mean_width": 1.0386700630187988
        }
      },
      "mean_width": 1.0386700630187988
    },
    "simvla_only_residual": {
      "q_calib": 0.40979576110839844,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.7792,
          "mean_width": 0.8195915222167969
        }
      },
      "mean_width": 0.8195915222167969
    },
    "simvla_only_binned": {
      "q_calib": null,
      "parts": {
        "test_id": {
          "n": 1250,
          "empirical_coverage": 0.768,
          "mean_width": 0.8570363715171814,
          "bin_assignment_counts": [
            562,
            266,
            258,
            164
          ]
        }
      },
      "bins": [
        {
          "lo": 0.5180937051773071,
          "hi": 1.4060887098312378,
          "n": 313,
          "q": 0.49297448992729187
        },
        {
          "lo": 1.4060887098312378,
          "hi": 1.7217333316802979,
          "n": 312,
          "q": 0.4532341957092285
        },
        {
          "lo": 1.7217333316802979,
          "hi": 2.2274467945098877,
          "n": 312,
          "q": 0.4220874309539795
        },
        {
          "lo": 2.2274467945098877,
          "hi": 3.328244686126709,
          "n": 313,
          "q": 0.17766594886779785
        }
      ]
    }
  }
}
```
