# Stage4 Metrics: holdout_object_bowl

- Checkpoint dir: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage4/holdout_object_bowl`

## Metrics JSON

```json
{
  "split_name": "holdout_object_bowl",
  "parts": {
    "train": 6000,
    "calib": 1500,
    "test_id": 1500,
    "test_ood": 1500
  },
  "models": {
    "full": {
      "best_epoch": 250,
      "best_calib_loss": 0.016270827502012253,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.998659610748291,
          "spearman": 0.9916837676456443,
          "auroc_top30_bad": 0.9998988095238096,
          "mae": 0.029728727415204048,
          "mse": 0.0019012250704690814,
          "risk_coverage": [
            [
              0.1,
              0.0007845218060538173
            ],
            [
              0.25,
              0.07967822253704071
            ],
            [
              0.5,
              0.22957035899162292
            ],
            [
              0.75,
              0.4580712914466858
            ],
            [
              1.0,
              0.8511459231376648
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 1.0,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.9925,
          "action_sensitivity_std": 0.7620857292760416
        },
        "calib": {
          "n": 1500,
          "pearson": 0.9786802530288696,
          "spearman": 0.9602273266125536,
          "auroc_top30_bad": 0.996184126984127,
          "mae": 0.14226171374320984,
          "mse": 0.03392402082681656,
          "risk_coverage": [
            [
              0.1,
              0.025257056578993797
            ],
            [
              0.25,
              0.11668643355369568
            ],
            [
              0.5,
              0.24918870627880096
            ],
            [
              0.75,
              0.5029638409614563
            ],
            [
              1.0,
              0.8862152695655823
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.988,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.98,
          "action_sensitivity_std": 0.6891729628960259
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.9879329800605774,
          "spearman": 0.9637744828600362,
          "auroc_top30_bad": 0.9996656084656085,
          "mae": 0.1201295480132103,
          "mse": 0.022069061174988747,
          "risk_coverage": [
            [
              0.1,
              0.04177241399884224
            ],
            [
              0.25,
              0.10354705154895782
            ],
            [
              0.5,
              0.22622302174568176
            ],
            [
              0.75,
              0.44104763865470886
            ],
            [
              1.0,
              0.8716886639595032
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.988,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.968,
          "action_sensitivity_std": 0.771555301345178
        },
        "test_ood": {
          "n": 1500,
          "pearson": 0.9804787635803223,
          "spearman": 0.963075736110472,
          "auroc_top30_bad": 0.9998645502645502,
          "mae": 0.14861875772476196,
          "mse": 0.03562439978122711,
          "risk_coverage": [
            [
              0.1,
              0.04899836704134941
            ],
            [
              0.25,
              0.10057047754526138
            ],
            [
              0.5,
              0.2428198605775833
            ],
            [
              0.75,
              0.47888368368148804
            ],
            [
              1.0,
              0.8572618961334229
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.976,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.972,
          "action_sensitivity_std": 0.6383692811155509
        }
      }
    },
    "context": {
      "best_epoch": 58,
      "best_calib_loss": 0.13213102519512177,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.07132364809513092,
          "spearman": 0.10697292806589583,
          "auroc_top30_bad": 0.5559444444444445,
          "mae": 0.607104480266571,
          "mse": 0.7087852954864502,
          "risk_coverage": [
            [
              0.1,
              0.7772848606109619
            ],
            [
              0.25,
              0.7918233871459961
            ],
            [
              0.5,
              0.8028134107589722
            ],
            [
              0.75,
              0.8216592073440552
            ],
            [
              1.0,
              0.8511459827423096
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.7605,
          "action_sensitivity_std": 0.0
        },
        "calib": {
          "n": 1500,
          "pearson": 0.07479556649923325,
          "spearman": 0.04531843415690021,
          "auroc_top30_bad": 0.5244804232804233,
          "mae": 0.6432967782020569,
          "mse": 0.7168322205543518,
          "risk_coverage": [
            [
              0.1,
              0.8049054741859436
            ],
            [
              0.25,
              0.8447259664535522
            ],
            [
              0.5,
              0.8830885291099548
            ],
            [
              0.75,
              0.868764340877533
            ],
            [
              1.0,
              0.886215329170227
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.798,
          "action_sensitivity_std": 2.247831920581015e-10
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.012146446853876114,
          "spearman": 0.037650282467761254,
          "auroc_top30_bad": 0.5399619047619049,
          "mae": 0.6540459394454956,
          "mse": 0.862292468547821,
          "risk_coverage": [
            [
              0.1,
              0.9373429417610168
            ],
            [
              0.25,
              0.865666925907135
            ],
            [
              0.5,
              0.8516251444816589
            ],
            [
              0.75,
              0.8656431436538696
            ],
            [
              1.0,
              0.8716886639595032
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.817,
          "action_sensitivity_std": 0.0
        },
        "test_ood": {
          "n": 1500,
          "pearson": 0.08111518621444702,
          "spearman": 0.07140683360279787,
          "auroc_top30_bad": 0.5430222222222222,
          "mae": 0.6222392320632935,
          "mse": 0.6057013869285583,
          "risk_coverage": [
            [
              0.1,
              0.7031955718994141
            ],
            [
              0.25,
              0.7587317824363708
            ],
            [
              0.5,
              0.8077880144119263
            ],
            [
              0.75,
              0.8318182229995728
            ],
            [
              1.0,
              0.8572619557380676
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "simvla_pairwise_true_order_accuracy": 0.793,
          "action_sensitivity_std": 0.0
        }
      }
    },
    "action": {
      "best_epoch": 24,
      "best_calib_loss": 0.03132632002234459,
      "metrics": {
        "train": {
          "n": 6000,
          "pearson": 0.9442667365074158,
          "spearman": 0.7730514294287392,
          "auroc_top30_bad": 0.9712004629629629,
          "mae": 0.17505812644958496,
          "mse": 0.07143408060073853,
          "risk_coverage": [
            [
              0.1,
              0.2666296064853668
            ],
            [
              0.25,
              0.2943883538246155
            ],
            [
              0.5,
              0.34449559450149536
            ],
            [
              0.75,
              0.4582606256008148
            ],
            [
              1.0,
              0.8511459827423096
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.508,
          "expert_lt_simvla_seed0": 0.962,
          "simvla_pairwise_true_order_accuracy": 0.955,
          "action_sensitivity_std": 0.737717388524614
        },
        "calib": {
          "n": 1500,
          "pearson": 0.9284480810165405,
          "spearman": 0.7619758480732475,
          "auroc_top30_bad": 0.9773925925925926,
          "mae": 0.20754756033420563,
          "mse": 0.09296528995037079,
          "risk_coverage": [
            [
              0.1,
              0.3039554953575134
            ],
            [
              0.25,
              0.32733798027038574
            ],
            [
              0.5,
              0.3661723732948303
            ],
            [
              0.75,
              0.5005122423171997
            ],
            [
              1.0,
              0.886215329170227
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.508,
          "expert_lt_simvla_seed0": 1.0,
          "simvla_pairwise_true_order_accuracy": 0.976,
          "action_sensitivity_std": 0.7331745341458177
        },
        "test_id": {
          "n": 1500,
          "pearson": 0.9632457494735718,
          "spearman": 0.7510697718829132,
          "auroc_top30_bad": 0.9925820105820105,
          "mae": 0.16847285628318787,
          "mse": 0.05772848427295685,
          "risk_coverage": [
            [
              0.1,
              0.262119859457016
            ],
            [
              0.25,
              0.30318698287010193
            ],
            [
              0.5,
              0.33008161187171936
            ],
            [
              0.75,
              0.438763290643692
            ],
            [
              1.0,
              0.8716886639595032
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.492,
          "expert_lt_simvla_seed0": 0.988,
          "simvla_pairwise_true_order_accuracy": 0.971,
          "action_sensitivity_std": 0.8200042325911192
        },
        "test_ood": {
          "n": 1500,
          "pearson": 0.9379510879516602,
          "spearman": 0.7452113981922517,
          "auroc_top30_bad": 0.9998433862433862,
          "mae": 0.1930067092180252,
          "mse": 0.07322586327791214,
          "risk_coverage": [
            [
              0.1,
              0.3232209086418152
            ],
            [
              0.25,
              0.3356510102748871
            ],
            [
              0.5,
              0.34576940536499023
            ],
            [
              0.75,
              0.4759085774421692
            ],
            [
              1.0,
              0.8572619557380676
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.504,
          "expert_lt_simvla_seed0": 0.964,
          "simvla_pairwise_true_order_accuracy": 0.962,
          "action_sensitivity_std": 0.7229999260726995
        }
      }
    }
  }
}
```
