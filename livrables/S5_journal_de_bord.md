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
