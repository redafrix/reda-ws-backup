# Stage 5 Rater Metrics: stage5_debug

- Checkpoint dir: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage5_debug`

## Metrics JSON

```json
{
  "split_name": "stage5_debug",
  "parts": {
    "debug": 500
  },
  "models": {
    "full": {
      "best_epoch": 1,
      "best_calib_loss": 0.2063334584236145,
      "metrics": {
        "debug": {
          "n": 500,
          "pearson": 0.30977708101272583,
          "spearman": 0.3679486858686497,
          "auroc_top30_bad": 0.757104761904762,
          "mae": 1.0368460416793823,
          "mse": 1.9638832807540894,
          "risk_coverage": [
            [
              0.1,
              0.5235137939453125
            ],
            [
              0.25,
              0.6240549683570862
            ],
            [
              0.5,
              0.8267024159431458
            ],
            [
              0.75,
              1.0181852579116821
            ],
            [
              1.0,
              1.1125930547714233
            ]
          ],
          "expert_lt_perturb_large": 0.64,
          "expert_lt_other_task": 0.32,
          "expert_lt_simvla_seed0": 0.8,
          "action_sensitivity_std": 0.06039073843908728,
          "simvla_only": {
            "pearson": 0.5761356949806213,
            "spearman": 0.7616550664810636,
            "auroc": 0.8188952380952381,
            "pairwise_acc": 0.616,
            "best_seed": {
              "predicted_best": 1.5196861028671265,
              "seed0": 1.5280561447143555,
              "random": 1.5098998546600342,
              "oracle_best": 1.4491374492645264,
              "gap_to_oracle": 0.0705486536026001,
              "improvement_over_seed0": 0.008370041847229004
            },
            "risk_coverage": {
              "0.1": 0.3547170162200928,
              "0.25": 0.5867564082145691,
              "0.5": 1.076301097869873,
              "0.75": 1.3625751733779907,
              "1.0": 1.5098998546600342
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4576653242111206,
                "rejected_mean": 1.9800105094909668,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3625751733779907,
                "rejected_mean": 1.9471968412399292,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.076301097869873,
                "rejected_mean": 1.9434984922409058,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.5867564082145691,
                "rejected_mean": 1.8143408298492432,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    },
    "context": {
      "best_epoch": 2,
      "best_calib_loss": 0.22743940353393555,
      "metrics": {
        "debug": {
          "n": 500,
          "pearson": 0.3819194436073303,
          "spearman": 0.33173140947800195,
          "auroc_top30_bad": 0.697952380952381,
          "mae": 0.6966556310653687,
          "mse": 0.6789479851722717,
          "risk_coverage": [
            [
              0.1,
              0.5235137939453125
            ],
            [
              0.25,
              0.654375433921814
            ],
            [
              0.5,
              0.8774013519287109
            ],
            [
              0.75,
              1.015007495880127
            ],
            [
              1.0,
              1.1125930547714233
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.02,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std": 1.509803699244461e-09,
          "simvla_only": {
            "pearson": 0.8825082778930664,
            "spearman": 0.8162216291465896,
            "auroc": 0.8742857142857143,
            "pairwise_acc": 0.72,
            "best_seed": {
              "predicted_best": 1.5280561447143555,
              "seed0": 1.5280561447143555,
              "random": 1.5098998546600342,
              "oracle_best": 1.4491374492645264,
              "gap_to_oracle": 0.0789186954498291,
              "improvement_over_seed0": 0.0
            },
            "risk_coverage": {
              "0.1": 0.3547169864177704,
              "0.25": 0.6066813468933105,
              "0.5": 1.0466679334640503,
              "0.75": 1.3310658931732178,
              "1.0": 1.5098998546600342
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.431999683380127,
                "rejected_mean": 2.2110025882720947,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3310658931732178,
                "rejected_mean": 2.040724754333496,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0466679334640503,
                "rejected_mean": 1.9731316566467285,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.6066813468933105,
                "rejected_mean": 1.807769775390625,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    },
    "action": {
      "best_epoch": 2,
      "best_calib_loss": 0.04269938915967941,
      "metrics": {
        "debug": {
          "n": 500,
          "pearson": 0.9152733087539673,
          "spearman": 0.8586362087625488,
          "auroc_top30_bad": 0.9915047619047619,
          "mae": 0.33081939816474915,
          "mse": 0.16823190450668335,
          "risk_coverage": [
            [
              0.1,
              0.39406028389930725
            ],
            [
              0.25,
              0.3975195586681366
            ],
            [
              0.5,
              0.4402482807636261
            ],
            [
              0.75,
              0.7813682556152344
            ],
            [
              1.0,
              1.1125930547714233
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.5,
          "expert_lt_simvla_seed0": 0.88,
          "action_sensitivity_std": 0.5906544840764328,
          "simvla_only": {
            "pearson": 0.9247154593467712,
            "spearman": 0.9323365813853021,
            "auroc": 0.9605333333333332,
            "pairwise_acc": 0.8,
            "best_seed": {
              "predicted_best": 1.4639075994491577,
              "seed0": 1.5280561447143555,
              "random": 1.5098998546600342,
              "oracle_best": 1.4491374492645264,
              "gap_to_oracle": 0.014770150184631348,
              "improvement_over_seed0": 0.06414854526519775
            },
            "risk_coverage": {
              "0.1": 0.3572571873664856,
              "0.25": 0.5850107669830322,
              "0.5": 0.9741491079330444,
              "0.75": 1.2895711660385132,
              "1.0": 1.5098998546600342
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4574834108352661,
                "rejected_mean": 1.981648564338684,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.2895711660385132,
                "rejected_mean": 2.163891553878784,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 0.9741491079330444,
                "rejected_mean": 2.0456507205963135,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.5850107669830322,
                "rejected_mean": 1.8149166107177734,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    }
  }
}
```
