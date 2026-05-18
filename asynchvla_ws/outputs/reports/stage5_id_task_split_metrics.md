# Stage 5 Rater Metrics v2: id_task_split

- Train setting: `mixed`
- Epochs: 251
- Runtime: 62.4s
- Checkpoint dir: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/checkpoints/stage5/id_task_split`

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
  }
}
```

## Full-candidate metrics

| mode | part | n | pearson | spearman | AUROC | MAE | exp<perturb | exp<other | exp<seed0 | act_std_mean |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| full | train | 10000 | 0.9979 | 0.9961 | 0.9986 | 0.0541 | 1.0000 | 0.9990 | 1.0000 | 0.7976 |
| full | calib | 2500 | 0.9446 | 0.9508 | 0.9760 | 0.2252 | 0.9960 | 0.9880 | 1.0000 | 0.6104 |
| full | test_id | 2500 | 0.9344 | 0.9218 | 0.9696 | 0.2641 | 0.9960 | 0.9760 | 1.0000 | 0.5741 |
| context | train | 10000 | 0.4892 | 0.4159 | 0.7530 | 0.6112 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| context | calib | 2500 | 0.3933 | 0.4103 | 0.7821 | 0.6270 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| context | test_id | 2500 | 0.3242 | 0.2994 | 0.6922 | 0.6251 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| action | train | 10000 | 0.8884 | 0.8218 | 0.8906 | 0.2006 | 0.9730 | 0.5290 | 0.9480 | 0.7724 |
| action | calib | 2500 | 0.7869 | 0.7411 | 0.8453 | 0.3122 | 1.0000 | 0.4760 | 0.9720 | 0.7249 |
| action | test_id | 2500 | 0.7244 | 0.6162 | 0.7611 | 0.3458 | 0.9760 | 0.5160 | 0.9120 | 0.6385 |

## SimVLA-only metrics

| mode | part | n_sim | pearson | spearman | AUROC | pairwise | best-pred | seed0 | random | oracle | impr_over_seed0 | gap_to_oracle |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| full | train | 5 | 0.999287 | 0.9987 | 0.9994 | 0.9125 | 1.6262181 | 1.7064503 | 1.6993423 | 1.6231465 | 0.08023226 | 0.0030715466 |
| full | calib | 5 | 0.96132815 | 0.9481 | 0.9981 | 0.8508 | 1.6593032 | 1.7279956 | 1.7276641 | 1.6490723 | 0.068692446 | 0.010230899 |
| full | test_id | 5 | 0.94607884 | 0.8356 | 0.9855 | 0.7936 | 1.4175155 | 1.4820594 | 1.4708991 | 1.4014566 | 0.06454384 | 0.016058922 |
| context | train | 5 | 0.9656782 | 0.9883 | 0.9934 | 0.5000 | 1.7064503 | 1.7064503 | 1.6993423 | 1.6231465 | 0.0 | 0.08330381 |
| context | calib | 5 | 0.84116876 | 0.8572 | 0.9486 | 0.5000 | 1.7279956 | 1.7279956 | 1.7276641 | 1.6490723 | 0.0 | 0.078923345 |
| context | test_id | 5 | 0.7303713 | 0.7796 | 0.8970 | 0.5000 | 1.4820594 | 1.4820594 | 1.4708991 | 1.4014566 | 0.0 | 0.080602765 |
| action | train | 5 | 0.9990397 | 0.9987 | 0.9993 | 0.9115 | 1.6280164 | 1.7064503 | 1.6993423 | 1.6231465 | 0.07843399 | 0.0048698187 |
| action | calib | 5 | 0.98845834 | 0.9894 | 0.9981 | 0.8800 | 1.6549758 | 1.7279956 | 1.7276641 | 1.6490723 | 0.07301986 | 0.0059034824 |
| action | test_id | 5 | 0.977255 | 0.9243 | 0.9954 | 0.8300 | 1.4166486 | 1.4820594 | 1.4708991 | 1.4014566 | 0.06541073 | 0.015192032 |

## SimVLA-only switch proxy (reject highest-uncertainty)

