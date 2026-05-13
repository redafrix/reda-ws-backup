# Stage4 Metrics: id_task_split

- Checkpoint dir: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage4/id_task_split`

## Metrics JSON

```json
{
  "split_name": "id_task_split",
  "parts": {
    "train": 6000,
    "calib": 1500,
    "test_id": 1500,
    "test_ood": 0
  },
  "models": {
    "full": {
      "best_epoch": 168,
      "best_calib_loss": 0.017341891303658485,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.9979942440986633,
          "spearman": 0.9917609307369475,
          "auroc_top30_bad": 0.9999400793650793,
          "mae": 0.04031410813331604,
          "mse": 0.003505455097183585,
          "risk_coverage": [
            [
              0.1,
              0.0017599669517949224
            ],
            [
              0.25,
              0.08218078315258026
            ],
            [
              0.5,
              0.248490110039711
            ],
            [
              0.75,
              0.5004395842552185
            ],
            [
              1.0,
              0.8937799334526062
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 1.0,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.99175,
          "action_sensitivity_std": 0.7666211998809356
        },
        "calib": {
          "n": 1500,
          "pearson": 0.9817774295806885,
          "spearman": 0.9575744548075589,
          "auroc_top30_bad": 0.9983449735449735,
          "mae": 0.14632052183151245,
          "mse": 0.04018029570579529,
          "risk_coverage": [
            [
              0.1,
              0.05219004303216934
            ],
            [
              0.25,
              0.11441239714622498
            ],
            [
              0.5,
              0.2542191743850708
            ],
            [
              0.75,
              0.5366949439048767
            ],
            [
              1.0,
              0.9579153656959534
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.996,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.97,
          "action_sensitivity_std": 0.7319999537007079
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.972759485244751,
          "spearman": 0.9559786224639183,
          "auroc_top30_bad": 0.9899470899470899,
          "mae": 0.13743320107460022,
          "mse": 0.04115775600075722,
          "risk_coverage": [
            [
              0.1,
              0.0413656048476696
            ],
            [
              0.25,
              0.0998426079750061
            ],
            [
              0.5,
              0.2353634089231491
            ],
            [
              0.75,
              0.5081590414047241
            ],
            [
              1.0,
              0.8799755573272705
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.988,
          "expert_lt_simvla_seed0": 0.992,
          "simvla_pairwise_true_order_accuracy": 0.947,
          "action_sensitivity_std": 0.6812728266452327
        }
      }
    },
    "context": {
      "best_epoch": 19,
      "best_calib_loss": 0.1449163258075714,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.10689008980989456,
          "spearman": 0.10891134657005436,
          "auroc_top30_bad": 0.5643968253968255,
          "mae": 0.6282354593276978,
          "mse": 0.7035982012748718,
          "risk_coverage": [
            [
              0.1,
              0.7653955817222595
            ],
            [
              0.25,
              0.7764222025871277
            ],
            [
              0.5,
              0.8256838917732239
            ],
            [
              0.75,
              0.8567534685134888
            ],
            [
              1.0,
              0.8937799334526062
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.80525,
          "action_sensitivity_std": 0.0
        },
        "calib": {
          "n": 1500,
          "pearson": 0.08914926648139954,
          "spearman": 0.09968645701305685,
          "auroc_top30_bad": 0.5486455026455026,
          "mae": 0.6948656439781189,
          "mse": 0.8461014032363892,
          "risk_coverage": [
            [
              0.1,
              0.6783066987991333
            ],
            [
              0.25,
              0.8989728093147278
            ],
            [
              0.5,
              0.9368657469749451
            ],
            [
              0.75,
              0.9253641366958618
            ],
            [
              1.0,
              0.9579153656959534
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.827,
          "action_sensitivity_std": 1.1239159602905075e-10
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.07003457099199295,
          "spearman": 0.08366031458164085,
          "auroc_top30_bad": 0.5496486772486772,
          "mae": 0.6465123891830444,
          "mse": 0.683255672454834,
          "risk_coverage": [
            [
              0.1,
              0.7160750031471252
            ],
            [
              0.25,
              0.7527380585670471
            ],
            [
              0.5,
              0.8306469917297363
            ],
            [
              0.75,
              0.8573271632194519
            ],
            [
              1.0,
              0.8799755573272705
            ]
          ],
          "expert_lt_perturb_large": 0.004,
          "expert_lt_other_task": 0.004,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.813,
          "action_sensitivity_std": 1.1239159602905075e-10
        }
      }
    },
    "action": {
      "best_epoch": 112,
      "best_calib_loss": 0.03579229116439819,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.9428264498710632,
          "spearman": 0.7968918339556815,
          "auroc_top30_bad": 0.9872496693121693,
          "mae": 0.1699472814798355,
          "mse": 0.07487663626670837,
          "risk_coverage": [
            [
              0.1,
              0.2978902757167816
            ],
            [
              0.25,
              0.30384954810142517
            ],
            [
              0.5,
              0.3476916551589966
            ],
            [
              0.75,
              0.5003979206085205
            ],
            [
              1.0,
              0.8937799334526062
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.491,
          "expert_lt_simvla_seed0": 0.975,
          "simvla_pairwise_true_order_accuracy": 0.96675,
          "action_sensitivity_std": 0.7343342778394992
        },
        "calib": {
          "n": 1500,
          "pearson": 0.9300669431686401,
          "spearman": 0.7541202688903483,
          "auroc_top30_bad": 0.9759195767195767,
          "mae": 0.2263048142194748,
          "mse": 0.10996761173009872,
          "risk_coverage": [
            [
              0.1,
              0.33648881316185
            ],
            [
              0.25,
              0.3592735230922699
            ],
            [
              0.5,
              0.3833872377872467
            ],
            [
              0.75,
              0.5334838628768921
            ],
            [
              1.0,
              0.9579153060913086
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.488,
          "expert_lt_simvla_seed0": 0.98,
          "simvla_pairwise_true_order_accuracy": 0.963,
          "action_sensitivity_std": 0.7853925559048346
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.9278537631034851,
          "spearman": 0.7387858776359721,
          "auroc_top30_bad": 0.9840656084656084,
          "mae": 0.21128718554973602,
          "mse": 0.091978058218956,
          "risk_coverage": [
            [
              0.1,
              0.3186417520046234
            ],
            [
              0.25,
              0.34863996505737305
            ],
            [
              0.5,
              0.3724033236503601
            ],
            [
              0.75,
              0.49083811044692993
            ],
            [
              1.0,
              0.8799755573272705
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.48,
          "expert_lt_simvla_seed0": 0.984,
          "simvla_pairwise_true_order_accuracy": 0.971,
          "action_sensitivity_std": 0.7334402605549754
        }
      }
    }
  }
}
```
