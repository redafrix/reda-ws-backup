# Receptacle Goal Object Test Report

Goal:
Extend the current pick-place pipeline from “place object on target area” to “place object inside a receptacle goal”.

Target:
- Use a large bowl / basket / tray / container as the goal object.
- Keep the manipulated object separate from the receptacle.
- Preserve old target-area task behavior.
- Always generate side-by-side videos.
## Starting git state
object-integration-static-assets
d689baa6a4dab4f67aff31d811e95eb96dfd33c0
?? configs/complex_object_tests/

## Last commits
d689baa Add config-driven physics overrides for object-specific tests
2c8bfbb Freeze local Isaac 4.5 baseline configs before object integration
5fb8803 Add output_dir argument override to collect.py
162ab15 Stabilize baseline apple collection: fix scale, add rolling resistance damping, tune gripper actuator gains, and correct finger joint limits
5029899 chore: ignore and untrack thumbnail cache folders
9ca7002 refactor: simplify relative path resolution for durable usd path
b0fb4b8 refactor: make catalog scene config explicit
3d67efd feat: configure catalog target object

## After archiving previous matrix configs
?? configs/accepted_object_tests/

## Accepted configs
configs/accepted_object_tests/complex_bowl_bowl01_mass020_stiff150.yaml
configs/accepted_object_tests/complex_cup_cup00_default.yaml
configs/accepted_object_tests/complex_cup_cup05_default.yaml
configs/accepted_object_tests/complex_cup_cup06_default.yaml
configs/accepted_object_tests/complex_plate_plate00_mass020_stiff150.yaml
configs/accepted_object_tests/fcan03_mass020_stiff150.yaml

## After accepted-config commit
ff269ae Save accepted object test configs from complex matrix
d689baa Add config-driven physics overrides for object-specific tests
2c8bfbb Freeze local Isaac 4.5 baseline configs before object integration
5fb8803 Add output_dir argument override to collect.py
162ab15 Stabilize baseline apple collection: fix scale, add rolling resistance damping, tune gripper actuator gains, and correct finger joint limits

