# Stage 6 Switch Decision Analysis

```json
[
  {
    "split": "id_task_split",
    "variant": "action_only_baseline",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 3.09151520729065,
            "accepted_mean": 1.4533945267068016,
            "rejected_mean": 3.9128717074394226,
            "error_reduction_vs_all": 0.2459477180732621,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.040269672870636,
            "accepted_mean": 1.2510503586292268,
            "rejected_mean": 3.0442179032325747,
            "error_reduction_vs_all": 0.4482918861508369,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.518812119960785,
            "accepted_mean": 1.012033515048027,
            "rejected_mean": 2.3866509745121003,
            "error_reduction_vs_all": 0.6873087297320366,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0627015829086304,
            "accepted_mean": 0.7340483886241913,
            "rejected_mean": 2.0211068634986877,
            "error_reduction_vs_all": 0.9652938561558724,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 3.0807732343673706,
            "accepted_mean": 1.4560139651430977,
            "rejected_mean": 3.960377814769745,
            "error_reduction_vs_all": 0.25043638496266474,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.038324773311615,
            "accepted_mean": 1.2501477185090384,
            "rejected_mean": 3.075358244895935,
            "error_reduction_vs_all": 0.456302631596724,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5243072509765625,
            "accepted_mean": 1.0088710905313492,
            "rejected_mean": 2.4040296096801756,
            "error_reduction_vs_all": 0.6975792595744132,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0602591633796692,
            "accepted_mean": 0.7229821856021881,
            "rejected_mean": 2.034273071606954,
            "error_reduction_vs_all": 0.9834681645035743,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.4814536809921264,
            "accepted_mean": 1.611160843875673,
            "rejected_mean": 2.77619278717041,
            "error_reduction_vs_all": 0.11650319432947365,
            "false_accept_high_error_rate": 0.23022222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.1096901893615723,
            "accepted_mean": 1.473871752222167,
            "rejected_mean": 2.487419220205313,
            "error_reduction_vs_all": 0.25379228598297976,
            "false_accept_high_error_rate": 0.1472785485592316,
            "false_reject_low_error_rate": 0.02875399361022364
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7278523445129395,
            "accepted_mean": 1.2246941858768463,
            "rejected_mean": 2.230633890533447,
            "error_reduction_vs_all": 0.5029698523283004,
            "false_accept_high_error_rate": 0.0368,
            "false_reject_low_error_rate": 0.0528
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3395645320415497,
            "accepted_mean": 0.9772974200332507,
            "rejected_mean": 1.978320123037381,
            "error_reduction_vs_all": 0.750366618171896,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.15154749199573106
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.5026013135910032,
            "accepted_mean": 1.6049001789093018,
            "rejected_mean": 2.8358545875549317,
            "error_reduction_vs_all": 0.12309544086456303,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.144300878047943,
            "accepted_mean": 1.4708644209061077,
            "rejected_mean": 2.491226321174985,
            "error_reduction_vs_all": 0.25713119886775715,
            "false_accept_high_error_rate": 0.1443850267379679,
            "false_reject_low_error_rate": 0.047619047619047616
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7393509149551392,
            "accepted_mean": 1.219582859992981,
            "rejected_mean": 2.2364083795547485,
            "error_reduction_vs_all": 0.5084127597808838,
            "false_accept_high_error_rate": 0.04,
            "false_reject_low_error_rate": 0.048
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3315710127353668,
            "accepted_mean": 0.9638631646595304,
            "rejected_mean": 1.98543061802094,
            "error_reduction_vs_all": 0.7641324551143345,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.1497326203208556
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.6521250247955326,
            "accepted_mean": 1.2848382909827762,
            "rejected_mean": 3.145446336746216,
            "error_reduction_vs_all": 0.18606080457634389,
            "false_accept_high_error_rate": 0.2311111111111111,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.068841576576233,
            "accepted_mean": 1.1753894264313811,
            "rejected_mean": 2.3555398622450356,
            "error_reduction_vs_all": 0.295509669127739,
            "false_accept_high_error_rate": 0.14621131270010673,
            "false_reject_low_error_rate": 0.04153354632587859
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6015543937683105,
            "accepted_mean": 1.0790684097766876,
            "rejected_mean": 1.8627297813415526,
            "error_reduction_vs_all": 0.3918306857824325,
            "false_accept_high_error_rate": 0.064,
            "false_reject_low_error_rate": 0.184
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1012459099292755,
            "accepted_mean": 0.9772421968059418,
            "rejected_mean": 1.6358026273731487,
            "error_reduction_vs_all": 0.4936568987531783,
            "false_accept_high_error_rate": 0.03194888178913738,
            "false_reject_low_error_rate": 0.21878335112059766
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.6721864223480223,
            "accepted_mean": 1.2985288263691797,
            "rejected_mean": 3.1338326501846314,
            "error_reduction_vs_all": 0.18353038238154507,
            "false_accept_high_error_rate": 0.2311111111111111,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.1045788526535034,
            "accepted_mean": 1.176840860416545,
            "rejected_mean": 2.388024782377576,
            "error_reduction_vs_all": 0.3052183483341797,
            "false_accept_high_error_rate": 0.1443850267379679,
            "false_reject_low_error_rate": 0.031746031746031744
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5940499305725098,
            "accepted_mean": 1.0721423523426057,
            "rejected_mean": 1.891976065158844,
            "error_reduction_vs_all": 0.40991685640811903,
            "false_accept_high_error_rate": 0.056,
            "false_reject_low_error_rate": 0.168
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.118068516254425,
            "accepted_mean": 0.9775516111699362,
            "rejected_mean": 1.6520270090052152,
            "error_reduction_vs_all": 0.5045075975807886,
            "false_accept_high_error_rate": 0.031746031746031744,
            "false_reject_low_error_rate": 0.2192513368983957
          }
        ]
      }
    }
  },
  {
    "split": "id_task_split",
    "variant": "context_gated_action",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 3.1761515140533447,
            "accepted_mean": 1.4530428185065587,
            "rejected_mean": 3.916037081241608,
            "error_reduction_vs_all": 0.24629942627350498,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.017004430294037,
            "accepted_mean": 1.2502547181924184,
            "rejected_mean": 3.046604824542999,
            "error_reduction_vs_all": 0.4490875265876453,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.516300916671753,
            "accepted_mean": 1.0107524020433425,
            "rejected_mean": 2.3879320875167847,
            "error_reduction_vs_all": 0.6885898427367212,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0757119953632355,
            "accepted_mean": 0.7315447937488556,
            "rejected_mean": 2.0219413951237994,
            "error_reduction_vs_all": 0.9677974510312081,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 3.24649121761322,
            "accepted_mean": 1.4556599781910577,
            "rejected_mean": 3.9635636973381043,
            "error_reduction_vs_all": 0.25079037191470466,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0185930132865906,
            "accepted_mean": 1.2494587520758311,
            "rejected_mean": 3.0774251441955567,
            "error_reduction_vs_all": 0.4569915980299313,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.512335181236267,
            "accepted_mean": 1.0076083320379257,
            "rejected_mean": 2.4052923681735994,
            "error_reduction_vs_all": 0.6988420180678367,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0852646827697754,
            "accepted_mean": 0.7209322793483735,
            "rejected_mean": 2.034956373691559,
            "error_reduction_vs_all": 0.985518070757389,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.6697041034698494,
            "accepted_mean": 1.5945944963296255,
            "rejected_mean": 2.925289915084839,
            "error_reduction_vs_all": 0.13306954187552122,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.1654670238494873,
            "accepted_mean": 1.4115709593418186,
            "rejected_mean": 2.6739235107129375,
            "error_reduction_vs_all": 0.31609307886332805,
            "false_accept_high_error_rate": 0.06616862326574173,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6541801691055298,
            "accepted_mean": 1.1509770519733429,
            "rejected_mean": 2.3043510244369507,
            "error_reduction_vs_all": 0.5766869862318038,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1818489134311676,
            "accepted_mean": 0.8644481669790067,
            "rejected_mean": 2.016016831901819,
            "error_reduction_vs_all": 0.86321587122614,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.07043756670224119
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.7047395229339597,
            "accepted_mean": 1.5940273337894015,
            "rejected_mean": 2.9337101936340333,
            "error_reduction_vs_all": 0.1339682859844633,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.156789004802704,
            "accepted_mean": 1.4038814733372653,
            "rejected_mean": 2.690048721101549,
            "error_reduction_vs_all": 0.3241141464365995,
            "false_accept_high_error_rate": 0.06417112299465241,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6612354516983032,
            "accepted_mean": 1.1387074699401856,
            "rejected_mean": 2.317283769607544,
            "error_reduction_vs_all": 0.5892881498336793,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1955620050430298,
            "accepted_mean": 0.8568840121466016,
            "rejected_mean": 2.021471722878237,
            "error_reduction_vs_all": 0.8711116076272633,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06951871657754011
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.5454649209976195,
            "accepted_mean": 1.2639896647400326,
            "rejected_mean": 3.333083972930908,
            "error_reduction_vs_all": 0.20690943081908753,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8500980138778687,
            "accepted_mean": 1.1140161770830286,
            "rejected_mean": 2.539267448952404,
            "error_reduction_vs_all": 0.35688291847609155,
            "false_accept_high_error_rate": 0.06616862326574173,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.2622175216674805,
            "accepted_mean": 0.9406492720127105,
            "rejected_mean": 2.0011489191055296,
            "error_reduction_vs_all": 0.5302498235464096,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 0.9191554188728333,
            "accepted_mean": 0.7899515614532434,
            "rejected_mean": 1.6983660946787993,
            "error_reduction_vs_all": 0.6809475341058767,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.09071504802561366
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.5500531673431395,
            "accepted_mean": 1.2739171005619896,
            "rejected_mean": 3.3553381824493407,
            "error_reduction_vs_all": 0.20814210818873513,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8875010907649994,
            "accepted_mean": 1.118359643348398,
            "rejected_mean": 2.5616118870084246,
            "error_reduction_vs_all": 0.36369956540232673,
            "false_accept_high_error_rate": 0.06417112299465241,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.2626129984855652,
            "accepted_mean": 0.939013504743576,
            "rejected_mean": 2.0251049127578735,
            "error_reduction_vs_all": 0.5430457040071487,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 0.9172378033399582,
            "accepted_mean": 0.7861301459017254,
            "rejected_mean": 1.7165165935608155,
            "error_reduction_vs_all": 0.6959290628489994,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0855614973262032
          }
        ]
      }
    }
  },
  {
    "split": "holdout_libero_object",
    "variant": "action_only_baseline",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 3.0351518869400027,
            "accepted_mean": 1.4908238607446354,
            "rejected_mean": 4.433566038131714,
            "error_reduction_vs_all": 0.2942742177387079,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9559860527515411,
            "accepted_mean": 1.3065423922459285,
            "rejected_mean": 3.220765137195587,
            "error_reduction_vs_all": 0.47855568623741473,
            "false_accept_high_error_rate": 0.06773333333333334,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4960726499557495,
            "accepted_mean": 1.0868930024504662,
            "rejected_mean": 2.48330315451622,
            "error_reduction_vs_all": 0.6982050760328771,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0939728319644928,
            "accepted_mean": 0.8845656050920486,
            "rejected_mean": 2.0852755696137746,
            "error_reduction_vs_all": 0.9005324733912946,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.07173333333333333
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 3.0929725170135502,
            "accepted_mean": 1.492092719508542,
            "rejected_mean": 4.515409500598907,
            "error_reduction_vs_all": 0.3023316781090364,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9673294126987457,
            "accepted_mean": 1.3023930543661117,
            "rejected_mean": 3.2705184273719787,
            "error_reduction_vs_all": 0.4920313432514667,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4887945652008057,
            "accepted_mean": 1.0790652762055397,
            "rejected_mean": 2.509783519029617,
            "error_reduction_vs_all": 0.7153591214120387,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0949659049510956,
            "accepted_mean": 0.8720887137651443,
            "rejected_mean": 2.1018696255683897,
            "error_reduction_vs_all": 0.9223356838524341,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.07333333333333333
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 4.257523107528686,
            "accepted_mean": 1.8425512992805906,
            "rejected_mean": 4.216021543502808,
            "error_reduction_vs_all": 0.23734702442222155,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.5921940207481384,
            "accepted_mean": 1.5942245459416633,
            "rejected_mean": 3.533816310163504,
            "error_reduction_vs_all": 0.48567377776114884,
            "false_accept_high_error_rate": 0.10032017075773746,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7141055464744568,
            "accepted_mean": 1.5133049760818482,
            "rejected_mean": 2.6464916713237763,
            "error_reduction_vs_all": 0.5665933476209639,
            "false_accept_high_error_rate": 0.1504,
            "false_reject_low_error_rate": 0.0848
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2662429213523865,
            "accepted_mean": 1.317924697844746,
            "rejected_mean": 2.3344316693736498,
            "error_reduction_vs_all": 0.761973625858066,
            "false_accept_high_error_rate": 0.07028753993610223,
            "false_reject_low_error_rate": 0.17609391675560299
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 4.265967226028442,
            "accepted_mean": 1.8651520199245877,
            "rejected_mean": 4.2584418678283695,
            "error_reduction_vs_all": 0.23932898479037834,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.6410791277885437,
            "accepted_mean": 1.6057274201337028,
            "rejected_mean": 3.584908311329191,
            "error_reduction_vs_all": 0.4987535845812632,
            "false_accept_high_error_rate": 0.10160427807486631,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7252783179283142,
            "accepted_mean": 1.5187286579608916,
            "rejected_mean": 2.6902333514690397,
            "error_reduction_vs_all": 0.5857523467540744,
            "false_accept_high_error_rate": 0.152,
            "false_reject_low_error_rate": 0.064
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2736802101135254,
            "accepted_mean": 1.2894424441314878,
            "rejected_mean": 2.3790661882270467,
            "error_reduction_vs_all": 0.8150385605834782,
            "false_accept_high_error_rate": 0.06349206349206349,
            "false_reject_low_error_rate": 0.1657754010695187
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.1001535892486576,
            "accepted_mean": 1.4810045104026794,
            "rejected_mean": 3.14072411441803,
            "error_reduction_vs_all": 0.16597196040153506,
            "false_accept_high_error_rate": 0.24177777777777779,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.7948403060436249,
            "accepted_mean": 1.376434391756068,
            "rejected_mean": 2.4568740045681547,
            "error_reduction_vs_all": 0.27054207904814653,
            "false_accept_high_error_rate": 0.18783351120597652,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.3970510959625244,
            "accepted_mean": 1.1574424994468688,
            "rejected_mean": 2.13651044216156,
            "error_reduction_vs_all": 0.48953397135734567,
            "false_accept_high_error_rate": 0.0896,
            "false_reject_low_error_rate": 0.0352
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.007766991853714,
            "accepted_mean": 0.8829912467124744,
            "rejected_mean": 1.9021817804527894,
            "error_reduction_vs_all": 0.7639852240917401,
            "false_accept_high_error_rate": 0.1182108626198083,
            "false_reject_low_error_rate": 0.13874066168623267
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.1314904928207397,
            "accepted_mean": 1.486814173857371,
            "rejected_mean": 3.1901038599014284,
            "error_reduction_vs_all": 0.1703289686044056,
            "false_accept_high_error_rate": 0.2311111111111111,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8386300206184387,
            "accepted_mean": 1.3786785185018324,
            "rejected_mean": 2.4836968675492304,
            "error_reduction_vs_all": 0.2784646239599442,
            "false_accept_high_error_rate": 0.17647058823529413,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4178446531295776,
            "accepted_mean": 1.1343616595268249,
            "rejected_mean": 2.1799246253967284,
            "error_reduction_vs_all": 0.5227814829349517,
            "false_accept_high_error_rate": 0.08,
            "false_reject_low_error_rate": 0.032
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.000914216041565,
            "accepted_mean": 0.8674457669258118,
            "rejected_mean": 1.923190921385658,
            "error_reduction_vs_all": 0.7896973755359649,
            "false_accept_high_error_rate": 0.09523809523809523,
            "false_reject_low_error_rate": 0.13903743315508021
          }
        ]
      },
      "test_ood": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 1.9486339569091797,
            "accepted_mean": 1.6255625941223568,
            "rejected_mean": 1.9680696210861206,
            "error_reduction_vs_all": 0.03425070269637631,
            "false_accept_high_error_rate": 0.2728888888888889,
            "false_reject_low_error_rate": 0.032
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.7880309522151947,
            "accepted_mean": 1.5720712427713828,
            "rejected_mean": 1.9224788068582455,
            "error_reduction_vs_all": 0.08774205404735036,
            "false_accept_high_error_rate": 0.21237993596584845,
            "false_reject_low_error_rate": 0.04792332268370607
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5339611172676086,
            "accepted_mean": 1.4714895466327667,
            "rejected_mean": 1.8481370470046996,
            "error_reduction_vs_all": 0.18832375018596648,
            "false_accept_high_error_rate": 0.1744,
            "false_reject_low_error_rate": 0.0928
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3382644653320312,
            "accepted_mean": 1.303267081800741,
            "rejected_mean": 1.7789157144287988,
            "error_reduction_vs_all": 0.3565462150179921,
            "false_accept_high_error_rate": 0.19488817891373802,
            "false_reject_low_error_rate": 0.1718249733191035
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 1.9532729029655456,
            "accepted_mean": 1.6296155211660597,
            "rejected_mean": 1.95097158908844,
            "error_reduction_vs_all": 0.032135606792238036,
            "false_accept_high_error_rate": 0.28444444444444444,
            "false_reject_low_error_rate": 0.04
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.7874723076820374,
            "accepted_mean": 1.5691184446135944,
            "rejected_mean": 1.9367084578862266,
            "error_reduction_vs_all": 0.09263268334470331,
            "false_accept_high_error_rate": 0.20320855614973263,
            "false_reject_low_error_rate": 0.06349206349206349
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5468175411224365,
            "accepted_mean": 1.461482973575592,
            "rejected_mean": 1.8620192823410033,
            "error_reduction_vs_all": 0.20026815438270562,
            "false_accept_high_error_rate": 0.168,
            "false_reject_low_error_rate": 0.088
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3459376394748688,
            "accepted_mean": 1.2949263226418268,
            "rejected_mean": 1.7853338163804242,
            "error_reduction_vs_all": 0.3668248053164709,
            "false_accept_high_error_rate": 0.1746031746031746,
            "false_reject_low_error_rate": 0.17647058823529413
          }
        ]
      }
    }
  },
  {
    "split": "holdout_libero_object",
    "variant": "context_gated_action",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 3.1448600053787237,
            "accepted_mean": 1.4899325315091345,
            "rejected_mean": 4.441588001251221,
            "error_reduction_vs_all": 0.2951655469742087,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0261977910995483,
            "accepted_mean": 1.3051171576738358,
            "rejected_mean": 3.2250408409118654,
            "error_reduction_vs_all": 0.4799809208095074,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5136431455612183,
            "accepted_mean": 1.0837691184878349,
            "rejected_mean": 2.486427038478851,
            "error_reduction_vs_all": 0.7013289599955084,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0871086716651917,
            "accepted_mean": 0.8790168828725815,
            "rejected_mean": 2.0871251436869303,
            "error_reduction_vs_all": 0.9060811956107617,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 3.1829046487808235,
            "accepted_mean": 1.491615736650096,
            "rejected_mean": 4.51970234632492,
            "error_reduction_vs_all": 0.3028086609674825,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0283783078193665,
            "accepted_mean": 1.3019650521675745,
            "rejected_mean": 3.2718024339675904,
            "error_reduction_vs_all": 0.4924593454500039,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5117363333702087,
            "accepted_mean": 1.0763876371979713,
            "rejected_mean": 2.5124611580371856,
            "error_reduction_vs_all": 0.7180367604196072,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0775606334209442,
            "accepted_mean": 0.8664861694574356,
            "rejected_mean": 2.103737140337626,
            "error_reduction_vs_all": 0.9279382281601428,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 4.2263829708099365,
            "accepted_mean": 1.842187925418218,
            "rejected_mean": 4.21929190826416,
            "error_reduction_vs_all": 0.23771039828459406,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.8516125082969666,
            "accepted_mean": 1.5515472889900717,
            "rejected_mean": 3.661575382890793,
            "error_reduction_vs_all": 0.5283510347127405,
            "false_accept_high_error_rate": 0.06616862326574173,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.8775267004966736,
            "accepted_mean": 1.2233175595760346,
            "rejected_mean": 2.9364790878295897,
            "error_reduction_vs_all": 0.8565807641267775,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2837861478328705,
            "accepted_mean": 0.8660306792480116,
            "rejected_mean": 2.4853845272400084,
            "error_reduction_vs_all": 1.2138676444548007,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06616862326574173
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 4.250928974151611,
            "accepted_mean": 1.8656025314331055,
            "rejected_mean": 4.254387264251709,
            "error_reduction_vs_all": 0.23887847328186051,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.8946176767349243,
            "accepted_mean": 1.559065182578755,
            "rejected_mean": 3.7234136831192743,
            "error_reduction_vs_all": 0.5454158221362111,
            "false_accept_high_error_rate": 0.06417112299465241,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.878698706626892,
            "accepted_mean": 1.2218901548385621,
            "rejected_mean": 2.9870718545913695,
            "error_reduction_vs_all": 0.8825908498764039,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2988595962524414,
            "accepted_mean": 0.8638620717184884,
            "rejected_mean": 2.5224435329437256,
            "error_reduction_vs_all": 1.2406189329964776,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06417112299465241
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.767056107521057,
            "accepted_mean": 1.4598634139696758,
            "rejected_mean": 3.3309939823150634,
            "error_reduction_vs_all": 0.18711305683453872,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0606454014778137,
            "accepted_mean": 1.303270105682035,
            "rejected_mean": 2.67589935936486,
            "error_reduction_vs_all": 0.34370636512217945,
            "false_accept_high_error_rate": 0.06937033084311633,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.74562007188797,
            "accepted_mean": 1.0249540028572082,
            "rejected_mean": 2.2689989387512206,
            "error_reduction_vs_all": 0.6220224679470063,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1062073409557343,
            "accepted_mean": 0.653864084722135,
            "rejected_mean": 1.9787205229319529,
            "error_reduction_vs_all": 0.9931123860820795,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06616862326574173
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.9132110595703122,
            "accepted_mean": 1.4655003004603915,
            "rejected_mean": 3.381928720474243,
            "error_reduction_vs_all": 0.19164284200138515,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.100319266319275,
            "accepted_mean": 1.2993908652009811,
            "rejected_mean": 2.719042759093027,
            "error_reduction_vs_all": 0.3577522772607955,
            "false_accept_high_error_rate": 0.06417112299465241,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7632796168327332,
            "accepted_mean": 1.0154623284339905,
            "rejected_mean": 2.298823956489563,
            "error_reduction_vs_all": 0.6416808140277861,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0877486169338226,
            "accepted_mean": 0.641842334043412,
            "rejected_mean": 1.9991963559930974,
            "error_reduction_vs_all": 1.0153008084183646,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06417112299465241
          }
        ]
      },
      "test_ood": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.0328285455703736,
            "accepted_mean": 1.5921765259901683,
            "rejected_mean": 2.2685442342758178,
            "error_reduction_vs_all": 0.06763677082856479,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8908412754535675,
            "accepted_mean": 1.5174151995202394,
            "rejected_mean": 2.0860976967186975,
            "error_reduction_vs_all": 0.14239809729849373,
            "false_accept_high_error_rate": 0.10352187833511206,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.731981635093689,
            "accepted_mean": 1.358108776140213,
            "rejected_mean": 1.9615178174972534,
            "error_reduction_vs_all": 0.30170452067852005,
            "false_accept_high_error_rate": 0.0016,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.4433498978614807,
            "accepted_mean": 1.1023163232750024,
            "rejected_mean": 1.846042275174323,
            "error_reduction_vs_all": 0.5574969735437307,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06616862326574173
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.0355817079544067,
            "accepted_mean": 1.598184163040585,
            "rejected_mean": 2.2338538122177125,
            "error_reduction_vs_all": 0.06356696491771263,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.892313539981842,
            "accepted_mean": 1.5247947509913522,
            "rejected_mean": 2.0682724373681203,
            "error_reduction_vs_all": 0.13695637696694551,
            "false_accept_high_error_rate": 0.0962566844919786,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.750980257987976,
            "accepted_mean": 1.3704585938453675,
            "rejected_mean": 1.953043662071228,
            "error_reduction_vs_all": 0.2912925341129302,
            "false_accept_high_error_rate": 0.008,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.4861798286437988,
            "accepted_mean": 1.1135094913225325,
            "rejected_mean": 1.8464528558088495,
            "error_reduction_vs_all": 0.5482416366357652,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06951871657754011
          }
        ]
      }
    }
  },
  {
    "split": "holdout_object_bowl",
    "variant": "action_only_baseline",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.72305006980896,
            "accepted_mean": 1.4058618086377779,
            "rejected_mean": 3.455031594276428,
            "error_reduction_vs_all": 0.20491697856386515,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9437905550003052,
            "accepted_mean": 1.2419212166388829,
            "rejected_mean": 2.717351498889923,
            "error_reduction_vs_all": 0.36885757056276014,
            "false_accept_high_error_rate": 0.06693333333333333,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.383994460105896,
            "accepted_mean": 1.0109063063025474,
            "rejected_mean": 2.2106512681007384,
            "error_reduction_vs_all": 0.5998724808990956,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0077393352985382,
            "accepted_mean": 0.8094370794534683,
            "rejected_mean": 1.877892689784368,
            "error_reduction_vs_all": 0.8013417077481747,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06773333333333334
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.732617712020874,
            "accepted_mean": 1.4106872901982732,
            "rejected_mean": 3.459897668361664,
            "error_reduction_vs_all": 0.20492103781633908,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9424365162849426,
            "accepted_mean": 1.2437928483088811,
            "rejected_mean": 2.7310547671318055,
            "error_reduction_vs_all": 0.37181547970573114,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.3894378542900085,
            "accepted_mean": 1.00458858948946,
            "rejected_mean": 2.226628066539764,
            "error_reduction_vs_all": 0.6110197385251523,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0046382546424866,
            "accepted_mean": 0.8016831229925155,
            "rejected_mean": 1.8869167296886444,
            "error_reduction_vs_all": 0.8139252050220968,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.068
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.068113327026367,
            "accepted_mean": 1.523936981042226,
            "rejected_mean": 1.649550787448883,
            "error_reduction_vs_all": 0.012561380640665698,
            "false_accept_high_error_rate": 0.2817777777777778,
            "false_reject_low_error_rate": 0.2
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.7801158130168915,
            "accepted_mean": 1.4771204350343254,
            "rejected_mean": 1.7142527299567152,
            "error_reduction_vs_all": 0.05937792664856634,
            "false_accept_high_error_rate": 0.24759871931696906,
            "false_reject_low_error_rate": 0.14057507987220447
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.504260540008545,
            "accepted_mean": 1.4042451375961305,
            "rejected_mean": 1.6687515857696533,
            "error_reduction_vs_all": 0.13225322408676132,
            "false_accept_high_error_rate": 0.176,
            "false_reject_low_error_rate": 0.1984
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2057543694972992,
            "accepted_mean": 1.1780726264079158,
            "rejected_mean": 1.6562286233062296,
            "error_reduction_vs_all": 0.358425735274976,
            "false_accept_high_error_rate": 0.03194888178913738,
            "false_reject_low_error_rate": 0.19850586979722518
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.0868266820907593,
            "accepted_mean": 1.5201192235946654,
            "rejected_mean": 1.606865224838257,
            "error_reduction_vs_all": 0.008674600124359166,
            "false_accept_high_error_rate": 0.28444444444444444,
            "false_reject_low_error_rate": 0.24
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.7753565311431885,
            "accepted_mean": 1.4600961297591102,
            "rejected_mean": 1.7327060264254373,
            "error_reduction_vs_all": 0.06869769395991443,
            "false_accept_high_error_rate": 0.24064171122994651,
            "false_reject_low_error_rate": 0.1746031746031746
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.518722951412201,
            "accepted_mean": 1.3816433124542236,
            "rejected_mean": 1.6759443349838257,
            "error_reduction_vs_all": 0.14715051126480105,
            "false_accept_high_error_rate": 0.168,
            "false_reject_low_error_rate": 0.192
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.16102534532547,
            "accepted_mean": 1.1611925477073306,
            "rejected_mean": 1.652638103872697,
            "error_reduction_vs_all": 0.367601276011694,
            "false_accept_high_error_rate": 0.06349206349206349,
            "false_reject_low_error_rate": 0.18181818181818182
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.656078243255615,
            "accepted_mean": 1.7449985154469807,
            "rejected_mean": 2.31960923576355,
            "error_reduction_vs_all": 0.05746107203165707,
            "false_accept_high_error_rate": 0.29333333333333333,
            "false_reject_low_error_rate": 0.008
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8694741129875183,
            "accepted_mean": 1.7986621139143677,
            "rejected_mean": 1.8138277431646475,
            "error_reduction_vs_all": 0.0037974735642700708,
            "false_accept_high_error_rate": 0.33938100320170755,
            "false_reject_low_error_rate": 0.22364217252396165
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4559205174446106,
            "accepted_mean": 1.8175836182594298,
            "rejected_mean": 1.7873355566978455,
            "error_reduction_vs_all": -0.015124030780792053,
            "false_accept_high_error_rate": 0.3776,
            "false_reject_low_error_rate": 0.2016
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1787908971309662,
            "accepted_mean": 1.9502092951212446,
            "rejected_mean": 1.7531045624069876,
            "error_reduction_vs_all": -0.14774970764260686,
            "false_accept_high_error_rate": 0.4952076677316294,
            "false_reject_low_error_rate": 0.2870864461045891
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.655094623565674,
            "accepted_mean": 1.7480935264958275,
            "rejected_mean": 2.3386440753936766,
            "error_reduction_vs_all": 0.05905505488978502,
            "false_accept_high_error_rate": 0.29333333333333333,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8811631798744202,
            "accepted_mean": 1.800650859739691,
            "rejected_mean": 1.826435469445728,
            "error_reduction_vs_all": 0.006497721645921439,
            "false_accept_high_error_rate": 0.33689839572192515,
            "false_reject_low_error_rate": 0.20634920634920634
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4704928398132324,
            "accepted_mean": 1.8208637492656707,
            "rejected_mean": 1.7934334135055543,
            "error_reduction_vs_all": -0.013715167880058221,
            "false_accept_high_error_rate": 0.368,
            "false_reject_low_error_rate": 0.192
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1868302524089813,
            "accepted_mean": 1.9305660398233504,
            "rejected_mean": 1.765569437633861,
            "error_reduction_vs_all": -0.12341745843773788,
            "false_accept_high_error_rate": 0.4603174603174603,
            "false_reject_low_error_rate": 0.28342245989304815
          }
        ]
      },
      "test_ood": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.3273521661758427,
            "accepted_mean": 1.5142798593044282,
            "rejected_mean": 2.601584612369537,
            "error_reduction_vs_all": 0.10873047530651081,
            "false_accept_high_error_rate": 0.24888888888888888,
            "false_reject_low_error_rate": 0.112
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.897838979959488,
            "accepted_mean": 1.415348489771785,
            "rejected_mean": 2.244668956381825,
            "error_reduction_vs_all": 0.20766184483915406,
            "false_accept_high_error_rate": 0.15795090715048027,
            "false_reject_low_error_rate": 0.14696485623003194
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.721242070198059,
            "accepted_mean": 1.335572224855423,
            "rejected_mean": 1.9104484443664551,
            "error_reduction_vs_all": 0.2874381097555161,
            "false_accept_high_error_rate": 0.1248,
            "false_reject_low_error_rate": 0.1936
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3931295275688171,
            "accepted_mean": 1.1336651094995749,
            "rejected_mean": 1.7864735741625473,
            "error_reduction_vs_all": 0.48934522511136413,
            "false_accept_high_error_rate": 0.019169329073482427,
            "false_reject_low_error_rate": 0.22518676627534684
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.37751567363739,
            "accepted_mean": 1.512873152891795,
            "rejected_mean": 2.5773644065856933,
            "error_reduction_vs_all": 0.10644912536938977,
            "false_accept_high_error_rate": 0.25333333333333335,
            "false_reject_low_error_rate": 0.12
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8891750276088715,
            "accepted_mean": 1.403628130010105,
            "rejected_mean": 2.2595572897366116,
            "error_reduction_vs_all": 0.2156941482510797,
            "false_accept_high_error_rate": 0.15508021390374332,
            "false_reject_low_error_rate": 0.19047619047619047
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.734998643398285,
            "accepted_mean": 1.3267281093597412,
            "rejected_mean": 1.9119164471626282,
            "error_reduction_vs_all": 0.2925941689014435,
            "false_accept_high_error_rate": 0.128,
            "false_reject_low_error_rate": 0.216
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3736605942249298,
            "accepted_mean": 1.0998660817978874,
            "rejected_mean": 1.7943262374974827,
            "error_reduction_vs_all": 0.5194561964632973,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.21390374331550802
          }
        ]
      }
    }
  },
  {
    "split": "holdout_object_bowl",
    "variant": "context_gated_action",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.7367575883865367,
            "accepted_mean": 1.4056922442317008,
            "rejected_mean": 3.4565576739311217,
            "error_reduction_vs_all": 0.20508654296994222,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9466596245765686,
            "accepted_mean": 1.2412852666775385,
            "rejected_mean": 2.7192593487739565,
            "error_reduction_vs_all": 0.36949352052410456,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.3910744786262512,
            "accepted_mean": 1.010218369615078,
            "rejected_mean": 2.211339204788208,
            "error_reduction_vs_all": 0.6005604175865651,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0110214948654175,
            "accepted_mean": 0.8070589223623276,
            "rejected_mean": 1.8786854088147482,
            "error_reduction_vs_all": 0.8037198648393155,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.7905086517333983,
            "accepted_mean": 1.41061568117804,
            "rejected_mean": 3.460542149543762,
            "error_reduction_vs_all": 0.20499264683657237,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.959432065486908,
            "accepted_mean": 1.2431501380999883,
            "rejected_mean": 2.732982897758484,
            "error_reduction_vs_all": 0.372458189914624,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4000588059425354,
            "accepted_mean": 1.003897250711918,
            "rejected_mean": 2.2273194053173064,
            "error_reduction_vs_all": 0.6117110773026944,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0149751007556915,
            "accepted_mean": 0.7986795326471329,
            "rejected_mean": 1.8879179264704387,
            "error_reduction_vs_all": 0.8169287953674794,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.0849127531051637,
            "accepted_mean": 1.4580160433451335,
            "rejected_mean": 2.242839226722717,
            "error_reduction_vs_all": 0.07848231833775832,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8975167870521545,
            "accepted_mean": 1.3580493854484028,
            "rejected_mean": 2.0707050413369372,
            "error_reduction_vs_all": 0.17844897623448897,
            "false_accept_high_error_rate": 0.0832443970117396,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5098183751106262,
            "accepted_mean": 1.1692486030578613,
            "rejected_mean": 1.9037481203079223,
            "error_reduction_vs_all": 0.3672497586250305,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1747453808784485,
            "accepted_mean": 0.9772480014033211,
            "rejected_mean": 1.7233130498018947,
            "error_reduction_vs_all": 0.5592503602795706,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06830309498399147
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.1001522064208986,
            "accepted_mean": 1.449910699526469,
            "rejected_mean": 2.238741941452026,
            "error_reduction_vs_all": 0.07888312419255561,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9033553898334503,
            "accepted_mean": 1.3483713578412877,
            "rejected_mean": 2.0643335240227834,
            "error_reduction_vs_all": 0.18042246587773692,
            "false_accept_high_error_rate": 0.0748663101604278,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5087780952453613,
            "accepted_mean": 1.1596015663146972,
            "rejected_mean": 1.897986081123352,
            "error_reduction_vs_all": 0.3691922574043274,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1791546940803528,
            "accepted_mean": 0.9604174636659168,
            "rejected_mean": 1.720278907587184,
            "error_reduction_vs_all": 0.5683763600531078,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06417112299465241
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.4407946109771728,
            "accepted_mean": 1.6506211272345648,
            "rejected_mean": 3.169005729675293,
            "error_reduction_vs_all": 0.151838460244073,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9259012341499329,
            "accepted_mean": 1.4571435323010895,
            "rejected_mean": 2.8362012606459306,
            "error_reduction_vs_all": 0.34531605517754826,
            "false_accept_high_error_rate": 0.0672358591248666,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6415038704872131,
            "accepted_mean": 1.2985810190200806,
            "rejected_mean": 2.306338155937195,
            "error_reduction_vs_all": 0.5038785684585572,
            "false_accept_high_error_rate": 0.0016,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3840212523937225,
            "accepted_mean": 1.114254551192823,
            "rejected_mean": 2.032350917636012,
            "error_reduction_vs_all": 0.6882050362858148,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0832443970117396
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.466443109512329,
            "accepted_mean": 1.6517350216706594,
            "rejected_mean": 3.2058706188201906,
            "error_reduction_vs_all": 0.15541355971495308,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9384341537952423,
            "accepted_mean": 1.4556038033834753,
            "rejected_mean": 2.8506227637094166,
            "error_reduction_vs_all": 0.35154477800213724,
            "false_accept_high_error_rate": 0.06417112299465241,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.643373191356659,
            "accepted_mean": 1.2973989617824555,
            "rejected_mean": 2.3168982009887698,
            "error_reduction_vs_all": 0.509749619603157,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3808550834655762,
            "accepted_mean": 1.116669889007296,
            "rejected_mean": 2.03976974512804,
            "error_reduction_vs_all": 0.6904786923783166,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0855614973262032
          }
        ]
      },
      "test_ood": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.563948440551758,
            "accepted_mean": 1.4764419053660498,
            "rejected_mean": 2.9421261978149413,
            "error_reduction_vs_all": 0.14656842924488922,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.046415150165558,
            "accepted_mean": 1.3102346035625025,
            "rejected_mean": 2.5593389607846926,
            "error_reduction_vs_all": 0.3127757310484365,
            "false_accept_high_error_rate": 0.06830309498399147,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.5559746026992798,
            "accepted_mean": 1.1177561085224152,
            "rejected_mean": 2.128264560699463,
            "error_reduction_vs_all": 0.5052542260885238,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2580578327178955,
            "accepted_mean": 0.8696439948897011,
            "rejected_mean": 1.8746684608998905,
            "error_reduction_vs_all": 0.7533663397212379,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.07470651013874066
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.527260279655456,
            "accepted_mean": 1.4680441996786329,
            "rejected_mean": 2.9808249855041504,
            "error_reduction_vs_all": 0.15127807858255182,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0768816471099854,
            "accepted_mean": 1.2984497531212587,
            "rejected_mean": 2.5717534243114413,
            "error_reduction_vs_all": 0.32087252513992603,
            "false_accept_high_error_rate": 0.06951871657754011,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.570462703704834,
            "accepted_mean": 1.1066490778923035,
            "rejected_mean": 2.131995478630066,
            "error_reduction_vs_all": 0.5126732003688812,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2571452856063843,
            "accepted_mean": 0.8551646499406724,
            "rejected_mean": 1.8767657573210363,
            "error_reduction_vs_all": 0.7641576283205123,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.08021390374331551
          }
        ]
      }
    }
  },
  {
    "split": "holdout_libero_spatial",
    "variant": "action_only_baseline",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 3.5483646631240853,
            "accepted_mean": 1.568217608961794,
            "rejected_mean": 4.288577872753144,
            "error_reduction_vs_all": 0.27203602637913504,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.1550203561782837,
            "accepted_mean": 1.3621052876551947,
            "rejected_mean": 3.2746986783981322,
            "error_reduction_vs_all": 0.47814834768573444,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6444513201713562,
            "accepted_mean": 1.1154436503529548,
            "rejected_mean": 2.5650636203289032,
            "error_reduction_vs_all": 0.7248099849879743,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.153622716665268,
            "accepted_mean": 0.8416513303995132,
            "rejected_mean": 2.173121070321401,
            "error_reduction_vs_all": 0.9986023049414159,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 3.6171094655990603,
            "accepted_mean": 1.5771077304416232,
            "rejected_mean": 4.30628753900528,
            "error_reduction_vs_all": 0.27291798085636576,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.167488932609558,
            "accepted_mean": 1.3728836727142335,
            "rejected_mean": 3.2814518270492554,
            "error_reduction_vs_all": 0.4771420385837555,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.674760103225708,
            "accepted_mean": 1.1225378592014312,
            "rejected_mean": 2.5775135633945463,
            "error_reduction_vs_all": 0.7274878520965578,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1741490066051483,
            "accepted_mean": 0.8456106810569763,
            "rejected_mean": 2.1848307213783262,
            "error_reduction_vs_all": 1.0044150302410126,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.313226628303528,
            "accepted_mean": 1.574299118783739,
            "rejected_mean": 2.195220299720764,
            "error_reduction_vs_all": 0.06209211809370241,
            "false_accept_high_error_rate": 0.2577777777777778,
            "false_reject_low_error_rate": 0.04
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.018332302570343,
            "accepted_mean": 1.3837720618812863,
            "rejected_mean": 2.3926345818339825,
            "error_reduction_vs_all": 0.25261917499615505,
            "false_accept_high_error_rate": 0.13127001067235858,
            "false_reject_low_error_rate": 0.022364217252396165
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.667097270488739,
            "accepted_mean": 1.162106794834137,
            "rejected_mean": 2.110675678920746,
            "error_reduction_vs_all": 0.47428444204330433,
            "false_accept_high_error_rate": 0.024,
            "false_reject_low_error_rate": 0.0592
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2328872680664062,
            "accepted_mean": 0.938007218483538,
            "rejected_mean": 1.8696828033206556,
            "error_reduction_vs_all": 0.6983840183939034,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.15581643543223053
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.3784024238586423,
            "accepted_mean": 1.5995766858259837,
            "rejected_mean": 2.191332221031189,
            "error_reduction_vs_all": 0.05917555352052051,
            "false_accept_high_error_rate": 0.26222222222222225,
            "false_reject_low_error_rate": 0.04
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.039981961250305,
            "accepted_mean": 1.4068467197889951,
            "rejected_mean": 2.4064717973981584,
            "error_reduction_vs_all": 0.25190551955750906,
            "false_accept_high_error_rate": 0.1443850267379679,
            "false_reject_low_error_rate": 0.031746031746031744
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7023524641990662,
            "accepted_mean": 1.1744524309635163,
            "rejected_mean": 2.1430520477294923,
            "error_reduction_vs_all": 0.4842998083829879,
            "false_accept_high_error_rate": 0.016,
            "false_reject_low_error_rate": 0.072
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.2626740634441376,
            "accepted_mean": 0.9435593045893169,
            "rejected_mean": 1.899699591697856,
            "error_reduction_vs_all": 0.7151929347571873,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.15508021390374332
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.066221809387207,
            "accepted_mean": 1.7559205482270983,
            "rejected_mean": 2.310755837917328,
            "error_reduction_vs_all": 0.05548352896902298,
            "false_accept_high_error_rate": 0.24977777777777777,
            "false_reject_low_error_rate": 0.04
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.8887851238250732,
            "accepted_mean": 1.6682943178215557,
            "rejected_mean": 2.239818915962792,
            "error_reduction_vs_all": 0.1431097593745656,
            "false_accept_high_error_rate": 0.18036286019210246,
            "false_reject_low_error_rate": 0.025559105431309903
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6247625350952148,
            "accepted_mean": 1.5444750946044923,
            "rejected_mean": 2.07833305978775,
            "error_reduction_vs_all": 0.266928982591629,
            "false_accept_high_error_rate": 0.0912,
            "false_reject_low_error_rate": 0.0832
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.324768602848053,
            "accepted_mean": 1.3758067524852082,
            "rejected_mean": 1.956913108823139,
            "error_reduction_vs_all": 0.43559732471091306,
            "false_accept_high_error_rate": 0.10223642172523961,
            "false_reject_low_error_rate": 0.16008537886872998
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.104437565803528,
            "accepted_mean": 1.7771770885255602,
            "rejected_mean": 2.441415061950684,
            "error_reduction_vs_all": 0.06642379734251236,
            "false_accept_high_error_rate": 0.24444444444444444,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9087336361408234,
            "accepted_mean": 1.679529844120862,
            "rejected_mean": 2.3306054066097928,
            "error_reduction_vs_all": 0.16407104174721066,
            "false_accept_high_error_rate": 0.1657754010695187,
            "false_reject_low_error_rate": 0.031746031746031744
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6562851071357727,
            "accepted_mean": 1.5536101770401,
            "rejected_mean": 2.133591594696045,
            "error_reduction_vs_all": 0.2899907088279725,
            "false_accept_high_error_rate": 0.088,
            "false_reject_low_error_rate": 0.08
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.3638636469841003,
            "accepted_mean": 1.3758373222653828,
            "rejected_mean": 2.0011896800229896,
            "error_reduction_vs_all": 0.4677635636026898,
            "false_accept_high_error_rate": 0.09523809523809523,
            "false_reject_low_error_rate": 0.16042780748663102
          }
        ]
      },
      "test_ood": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.069823431968689,
            "accepted_mean": 1.8795900795194838,
            "rejected_mean": 2.231306254863739,
            "error_reduction_vs_all": 0.03517161753442544,
            "false_accept_high_error_rate": 0.26222222222222225,
            "false_reject_low_error_rate": 0.14
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9190280139446259,
            "accepted_mean": 1.8234567718505859,
            "rejected_mean": 2.188676472663879,
            "error_reduction_vs_all": 0.09130492520332334,
            "false_accept_high_error_rate": 0.19866666666666666,
            "false_reject_low_error_rate": 0.056
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4225564002990723,
            "accepted_mean": 1.778692656517029,
            "rejected_mean": 2.0508307375907897,
            "error_reduction_vs_all": 0.1360690405368803,
            "false_accept_high_error_rate": 0.122,
            "false_reject_low_error_rate": 0.176
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.0505734384059906,
            "accepted_mean": 1.7372561612129211,
            "rejected_mean": 1.9739302090009054,
            "error_reduction_vs_all": 0.17750553584098805,
            "false_accept_high_error_rate": 0.104,
            "false_reject_low_error_rate": 0.24
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.067994165420532,
            "accepted_mean": 1.8965779536300236,
            "rejected_mean": 2.1930990517139435,
            "error_reduction_vs_all": 0.029652109808391947,
            "false_accept_high_error_rate": 0.2777777777777778,
            "false_reject_low_error_rate": 0.2
          },
          {
            "reject_rate": 0.25,
            "threshold": 1.9359078705310822,
            "accepted_mean": 1.8373638319969177,
            "rejected_mean": 2.192828757762909,
            "error_reduction_vs_all": 0.08886623144149786,
            "false_accept_high_error_rate": 0.20666666666666667,
            "false_reject_low_error_rate": 0.08
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.4718773365020752,
            "accepted_mean": 1.7909198606014252,
            "rejected_mean": 2.061540266275406,
            "error_reduction_vs_all": 0.13531020283699036,
            "false_accept_high_error_rate": 0.14,
            "false_reject_low_error_rate": 0.2
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.057366818189621,
            "accepted_mean": 1.7532806420326232,
            "rejected_mean": 1.9838798705736795,
            "error_reduction_vs_all": 0.17294942140579228,
            "false_accept_high_error_rate": 0.14,
            "false_reject_low_error_rate": 0.26
          }
        ]
      }
    }
  },
  {
    "split": "holdout_libero_spatial",
    "variant": "context_gated_action",
    "parts": {
      "train": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 3.4255178689956676,
            "accepted_mean": 1.5681292934219042,
            "rejected_mean": 4.289372712612152,
            "error_reduction_vs_all": 0.2721243419190249,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.108215868473053,
            "accepted_mean": 1.361621087495486,
            "rejected_mean": 3.276151278877258,
            "error_reduction_vs_all": 0.4786325478454432,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6181873679161072,
            "accepted_mean": 1.1144175255894662,
            "rejected_mean": 2.566089745092392,
            "error_reduction_vs_all": 0.725836109751463,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1321427822113037,
            "accepted_mean": 0.8401909522294998,
            "rejected_mean": 2.173607863044739,
            "error_reduction_vs_all": 1.0000626831114294,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 3.3825411796569833,
            "accepted_mean": 1.5771077304416232,
            "rejected_mean": 4.30628753900528,
            "error_reduction_vs_all": 0.27291798085636576,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.134982943534851,
            "accepted_mean": 1.3725075308481853,
            "rejected_mean": 3.2825802526473997,
            "error_reduction_vs_all": 0.47751818044980365,
            "false_accept_high_error_rate": 0.06666666666666667,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.650318682193756,
            "accepted_mean": 1.121159267425537,
            "rejected_mean": 2.5788921551704407,
            "error_reduction_vs_all": 0.7288664438724519,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.145195484161377,
            "accepted_mean": 0.8436733469963074,
            "rejected_mean": 2.1854764993985496,
            "error_reduction_vs_all": 1.0063523643016816,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06666666666666667
          }
        ]
      },
      "calib": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.5470976352691657,
            "accepted_mean": 1.5135126152038574,
            "rejected_mean": 2.7422988319396975,
            "error_reduction_vs_all": 0.12287862167358399,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.080787181854248,
            "accepted_mean": 1.3457583691547113,
            "rejected_mean": 2.5064327610186496,
            "error_reduction_vs_all": 0.2906328677227301,
            "false_accept_high_error_rate": 0.07470651013874066,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.662714421749115,
            "accepted_mean": 1.0914653871536255,
            "rejected_mean": 2.1813170866012572,
            "error_reduction_vs_all": 0.5449258497238159,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1098701059818268,
            "accepted_mean": 0.7512874532812319,
            "rejected_mean": 1.9320555744074452,
            "error_reduction_vs_all": 0.8851037835962094,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06616862326574173
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.5671860218048095,
            "accepted_mean": 1.5304330678780873,
            "rejected_mean": 2.813624782562256,
            "error_reduction_vs_all": 0.12831917146841687,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.098213315010071,
            "accepted_mean": 1.3633799943375715,
            "rejected_mean": 2.535492077706352,
            "error_reduction_vs_all": 0.29537224500893267,
            "false_accept_high_error_rate": 0.08021390374331551,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.6787967681884766,
            "accepted_mean": 1.11210355591774,
            "rejected_mean": 2.2054009227752687,
            "error_reduction_vs_all": 0.5466486834287643,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.1369667947292328,
            "accepted_mean": 0.7624138068585169,
            "rejected_mean": 1.9607272192756122,
            "error_reduction_vs_all": 0.8963384324879873,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.06417112299465241
          }
        ]
      },
      "test_id": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.2751375198364263,
            "accepted_mean": 1.7245807701216804,
            "rejected_mean": 2.592813840866089,
            "error_reduction_vs_all": 0.08682330707444086,
            "false_accept_high_error_rate": 0.22311111111111112,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0090808272361755,
            "accepted_mean": 1.6125679534552828,
            "rejected_mean": 2.4066419300560753,
            "error_reduction_vs_all": 0.19883612374083848,
            "false_accept_high_error_rate": 0.09711846318036287,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.7884730696678162,
            "accepted_mean": 1.4368013283729553,
            "rejected_mean": 2.186006826019287,
            "error_reduction_vs_all": 0.374602748823166,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.5022497475147247,
            "accepted_mean": 1.1828200857098492,
            "rejected_mean": 2.021379305942336,
            "error_reduction_vs_all": 0.6285839914862721,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.07150480256136606
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.3772403478622435,
            "accepted_mean": 1.7490210655000475,
            "rejected_mean": 2.694819269180298,
            "error_reduction_vs_all": 0.09457982036802504,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0289787650108337,
            "accepted_mean": 1.6236376972759472,
            "rejected_mean": 2.496507493276445,
            "error_reduction_vs_all": 0.21996318859212538,
            "false_accept_high_error_rate": 0.09090909090909091,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.8181908130645752,
            "accepted_mean": 1.4468697690963745,
            "rejected_mean": 2.2403320026397706,
            "error_reduction_vs_all": 0.39673111677169803,
            "false_accept_high_error_rate": 0.008,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.5448409020900726,
            "accepted_mean": 1.1901155502077132,
            "rejected_mean": 2.0637590470798512,
            "error_reduction_vs_all": 0.6534853356603594,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.0748663101604278
          }
        ]
      },
      "test_ood": {
        "all_simvla": [
          {
            "reject_rate": 0.1,
            "threshold": 2.215623617172241,
            "accepted_mean": 1.8440360188484193,
            "rejected_mean": 2.5512928009033202,
            "error_reduction_vs_all": 0.07072567820548992,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0206016898155212,
            "accepted_mean": 1.765569986184438,
            "rejected_mean": 2.362336829662323,
            "error_reduction_vs_all": 0.14919171086947114,
            "false_accept_high_error_rate": 0.09466666666666666,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.837638795375824,
            "accepted_mean": 1.659000018119812,
            "rejected_mean": 2.1705233759880067,
            "error_reduction_vs_all": 0.2557616789340973,
            "false_accept_high_error_rate": 0.014,
            "false_reject_low_error_rate": 0.03
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.6369534134864807,
            "accepted_mean": 1.4488819861412048,
            "rejected_mean": 2.0700549340248107,
            "error_reduction_vs_all": 0.4658797109127044,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.08
          }
        ],
        "seed0_only": [
          {
            "reject_rate": 0.1,
            "threshold": 2.2260414361953735,
            "accepted_mean": 1.8553364290131462,
            "rejected_mean": 2.564272773265839,
            "error_reduction_vs_all": 0.0708936344252693,
            "false_accept_high_error_rate": 0.2222222222222222,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.25,
            "threshold": 2.0386186838150024,
            "accepted_mean": 1.7717185123761494,
            "rejected_mean": 2.389764716625214,
            "error_reduction_vs_all": 0.1545115510622661,
            "false_accept_high_error_rate": 0.09333333333333334,
            "false_reject_low_error_rate": 0.0
          },
          {
            "reject_rate": 0.5,
            "threshold": 1.843848466873169,
            "accepted_mean": 1.665837494134903,
            "rejected_mean": 2.186622632741928,
            "error_reduction_vs_all": 0.2603925693035125,
            "false_accept_high_error_rate": 0.03,
            "false_reject_low_error_rate": 0.04
          },
          {
            "reject_rate": 0.75,
            "threshold": 1.6643955707550049,
            "accepted_mean": 1.461481282711029,
            "rejected_mean": 2.0811463236808776,
            "error_reduction_vs_all": 0.46474878072738646,
            "false_accept_high_error_rate": 0.0,
            "false_reject_low_error_rate": 0.1
          }
        ]
      }
    }
  }
]
```