| mode | part | reject% | accepted_mean | rejected_mean |
| --- | --- | ---: | ---: | ---: |
| full | train | 10 | 1.4531065 | 3.9154642 |
| full | train | 25 | 1.2505153 | 3.0458233 |
| full | train | 50 | 1.0113238 | 2.387361 |
| full | train | 75 | 0.7329088 | 2.0214868 |
| full | calib | 10 | 1.5893017 | 2.9729247 |
| full | calib | 25 | 1.4108166 | 2.6761823 |
| full | calib | 50 | 1.1841578 | 2.2711704 |
| full | calib | 75 | 0.93630266 | 1.9908887 |
| full | test_id | 10 | 1.2655272 | 3.3192453 |
| full | test_id | 25 | 1.122791 | 2.5129988 |
| full | test_id | 50 | 0.9940589 | 1.9477392 |
| full | test_id | 75 | 0.90171796 | 1.6602216 |
| context | train | 10 | 1.4672145 | 3.7884922 |
| context | train | 25 | 1.254057 | 3.035198 |
| context | train | 50 | 1.0164756 | 2.382209 |
| context | train | 75 | 0.7377488 | 2.0198734 |
| context | calib | 10 | 1.6393344 | 2.52263 |
| context | calib | 25 | 1.4531437 | 2.549471 |
| context | calib | 50 | 1.1928794 | 2.2624485 |
| context | calib | 75 | 1.0338179 | 1.9584529 |
| context | test_id | 10 | 1.2999963 | 3.0090237 |
| context | test_id | 25 | 1.1833577 | 2.331686 |
| context | test_id | 50 | 1.0437849 | 1.8980132 |
| context | test_id | 75 | 0.8568005 | 1.6751622 |
| action | train | 10 | 1.4533203 | 3.9135385 |
| action | train | 25 | 1.2504091 | 3.0461414 |
| action | train | 50 | 1.0112164 | 2.3874679 |
| action | train | 75 | 0.7323293 | 2.0216799 |
| action | calib | 10 | 1.5889727 | 2.9758856 |
| action | calib | 25 | 1.4106617 | 2.676645 |
| action | calib | 50 | 1.1520206 | 2.3033075 |
| action | calib | 75 | 0.87871826 | 2.0100427 |
| action | test_id | 10 | 1.2636862 | 3.3358152 |
| action | test_id | 25 | 1.1176513 | 2.5283854 |
| action | test_id | 50 | 0.9699171 | 1.971881 |
| action | test_id | 75 | 0.826248 | 1.6853245 |

## Best epoch / val loss per mode

```json
{
  "full": {
    "best_epoch": 241,
    "best_val_loss": 0.03422805666923523
  },
  "context": {
    "best_epoch": 110,
    "best_val_loss": 0.12884977459907532
  },
  "action": {
    "best_epoch": 160,
    "best_val_loss": 0.05945848301053047
  }
}
```

## Full metrics JSON

