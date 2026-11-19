# Registre des écarts · maquette (S4) → application (S5)

Ingryd Lo Tierzo Silva et Sara Lhasseni · tenu au fil de la construction. Version finale : une demi-page.
Légende : **[données]** choix sur les données · **[analyse]** choix analytique · **[outil]** écart imposé par l'outil.

| # | Écart | Pourquoi | Effet chiffré |
|---|---|---|---|
| E1 | **[outil]** Power BI abandonné ; application HTML publiée par GitHub Pages | Publication sans authentification impossible sans licence ni autorisation (retour du rendu 4, priorité 1) | — |
| E2 | **[outil]** Le prototype affichait des valeurs écrites en dur ; l'application recalcule chaque indicateur à partir des 149 811 lignes à chaque filtre | Consigne : « un indicateur se recalcule à chaque filtre » | Recalcul < 50 ms |
| E3 | **[données]** ID_AW 164662498 présent 3 fois (seul le poids du prix diffère : 60, 50, 40) : une seule ligne gardée | Grain : une ligne = une attribution | 149 813 → 149 811 lignes ; KPI 3 : 11 504 / 21 421 → 11 502 / 21 419 (53,7 % inchangé) ; médiane des montants 45 781 → 45 780 € |
| E4 | **[données]** NUMBER_OFFERS = 999 (3 lignes, BG 2014, même acheteur, 45 lots) mis à vide comme 940 | Valeur sentinelle probable, répond au retour du rendu 4 | KPI 1 : 32 573 / 117 473 → 32 573 / 117 468 (27,7 % inchangé ; −3 pour 999, −2 pour E3) |
| E5 | **[données]** Les effectifs s'expliquent ensemble : 336 doublons = 334 (principal, 150 147 → 149 813) + 2 (rares, 6 024 → 6 022) | Incohérence relevée par l'évaluateur (149 811 attendu s'il n'y avait qu'un fichier) | — |
| E6 | **[analyse]** Le journal du fichier rares de la S3 écrit « toujours combiner P et R » : règle abandonnée, les deux fichiers ne sont jamais empilés | Erreur sanctionnée n° 11 (et non n° 15) | — |
