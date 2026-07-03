# Franka Wrist Camera Isaac Lab Repo Setup and Script Test Report

Goal:
Clone, inspect, setup, and test the existing repo as-is.

No object replacement yet.
No new assets yet.
No code rewrite yet.
## Git/Auth environment check
whoami: redafrix
date: Fri Jun 12 09:45:33 AM CEST 2026
git version:
git version 2.34.1

git remotes/credentials visible config names only:
user.name=redafrix
user.email=redafrix2002@gmail.com
color.ui=true
core.editor=code --wait
[REDACTED]
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
[REDACTED]
[REDACTED]
[REDACTED]
[REDACTED]
safe.directory=/home/redafrix/tests/internship
safe.directory=/home/redafrix/tests/internship

SSH GitHub test:
git@github.com: Permission denied (public[REDACTED]
Trying SSH clone first...
SSH clone failed, trying HTTPS clone...

## Repo git state
origin	https://github.com/Gontary101/franka_wrist_camera_isaaclab.git (fetch)
origin	https://github.com/Gontary101/franka_wrist_camera_isaaclab.git (push)
master
5029899cb489ede48fc524e4f76930832e9607c8

## Complete file inventory
./agent_camera.mp4 | 1404811 bytes
./AGENTS.md | 2575 bytes
./camera_probes/wrist_probe_000100.png | 1647 bytes
./camera_probes/wrist_probe_000200.png | 1647 bytes
./camera_probes/wrist_probe_000300.png | 1647 bytes
./camera_probes/wrist_probe_000400.png | 1647 bytes
./camera_probes/wrist_probe_000500.png | 1647 bytes
./camera_probes/wrist_probe_000600.png | 1647 bytes
./configs/collection.yaml | 601 bytes
./configs/object_catalog.generated.yaml | 12921 bytes
./configs/object_catalog.yaml | 1216 bytes
./configs/objects.yaml | 354 bytes
./configs/scene.yaml | 347 bytes
./.gitignore | 122 bytes
./guidelines.md | 4093 bytes
./objects/apple/apple00.usd | 131887 bytes
./objects/apple/apple01.usd | 39987 bytes
./objects/apple/apple02.usd | 29510 bytes
./objects/apple/apple03.usd | 23360 bytes
./objects/apple/apple04.usd | 29510 bytes
./objects/apple/apple05.usd | 23481 bytes
./objects/apple/apple06.usd | 29510 bytes
./objects/apple/apple07.usd | 30706 bytes
./objects/apple/apple08.usd | 39142 bytes
./objects/apple/apple09.usd | 3696259 bytes
./objects/apple/apple10.usd | 14994 bytes
./objects/apple/apple11.usd | 2311013 bytes
./objects/apple/apple12.usd | 29161 bytes
./objects/apple/apple13.usd | 67670 bytes
./objects/apple/apple14.usd | 327733 bytes
./objects/apple/apple15.usd | 1922025 bytes
./objects/apple/apple18.usd | 53141 bytes
./objects/apple/apple19.usd | 29511 bytes
./objects/apple/apple20.usd | 38397 bytes
./objects/apple/apple22.usd | 43614 bytes
./objects/apple/texture/apple00.jpg | 73722 bytes
./objects/apple/texture/apple01.jpg | 122974 bytes
./objects/apple/texture/apple02.jpg | 1163832 bytes
./objects/apple/texture/apple03.jpg | 1056726 bytes
./objects/apple/texture/apple04.jpg | 1149503 bytes
./objects/apple/texture/apple05.jpg | 57327 bytes
./objects/apple/texture/apple06.jpg | 1178107 bytes
./objects/apple/texture/apple07.jpg | 1345388 bytes
./objects/apple/texture/apple08.jpg | 25964 bytes
./objects/apple/texture/apple09.jpg | 1011443 bytes
./objects/apple/texture/apple10.jpg | 51514 bytes
./objects/apple/texture/apple11.jpg | 78501 bytes
./objects/apple/texture/apple12.jpg | 973024 bytes
./objects/apple/texture/apple13.jpg | 58233 bytes
./objects/apple/texture/apple14.jpg | 134347 bytes
./objects/apple/texture/apple15.jpg | 1038439 bytes
./objects/apple/texture/apple18.jpg | 1158918 bytes
./objects/apple/texture/apple19.jpg | 1157642 bytes
./objects/apple/texture/apple20.jpg | 100773 bytes
./objects/apple/texture/apple22.jpg | 1637741 bytes
./objects/avocado/avocado00.usd | 9325591 bytes
./objects/avocado/avocado01.usd | 66041 bytes
./objects/avocado/avocado02.usd | 18681 bytes
./objects/avocado/avocado04.usd | 2021573 bytes
./objects/avocado/avocado05.usd | 5836254 bytes
./objects/avocado/avocado06.usd | 12422 bytes
./objects/avocado/avocado08.usd | 13130 bytes
./objects/avocado/texture/avocado00.jpg | 1358470 bytes
./objects/avocado/texture/avocado01.jpg | 123716 bytes
./objects/avocado/texture/avocado02.jpg | 990365 bytes
./objects/avocado/texture/avocado04.jpg | 143864 bytes
./objects/avocado/texture/avocado05.jpg | 193663 bytes
./objects/avocado/texture/avocado06.jpg | 938326 bytes
./objects/avocado/texture/avocado08.jpg | 443453 bytes
./objects/beer/beer00.usd | 36409 bytes
./objects/beer/beer01.usd | 59564 bytes
./objects/beer/beer03.usd | 26388 bytes
./objects/beer/beer05.usd | 110406 bytes
./objects/beer/beer07.usd | 351073 bytes
./objects/beer/beer09.usd | 14373 bytes
./objects/beer/beer13.usd | 19887 bytes
./objects/beer/beer19.usd | 122046 bytes
./objects/beer/texture/beer00.jpg | 999755 bytes
./objects/beer/texture/beer01.jpg | 880919 bytes
./objects/beer/texture/beer03.jpg | 137474 bytes
./objects/beer/texture/beer05.jpg | 119769 bytes
./objects/beer/texture/beer07.jpg | 17475 bytes
./objects/beer/texture/beer09.jpg | 419744 bytes
./objects/beer/texture/beer13.jpg | 671660 bytes
./objects/beer/texture/beer19.jpg | 12858 bytes
./objects/bottle/dbottle02.usd | 553832 bytes
./objects/bottle/dbottle04.usd | 12503154 bytes
./objects/bottle/texture/bottled_drink02.jpg | 764968 bytes
./objects/bottle/texture/bottled_drink04.jpg | 102138 bytes
./objects/bottle/texture/bottled_water01.jpg | 5338 bytes
./objects/bottle/texture/bottled_water02.jpg | 263904 bytes
./objects/bottle/texture/bottled_water11.jpg | 74171 bytes
./objects/bottle/texture/water_bottle07.jpg | 65433 bytes
./objects/bottle/texture/water_bottle08.jpg | 84721 bytes
./objects/bottle/texture/water_bottle23.jpg | 973833 bytes
./objects/bottle/wbottle01.usd | 71844 bytes
./objects/bottle/wbottle02.usd | 5276709 bytes
./objects/bottle/wbottle07.usd | 2872560 bytes
./objects/bottle/wbottle08.usd | 197846 bytes
./objects/bottle/wbottle11.usd | 691595 bytes
./objects/bottle/wbottle12.usd | 720382 bytes
./objects/bottle/wbottle17.usd | 25723799 bytes
./objects/bottle/wbottle23.usd | 321711 bytes
./objects/bowl/bowl00.usd | 27021 bytes
./objects/bowl/bowl01.usd | 24306 bytes
./objects/bowl/bowl02.usd | 17392 bytes
./objects/bowl/bowl04.usd | 2965944 bytes
./objects/bowl/bowl05.usd | 51921 bytes
./objects/bowl/bowl06.usd | 1700358 bytes
./objects/bowl/bowl07.usd | 17568 bytes
./objects/bowl/bowl08.usd | 50679 bytes
./objects/bowl/bowl09.usd | 1482253 bytes
./objects/bowl/bowl10.usd | 80310 bytes
./objects/bowl/bowl11.usd | 716911 bytes
./objects/bowl/bowl12.usd | 41663 bytes
./objects/bowl/bowl13.usd | 35245 bytes
./objects/bowl/bowl14.usd | 27062 bytes
./objects/bowl/bowl15.usd | 22338 bytes
./objects/bowl/bowl16.usd | 75105 bytes
./objects/bowl/bowl17.usd | 2035754 bytes
./objects/bowl/bowl18.usd | 28476 bytes
./objects/bowl/bowl19.usd | 731345 bytes
./objects/bowl/texture/bowl00.jpg | 11165 bytes
./objects/bowl/texture/bowl01.jpg | 50952 bytes
./objects/bowl/texture/bowl02.jpg | 91126 bytes
./objects/bowl/texture/bowl04.jpg | 17197 bytes
./objects/bowl/texture/bowl06.jpg | 168805 bytes
./objects/bowl/texture/bowl07.jpg | 33303 bytes
./objects/bowl/texture/bowl08.jpg | 192215 bytes
./objects/bowl/texture/bowl09.jpg | 57445 bytes
./objects/bowl/texture/bowl10.jpg | 678292 bytes
./objects/bowl/texture/bowl11.jpg | 85227 bytes
./objects/bowl/texture/bowl12.jpg | 109567 bytes
./objects/bowl/texture/bowl13.jpg | 166330 bytes
./objects/bowl/texture/bowl14.jpg | 1593908 bytes
./objects/bowl/texture/bowl15.jpg | 479592 bytes
./objects/bowl/texture/bowl16.jpg | 1053070 bytes
./objects/bowl/texture/bowl17.jpg | 161506 bytes
./objects/bowl/texture/bowl18.jpg | 24258 bytes
./objects/bowl/texture/bowl19.jpg | 560619 bytes
./objects/box/box00.usd | 142625 bytes
./objects/box/box01.usd | 141739 bytes
./objects/box/box02.usd | 142602 bytes
./objects/box/box03.usd | 141730 bytes
./objects/box/box04.usd | 141730 bytes
./objects/box/box05.usd | 142620 bytes
./objects/box/box06.usd | 9571 bytes
./objects/box/box08.usd | 52621 bytes
./objects/box/box09.usd | 50213 bytes
./objects/box/box10.usd | 53148 bytes
./objects/box/box11.usd | 52142 bytes
./objects/box/box12.usd | 54083 bytes
./objects/box/box13.usd | 54071 bytes
./objects/box/box14.usd | 55987 bytes
./objects/box/box15.usd | 56931 bytes
./objects/box/texture/box06.jpg | 128373 bytes
./objects/box/texture/box08.jpg | 132814 bytes
./objects/box/texture/box09.jpg | 103386 bytes
./objects/box/texture/box10.jpg | 110984 bytes
./objects/box/texture/box11.jpg | 95642 bytes
./objects/box/texture/box12.jpg | 146334 bytes
./objects/box/texture/box13.jpg | 107431 bytes
./objects/box/texture/box14.jpg | 132368 bytes
./objects/box/texture/box15.jpg | 120840 bytes
./objects/can/can00.usd | 252628 bytes
./objects/can/can02.usd | 34609 bytes
./objects/can/can03.usd | 532639 bytes
./objects/can/can04.usd | 127156 bytes
./objects/can/can11.usd | 716656 bytes
./objects/can/can12.usd | 232394 bytes
./objects/can/can13.usd | 86250 bytes
./objects/can/can15.usd | 35863 bytes
./objects/can/fcan01.usd | 621150 bytes
./objects/can/fcan03.usd | 20056 bytes
./objects/can/fcan04.usd | 100288 bytes
./objects/can/fcan05.usd | 5224553 bytes
./objects/can/fcan08.usd | 66226 bytes
./objects/can/fcan11.usd | 25573 bytes
./objects/can/fcan15.usd | 17066 bytes
./objects/can/fcan17.usd | 446873 bytes
./objects/can/fcan18.usd | 446877 bytes
./objects/can/texture/can00.jpg | 554337 bytes
./objects/can/texture/can02.jpg | 350071 bytes
./objects/can/texture/can03.jpg | 663495 bytes
./objects/can/texture/can04.jpg | 76972 bytes
./objects/can/texture/can11.jpg | 74525 bytes
./objects/can/texture/can12.jpg | 1897 bytes
./objects/can/texture/can13.jpg | 156621 bytes
./objects/can/texture/can15.jpg | 1063805 bytes
./objects/can/texture/canned_food01.jpg | 42431 bytes
./objects/can/texture/canned_food03.jpg | 1568548 bytes
./objects/can/texture/canned_food04.jpg | 136496 bytes
./objects/can/texture/canned_food05.jpg | 110298 bytes
./objects/can/texture/canned_food08.jpg | 839008 bytes
./objects/can/texture/canned_food11.jpg | 96964 bytes
./objects/can/texture/canned_food15.jpg | 974721 bytes
./objects/can/texture/canned_food17.jpg | 1372292 bytes
./objects/can/texture/canned_food18.jpg | 1245745 bytes
./objects/citation.tex | 436 bytes
./objects/cup/cup00.usd | 40140 bytes
./objects/cup/cup01.usd | 60629 bytes
./objects/cup/cup02.usd | 60633 bytes
./objects/cup/cup03.usd | 60627 bytes
./objects/cup/cup04.usd | 60631 bytes
./objects/cup/cup05.usd | 196488 bytes
./objects/cup/cup06.usd | 196498 bytes
./objects/cup/cup07.usd | 196506 bytes
./objects/cup/cup08.usd | 196498 bytes
./objects/cup/cup09.usd | 196501 bytes
./objects/cup/texture/cup01.jpg | 25479 bytes
./objects/cup/texture/cup02.jpg | 146632 bytes
./objects/cup/texture/cup03.jpg | 88795 bytes
./objects/cup/texture/cup04.jpg | 36232 bytes
./objects/egg/egg00.usd | 73155 bytes
./objects/egg/egg03.usd | 84496 bytes
./objects/egg/egg04.usd | 1058929 bytes
./objects/egg/egg05.usd | 6820454 bytes
./objects/egg/egg06.usd | 981286 bytes
./objects/egg/egg07.usd | 65520 bytes
./objects/egg/egg09.usd | 284539 bytes
./objects/egg/egg10.usd | 5597002 bytes
./objects/egg/egg11.usd | 72302 bytes
./objects/egg/egg12.usd | 929339 bytes
./objects/egg/egg13.usd | 148273 bytes
./objects/egg/texture/egg03.jpg | 724259 bytes
./objects/egg/texture/egg04.jpg | 45565 bytes
./objects/egg/texture/egg05.jpg | 147465 bytes
./objects/egg/texture/egg06.jpg | 59536 bytes
./objects/egg/texture/egg07.jpg | 17013 bytes
./objects/egg/texture/egg09.jpg | 16234 bytes
./objects/egg/texture/egg10.jpg | 149274 bytes
./objects/egg/texture/egg11.jpg | 34829 bytes
./objects/egg/texture/egg13.jpg | 1826683 bytes
./objects/kiwi/kiwi00.usd | 14189170 bytes
./objects/kiwi/kiwi05.usd | 11234456 bytes
./objects/kiwi/kiwi07.usd | 704381 bytes
./objects/kiwi/texture/kiwi00.jpg | 1249494 bytes
./objects/kiwi/texture/kiwi05.jpg | 42242 bytes
./objects/kiwi/texture/kiwi07.jpg | 1828723 bytes
./objects/lemon/lemon01.usd | 13427088 bytes
./objects/lemon/lemon02.usd | 18083512 bytes
./objects/lemon/lemon03.usd | 781028 bytes
./objects/lemon/lemon04.usd | 102008 bytes
./objects/lemon/lemon05.usd | 58962 bytes
./objects/lemon/lemon06.usd | 14944860 bytes
./objects/lemon/lemon08.usd | 703704 bytes
./objects/lemon/lemon09.usd | 624741 bytes
./objects/lemon/lemon10.usd | 104983 bytes
./objects/lemon/lemon12.usd | 107836 bytes
./objects/lemon/lemon13.usd | 9644698 bytes
./objects/lemon/lemon14.usd | 1586565 bytes
./objects/lemon/lemon15.usd | 83360 bytes
./objects/lemon/texture/lemon01.jpg | 1454693 bytes
./objects/lemon/texture/lemon02.jpg | 797466 bytes
./objects/lemon/texture/lemon03.jpg | 54807 bytes
./objects/lemon/texture/lemon04.jpg | 562213 bytes
./objects/lemon/texture/lemon05.jpg | 876327 bytes
./objects/lemon/texture/lemon06.jpg | 571897 bytes
./objects/lemon/texture/lemon08.jpg | 69538 bytes
./objects/lemon/texture/lemon09.jpg | 756685 bytes
./objects/lemon/texture/lemon10.jpg | 58093 bytes
./objects/lemon/texture/lemon12.jpg | 512640 bytes
./objects/lemon/texture/lemon13.jpg | 71398 bytes
./objects/lemon/texture/lemon14.jpg | 65029 bytes
./objects/lemon/texture/lemon15.jpg | 1071022 bytes
./objects/lime/lime00.usd | 3621760 bytes
./objects/lime/lime01.usd | 120310 bytes
./objects/lime/lime02.usd | 165025 bytes
./objects/lime/lime03.usd | 406684 bytes
./objects/lime/texture/lime00.jpg | 899817 bytes
./objects/lime/texture/lime01.jpg | 115506 bytes
./objects/lime/texture/lime02.jpg | 107064 bytes
./objects/lime/texture/lime03.jpg | 71714 bytes
./objects/metadata.json | 36654 bytes
./objects/onion/onion00.usd | 16068 bytes
./objects/onion/onion02.usd | 29522 bytes
./objects/onion/onion04.usd | 12010663 bytes
./objects/onion/onion07.usd | 3849269 bytes
./objects/onion/onion08.usd | 3561473 bytes
./objects/onion/onion09.usd | 89937 bytes
./objects/onion/onion10.usd | 1978448 bytes
./objects/onion/texture/onion00.jpg | 115822 bytes
./objects/onion/texture/onion02.jpg | 1041250 bytes
./objects/onion/texture/onion04.jpg | 2023269 bytes
./objects/onion/texture/onion07.jpg | 50005 bytes
./objects/onion/texture/onion08.jpg | 105106 bytes
./objects/onion/texture/onion09.jpg | 1355704 bytes
./objects/onion/texture/onion10.jpg | 111574 bytes
./objects/orange/orange02.usd | 23860 bytes
./objects/orange/orange03.usd | 26602 bytes
./objects/orange/orange05.usd | 16532 bytes
./objects/orange/orange09.usd | 7013910 bytes
./objects/orange/orange12.usd | 54395 bytes
./objects/orange/orange13.usd | 1928500 bytes
./objects/orange/texture/orange02.jpg | 118975 bytes
./objects/orange/texture/orange03.jpg | 1594273 bytes
./objects/orange/texture/orange04.jpg | 115927 bytes
./objects/orange/texture/orange05.jpg | 1006254 bytes
./objects/orange/texture/orange09.jpg | 86319 bytes
./objects/orange/texture/orange12.jpg | 31806 bytes
./objects/orange/texture/orange13.jpg | 91143 bytes
./objects/peach/peach01.usd | 1250396 bytes
./objects/peach/peach02.usd | 35717 bytes
./objects/peach/peach03.usd | 181890 bytes
./objects/peach/peach05.usd | 3697804 bytes
./objects/peach/peach06.usd | 258911 bytes
./objects/peach/texture/peach01.jpg | 102979 bytes
./objects/peach/texture/peach02.jpg | 84683 bytes
./objects/peach/texture/peach03.jpg | 136837 bytes
./objects/peach/texture/peach05.jpg | 67124 bytes
./objects/peach/texture/peach06.jpg | 26191 bytes
./objects/placemat/placemat00.usd | 4376 bytes
./objects/placemat/placemat01.usd | 5982 bytes
./objects/placemat/placemat02.usd | 5499 bytes
./objects/placemat/placemat03.usd | 5191 bytes
./objects/placemat/placemat04.usd | 5984 bytes
./objects/placemat/placemat05.usd | 5191 bytes
./objects/placemat/texture/placemat00.png | 140982 bytes
./objects/placemat/texture/placemat01.png | 22444 bytes
./objects/placemat/texture/placemat02.png | 250162 bytes
./objects/placemat/texture/placemat03.png | 212381 bytes
./objects/placemat/texture/placemat04.png | 96771 bytes
./objects/placemat/texture/placemat05.png | 173281 bytes
./objects/plate/plate00.usd | 53477 bytes
./objects/plate/plate01.usd | 90298 bytes
./objects/plate/plate02.usd | 98666 bytes
./objects/plate/plate03.usd | 681763 bytes
./objects/plate/plate04.usd | 23747 bytes
./objects/plate/plate05.usd | 30379 bytes
./objects/plate/plate06.usd | 64111 bytes
./objects/plate/plate07.usd | 19820 bytes
./objects/plate/plate08.usd | 26677 bytes
./objects/plate/plate09.usd | 22926 bytes
./objects/plate/plate10.usd | 30380 bytes
./objects/plate/plate12.usd | 79940 bytes
./objects/plate/plate13.usd | 72818 bytes
./objects/plate/plate14.usd | 364788 bytes
./objects/plate/plate15.usd | 33356 bytes
./objects/plate/plate16.usd | 2326145 bytes
./objects/plate/texture/plate00.jpg | 84003 bytes
./objects/plate/texture/plate02.jpg | 58188 bytes
./objects/plate/texture/plate04.jpg | 17674 bytes
./objects/plate/texture/plate05.jpg | 314968 bytes
./objects/plate/texture/plate06.jpg | 92760 bytes
./objects/plate/texture/plate07.jpg | 76625 bytes
./objects/plate/texture/plate08.jpg | 1149481 bytes
./objects/plate/texture/plate10.jpg | 1046634 bytes
./objects/plate/texture/plate12.jpg | 21654 bytes
./objects/plate/texture/plate14.jpg | 121336 bytes
./objects/plate/texture/plate16.jpg | 579534 bytes
./objects/potato/potato00.usd | 9123591 bytes
./objects/potato/potato02.usd | 64656 bytes
./objects/potato/potato03.usd | 11607 bytes
./objects/potato/potato06.usd | 92306 bytes
./objects/potato/potato07.usd | 237510 bytes
./objects/potato/potato10.usd | 78838 bytes
./objects/potato/potato13.usd | 8855 bytes
./objects/potato/potato14.usd | 22469 bytes
./objects/potato/potato16.usd | 14361 bytes
./objects/potato/potato17.usd | 4848966 bytes
./objects/potato/potato18.usd | 393049 bytes
./objects/potato/texture/potato00.jpg | 1315122 bytes
./objects/potato/texture/potato02.jpg | 76934 bytes
./objects/potato/texture/potato03.jpg | 12537 bytes
./objects/potato/texture/potato06.jpg | 1331569 bytes
./objects/potato/texture/potato07.jpg | 1107393 bytes
./objects/potato/texture/potato10.jpg | 815691 bytes
./objects/potato/texture/potato13.jpg | 47014 bytes
./objects/potato/texture/potato14.jpg | 110175 bytes
./objects/potato/texture/potato16.jpg | 959361 bytes
./objects/potato/texture/potato17.jpg | 107623 bytes
./objects/potato/texture/potato18.jpg | 778968 bytes
./objects/tangerine/tangerine00.usd | 113247 bytes
./objects/tangerine/tangerine03.usd | 781084 bytes
./objects/tangerine/tangerine04.usd | 140866 bytes
./objects/tangerine/tangerine05.usd | 185358 bytes
./objects/tangerine/tangerine06.usd | 61008 bytes
./objects/tangerine/texture/tangerine00.jpg | 1092511 bytes
./objects/tangerine/texture/tangerine03.jpg | 1163074 bytes
./objects/tangerine/texture/tangerine04.jpg | 65278 bytes
./objects/tangerine/texture/tangerine05.jpg | 1523078 bytes
./objects/tangerine/texture/tangerine06.jpg | 910619 bytes
./objects/tomato/texture/tomato01.jpg | 21007 bytes
./objects/tomato/texture/tomato03.jpg | 32698 bytes
./objects/tomato/texture/tomato07.jpg | 115621 bytes
./objects/tomato/tomato01.usd | 14974 bytes
./objects/tomato/tomato02.usd | 58544 bytes
./objects/tomato/tomato03.usd | 1789996 bytes
./objects/tomato/tomato07.usd | 4387772 bytes
./objects/tray/texture/tray00.jpg | 866339 bytes
./objects/tray/texture/tray02.jpg | 104032 bytes
./objects/tray/texture/tray03.jpg | 1707426 bytes
./objects/tray/texture/tray04.jpg | 1273984 bytes
./objects/tray/texture/tray05.jpg | 104164 bytes
./objects/tray/texture/tray06.jpg | 148209 bytes
./objects/tray/texture/tray07.jpg | 103146 bytes
./objects/tray/texture/tray08.jpg | 112283 bytes
./objects/tray/texture/tray09.jpg | 96795 bytes
./objects/tray/texture/tray10.jpg | 137288 bytes
./objects/tray/texture/tray11.jpg | 106956 bytes
./objects/tray/texture/tray12.jpg | 97579 bytes
./objects/tray/tray04.usd | 22783 bytes
./objects/tray/tray05.usd | 43045 bytes
./objects/tray/tray06.usd | 43992 bytes
./objects/tray/tray07.usd | 43992 bytes
./objects/tray/tray08.usd | 43480 bytes
./objects/tray/tray09.usd | 43480 bytes
./objects/tray/tray10.usd | 43483 bytes
./objects/tray/tray11.usd | 44449 bytes
./objects/tray/tray12.usd | 44449 bytes
./objects/tree.md | 13563 bytes
./objects/unseen/apple99.usd | 30494 bytes
./objects/unseen/can99.usd | 716663 bytes
./objects/unseen/cup99.usd | 60631 bytes
./objects/unseen/dbottle99.usd | 553832 bytes
./objects/unseen/peach99.usd | 259898 bytes
./objects/unseen/texture/apple99.jpg | 1209414 bytes
./objects/unseen/texture/bottled_drink99.jpg | 804507 bytes
./objects/unseen/texture/can99.jpg | 327663 bytes
./objects/unseen/texture/cup99.jpg | 105726 bytes
./objects/unseen/texture/peach99.jpg | 57648 bytes
./pyproject.toml | 411 bytes
./README.md | 3155 bytes
./run_collect | 1143 bytes
./run_collect.sh | 1143 bytes
./run_sim.sh | 1116 bytes
./scripts/collect.py | 2466 bytes
./scripts/debug_scene.py | 7492 bytes
./scripts/export_ila.py | 924 bytes
./scripts/generate_object_catalog.py | 1267 bytes
./scripts/inspect_collection.py | 4358 bytes
./scripts/inspect_episode.py | 1087 bytes
./scripts/inspect_ila_dataset.py | 1334 bytes
./scripts/inspect_object_catalog.py | 1863 bytes
./scripts/inspect_objects.py | 658 bytes
./scripts/run.sh | 365 bytes
./scripts/visualize_ila_episode.py | 3006 bytes
./scripts/write_ila_splits.py | 1007 bytes
./scripts/write_ila_stats.py | 764 bytes
./sim_output.log | 0 bytes
./src/franka_wrist_camera_scene/app/camera_warmup.py | 1214 bytes
./src/franka_wrist_camera_scene/app/__init__.py | 44 bytes
./src/franka_wrist_camera_scene/app/launcher.py | 1195 bytes
./src/franka_wrist_camera_scene/collection/__init__.py | 52 bytes
./src/franka_wrist_camera_scene/collection/pick_place.py | 9690 bytes
./src/franka_wrist_camera_scene/control/gripper.py | 1611 bytes
./src/franka_wrist_camera_scene/control/ik.py | 3706 bytes
./src/franka_wrist_camera_scene/control/__init__.py | 84 bytes
./src/franka_wrist_camera_scene/control/motion_primitives.py | 4461 bytes
./src/franka_wrist_camera_scene/control/trajectory.py | 2561 bytes
./src/franka_wrist_camera_scene/datasets/ila.py | 3267 bytes
./src/franka_wrist_camera_scene/datasets/__init__.py | 23 bytes
./src/franka_wrist_camera_scene/debug/camera_probe.py | 1594 bytes
./src/franka_wrist_camera_scene/debug/__init__.py | 76 bytes
./src/franka_wrist_camera_scene/debug/video_recorder.py | 2444 bytes
./src/franka_wrist_camera_scene/debug/visualization.py | 1989 bytes
./src/franka_wrist_camera_scene/episode/__init__.py | 55 bytes
./src/franka_wrist_camera_scene/episode/manifest.py | 3408 bytes
./src/franka_wrist_camera_scene/episode/recorder.py | 6904 bytes
./src/franka_wrist_camera_scene/episode/reset.py | 1738 bytes
./src/franka_wrist_camera_scene/episode/schema.py | 1136 bytes
./src/franka_wrist_camera_scene/episode/success.py | 899 bytes
./src/franka_wrist_camera_scene/export/ila.py | 3841 bytes
./src/franka_wrist_camera_scene/export/ila_splits.py | 1444 bytes
./src/franka_wrist_camera_scene/export/ila_stats.py | 1935 bytes
./src/franka_wrist_camera_scene/export/__init__.py | 25 bytes
./src/franka_wrist_camera_scene/__init__.py | 57 bytes
./src/franka_wrist_camera_scene/objects/catalog_generator.py | 3852 bytes
./src/franka_wrist_camera_scene/objects/catalog.py | 2135 bytes
./src/franka_wrist_camera_scene/objects/__init__.py | 42 bytes
./src/franka_wrist_camera_scene/objects/registry.py | 1803 bytes
./src/franka_wrist_camera_scene/objects/selection.py | 709 bytes
./src/franka_wrist_camera_scene/policies/circle_policy.py | 1424 bytes
./src/franka_wrist_camera_scene/policies/__init__.py | 66 bytes
./src/franka_wrist_camera_scene/policies/pick_place_scripted.py | 8802 bytes
./src/franka_wrist_camera_scene/policies/scripted_base.py | 377 bytes
./src/franka_wrist_camera_scene/scene/__init__.py | 74 bytes
./src/franka_wrist_camera_scene/scene/lighting.py | 654 bytes
./src/franka_wrist_camera_scene/scene/object_context.py | 886 bytes
./src/franka_wrist_camera_scene/scene/tabletop.py | 4292 bytes
./src/franka_wrist_camera_scene/settings.py | 812 bytes
./src/franka_wrist_camera_scene/tasks/base.py | 268 bytes
./src/franka_wrist_camera_scene/tasks/__init__.py | 67 bytes
./src/franka_wrist_camera_scene/tasks/pick_place.py | 2852 bytes
./src/franka_wrist_camera_scene/tasks/sampling.py | 2011 bytes
./src/franka_wrist_camera_scene/utils/__init__.py | 80 bytes
./src/franka_wrist_camera_scene/utils/paths.py | 624 bytes
./wrist_camera.mp4 | 788890 bytes

## Directory tree
.
./agent_camera.mp4
./AGENTS.md
./camera_probes
./camera_probes/wrist_probe_000100.png
./camera_probes/wrist_probe_000200.png
./camera_probes/wrist_probe_000300.png
./camera_probes/wrist_probe_000400.png
./camera_probes/wrist_probe_000500.png
./camera_probes/wrist_probe_000600.png
./configs
./configs/collection.yaml
./configs/object_catalog.generated.yaml
./configs/object_catalog.yaml
./configs/objects.yaml
./configs/scene.yaml
./.gitignore
./guidelines.md
./objects
./objects/apple
./objects/apple/apple00.usd
./objects/apple/apple01.usd
./objects/apple/apple02.usd
./objects/apple/apple03.usd
./objects/apple/apple04.usd
./objects/apple/apple05.usd
./objects/apple/apple06.usd
./objects/apple/apple07.usd
./objects/apple/apple08.usd
./objects/apple/apple09.usd
./objects/apple/apple10.usd
./objects/apple/apple11.usd
./objects/apple/apple12.usd
./objects/apple/apple13.usd
./objects/apple/apple14.usd
./objects/apple/apple15.usd
./objects/apple/apple18.usd
./objects/apple/apple19.usd
./objects/apple/apple20.usd
./objects/apple/apple22.usd
./objects/apple/texture
./objects/apple/texture/apple00.jpg
./objects/apple/texture/apple01.jpg
./objects/apple/texture/apple02.jpg
./objects/apple/texture/apple03.jpg
./objects/apple/texture/apple04.jpg
./objects/apple/texture/apple05.jpg
./objects/apple/texture/apple06.jpg
./objects/apple/texture/apple07.jpg
./objects/apple/texture/apple08.jpg
./objects/apple/texture/apple09.jpg
./objects/apple/texture/apple10.jpg
./objects/apple/texture/apple11.jpg
./objects/apple/texture/apple12.jpg
./objects/apple/texture/apple13.jpg
./objects/apple/texture/apple14.jpg
./objects/apple/texture/apple15.jpg
./objects/apple/texture/apple18.jpg
./objects/apple/texture/apple19.jpg
./objects/apple/texture/apple20.jpg
./objects/apple/texture/apple22.jpg
./objects/avocado
./objects/avocado/avocado00.usd
./objects/avocado/avocado01.usd
./objects/avocado/avocado02.usd
./objects/avocado/avocado04.usd
./objects/avocado/avocado05.usd
./objects/avocado/avocado06.usd
./objects/avocado/avocado08.usd
./objects/avocado/texture
./objects/avocado/texture/avocado00.jpg
./objects/avocado/texture/avocado01.jpg
./objects/avocado/texture/avocado02.jpg
./objects/avocado/texture/avocado04.jpg
./objects/avocado/texture/avocado05.jpg
./objects/avocado/texture/avocado06.jpg
./objects/avocado/texture/avocado08.jpg
./objects/beer
./objects/beer/beer00.usd
./objects/beer/beer01.usd
./objects/beer/beer03.usd
./objects/beer/beer05.usd
./objects/beer/beer07.usd
./objects/beer/beer09.usd
./objects/beer/beer13.usd
./objects/beer/beer19.usd
./objects/beer/texture
./objects/beer/texture/beer00.jpg
./objects/beer/texture/beer01.jpg
./objects/beer/texture/beer03.jpg
./objects/beer/texture/beer05.jpg
./objects/beer/texture/beer07.jpg
./objects/beer/texture/beer09.jpg
./objects/beer/texture/beer13.jpg
./objects/beer/texture/beer19.jpg
./objects/bottle
./objects/bottle/dbottle02.usd
./objects/bottle/dbottle04.usd
./objects/bottle/texture
./objects/bottle/texture/bottled_drink02.jpg
./objects/bottle/texture/bottled_drink04.jpg
./objects/bottle/texture/bottled_water01.jpg
./objects/bottle/texture/bottled_water02.jpg
./objects/bottle/texture/bottled_water11.jpg
./objects/bottle/texture/water_bottle07.jpg
./objects/bottle/texture/water_bottle08.jpg
./objects/bottle/texture/water_bottle23.jpg
./objects/bottle/wbottle01.usd
./objects/bottle/wbottle02.usd
./objects/bottle/wbottle07.usd
./objects/bottle/wbottle08.usd
./objects/bottle/wbottle11.usd
./objects/bottle/wbottle12.usd
./objects/bottle/wbottle17.usd
./objects/bottle/wbottle23.usd
./objects/bowl
./objects/bowl/bowl00.usd
./objects/bowl/bowl01.usd
./objects/bowl/bowl02.usd
./objects/bowl/bowl04.usd
./objects/bowl/bowl05.usd
./objects/bowl/bowl06.usd
./objects/bowl/bowl07.usd
./objects/bowl/bowl08.usd
./objects/bowl/bowl09.usd
./objects/bowl/bowl10.usd
./objects/bowl/bowl11.usd
./objects/bowl/bowl12.usd
./objects/bowl/bowl13.usd
./objects/bowl/bowl14.usd
./objects/bowl/bowl15.usd
./objects/bowl/bowl16.usd
./objects/bowl/bowl17.usd
./objects/bowl/bowl18.usd
./objects/bowl/bowl19.usd
./objects/bowl/texture
./objects/bowl/texture/bowl00.jpg
./objects/bowl/texture/bowl01.jpg
./objects/bowl/texture/bowl02.jpg
./objects/bowl/texture/bowl04.jpg
./objects/bowl/texture/bowl06.jpg
./objects/bowl/texture/bowl07.jpg
./objects/bowl/texture/bowl08.jpg
./objects/bowl/texture/bowl09.jpg
./objects/bowl/texture/bowl10.jpg
./objects/bowl/texture/bowl11.jpg
./objects/bowl/texture/bowl12.jpg
./objects/bowl/texture/bowl13.jpg
./objects/bowl/texture/bowl14.jpg
./objects/bowl/texture/bowl15.jpg
./objects/bowl/texture/bowl16.jpg
./objects/bowl/texture/bowl17.jpg
./objects/bowl/texture/bowl18.jpg
./objects/bowl/texture/bowl19.jpg
./objects/box
./objects/box/box00.usd
./objects/box/box01.usd
./objects/box/box02.usd
./objects/box/box03.usd
./objects/box/box04.usd
./objects/box/box05.usd
./objects/box/box06.usd
./objects/box/box08.usd
./objects/box/box09.usd
./objects/box/box10.usd
./objects/box/box11.usd
./objects/box/box12.usd
./objects/box/box13.usd
./objects/box/box14.usd
./objects/box/box15.usd
./objects/box/texture
./objects/box/texture/box06.jpg
./objects/box/texture/box08.jpg
./objects/box/texture/box09.jpg
./objects/box/texture/box10.jpg
./objects/box/texture/box11.jpg
./objects/box/texture/box12.jpg
./objects/box/texture/box13.jpg
./objects/box/texture/box14.jpg
./objects/box/texture/box15.jpg
./objects/can
./objects/can/can00.usd
./objects/can/can02.usd
./objects/can/can03.usd
./objects/can/can04.usd
./objects/can/can11.usd
./objects/can/can12.usd
./objects/can/can13.usd
./objects/can/can15.usd
./objects/can/fcan01.usd
./objects/can/fcan03.usd
./objects/can/fcan04.usd
./objects/can/fcan05.usd
./objects/can/fcan08.usd
./objects/can/fcan11.usd
./objects/can/fcan15.usd
./objects/can/fcan17.usd
./objects/can/fcan18.usd
./objects/can/texture
./objects/can/texture/can00.jpg
./objects/can/texture/can02.jpg
./objects/can/texture/can03.jpg
./objects/can/texture/can04.jpg
./objects/can/texture/can11.jpg
./objects/can/texture/can12.jpg
./objects/can/texture/can13.jpg
./objects/can/texture/can15.jpg
./objects/can/texture/canned_food01.jpg
./objects/can/texture/canned_food03.jpg
./objects/can/texture/canned_food04.jpg
./objects/can/texture/canned_food05.jpg
./objects/can/texture/canned_food08.jpg
./objects/can/texture/canned_food11.jpg
./objects/can/texture/canned_food15.jpg
./objects/can/texture/canned_food17.jpg
./objects/can/texture/canned_food18.jpg
./objects/citation.tex
./objects/cup
./objects/cup/cup00.usd
./objects/cup/cup01.usd
./objects/cup/cup02.usd
./objects/cup/cup03.usd
./objects/cup/cup04.usd
./objects/cup/cup05.usd
./objects/cup/cup06.usd
./objects/cup/cup07.usd
./objects/cup/cup08.usd
./objects/cup/cup09.usd
./objects/cup/texture
./objects/cup/texture/cup01.jpg
./objects/cup/texture/cup02.jpg
./objects/cup/texture/cup03.jpg
./objects/cup/texture/cup04.jpg
./objects/egg
./objects/egg/egg00.usd
./objects/egg/egg03.usd
./objects/egg/egg04.usd
./objects/egg/egg05.usd
./objects/egg/egg06.usd
./objects/egg/egg07.usd
./objects/egg/egg09.usd
./objects/egg/egg10.usd
./objects/egg/egg11.usd
./objects/egg/egg12.usd
./objects/egg/egg13.usd
./objects/egg/texture
./objects/egg/texture/egg03.jpg
./objects/egg/texture/egg04.jpg
./objects/egg/texture/egg05.jpg
./objects/egg/texture/egg06.jpg
./objects/egg/texture/egg07.jpg
./objects/egg/texture/egg09.jpg
./objects/egg/texture/egg10.jpg
./objects/egg/texture/egg11.jpg
./objects/egg/texture/egg13.jpg
./objects/kiwi
./objects/kiwi/kiwi00.usd
./objects/kiwi/kiwi05.usd
./objects/kiwi/kiwi07.usd
./objects/kiwi/texture
./objects/kiwi/texture/kiwi00.jpg
./objects/kiwi/texture/kiwi05.jpg
./objects/kiwi/texture/kiwi07.jpg
./objects/lemon
./objects/lemon/lemon01.usd
./objects/lemon/lemon02.usd
./objects/lemon/lemon03.usd
./objects/lemon/lemon04.usd
./objects/lemon/lemon05.usd
./objects/lemon/lemon06.usd
./objects/lemon/lemon08.usd
./objects/lemon/lemon09.usd
./objects/lemon/lemon10.usd
./objects/lemon/lemon12.usd
./objects/lemon/lemon13.usd
./objects/lemon/lemon14.usd
./objects/lemon/lemon15.usd
./objects/lemon/texture
./objects/lemon/texture/lemon01.jpg
./objects/lemon/texture/lemon02.jpg
./objects/lemon/texture/lemon03.jpg
./objects/lemon/texture/lemon04.jpg
./objects/lemon/texture/lemon05.jpg
./objects/lemon/texture/lemon06.jpg
./objects/lemon/texture/lemon08.jpg
./objects/lemon/texture/lemon09.jpg
./objects/lemon/texture/lemon10.jpg
./objects/lemon/texture/lemon12.jpg
./objects/lemon/texture/lemon13.jpg
./objects/lemon/texture/lemon14.jpg
./objects/lemon/texture/lemon15.jpg
./objects/lime
./objects/lime/lime00.usd
./objects/lime/lime01.usd
./objects/lime/lime02.usd
./objects/lime/lime03.usd
./objects/lime/texture
./objects/lime/texture/lime00.jpg
./objects/lime/texture/lime01.jpg
./objects/lime/texture/lime02.jpg
./objects/lime/texture/lime03.jpg
./objects/metadata.json
./objects/onion
./objects/onion/onion00.usd
./objects/onion/onion02.usd
./objects/onion/onion04.usd
./objects/onion/onion07.usd
./objects/onion/onion08.usd
./objects/onion/onion09.usd
./objects/onion/onion10.usd
./objects/onion/texture
./objects/onion/texture/onion00.jpg
./objects/onion/texture/onion02.jpg
./objects/onion/texture/onion04.jpg
./objects/onion/texture/onion07.jpg
./objects/onion/texture/onion08.jpg
./objects/onion/texture/onion09.jpg
./objects/onion/texture/onion10.jpg
./objects/orange
./objects/orange/orange02.usd
./objects/orange/orange03.usd
./objects/orange/orange05.usd
./objects/orange/orange09.usd
./objects/orange/orange12.usd
./objects/orange/orange13.usd
./objects/orange/texture
./objects/orange/texture/orange02.jpg
./objects/orange/texture/orange03.jpg
./objects/orange/texture/orange04.jpg
./objects/orange/texture/orange05.jpg
./objects/orange/texture/orange09.jpg
./objects/orange/texture/orange12.jpg
./objects/orange/texture/orange13.jpg
./objects/peach
./objects/peach/peach01.usd
./objects/peach/peach02.usd
./objects/peach/peach03.usd
./objects/peach/peach05.usd
./objects/peach/peach06.usd
./objects/peach/texture
./objects/peach/texture/peach01.jpg
./objects/peach/texture/peach02.jpg
./objects/peach/texture/peach03.jpg
./objects/peach/texture/peach05.jpg
./objects/peach/texture/peach06.jpg
./objects/placemat
./objects/placemat/placemat00.usd
./objects/placemat/placemat01.usd
./objects/placemat/placemat02.usd
./objects/placemat/placemat03.usd
./objects/placemat/placemat04.usd
./objects/placemat/placemat05.usd
./objects/placemat/texture
./objects/placemat/texture/placemat00.png
./objects/placemat/texture/placemat01.png
./objects/placemat/texture/placemat02.png
./objects/placemat/texture/placemat03.png
./objects/placemat/texture/placemat04.png
./objects/placemat/texture/placemat05.png
./objects/plate
./objects/plate/plate00.usd
./objects/plate/plate01.usd
./objects/plate/plate02.usd
./objects/plate/plate03.usd
./objects/plate/plate04.usd
./objects/plate/plate05.usd
./objects/plate/plate06.usd
./objects/plate/plate07.usd
./objects/plate/plate08.usd
./objects/plate/plate09.usd
./objects/plate/plate10.usd
./objects/plate/plate12.usd
./objects/plate/plate13.usd
./objects/plate/plate14.usd
./objects/plate/plate15.usd
./objects/plate/plate16.usd
./objects/plate/texture
./objects/plate/texture/plate00.jpg
./objects/plate/texture/plate02.jpg
./objects/plate/texture/plate04.jpg
./objects/plate/texture/plate05.jpg
./objects/plate/texture/plate06.jpg
./objects/plate/texture/plate07.jpg
./objects/plate/texture/plate08.jpg
./objects/plate/texture/plate10.jpg
./objects/plate/texture/plate12.jpg
./objects/plate/texture/plate14.jpg
./objects/plate/texture/plate16.jpg
./objects/potato
./objects/potato/potato00.usd
./objects/potato/potato02.usd
./objects/potato/potato03.usd
./objects/potato/potato06.usd
./objects/potato/potato07.usd
./objects/potato/potato10.usd
./objects/potato/potato13.usd
./objects/potato/potato14.usd
./objects/potato/potato16.usd
./objects/potato/potato17.usd
./objects/potato/potato18.usd
./objects/potato/texture
./objects/potato/texture/potato00.jpg
./objects/potato/texture/potato02.jpg
./objects/potato/texture/potato03.jpg
./objects/potato/texture/potato06.jpg
./objects/potato/texture/potato07.jpg
./objects/potato/texture/potato10.jpg
./objects/potato/texture/potato13.jpg
./objects/potato/texture/potato14.jpg
./objects/potato/texture/potato16.jpg
./objects/potato/texture/potato17.jpg
./objects/potato/texture/potato18.jpg
./objects/tangerine
./objects/tangerine/tangerine00.usd
./objects/tangerine/tangerine03.usd
./objects/tangerine/tangerine04.usd
./objects/tangerine/tangerine05.usd
./objects/tangerine/tangerine06.usd
./objects/tangerine/texture
./objects/tangerine/texture/tangerine00.jpg
./objects/tangerine/texture/tangerine03.jpg
./objects/tangerine/texture/tangerine04.jpg
./objects/tangerine/texture/tangerine05.jpg
./objects/tangerine/texture/tangerine06.jpg
./objects/tomato
./objects/tomato/texture
./objects/tomato/texture/tomato01.jpg
./objects/tomato/texture/tomato03.jpg
./objects/tomato/texture/tomato07.jpg
./objects/tomato/tomato01.usd
./objects/tomato/tomato02.usd
./objects/tomato/tomato03.usd
./objects/tomato/tomato07.usd
./objects/tray
./objects/tray/texture
./objects/tray/texture/tray00.jpg
./objects/tray/texture/tray02.jpg
./objects/tray/texture/tray03.jpg
./objects/tray/texture/tray04.jpg
./objects/tray/texture/tray05.jpg
./objects/tray/texture/tray06.jpg
./objects/tray/texture/tray07.jpg
./objects/tray/texture/tray08.jpg
./objects/tray/texture/tray09.jpg
./objects/tray/texture/tray10.jpg
./objects/tray/texture/tray11.jpg
./objects/tray/texture/tray12.jpg
./objects/tray/tray04.usd
./objects/tray/tray05.usd
./objects/tray/tray06.usd
./objects/tray/tray07.usd
./objects/tray/tray08.usd
./objects/tray/tray09.usd
./objects/tray/tray10.usd
./objects/tray/tray11.usd
./objects/tray/tray12.usd
./objects/tree.md
./objects/unseen
./objects/unseen/apple99.usd
./objects/unseen/can99.usd
./objects/unseen/cup99.usd
./objects/unseen/dbottle99.usd
./objects/unseen/peach99.usd
./objects/unseen/texture
./objects/unseen/texture/apple99.jpg
./objects/unseen/texture/bottled_drink99.jpg
./objects/unseen/texture/can99.jpg
./objects/unseen/texture/cup99.jpg
./objects/unseen/texture/peach99.jpg
./pyproject.toml
./README.md
./run_collect
./run_collect.sh
./run_sim.sh
./scripts
./scripts/collect.py
./scripts/debug_scene.py
./scripts/export_ila.py
./scripts/generate_object_catalog.py
./scripts/inspect_collection.py
./scripts/inspect_episode.py
./scripts/inspect_ila_dataset.py
./scripts/inspect_object_catalog.py
./scripts/inspect_objects.py
./scripts/run.sh
./scripts/visualize_ila_episode.py
./scripts/write_ila_splits.py
./scripts/write_ila_stats.py
./sim_output.log
./src
./src/franka_wrist_camera_scene
./src/franka_wrist_camera_scene/app
./src/franka_wrist_camera_scene/app/camera_warmup.py
./src/franka_wrist_camera_scene/app/__init__.py
./src/franka_wrist_camera_scene/app/launcher.py
./src/franka_wrist_camera_scene/collection
./src/franka_wrist_camera_scene/collection/__init__.py
./src/franka_wrist_camera_scene/collection/pick_place.py
./src/franka_wrist_camera_scene/control
./src/franka_wrist_camera_scene/control/gripper.py
./src/franka_wrist_camera_scene/control/ik.py
./src/franka_wrist_camera_scene/control/__init__.py
./src/franka_wrist_camera_scene/control/motion_primitives.py
./src/franka_wrist_camera_scene/control/trajectory.py
./src/franka_wrist_camera_scene/datasets
./src/franka_wrist_camera_scene/datasets/ila.py
./src/franka_wrist_camera_scene/datasets/__init__.py
./src/franka_wrist_camera_scene/debug
./src/franka_wrist_camera_scene/debug/camera_probe.py
./src/franka_wrist_camera_scene/debug/__init__.py
./src/franka_wrist_camera_scene/debug/video_recorder.py
./src/franka_wrist_camera_scene/debug/visualization.py
./src/franka_wrist_camera_scene/episode
./src/franka_wrist_camera_scene/episode/__init__.py
./src/franka_wrist_camera_scene/episode/manifest.py
./src/franka_wrist_camera_scene/episode/recorder.py
./src/franka_wrist_camera_scene/episode/reset.py
./src/franka_wrist_camera_scene/episode/schema.py
./src/franka_wrist_camera_scene/episode/success.py
./src/franka_wrist_camera_scene/export
./src/franka_wrist_camera_scene/export/ila.py
./src/franka_wrist_camera_scene/export/ila_splits.py
./src/franka_wrist_camera_scene/export/ila_stats.py
./src/franka_wrist_camera_scene/export/__init__.py
./src/franka_wrist_camera_scene/__init__.py
./src/franka_wrist_camera_scene/objects
./src/franka_wrist_camera_scene/objects/catalog_generator.py
./src/franka_wrist_camera_scene/objects/catalog.py
./src/franka_wrist_camera_scene/objects/__init__.py
./src/franka_wrist_camera_scene/objects/registry.py
./src/franka_wrist_camera_scene/objects/selection.py
./src/franka_wrist_camera_scene/policies
./src/franka_wrist_camera_scene/policies/circle_policy.py
./src/franka_wrist_camera_scene/policies/__init__.py
./src/franka_wrist_camera_scene/policies/pick_place_scripted.py
./src/franka_wrist_camera_scene/policies/scripted_base.py
./src/franka_wrist_camera_scene/scene
./src/franka_wrist_camera_scene/scene/__init__.py
./src/franka_wrist_camera_scene/scene/lighting.py
./src/franka_wrist_camera_scene/scene/object_context.py
./src/franka_wrist_camera_scene/scene/tabletop.py
./src/franka_wrist_camera_scene/settings.py
./src/franka_wrist_camera_scene/tasks
./src/franka_wrist_camera_scene/tasks/base.py
./src/franka_wrist_camera_scene/tasks/__init__.py
./src/franka_wrist_camera_scene/tasks/pick_place.py
./src/franka_wrist_camera_scene/tasks/sampling.py
./src/franka_wrist_camera_scene/utils
./src/franka_wrist_camera_scene/utils/__init__.py
./src/franka_wrist_camera_scene/utils/paths.py
./wrist_camera.mp4

## Key docs extracted

### README.md
# Franka wrist-camera tabletop scene for Isaac Lab

Clean Isaac Lab scene for a Franka Panda arm on a tabletop inside a warehouse background, with:

- a wrist-mounted RGB-D camera attached under `Robot/panda_hand/wrist_rgbd_camera`
- a fixed third-person “agent view” RGB-D camera
- a Seattle lab table, simple tabletop props, dome lighting, and a warehouse USD background
- a differential-IK controller that moves the gripper through a 40 cm horizontal circle above the table
- viewport markers showing the desired circular path and current IK target
- an optional wrist-camera pixel/depth probe for checking `(u, v, z)` image coordinates

The repo targets Isaac Sim 5.1 / Isaac Lab with Python 3.11 and your existing setup:

```bash
~/IsaacLab
conda env: env_isaaclab
```

## Run

```bash
unzip franka_wrist_camera_isaaclab.zip
cd franka_wrist_camera_isaaclab
conda activate env_isaaclab
./scripts/run.sh
```

Headless smoke run:

```bash
conda activate env_isaaclab
./scripts/run.sh --headless --max_steps 600
```

Custom Isaac Lab path:

```bash
ISAACLAB_ROOT=~/IsaacLab ./scripts/run.sh
```

## Circle IK test

The default gripper path is a 40 cm diameter circle in the air above the table:

```bash
./scripts/run.sh --circle_diameter 0.40 --circle_frequency 0.045
```

The path center, table height, robot base pose, and default camera geometry are centralized in:

```text
src/franka_wrist_camera_scene/settings.py
```

The IK control node is isolated in:

```text
src/franka_wrist_camera_scene/control.py
```

## Camera attachment note

The wrist-camera line is in `src/franka_wrist_camera_scene/scene.py`:

```python
prim_path="{ENV_REGEX_NS}/Robot/panda_hand/wrist_rgbd_camera"
```

That means the camera prim is created as a child of the Franka hand link, so it follows the wrist through the USD/physics hierarchy. The local camera pose is then set with `CameraCfg.OffsetCfg`, relative to `panda_hand`.

## Wrist camera coordinate probe

To visually verify the image coordinate convention:

```bash
./scripts/run.sh --probe_u 320 --probe_v 240 --save_probe_every 60
```

Images are saved under:

```text
camera_probes/
```

The convention is:

```python
z = depth[v, u]
```

where `u` is the image column, `v` is the image row, and `z` is `distance_to_image_plane` in meters.

## Files

```text
franka_wrist_camera_isaaclab/
├── README.md
├── pyproject.toml
├── scripts/
│   ├── run.sh
│   └── run_scene.py
└── src/
    └── franka_wrist_camera_scene/
        ├── __init__.py
        ├── camera_probe.py
        ├── control.py
        ├── scene.py
        ├── settings.py
        └── visualization.py
```

## Notes

- The scene uses Isaac Lab’s built-in Franka Panda high-PD config because it is intended for differential IK task-space control.
- The IK target uses the `panda_hand` body and the `panda_joint.*` joints.
- The robot starts from a stable tabletop-ready Franka pose and the controller immediately tracks a downward-facing gripper pose above the table.
- First launch can take time if Isaac Sim has to download or cache warehouse/table assets.

### AGENTS.md
# AGENTS.md

This repository is an Isaac Lab data-collection and evaluation environment for Franka tabletop manipulation.

## Architecture rules

Keep modules small and single-purpose.

Do not put task logic, policy logic, dataset writing, and simulator launching in the same file.

Use configuration files under `configs/` for experiment/task parameters. Do not add CLI arguments unless the value must change per invocation, such as config path, headless mode, device, or output directory.

Do not add broad `try/except` blocks. If a failure should stop data collection, let it fail clearly. Only catch exceptions when the code can recover in a specific, tested way.

Do not add fallback behavior that silently changes semantics. No hidden alternate camera paths, no silent object respawn, no automatic task substitution, no ignored failed resets.

Use dataclasses for typed configs and episode/task records.

Keep all randomization seeded and recorded in episode metadata.

Every episode must record:
- task name
- language instruction
- seed
- success flag
- timestamps
- camera frame paths or arrays
- robot state
- action representation
- object poses
- randomization metadata

## File ownership

`scene/` owns Isaac Lab scene construction and assets.

`tasks/` owns task definitions, reset sampling, language templates, and success checks.

`policies/` owns scripted demonstrators.

`control/` owns IK, gripper control, motion primitives, and trajectory utilities.

`episode/` owns episode schemas, reset orchestration, and recording.

`export/` owns conversion to model-specific formats.

`scripts/` should only load configs and call package code.

## Code quality

Prefer explicit simple code over clever abstractions.

Do not introduce framework-like registries unless there are at least two concrete implementations using them.

No global mutable state except Isaac Sim application objects that must be global.

No hardcoded absolute paths. Use config values or paths relative to repo root.

No print spam in library code. Use concise logging from scripts.

Do not mix debug visualization with data collection logic.

Keep Isaac Sim compatibility patches isolated in `app/launcher.py`.

## Testing expectations

Pure Python modules must be testable without launching Isaac Sim.

Task sampling, language generation, success predicates, episode schema validation, and exporters should have unit tests.

Simulation-dependent tests should be smoke tests only:
- scene launches
- reset runs
- one scripted episode finishes
- one episode writes a valid dataset directory

### guidelines.md
# Repository Coding Guidelines & Conventions

This document records the architectural standards and implementation guidelines established for the Franka Tabletop Isaac Lab project. Refer to this to prevent design drift, circular dependencies, or simulation setup corruption.

---

## 1. Decoupled Architecture

Keep the policy, trajectory generation, and controller loops strictly decoupled:

*   **Policies**: Policies (e.g., `CircleMotionPolicy`, `PickPlaceScriptedPolicy`) are finite-state machines or neural network steps. They must output a unified command structure using the `PolicyCommand` dataclass.
*   **Dataclasses / Commands**: `PolicyCommand` resides in `policies/scripted_base.py` and encapsulates:
    *   `target_pos_w`: Tensor representing target TCP position in world coordinates.
    *   `target_quat_w`: Tensor representing target TCP orientation in world coordinates.
    *   `finger_opening_m`: Total opening width of one finger (parallel gripper fingers target the same distance).
    *   `done`: Boolean flag indicating execution completion.
*   **IK Controller**: `CartesianIKController` in `control/ik.py` should remain general. It must **never** contain code relating to circles, specific task trajectories, or gripper commands. It simply consumes `target_pos_w` and `target_quat_w`, computes differential IK, and sets joint targets.
*   **Gripper Controller**: `GripperController` in `control/gripper.py` is dedicated to parallel finger controls.

---

## 2. Config Files & Settings

To prevent drift risk between scene layouts and task planners, establish a single source of truth:

*   **YAML Configuration**: Always mirror layout parameters (table heights, sizes, camera specifications, initial joint states) into `configs/scene.yaml`.
*   **No Redundant Settings**: [settings.py](src/franka_wrist_camera_scene/settings.py) dynamically reads constants using `load_yaml_config("scene.yaml")` from `utils/paths.py` to maintain compatibility without risking settings drift.
*   **Casing Conventions**: Use lowercase strings for conventions (e.g., `ros`, `world`) in configuration files to prevent parser mismatches inside Isaac Lab's camera and frame utilities.

---

## 3. Explicit Imports

*   **Keep Package Roots Empty**: To prevent submodules from becoming dependency magnets, keep the package `__init__.py` clean. 
*   **Explicit Submodule Imports**: Scripts and modules should import directly from the explicit submodule path (e.g., `from franka_wrist_camera_scene.control.ik import CartesianIKController`) rather than from the package root `__all__`.

---

## 4. Script Modularity

Main entry scripts (e.g., [debug_scene.py](scripts/debug_scene.py)) must remain lightweight and restricted to CLI parsing, pipeline setup, and the simulation step loop:

*   **Reset Logic**: episodic reset operations must be housed under `episode/reset.py` (e.g., `reset_robot_to_default(scene)`).
*   **Camera Warmup**: RTX-specific render prim offsets or warmup workarounds must be housed under `app/camera_warmup.py` (e.g., `nudge_camera_prims(sim, scene)`).

---

## 5. Isaac Lab Simulation Conventions

*   **Dynamic Rigid Bodies**: When creating movable objects (such as target manipulation cubes), spawn them using `RigidObjectCfg` instead of `AssetBaseCfg`.
*   **Geometry Configuration**: Specify physics properties directly in the shape configuration using `rigid_props=sim_utils.RigidBodyPropertiesCfg()` and `collision_props=sim_utils.CollisionPropertiesCfg()` (Note: the keyword argument is `rigid_props`, **not** `rigid_body_props`).
*   **TCP Alignment**: When target coordinates (like object pick poses) are defined in world coordinates, adjust wrist/hand commands by subtracting the TCP offset vector (`tcp_offset_w = quat_apply(quat_w, tcp_offset_local)`) to ensure the gripper matches the target's center instead of floating or penetrating the mesh.
*   **Wrist Camera Updates**: Keep the hand-mounted camera's `update_period` at `0.0` to force updates on every physics simulation step, eliminating camera coordinate lag relative to rapid link movements.

### pyproject.toml
[project]
name = "franka-wrist-camera-isaaclab"
version = "0.1.0"
description = "Isaac Lab Franka Panda tabletop scene with wrist and third-person cameras."
requires-python = ">=3.11,<3.12"
readme = "README.md"

[tool.ruff]
line-length = 110
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM", "C4"]
ignore = ["E501"]

[tool.black]
line-length = 110
target-version = ["py311"]

### .gitignore
__pycache__/
*.py[cod]
*.egg-info/
.ruff_cache/
.mypy_cache/
.pytest_cache/
logs/
runs/
.cache/

.thumbs/
data/
exports/


## Environment detection
PWD: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab
Python candidates:
/usr/bin/python
Python 3.10.12
/usr/bin/python3
Python 3.10.12

Conda:

IsaacLab candidates:
FOUND_ISSACLAB_CANDIDATE=/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab
total 176
drwxrwxr-x 11 redafrix redafrix  4096 Jun 11 11:06 .
drwxrwxr-x 16 redafrix redafrix  4096 Jun 11 16:32 ..
drwxrwxr-x  4 redafrix redafrix  4096 Jun 11 11:06 apps
-rw-rw-r--  1 redafrix redafrix  1490 Jun 11 11:06 CITATION.cff
-rw-rw-r--  1 redafrix redafrix  1770 Jun 11 11:06 CONTRIBUTING.md
-rw-rw-r--  1 redafrix redafrix  2608 Jun 11 11:06 CONTRIBUTORS.md
drwxrwxr-x  6 redafrix redafrix  4096 Jun 11 11:06 docker
-rw-rw-r--  1 redafrix redafrix   445 Jun 11 11:06 .dockerignore
drwxrwxr-x  6 redafrix redafrix  4096 Jun 11 11:06 docs
-rw-rw-r--  1 redafrix redafrix   285 Jun 11 11:06 environment.yml
-rw-rw-r--  1 redafrix redafrix   861 Jun 11 11:06 .flake8
drwxrwxr-x  8 redafrix redafrix  4096 Jun 11 11:06 .git
-rw-rw-r--  1 redafrix redafrix   505 Jun 11 11:06 .gitattributes
drwxrwxr-x  5 redafrix redafrix  4096 Jun 11 11:06 .github
-rw-rw-r--  1 redafrix redafrix   853 Jun 11 11:06 .gitignore
-rw-rw-r--  1 redafrix redafrix 24001 Jun 11 11:06 isaaclab.bat
-rwxrwxr-x  1 redafrix redafrix 22640 Jun 11 11:06 isaaclab.sh
lrwxrwxrwx  1 redafrix redafrix    62 Jun 11 11:06 _isaac_sim -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim
-rw-rw-r--  1 redafrix redafrix  1630 Jun 11 11:06 LICENSE
-rw-rw-r--  1 redafrix redafrix 10142 Jun 11 11:06 LICENSE-mimic
-rw-rw-r--  1 redafrix redafrix  3158 Jun 11 11:06 .pre-commit-config.yaml
-rw-rw-r--  1 redafrix redafrix  2462 Jun 11 11:06 pyproject.toml
-rw-rw-r--  1 redafrix redafrix    68 Jun 11 11:06 pytest.ini
-rw-rw-r--  1 redafrix redafrix  9003 Jun 11 11:06 README.md
drwxrwxr-x  9 redafrix redafrix  4096 Jun 11 11:06 scripts
-rw-rw-r--  1 redafrix redafrix  1708 Jun 11 11:06 SECURITY.md
drwxrwxr-x  7 redafrix redafrix  4096 Jun 11 11:06 source
drwxrwxr-x  3 redafrix redafrix  4096 Jun 11 11:06 tools
-rw-rw-r--  1 redafrix redafrix     6 Jun 11 11:06 VERSION
drwxrwxr-x  3 redafrix redafrix  4096 Jun 11 11:06 .vscode

Isaac Sim candidates:
FOUND_ISAACSIM_CANDIDATE=/home/redafrix/isaacsim
total 268
drwxrwxr-x  21 redafrix redafrix  4096 Oct 31  2025 .
drwxr-xr-x  90 redafrix redafrix  4096 Jun 11 21:55 ..
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 apps
-rwxr-xr-x   1 redafrix redafrix   889 Jan 28  2025 clear_caches.sh
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 config
drwxr-xr-x   4 redafrix redafrix  4096 Jan 28  2025 data
drwxr-xr-x   3 redafrix redafrix  4096 Jan 28  2025 docs
-rw-r--r--   1 redafrix redafrix   265 Jan 28  2025 environment.yml
lrwxrwxrwx   1 redafrix redafrix    64 Oct 23  2025 extension_examples -> exts/isaacsim.examples.interactive/isaacsim/examples/interactive
drwxr-xr-x  89 redafrix redafrix  4096 Jan 28  2025 exts
drwxr-xr-x 429 redafrix redafrix 36864 Jan 28  2025 extscache
drwxr-xr-x  75 redafrix redafrix  4096 Jan 28  2025 extsDeprecated
drwxr-xr-x  37 redafrix redafrix  4096 Jan 28  2025 extsPhysics
drwxr-xr-x   2 redafrix redafrix  4096 Oct 23  2025 extsUser
drwxr-xr-x   6 redafrix redafrix  4096 Oct 31  2025 isaacsim
-rwxr-xr-x   1 redafrix redafrix  2323 Jan 28  2025 isaac-sim.docker.gui.sh
-rwxr-xr-x   1 redafrix redafrix  2156 Jan 28  2025 isaac-sim.docker.sh
-rwxr-xr-x   1 redafrix redafrix   235 Jan 28  2025 isaac-sim.fabric.sh
-rwxr-xr-x   1 redafrix redafrix   254 Jan 28  2025 isaac-sim.old_streaming.sh
-rwxr-xr-x   1 redafrix redafrix   232 Jan 28  2025 isaac-sim.selector.sh
-rwxr-xr-x   1 redafrix redafrix   228 Jan 28  2025 isaac-sim.sh
-rwxr-xr-x   1 redafrix redafrix   250 Jan 28  2025 isaac-sim.streaming.sh
-rwxr-xr-x   1 redafrix redafrix   234 Jan 28  2025 isaac-sim.xr.vr.sh
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 jupyter_kernel
-rwxr-xr-x   1 redafrix redafrix  1927 Jan 28  2025 jupyter_notebook.sh
drwxr-xr-x  19 redafrix redafrix  4096 Oct 31  2025 kit
-rw-r--r--   1 redafrix redafrix 49043 Jan 28  2025 LICENSE.txt
drwxr-xr-x   3 redafrix redafrix  4096 Jan 28  2025 logs
-rw-r--r--   1 redafrix redafrix   201 Jan 28  2025 PACKAGE-INFO.yaml
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 PACKAGE-LICENSES
-rwxr-xr-x   1 redafrix redafrix   532 Jan 28  2025 post_install.sh
drwxr-xr-x   3 redafrix redafrix  4096 Jan 28  2025 python_packages
-rwxr-xr-x   1 redafrix redafrix  1218 Jan 28  2025 python.sh
-rw-r--r--   1 redafrix redafrix     0 Jan 28  2025 requirements.txt
-rwxr-xr-x   1 redafrix redafrix   905 Jan 28  2025 setup_conda_env.sh
-rwxr--r--   1 redafrix redafrix  1393 Jan 28  2025 setup_python_env.sh
drwxr-xr-x   9 redafrix redafrix  4096 Jan 28  2025 standalone_examples
-rw-r--r--   1 redafrix redafrix   320 Jan 28  2025 tensorboard
drwxr-xr-x   2 redafrix redafrix 24576 Jan 28  2025 tests
drwxr-xr-x   4 redafrix redafrix  4096 Jan 28  2025 tools
-rw-r--r--   1 redafrix redafrix    37 Jan 28  2025 VERSION
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 .vscode
-rwxr-xr-x   1 redafrix redafrix  1379 Jan 28  2025 warmup.sh
FOUND_ISAACSIM_CANDIDATE=/home/redafrix/isaacsim
total 268
drwxrwxr-x  21 redafrix redafrix  4096 Oct 31  2025 .
drwxr-xr-x  90 redafrix redafrix  4096 Jun 11 21:55 ..
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 apps
-rwxr-xr-x   1 redafrix redafrix   889 Jan 28  2025 clear_caches.sh
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 config
drwxr-xr-x   4 redafrix redafrix  4096 Jan 28  2025 data
drwxr-xr-x   3 redafrix redafrix  4096 Jan 28  2025 docs
-rw-r--r--   1 redafrix redafrix   265 Jan 28  2025 environment.yml
lrwxrwxrwx   1 redafrix redafrix    64 Oct 23  2025 extension_examples -> exts/isaacsim.examples.interactive/isaacsim/examples/interactive
drwxr-xr-x  89 redafrix redafrix  4096 Jan 28  2025 exts
drwxr-xr-x 429 redafrix redafrix 36864 Jan 28  2025 extscache
drwxr-xr-x  75 redafrix redafrix  4096 Jan 28  2025 extsDeprecated
drwxr-xr-x  37 redafrix redafrix  4096 Jan 28  2025 extsPhysics
drwxr-xr-x   2 redafrix redafrix  4096 Oct 23  2025 extsUser
drwxr-xr-x   6 redafrix redafrix  4096 Oct 31  2025 isaacsim
-rwxr-xr-x   1 redafrix redafrix  2323 Jan 28  2025 isaac-sim.docker.gui.sh
-rwxr-xr-x   1 redafrix redafrix  2156 Jan 28  2025 isaac-sim.docker.sh
-rwxr-xr-x   1 redafrix redafrix   235 Jan 28  2025 isaac-sim.fabric.sh
-rwxr-xr-x   1 redafrix redafrix   254 Jan 28  2025 isaac-sim.old_streaming.sh
-rwxr-xr-x   1 redafrix redafrix   232 Jan 28  2025 isaac-sim.selector.sh
-rwxr-xr-x   1 redafrix redafrix   228 Jan 28  2025 isaac-sim.sh
-rwxr-xr-x   1 redafrix redafrix   250 Jan 28  2025 isaac-sim.streaming.sh
-rwxr-xr-x   1 redafrix redafrix   234 Jan 28  2025 isaac-sim.xr.vr.sh
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 jupyter_kernel
-rwxr-xr-x   1 redafrix redafrix  1927 Jan 28  2025 jupyter_notebook.sh
drwxr-xr-x  19 redafrix redafrix  4096 Oct 31  2025 kit
-rw-r--r--   1 redafrix redafrix 49043 Jan 28  2025 LICENSE.txt
drwxr-xr-x   3 redafrix redafrix  4096 Jan 28  2025 logs
-rw-r--r--   1 redafrix redafrix   201 Jan 28  2025 PACKAGE-INFO.yaml
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 PACKAGE-LICENSES
-rwxr-xr-x   1 redafrix redafrix   532 Jan 28  2025 post_install.sh
drwxr-xr-x   3 redafrix redafrix  4096 Jan 28  2025 python_packages
-rwxr-xr-x   1 redafrix redafrix  1218 Jan 28  2025 python.sh
-rw-r--r--   1 redafrix redafrix     0 Jan 28  2025 requirements.txt
-rwxr-xr-x   1 redafrix redafrix   905 Jan 28  2025 setup_conda_env.sh
-rwxr--r--   1 redafrix redafrix  1393 Jan 28  2025 setup_python_env.sh
drwxr-xr-x   9 redafrix redafrix  4096 Jan 28  2025 standalone_examples
-rw-r--r--   1 redafrix redafrix   320 Jan 28  2025 tensorboard
drwxr-xr-x   2 redafrix redafrix 24576 Jan 28  2025 tests
drwxr-xr-x   4 redafrix redafrix  4096 Jan 28  2025 tools
-rw-r--r--   1 redafrix redafrix    37 Jan 28  2025 VERSION
drwxr-xr-x   2 redafrix redafrix  4096 Jan 28  2025 .vscode
-rwxr-xr-x   1 redafrix redafrix  1379 Jan 28  2025 warmup.sh

GPU:
Fri Jun 12 09:46:41 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   55C    P0            590W /   80W |      16MiB /   8188MiB |     20%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            2806      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+

Disk:
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  262G   25G  92% /
/dev/nvme0n1p5  302G  262G   25G  92% /

## Selected IsaacLab root
ISAACLAB_ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab
isaaclab.sh exists: YES

## Python files
scripts/collect.py
scripts/debug_scene.py
scripts/export_ila.py
scripts/generate_object_catalog.py
scripts/inspect_collection.py
scripts/inspect_episode.py
scripts/inspect_ila_dataset.py
scripts/inspect_object_catalog.py
scripts/inspect_objects.py
scripts/visualize_ila_episode.py
scripts/write_ila_splits.py
scripts/write_ila_stats.py
src/franka_wrist_camera_scene/app/camera_warmup.py
src/franka_wrist_camera_scene/app/__init__.py
src/franka_wrist_camera_scene/app/launcher.py
src/franka_wrist_camera_scene/collection/__init__.py
src/franka_wrist_camera_scene/collection/pick_place.py
src/franka_wrist_camera_scene/control/gripper.py
src/franka_wrist_camera_scene/control/ik.py
src/franka_wrist_camera_scene/control/__init__.py
src/franka_wrist_camera_scene/control/motion_primitives.py
src/franka_wrist_camera_scene/control/trajectory.py
src/franka_wrist_camera_scene/datasets/ila.py
src/franka_wrist_camera_scene/datasets/__init__.py
src/franka_wrist_camera_scene/debug/camera_probe.py
src/franka_wrist_camera_scene/debug/__init__.py
src/franka_wrist_camera_scene/debug/video_recorder.py
src/franka_wrist_camera_scene/debug/visualization.py
src/franka_wrist_camera_scene/episode/__init__.py
src/franka_wrist_camera_scene/episode/manifest.py
src/franka_wrist_camera_scene/episode/recorder.py
src/franka_wrist_camera_scene/episode/reset.py
src/franka_wrist_camera_scene/episode/schema.py
src/franka_wrist_camera_scene/episode/success.py
src/franka_wrist_camera_scene/export/ila.py
src/franka_wrist_camera_scene/export/ila_splits.py
src/franka_wrist_camera_scene/export/ila_stats.py
src/franka_wrist_camera_scene/export/__init__.py
src/franka_wrist_camera_scene/__init__.py
src/franka_wrist_camera_scene/objects/catalog_generator.py
src/franka_wrist_camera_scene/objects/catalog.py
src/franka_wrist_camera_scene/objects/__init__.py
src/franka_wrist_camera_scene/objects/registry.py
src/franka_wrist_camera_scene/objects/selection.py
src/franka_wrist_camera_scene/policies/circle_policy.py
src/franka_wrist_camera_scene/policies/__init__.py
src/franka_wrist_camera_scene/policies/pick_place_scripted.py
src/franka_wrist_camera_scene/policies/scripted_base.py
src/franka_wrist_camera_scene/scene/__init__.py
src/franka_wrist_camera_scene/scene/lighting.py
src/franka_wrist_camera_scene/scene/object_context.py
src/franka_wrist_camera_scene/scene/tabletop.py
src/franka_wrist_camera_scene/settings.py
src/franka_wrist_camera_scene/tasks/base.py
src/franka_wrist_camera_scene/tasks/__init__.py
src/franka_wrist_camera_scene/tasks/pick_place.py
src/franka_wrist_camera_scene/tasks/sampling.py
src/franka_wrist_camera_scene/utils/__init__.py
src/franka_wrist_camera_scene/utils/paths.py

## Shell scripts
./run_collect
./run_collect.sh
./run_sim.sh
./scripts/run.sh

## Config files
configs/collection.yaml
configs/object_catalog.generated.yaml
configs/object_catalog.yaml
configs/objects.yaml
configs/scene.yaml

## py_compile result
status=0

## Help output summaries

### help_collect.py.log
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/scripts/collect.py", line 15, in <module>
    from isaaclab.app import AppLauncher  # noqa: E402
ModuleNotFoundError: No module named 'isaaclab'

### help_debug_scene.py.log
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/scripts/debug_scene.py", line 15, in <module>
    from isaaclab.app import AppLauncher  # noqa: E402
ModuleNotFoundError: No module named 'isaaclab'

### help_export_ila.py.log
usage: export_ila.py [-h] raw_collection_dir export_dir

Export raw tabletop collection to ILA format.

positional arguments:
  raw_collection_dir
  export_dir

options:
  -h, --help          show this help message and exit

### help_generate_object_catalog.py.log
usage: generate_object_catalog.py [-h] [--asset-root ASSET_ROOT]
                                  [--output OUTPUT]

Generate a USD object catalog.

options:
  -h, --help            show this help message and exit
  --asset-root ASSET_ROOT
                        Root directory containing object USD asset folders.
  --output OUTPUT       Generated catalog YAML path.

### help_inspect_collection.py.log
usage: inspect_collection.py [-h] collection_dir

Inspect a raw tabletop collection.

positional arguments:
  collection_dir

options:
  -h, --help      show this help message and exit

### help_inspect_episode.py.log
usage: inspect_episode.py [-h] episode_dir

Inspect one raw tabletop episode.

positional arguments:
  episode_dir

options:
  -h, --help   show this help message and exit

### help_inspect_ila_dataset.py.log
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/scripts/inspect_ila_dataset.py", line 13, in <module>
    from franka_wrist_camera_scene.datasets.ila import ILADataset
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/datasets/ila.py", line 9, in <module>
    import torch
ModuleNotFoundError: No module named 'torch'

### help_inspect_object_catalog.py.log
usage: inspect_object_catalog.py [-h] [--config CONFIG]

Inspect a USD object catalog.

options:
  -h, --help       show this help message and exit
  --config CONFIG  Catalog config name under configs/.

### help_inspect_objects.py.log
objects: 1
id                     label          category       kind       size
cube_primitive_006     cube           primitive      cuboid     (0.06, 0.06, 0.06)

### help_visualize_ila_episode.py.log
usage: visualize_ila_episode.py [-h] [--output OUTPUT]
                                [--num_frames NUM_FRAMES]
                                dataset_dir episode_id

Visualize one exported ILA episode.

positional arguments:
  dataset_dir
  episode_id

options:
  -h, --help            show this help message and exit
  --output OUTPUT
  --num_frames NUM_FRAMES

### help_write_ila_splits.py.log
usage: write_ila_splits.py [-h] [--val_fraction VAL_FRACTION] dataset_dir

Write deterministic ILA train/val splits.

positional arguments:
  dataset_dir

options:
  -h, --help            show this help message and exit
  --val_fraction VAL_FRACTION

### help_write_ila_stats.py.log
usage: write_ila_stats.py [-h] dataset_dir

Write ILA dataset statistics.

positional arguments:
  dataset_dir

options:
  -h, --help   show this help message and exit

## Script names
collect.py
debug_scene.py
export_ila.py
generate_object_catalog.py
inspect_collection.py
inspect_episode.py
inspect_ila_dataset.py
inspect_object_catalog.py
inspect_objects.py
run.sh
visualize_ila_episode.py
write_ila_splits.py
write_ila_stats.py

## run.sh content
#!/usr/bin/env bash
# Main entry point bash script to run simulation, collection, or evaluation commands.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

export PYTHONPATH="$REPO_ROOT/src:${PYTHONPATH:-}"
exec "$ISAACLAB_ROOT/isaaclab.sh" -p "$REPO_ROOT/scripts/debug_scene.py" "$@"

## Root run scripts
### run_collect
#!/usr/bin/env bash
# Helper script to run the Franka wrist camera data collection with pre-configured env variables.

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Clean up conda env variables to prevent conflicting python environment paths
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"

# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
export TERM=xterm

ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

exec "$ISAACLAB_ROOT/isaaclab.sh" -p "${SCRIPT_DIR}/scripts/collect.py" "$@"
### run_collect.sh
#!/usr/bin/env bash
# Helper script to run the Franka wrist camera data collection with pre-configured env variables.

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Clean up conda env variables to prevent conflicting python environment paths
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"

# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
export TERM=xterm

ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

exec "$ISAACLAB_ROOT/isaaclab.sh" -p "${SCRIPT_DIR}/scripts/collect.py" "$@"
### run_sim.sh
#!/usr/bin/env bash
# Helper script to run the Franka wrist camera simulation with pre-configured env variables.

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Get directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Clean up conda env variables to prevent conflicting python environment paths
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"

# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
export TERM=xterm

# Execute the simulation run script passing along all arguments
exec "${SCRIPT_DIR}/scripts/run.sh" "$@"

## scripts/run.sh headless smoke result
status=0
log=/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/run_sh_headless_max300.log

## debug_scene.py direct smoke result
status=0
log=/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/debug_scene_headless_max300.log
CMD: python3 scripts/generate_object_catalog.py --help
CMD: python3 scripts/inspect_object_catalog.py --help
CMD: python3 scripts/inspect_objects.py --help
CMD: python3 scripts/inspect_collection.py --help
CMD: python3 scripts/export_ila.py --help
CMD: python3 scripts/write_ila_splits.py --help
CMD: python3 scripts/write_ila_stats.py --help
CMD: python3 scripts/inspect_ila_dataset.py --help
CMD: python3 scripts/visualize_ila_episode.py --help
Trying safe run: scripts/generate_object_catalog.py
Trying safe run: scripts/inspect_object_catalog.py
Trying safe run: scripts/inspect_objects.py

## Object/config script logs

### generate_object_catalog_safe_run.log
[INFO] Saved generated object catalog to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/configs/object_catalog.generated.yaml

### inspect_object_catalog_safe_run.log
config: object_catalog.yaml
asset_root: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/objects
categories: 5
variants: 11
missing files: 0

category           label        split    role       affordances                  variants
apple              apple        train    target     pickable,reachable           3       
can                can          train    target     pickable,reachable           3       
cup                cup          train    target     pickable,reachable           2       
plate              plate        train    clutter    reachable,support            2       
unseen_apple       apple        unseen   target     pickable,reachable           1       

### inspect_objects_safe_run.log
objects: 1
id                     label          category       kind       size
cube_primitive_006     cube           primitive      cuboid     (0.06, 0.06, 0.06)

### generate_object_catalog_safe_run.log
[INFO] Saved generated object catalog to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/configs/object_catalog.generated.yaml

### inspect_object_catalog_safe_run.log
config: object_catalog.yaml
asset_root: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/objects
categories: 5
variants: 11
missing files: 0

category           label        split    role       affordances                  variants
apple              apple        train    target     pickable,reachable           3       
can                can          train    target     pickable,reachable           3       
cup                cup          train    target     pickable,reachable           2       
plate              plate        train    clutter    reachable,support            2       
unseen_apple       apple        unseen   target     pickable,reachable           1       
## collect.py help
Traceback (most recent call last):
  File "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab/scripts/collect.py", line 15, in <module>
    from isaaclab.app import AppLauncher  # noqa: E402
ModuleNotFoundError: No module named 'isaaclab'

## collect.py tiny result
status=0
log=/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/collect_tiny_episode.log

## Tiny collect outputs
Tiny collection produced no files; skipping post-collection inspection/export tests.

## Post-collection script logs

## Runtime generated files
Repo local files changed/untracked:

camera_probes:
camera_probes/wrist_probe_000100.png | 1647 bytes
camera_probes/wrist_probe_000200.png | 1647 bytes
camera_probes/wrist_probe_000300.png | 1647 bytes
camera_probes/wrist_probe_000400.png | 1647 bytes
camera_probes/wrist_probe_000500.png | 1647 bytes
camera_probes/wrist_probe_000600.png | 1647 bytes

videos/mp4:
./agent_camera.mp4 | 1404811 bytes
./wrist_camera.mp4 | 788890 bytes

images:
./objects/egg/texture/egg04.jpg | 45565 bytes
./objects/egg/texture/egg05.jpg | 147465 bytes
./objects/egg/texture/egg06.jpg | 59536 bytes
./objects/egg/texture/egg07.jpg | 17013 bytes
./objects/egg/texture/egg09.jpg | 16234 bytes
./objects/egg/texture/egg10.jpg | 149274 bytes
./objects/egg/texture/egg11.jpg | 34829 bytes
./objects/egg/texture/egg13.jpg | 1826683 bytes
./objects/kiwi/texture/kiwi00.jpg | 1249494 bytes
./objects/kiwi/texture/kiwi05.jpg | 42242 bytes
./objects/kiwi/texture/kiwi07.jpg | 1828723 bytes
./objects/lemon/texture/lemon01.jpg | 1454693 bytes
./objects/lemon/texture/lemon02.jpg | 797466 bytes
./objects/lemon/texture/lemon03.jpg | 54807 bytes
./objects/lemon/texture/lemon04.jpg | 562213 bytes
./objects/lemon/texture/lemon05.jpg | 876327 bytes
./objects/lemon/texture/lemon06.jpg | 571897 bytes
./objects/lemon/texture/lemon08.jpg | 69538 bytes
./objects/lemon/texture/lemon09.jpg | 756685 bytes
./objects/lemon/texture/lemon10.jpg | 58093 bytes
./objects/lemon/texture/lemon12.jpg | 512640 bytes
./objects/lemon/texture/lemon13.jpg | 71398 bytes
./objects/lemon/texture/lemon14.jpg | 65029 bytes
./objects/lemon/texture/lemon15.jpg | 1071022 bytes
./objects/lime/texture/lime00.jpg | 899817 bytes
./objects/lime/texture/lime01.jpg | 115506 bytes
./objects/lime/texture/lime02.jpg | 107064 bytes
./objects/lime/texture/lime03.jpg | 71714 bytes
./objects/onion/texture/onion00.jpg | 115822 bytes
./objects/onion/texture/onion02.jpg | 1041250 bytes
./objects/onion/texture/onion04.jpg | 2023269 bytes
./objects/onion/texture/onion07.jpg | 50005 bytes
./objects/onion/texture/onion08.jpg | 105106 bytes
./objects/onion/texture/onion09.jpg | 1355704 bytes
./objects/onion/texture/onion10.jpg | 111574 bytes
./objects/orange/texture/orange02.jpg | 118975 bytes
./objects/orange/texture/orange03.jpg | 1594273 bytes
./objects/orange/texture/orange04.jpg | 115927 bytes
./objects/orange/texture/orange05.jpg | 1006254 bytes
./objects/orange/texture/orange09.jpg | 86319 bytes
./objects/orange/texture/orange12.jpg | 31806 bytes
./objects/orange/texture/orange13.jpg | 91143 bytes
./objects/peach/texture/peach01.jpg | 102979 bytes
./objects/peach/texture/peach02.jpg | 84683 bytes
./objects/peach/texture/peach03.jpg | 136837 bytes
./objects/peach/texture/peach05.jpg | 67124 bytes
./objects/peach/texture/peach06.jpg | 26191 bytes
./objects/placemat/texture/placemat00.png | 140982 bytes
./objects/placemat/texture/placemat01.png | 22444 bytes
./objects/placemat/texture/placemat02.png | 250162 bytes
./objects/placemat/texture/placemat03.png | 212381 bytes
./objects/placemat/texture/placemat04.png | 96771 bytes
./objects/placemat/texture/placemat05.png | 173281 bytes
./objects/plate/texture/plate00.jpg | 84003 bytes
./objects/plate/texture/plate02.jpg | 58188 bytes
./objects/plate/texture/plate04.jpg | 17674 bytes
./objects/plate/texture/plate05.jpg | 314968 bytes
./objects/plate/texture/plate06.jpg | 92760 bytes
./objects/plate/texture/plate07.jpg | 76625 bytes
./objects/plate/texture/plate08.jpg | 1149481 bytes
./objects/plate/texture/plate10.jpg | 1046634 bytes
./objects/plate/texture/plate12.jpg | 21654 bytes
./objects/plate/texture/plate14.jpg | 121336 bytes
./objects/plate/texture/plate16.jpg | 579534 bytes
./objects/potato/texture/potato00.jpg | 1315122 bytes
./objects/potato/texture/potato02.jpg | 76934 bytes
./objects/potato/texture/potato03.jpg | 12537 bytes
./objects/potato/texture/potato06.jpg | 1331569 bytes
./objects/potato/texture/potato07.jpg | 1107393 bytes
./objects/potato/texture/potato10.jpg | 815691 bytes
./objects/potato/texture/potato13.jpg | 47014 bytes
./objects/potato/texture/potato14.jpg | 110175 bytes
./objects/potato/texture/potato16.jpg | 959361 bytes
./objects/potato/texture/potato17.jpg | 107623 bytes
./objects/potato/texture/potato18.jpg | 778968 bytes
./objects/tangerine/texture/tangerine00.jpg | 1092511 bytes
./objects/tangerine/texture/tangerine03.jpg | 1163074 bytes
./objects/tangerine/texture/tangerine04.jpg | 65278 bytes
./objects/tangerine/texture/tangerine05.jpg | 1523078 bytes
./objects/tangerine/texture/tangerine06.jpg | 910619 bytes
./objects/tomato/texture/tomato01.jpg | 21007 bytes
./objects/tomato/texture/tomato03.jpg | 32698 bytes
./objects/tomato/texture/tomato07.jpg | 115621 bytes
./objects/tray/texture/tray00.jpg | 866339 bytes
./objects/tray/texture/tray02.jpg | 104032 bytes
./objects/tray/texture/tray03.jpg | 1707426 bytes
./objects/tray/texture/tray04.jpg | 1273984 bytes
./objects/tray/texture/tray05.jpg | 104164 bytes
./objects/tray/texture/tray06.jpg | 148209 bytes
./objects/tray/texture/tray07.jpg | 103146 bytes
./objects/tray/texture/tray08.jpg | 112283 bytes
./objects/tray/texture/tray09.jpg | 96795 bytes
./objects/tray/texture/tray10.jpg | 137288 bytes
./objects/tray/texture/tray11.jpg | 106956 bytes
./objects/tray/texture/tray12.jpg | 97579 bytes
./objects/unseen/texture/apple99.jpg | 1209414 bytes
./objects/unseen/texture/bottled_drink99.jpg | 804507 bytes
./objects/unseen/texture/can99.jpg | 327663 bytes
./objects/unseen/texture/cup99.jpg | 105726 bytes
./objects/unseen/texture/peach99.jpg | 57648 bytes

# FINAL SUMMARY

- repo: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab
- branch: master
- commit: 5029899cb489ede48fc524e4f76930832e9607c8
- isaaclab_root: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab
- py_compile_status: 0
- run_sh_headless_status: 0
- debug_scene_status: 0
- collect_tiny_status: 0

## Existing repo scripts found
collect.py
debug_scene.py
export_ila.py
generate_object_catalog.py
inspect_collection.py
inspect_episode.py
inspect_ila_dataset.py
inspect_object_catalog.py
inspect_objects.py
run.sh
visualize_ila_episode.py
write_ila_splits.py
write_ila_stats.py

## Existing root run scripts found
run_collect
run_collect.sh
run_sim.sh

## Important generated outputs

## Reports
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/ARCHITECTURE_SUMMARY.md | 9577 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/FILE_INVENTORY.txt | 40865 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/FULL_TEXT_FILE_DUMP.md | 254461 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md | 83250 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/SAFE_SCRIPT_TEST_PLAN.md | 4419 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/reports/SCRIPT_HELP_OUTPUTS.md | 2419 bytes

## Logs
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/collect_help.log | 283 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/collect_tiny_episode.log | 45 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/debug_scene_headless_max300.log | 45 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/generate_object_catalog_safe_run.log | 175 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/git_clone_https.log | 988 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/git_clone_ssh.log | 287 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_collect.py.log | 283 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_debug_scene.py.log | 287 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_export_ila.py.log | 224 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_generate_object_catalog.py.log | 370 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_inspect_collection.py.log | 185 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_inspect_episode.py.log | 172 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_inspect_ila_dataset.py.log | 491 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_inspect_object_catalog.py.log | 203 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_inspect_objects.py.log | 163 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_visualize_ila_episode.py.log | 365 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_write_ila_splits.py.log | 250 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/help_write_ila_stats.py.log | 168 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/inspect_object_catalog_safe_run.log | 728 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/inspect_objects_safe_run.log | 163 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/python_py_compile.log | 0 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/logs/run_sh_headless_max300.log | 45 bytes

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  262G   25G  92% /

## Do not modify object replacement yet
Next step after this report: only after confirming baseline scripts work, create a separate branch for replacing/adding new objects.
