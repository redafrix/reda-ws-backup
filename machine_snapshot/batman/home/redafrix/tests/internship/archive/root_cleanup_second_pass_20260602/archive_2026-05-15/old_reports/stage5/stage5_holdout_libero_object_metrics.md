# Stage 5 Rater Metrics v2: holdout_libero_object

- Train setting: `mixed`
- Epochs: 251
- Runtime: 70.6s
- Checkpoint dir: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage5/holdout_libero_object`

## Split info

```json
{
  "train": {
    "rows": 10000,
    "contexts": 1000,
    "candidate_types": {
      "expert_action": 1000,
      "simvla_seed0": 1000,
      "simvla_seed1": 1000,
      "simvla_seed2": 1000,
      "simvla_seed3": 1000,
      "simvla_seed4": 1000,
      "perturb_small": 1000,
      "perturb_large": 1000,
      "same_task_far": 1000,
      "other_demo_or_other_task": 1000
    }
  },
  "calib": {
    "rows": 2500,
    "contexts": 250,
    "candidate_types": {
      "expert_action": 250,
      "simvla_seed0": 250,
      "simvla_seed1": 250,
      "simvla_seed2": 250,
      "simvla_seed3": 250,
      "simvla_seed4": 250,
      "perturb_small": 250,
      "perturb_large": 250,
      "same_task_far": 250,
      "other_demo_or_other_task": 250
    }
  },
  "test_id": {
    "rows": 2500,
    "contexts": 250,
    "candidate_types": {
      "expert_action": 250,
      "simvla_seed0": 250,
      "simvla_seed1": 250,
      "simvla_seed2": 250,
      "simvla_seed3": 250,
      "simvla_seed4": 250,
      "perturb_small": 250,
      "perturb_large": 250,
      "same_task_far": 250,
      "other_demo_or_other_task": 250
    }
  },
  "test_ood": {
    "rows": 2500,
    "contexts": 250,
    "candidate_types": {
      "expert_action": 250,
      "simvla_seed0": 250,
      "simvla_seed1": 250,
      "simvla_seed2": 250,
      "simvla_seed3": 250,
      "simvla_seed4": 250,
      "perturb_small": 250,
      "perturb_large": 250,
      "same_task_far": 250,
      "other_demo_or_other_task": 250
    }
  }
}
```

## Candidate type counts per part

```json
{
  "train": {
    "expert_action": 1000,
    "simvla_seed0": 1000,
    "simvla_seed1": 1000,
    "simvla_seed2": 1000,
    "simvla_seed3": 1000,
    "simvla_seed4": 1000,
    "perturb_small": 1000,
    "perturb_large": 1000,
    "same_task_far": 1000,
    "other_demo_or_other_task": 1000
  },
  "calib": {
    "expert_action": 250,
    "simvla_seed0": 250,
    "simvla_seed1": 250,
    "simvla_seed2": 250,
    "simvla_seed3": 250,
    "simvla_seed4": 250,
    "perturb_small": 250,
    "perturb_large": 250,
    "same_task_far": 250,
    "other_demo_or_other_task": 250
  },
  "test_id": {
    "expert_action": 250,
    "simvla_seed0": 250,
    "simvla_seed1": 250,
    "simvla_seed2": 250,
    "simvla_seed3": 250,
    "simvla_seed4": 250,
    "perturb_small": 250,
    "perturb_large": 250,
    "same_task_far": 250,
    "other_demo_or_other_task": 250
  },
  "test_ood": {
    "expert_action": 250,
    "simvla_seed0": 250,
    "simvla_seed1": 250,
    "simvla_seed2": 250,
    "simvla_seed3": 250,
    "simvla_seed4": 250,
    "perturb_small": 250,
    "perturb_large": 250,
    "same_task_far": 250,
    "other_demo_or_other_task": 250
  }
}
```

## Full-candidate metrics

| mode | part | n | pearson | spearman | AUROC | MAE | exp<perturb | exp<other | exp<seed0 | act_std_mean |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| full | train | 10000 | 0.9970 | 0.9924 | 0.9971 | 0.0721 | 1.0000 | 1.0000 | 1.0000 | 0.7806 |
| full | calib | 2500 | 0.9609 | 0.9463 | 0.9801 | 0.2518 | 0.9960 | 0.9760 | 1.0000 | 0.7180 |
| full | test_id | 2500 | 0.9428 | 0.9451 | 0.9661 | 0.2619 | 1.0000 | 0.9800 | 0.9960 | 0.5940 |
| full | test_ood | 2500 | 0.9165 | 0.9128 | 0.9369 | 0.2563 | 1.0000 | 0.9840 | 0.9920 | 0.6073 |
| context | train | 10000 | 0.5040 | 0.4284 | 0.7710 | 0.6307 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| context | calib | 2500 | 0.4569 | 0.3937 | 0.7734 | 0.7874 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| context | test_id | 2500 | 0.4259 | 0.3695 | 0.6801 | 0.6515 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| context | test_ood | 2500 | 0.1890 | 0.2244 | 0.6017 | 0.6061 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| action | train | 10000 | 0.9035 | 0.8182 | 0.8829 | 0.1998 | 0.9870 | 0.5080 | 0.9780 | 0.7776 |
| action | calib | 2500 | 0.8955 | 0.8115 | 0.8529 | 0.2773 | 0.9960 | 0.5280 | 0.9680 | 0.8660 |
| action | test_id | 2500 | 0.7127 | 0.6307 | 0.7108 | 0.3844 | 1.0000 | 0.5000 | 0.9480 | 0.7171 |
| action | test_ood | 2500 | 0.5752 | 0.5292 | 0.6775 | 0.3896 | 1.0000 | 0.4880 | 0.9960 | 0.6470 |

## SimVLA-only metrics

| mode | part | n_sim | pearson | spearman | AUROC | pairwise | best-pred | seed0 | random | oracle | impr_over_seed0 | gap_to_oracle |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| full | train | 5 | 0.9988083 | 0.9973 | 0.9993 | 0.8860 | 1.7079749 | 1.7944244 | 1.7850981 | 1.701594 | 0.086449504 | 0.0063809156 |
| full | calib | 5 | 0.985207 | 0.9793 | 0.9952 | 0.8516 | 2.003093 | 2.1044812 | 2.0798984 | 1.9888954 | 0.101388216 | 0.014197588 |
| full | test_id | 5 | 0.9495149 | 0.9303 | 0.9414 | 0.8264 | 1.5915052 | 1.6571431 | 1.6469765 | 1.5798976 | 0.065637946 | 0.011607528 |
| full | test_ood | 5 | 0.7905878 | 0.8046 | 0.8587 | 0.8132 | 1.6058952 | 1.6617512 | 1.6598133 | 1.592024 | 0.05585599 | 0.013871193 |
| context | train | 5 | 0.9431486 | 0.9859 | 0.9918 | 0.5001 | 1.794418 | 1.7944244 | 1.7850981 | 1.701594 | 6.4373016e-06 | 0.09282398 |
| context | calib | 5 | 0.91642547 | 0.9092 | 0.9823 | 0.5000 | 2.1044812 | 2.1044812 | 2.0798984 | 1.9888954 | 0.0 | 0.115585804 |
| context | test_id | 5 | 0.8918461 | 0.8420 | 0.8364 | 0.5004 | 1.6570551 | 1.6571431 | 1.6469765 | 1.5798976 | 8.7976456e-05 | 0.0771575 |
| context | test_ood | 5 | 0.70423293 | 0.6738 | 0.7416 | 0.5000 | 1.6617512 | 1.6617512 | 1.6598133 | 1.592024 | 0.0 | 0.06972718 |
| action | train | 5 | 0.9995085 | 0.9983 | 0.9998 | 0.9190 | 1.7061149 | 1.7944244 | 1.7850981 | 1.701594 | 0.08830953 | 0.004520893 |
| action | calib | 5 | 0.99475145 | 0.9937 | 0.9996 | 0.8964 | 1.9960959 | 2.1044812 | 2.0798984 | 1.9888954 | 0.108385324 | 0.0072004795 |
| action | test_id | 5 | 0.99119383 | 0.9898 | 0.9885 | 0.8596 | 1.5887554 | 1.6571431 | 1.6469765 | 1.5798976 | 0.06838775 | 0.008857727 |
| action | test_ood | 5 | 0.965026 | 0.9458 | 0.9506 | 0.8652 | 1.6032382 | 1.6617512 | 1.6598133 | 1.592024 | 0.058512926 | 0.011214256 |

## SimVLA-only switch proxy (reject highest-uncertainty)

| mode | part | reject% | accepted_mean | rejected_mean |
| --- | --- | ---: | ---: | ---: |
| full | train | 10 | 1.4900296 | 4.440715 |
| full | train | 25 | 1.3057647 | 3.223098 |
| full | train | 50 | 1.0845588 | 2.4856374 |
| full | train | 75 | 0.880763 | 2.086543 |
| full | calib | 10 | 1.8425293 | 4.216221 |
| full | calib | 25 | 1.547881 | 3.6725504 |
| full | calib | 50 | 1.2289747 | 2.930822 |
| full | calib | 75 | 0.90762424 | 2.4698231 |
| full | test_id | 10 | 1.4608028 | 3.3225412 |
| full | test_id | 25 | 1.3122789 | 2.6489305 |
| full | test_id | 50 | 1.0648236 | 2.2291293 |
| full | test_id | 75 | 0.67195904 | 1.9712894 |
| full | test_ood | 10 | 1.6017154 | 2.182695 |
| full | test_ood | 25 | 1.533041 | 2.03932 |
| full | test_ood | 50 | 1.4010117 | 1.9186149 |
| full | test_ood | 75 | 1.1666452 | 1.8238522 |
| context | train | 10 | 1.49247 | 4.41875 |
| context | train | 25 | 1.3087261 | 3.2142146 |
| context | train | 50 | 1.0905095 | 2.4796865 |
| context | train | 75 | 0.88906837 | 2.0837748 |
| context | calib | 10 | 1.8622402 | 4.0388203 |
| context | calib | 25 | 1.5950117 | 3.5314598 |
| context | calib | 50 | 1.2959015 | 2.863895 |
| context | calib | 75 | 0.92889965 | 2.4627464 |
| context | test_id | 10 | 1.4662086 | 3.2738876 |
| context | test_id | 25 | 1.3806921 | 2.444128 |
| context | test_id | 50 | 1.111725 | 2.1822278 |
| context | test_id | 75 | 0.67521083 | 1.9702077 |
| context | test_ood | 10 | 1.6291372 | 1.9358985 |
| context | test_ood | 25 | 1.570887 | 1.9260238 |
| context | test_ood | 50 | 1.4229139 | 1.8967127 |
| context | test_ood | 75 | 1.183735 | 1.8181677 |
| action | train | 10 | 1.4899627 | 4.4413176 |
| action | train | 25 | 1.3051956 | 3.2248054 |
| action | train | 50 | 1.0841758 | 2.4860203 |
| action | train | 75 | 0.8803763 | 2.086672 |
| action | calib | 10 | 1.8418514 | 4.2223215 |
| action | calib | 25 | 1.5439537 | 3.6843083 |
| action | calib | 50 | 1.2212381 | 2.9385586 |
| action | calib | 75 | 0.87651455 | 2.480171 |
| action | test_id | 10 | 1.4603863 | 3.3262892 |
| action | test_id | 25 | 1.3025379 | 2.6780913 |
| action | test_id | 50 | 1.0240992 | 2.2698536 |
| action | test_id | 75 | 0.6572394 | 1.9761853 |
| action | test_ood | 10 | 1.591064 | 2.2785563 |
| action | test_ood | 25 | 1.5188162 | 2.081903 |
| action | test_ood | 50 | 1.368898 | 1.9507285 |
| action | test_ood | 75 | 1.1057502 | 1.8441072 |

## Best epoch / val loss per mode

```json
{
  "full": {
    "best_epoch": 218,
    "best_val_loss": 0.039050403982400894
  },
  "context": {
    "best_epoch": 15,
    "best_val_loss": 0.1687949001789093
  },
  "action": {
    "best_epoch": 231,
    "best_val_loss": 0.04827592149376869
  }
}
```

## Full metrics JSON

```json
{
  "split_id": "holdout_libero_object",
  "train_setting": "mixed",
  "split_info": {
    "train": {
      "rows": 10000,
      "contexts": 1000,
      "candidate_types": {
        "expert_action": 1000,
        "simvla_seed0": 1000,
        "simvla_seed1": 1000,
        "simvla_seed2": 1000,
        "simvla_seed3": 1000,
        "simvla_seed4": 1000,
        "perturb_small": 1000,
        "perturb_large": 1000,
        "same_task_far": 1000,
        "other_demo_or_other_task": 1000
      }
    },
    "calib": {
      "rows": 2500,
      "contexts": 250,
      "candidate_types": {
        "expert_action": 250,
        "simvla_seed0": 250,
        "simvla_seed1": 250,
        "simvla_seed2": 250,
        "simvla_seed3": 250,
        "simvla_seed4": 250,
        "perturb_small": 250,
        "perturb_large": 250,
        "same_task_far": 250,
        "other_demo_or_other_task": 250
      }
    },
    "test_id": {
      "rows": 2500,
      "contexts": 250,
      "candidate_types": {
        "expert_action": 250,
        "simvla_seed0": 250,
        "simvla_seed1": 250,
        "simvla_seed2": 250,
        "simvla_seed3": 250,
        "simvla_seed4": 250,
        "perturb_small": 250,
        "perturb_large": 250,
        "same_task_far": 250,
        "other_demo_or_other_task": 250
      }
    },
    "test_ood": {
      "rows": 2500,
      "contexts": 250,
      "candidate_types": {
        "expert_action": 250,
        "simvla_seed0": 250,
        "simvla_seed1": 250,
        "simvla_seed2": 250,
        "simvla_seed3": 250,
        "simvla_seed4": 250,
        "perturb_small": 250,
        "perturb_large": 250,
        "same_task_far": 250,
        "other_demo_or_other_task": 250
      }
    }
  },
  "epochs": 251,
  "models": {
    "full": {
      "best_epoch": 218,
      "best_val_loss": 0.039050403982400894,
      "input_dim": 1038,
      "metrics": {
        "train": {
          "n": 10000,
          "pearson": 0.9970053434371948,
          "spearman": 0.9923582893626922,
          "auroc_top30_bad": 0.9971436428571429,
          "mae": 0.07208742946386337,
          "mse": 0.009240236133337021,
          "risk_coverage": [
            [
              0.1,
              0.0772714838385582
            ],
            [
              0.25,
              0.20093917846679688
            ],
            [
              0.5,
              0.6194016337394714
            ],
            [
              0.75,
              0.9882450103759766
            ],
            [
              1.0,
              1.4164187908172607
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 1.0,
          "expert_lt_simvla_seed0": 1.0,
          "action_sensitivity_std_mean": 0.780610954795896,
          "action_sensitivity_std_min": 0.38874610675618737,
          "simvla_only": {
            "pearson": 0.9988083243370056,
            "spearman": 0.9973157561552776,
            "auroc": 0.999271619047619,
            "pairwise_acc": 0.886,
            "best_seed": {
              "predicted_best": 1.707974910736084,
              "seed0": 1.7944244146347046,
              "random": 1.7850980758666992,
              "oracle_best": 1.7015939950942993,
              "gap_to_oracle": 0.006380915641784668,
              "improvement_over_seed0": 0.0864495038986206
            },
            "risk_coverage": {
              "0.1": 0.7248267531394958,
              "0.25": 0.8807629942893982,
              "0.5": 1.0845588445663452,
              "0.75": 1.3057646751403809,
              "1.0": 1.7850980758666992
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4900295734405518,
                "rejected_mean": 4.4407148361206055,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3057646751403809,
                "rejected_mean": 3.223098039627075,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0845588445663452,
                "rejected_mean": 2.4856374263763428,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8807629942893982,
                "rejected_mean": 2.086543083190918,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "calib": {
          "n": 2500,
          "pearson": 0.9609378576278687,
          "spearman": 0.9463438113272584,
          "auroc_top30_bad": 0.9800929523809523,
          "mae": 0.2517644464969635,
          "mse": 0.12333271652460098,
          "risk_coverage": [
            [
              0.1,
              0.13930712640285492
            ],
            [
              0.25,
              0.2661813795566559
            ],
            [
              0.5,
              0.6161318421363831
            ],
            [
              0.75,
              1.0258758068084717
            ],
            [
              1.0,
              1.5154402256011963
            ]
          ],
          "expert_lt_perturb_large": 0.996,
          "expert_lt_other_task": 0.976,
          "expert_lt_simvla_seed0": 1.0,
          "action_sensitivity_std_mean": 0.7180048471427224,
          "action_sensitivity_std_min": 0.16267853323725398,
          "simvla_only": {
            "pearson": 0.9852070212364197,
            "spearman": 0.9792993208955655,
            "auroc": 0.9952487619047619,
            "pairwise_acc": 0.8516,
            "best_seed": {
              "predicted_best": 2.0030930042266846,
              "seed0": 2.1044812202453613,
              "random": 2.0798983573913574,
              "oracle_best": 1.9888954162597656,
              "gap_to_oracle": 0.014197587966918945,
              "improvement_over_seed0": 0.10138821601867676
            },
            "risk_coverage": {
              "0.1": 0.6288800835609436,
              "0.25": 0.9076242446899414,
              "0.5": 1.22897469997406,
              "0.75": 1.547881007194519,
              "1.0": 2.0798983573913574
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.842529296875,
                "rejected_mean": 4.216220855712891,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.547881007194519,
                "rejected_mean": 3.6725504398345947,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.22897469997406,
                "rejected_mean": 2.9308218955993652,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.9076242446899414,
                "rejected_mean": 2.469823122024536,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_id": {
          "n": 2500,
          "pearson": 0.9427591562271118,
          "spearman": 0.9450533826930779,
          "auroc_top30_bad": 0.9661192380952383,
          "mae": 0.2618516981601715,
          "mse": 0.11730417609214783,
          "risk_coverage": [
            [
              0.1,
              0.14240892231464386
            ],
            [
              0.25,
              0.2369774878025055
            ],
            [
              0.5,
              0.6563688516616821
            ],
            [
              0.75,
              1.0446569919586182
            ],
            [
              1.0,
              1.4041494131088257
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.98,
          "expert_lt_simvla_seed0": 0.996,
          "action_sensitivity_std_mean": 0.594000288635715,
          "action_sensitivity_std_min": 0.2056575555212905,
          "simvla_only": {
            "pearson": 0.9495149254798889,
            "spearman": 0.930261623207439,
            "auroc": 0.941424761904762,
            "pairwise_acc": 0.8264,
            "best_seed": {
              "predicted_best": 1.5915051698684692,
              "seed0": 1.6571431159973145,
              "random": 1.6469764709472656,
              "oracle_best": 1.5798976421356201,
              "gap_to_oracle": 0.011607527732849121,
              "improvement_over_seed0": 0.06563794612884521
            },
            "risk_coverage": {
              "0.1": 0.4874306321144104,
              "0.25": 0.6719590425491333,
              "0.5": 1.0648236274719238,
              "0.75": 1.3122788667678833,
              "1.0": 1.6469765901565552
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4608027935028076,
                "rejected_mean": 3.3225412368774414,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3122788667678833,
                "rejected_mean": 2.648930549621582,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0648236274719238,
                "rejected_mean": 2.2291293144226074,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.6719590425491333,
                "rejected_mean": 1.9712893962860107,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_ood": {
          "n": 2500,
          "pearson": 0.916512668132782,
          "spearman": 0.9127972146863454,
          "auroc_top30_bad": 0.9369127619047619,
          "mae": 0.25633832812309265,
          "mse": 0.1198132187128067,
          "risk_coverage": [
            [
              0.1,
              0.12732386589050293
            ],
            [
              0.25,
              0.26996850967407227
            ],
            [
              0.5,
              0.8188950419425964
            ],
            [
              0.75,
              1.146715521812439
            ],
            [
              1.0,
              1.419131875038147
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.984,
          "expert_lt_simvla_seed0": 0.992,
          "action_sensitivity_std_mean": 0.6072976687734574,
          "action_sensitivity_std_min": 0.24590561167444558,
          "simvla_only": {
            "pearson": 0.7905877828598022,
            "spearman": 0.804627648401695,
            "auroc": 0.8587215238095238,
            "pairwise_acc": 0.8132,
            "best_seed": {
              "predicted_best": 1.6058951616287231,
              "seed0": 1.6617511510849,
              "random": 1.6598132848739624,
              "oracle_best": 1.5920239686965942,
              "gap_to_oracle": 0.013871192932128906,
              "improvement_over_seed0": 0.05585598945617676
            },
            "risk_coverage": {
              "0.1": 0.8940817713737488,
              "0.25": 1.1666451692581177,
              "0.5": 1.4010117053985596,
              "0.75": 1.533041000366211,
              "1.0": 1.6598132848739624
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.6017154455184937,
                "rejected_mean": 2.182694911956787,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.533041000366211,
                "rejected_mean": 2.0393199920654297,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.4010117053985596,
                "rejected_mean": 1.9186148643493652,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 1.1666451692581177,
                "rejected_mean": 1.8238521814346313,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    },
    "context": {
      "best_epoch": 15,
      "best_val_loss": 0.1687949001789093,
      "input_dim": 968,
      "metrics": {
        "train": {
          "n": 10000,
          "pearson": 0.5039600133895874,
          "spearman": 0.4283743512365183,
          "auroc_top30_bad": 0.7710072857142857,
          "mae": 0.6307147741317749,
          "mse": 0.9684471487998962,
          "risk_coverage": [
            [
              0.1,
              0.8248826861381531
            ],
            [
              0.25,
              0.9159193634986877
            ],
            [
              0.5,
              1.036048173904419
            ],
            [
              0.75,
              1.168327808380127
            ],
            [
              1.0,
              1.4164187908172607
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 5.462855929083633e-11,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.9431486129760742,
            "spearman": 0.9859003337130245,
            "auroc": 0.9918466666666667,
            "pairwise_acc": 0.5001,
            "best_seed": {
              "predicted_best": 1.7944179773330688,
              "seed0": 1.7944244146347046,
              "random": 1.7850980758666992,
              "oracle_best": 1.7015939950942993,
              "gap_to_oracle": 0.09282398223876953,
              "improvement_over_seed0": 6.4373016357421875e-06
            },
            "risk_coverage": {
              "0.1": 0.749329149723053,
              "0.25": 0.8890683650970459,
              "0.5": 1.0905095338821411,
              "0.75": 1.3087260723114014,
              "1.0": 1.7850980758666992
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4924700260162354,
                "rejected_mean": 4.418749809265137,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3087260723114014,
                "rejected_mean": 3.214214563369751,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0905095338821411,
                "rejected_mean": 2.4796864986419678,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8890683650970459,
                "rejected_mean": 2.0837748050689697,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "calib": {
          "n": 2500,
          "pearson": 0.45687225461006165,
          "spearman": 0.3936626593971711,
          "auroc_top30_bad": 0.773432761904762,
          "mae": 0.7874257564544678,
          "mse": 1.0458840131759644,
          "risk_coverage": [
            [
              0.1,
              0.7770145535469055
            ],
            [
              0.25,
              0.868464469909668
            ],
            [
              0.5,
              1.0883443355560303
            ],
            [
              0.75,
              1.2720458507537842
            ],
            [
              1.0,
              1.5154402256011963
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 1.430511474609375e-10,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.9164254665374756,
            "spearman": 0.9091807868109595,
            "auroc": 0.9822628571428571,
            "pairwise_acc": 0.5,
            "best_seed": {
              "predicted_best": 2.1044812202453613,
              "seed0": 2.1044812202453613,
              "random": 2.0798983573913574,
              "oracle_best": 1.9888954162597656,
              "gap_to_oracle": 0.1155858039855957,
              "improvement_over_seed0": 0.0
            },
            "risk_coverage": {
              "0.1": 0.801540195941925,
              "0.25": 0.9288996458053589,
              "0.5": 1.2959015369415283,
              "0.75": 1.5950117111206055,
              "1.0": 2.0798983573913574
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.862240195274353,
                "rejected_mean": 4.038820266723633,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.5950117111206055,
                "rejected_mean": 3.5314598083496094,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.2959015369415283,
                "rejected_mean": 2.8638949394226074,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.9288996458053589,
                "rejected_mean": 2.4627463817596436,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_id": {
          "n": 2500,
          "pearson": 0.4259342551231384,
          "spearman": 0.3694798038207132,
          "auroc_top30_bad": 0.6800918095238095,
          "mae": 0.6514769792556763,
          "mse": 0.8042439222335815,
          "risk_coverage": [
            [
              0.1,
              0.7899407744407654
            ],
            [
              0.25,
              0.8745449185371399
            ],
            [
              0.5,
              1.1040555238723755
            ],
            [
              0.75,
              1.257516622543335
            ],
            [
              1.0,
              1.4041494131088257
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 1.430511474609375e-10,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.8918461203575134,
            "spearman": 0.841981505018018,
            "auroc": 0.8363885714285715,
            "pairwise_acc": 0.5004,
            "best_seed": {
              "predicted_best": 1.657055139541626,
              "seed0": 1.6571431159973145,
              "random": 1.6469764709472656,
              "oracle_best": 1.5798976421356201,
              "gap_to_oracle": 0.07715749740600586,
              "improvement_over_seed0": 8.797645568847656e-05
            },
            "risk_coverage": {
              "0.1": 0.5293142199516296,
              "0.25": 0.6752108335494995,
              "0.5": 1.1117249727249146,
              "0.75": 1.3806921243667603,
              "1.0": 1.6469765901565552
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.466208577156067,
                "rejected_mean": 3.2738876342773438,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3806921243667603,
                "rejected_mean": 2.4441280364990234,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.1117249727249146,
                "rejected_mean": 2.182227849960327,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.6752108335494995,
                "rejected_mean": 1.970207691192627,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_ood": {
          "n": 2500,
          "pearson": 0.18904122710227966,
          "spearman": 0.22442155178616272,
          "auroc_top30_bad": 0.6016990476190476,
          "mae": 0.6061264276504517,
          "mse": 0.6738530397415161,
          "risk_coverage": [
            [
              0.1,
              0.9829366207122803
            ],
            [
              0.25,
              1.1639249324798584
            ],
            [
              0.5,
              1.2985032796859741
            ],
            [
              0.75,
              1.3752679824829102
            ],
            [
              1.0,
              1.419131875038147
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 0.0,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.704232931137085,
            "spearman": 0.6738483917184919,
            "auroc": 0.7416228571428571,
            "pairwise_acc": 0.5,
            "best_seed": {
              "predicted_best": 1.6617511510849,
              "seed0": 1.6617511510849,
              "random": 1.6598132848739624,
              "oracle_best": 1.5920239686965942,
              "gap_to_oracle": 0.06972718238830566,
              "improvement_over_seed0": 0.0
            },
            "risk_coverage": {
              "0.1": 0.897051990032196,
              "0.25": 1.1837350130081177,
              "0.5": 1.422913908958435,
              "0.75": 1.5708869695663452,
              "1.0": 1.6598132848739624
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.6291371583938599,
                "rejected_mean": 1.9358985424041748,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.5708869695663452,
                "rejected_mean": 1.9260238409042358,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.422913908958435,
                "rejected_mean": 1.8967126607894897,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 1.1837350130081177,
                "rejected_mean": 1.8181676864624023,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    },
    "action": {
      "best_epoch": 231,
      "best_val_loss": 0.04827592149376869,
      "input_dim": 70,
      "metrics": {
        "train": {
          "n": 10000,
          "pearson": 0.9034677743911743,
          "spearman": 0.8182252593564472,
          "auroc_top30_bad": 0.8829434285714285,
          "mae": 0.199844628572464,
          "mse": 0.21959318220615387,
          "risk_coverage": [
            [
              0.1,
              0.5241652727127075
            ],
            [
              0.25,
              0.5417160987854004
            ],
            [
              0.5,
              0.7136615514755249
            ],
            [
              0.75,
              1.0137447118759155
            ],
            [
              1.0,
              1.4164189100265503
            ]
          ],
          "expert_lt_perturb_large": 0.987,
          "expert_lt_other_task": 0.508,
          "expert_lt_simvla_seed0": 0.978,
          "action_sensitivity_std_mean": 0.777613300495053,
          "action_sensitivity_std_min": 0.36285153478977245,
          "simvla_only": {
            "pearson": 0.9995085000991821,
            "spearman": 0.9983166861324656,
            "auroc": 0.9997809523809523,
            "pairwise_acc": 0.919,
            "best_seed": {
              "predicted_best": 1.7061148881912231,
              "seed0": 1.7944244146347046,
              "random": 1.7850980758666992,
              "oracle_best": 1.7015939950942993,
              "gap_to_oracle": 0.004520893096923828,
              "improvement_over_seed0": 0.08830952644348145
            },
            "risk_coverage": {
              "0.1": 0.7277416586875916,
              "0.25": 0.8803762793540955,
              "0.5": 1.0841758251190186,
              "0.75": 1.3051955699920654,
              "1.0": 1.7850980758666992
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4899626970291138,
                "rejected_mean": 4.441317558288574,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3051955699920654,
                "rejected_mean": 3.2248053550720215,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0841758251190186,
                "rejected_mean": 2.48602032661438,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8803762793540955,
                "rejected_mean": 2.086672067642212,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "calib": {
          "n": 2500,
          "pearson": 0.8955245018005371,
          "spearman": 0.8115070336941125,
          "auroc_top30_bad": 0.8528982857142857,
          "mae": 0.27731773257255554,
          "mse": 0.2820695638656616,
          "risk_coverage": [
            [
              0.1,
              0.5246310830116272
            ],
            [
              0.25,
              0.6058406233787537
            ],
            [
              0.5,
              0.7022333145141602
            ],
            [
              0.75,
              1.0346696376800537
            ],
            [
              1.0,
              1.5154402256011963
            ]
          ],
          "expert_lt_perturb_large": 0.996,
          "expert_lt_other_task": 0.528,
          "expert_lt_simvla_seed0": 0.968,
          "action_sensitivity_std_mean": 0.8659850998362107,
          "action_sensitivity_std_min": 0.3736652857347031,
          "simvla_only": {
            "pearson": 0.9947514533996582,
            "spearman": 0.9936706929092436,
            "auroc": 0.9996099047619048,
            "pairwise_acc": 0.8964,
            "best_seed": {
              "predicted_best": 1.996095895767212,
              "seed0": 2.1044812202453613,
              "random": 2.0798983573913574,
              "oracle_best": 1.9888954162597656,
              "gap_to_oracle": 0.007200479507446289,
              "improvement_over_seed0": 0.10838532447814941
            },
            "risk_coverage": {
              "0.1": 0.6350939273834229,
              "0.25": 0.8765145540237427,
              "0.5": 1.221238136291504,
              "0.75": 1.5439536571502686,
              "1.0": 2.0798983573913574
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.8418513536453247,
                "rejected_mean": 4.222321510314941,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.5439536571502686,
                "rejected_mean": 3.6843082904815674,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.221238136291504,
                "rejected_mean": 2.938558578491211,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8765145540237427,
                "rejected_mean": 2.480170965194702,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_id": {
          "n": 2500,
          "pearson": 0.7126716375350952,
          "spearman": 0.6307110256860439,
          "auroc_top30_bad": 0.7108445714285714,
          "mae": 0.3844043016433716,
          "mse": 0.5395169854164124,
          "risk_coverage": [
            [
              0.1,
              0.5582518577575684
            ],
            [
              0.25,
              0.6504276394844055
            ],
            [
              0.5,
              0.8937755823135376
            ],
            [
              0.75,
              1.0973567962646484
            ],
            [
              1.0,
              1.4041494131088257
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.5,
          "expert_lt_simvla_seed0": 0.948,
          "action_sensitivity_std_mean": 0.7171211917563679,
          "action_sensitivity_std_min": 0.33604317528915617,
          "simvla_only": {
            "pearson": 0.9911938309669495,
            "spearman": 0.9898046398749696,
            "auroc": 0.9885257142857143,
            "pairwise_acc": 0.8596,
            "best_seed": {
              "predicted_best": 1.5887553691864014,
              "seed0": 1.6571431159973145,
              "random": 1.6469764709472656,
              "oracle_best": 1.5798976421356201,
              "gap_to_oracle": 0.00885772705078125,
              "improvement_over_seed0": 0.06838774681091309
            },
            "risk_coverage": {
              "0.1": 0.4186937212944031,
              "0.25": 0.6572393774986267,
              "0.5": 1.0240992307662964,
              "0.75": 1.3025379180908203,
              "1.0": 1.6469765901565552
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4603862762451172,
                "rejected_mean": 3.326289176940918,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.3025379180908203,
                "rejected_mean": 2.678091287612915,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0240992307662964,
                "rejected_mean": 2.2698535919189453,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.6572393774986267,
                "rejected_mean": 1.9761853218078613,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_ood": {
          "n": 2500,
          "pearson": 0.5752158164978027,
          "spearman": 0.5291733072803118,
          "auroc_top30_bad": 0.6775066666666667,
          "mae": 0.38963669538497925,
          "mse": 0.5545717477798462,
          "risk_coverage": [
            [
              0.1,
              0.6207029819488525
            ],
            [
              0.25,
              0.8818138837814331
            ],
            [
              0.5,
              0.9852472543716431
            ],
            [
              0.75,
              1.2228877544403076
            ],
            [
              1.0,
              1.419131875038147
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.488,
          "expert_lt_simvla_seed0": 0.996,
          "action_sensitivity_std_mean": 0.6470296027985337,
          "action_sensitivity_std_min": 0.43214662331785825,
          "simvla_only": {
            "pearson": 0.9650260210037231,
            "spearman": 0.9458248213918858,
            "auroc": 0.9506133333333333,
            "pairwise_acc": 0.8652,
            "best_seed": {
              "predicted_best": 1.6032382249832153,
              "seed0": 1.6617511510849,
              "random": 1.6598132848739624,
              "oracle_best": 1.5920239686965942,
              "gap_to_oracle": 0.011214256286621094,
              "improvement_over_seed0": 0.05851292610168457
            },
            "risk_coverage": {
              "0.1": 0.8518918752670288,
              "0.25": 1.1057502031326294,
              "0.5": 1.3688980340957642,
              "0.75": 1.5188162326812744,
              "1.0": 1.6598132848739624
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.5910639762878418,
                "rejected_mean": 2.2785563468933105,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.5188162326812744,
                "rejected_mean": 2.0819029808044434,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.3688980340957642,
                "rejected_mean": 1.9507285356521606,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 1.1057502031326294,
                "rejected_mean": 1.8441071510314941,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    }
  },
  "candidate_type_counts": {
    "train": {
      "expert_action": 1000,
      "simvla_seed0": 1000,
      "simvla_seed1": 1000,
      "simvla_seed2": 1000,
      "simvla_seed3": 1000,
      "simvla_seed4": 1000,
      "perturb_small": 1000,
      "perturb_large": 1000,
      "same_task_far": 1000,
      "other_demo_or_other_task": 1000
    },
    "calib": {
      "expert_action": 250,
      "simvla_seed0": 250,
      "simvla_seed1": 250,
      "simvla_seed2": 250,
      "simvla_seed3": 250,
      "simvla_seed4": 250,
      "perturb_small": 250,
      "perturb_large": 250,
      "same_task_far": 250,
      "other_demo_or_other_task": 250
    },
    "test_id": {
      "expert_action": 250,
      "simvla_seed0": 250,
      "simvla_seed1": 250,
      "simvla_seed2": 250,
      "simvla_seed3": 250,
      "simvla_seed4": 250,
      "perturb_small": 250,
      "perturb_large": 250,
      "same_task_far": 250,
      "other_demo_or_other_task": 250
    },
    "test_ood": {
      "expert_action": 250,
      "simvla_seed0": 250,
      "simvla_seed1": 250,
      "simvla_seed2": 250,
      "simvla_seed3": 250,
      "simvla_seed4": 250,
      "perturb_small": 250,
      "perturb_large": 250,
      "same_task_far": 250,
      "other_demo_or_other_task": 250
    }
  },
  "runtime_seconds": 70.61832070350647
}
```
