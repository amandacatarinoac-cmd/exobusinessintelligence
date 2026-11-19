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
| E7 | **[analyse]** Indice d'anomalie (KPI 6) : la strate CPV × contrat devient un résidu de régression du log10 du montant sur secteur × contrat, pays, année, classe de lots et procédure (z robuste) | Retour du rendu 4, priorité 2 : l'ancien indice repérait surtout les plus gros contrats | z > 3 : 489 attributions (36,4 % du montant) → 566 (28,8 %) ; R² = 0,39 |
| E8 | **[analyse]** Une seule liste d'audit : les N attributions au z le plus élevé, N réglable (100, 500, 1 000, 5 %) ; z > 3 devient un simple signal | La story 8 mélangeait 489 marchés et l'audit de 5 % (7 460) | N = 500 : 27,6 % du montant pondéré couvert |
| E9 | **[analyse]** Axe A : NOC et AWP signalées et exclues du classement (pas de mise en concurrence publiée) ; segments sous 100 marchés jamais en tête | Consigne, vue segmentation | — |
| E10 | **[analyse]** Axe B : enjeu = montant pondéré des marchés non allotis 2016-2017 ; taux de renseignement affiché par segment | Consigne, vue segmentation | 4 pays sous 40 % (ES, IT, AT, NO), dont 3 renseignés à moins de 50 % |
| E11 | **[analyse]** Test du dernier centile intégré à l'axe C (demandé avant la story 12) | Retour du rendu 4 | Royaume-Uni : 42,3 % du montant pondéré, 11,0 % sans le dernier centile |
| E12 | **[outil]** Vue 4 : tableau paginé (25 lignes) au lieu d'une liste continue | Fluidité sur 149 811 lignes | — |
