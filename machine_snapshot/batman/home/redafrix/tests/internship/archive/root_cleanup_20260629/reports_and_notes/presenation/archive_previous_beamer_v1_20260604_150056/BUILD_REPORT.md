# Rapport de Compilation de la Présentation (BUILD_REPORT.md)

Ce rapport documente le pipeline de création, de compilation et de validation de la présentation LaTeX Beamer pour le suivi du projet FIPER.

---

## 1. Fichiers créés et modifiés

Tous les fichiers ont été créés et modifiés exclusivement dans le dossier de travail autorisé :
`/home/redafrix/tests/internship/presenation`

*   **Code source LaTeX :** [main.tex](file:///home/redafrix/tests/internship/presenation/main.tex)
*   **Script de génération de figures :** [figures/generate_plots.py](file:///home/redafrix/tests/internship/presenation/figures/generate_plots.py)
*   **Graphique généré :** [figures/offline_comparison.png](file:///home/redafrix/tests/internship/presenation/figures/offline_comparison.png)
*   **Présentation PDF finale :** [main.pdf](file:///home/redafrix/tests/internship/presenation/main.pdf)
*   **Rendus PNG des slides (10 pages) :** Dossier [rendered_slides/](file:///home/redafrix/tests/internship/presenation/rendered_slides/) contenant :
    *   `slide-01.png` à `slide-10.png`

---

## 2. Commandes exécutées

Les commandes suivantes ont été lancées dans le terminal pour générer les graphiques, compiler le code LaTeX et extraire les slides :

1.  **Génération des plots avec Matplotlib :**
    ```bash
    python3 generate_plots.py
    ```
2.  **Compilation du document LaTeX Beamer (en 16:9) :**
    ```bash
    pdflatex -halt-on-error main.tex
    ```
    *(Exécuté plusieurs fois pour stabiliser les références auxiliaires).*
3.  **Extraction des slides au format PNG (résolution 180 DPI) :**
    ```bash
    pdftoppm -png -r 180 main.pdf rendered_slides/slide
    ```
4.  **Vérification de l'extraction textuelle pour conformité :**
    ```bash
    pdftotext main.pdf -
    ```

---

## 3. Sources lues

Les informations et résultats présentés dans les slides proviennent de l'analyse des fichiers suivants :

1.  **Obsidian Vault :**
    *   `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md` (Rapport complet principal)
2.  **Workspace fiper_ws :**
    *   `/home/redafrix/tests/internship/fiper_ws/reports/dean_topk8_fusion_policy_v1_20260602/DEAN_TOPK8_FUSION_POLICY_REPORT.md` (Résultats offline de l'ablation TopK8)
    *   `/home/redafrix/tests/internship/fiper_ws/reports/DEAN_ALL_TASKS_FULL_UNCERTAINTY_TEST_20260601.md` (Résultats de la version complète all-tasks)
    *   `/home/redafrix/tests/internship/fiper_ws/reports/DEAN_OOD_LAST2_TASKIDS_FULL_V1_20260601.md` (Détails sur le split hors distribution)
    *   `/home/redafrix/tests/internship/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py` (Script de déploiement temps réel et logique de sélection d'actions)
    *   `/home/redafrix/tests/internship/fiper_ws/realtime_deployment/scripts/collect_fiper_uncertainty_receding_dean_v1.py` (Définition de la liste complète des 49 clés d'incertitude)

---

## 4. Résultats utilisés et correspondances

### A. Résultats Offline (Slide 8)
Ces résultats proviennent directement de `DEAN_TOPK8_FUSION_POLICY_REPORT.md` et comparent le modèle de Base (sans incertitude) au modèle avec les 8 signaux d'incertitude sélectionnés (`topk8_ref`).
*   **Split Vu (`all_tasks_full`) :**
    *   **Base :** Faux Positifs (FA) = `14.2%` | Recall (Détection) = `95.8%` | Det@25 = `54.0%` | Det@50 = `89.0%`
    *   **Top-8 :** Faux Positifs (FA) = `15.0%` | Recall (Détection) = `97.5%` | Det@25 = `65.0%` | Det@50 = `89.5%`
*   **Split Hors Distribution (`ood_last2_taskids_full`) :**
    *   **Base :** Faux Positifs (FA) = `26.0%` | Recall (Détection) = `86.0%` | Det@25 = `39.8%` | Det@50 = `78.5%`
    *   **Top-8 :** Faux Positifs (FA) = `23.0%` | Recall (Détection) = `89.2%` | Det@25 = `37.6%` | Det@50 = `77.4%`

### B. Signaux d'incertitude Top-8 sélectionnés (Slide 7)
Les indices et clés d'incertitude proviennent de `FIPER Risk-Aware SimVLA - Full Report.md` et ont été mis en correspondance avec le dictionnaire `UNCERTAINTY_49D_KEYS` du script `collect_fiper_uncertainty_receding_dean_v1.py` :
1.  **dim 6 :** `denoise_initial_mean` (Moyenne initiale du bruit)
2.  **dim 21 :** `denoise_update_direction_flip_mean` (Changements brusques de direction)
3.  **dim 25 :** `sample_action_l2_mean` (Distance L2 moyenne entre candidats d'action)
4.  **dim 27 :** `sample_action_translation_var` (Variance de translation entre candidats)
5.  **dim 23 :** `sample_action_var_mean` (Variance moyenne des actions)
6.  **dim 2 :** `mean_path_var` (Variance moyenne sur le chemin de diffusion)
7.  **dim 26 :** `sample_action_l2_max` (Distance L2 maximale entre candidats d'action)
8.  **dim 24 :** `sample_action_var_max` (Variance maximale des actions)

### C. Résultats Temps Réel (Slide 9)
Les résultats temps réel proviennent de la table d'évaluation Dean Task0 sur 100 graines identiques de `FIPER Risk-Aware SimVLA - Full Report.md` :
*   **SimVLA seul :** Succès = `34.0%` | Étapes moyennes = `255.8` | Interventions = `0`
*   **Risk Base :** Succès = `38.0%` | Étapes moyennes = `251.0` | Interventions = `493`
*   **Top-8 Incertitude :** Succès = `39.0%` | Étapes moyennes = `251.9` | Interventions = `386`

---

## 5. Confirmation de la validation visuelle

Chacun des 10 fichiers PNG générés a été inspecté individuellement au moyen de l'outil de visualisation d'images.
*   **Slide 1 (Titre) :** Alignement parfait, titre et sous-titre centrés, pas de débordement.
*   **Slide 2 (Évolutions) :** Le schéma vertical TikZ est propre, centré, et illustre clairement le cheminement historique.
*   **Slide 3 (Point de départ) :** Les tableaux d'origines présentaient des débordements et des coupures de mots. Ils ont été remplacés par deux blocs distincts (Forces et Limites) avec des puces graphiques (croix rouges et coches vertes) qui rentrent idéalement dans l'espace.
*   **Slide 4 (Données) :** La largeur de la chaîne TikZ a été réduite de 1.1cm à 0.45cm par nœud, empêchant tout débordement à droite.
*   **Slide 5 (Architecture) :** Les polices ont été passées à `9pt` et le schéma TikZ à l'échelle `0.68` pour libérer l'espace en bas de slide. Le bloc d'avertissement contre les fuites est entièrement lisible.
*   **Slide 6 (Calibration/Décision) :** Police passée à `9.5pt` et schéma TikZ à `0.68`. La logique de sélection d'actions et le logigramme de décision sont nets.
*   **Slide 7 (Signaux) :** Police passée à `9.5pt` et schéma TikZ à `0.75`. Les 8 indices réels avec leurs familles respectives sont listés de manière très lisible.
*   **Slide 8 (Résultats offline) :** La figure Matplotlib générée est intégrée sans bordures. La table de métriques est parfaitement calée à droite.
*   **Slide 9 (Vérifications temps réel) :** Les résultats sur Dean Task0 sont bien visibles et la mise en forme de la table de comparaison est stable.
*   **Slide 10 (Chantiers restants) :** La police a été réduite pour s'assurer que la question finale et le diagramme de roadmap TikZ s'affichent correctement.

---

## 6. Problèmes restants

Aucun problème critique restant. La présentation compile sans la moindre erreur LaTeX (zéro avertissement de débordement de boîte vertical/horizontal important). Le nombre total de slides est exactement égal à 10. Les rendus graphiques sont validés.