```json
{
  "split_id": "id_task_split",
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
    }
  },
  "epochs": 251,
  "models": {
    "full": {
      "best_epoch": 241,
      "best_val_loss": 0.03422805666923523,
      "input_dim": 1038,
      "metrics": {
        "train": {
          "n": 10000,
          "pearson": 0.9979084730148315,
          "spearman": 0.9960866325817579,
          "auroc_top30_bad": 0.9985899285714286,
          "mae": 0.0540509931743145,
          "mse": 0.005087703466415405,
          "risk_coverage": [
            [
              0.1,
              0.04779443517327309
            ],
            [
              0.25,
              0.18857212364673615
            ],
            [
              0.5,
              0.5938173532485962
            ],
            [
              0.75,
              0.9743573069572449
            ],
            [
              1.0,
              1.3900039196014404
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.999,
          "expert_lt_simvla_seed0": 1.0,
          "action_sensitivity_std_mean": 0.7976349325814497,
          "action_sensitivity_std_min": 0.32965535130089174,
          "simvla_only": {
            "pearson": 0.9992870092391968,
            "spearman": 0.9987355307413301,
            "auroc": 0.9994428571428571,
            "pairwise_acc": 0.9125,
            "best_seed": {
              "predicted_best": 1.6262180805206299,
              "seed0": 1.706450343132019,
              "random": 1.6993422508239746,
              "oracle_best": 1.6231465339660645,
              "gap_to_oracle": 0.0030715465545654297,
              "improvement_over_seed0": 0.08023226261138916
            },
            "risk_coverage": {
              "0.1": 0.5173107981681824,
              "0.25": 0.7329087853431702,
              "0.5": 1.0113238096237183,
              "0.75": 1.250515341758728,
              "1.0": 1.699342131614685
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4531065225601196,
                "rejected_mean": 3.915464162826538,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.250515341758728,
                "rejected_mean": 3.045823335647583,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0113238096237183,
                "rejected_mean": 2.3873610496520996,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.7329087853431702,
                "rejected_mean": 2.021486759185791,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "calib": {
          "n": 2500,
          "pearson": 0.9445512294769287,
          "spearman": 0.9507795878792229,
          "auroc_top30_bad": 0.9760487619047619,
          "mae": 0.2252279371023178,
          "mse": 0.10484936833381653,
          "risk_coverage": [
            [
              0.1,
              0.10805482417345047
            ],
            [
              0.25,
              0.2509222626686096
            ],
            [
              0.5,
              0.6733561754226685
            ],
            [
              0.75,
              1.0320911407470703
            ],
            [
              1.0,
              1.3786587715148926
            ]
          ],
          "expert_lt_perturb_large": 0.996,
          "expert_lt_other_task": 0.988,
          "expert_lt_simvla_seed0": 1.0,
          "action_sensitivity_std_mean": 0.6103682172869267,
          "action_sensitivity_std_min": 0.11804290035519785,
          "simvla_only": {
            "pearson": 0.9613281488418579,
            "spearman": 0.948067849771424,
            "auroc": 0.9980982857142857,
            "pairwise_acc": 0.8508,
            "best_seed": {
              "predicted_best": 1.6593031883239746,
              "seed0": 1.7279956340789795,
              "random": 1.7276641130447388,
              "oracle_best": 1.649072289466858,
              "gap_to_oracle": 0.0102308988571167,
              "improvement_over_seed0": 0.06869244575500488
            },
            "risk_coverage": {
              "0.1": 0.6539244651794434,
              "0.25": 0.936302661895752,
              "0.5": 1.1841578483581543,
              "0.75": 1.4108165502548218,
              "1.0": 1.7276641130447388
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.5893017053604126,
                "rejected_mean": 2.9729247093200684,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.4108165502548218,
                "rejected_mean": 2.676182270050049,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.1841578483581543,
                "rejected_mean": 2.2711703777313232,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.936302661895752,
                "rejected_mean": 1.9908887147903442,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_id": {
          "n": 2500,
          "pearson": 0.9344347715377808,
          "spearman": 0.9217812565970355,
          "auroc_top30_bad": 0.9695527619047619,
          "mae": 0.2641434669494629,
          "mse": 0.12223347276449203,
          "risk_coverage": [
            [
              0.1,
              0.11769794672727585
            ],
            [
              0.25,
              0.2686421275138855
            ],
            [
              0.5,
              0.6173638105392456
            ],
            [
              0.75,
              0.9077528715133667
            ],
            [
              1.0,
              1.2518880367279053
            ]
          ],
          "expert_lt_perturb_large": 0.996,
          "expert_lt_other_task": 0.976,
          "expert_lt_simvla_seed0": 1.0,
          "action_sensitivity_std_mean": 0.5740825475838673,
          "action_sensitivity_std_min": 0.09487416002543494,
          "simvla_only": {
            "pearson": 0.9460788369178772,
            "spearman": 0.835599228159506,
            "auroc": 0.9854537142857143,
            "pairwise_acc": 0.7936,
            "best_seed": {
              "predicted_best": 1.417515516281128,
              "seed0": 1.482059359550476,
              "random": 1.4708991050720215,
              "oracle_best": 1.401456594467163,
              "gap_to_oracle": 0.016058921813964844,
              "improvement_over_seed0": 0.06454384326934814
            },
            "risk_coverage": {
              "0.1": 0.7905685305595398,
              "0.25": 0.9017179608345032,
              "0.5": 0.9940589070320129,
              "0.75": 1.122791051864624,
              "1.0": 1.470898985862732
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.2655272483825684,
                "rejected_mean": 3.3192453384399414,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.122791051864624,
                "rejected_mean": 2.5129988193511963,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 0.9940589070320129,
                "rejected_mean": 1.9477392435073853,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.9017179608345032,
                "rejected_mean": 1.6602215766906738,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    },
    "context": {
      "best_epoch": 110,
      "best_val_loss": 0.12884977459907532,
      "input_dim": 968,
      "metrics": {
        "train": {
          "n": 10000,
          "pearson": 0.4892260432243347,
          "spearman": 0.4158840940210416,
          "auroc_top30_bad": 0.7530188095238096,
          "mae": 0.6112239360809326,
          "mse": 0.7948291301727295,
          "risk_coverage": [
            [
              0.1,
              0.7859430909156799
            ],
            [
              0.25,
              0.8767164349555969
            ],
            [
              0.5,
              1.0289077758789062
            ],
            [
              0.75,
              1.1657264232635498
            ],
            [
              1.0,
              1.3900039196014404
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 0.0,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.9656782150268555,
            "spearman": 0.9883462149526262,
            "auroc": 0.9934285714285713,
            "pairwise_acc": 0.5,
            "best_seed": {
              "predicted_best": 1.706450343132019,
              "seed0": 1.706450343132019,
              "random": 1.6993422508239746,
              "oracle_best": 1.6231465339660645,
              "gap_to_oracle": 0.08330380916595459,
              "improvement_over_seed0": 0.0
            },
            "risk_coverage": {
              "0.1": 0.5241422057151794,
              "0.25": 0.7377488017082214,
              "0.5": 1.0164755582809448,
              "0.75": 1.2540570497512817,
              "1.0": 1.699342131614685
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4672144651412964,
                "rejected_mean": 3.788492202758789,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.2540570497512817,
                "rejected_mean": 3.0351979732513428,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0164755582809448,
                "rejected_mean": 2.382209062576294,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.7377488017082214,
                "rejected_mean": 2.0198733806610107,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "calib": {
          "n": 2500,
          "pearson": 0.39334726333618164,
          "spearman": 0.41031243131242046,
          "auroc_top30_bad": 0.7821409523809524,
          "mae": 0.6269643902778625,
          "mse": 0.6915726661682129,
          "risk_coverage": [
            [
              0.1,
              0.8014701008796692
            ],
            [
              0.25,
              0.9535086154937744
            ],
            [
              0.5,
              1.0777033567428589
            ],
            [
              0.75,
              1.2188385725021362
            ],
            [
              1.0,
              1.378658652305603
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 0.0,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.8411687612533569,
            "spearman": 0.8572144331693645,
            "auroc": 0.948632380952381,
            "pairwise_acc": 0.5,
            "best_seed": {
              "predicted_best": 1.7279956340789795,
              "seed0": 1.7279956340789795,
              "random": 1.7276641130447388,
              "oracle_best": 1.649072289466858,
              "gap_to_oracle": 0.07892334461212158,
              "improvement_over_seed0": 0.0
            },
            "risk_coverage": {
              "0.1": 0.6950767636299133,
              "0.25": 1.0338178873062134,
              "0.5": 1.1928794384002686,
              "0.75": 1.4531437158584595,
              "1.0": 1.7276641130447388
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.6393344402313232,
                "rejected_mean": 2.522629976272583,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.4531437158584595,
                "rejected_mean": 2.549470901489258,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.1928794384002686,
                "rejected_mean": 2.26244854927063,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 1.0338178873062134,
                "rejected_mean": 1.9584529399871826,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_id": {
          "n": 2500,
          "pearson": 0.32418251037597656,
          "spearman": 0.29939837200304265,
          "auroc_top30_bad": 0.692152380952381,
          "mae": 0.625068724155426,
          "mse": 0.6580212116241455,
          "risk_coverage": [
            [
              0.1,
              0.8889057636260986
            ],
            [
              0.25,
              0.9522525668144226
            ],
            [
              0.5,
              1.031799077987671
            ],
            [
              0.75,
              1.1010152101516724
            ],
            [
              1.0,
              1.2518879175186157
            ]
          ],
          "expert_lt_perturb_large": 0.0,
          "expert_lt_other_task": 0.0,
          "expert_lt_simvla_seed0": 0.0,
          "action_sensitivity_std_mean": 0.0,
          "action_sensitivity_std_min": 0.0,
          "simvla_only": {
            "pearson": 0.7303712964057922,
            "spearman": 0.7795842858442493,
            "auroc": 0.8970057142857144,
            "pairwise_acc": 0.5,
            "best_seed": {
              "predicted_best": 1.482059359550476,
              "seed0": 1.482059359550476,
              "random": 1.4708991050720215,
              "oracle_best": 1.401456594467163,
              "gap_to_oracle": 0.08060276508331299,
              "improvement_over_seed0": 0.0
            },
            "risk_coverage": {
              "0.1": 0.6377904415130615,
              "0.25": 0.8568004965782166,
              "0.5": 1.0437848567962646,
              "0.75": 1.1833577156066895,
              "1.0": 1.470898985862732
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.299996256828308,
                "rejected_mean": 3.009023666381836,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.1833577156066895,
                "rejected_mean": 2.331686019897461,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.0437848567962646,
                "rejected_mean": 1.8980132341384888,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8568004965782166,
                "rejected_mean": 1.6751621961593628,
                "acceptance_rate": 0.25
              }
            }
          }
        }
      }
    },
    "action": {
      "best_epoch": 160,
      "best_val_loss": 0.05945848301053047,
      "input_dim": 70,
      "metrics": {
        "train": {
          "n": 10000,
          "pearson": 0.8884177207946777,
          "spearman": 0.8217723412084746,
          "auroc_top30_bad": 0.8906357142857144,
          "mae": 0.20059894025325775,
          "mse": 0.22343410551548004,
          "risk_coverage": [
            [
              0.1,
              0.5414233207702637
            ],
            [
              0.25,
              0.5265417695045471
            ],
            [
              0.5,
              0.6894495487213135
            ],
            [
              0.75,
              1.0039204359054565
            ],
            [
              1.0,
              1.3900039196014404
            ]
          ],
          "expert_lt_perturb_large": 0.973,
          "expert_lt_other_task": 0.529,
          "expert_lt_simvla_seed0": 0.948,
          "action_sensitivity_std_mean": 0.7723969186613322,
          "action_sensitivity_std_min": 0.36067857761350985,
          "simvla_only": {
            "pearson": 0.9990397095680237,
            "spearman": 0.9987016237799714,
            "auroc": 0.999348,
            "pairwise_acc": 0.9115,
            "best_seed": {
              "predicted_best": 1.6280163526535034,
              "seed0": 1.706450343132019,
              "random": 1.6993422508239746,
              "oracle_best": 1.6231465339660645,
              "gap_to_oracle": 0.004869818687438965,
              "improvement_over_seed0": 0.07843399047851562
            },
            "risk_coverage": {
              "0.1": 0.5183482766151428,
              "0.25": 0.7323293089866638,
              "0.5": 1.011216402053833,
              "0.75": 1.2504091262817383,
              "1.0": 1.699342131614685
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.4533202648162842,
                "rejected_mean": 3.9135384559631348,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.2504091262817383,
                "rejected_mean": 3.0461413860321045,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.011216402053833,
                "rejected_mean": 2.387467861175537,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.7323293089866638,
                "rejected_mean": 2.0216798782348633,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "calib": {
          "n": 2500,
          "pearson": 0.7868512272834778,
          "spearman": 0.7410942363008199,
          "auroc_top30_bad": 0.845336761904762,
          "mae": 0.3121599555015564,
          "mse": 0.34561610221862793,
          "risk_coverage": [
            [
              0.1,
              0.6901659369468689
            ],
            [
              0.25,
              0.7211593389511108
            ],
            [
              0.5,
              0.7974651455879211
            ],
            [
              0.75,
              1.0533430576324463
            ],
            [
              1.0,
              1.378658652305603
            ]
          ],
          "expert_lt_perturb_large": 1.0,
          "expert_lt_other_task": 0.476,
          "expert_lt_simvla_seed0": 0.972,
          "action_sensitivity_std_mean": 0.7249447635446716,
          "action_sensitivity_std_min": 0.3519838682119636,
          "simvla_only": {
            "pearson": 0.9884583353996277,
            "spearman": 0.9893522384334327,
            "auroc": 0.9980647619047619,
            "pairwise_acc": 0.88,
            "best_seed": {
              "predicted_best": 1.6549757719039917,
              "seed0": 1.7279956340789795,
              "random": 1.7276641130447388,
              "oracle_best": 1.649072289466858,
              "gap_to_oracle": 0.005903482437133789,
              "improvement_over_seed0": 0.07301986217498779
            },
            "risk_coverage": {
              "0.1": 0.6660110950469971,
              "0.25": 0.8787182569503784,
              "0.5": 1.1520205736160278,
              "0.75": 1.4106616973876953,
              "1.0": 1.7276641130447388
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.5889726877212524,
                "rejected_mean": 2.9758856296539307,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.4106616973876953,
                "rejected_mean": 2.676645040512085,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 1.1520205736160278,
                "rejected_mean": 2.30330753326416,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8787182569503784,
                "rejected_mean": 2.010042667388916,
                "acceptance_rate": 0.25
              }
            }
          }
        },
        "test_id": {
          "n": 2500,
          "pearson": 0.7244462966918945,
          "spearman": 0.6161520891507737,
          "auroc_top30_bad": 0.7611333333333333,
          "mae": 0.3458299934864044,
          "mse": 0.39398452639579773,
          "risk_coverage": [
            [
              0.1,
              0.5887282490730286
            ],
            [
              0.25,
              0.7725529670715332
            ],
            [
              0.5,
              0.8196659088134766
            ],
            [
              0.75,
              0.9448174238204956
            ],
            [
              1.0,
              1.2518879175186157
            ]
          ],
          "expert_lt_perturb_large": 0.976,
          "expert_lt_other_task": 0.516,
          "expert_lt_simvla_seed0": 0.912,
          "action_sensitivity_std_mean": 0.6384675945869633,
          "action_sensitivity_std_min": 0.2908930616832037,
          "simvla_only": {
            "pearson": 0.9772549867630005,
            "spearman": 0.9243378879602484,
            "auroc": 0.9954011428571429,
            "pairwise_acc": 0.83,
            "best_seed": {
              "predicted_best": 1.4166486263275146,
              "seed0": 1.482059359550476,
              "random": 1.4708991050720215,
              "oracle_best": 1.401456594467163,
              "gap_to_oracle": 0.015192031860351562,
              "improvement_over_seed0": 0.06541073322296143
            },
            "risk_coverage": {
              "0.1": 0.6817060708999634,
              "0.25": 0.8262479901313782,
              "0.5": 0.9699171185493469,
              "0.75": 1.117651343345642,
              "1.0": 1.4708991050720215
            },
            "switch_proxy": {
              "0.1": {
                "accepted_mean": 1.263686180114746,
                "rejected_mean": 3.335815191268921,
                "acceptance_rate": 0.9
              },
              "0.25": {
                "accepted_mean": 1.117651343345642,
                "rejected_mean": 2.5283854007720947,
                "acceptance_rate": 0.75
              },
              "0.5": {
                "accepted_mean": 0.9699171185493469,
                "rejected_mean": 1.9718810319900513,
                "acceptance_rate": 0.5
              },
              "0.75": {
                "accepted_mean": 0.8262479901313782,
                "rejected_mean": 1.6853245496749878,
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
    }
  },
  "runtime_seconds": 62.44533324241638
}
```
