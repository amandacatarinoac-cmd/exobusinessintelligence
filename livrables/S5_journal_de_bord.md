# Journal de bord · séance 5

## 19 novembre 2026 (soir)

- Lecture des sources : README, prototype HTML, rendu 4, consigne S5, évaluation du rendu 4, user stories.
- Diagnostic du prototype : seules les 6 022 lignes des procédures rares sont embarquées et recalculées ; tout le fichier principal est écrit en dur (KPI, segments, relations, liste d'audit). Les filtres ne changent aucun chiffre.
- Décisions validées : application HTML publiée sur GitHub Pages ; 999 traité comme 940 ; ID_AW 164662498 gardé sur une seule ligne ; une seule liste d'audit avec capacité N réglable ; NOC exclue du KPI 1 par précaution, statut « définitionnel » retiré ; réécriture des stories 1, 7, 10 et 12.
- Données récupérées depuis le Drive ; script `scripts/prepare_data.py` (deux JSON séparés, jamais empilés).
- Script de référence `scripts/reference.py` : valeurs de contrôle retrouvées sans filtre (27,7 % ; 53,7 % ; médiane 45 780 € ; 3 213 Md€). Écarts consignés au registre (E3, E4).
- Version v0 en ligne (couche de mesures) : contrôle filtré FR × 2016 identique au calcul de référence (KPI 1 : 317 / 2 587 = 12,3 % ; KPI 3 : 2 740 / 6 045 = 45,3 %).
- GitHub Pages activé. Test de l'URL publique dans un navigateur vierge (sans cookies ni session) : chargement en 1,1 s, aucune erreur, valeurs identiques au calcul de référence sans filtre, en FR × 2016 et sous le seuil (MT × 2016 × travaux). Pages publie la racine de la branche : l'application est sous `/docs/` tant que le dossier source n'est pas réglé sur `/docs`.
- Vue 3 construite sur les trois axes, recalculée à partir des lignes, avec descente vers la vue 4 (première version) et retour. Contrôles contre `reference.py vue3` : axe A, 21 segments en alerte, PL × 33 à 48,5 % (12 917 / 26 643, 17,47 Md€ en jeu), capacité 20 → 36,09 Md€ couverts (21,4 % de la dépense à offre unique) ; axe B, NO, ES, IT, AT sous 40 % ; axe C, 566 z > 3, liste de 500 = 27,6 % du montant, Royaume-Uni 83 / 500. Trois filtres croisés (FR × 2016 × services) : affichage correct sous le seuil. Largeur mobile 390 px sans défilement horizontal.
- Constats nouveaux : la part du Royaume-Uni dans le montant pondéré tombe de 42,3 % à 11,0 % sans le dernier centile ; la Lettonie pèse 18,2 % de la liste d'audit pour 2,6 % des attributions.
- Vue 1 : six KPI recalculés (deux par axe), effectif visible sans clic, périmètre écrit (fenêtre 2016-2017 pour KPI 3 et 4), liens vers la vue 3 et la vue 2. KPI 4 estimé par pays (France, Allemagne, Royaume-Uni estimables) avec intervalle. Contrôles contre `reference.py` : KPI 5 queue 69,4 % (sans filtre), 53,4 % (FR × 2016), 12,0 % (UK) ; KPI 6 566 / 149 811 et 28,8 %, 12 en FR × 2016, 86 au UK. Cas sous le seuil (MT × 2016 × travaux) et non estimable (ES) vérifiés. Chargement des six cartes en moins d'une seconde.

## 20 novembre 2026

- Vue 2 : quatre relations (R1 et R2 axe A, R3 axe B, R4 axe C), stratification au choix (pays, contrat, procédure, classe de valeur), règle de la S3 reprise (strate publiée si chaque groupe ≥ 30). Lecture automatique sans formulation causale ; repère le changement de sens entre strates. Contrôles contre la note de la S3 : R1 0,62 [0,57 ; 0,66] et 0,60 ajusté sur le pays ; R2 1,46 et +7,3 points ; R3 1,30 [1,13 ; 1,49], 1,15 [0,99 ; 1,33] ajusté sur la valeur. Bug corrigé : sens des strates mal libellé quand l'association brute est inférieure à 1.