## Receptacle keyword search
configs/object_catalog.yaml:30:  - id: cup
configs/object_catalog.yaml:31:    label: cup
configs/object_catalog.yaml:36:      - id: cup00
configs/object_catalog.yaml:37:        usd_path: cup/cup00.usd
configs/object_catalog.yaml:38:      - id: cup01
configs/object_catalog.yaml:39:        usd_path: cup/cup01.usd
configs/object_catalog.yaml:41:  - id: plate
configs/object_catalog.yaml:42:    label: plate
configs/object_catalog.yaml:47:      - id: plate00
configs/object_catalog.yaml:48:        usd_path: plate/plate00.usd
configs/object_catalog.yaml:49:      - id: plate02
configs/object_catalog.yaml:50:        usd_path: plate/plate02.usd
configs/object_catalog.generated.yaml:125:- id: bowl
configs/object_catalog.generated.yaml:126:  label: bowl
configs/object_catalog.generated.yaml:133:  - id: bowl00
configs/object_catalog.generated.yaml:134:    usd_path: bowl/bowl00.usd
configs/object_catalog.generated.yaml:135:  - id: bowl01
configs/object_catalog.generated.yaml:136:    usd_path: bowl/bowl01.usd
configs/object_catalog.generated.yaml:137:  - id: bowl02
configs/object_catalog.generated.yaml:138:    usd_path: bowl/bowl02.usd
configs/object_catalog.generated.yaml:139:  - id: bowl04
configs/object_catalog.generated.yaml:140:    usd_path: bowl/bowl04.usd
configs/object_catalog.generated.yaml:141:  - id: bowl05
configs/object_catalog.generated.yaml:142:    usd_path: bowl/bowl05.usd
configs/object_catalog.generated.yaml:143:  - id: bowl06
configs/object_catalog.generated.yaml:144:    usd_path: bowl/bowl06.usd
configs/object_catalog.generated.yaml:145:  - id: bowl07
configs/object_catalog.generated.yaml:146:    usd_path: bowl/bowl07.usd
configs/object_catalog.generated.yaml:147:  - id: bowl08
configs/object_catalog.generated.yaml:148:    usd_path: bowl/bowl08.usd
configs/object_catalog.generated.yaml:149:  - id: bowl09
configs/object_catalog.generated.yaml:150:    usd_path: bowl/bowl09.usd
configs/object_catalog.generated.yaml:151:  - id: bowl10
configs/object_catalog.generated.yaml:152:    usd_path: bowl/bowl10.usd
configs/object_catalog.generated.yaml:153:  - id: bowl11
configs/object_catalog.generated.yaml:154:    usd_path: bowl/bowl11.usd
configs/object_catalog.generated.yaml:155:  - id: bowl12
configs/object_catalog.generated.yaml:156:    usd_path: bowl/bowl12.usd
configs/object_catalog.generated.yaml:157:  - id: bowl13
configs/object_catalog.generated.yaml:158:    usd_path: bowl/bowl13.usd
configs/object_catalog.generated.yaml:159:  - id: bowl14
configs/object_catalog.generated.yaml:160:    usd_path: bowl/bowl14.usd
configs/object_catalog.generated.yaml:161:  - id: bowl15
configs/object_catalog.generated.yaml:162:    usd_path: bowl/bowl15.usd
configs/object_catalog.generated.yaml:163:  - id: bowl16
configs/object_catalog.generated.yaml:164:    usd_path: bowl/bowl16.usd
configs/object_catalog.generated.yaml:165:  - id: bowl17
configs/object_catalog.generated.yaml:166:    usd_path: bowl/bowl17.usd
configs/object_catalog.generated.yaml:167:  - id: bowl18
configs/object_catalog.generated.yaml:168:    usd_path: bowl/bowl18.usd
configs/object_catalog.generated.yaml:169:  - id: bowl19
configs/object_catalog.generated.yaml:170:    usd_path: bowl/bowl19.usd
configs/object_catalog.generated.yaml:171:- id: box
configs/object_catalog.generated.yaml:172:  label: box
configs/object_catalog.generated.yaml:179:  - id: box00
configs/object_catalog.generated.yaml:180:    usd_path: box/box00.usd
configs/object_catalog.generated.yaml:181:  - id: box01
configs/object_catalog.generated.yaml:182:    usd_path: box/box01.usd
configs/object_catalog.generated.yaml:183:  - id: box02
configs/object_catalog.generated.yaml:184:    usd_path: box/box02.usd
configs/object_catalog.generated.yaml:185:  - id: box03
configs/object_catalog.generated.yaml:186:    usd_path: box/box03.usd
configs/object_catalog.generated.yaml:187:  - id: box04
configs/object_catalog.generated.yaml:188:    usd_path: box/box04.usd
configs/object_catalog.generated.yaml:189:  - id: box05
configs/object_catalog.generated.yaml:190:    usd_path: box/box05.usd
configs/object_catalog.generated.yaml:191:  - id: box06
configs/object_catalog.generated.yaml:192:    usd_path: box/box06.usd
configs/object_catalog.generated.yaml:193:  - id: box08
configs/object_catalog.generated.yaml:194:    usd_path: box/box08.usd
configs/object_catalog.generated.yaml:195:  - id: box09
configs/object_catalog.generated.yaml:196:    usd_path: box/box09.usd
configs/object_catalog.generated.yaml:197:  - id: box10
configs/object_catalog.generated.yaml:198:    usd_path: box/box10.usd
configs/object_catalog.generated.yaml:199:  - id: box11
configs/object_catalog.generated.yaml:200:    usd_path: box/box11.usd
configs/object_catalog.generated.yaml:201:  - id: box12
configs/object_catalog.generated.yaml:202:    usd_path: box/box12.usd
configs/object_catalog.generated.yaml:203:  - id: box13
configs/object_catalog.generated.yaml:204:    usd_path: box/box13.usd
configs/object_catalog.generated.yaml:205:  - id: box14
configs/object_catalog.generated.yaml:206:    usd_path: box/box14.usd
configs/object_catalog.generated.yaml:207:  - id: box15
configs/object_catalog.generated.yaml:208:    usd_path: box/box15.usd
configs/object_catalog.generated.yaml:251:- id: cup
configs/object_catalog.generated.yaml:252:  label: cup
configs/object_catalog.generated.yaml:259:  - id: cup00
configs/object_catalog.generated.yaml:260:    usd_path: cup/cup00.usd
configs/object_catalog.generated.yaml:261:  - id: cup01
configs/object_catalog.generated.yaml:262:    usd_path: cup/cup01.usd
configs/object_catalog.generated.yaml:263:  - id: cup02
configs/object_catalog.generated.yaml:264:    usd_path: cup/cup02.usd
configs/object_catalog.generated.yaml:265:  - id: cup03
configs/object_catalog.generated.yaml:266:    usd_path: cup/cup03.usd
configs/object_catalog.generated.yaml:267:  - id: cup04
configs/object_catalog.generated.yaml:268:    usd_path: cup/cup04.usd
configs/object_catalog.generated.yaml:269:  - id: cup05
configs/object_catalog.generated.yaml:270:    usd_path: cup/cup05.usd
configs/object_catalog.generated.yaml:271:  - id: cup06
configs/object_catalog.generated.yaml:272:    usd_path: cup/cup06.usd
configs/object_catalog.generated.yaml:273:  - id: cup07
configs/object_catalog.generated.yaml:274:    usd_path: cup/cup07.usd
configs/object_catalog.generated.yaml:275:  - id: cup08
configs/object_catalog.generated.yaml:276:    usd_path: cup/cup08.usd
configs/object_catalog.generated.yaml:277:  - id: cup09
configs/object_catalog.generated.yaml:278:    usd_path: cup/cup09.usd
configs/object_catalog.generated.yaml:453:- id: plate
configs/object_catalog.generated.yaml:454:  label: plate
configs/object_catalog.generated.yaml:461:  - id: plate00
configs/object_catalog.generated.yaml:462:    usd_path: plate/plate00.usd
configs/object_catalog.generated.yaml:463:  - id: plate01
configs/object_catalog.generated.yaml:464:    usd_path: plate/plate01.usd
configs/object_catalog.generated.yaml:465:  - id: plate02
configs/object_catalog.generated.yaml:466:    usd_path: plate/plate02.usd
configs/object_catalog.generated.yaml:467:  - id: plate03
configs/object_catalog.generated.yaml:468:    usd_path: plate/plate03.usd
configs/object_catalog.generated.yaml:469:  - id: plate04
configs/object_catalog.generated.yaml:470:    usd_path: plate/plate04.usd
configs/object_catalog.generated.yaml:471:  - id: plate05
configs/object_catalog.generated.yaml:472:    usd_path: plate/plate05.usd
configs/object_catalog.generated.yaml:473:  - id: plate06
configs/object_catalog.generated.yaml:474:    usd_path: plate/plate06.usd
configs/object_catalog.generated.yaml:475:  - id: plate07
configs/object_catalog.generated.yaml:476:    usd_path: plate/plate07.usd
configs/object_catalog.generated.yaml:477:  - id: plate08
configs/object_catalog.generated.yaml:478:    usd_path: plate/plate08.usd
configs/object_catalog.generated.yaml:479:  - id: plate09
configs/object_catalog.generated.yaml:480:    usd_path: plate/plate09.usd
configs/object_catalog.generated.yaml:481:  - id: plate10
configs/object_catalog.generated.yaml:482:    usd_path: plate/plate10.usd
configs/object_catalog.generated.yaml:483:  - id: plate12
configs/object_catalog.generated.yaml:484:    usd_path: plate/plate12.usd
configs/object_catalog.generated.yaml:485:  - id: plate13
configs/object_catalog.generated.yaml:486:    usd_path: plate/plate13.usd
configs/object_catalog.generated.yaml:487:  - id: plate14
configs/object_catalog.generated.yaml:488:    usd_path: plate/plate14.usd
configs/object_catalog.generated.yaml:489:  - id: plate15
configs/object_catalog.generated.yaml:490:    usd_path: plate/plate15.usd
configs/object_catalog.generated.yaml:491:  - id: plate16
configs/object_catalog.generated.yaml:492:    usd_path: plate/plate16.usd
configs/object_catalog.generated.yaml:557:- id: tray
configs/object_catalog.generated.yaml:558:  label: tray
configs/object_catalog.generated.yaml:565:  - id: tray04
configs/object_catalog.generated.yaml:566:    usd_path: tray/tray04.usd
configs/object_catalog.generated.yaml:567:  - id: tray05
configs/object_catalog.generated.yaml:568:    usd_path: tray/tray05.usd
configs/object_catalog.generated.yaml:569:  - id: tray06
configs/object_catalog.generated.yaml:570:    usd_path: tray/tray06.usd
configs/object_catalog.generated.yaml:571:  - id: tray07
configs/object_catalog.generated.yaml:572:    usd_path: tray/tray07.usd
configs/object_catalog.generated.yaml:573:  - id: tray08
configs/object_catalog.generated.yaml:574:    usd_path: tray/tray08.usd
configs/object_catalog.generated.yaml:575:  - id: tray09
configs/object_catalog.generated.yaml:576:    usd_path: tray/tray09.usd
configs/object_catalog.generated.yaml:577:  - id: tray10
configs/object_catalog.generated.yaml:578:    usd_path: tray/tray10.usd
configs/object_catalog.generated.yaml:579:  - id: tray11
configs/object_catalog.generated.yaml:580:    usd_path: tray/tray11.usd
configs/object_catalog.generated.yaml:581:  - id: tray12
configs/object_catalog.generated.yaml:582:    usd_path: tray/tray12.usd
configs/object_catalog.generated.yaml:613:- id: unseen_cup
configs/object_catalog.generated.yaml:614:  label: cup
configs/object_catalog.generated.yaml:621:  - id: cup99
configs/object_catalog.generated.yaml:622:    usd_path: unseen/cup99.usd
objects/metadata.json:388:    "bowl00.usd": {
objects/metadata.json:390:            "bowl",
objects/metadata.json:391:            "pure red bowl"
objects/metadata.json:394:    "bowl01.usd": {
objects/metadata.json:396:            "bowl",
objects/metadata.json:397:            "ceramic bowl",
objects/metadata.json:398:            "bowl with enameled gold rim",
objects/metadata.json:399:            "ceramic bowl with enameled gold rim"
objects/metadata.json:402:    "bowl02.usd": {
objects/metadata.json:404:            "bowl",
objects/metadata.json:405:            "orange bowl",
objects/metadata.json:406:            "bowl with black saw-shaped stripes",
objects/metadata.json:407:            "orange bowl with black saw-shaped stripes"
objects/metadata.json:410:    "bowl04.usd": {
objects/metadata.json:412:            "bowl",
objects/metadata.json:413:            "white bowl",
objects/metadata.json:414:            "deep bowl",
objects/metadata.json:415:            "white deep bowl"
objects/metadata.json:418:    "bowl05.usd": {
objects/metadata.json:420:            "bowl",
objects/metadata.json:421:            "grey bowl",
objects/metadata.json:422:            "shallow bowl",
objects/metadata.json:423:            "bowl with large bottom surface",
objects/metadata.json:424:            "grey shallow bowl",
objects/metadata.json:425:            "grey bowl with large bottom surface",
objects/metadata.json:426:            "shallow bowl with large bottom surface",
objects/metadata.json:427:            "grey shallow bowl with large bottom surface"
objects/metadata.json:430:    "bowl06.usd": {
objects/metadata.json:432:            "bowl",
objects/metadata.json:433:            "ceramic bowl",
objects/metadata.json:434:            "deep bowl",
objects/metadata.json:435:            "bowl with black stripes",
objects/metadata.json:436:            "ceramic deep bowl",
objects/metadata.json:437:            "ceramic bowl with black stripes",
objects/metadata.json:438:            "deep bowl with black stripes",
objects/metadata.json:439:            "ceramic deep bowl with black stripes"
objects/metadata.json:442:    "bowl07.usd": {
objects/metadata.json:444:            "bowl",
objects/metadata.json:445:            "dark brown bowl",
objects/metadata.json:446:            "wooden bowl",
objects/metadata.json:447:            "dark brown wooden bowl",
objects/metadata.json:448:            "shallow bowl",
objects/metadata.json:449:            "wooden shallow bowl"
objects/metadata.json:452:    "bowl08.usd": {
objects/metadata.json:454:            "bowl",
objects/metadata.json:455:            "dark brown bowl",
objects/metadata.json:456:            "wooden bowl",
objects/metadata.json:457:            "dark brown wooden bowl",
objects/metadata.json:458:            "deep bowl",
objects/metadata.json:459:            "wooden deep bowl"
objects/metadata.json:462:    "bowl09.usd": {
objects/metadata.json:464:            "bowl",
objects/metadata.json:465:            "dark brown bowl",
objects/metadata.json:466:            "wooden bowl",
objects/metadata.json:467:            "light brown wooden bowl",
objects/metadata.json:468:            "shallow bowl",
objects/metadata.json:469:            "wooden shallow bowl"
objects/metadata.json:472:    "bowl10.usd": {
objects/metadata.json:474:            "bowl",
objects/metadata.json:475:            "wooden bowl",
objects/metadata.json:476:            "deep bowl",
objects/metadata.json:477:            "wooden deep bowl"
objects/metadata.json:480:    "bowl11.usd": {
objects/metadata.json:482:            "bowl",
objects/metadata.json:483:            "ceramic bowl",
objects/metadata.json:484:            "deep bowl",
objects/metadata.json:485:            "bowl with cyan patterns",
objects/metadata.json:486:            "ceramic deep bowl",
objects/metadata.json:487:            "ceramic bowl with cyan patterns",
objects/metadata.json:488:            "deep bowl with cyan patterns",
objects/metadata.json:489:            "ceramic deep bowl with cyan patterns"
objects/metadata.json:492:    "bowl12.usd": {
objects/metadata.json:494:            "bowl",
objects/metadata.json:495:            "ceramic bowl",
objects/metadata.json:496:            "deep bowl",
objects/metadata.json:497:            "bowl with floral patterns",
objects/metadata.json:498:            "ceramic deep bowl",
objects/metadata.json:499:            "ceramic bowl with floral patterns",
objects/metadata.json:500:            "deep bowl with floral patterns",
objects/metadata.json:501:            "ceramic deep bowl with floral patterns"
objects/metadata.json:504:    "bowl13.usd": {
objects/metadata.json:506:            "bowl",
objects/metadata.json:507:            "ceramic bowl",
objects/metadata.json:508:            "shallow bowl",
objects/metadata.json:509:            "bowl with floral patterns",
objects/metadata.json:510:            "ceramic shallow bowl",
objects/metadata.json:511:            "ceramic bowl with floral patterns",
objects/metadata.json:512:            "shallow bowl with floral patterns",
objects/metadata.json:513:            "ceramic shallow bowl with floral patterns"
objects/metadata.json:516:    "bowl14.usd": {
objects/metadata.json:518:            "bowl",
objects/metadata.json:519:            "marble bowl",
objects/metadata.json:520:            "deep bowl",
objects/metadata.json:521:            "marble deep bowl"
objects/metadata.json:524:    "bowl15.usd": {
objects/metadata.json:526:            "bowl",
objects/metadata.json:527:            "wooden bowl",
objects/metadata.json:528:            "shallow bowl",
objects/metadata.json:529:            "wooden shallow bowl"
objects/metadata.json:532:    "bowl16.usd": {
objects/metadata.json:534:            "bowl",
objects/metadata.json:535:            "ceramic bowl",
objects/metadata.json:536:            "deep bowl",
objects/metadata.json:537:            "bowl with bird patterns",
objects/metadata.json:538:            "ceramic deep bowl",
objects/metadata.json:539:            "ceramic bowl with bird patterns",
objects/metadata.json:540:            "deep bowl with bird patterns",
objects/metadata.json:541:            "ceramic deep bowl with bird patterns"
objects/metadata.json:544:    "bowl17.usd": {
objects/metadata.json:546:            "bowl",
objects/metadata.json:547:            "ceramic bowl",
objects/metadata.json:548:            "deep bowl",
objects/metadata.json:549:            "bowl with pink floral patterns",
objects/metadata.json:550:            "ceramic deep bowl",
objects/metadata.json:551:            "ceramic bowl with pink floral patterns",
objects/metadata.json:552:            "deep bowl with pink floral patterns",
objects/metadata.json:553:            "ceramic deep bowl with pink floral patterns"
objects/metadata.json:556:    "bowl18.usd": {
objects/metadata.json:558:            "bowl",
objects/metadata.json:559:            "grey bowl",
objects/metadata.json:560:            "shallow bowl",
objects/metadata.json:561:            "grey shallow bowl"
objects/metadata.json:564:    "bowl19.usd": {
objects/metadata.json:566:            "bowl",
objects/metadata.json:567:            "yellow bowl",
objects/metadata.json:568:            "bowl saying puffo pops",
objects/metadata.json:569:            "yellow bowl saying puffo pops"
objects/metadata.json:572:    "box00.usd": {
objects/metadata.json:574:            "box",
objects/metadata.json:575:            "black box",
objects/metadata.json:576:            "plastic box",
objects/metadata.json:577:            "black plastic box"
objects/metadata.json:580:    "box01.usd": {
objects/metadata.json:582:            "box",
objects/metadata.json:583:            "white box",
objects/metadata.json:584:            "plastic box",
objects/metadata.json:585:            "white plastic box"
objects/metadata.json:588:    "box02.usd": {
objects/metadata.json:590:            "box",
objects/metadata.json:591:            "pink box",
objects/metadata.json:592:            "plastic box",
objects/metadata.json:593:            "pink plastic box"
objects/metadata.json:596:    "box03.usd": {
objects/metadata.json:598:            "box",
objects/metadata.json:599:            "green box",
objects/metadata.json:600:            "plastic box",
objects/metadata.json:601:            "green plastic box"
objects/metadata.json:604:    "box04.usd": {
objects/metadata.json:606:            "box",
objects/metadata.json:607:            "yellow box",
objects/metadata.json:608:            "plastic box",
objects/metadata.json:609:            "yellow plastic box"
objects/metadata.json:612:    "box05.usd": {
objects/metadata.json:614:            "box",
objects/metadata.json:615:            "blue box",
objects/metadata.json:616:            "plastic box",
objects/metadata.json:617:            "blue plastic box"
objects/metadata.json:620:    "box06.usd": {
objects/metadata.json:622:            "box",
objects/metadata.json:623:            "paper box"
objects/metadata.json:626:    "box08.usd": {
objects/metadata.json:628:            "box",
objects/metadata.json:629:            "red box",
objects/metadata.json:630:            "plastic box",
objects/metadata.json:631:            "box with MMLab At NTU words",
objects/metadata.json:632:            "red box with MMLab At NTU words"
objects/metadata.json:635:    "box09.usd": {
objects/metadata.json:637:            "box",
objects/metadata.json:638:            "white box",
objects/metadata.json:639:            "plastic box",
objects/metadata.json:640:            "box with Microsoft Logo",
objects/metadata.json:641:            "white box with Microsoft Logo"
objects/metadata.json:644:    "box10.usd": {
objects/metadata.json:646:            "box",
objects/metadata.json:647:            "white box",
objects/metadata.json:648:            "plastic box",
objects/metadata.json:649:            "box with Google Logo",
objects/metadata.json:650:            "white box with Google Logo"
objects/metadata.json:653:    "box11.usd": {
objects/metadata.json:655:            "box",
objects/metadata.json:656:            "black box",
objects/metadata.json:657:            "plastic box",
objects/metadata.json:658:            "box with Apple Logo",
objects/metadata.json:659:            "black box with Apple Logo"
objects/metadata.json:662:    "box12.usd": {
objects/metadata.json:664:            "box",
objects/metadata.json:665:            "white box",
objects/metadata.json:666:            "plastic box",
objects/metadata.json:667:            "box with Tencent Logo",
objects/metadata.json:668:            "white box with Tencent Logo"
objects/metadata.json:671:    "box13.usd": {
objects/metadata.json:673:            "box",
objects/metadata.json:674:            "white box",
objects/metadata.json:675:            "plastic box",
objects/metadata.json:676:            "box with OpenAI Logo",
objects/metadata.json:677:            "white box with OpenAI Logo"
objects/metadata.json:680:    "box14.usd": {
objects/metadata.json:682:            "box",
objects/metadata.json:683:            "white box",
objects/metadata.json:684:            "plastic box",
objects/metadata.json:685:            "box with Nvidia Logo",
objects/metadata.json:686:            "white box with Nvidia Logo"
objects/metadata.json:689:    "box15.usd": {
objects/metadata.json:691:            "box",
objects/metadata.json:692:            "white box",
objects/metadata.json:693:            "plastic box",
objects/metadata.json:694:            "box with Tesla Logo",
objects/metadata.json:695:            "white box with Tesla Logo"
objects/metadata.json:827:    "cup00.usd": {
objects/metadata.json:829:            "cup",
objects/metadata.json:830:            "tall cup",
objects/metadata.json:831:            "cone-shaped cup",
objects/metadata.json:832:            "tall cone-shaped cup"
objects/metadata.json:835:    "cup01.usd": {
objects/metadata.json:837:            "cup",
objects/metadata.json:838:            "yellow cup",
objects/metadata.json:839:            "tall cup",
objects/metadata.json:840:            "cup with red flower",
objects/metadata.json:841:            "yellow tall cup",
objects/metadata.json:842:            "yellow cup with red flower",
objects/metadata.json:843:            "tall cup with red flower",
objects/metadata.json:844:            "yellow tall cup with red flower"
objects/metadata.json:847:    "cup02.usd": {
objects/metadata.json:849:            "cup",
objects/metadata.json:850:            "yellow cup",
objects/metadata.json:851:            "tall cup",
objects/metadata.json:852:            "cup with red watermelon",
objects/metadata.json:853:            "yellow tall cup",
objects/metadata.json:854:            "yellow cup with red watermelon",
objects/metadata.json:855:            "tall cup with red watermelon",
objects/metadata.json:856:            "yellow tall cup with red watermelon"
objects/metadata.json:859:    "cup03.usd": {
objects/metadata.json:861:            "cup",
objects/metadata.json:862:            "blue cup",
objects/metadata.json:863:            "tall cup",
objects/metadata.json:864:            "cup with NTU Singapore logo",
objects/metadata.json:865:            "blue tall cup",
objects/metadata.json:866:            "blue cup with NTU Singapore logo",
objects/metadata.json:867:            "tall cup with NTU Singapore logo",
objects/metadata.json:868:            "blue tall cup with NTU Singapore logo"
objects/metadata.json:871:    "cup04.usd": {
objects/metadata.json:873:            "cup",
objects/metadata.json:874:            "red cup",
objects/metadata.json:875:            "tall cup",
objects/metadata.json:876:            "cup with MMLab at NTU logo",
objects/metadata.json:877:            "red tall cup",
objects/metadata.json:878:            "red cup with MMLab at NTU logo",
objects/metadata.json:879:            "tall cup with MMLab at NTU logo",
objects/metadata.json:880:            "red tall cup with MMLab at NTU logo"
objects/metadata.json:883:    "cup05.usd": {
objects/metadata.json:885:            "cup",
objects/metadata.json:886:            "white cup",
objects/metadata.json:887:            "short cup",
objects/metadata.json:888:            "white short cup"
objects/metadata.json:891:    "cup06.usd": {
objects/metadata.json:893:            "cup",
objects/metadata.json:894:            "white cup",
objects/metadata.json:895:            "tall cup",
objects/metadata.json:896:            "white tall cup"
objects/metadata.json:899:    "cup07.usd": {
objects/metadata.json:901:            "cup",
objects/metadata.json:902:            "yellow cup",
objects/metadata.json:903:            "tall cup",
objects/metadata.json:904:            "yellow tall cup"
objects/metadata.json:907:    "cup08.usd": {
objects/metadata.json:909:            "cup",
objects/metadata.json:910:            "red cup",
objects/metadata.json:911:            "tall cup",
objects/metadata.json:912:            "red tall cup"
objects/metadata.json:915:    "cup09.usd": {
objects/metadata.json:917:            "cup",
objects/metadata.json:918:            "black cup",
objects/metadata.json:919:            "tall cup",
objects/metadata.json:920:            "black tall cup"
objects/metadata.json:1158:            "white big-flower patterned square placemat",
objects/metadata.json:1159:            "square mat with minimal large-floral design"
objects/metadata.json:1198:    "plate00.usd": {
objects/metadata.json:1200:            "plate",
objects/metadata.json:1201:            "yellow plate",
objects/metadata.json:1202:            "plate with red square patterns",
objects/metadata.json:1203:            "yellow plate with red square patterns"
objects/metadata.json:1206:    "plate01.usd": {
objects/metadata.json:1208:            "plate",
objects/metadata.json:1209:            "white plate"
objects/metadata.json:1212:    "plate02.usd": {
objects/metadata.json:1214:            "plate",
objects/metadata.json:1215:            "ceramic plate",
objects/metadata.json:1216:            "plate with blue floral patterns",
objects/metadata.json:1217:            "ceramic plate with blue floral patterns"
objects/metadata.json:1220:    "plate03.usd": {
objects/metadata.json:1222:            "plate",
objects/metadata.json:1223:            "white plate"
objects/metadata.json:1226:    "plate04.usd": {
objects/metadata.json:1228:            "plate",
objects/metadata.json:1229:            "white plate"
objects/metadata.json:1232:    "plate05.usd": {
objects/metadata.json:1234:            "plate",
objects/metadata.json:1235:            "yellow and red plate",
objects/metadata.json:1236:            "plate with floral patterns",
objects/metadata.json:1237:            "yellow and red plate with floral patterns"
objects/metadata.json:1240:    "plate06.usd": {
objects/metadata.json:1242:            "plate",
objects/metadata.json:1243:            "white plate",
objects/metadata.json:1244:            "plate with grey edge",
objects/metadata.json:1245:            "plate with black line patterns",
objects/metadata.json:1246:            "white plate with grey edge",
objects/metadata.json:1247:            "white plate with black line patterns",
objects/metadata.json:1248:            "plate with grey edge and black line patterns",
objects/metadata.json:1249:            "white plate with grey edge and black line patterns"
objects/metadata.json:1252:    "plate07.usd": {
objects/metadata.json:1254:            "plate",
objects/metadata.json:1255:            "yellow plate",
objects/metadata.json:1256:            "plate with white edge",
objects/metadata.json:1257:            "yellow plate with white edge"
objects/metadata.json:1260:    "plate08.usd": {
objects/metadata.json:1262:            "plate",
objects/metadata.json:1263:            "wooden plate"
objects/metadata.json:1266:    "plate09.usd": {
objects/metadata.json:1268:            "plate",
objects/metadata.json:1269:            "white plate"
objects/metadata.json:1272:    "plate10.usd": {
objects/metadata.json:1274:            "plate",
objects/metadata.json:1275:            "yellow and red plate",
objects/metadata.json:1276:            "plate with floral patterns",
objects/metadata.json:1277:            "yellow and red plate with floral patterns"
objects/metadata.json:1280:    "plate12.usd": {
objects/metadata.json:1282:            "plate",
objects/metadata.json:1283:            "blue plate"
objects/metadata.json:1286:    "plate13.usd": {
objects/metadata.json:1288:            "plate",
objects/metadata.json:1289:            "white plate"
objects/metadata.json:1292:    "plate14.usd": {
objects/metadata.json:1294:            "plate",
objects/metadata.json:1295:            "white plate",
objects/metadata.json:1296:            "plate with black edge",
objects/metadata.json:1297:            "plate with dragon patterns",
objects/metadata.json:1298:            "white plate with black edge",
objects/metadata.json:1299:            "white plate with dragon patterns",
objects/metadata.json:1300:            "plate with black edge and dragon patterns",
objects/metadata.json:1301:            "white plate with black edge and dragon patterns"
objects/metadata.json:1304:    "plate15.usd": {
objects/metadata.json:1306:            "plate",
objects/metadata.json:1307:            "white plate"
objects/metadata.json:1310:    "plate16.usd": {
objects/metadata.json:1312:            "plate",
objects/metadata.json:1313:            "plate with dart patterns"
objects/metadata.json:1434:    "tray00.usd": {
objects/metadata.json:1436:            "tray",
objects/metadata.json:1437:            "dark color tray",
objects/metadata.json:1438:            "wooden tray",
objects/metadata.json:1439:            "dark color wooden tray"
objects/metadata.json:1442:    "tray01.usd": {
objects/metadata.json:1444:            "tray",
objects/metadata.json:1445:            "white tray"
objects/metadata.json:1448:    "tray02.usd": {
objects/metadata.json:1450:            "tray",
objects/metadata.json:1451:            "red patterned tray"
objects/metadata.json:1454:    "tray03.usd": {
objects/metadata.json:1456:            "tray",
objects/metadata.json:1457:            "yellow tray",
objects/metadata.json:1458:            "tray with painting",
objects/metadata.json:1459:            "yellow tray with painting"
objects/metadata.json:1462:    "tray04.usd": {
objects/metadata.json:1464:            "tray",
objects/metadata.json:1465:            "light color tray",
objects/metadata.json:1466:            "wooden tray",
objects/metadata.json:1467:            "light color wooden tray"
objects/metadata.json:1470:    "tray05.usd": {
objects/metadata.json:1472:            "tray",
objects/metadata.json:1473:            "white tray",
objects/metadata.json:1474:            "tray with Bytedance logo",
objects/metadata.json:1475:            "white tray with Bytedance logo"
objects/metadata.json:1478:    "tray06.usd": {
objects/metadata.json:1480:            "tray",
objects/metadata.json:1481:            "white tray",
objects/metadata.json:1482:            "tray with NTU logo",
objects/metadata.json:1483:            "white tray with NTU logo"
objects/metadata.json:1486:    "tray07.usd": {
objects/metadata.json:1488:            "tray",
objects/metadata.json:1489:            "white tray",
objects/metadata.json:1490:            "tray with Meta logo",
objects/metadata.json:1491:            "white tray with Meta logo"
objects/metadata.json:1494:    "tray08.usd": {
objects/metadata.json:1496:            "tray",
objects/metadata.json:1497:            "white tray",
objects/metadata.json:1498:            "tray with CapitaLand logo",
objects/metadata.json:1499:            "white tray with CapitaLand logo"
objects/metadata.json:1502:    "tray09.usd": {
objects/metadata.json:1504:            "tray",
objects/metadata.json:1505:            "white tray",
objects/metadata.json:1506:            "tray with HSBC logo",
objects/metadata.json:1507:            "white tray with HSBC logo"
objects/metadata.json:1510:    "tray10.usd": {
objects/metadata.json:1512:            "tray",
objects/metadata.json:1513:            "white tray",
objects/metadata.json:1514:            "tray with Don Don Donki logo",
objects/metadata.json:1515:            "white tray with Don Don Donki logo"
objects/metadata.json:1518:    "tray11.usd": {
objects/metadata.json:1520:            "tray",
objects/metadata.json:1521:            "white tray",
objects/metadata.json:1522:            "tray with Shell logo",
objects/metadata.json:1523:            "white tray with Shell logo"
objects/metadata.json:1526:    "tray12.usd": {
objects/metadata.json:1528:            "tray",
objects/metadata.json:1529:            "white tray",
objects/metadata.json:1530:            "tray with Mastercard logo",
objects/metadata.json:1531:            "white tray with Mastercard logo"
objects/tree.md:103:├── bowl
objects/tree.md:105:│   │   ├── bowl00.jpg
objects/tree.md:106:│   │   ├── bowl01.jpg
objects/tree.md:107:│   │   ├── bowl02.jpg
objects/tree.md:108:│   │   ├── bowl04.jpg
objects/tree.md:109:│   │   ├── bowl06.jpg
objects/tree.md:110:│   │   ├── bowl07.jpg
objects/tree.md:111:│   │   ├── bowl08.jpg
objects/tree.md:112:│   │   ├── bowl09.jpg
objects/tree.md:113:│   │   ├── bowl10.jpg
objects/tree.md:114:│   │   ├── bowl11.jpg
objects/tree.md:115:│   │   ├── bowl12.jpg
objects/tree.md:116:│   │   ├── bowl13.jpg
objects/tree.md:117:│   │   ├── bowl14.jpg
objects/tree.md:118:│   │   ├── bowl15.jpg
objects/tree.md:119:│   │   ├── bowl16.jpg
objects/tree.md:120:│   │   ├── bowl17.jpg
objects/tree.md:121:│   │   ├── bowl18.jpg
objects/tree.md:122:│   │   └── bowl19.jpg
objects/tree.md:123:│   ├── bowl00.usd
objects/tree.md:124:│   ├── bowl01.usd
objects/tree.md:125:│   ├── bowl02.usd
objects/tree.md:126:│   ├── bowl04.usd
objects/tree.md:127:│   ├── bowl05.usd
objects/tree.md:128:│   ├── bowl06.usd
objects/tree.md:129:│   ├── bowl07.usd
objects/tree.md:130:│   ├── bowl08.usd
objects/tree.md:131:│   ├── bowl09.usd
objects/tree.md:132:│   ├── bowl10.usd
objects/tree.md:133:│   ├── bowl11.usd
objects/tree.md:134:│   ├── bowl12.usd
objects/tree.md:135:│   ├── bowl13.usd
objects/tree.md:136:│   ├── bowl14.usd
objects/tree.md:137:│   ├── bowl15.usd
objects/tree.md:138:│   ├── bowl16.usd
objects/tree.md:139:│   ├── bowl17.usd
objects/tree.md:140:│   ├── bowl18.usd
objects/tree.md:141:│   └── bowl19.usd
objects/tree.md:142:├── box
objects/tree.md:144:│   │   ├── box06.jpg
objects/tree.md:145:│   │   ├── box08.jpg
objects/tree.md:146:│   │   ├── box09.jpg
objects/tree.md:147:│   │   ├── box10.jpg
objects/tree.md:148:│   │   ├── box11.jpg
objects/tree.md:149:│   │   ├── box12.jpg
objects/tree.md:150:│   │   ├── box13.jpg
objects/tree.md:151:│   │   ├── box14.jpg
objects/tree.md:152:│   │   └── box15.jpg
objects/tree.md:153:│   ├── box00.usd
objects/tree.md:154:│   ├── box01.usd
objects/tree.md:155:│   ├── box02.usd
objects/tree.md:156:│   ├── box03.usd
objects/tree.md:157:│   ├── box04.usd
objects/tree.md:158:│   ├── box05.usd
objects/tree.md:159:│   ├── box06.usd
objects/tree.md:160:│   ├── box08.usd
objects/tree.md:161:│   ├── box09.usd
objects/tree.md:162:│   ├── box10.usd
objects/tree.md:163:│   ├── box11.usd
objects/tree.md:164:│   ├── box12.usd
objects/tree.md:165:│   ├── box13.usd
objects/tree.md:166:│   ├── box14.usd
objects/tree.md:167:│   └── box15.usd
objects/tree.md:204:├── cup
objects/tree.md:206:│   │   ├── cup01.jpg
objects/tree.md:207:│   │   ├── cup02.jpg
objects/tree.md:208:│   │   ├── cup03.jpg
objects/tree.md:209:│   │   └── cup04.jpg
objects/tree.md:210:│   ├── cup00.usd
objects/tree.md:211:│   ├── cup01.usd
objects/tree.md:212:│   ├── cup02.usd
objects/tree.md:213:│   ├── cup03.usd
objects/tree.md:214:│   ├── cup04.usd
objects/tree.md:215:│   ├── cup05.usd
objects/tree.md:216:│   ├── cup06.usd
objects/tree.md:217:│   ├── cup07.usd
objects/tree.md:218:│   ├── cup08.usd
objects/tree.md:219:│   └── cup09.usd
objects/tree.md:345:├── plate
objects/tree.md:347:│   │   ├── plate00.jpg
objects/tree.md:348:│   │   ├── plate02.jpg
objects/tree.md:349:│   │   ├── plate04.jpg
objects/tree.md:350:│   │   ├── plate05.jpg
objects/tree.md:351:│   │   ├── plate06.jpg
objects/tree.md:352:│   │   ├── plate07.jpg
objects/tree.md:353:│   │   ├── plate08.jpg
objects/tree.md:354:│   │   ├── plate10.jpg
objects/tree.md:355:│   │   ├── plate12.jpg
objects/tree.md:356:│   │   ├── plate14.jpg
objects/tree.md:357:│   │   └── plate16.jpg
objects/tree.md:358:│   ├── plate00.usd
objects/tree.md:359:│   ├── plate01.usd
objects/tree.md:360:│   ├── plate02.usd
objects/tree.md:361:│   ├── plate03.usd
objects/tree.md:362:│   ├── plate04.usd
objects/tree.md:363:│   ├── plate05.usd
objects/tree.md:364:│   ├── plate06.usd
objects/tree.md:365:│   ├── plate07.usd
objects/tree.md:366:│   ├── plate08.usd
objects/tree.md:367:│   ├── plate09.usd
objects/tree.md:368:│   ├── plate10.usd
objects/tree.md:369:│   ├── plate12.usd
objects/tree.md:370:│   ├── plate13.usd
objects/tree.md:371:│   ├── plate14.usd
objects/tree.md:372:│   ├── plate15.usd
objects/tree.md:373:│   └── plate16.usd
objects/tree.md:419:├── tray
objects/tree.md:421:│   │   ├── tray00.jpg
objects/tree.md:422:│   │   ├── tray02.jpg
objects/tree.md:423:│   │   ├── tray03.jpg
objects/tree.md:424:│   │   ├── tray04.jpg
objects/tree.md:425:│   │   ├── tray05.jpg
objects/tree.md:426:│   │   ├── tray06.jpg
objects/tree.md:427:│   │   ├── tray07.jpg
objects/tree.md:428:│   │   ├── tray08.jpg
objects/tree.md:429:│   │   ├── tray09.jpg
objects/tree.md:430:│   │   ├── tray10.jpg
objects/tree.md:431:│   │   ├── tray11.jpg
objects/tree.md:432:│   │   └── tray12.jpg
objects/tree.md:433:│   ├── tray04.usd
objects/tree.md:434:│   ├── tray05.usd
objects/tree.md:435:│   ├── tray06.usd
objects/tree.md:436:│   ├── tray07.usd
objects/tree.md:437:│   ├── tray08.usd
objects/tree.md:438:│   ├── tray09.usd
objects/tree.md:439:│   ├── tray10.usd
objects/tree.md:440:│   ├── tray11.usd
objects/tree.md:441:│   └── tray12.usd
objects/tree.md:447:│   │   ├── cup99.jpg
objects/tree.md:451:│   ├── cup99.usd
objects/metadata.json:388:    "bowl00.usd": {
objects/metadata.json:390:            "bowl",
objects/metadata.json:391:            "pure red bowl"
objects/metadata.json:394:    "bowl01.usd": {
objects/metadata.json:396:            "bowl",
objects/metadata.json:397:            "ceramic bowl",
objects/metadata.json:398:            "bowl with enameled gold rim",
objects/metadata.json:399:            "ceramic bowl with enameled gold rim"
objects/metadata.json:402:    "bowl02.usd": {
objects/metadata.json:404:            "bowl",
objects/metadata.json:405:            "orange bowl",
objects/metadata.json:406:            "bowl with black saw-shaped stripes",
objects/metadata.json:407:            "orange bowl with black saw-shaped stripes"
objects/metadata.json:410:    "bowl04.usd": {
objects/metadata.json:412:            "bowl",
objects/metadata.json:413:            "white bowl",
objects/metadata.json:414:            "deep bowl",
objects/metadata.json:415:            "white deep bowl"
objects/metadata.json:418:    "bowl05.usd": {
objects/metadata.json:420:            "bowl",
objects/metadata.json:421:            "grey bowl",
objects/metadata.json:422:            "shallow bowl",
objects/metadata.json:423:            "bowl with large bottom surface",
objects/metadata.json:424:            "grey shallow bowl",
objects/metadata.json:425:            "grey bowl with large bottom surface",
objects/metadata.json:426:            "shallow bowl with large bottom surface",
objects/metadata.json:427:            "grey shallow bowl with large bottom surface"
objects/metadata.json:430:    "bowl06.usd": {
objects/metadata.json:432:            "bowl",
objects/metadata.json:433:            "ceramic bowl",
objects/metadata.json:434:            "deep bowl",
objects/metadata.json:435:            "bowl with black stripes",
objects/metadata.json:436:            "ceramic deep bowl",
objects/metadata.json:437:            "ceramic bowl with black stripes",
objects/metadata.json:438:            "deep bowl with black stripes",
objects/metadata.json:439:            "ceramic deep bowl with black stripes"
objects/metadata.json:442:    "bowl07.usd": {
objects/metadata.json:444:            "bowl",
objects/metadata.json:445:            "dark brown bowl",
objects/metadata.json:446:            "wooden bowl",
objects/metadata.json:447:            "dark brown wooden bowl",
objects/metadata.json:448:            "shallow bowl",
objects/metadata.json:449:            "wooden shallow bowl"
objects/metadata.json:452:    "bowl08.usd": {
objects/metadata.json:454:            "bowl",
objects/metadata.json:455:            "dark brown bowl",
objects/metadata.json:456:            "wooden bowl",
objects/metadata.json:457:            "dark brown wooden bowl",
objects/metadata.json:458:            "deep bowl",
objects/metadata.json:459:            "wooden deep bowl"
objects/metadata.json:462:    "bowl09.usd": {
objects/metadata.json:464:            "bowl",
objects/metadata.json:465:            "dark brown bowl",
objects/metadata.json:466:            "wooden bowl",
objects/metadata.json:467:            "light brown wooden bowl",
objects/metadata.json:468:            "shallow bowl",
objects/metadata.json:469:            "wooden shallow bowl"
objects/metadata.json:472:    "bowl10.usd": {
objects/metadata.json:474:            "bowl",
objects/metadata.json:475:            "wooden bowl",
objects/metadata.json:476:            "deep bowl",
objects/metadata.json:477:            "wooden deep bowl"
objects/metadata.json:480:    "bowl11.usd": {
objects/metadata.json:482:            "bowl",
objects/metadata.json:483:            "ceramic bowl",
objects/metadata.json:484:            "deep bowl",
objects/metadata.json:485:            "bowl with cyan patterns",
objects/metadata.json:486:            "ceramic deep bowl",
objects/metadata.json:487:            "ceramic bowl with cyan patterns",
objects/metadata.json:488:            "deep bowl with cyan patterns",
objects/metadata.json:489:            "ceramic deep bowl with cyan patterns"
objects/metadata.json:492:    "bowl12.usd": {
objects/metadata.json:494:            "bowl",
objects/metadata.json:495:            "ceramic bowl",
objects/metadata.json:496:            "deep bowl",
objects/metadata.json:497:            "bowl with floral patterns",
objects/metadata.json:498:            "ceramic deep bowl",
objects/metadata.json:499:            "ceramic bowl with floral patterns",
objects/metadata.json:500:            "deep bowl with floral patterns",
objects/metadata.json:501:            "ceramic deep bowl with floral patterns"
objects/metadata.json:504:    "bowl13.usd": {
objects/metadata.json:506:            "bowl",
objects/metadata.json:507:            "ceramic bowl",
objects/metadata.json:508:            "shallow bowl",
objects/metadata.json:509:            "bowl with floral patterns",
objects/metadata.json:510:            "ceramic shallow bowl",
objects/metadata.json:511:            "ceramic bowl with floral patterns",
objects/metadata.json:512:            "shallow bowl with floral patterns",
objects/metadata.json:513:            "ceramic shallow bowl with floral patterns"
objects/metadata.json:516:    "bowl14.usd": {
objects/metadata.json:518:            "bowl",
objects/metadata.json:519:            "marble bowl",
objects/metadata.json:520:            "deep bowl",
objects/metadata.json:521:            "marble deep bowl"
objects/metadata.json:524:    "bowl15.usd": {
objects/metadata.json:526:            "bowl",
objects/metadata.json:527:            "wooden bowl",
objects/metadata.json:528:            "shallow bowl",
objects/metadata.json:529:            "wooden shallow bowl"

## Candidate receptacle-like variants
- bowl/bowl00 -> bowl/bowl00.usd
- bowl/bowl01 -> bowl/bowl01.usd
- bowl/bowl02 -> bowl/bowl02.usd
- bowl/bowl04 -> bowl/bowl04.usd
- bowl/bowl05 -> bowl/bowl05.usd
- bowl/bowl06 -> bowl/bowl06.usd
- bowl/bowl07 -> bowl/bowl07.usd
- bowl/bowl08 -> bowl/bowl08.usd
- bowl/bowl09 -> bowl/bowl09.usd
- bowl/bowl10 -> bowl/bowl10.usd
- bowl/bowl11 -> bowl/bowl11.usd
- bowl/bowl12 -> bowl/bowl12.usd
- bowl/bowl13 -> bowl/bowl13.usd
- bowl/bowl14 -> bowl/bowl14.usd
- bowl/bowl15 -> bowl/bowl15.usd
- bowl/bowl16 -> bowl/bowl16.usd
- bowl/bowl17 -> bowl/bowl17.usd
- bowl/bowl18 -> bowl/bowl18.usd
- bowl/bowl19 -> bowl/bowl19.usd
- box/box00 -> box/box00.usd
- box/box01 -> box/box01.usd
- box/box02 -> box/box02.usd
- box/box03 -> box/box03.usd
- box/box04 -> box/box04.usd
- box/box05 -> box/box05.usd
- box/box06 -> box/box06.usd
- box/box08 -> box/box08.usd
- box/box09 -> box/box09.usd
- box/box10 -> box/box10.usd
- box/box11 -> box/box11.usd
- box/box12 -> box/box12.usd
- box/box13 -> box/box13.usd
- box/box14 -> box/box14.usd
- box/box15 -> box/box15.usd
- cup/cup00 -> cup/cup00.usd
- cup/cup01 -> cup/cup01.usd
- cup/cup02 -> cup/cup02.usd
- cup/cup03 -> cup/cup03.usd
- cup/cup04 -> cup/cup04.usd
- cup/cup05 -> cup/cup05.usd
- cup/cup06 -> cup/cup06.usd
- cup/cup07 -> cup/cup07.usd
- cup/cup08 -> cup/cup08.usd
- cup/cup09 -> cup/cup09.usd
- plate/plate00 -> plate/plate00.usd
- plate/plate01 -> plate/plate01.usd
- plate/plate02 -> plate/plate02.usd
- plate/plate03 -> plate/plate03.usd
- plate/plate04 -> plate/plate04.usd
- plate/plate05 -> plate/plate05.usd
- plate/plate06 -> plate/plate06.usd
- plate/plate07 -> plate/plate07.usd
- plate/plate08 -> plate/plate08.usd
- plate/plate09 -> plate/plate09.usd
- plate/plate10 -> plate/plate10.usd
- plate/plate12 -> plate/plate12.usd
- plate/plate13 -> plate/plate13.usd
- plate/plate14 -> plate/plate14.usd
- plate/plate15 -> plate/plate15.usd
- plate/plate16 -> plate/plate16.usd
- tray/tray04 -> tray/tray04.usd
- tray/tray05 -> tray/tray05.usd
- tray/tray06 -> tray/tray06.usd
- tray/tray07 -> tray/tray07.usd
- tray/tray08 -> tray/tray08.usd
- tray/tray09 -> tray/tray09.usd
- tray/tray10 -> tray/tray10.usd
- tray/tray11 -> tray/tray11.usd
- tray/tray12 -> tray/tray12.usd
- unseen_cup/cup99 -> unseen/cup99.usd

candidate_count=70
## Receptacle size inspection
| category | variant | usd | exists | approx_note |
|---|---|---|---:|---|
| bowl | bowl00 | bowl/bowl00.usd | True | mentions bowl;  |
| bowl | bowl01 | bowl/bowl01.usd | True | mentions bowl;  |
| bowl | bowl02 | bowl/bowl02.usd | True | mentions bowl;  |
| bowl | bowl04 | bowl/bowl04.usd | True | mentions bowl;  |
| bowl | bowl05 | bowl/bowl05.usd | True | mentions bowl;  |
| bowl | bowl06 | bowl/bowl06.usd | True | mentions bowl;  |
| bowl | bowl07 | bowl/bowl07.usd | True | mentions bowl;  |
| bowl | bowl08 | bowl/bowl08.usd | True | mentions bowl;  |
| bowl | bowl09 | bowl/bowl09.usd | True | mentions bowl;  |
| bowl | bowl10 | bowl/bowl10.usd | True | mentions bowl;  |
| bowl | bowl11 | bowl/bowl11.usd | True | mentions bowl;  |
| bowl | bowl12 | bowl/bowl12.usd | True | mentions bowl;  |
| bowl | bowl13 | bowl/bowl13.usd | True | mentions bowl;  |
| bowl | bowl14 | bowl/bowl14.usd | True | mentions bowl;  |
| bowl | bowl15 | bowl/bowl15.usd | True | mentions bowl;  |
| bowl | bowl16 | bowl/bowl16.usd | True | mentions bowl;  |
| bowl | bowl17 | bowl/bowl17.usd | True | mentions bowl;  |
| bowl | bowl18 | bowl/bowl18.usd | True | mentions bowl;  |
| bowl | bowl19 | bowl/bowl19.usd | True | mentions bowl;  |
| box | box00 | box/box00.usd | True |  |
| box | box01 | box/box01.usd | True |  |
| box | box02 | box/box02.usd | True |  |
| box | box03 | box/box03.usd | True |  |
| box | box04 | box/box04.usd | True |  |
| box | box05 | box/box05.usd | True |  |
| box | box06 | box/box06.usd | True |  |
| box | box08 | box/box08.usd | True |  |
| box | box09 | box/box09.usd | True |  |
| box | box10 | box/box10.usd | True |  |
| box | box11 | box/box11.usd | True |  |
| box | box12 | box/box12.usd | True |  |
| box | box13 | box/box13.usd | True |  |
| box | box14 | box/box14.usd | True |  |
| box | box15 | box/box15.usd | True |  |
| cup | cup00 | cup/cup00.usd | True | has extent;  |
| cup | cup01 | cup/cup01.usd | True | has extent;  |
| cup | cup02 | cup/cup02.usd | True | has extent;  |
| cup | cup03 | cup/cup03.usd | True | has extent;  |
| cup | cup04 | cup/cup04.usd | True | has extent;  |
| cup | cup05 | cup/cup05.usd | True | has extent;  |
| cup | cup06 | cup/cup06.usd | True | has extent;  |
| cup | cup07 | cup/cup07.usd | True | has extent;  |
| cup | cup08 | cup/cup08.usd | True | has extent;  |
| cup | cup09 | cup/cup09.usd | True | has extent;  |
| plate | plate00 | plate/plate00.usd | True |  |
| plate | plate01 | plate/plate01.usd | True |  |
| plate | plate02 | plate/plate02.usd | True |  |
| plate | plate03 | plate/plate03.usd | True |  |
| plate | plate04 | plate/plate04.usd | True |  |
| plate | plate05 | plate/plate05.usd | True |  |
| plate | plate06 | plate/plate06.usd | True |  |
| plate | plate07 | plate/plate07.usd | True |  |
| plate | plate08 | plate/plate08.usd | True |  |
| plate | plate09 | plate/plate09.usd | True |  |
| plate | plate10 | plate/plate10.usd | True |  |
| plate | plate12 | plate/plate12.usd | True |  |
| plate | plate13 | plate/plate13.usd | True |  |
| plate | plate14 | plate/plate14.usd | True |  |
| plate | plate15 | plate/plate15.usd | True |  |
| plate | plate16 | plate/plate16.usd | True |  |
| tray | tray04 | tray/tray04.usd | True | mentions tray;  |
| tray | tray05 | tray/tray05.usd | True | mentions tray;  |
| tray | tray06 | tray/tray06.usd | True | mentions tray;  |
| tray | tray07 | tray/tray07.usd | True | mentions tray;  |
| tray | tray08 | tray/tray08.usd | True | mentions tray;  |
| tray | tray09 | tray/tray09.usd | True | mentions tray;  |
| tray | tray10 | tray/tray10.usd | True | mentions tray;  |
| tray | tray11 | tray/tray11.usd | True | mentions tray;  |
| tray | tray12 | tray/tray12.usd | True | mentions tray;  |
| unseen_cup | cup99 | unseen/cup99.usd | True | has extent;  |
SELECTED_RECEPTACLE_CATEGORY tray
SELECTED_RECEPTACLE_LABEL tray
SELECTED_RECEPTACLE_VARIANT tray04
SELECTED_RECEPTACLE_USD tray/tray04.usd
RECEPTACLE_CATEGORY=tray
RECEPTACLE_LABEL=tray
RECEPTACLE_VARIANT=tray04
RECEPTACLE_USD=tray/tray04.usd

## Scene/task code relevant files
src/franka_wrist_camera_scene/collection/pick_place.py:13:from franka_wrist_camera_scene.episode.reset import reset_pick_place_episode
src/franka_wrist_camera_scene/collection/pick_place.py:14:from franka_wrist_camera_scene.episode.success import pick_place_success
src/franka_wrist_camera_scene/collection/pick_place.py:17:from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg, make_tabletop_scene_cfg
src/franka_wrist_camera_scene/collection/pick_place.py:21:from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
src/franka_wrist_camera_scene/collection/pick_place.py:74:        object_pos_local=policy.spec.object_pos_local,
src/franka_wrist_camera_scene/collection/pick_place.py:75:        place_pos_local=policy.spec.place_pos_local,
src/franka_wrist_camera_scene/collection/pick_place.py:143:    success = bool(pick_place_success(scene, policy.spec)[0].item())
src/franka_wrist_camera_scene/collection/pick_place.py:180:        make_tabletop_scene_cfg(
src/franka_wrist_camera_scene/collection/pick_place.py:189:    spec = PickPlaceTaskSpec()
src/franka_wrist_camera_scene/collection/pick_place.py:236:        reset_pick_place_episode(scene, episode_spec)
src/franka_wrist_camera_scene/episode/reset.py:9:from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
src/franka_wrist_camera_scene/episode/reset.py:27:def reset_pick_place_objects(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
src/franka_wrist_camera_scene/episode/reset.py:32:    pos_local = torch.tensor(spec.object_pos_local, device=root_state.device).view(1, 3)
src/franka_wrist_camera_scene/episode/reset.py:42:def reset_pick_place_episode(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
src/franka_wrist_camera_scene/episode/recorder.py:29:    object_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/recorder.py:30:    place_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/recorder.py:148:            object_pos_local=self.object_pos_local,
src/franka_wrist_camera_scene/episode/recorder.py:149:            place_pos_local=self.place_pos_local,
src/franka_wrist_camera_scene/episode/success.py:8:from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
src/franka_wrist_camera_scene/episode/success.py:11:def pick_place_success(
src/franka_wrist_camera_scene/episode/success.py:13:    spec: PickPlaceTaskSpec,
src/franka_wrist_camera_scene/episode/success.py:21:    target_pos_local = torch.tensor(spec.place_pos_local, device=obj_pos_w.device).view(1, 3)
src/franka_wrist_camera_scene/episode/schema.py:24:    object_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/schema.py:25:    place_pos_local: tuple[float, float, float] | None = None
src/franka_wrist_camera_scene/episode/manifest.py:17:    object_pos_local: tuple[float, float, float] | None
src/franka_wrist_camera_scene/episode/manifest.py:18:    place_pos_local: tuple[float, float, float] | None
src/franka_wrist_camera_scene/episode/manifest.py:67:                object_pos_local=tuple(meta["object_pos_local"]) if meta.get("object_pos_local") is not None else None,
src/franka_wrist_camera_scene/episode/manifest.py:68:                place_pos_local=tuple(meta["place_pos_local"]) if meta.get("place_pos_local") is not None else None,
src/franka_wrist_camera_scene/scene/tabletop.py:6:from isaaclab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
src/franka_wrist_camera_scene/scene/tabletop.py:33:    warehouse = AssetBaseCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:36:        init_state=AssetBaseCfg.InitialStateCfg(pos=(-4.0, -2.0, 0.0)),
src/franka_wrist_camera_scene/scene/tabletop.py:39:    table = AssetBaseCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:47:        init_state=AssetBaseCfg.InitialStateCfg(pos=(0.45, 0.0, TABLE_HEIGHT_M - 0.5 * TABLE_SIZE[2])),
src/franka_wrist_camera_scene/scene/tabletop.py:50:    dome_light = AssetBaseCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:59:    target_cube = RigidObjectCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:70:        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.58, -0.16, TABLE_HEIGHT_M + 0.05)),
src/franka_wrist_camera_scene/scene/tabletop.py:73:    place_target = AssetBaseCfg(
src/franka_wrist_camera_scene/scene/tabletop.py:79:        init_state=AssetBaseCfg.InitialStateCfg(pos=(0.55, 0.22, TABLE_HEIGHT_M + 0.002)),
src/franka_wrist_camera_scene/scene/tabletop.py:112:def make_tabletop_scene_cfg(
src/franka_wrist_camera_scene/scene/tabletop.py:120:    scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
src/franka_wrist_camera_scene/scene/tabletop.py:131:        if scene_cfg.target_cube.spawn.mass_props is None:
src/franka_wrist_camera_scene/scene/tabletop.py:132:            scene_cfg.target_cube.spawn.mass_props = sim_utils.schemas.MassPropertiesCfg()
src/franka_wrist_camera_scene/scene/tabletop.py:133:        scene_cfg.target_cube.spawn.mass_props.mass = float(physics_overrides["target_mass"])
src/franka_wrist_camera_scene/scene/tabletop.py:135:        scene_cfg.target_cube.spawn.rigid_props.linear_damping = float(physics_overrides["target_linear_damping"])
src/franka_wrist_camera_scene/scene/tabletop.py:137:        scene_cfg.target_cube.spawn.rigid_props.angular_damping = float(physics_overrides["target_angular_damping"])
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:11:from ..tasks.pick_place import PickPlaceTaskSpec
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:18:    def __init__(self, spec: PickPlaceTaskSpec):
src/franka_wrist_camera_scene/policies/pick_place_scripted.py:58:        place_local = torch.tensor(self.spec.place_pos_local, device=self._device)
src/franka_wrist_camera_scene/tasks/pick_place.py:10:class PickPlaceTaskSpec(TaskSpec):
src/franka_wrist_camera_scene/tasks/pick_place.py:13:    object_name: str = "target_cube"
src/franka_wrist_camera_scene/tasks/pick_place.py:17:    object_pos_local: tuple[float, float, float] = (0.58, -0.16, 1.08)
src/franka_wrist_camera_scene/tasks/pick_place.py:18:    place_pos_local: tuple[float, float, float] = (0.55, 0.22, 1.08)
src/franka_wrist_camera_scene/tasks/pick_place.py:46:    base_spec: PickPlaceTaskSpec,
src/franka_wrist_camera_scene/tasks/pick_place.py:50:) -> PickPlaceTaskSpec:
src/franka_wrist_camera_scene/tasks/pick_place.py:52:        base_spec.object_pos_local[0] + object_xy_offset[0],
src/franka_wrist_camera_scene/tasks/pick_place.py:53:        base_spec.object_pos_local[1] + object_xy_offset[1],
src/franka_wrist_camera_scene/tasks/pick_place.py:54:        base_spec.object_pos_local[2],
src/franka_wrist_camera_scene/tasks/pick_place.py:57:        base_spec.place_pos_local[0] + place_xy_offset[0],
src/franka_wrist_camera_scene/tasks/pick_place.py:58:        base_spec.place_pos_local[1] + place_xy_offset[1],
src/franka_wrist_camera_scene/tasks/pick_place.py:59:        base_spec.place_pos_local[2],
src/franka_wrist_camera_scene/tasks/pick_place.py:62:    return PickPlaceTaskSpec(
src/franka_wrist_camera_scene/tasks/pick_place.py:66:        object_pos_local=object_pos,
src/franka_wrist_camera_scene/tasks/pick_place.py:67:        place_pos_local=place_pos,
src/franka_wrist_camera_scene/export/ila.py:59:        "object_pos_local": meta["object_pos_local"],
src/franka_wrist_camera_scene/export/ila.py:60:        "place_pos_local": meta["place_pos_local"],
scripts/inspect_collection.py:42:        "object_pos_local": tuple(meta["object_pos_local"]),
scripts/inspect_collection.py:43:        "place_pos_local": tuple(meta["place_pos_local"]),
scripts/inspect_collection.py:97:        tuple(round(float(x), 4) for x in summary["object_pos_local"]),
scripts/inspect_collection.py:98:        tuple(round(float(x), 4) for x in summary["place_pos_local"]),
scripts/inspect_collection.py:110:    print(f"{'object_pos_local':<26} {'place_pos_local':<26} {'success':<8}")
scripts/debug_scene.py:69:from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg, make_tabletop_scene_cfg
scripts/debug_scene.py:72:from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
scripts/debug_scene.py:74:from franka_wrist_camera_scene.episode.reset import reset_robot_to_default, reset_pick_place_episode
scripts/debug_scene.py:75:from franka_wrist_camera_scene.episode.success import pick_place_success
scripts/debug_scene.py:110:        obj_pos = scene["target_cube"].data.root_pos_w[0].cpu().numpy()
scripts/debug_scene.py:143:                    success = pick_place_success(scene, policy.spec)
scripts/debug_scene.py:168:    scene_cfg = make_tabletop_scene_cfg(
scripts/debug_scene.py:186:        spec = PickPlaceTaskSpec()
scripts/debug_scene.py:198:        reset_pick_place_episode(scene, spec)

## Receptacle goal patch diff
diff --git a/src/franka_wrist_camera_scene/collection/pick_place.py b/src/franka_wrist_camera_scene/collection/pick_place.py
index 80b2244..3b44c4e 100644
--- a/src/franka_wrist_camera_scene/collection/pick_place.py
+++ b/src/franka_wrist_camera_scene/collection/pick_place.py
@@ -174,6 +174,20 @@ def collect_pick_place_dataset(
         variant_id=target_object_cfg["variant_id"],
     )
 
+    goal_receptacle_cfg = collection_cfg.get("goal_receptacle")
+    goal_receptacle_context = None
+    goal_receptacle_pos_local = None
+    goal_receptacle_scale = None
+    if goal_receptacle_cfg:
+        goal_receptacle_context = load_catalog_object_context(
+            catalog_config=goal_receptacle_cfg["catalog_config"],
+            category_id=goal_receptacle_cfg["category_id"],
+            variant_id=goal_receptacle_cfg["variant_id"],
+        )
+        goal_receptacle_pos_local = tuple(float(x) for x in goal_receptacle_cfg.get("pos_local", [0.55, 0.22, 1.08]))
+        if "scale" in goal_receptacle_cfg:
+            goal_receptacle_scale = tuple(float(x) for x in goal_receptacle_cfg["scale"])
+
     durable_usd_path = object_context.usd_path.relative_to(REPO_ROOT).as_posix()
 
     scene = InteractiveScene(
@@ -182,6 +196,9 @@ def collect_pick_place_dataset(
             num_envs=1,
             env_spacing=2.5,
             physics_overrides=collection_cfg.get("physics_overrides", {}),
+            goal_receptacle_context=goal_receptacle_context,
+            goal_receptacle_pos_local=goal_receptacle_pos_local,
+            goal_receptacle_scale=goal_receptacle_scale,
         )
     )
     robot: Articulation = scene["robot"]
diff --git a/src/franka_wrist_camera_scene/scene/tabletop.py b/src/franka_wrist_camera_scene/scene/tabletop.py
index 7b97b17..5876001 100644
--- a/src/franka_wrist_camera_scene/scene/tabletop.py
+++ b/src/franka_wrist_camera_scene/scene/tabletop.py
@@ -114,11 +114,35 @@ def make_tabletop_scene_cfg(
     num_envs: int = 1,
     env_spacing: float = 2.5,
     physics_overrides: dict | None = None,
+    goal_receptacle_context: CatalogObjectContext | None = None,
+    goal_receptacle_pos_local: tuple[float, float, float] | None = None,
+    goal_receptacle_scale: tuple[float, float, float] | None = None,
 ) -> TabletopFrankaSceneCfg:
     """Create a tabletop scene configuration with the specified target object."""
     scene_cfg = TabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
     scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
 
+    # Optional static receptacle goal object for harder place-inside tasks.
+    # This is config-driven and disabled by default, so old pick-place configs behave unchanged.
+    if goal_receptacle_context is not None:
+        receptacle_pos = goal_receptacle_pos_local or (0.55, 0.22, TABLE_HEIGHT_M + 0.05)
+        receptacle_scale = goal_receptacle_scale or scene_cfg.target_cube.spawn.scale
+        scene_cfg.goal_receptacle = RigidObjectCfg(
+            prim_path="{ENV_REGEX_NS}/GoalReceptacle",
+            spawn=sim_utils.UsdFileCfg(
+                usd_path=str(goal_receptacle_context.usd_path),
+                scale=receptacle_scale,
+                rigid_props=sim_utils.RigidBodyPropertiesCfg(
+                    kinematic_enabled=True,
+                    disable_gravity=True,
+                    linear_damping=1.0,
+                    angular_damping=10.0,
+                ),
+                collision_props=sim_utils.CollisionPropertiesCfg(),
+            ),
+            init_state=RigidObjectCfg.InitialStateCfg(pos=receptacle_pos),
+        )
+
     # Baseline local Isaac 4.5 stabilization defaults.
     if "panda_hand" in scene_cfg.robot.actuators:
         scene_cfg.robot.actuators["panda_hand"].stiffness = 150.0

## Receptacle test configs

### configs/receptacle_goal_tests/receptacle_tray_tray04_apple01_default.yaml
output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_apple01_default
start_episode_id: 0
num_episodes: 1
max_steps: 2600
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 123

target_object:
  catalog_config: object_catalog.generated.yaml
  category_id: apple
  variant_id: apple01

goal_receptacle:
  catalog_config: object_catalog.generated.yaml
  category_id: tray
  variant_id: tray04
  pos_local: [0.55, 0.22, 1.08]
  scale: [0.085, 0.085, 0.085]
  fixed: true

pose_randomization:
  object_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]
  place_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]

lighting_randomization:
  dome_light_intensity_range: [650.0, 1200.0]
  dome_light_color_options:
    - [0.90, 0.90, 0.90]
    - [1.00, 0.92, 0.84]
    - [0.82, 0.88, 1.00]

### configs/receptacle_goal_tests/receptacle_tray_tray04_cup05_default.yaml
output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_cup05_default
start_episode_id: 0
num_episodes: 1
max_steps: 2600
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 123

target_object:
  catalog_config: object_catalog.generated.yaml
  category_id: cup
  variant_id: cup05

goal_receptacle:
  catalog_config: object_catalog.generated.yaml
  category_id: tray
  variant_id: tray04
  pos_local: [0.55, 0.22, 1.08]
  scale: [0.085, 0.085, 0.085]
  fixed: true

pose_randomization:
  object_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]
  place_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]

lighting_randomization:
  dome_light_intensity_range: [650.0, 1200.0]
  dome_light_color_options:
    - [0.90, 0.90, 0.90]
    - [1.00, 0.92, 0.84]
    - [0.82, 0.88, 1.00]

### configs/receptacle_goal_tests/receptacle_tray_tray04_fcan03_mass020.yaml
output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020
start_episode_id: 0
num_episodes: 1
max_steps: 2600
settle_time_s: 1.0

record_cameras: true
camera_fps: 30
record_depth: true

seed: 123

target_object:
  catalog_config: object_catalog.generated.yaml
  category_id: can
  variant_id: fcan03

goal_receptacle:
  catalog_config: object_catalog.generated.yaml
  category_id: tray
  variant_id: tray04
  pos_local: [0.55, 0.22, 1.08]
  scale: [0.085, 0.085, 0.085]
  fixed: true

physics_overrides:
  target_mass: 0.20
  gripper_stiffness: 150.0
  gripper_damping: 15.0

pose_randomization:
  object_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]
  place_xy_range:
    x: [0.0, 0.0]
    y: [0.0, 0.0]

lighting_randomization:
  dome_light_intensity_range: [650.0, 1200.0]
  dome_light_color_options:
    - [0.90, 0.90, 0.90]
    - [1.00, 0.92, 0.84]
    - [0.82, 0.88, 1.00]

## Result receptacle_tray_tray04_apple01_default
- status: 0
- success_center_approx: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_apple01_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/receptacle_tray_tray04_apple01_default_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 500364 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_apple01_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_apple01_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the apple and place it on the target area",
  "success": true,
  "num_steps": 1933,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 484,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "apple",
  "object_variant_id": "apple01",
  "object_label": "apple",
  "object_usd_path": "objects/apple/apple01.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result receptacle_tray_tray04_cup05_default
- status: 0
- success_center_approx: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_cup05_default
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/receptacle_tray_tray04_cup05_default_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 451078 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_cup05_default/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_cup05_default/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the cup and place it on the target area",
  "success": true,
  "num_steps": 1933,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 484,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "cup",
  "object_variant_id": "cup05",
  "object_label": "cup",
  "object_usd_path": "objects/cup/cup05.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Result receptacle_tray_tray04_fcan03_mass020
- status: 0
- success_center_approx: YES
- output_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020
- video: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/receptacle_tray_tray04_fcan03_mass020_000000_SUCCESS_agent_plus_wrist.mp4
- video_size: 510031 bytes

### log tail
```
[INFO] Episode 0 success: True
[INFO] Saved episode data to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020/000000
[INFO] Saved collection manifest to: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020/manifest.json
```

### meta
```json
{
  "episode_id": 0,
  "task_name": "pick_place",
  "instruction": "pick up the can and place it on the target area",
  "success": true,
  "num_steps": 1953,
  "sim_dt": 0.008333333333333333,
  "seed": 123,
  "record_cameras": true,
  "record_depth": true,
  "num_camera_frames": 489,
  "object_pos_local": [
    0.58,
    -0.16,
    1.08
  ],
  "place_pos_local": [
    0.55,
    0.22,
    1.08
  ],
  "object_xy_offset": [
    0.0,
    0.0
  ],
  "place_xy_offset": [
    0.0,
    0.0
  ],
  "object_category_id": "can",
  "object_variant_id": "fcan03",
  "object_label": "can",
  "object_usd_path": "objects/can/fcan03.usd",
  "light_intensity": 1145.6593828734322,
  "light_color": [
    0.9,
    0.9,
    0.9
  ]
}
```

## Receptacle goal results table
| run | object | success_center_approx | steps | frames |
|---|---|---:|---:|---:|
| receptacle_tray_tray04_apple01_default | apple/apple01 | True | 1933 | 484 |
| receptacle_tray_tray04_cup05_default | cup/cup05 | True | 1933 | 484 |
| receptacle_tray_tray04_fcan03_mass020 | can/fcan03 | True | 1953 | 489 |

## Important note
Success is still the existing center-near-place metric, not yet a true inside-container geometric check.

# FINAL SUMMARY
- branch: object-integration-static-assets
- commit: ff269ae5926034c1f576747e32ce3875945a0564
- apple_recheck_after_receptacle_patch: YES
- videos_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos
- generated_video_count: 21
- generated_preview_count: 5
- patch_path: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/patches/receptacle_goal_object_test.patch

## git diff
 .../collection/pick_place.py                       | 17 +++++++++++++++
 src/franka_wrist_camera_scene/scene/tabletop.py    | 24 ++++++++++++++++++++++
 2 files changed, 41 insertions(+)

## git status
 M src/franka_wrist_camera_scene/collection/pick_place.py
 M src/franka_wrist_camera_scene/scene/tabletop.py
?? configs/receptacle_goal_tests/

## videos
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/apple_recheck_after_receptacle_patch_000000_SUCCESS_agent_plus_wrist.mp4 | 484914 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/receptacle_tray_tray04_apple01_default_000000_SUCCESS_agent_plus_wrist.mp4 | 500364 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/receptacle_tray_tray04_cup05_default_000000_SUCCESS_agent_plus_wrist.mp4 | 451078 bytes
/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/receptacle_tray_tray04_fcan03_mass020_000000_SUCCESS_agent_plus_wrist.mp4 | 510031 bytes
