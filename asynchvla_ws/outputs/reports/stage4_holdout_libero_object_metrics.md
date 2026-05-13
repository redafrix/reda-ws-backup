# Stage4 Metrics: holdout_libero_object

- Checkpoint dir: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage4/holdout_libero_object`

## Metrics JSON

```json
{
  "split_name": "holdout_libero_object",
  "parts": {
    "train": 6000,
    "calib": 1500,
    "test_id": 1500,
    "test_ood": 1200
  },
  "models": {
    "full": {
      "best_epoch": 197,
      "best_calib_loss": 0.014243168756365776,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.9988492727279663,
          "spearman": 0.9930013578201308,
          "auroc_top30_bad": 0.9999112433862434,
          "mae": 0.031211616471409798,
          "mse": 0.0018602462951093912,
          "risk_coverage": [
            [
              0.1,
              0.0
            ],
            [
              0.25,
              0.08150424808263779
            ],
            [
              0.5,
              0.24205444753170013
            ],
            [
              0.75,
              0.49716678261756897
            ],
            [
              1.0,
              0.9100528955459595
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 1.0,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.98925,
          "action_sensitivity_std": 0.8140610819397194
        },
        "calib": {
          "n": 1500,
          "pearson": 0.977689266204834,
          "spearman": 0.9481715708382141,
          "auroc_top30_bad": 0.9989248677248677,
          "mae": 0.1334245204925537,
          "mse": 0.03145049139857292,
          "risk_coverage": [
            [
              0.1,
              0.027903515845537186
            ],
            [
              0.25,
              0.11346383392810822
            ],
            [
              0.5,
              0.21831806004047394
            ],
            [
              0.75,
              0.445928692817688
            ],
            [
              1.0,
              0.8411845564842224
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.984,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.952,
          "action_sensitivity_std": 0.6971942274805244
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.9646300077438354,
          "spearman": 0.9418755807538403,
          "auroc_top30_bad": 0.9911873015873016,
          "mae": 0.15683025121688843,
          "mse": 0.053164735436439514,
          "risk_coverage": [
            [
              0.1,
              0.05006656050682068
            ],
            [
              0.25,
              0.1211637333035469
            ],
            [
              0.5,
              0.25075384974479675
            ],
            [
              0.75,
              0.5488797426223755
            ],
            [
              1.0,
              0.9106737375259399
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.976,
          "expert_lt_simvla_seed0": 0.992,
          "simvla_pairwise_true_order_accuracy": 0.931,
          "action_sensitivity_std": 0.679554728859954
        },
        "test_ood": {
          "n": 1200,
          "pearson": 0.9877446293830872,
          "spearman": 0.9557132614118118,
          "auroc_top30_bad": 0.9993816137566137,
          "mae": 0.09264756739139557,
          "mse": 0.015056272968649864,
          "risk_coverage": [
            [
              0.1,
              0.01898925192654133
            ],
            [
              0.25,
              0.10667770355939865
            ],
            [
              0.5,
              0.21380513906478882
            ],
            [
              0.75,
              0.4588828384876251
            ],
            [
              1.0,
              0.8271518349647522
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.965,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.9575,
          "action_sensitivity_std": 0.6974606890224283
        }
      }
    },
    "context": {
      "best_epoch": 68,
      "best_calib_loss": 0.12923619151115417,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.08415881544351578,
          "spearman": 0.10229450890883585,
          "auroc_top30_bad": 0.5555630952380952,
          "mae": 0.6478137373924255,
          "mse": 0.8349005579948425,
          "risk_coverage": [
            [
              0.1,
              0.7696555852890015
            ],
            [
              0.25,
              0.8441219329833984
            ],
            [
              0.5,
              0.8657842874526978
            ],
            [
              0.75,
              0.8755108118057251
            ],
            [
              1.0,
              0.9100528955459595
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.80675,
          "action_sensitivity_std": 0.0
        },
        "calib": {
          "n": 1500,
          "pearson": 0.028836222365498543,
          "spearman": 0.05116257622243128,
          "auroc_top30_bad": 0.5076190476190475,
          "mae": 0.6315862536430359,
          "mse": 0.6970278024673462,
          "risk_coverage": [
            [
              0.1,
              0.8148783445358276
            ],
            [
              0.25,
              0.8274161219596863
            ],
            [
              0.5,
              0.8168950080871582
            ],
            [
              0.75,
              0.8380735516548157
            ],
            [
              1.0,
              0.8411845564842224
            ]
          ],
          "expert_lt_perturb_large": 0.004,
          "expert_lt_other_task": 0.004,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.811,
          "action_sensitivity_std": 2.0124495435738486e-10
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.08014225214719772,
          "spearman": 0.07500438433432659,
          "auroc_top30_bad": 0.5229904761904762,
          "mae": 0.6624733209609985,
          "mse": 0.6986788511276245,
          "risk_coverage": [
            [
              0.1,
              0.6862798929214478
            ],
            [
              0.25,
              0.8169624209403992
            ],
            [
              0.5,
              0.8710499405860901
            ],
            [
              0.75,
              0.8960516452789307
            ],
            [
              1.0,
              0.9106736779212952
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.854,
          "action_sensitivity_std": 0.0
        },
        "test_ood": {
          "n": 1200,
          "pearson": 0.032917238771915436,
          "spearman": 0.027980535781257424,
          "auroc_top30_bad": 0.5099603174603174,
          "mae": 0.6308258771896362,
          "mse": 0.593284547328949,
          "risk_coverage": [
            [
              0.1,
              0.7609438300132751
            ],
            [
              0.25,
              0.8062348961830139
            ],
            [
              0.5,
              0.8144536018371582
            ],
            [
              0.75,
              0.8162211179733276
            ],
            [
              1.0,
              0.8271517753601074
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.8175,
          "action_sensitivity_std": 0.0
        }
      }
    },
    "action": {
      "best_epoch": 49,
      "best_calib_loss": 0.025149693712592125,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.9455997943878174,
          "spearman": 0.78816426717418,
          "auroc_top30_bad": 0.9786484126984126,
          "mae": 0.17445221543312073,
          "mse": 0.08052171021699905,
          "risk_coverage": [
            [
              0.1,
              0.2853209376335144
            ],
            [
              0.25,
              0.3067626655101776
            ],
            [
              0.5,
              0.34741976857185364
            ],
            [
              0.75,
              0.4978465735912323
            ],
            [
              1.0,
              0.9100528955459595
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.49,
          "expert_lt_simvla_seed0": 0.971,
          "simvla_pairwise_true_order_accuracy": 0.971,
          "action_sensitivity_std": 0.7725605687871212
        },
        "calib": {
          "n": 1500,
          "pearson": 0.9471619129180908,
          "spearman": 0.7573303051291217,
          "auroc_top30_bad": 0.986278306878307,
          "mae": 0.17873790860176086,
          "mse": 0.06438802927732468,
          "risk_coverage": [
            [
              0.1,
              0.28137850761413574
            ],
            [
              0.25,
              0.2906947731971741
            ],
            [
              0.5,
              0.31663843989372253
            ],
            [
              0.75,
              0.44413214921951294
            ],
            [
              1.0,
              0.8411845564842224
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.484,
          "expert_lt_simvla_seed0": 0.948,
          "simvla_pairwise_true_order_accuracy": 0.952,
          "action_sensitivity_std": 0.7318274286835025
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.9150746464729309,
          "spearman": 0.7454276895268647,
          "auroc_top30_bad": 0.9918835978835978,
          "mae": 0.22417175769805908,
          "mse": 0.10294054448604584,
          "risk_coverage": [
            [
              0.1,
              0.32346904277801514
            ],
            [
              0.25,
              0.3499661087989807
            ],
            [
              0.5,
              0.3633033037185669
            ],
            [
              0.75,
              0.5362765192985535
            ],
            [
              1.0,
              0.9106736779212952
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.524,
          "expert_lt_simvla_seed0": 0.976,
          "simvla_pairwise_true_order_accuracy": 0.957,
          "action_sensitivity_std": 0.7293291580951816
        },
        "test_ood": {
          "n": 1200,
          "pearson": 0.9598546028137207,
          "spearman": 0.7690567659243603,
          "auroc_top30_bad": 0.9994874338624338,
          "mae": 0.15813133120536804,
          "mse": 0.046101462095975876,
          "risk_coverage": [
            [
              0.1,
              0.2619861662387848
            ],
            [
              0.25,
              0.28371408581733704
            ],
            [
              0.5,
              0.29759079217910767
            ],
            [
              0.75,
              0.45747023820877075
            ],
            [
              1.0,
              0.8271517753601074
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.5,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.97,
          "action_sensitivity_std": 0.7346785848005886
        }
      }
    }
  }
}
```
