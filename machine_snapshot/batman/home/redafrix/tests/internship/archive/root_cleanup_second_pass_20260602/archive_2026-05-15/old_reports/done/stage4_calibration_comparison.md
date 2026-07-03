# Stage 4 Calibration Comparison

Methods: global 90% residual conformal; candidate-type conditional residual conformal for analysis; predicted-error-bin residual conformal using 3 calibration quantile bins. Quantile rater was not trained in this pilot; the three conformal variants are the implemented calibration comparison.

```json
[
  {
    "split": "id_task_split",
    "global_eta": 0.26254484653472904,
    "type_eta": {
      "expert_action": 0,
      "other_demo_or_other_task": 0.24775455743074415,
      "perturb_large": 0.29898470640182495,
      "perturb_small": 0.0993449792265892,
      "same_task_far": 0.1646953225135803,
      "simvla_seed0": 0.5646445512771605
    },
    "bin_eta": [
      [
        0.0002508473116904497,
        0.36008300095796586,
        0.11505551934242256
      ],
      [
        0.36008300095796586,
        1.1843257236480713,
        0.13141900300979614
      ],
      [
        1.1843257236480713,
        3.8645057678222656,
        0.4612156867980959
      ]
    ],
    "parts": {
      "train": {
        "n": 6000,
        "overall": {
          "global": 0.997,
          "type": 0.9756666666666667,
          "bin": 0.9676666666666667
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.005743950583088008
          },
          "other_demo_or_other_task": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 0.961,
            "mean_true": 0.7768446874022484,
            "mean_pred": 0.7419739350676536
          },
          "perturb_large": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 1.9188841239213943,
            "mean_pred": 1.8917728234529496
          },
          "perturb_small": {
            "n": 1000,
            "global": 1.0,
            "type": 0.859,
            "bin": 0.892,
            "mean_true": 0.2554228471666575,
            "mean_pred": 0.21013580030808227
          },
          "same_task_far": {
            "n": 1000,
            "global": 1.0,
            "type": 0.995,
            "bin": 0.964,
            "mean_true": 0.6481495115607977,
            "mean_pred": 0.614046740746533
          },
          "simvla_seed0": {
            "n": 1000,
            "global": 0.982,
            "type": 1.0,
            "bin": 0.989,
            "mean_true": 1.7633786560893059,
            "mean_pred": 1.7283748781234025
          }
        }
      },
      "calib": {
        "n": 1500,
        "overall": {
          "global": 0.9,
          "type": 0.9166666666666666,
          "bin": 0.8993333333333333
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.16470029043091927
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 0.908,
            "type": 0.9,
            "bin": 0.848,
            "mean_true": 0.8730763829946518,
            "mean_pred": 0.8556526063159108
          },
          "perturb_large": {
            "n": 250,
            "global": 0.836,
            "type": 0.9,
            "bin": 0.976,
            "mean_true": 1.9225167379379273,
            "mean_pred": 1.8153540377616881
          },
          "perturb_small": {
            "n": 250,
            "global": 1.0,
            "type": 0.9,
            "bin": 0.932,
            "mean_true": 0.2553125400543213,
            "mean_pred": 0.3004061503747944
          },
          "same_task_far": {
            "n": 250,
            "global": 0.964,
            "type": 0.9,
            "bin": 0.832,
            "mean_true": 0.6635248019695282,
            "mean_pred": 0.6624241611845791
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.692,
            "type": 0.9,
            "bin": 0.808,
            "mean_true": 2.0330613836050033,
            "mean_pred": 1.8763049215078353
          }
        }
      },
      "test_id": {
        "n": 1500,
        "overall": {
          "global": 0.9513333333333334,
          "type": 0.9646666666666667,
          "bin": 0.9613333333333334
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.16757236147968796
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 0.956,
            "mean_true": 0.7654269440174103,
            "mean_pred": 0.8322914113402367
          },
          "perturb_large": {
            "n": 250,
            "global": 0.82,
            "type": 0.88,
            "bin": 0.988,
            "mean_true": 1.922516740322113,
            "mean_pred": 1.7890926685333253
          },
          "perturb_small": {
            "n": 250,
            "global": 0.988,
            "type": 0.912,
            "bin": 0.912,
            "mean_true": 0.2553125407099724,
            "mean_pred": 0.3162369293682277
          },
          "same_task_far": {
            "n": 250,
            "global": 1.0,
            "type": 0.996,
            "bin": 0.992,
            "mean_true": 0.5625122112929821,
            "mean_pred": 0.6904039586782456
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.9,
            "type": 1.0,
            "bin": 0.92,
            "mean_true": 1.7740848944187164,
            "mean_pred": 1.7120825030803681
          }
        }
      }
    }
  },
  {
    "split": "holdout_libero_object",
    "global_eta": 0.1700295269489289,
    "type_eta": {
      "expert_action": 0,
      "other_demo_or_other_task": 0.1636053413152694,
      "perturb_large": 0.26878193616867063,
      "perturb_small": 0.03880385309457778,
      "same_task_far": 0.13498676419258118,
      "simvla_seed0": 0.2657571852207184
    },
    "bin_eta": [
      [
        0.0011046594008803368,
        0.35706056118011475,
        0.058982336521148725
      ],
      [
        0.35706056118011475,
        1.0227789282798767,
        0.09881948232650763
      ],
      [
        1.0227789282798767,
        2.819391965866089,
        0.2662676930427551
      ]
    ],
    "parts": {
      "train": {
        "n": 6000,
        "overall": {
          "global": 0.9991666666666666,
          "type": 0.946,
          "bin": 0.9541666666666667
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.01470328202888777
          },
          "other_demo_or_other_task": {
            "n": 1000,
            "global": 1.0,
            "type": 0.999,
            "bin": 0.925,
            "mean_true": 0.7833337866067887,
            "mean_pred": 0.7610093989344314
          },
          "perturb_large": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 1.9188841246366501,
            "mean_pred": 1.9344423197507858
          },
          "perturb_small": {
            "n": 1000,
            "global": 0.995,
            "type": 0.678,
            "bin": 0.861,
            "mean_true": 0.25542284704744816,
            "mean_pred": 0.2335630703009665
          },
          "same_task_far": {
            "n": 1000,
            "global": 1.0,
            "type": 0.999,
            "bin": 0.943,
            "mean_true": 0.6365546908527613,
            "mean_pred": 0.6119099754840136
          },
          "simvla_seed0": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 0.996,
            "mean_true": 1.8661219133734703,
            "mean_pred": 1.87023114913702
          }
        }
      },
      "calib": {
        "n": 1500,
        "overall": {
          "global": 0.9,
          "type": 0.9166666666666666,
          "bin": 0.8993333333333333
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.15835749270999805
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 0.9,
            "type": 0.9,
            "bin": 0.864,
            "mean_true": 0.675784527271986,
            "mean_pred": 0.7075606038719415
          },
          "perturb_large": {
            "n": 250,
            "global": 0.748,
            "type": 0.9,
            "bin": 0.892,
            "mean_true": 1.922516740322113,
            "mean_pred": 1.8560084199905396
          },
          "perturb_small": {
            "n": 250,
            "global": 0.98,
            "type": 0.9,
            "bin": 0.932,
            "mean_true": 0.25531254160404204,
            "mean_pred": 0.3338858204483986
          },
          "same_task_far": {
            "n": 250,
            "global": 0.96,
            "type": 0.9,
            "bin": 0.816,
            "mean_true": 0.5029336425960064,
            "mean_pred": 0.5346328715533019
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.812,
            "type": 0.9,
            "bin": 0.892,
            "mean_true": 1.6905601416826248,
            "mean_pred": 1.6869818373918533
          }
        }
      },
      "test_id": {
        "n": 1500,
        "overall": {
          "global": 0.9233333333333333,
          "type": 0.9426666666666667,
          "bin": 0.942
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.2446447577290237
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 0.964,
            "type": 0.964,
            "bin": 0.952,
            "mean_true": 0.7743899204730987,
            "mean_pred": 0.8513486704826355
          },
          "perturb_large": {
            "n": 250,
            "global": 0.788,
            "type": 0.952,
            "bin": 0.948,
            "mean_true": 1.9225167417526245,
            "mean_pred": 1.8796517505645751
          },
          "perturb_small": {
            "n": 250,
            "global": 0.984,
            "type": 0.916,
            "bin": 0.94,
            "mean_true": 0.25531254076957705,
            "mean_pred": 0.3752386192632839
          },
          "same_task_far": {
            "n": 250,
            "global": 0.988,
            "type": 0.94,
            "bin": 0.932,
            "mean_true": 0.6553350666463376,
            "mean_pred": 0.769006115436554
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.816,
            "type": 0.884,
            "bin": 0.88,
            "mean_true": 1.8564880595207214,
            "mean_pred": 1.7881537779569625
          }
        }
      },
      "test_ood": {
        "n": 1200,
        "overall": {
          "global": 0.9225,
          "type": 0.945,
          "bin": 0.8883333333333333
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 200,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.1210931383370189
          },
          "other_demo_or_other_task": {
            "n": 200,
            "global": 0.965,
            "type": 0.96,
            "bin": 0.81,
            "mean_true": 0.5297832837328315,
            "mean_pred": 0.549264939634013
          },
          "perturb_large": {
            "n": 200,
            "global": 0.77,
            "type": 0.91,
            "bin": 0.905,
            "mean_true": 1.914658175110817,
            "mean_pred": 1.8407512563467026
          },
          "perturb_small": {
            "n": 200,
            "global": 0.99,
            "type": 0.925,
            "bin": 0.945,
            "mean_true": 0.25530532650649546,
            "mean_pred": 0.3006316489353776
          },
          "same_task_far": {
            "n": 200,
            "global": 0.905,
            "type": 0.875,
            "bin": 0.67,
            "mean_true": 0.5352852449566126,
            "mean_pred": 0.48448431983590123
          },
          "simvla_seed0": {
            "n": 200,
            "global": 0.905,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 1.7278787818551065,
            "mean_pred": 1.7020932501554489
          }
        }
      }
    }
  },
  {
    "split": "holdout_object_bowl",
    "global_eta": 0.182714056968689,
    "type_eta": {
      "expert_action": 0,
      "other_demo_or_other_task": 0.22677695453166963,
      "perturb_large": 0.29640012979507446,
      "perturb_small": 0.07379710972309113,
      "same_task_far": 0.1134493768215179,
      "simvla_seed0": 0.17442700862884516
    },
    "bin_eta": [
      [
        0.0004413023416418582,
        0.43927689939737324,
        0.07331661283969881
      ],
      [
        0.43927689939737324,
        1.173552827835083,
        0.09095847606658945
      ],
      [
        1.173552827835083,
        4.802892208099365,
        0.2755964517593384
      ]
    ],
    "parts": {
      "train": {
        "n": 6000,
        "overall": {
          "global": 0.9973333333333333,
          "type": 0.9853333333333333,
          "bin": 0.9776666666666667
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.010501613128190002
          },
          "other_demo_or_other_task": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 0.969,
            "mean_true": 0.7611042740941047,
            "mean_pred": 0.7633598398584872
          },
          "perturb_large": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 1.918884123325348,
            "mean_pred": 1.9339445062875749
          },
          "perturb_small": {
            "n": 1000,
            "global": 0.984,
            "type": 0.927,
            "bin": 0.927,
            "mean_true": 0.2554228469729424,
            "mean_pred": 0.24959452079760377
          },
          "same_task_far": {
            "n": 1000,
            "global": 1.0,
            "type": 0.985,
            "bin": 0.97,
            "mean_true": 0.5657157869115472,
            "mean_pred": 0.5671098235158716
          },
          "simvla_seed0": {
            "n": 1000,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 1.6057486926913263,
            "mean_pred": 1.6233564745783806
          }
        }
      },
      "calib": {
        "n": 1500,
        "overall": {
          "global": 0.9,
          "type": 0.9166666666666666,
          "bin": 0.8993333333333333
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.15589653239760082
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 0.876,
            "type": 0.9,
            "bin": 0.82,
            "mean_true": 0.7878475907444954,
            "mean_pred": 0.8258917578905821
          },
          "perturb_large": {
            "n": 250,
            "global": 0.692,
            "type": 0.9,
            "bin": 0.868,
            "mean_true": 1.9225167369842528,
            "mean_pred": 1.8249443364143372
          },
          "perturb_small": {
            "n": 250,
            "global": 0.984,
            "type": 0.9,
            "bin": 0.892,
            "mean_true": 0.2553125408887863,
            "mean_pred": 0.3638618036005646
          },
          "same_task_far": {
            "n": 250,
            "global": 0.944,
            "type": 0.9,
            "bin": 0.872,
            "mean_true": 0.6095741613507271,
            "mean_pred": 0.6763972515463829
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.904,
            "type": 0.9,
            "bin": 0.944,
            "mean_true": 1.7420408205986022,
            "mean_pred": 1.7746446466445922
          }
        }
      },
      "test_id": {
        "n": 1500,
        "overall": {
          "global": 0.9313333333333333,
          "type": 0.9453333333333334,
          "bin": 0.9253333333333333
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.1375047037281329
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 0.976,
            "type": 1.0,
            "bin": 0.908,
            "mean_true": 0.6429996911287308,
            "mean_pred": 0.7147062692642212
          },
          "perturb_large": {
            "n": 250,
            "global": 0.756,
            "type": 0.964,
            "bin": 0.948,
            "mean_true": 1.922516740322113,
            "mean_pred": 1.8502867360115052
          },
          "perturb_small": {
            "n": 250,
            "global": 0.948,
            "type": 0.904,
            "bin": 0.904,
            "mean_true": 0.2553125413060188,
            "mean_pred": 0.3268221476515755
          },
          "same_task_far": {
            "n": 250,
            "global": 0.964,
            "type": 0.864,
            "bin": 0.824,
            "mean_true": 0.4910696451663971,
            "mean_pred": 0.5405314651755616
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.944,
            "type": 0.94,
            "bin": 0.968,
            "mean_true": 1.9182332221269607,
            "mean_pred": 1.9595397591590882
          }
        }
      },
      "test_ood": {
        "n": 1500,
        "overall": {
          "global": 0.9113333333333333,
          "type": 0.93,
          "bin": 0.928
        },
        "per_candidate_type": {
          "expert_action": {
            "n": 250,
            "global": 1.0,
            "type": 1.0,
            "bin": 1.0,
            "mean_true": 0.0,
            "mean_pred": 0.2083183642481745
          },
          "other_demo_or_other_task": {
            "n": 250,
            "global": 0.988,
            "type": 0.996,
            "bin": 0.952,
            "mean_true": 0.6085226790308952,
            "mean_pred": 0.7142413527322933
          },
          "perturb_large": {
            "n": 250,
            "global": 0.744,
            "type": 0.912,
            "bin": 0.896,
            "mean_true": 1.9225167384147643,
            "mean_pred": 1.832442265510559
          },
          "perturb_small": {
            "n": 250,
            "global": 0.968,
            "type": 0.936,
            "bin": 0.932,
            "mean_true": 0.25531254065036774,
            "mean_pred": 0.3901042254343629
          },
          "same_task_far": {
            "n": 250,
            "global": 0.992,
            "type": 0.968,
            "bin": 0.952,
            "mean_true": 0.6661153256893158,
            "mean_pred": 0.7471462942957878
          },
          "simvla_seed0": {
            "n": 250,
            "global": 0.776,
            "type": 0.768,
            "bin": 0.836,
            "mean_true": 1.6911044684648513,
            "mean_pred": 1.6335441708564757
          }
        }
      }
    }
  }
]
```
