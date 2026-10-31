# Rapport detaille des resultats DPMM - 23 postes, ENNVM 2007 et ENCDM 2014

Ce rapport analyse les sorties du Dirichlet Process Mixture Model tronque applique aux matrices de parts budgetaires en 23 postes. La troncature fixe K_MAX=7 ne doit pas etre lue comme un K impose de maniere naive : le nombre effectif est juge a partir des poids posteriori, des tailles affectees, des composantes quasi vides, de la qualite d'affectation et de la coherence economique des profils.

## Rappel methodologique

Le modele estime des composantes Dirichlet avec une priorisation de type processus de Dirichlet tronque. Les quatre priors testes sur alpha_DP sont gamma_1_1, gamma_1_2, gamma_0p5_2 et gamma_0p25_2. Les labels sont stabilises par une contrainte d'ordre sur S1, ce qui rend la comparaison des composantes interpretable apres estimation. Les menages sont ensuite affectes au cluster de probabilite posteriori maximale sur l'echantillon complet.

## Libelles des 23 postes

| Poste | Libelle | Codes source |
| --- | --- | --- |
| S1 | S1 alimentaire 01 | DAM_G01 |
| S2 | S2 alimentaire 02/04/05 | DAM_G02, DAM_G04, DAM_G05 |
| S3 | S3 alimentaire 06/07/08 | DAM_G06, DAM_G07, DAM_G08 |
| S4 | S4 alimentaire 09/10 | DAM_G09, DAM_G10 |
| S5 | S5 alimentaire 13/14 | DAM_G13, DAM_G14 |
| S6 | S6 alimentaire mixte | DAM_G03, DAM_G11, DAM_G12, DAM_G15, DAM_G17, DAM_G18 |
| S7 | S7 habillement-chaussures | DAM_G21 a DAM_G28 |
| S8 | S8 logement poste 31 | DAM_G31 |
| S9 | S9 logement/energie 32/34 | DAM_G32, DAM_G34 |
| S10 | S10 ameublement-equipement | DAM_G41 a DAM_G47 |
| S11 | S11 logement poste 33 | DAM_G33 |
| S12 | S12 sante 51 | DAM_G51 |
| S13 | S13 sante 52/53 | DAM_G52, DAM_G53 |
| S14 | S14 transport 61 | DAM_G61 |
| S15 | S15 transport 62 | DAM_G62 |
| S16 | S16 transport/communication 63 | DAM_G63 |
| S17 | S17 loisirs/culture 71/74 | DAM_G71 a DAM_G74 |
| S18 | S18 culture/enseignement 75/76/77 | DAM_G75, DAM_G76; + DAM_G77 dans ENCDM |
| S19 | S19 autres 81/84 | DAM_G81 a DAM_G84 |
| S20 | S20 autres 87/88 | DAM_G87, DAM_G88 |
| S21 | S21 autres 85/86 | DAM_G85, DAM_G86 |
| S22 | S22 autres 89 | DAM_G89 |
| S23 | S23 autres 91/94 | DAM_G91 a DAM_G94 |

## Conclusion generale

Pour les deux bases, le DPMM 23 postes est plus stable que ce que l'on pouvait craindre avec une troncature a 7 composantes : aucune solution principale ne contient de cluster vide ou quasi vide. En 2007, certains priors suggerent une composante rare autour de 2%, mais elle reste exploitable et economiquement lisible. En 2014, les sept groupes sont clairement substantiels, avec un minimum superieur a 3,7% selon les priors. La conclusion operationnelle est donc plus nette que pour 9 postes : le DPMM 23 postes soutient une segmentation effective a 7 profils, tout en gardant l'idee qu'une presentation synthetique peut regrouper certains profils voisins en 6 familles comportementales.

## ENNVM 2007 - resultats DPMM 23 postes

### Structure moyenne de reference

| Famille | Part moyenne |
| --- | --- |
| Alimentaire | 46.5% |
| Logement-energie | 22.7% |
| Transport-communication | 7.3% |
| Autres depenses | 6.9% |
| Sante | 6.9% |
| Culture-enseignement | 3.3% |
| Ameublement-equipement | 3.3% |
| Habillement | 3.0% |

| Poste | Libelle | Codes source | Part moyenne |
| --- | --- | --- | --- |
| S1 | S1 alimentaire 01 | DAM_G01 | 9.3% |
| S2 | S2 alimentaire 02/04/05 | DAM_G02, DAM_G04, DAM_G05 | 15.8% |
| S3 | S3 alimentaire 06/07/08 | DAM_G06, DAM_G07, DAM_G08 | 8.9% |
| S4 | S4 alimentaire 09/10 | DAM_G09, DAM_G10 | 2.3% |
| S5 | S5 alimentaire 13/14 | DAM_G13, DAM_G14 | 0.2% |
| S6 | S6 alimentaire mixte | DAM_G03, DAM_G11, DAM_G12, DAM_G15, DAM_G17, DAM_G18 | 10.1% |
| S7 | S7 habillement-chaussures | DAM_G21 a DAM_G28 | 3.0% |
| S8 | S8 logement poste 31 | DAM_G31 | 10.9% |
| S9 | S9 logement/energie 32/34 | DAM_G32, DAM_G34 | 2.4% |
| S10 | S10 ameublement-equipement | DAM_G41 a DAM_G47 | 3.3% |
| S11 | S11 logement poste 33 | DAM_G33 | 9.4% |
| S12 | S12 sante 51 | DAM_G51 | 2.4% |
| S13 | S13 sante 52/53 | DAM_G52, DAM_G53 | 4.5% |
| S14 | S14 transport 61 | DAM_G61 | 3.1% |
| S15 | S15 transport 62 | DAM_G62 | 1.9% |
| S16 | S16 transport/communication 63 | DAM_G63 | 2.3% |
| S17 | S17 loisirs/culture 71/74 | DAM_G71 a DAM_G74 | 1.3% |
| S18 | S18 culture/enseignement 75/76/77 | DAM_G75, DAM_G76; + DAM_G77 dans ENCDM | 2.1% |
| S19 | S19 autres 81/84 | DAM_G81 a DAM_G84 | 0.1% |
| S20 | S20 autres 87/88 | DAM_G87, DAM_G88 | 1.2% |
| S21 | S21 autres 85/86 | DAM_G85, DAM_G86 | 1.2% |
| S22 | S22 autres 89 | DAM_G89 | 2.3% |
| S23 | S23 autres 91/94 | DAM_G91 a DAM_G94 | 2.1% |

### Comparaison des priors et nombre effectif de clusters

| Prior | K_MAX | alpha_DP moy. | K eff >1% | K eff >2% | K eff >3% | Plus petit cluster | n min | Prob. max moy. | Ambigus | Divergences | ESS min |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 7 | 1.856 | 7 | 7 | 6 | 2.2% | 155 | 0.846 | 11.1% | 0 | 288.4 |
| gamma_1_2 | 7 | 1.369 | 7 | 7 | 6 | 2.3% | 160 | 0.851 | 11.5% | 0 | 252.1 |
| gamma_0p5_2 | 7 | 1.171 | 7 | 6 | 6 | 1.8% | 128 | 0.864 | 9.5% | 0 | 241.0 |
| gamma_0p25_2 | 7 | 1.287 | 7 | 7 | 7 | 2.7% | 194 | 0.855 | 10.7% | 0 | 184.2 |

Lecture : les quatre priors gardent les 7 composantes au seuil de 1%, mais la lecture a 23 postes montre que les groupes ne sont pas artificiellement vides. Le prior gamma_0p25_2 est retenu comme lecture principale car il combine des tailles non minuscules, un K effectif de 7 meme au seuil de 3%, et la meilleure separation socio-economique globale selon eta2_DAM. gamma_0p5_2 donne la classification la plus nette, mais avec un petit cluster plus proche du seuil de rarete.

### Diagnostic socio-economique global par prior

| Prior | Prob. max | Ambigus | Part min | n min | Small <1% | n<100 | eta2 DAM | eta2 log_DAM | Associations dominantes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 0.846 | 11.1% | 2.2% | 155 | 0 | 0 | 0.259 | 0.297 | quintile_DAM=0.295 ; Milieu=0.254 ; Quintiles=0.213 ; Profession_CM=0.167 ; Niveau_scolaire_CM=0.164 |
| gamma_1_2 | 0.851 | 11.5% | 2.3% | 160 | 0 | 0 | 0.254 | 0.291 | quintile_DAM=0.292 ; Milieu=0.241 ; Quintiles=0.213 ; Sexe_CM=0.165 ; Niveau_scolaire_CM=0.163 |
| gamma_0p5_2 | 0.864 | 9.5% | 1.8% | 128 | 0 | 0 | 0.257 | 0.291 | quintile_DAM=0.291 ; Milieu=0.239 ; Quintiles=0.214 ; Sexe_CM=0.162 ; Niveau_scolaire_CM=0.160 |
| gamma_0p25_2 | 0.855 | 10.7% | 2.7% | 194 | 0 | 0 | 0.279 | 0.300 | quintile_DAM=0.299 ; Milieu=0.234 ; Quintiles=0.218 ; Niveau_scolaire_CM=0.169 ; Profession_CM=0.165 |

### Lecture principale des profils : gamma_0p25_2

#### Tailles, poids et concentration

| Cluster | Poids posteriori | Affectes | phi | S1 theorique | >1% |
| --- | --- | --- | --- | --- | --- |
| C1 | 25.8% | 1899 (26.9%) | 24.4 | 10.4% | oui |
| C2 | 4.7% | 310 (4.4%) | 21.7 | 10.3% | oui |
| C3 | 18.2% | 1159 (16.4%) | 11.9 | 10.3% | oui |
| C4 | 31.4% | 2257 (32.0%) | 20.3 | 10.3% | oui |
| C5 | 3.4% | 194 (2.7%) | 5.8 | 8.4% | oui |
| C6 | 9.2% | 689 (9.8%) | 26.4 | 8.4% | oui |
| C7 | 7.3% | 554 (7.8%) | 23.5 | 5.4% | oui |

#### Lecture par grandes familles budgetaires

| Cluster | Taille | Lecture comportementale | Familles dominantes |
| --- | --- | --- | --- |
| C1 | 1899 (26.9%) | Alimentaire S2 dominant | Alimentaire 46.1%, Logement-energie 20.8%, Sante 9.6%, Transport-communication 5.8% |
| C2 | 310 (4.4%) | Transport-communication tres eleve | Alimentaire 37.8%, Transport-communication 22.6%, Logement-energie 18.5%, Autres depenses 9.6% |
| C3 | 1159 (16.4%) | Profil intermediaire | Alimentaire 42.8%, Logement-energie 29.7%, Sante 8.3%, Autres depenses 8.0% |
| C4 | 2257 (32.0%) | Alimentaire contraint | Alimentaire 55.5%, Logement-energie 23.3%, Autres depenses 4.4%, Sante 4.3% |
| C5 | 194 (2.7%) | Logement-energie eleve | Alimentaire 33.3%, Logement-energie 32.9%, Autres depenses 9.0%, Sante 8.2% |
| C6 | 689 (9.8%) | Autres depenses elevees | Alimentaire 45.5%, Logement-energie 18.6%, Autres depenses 12.3%, Transport-communication 6.9% |
| C7 | 554 (7.8%) | Transport-communication tres eleve | Alimentaire 30.0%, Transport-communication 23.1%, Logement-energie 16.8%, Autres depenses 10.6% |

#### Signatures fines S1-S23

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1899 (26.9%) | Alimentaire S2 dominant | S2 16.3%, S8 10.5%, S6 9.5%, S3 9.2%, S1 8.9% | S13 +2.3 pp, S7 +1.4 pp, S10 +0.7 pp, S16 +0.6 pp | S14 -2.3 pp, S11 -1.2 pp, S22 -1.2 pp |
| C2 | 310 (4.4%) | Transport-communication tres eleve | S14 18.8%, S2 14.7%, S8 9.9%, S6 7.5%, S3 7.2% | S14 +15.7 pp, S20 +3.0 pp, S16 +0.8 pp, S23 +0.6 pp | S13 -2.8 pp, S1 -2.8 pp, S11 -2.7 pp |
| C3 | 1159 (16.4%) | Profil intermediaire | S2 15.4%, S8 14.7%, S11 11.3%, S1 9.4%, S6 8.7% | S8 +3.7 pp, S13 +2.1 pp, S11 +1.9 pp, S9 +1.3 pp | S14 -2.2 pp, S7 -1.5 pp, S3 -1.5 pp |
| C4 | 2257 (32.0%) | Alimentaire contraint | S2 17.2%, S6 12.5%, S1 11.6%, S11 11.0%, S3 10.9% | S6 +2.4 pp, S1 +2.3 pp, S3 +2.0 pp, S11 +1.6 pp | S13 -2.5 pp, S14 -2.3 pp, S16 -0.8 pp |
| C5 | 194 (2.7%) | Logement-energie eleve | S8 15.5%, S11 13.0%, S2 12.5%, S6 7.4%, S13 6.6% | S8 +4.5 pp, S11 +3.6 pp, S13 +2.1 pp, S9 +2.0 pp | S3 -3.6 pp, S1 -3.3 pp, S2 -3.2 pp |
| C6 | 689 (9.8%) | Autres depenses elevees | S2 14.3%, S6 11.1%, S1 9.0%, S8 8.8%, S22 8.6% | S22 +6.3 pp, S15 +2.1 pp, S7 +1.1 pp, S6 +1.1 pp | S14 -2.2 pp, S8 -2.1 pp, S11 -1.6 pp |
| C7 | 554 (7.8%) | Transport-communication tres eleve | S14 18.8%, S2 12.3%, S8 9.0%, S6 6.2%, S3 5.8% | S14 +15.7 pp, S20 +2.6 pp, S23 +1.4 pp, S18 +1.0 pp | S1 -4.8 pp, S11 -4.2 pp, S6 -3.9 pp |

#### Tableau numerique des postes structurants

| Cluster | Taille | S1 | S2 | S3 | S6 | S7 | S8 | S9 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1899 (26.9%) | 8.9 | 16.3 | 9.2 | 9.5 | 4.4 | 10.5 | 2.1 | 8.2 | 2.8 | 6.8 | 0.7 | 2.2 | 2.8 | 1.5 | 2.3 |
| C2 | 310 (4.4%) | 6.6 | 14.7 | 7.2 | 7.5 | 1.4 | 9.9 | 2.0 | 6.7 | 2.3 | 1.7 | 18.8 | 0.7 | 3.0 | 1.2 | 2.1 |
| C3 | 1159 (16.4%) | 9.4 | 15.4 | 7.5 | 8.7 | 1.5 | 14.7 | 3.7 | 11.3 | 1.7 | 6.6 | 0.8 | 1.7 | 2.3 | 1.0 | 1.9 |
| C4 | 2257 (32.0%) | 11.6 | 17.2 | 10.9 | 12.5 | 2.4 | 10.3 | 1.9 | 11.0 | 2.4 | 2.0 | 0.8 | 1.6 | 1.5 | 0.9 | 1.8 |
| C5 | 194 (2.7%) | 6.0 | 12.5 | 5.3 | 7.4 | 1.9 | 15.5 | 4.4 | 13.0 | 1.6 | 6.6 | 3.9 | 1.6 | 2.7 | 1.8 | 2.8 |
| C6 | 689 (9.8%) | 9.0 | 14.3 | 8.6 | 11.1 | 4.2 | 8.8 | 2.1 | 7.8 | 2.9 | 3.0 | 0.8 | 4.0 | 2.0 | 1.4 | 1.6 |
| C7 | 554 (7.8%) | 4.5 | 12.3 | 5.8 | 6.2 | 3.8 | 9.0 | 2.6 | 5.2 | 2.1 | 5.1 | 18.8 | 1.2 | 3.1 | 2.1 | 3.1 |

#### Caracterisation socio-economique

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1899 | 58267 | 51360 | +2.4% | 71.6% | 28.4% | Q4 (30.6%) |
| C2 | 310 | 93006 | 74492 | +63.5% | 66.8% | 33.2% | Q5 (49.7%) |
| C3 | 1159 | 43778 | 33818 | -23.0% | 63.6% | 36.4% | Q1 (34.9%) |
| C4 | 2257 | 36847 | 32852 | -35.2% | 46.3% | 53.7% | Q1 (30.8%) |
| C5 | 194 | 56029 | 25619 | -1.5% | 60.3% | 39.7% | Q1 (50.0%) |
| C6 | 689 | 53541 | 45882 | -5.9% | 53.0% | 47.0% | Q3 (27.7%) |
| C7 | 554 | 145484 | 111086 | +155.7% | 78.3% | 21.7% | Q5 (76.4%) |

### Sensibilite des profils aux priors

#### gamma_1_1

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1983 (28.1%) | Alimentaire S2 dominant | S2 16.2%, S8 10.7%, S6 9.6%, S3 9.0%, S1 8.8% | S13 +2.4 pp, S7 +1.3 pp, S15 +0.6 pp, S10 +0.6 pp | S14 -2.4 pp, S9 -1.4 pp, S11 -1.3 pp |
| C2 | 543 (7.7%) | Transport-communication tres eleve | S14 22.0%, S2 13.3%, S8 9.2%, S6 7.0%, S3 6.3% | S14 +18.9 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.6 pp | S1 -4.0 pp, S11 -3.4 pp, S6 -3.0 pp |
| C3 | 336 (4.8%) | Transport-communication tres eleve | S14 14.2%, S2 12.7%, S8 9.3%, S6 6.5%, S3 6.1% | S14 +11.1 pp, S20 +2.5 pp, S18 +2.4 pp, S17 +1.4 pp | S1 -4.1 pp, S11 -4.1 pp, S6 -3.5 pp |
| C4 | 2141 (30.3%) | Alimentaire contraint | S2 17.4%, S6 12.3%, S1 11.5%, S11 11.0%, S3 10.9% | S6 +2.3 pp, S1 +2.2 pp, S3 +2.0 pp, S2 +1.7 pp | S13 -2.5 pp, S14 -2.4 pp, S9 -1.5 pp |
| C5 | 728 (10.3%) | Profil intermediaire | S2 14.2%, S9 10.7%, S6 10.5%, S1 9.6%, S3 9.0% | S9 +8.3 pp, S7 +1.3 pp, S10 +0.6 pp, S6 +0.4 pp | S8 -3.9 pp, S13 -2.0 pp, S14 -1.8 pp |
| C6 | 155 (2.2%) | Logement-energie eleve | S8 16.1%, S11 14.1%, S2 12.6%, S6 7.4%, S1 7.1% | S8 +5.2 pp, S11 +4.7 pp, S9 +2.2 pp, S13 +1.5 pp | S3 -4.1 pp, S2 -3.2 pp, S6 -2.7 pp |
| C7 | 1176 (16.7%) | Profil intermediaire | S2 15.4%, S8 14.5%, S11 11.5%, S1 9.4%, S6 9.1% | S8 +3.5 pp, S13 +2.2 pp, S11 +2.1 pp, S21 +0.6 pp | S14 -2.5 pp, S7 -1.4 pp, S3 -1.3 pp |

#### gamma_1_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1593 (22.6%) | Alimentaire S2 dominant | S2 16.4%, S8 10.9%, S6 9.3%, S3 9.1%, S1 8.8% | S13 +3.1 pp, S7 +1.4 pp, S10 +0.7 pp, S16 +0.7 pp | S14 -2.3 pp, S22 -1.5 pp, S9 -1.3 pp |
| C2 | 835 (11.8%) | Transport-communication tres eleve | S14 19.2%, S2 13.0%, S8 9.2%, S6 6.7%, S3 6.2% | S14 +16.1 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.1 pp, S11 -3.8 pp, S6 -3.3 pp |
| C3 | 1168 (16.5%) | Profil intermediaire | S2 15.2%, S8 14.4%, S11 11.3%, S1 9.2%, S6 8.7% | S8 +3.4 pp, S13 +2.3 pp, S11 +1.9 pp, S9 +0.8 pp | S14 -2.1 pp, S3 -1.5 pp, S7 -1.5 pp |
| C4 | 1862 (26.4%) | Alimentaire contraint | S2 17.8%, S6 12.5%, S1 11.9%, S11 11.3%, S3 11.1% | S1 +2.6 pp, S6 +2.4 pp, S3 +2.2 pp, S2 +2.0 pp | S13 -2.4 pp, S14 -2.3 pp, S22 -1.4 pp |
| C5 | 160 (2.3%) | Logement-energie eleve | S8 16.3%, S11 14.1%, S2 12.4%, S6 7.4%, S1 6.9% | S8 +5.4 pp, S11 +4.7 pp, S9 +2.1 pp, S13 +1.5 pp | S3 -4.0 pp, S2 -3.3 pp, S6 -2.6 pp |
| C6 | 864 (12.2%) | Autres depenses elevees | S2 15.0%, S6 11.5%, S8 9.8%, S1 9.5%, S22 9.5% | S22 +7.2 pp, S6 +1.4 pp, S7 +0.9 pp, S12 +0.5 pp | S13 -2.3 pp, S14 -2.2 pp, S9 -1.3 pp |
| C7 | 580 (8.2%) | Profil intermediaire | S2 14.5%, S6 10.4%, S9 9.2%, S1 9.0%, S3 8.8% | S9 +6.8 pp, S15 +2.0 pp, S7 +1.3 pp, S10 +1.0 pp | S8 -3.7 pp, S14 -2.1 pp, S11 -1.7 pp |

#### gamma_0p5_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 2070 (29.3%) | Alimentaire S2 dominant | S2 16.1%, S8 10.5%, S6 9.6%, S3 9.0%, S1 8.8% | S13 +2.2 pp, S7 +1.4 pp, S10 +0.7 pp, S16 +0.5 pp | S14 -2.3 pp, S11 -1.3 pp, S22 -0.6 pp |
| C2 | 747 (10.6%) | Transport-communication tres eleve | S14 20.0%, S2 12.9%, S8 9.3%, S6 6.4%, S3 6.0% | S14 +16.9 pp, S20 +2.9 pp, S23 +1.3 pp, S16 +0.8 pp | S1 -4.2 pp, S11 -3.8 pp, S6 -3.6 pp |
| C3 | 2404 (34.0%) | Alimentaire contraint | S2 17.1%, S6 12.3%, S1 11.4%, S11 10.9%, S3 10.8% | S6 +2.3 pp, S1 +2.1 pp, S3 +1.9 pp, S11 +1.5 pp | S13 -2.6 pp, S14 -2.3 pp, S16 -0.7 pp |
| C4 | 1194 (16.9%) | Profil intermediaire | S2 15.5%, S8 14.6%, S11 11.4%, S1 9.5%, S6 8.9% | S8 +3.6 pp, S11 +2.0 pp, S13 +1.9 pp, S9 +0.9 pp | S14 -2.2 pp, S7 -1.5 pp, S10 -1.4 pp |
| C5 | 186 (2.6%) | Logement-energie eleve | S8 15.8%, S11 13.3%, S2 12.8%, S6 7.6%, S13 6.7% | S8 +4.9 pp, S11 +3.9 pp, S13 +2.2 pp, S9 +2.1 pp | S3 -3.6 pp, S1 -3.0 pp, S2 -2.9 pp |
| C6 | 128 (1.8%) | Transport-communication tres eleve | S2 13.5%, S14 10.5%, S8 8.9%, S6 8.6%, S3 7.4% | S14 +7.5 pp, S22 +3.1 pp, S20 +1.6 pp, S18 +0.8 pp | S11 -3.4 pp, S1 -2.4 pp, S2 -2.3 pp |
| C7 | 333 (4.7%) | Autres depenses elevees | S2 14.0%, S6 10.9%, S1 8.7%, S3 8.6%, S22 7.9% | S22 +5.6 pp, S9 +3.5 pp, S15 +1.9 pp, S7 +1.0 pp | S8 -3.7 pp, S14 -2.1 pp, S11 -2.0 pp |

#### gamma_0p25_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1899 (26.9%) | Alimentaire S2 dominant | S2 16.3%, S8 10.5%, S6 9.5%, S3 9.2%, S1 8.9% | S13 +2.3 pp, S7 +1.4 pp, S10 +0.7 pp, S16 +0.6 pp | S14 -2.3 pp, S11 -1.2 pp, S22 -1.2 pp |
| C2 | 310 (4.4%) | Transport-communication tres eleve | S14 18.8%, S2 14.7%, S8 9.9%, S6 7.5%, S3 7.2% | S14 +15.7 pp, S20 +3.0 pp, S16 +0.8 pp, S23 +0.6 pp | S13 -2.8 pp, S1 -2.8 pp, S11 -2.7 pp |
| C3 | 1159 (16.4%) | Profil intermediaire | S2 15.4%, S8 14.7%, S11 11.3%, S1 9.4%, S6 8.7% | S8 +3.7 pp, S13 +2.1 pp, S11 +1.9 pp, S9 +1.3 pp | S14 -2.2 pp, S7 -1.5 pp, S3 -1.5 pp |
| C4 | 2257 (32.0%) | Alimentaire contraint | S2 17.2%, S6 12.5%, S1 11.6%, S11 11.0%, S3 10.9% | S6 +2.4 pp, S1 +2.3 pp, S3 +2.0 pp, S11 +1.6 pp | S13 -2.5 pp, S14 -2.3 pp, S16 -0.8 pp |
| C5 | 194 (2.7%) | Logement-energie eleve | S8 15.5%, S11 13.0%, S2 12.5%, S6 7.4%, S13 6.6% | S8 +4.5 pp, S11 +3.6 pp, S13 +2.1 pp, S9 +2.0 pp | S3 -3.6 pp, S1 -3.3 pp, S2 -3.2 pp |
| C6 | 689 (9.8%) | Autres depenses elevees | S2 14.3%, S6 11.1%, S1 9.0%, S8 8.8%, S22 8.6% | S22 +6.3 pp, S15 +2.1 pp, S7 +1.1 pp, S6 +1.1 pp | S14 -2.2 pp, S8 -2.1 pp, S11 -1.6 pp |
| C7 | 554 (7.8%) | Transport-communication tres eleve | S14 18.8%, S2 12.3%, S8 9.0%, S6 6.2%, S3 5.8% | S14 +15.7 pp, S20 +2.6 pp, S23 +1.4 pp, S18 +1.0 pp | S1 -4.8 pp, S11 -4.2 pp, S6 -3.9 pp |

### Annexe numerique : profils complets S1-S23 par prior

#### Profils numeriques complets - gamma_1_1

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1983 (28.1%) | 8.8 | 16.2 | 9.0 | 2.0 | 0.3 | 9.6 | 4.3 | 10.7 | 1.0 | 3.9 | 8.1 | 2.9 | 6.9 | 0.7 | 2.6 | 2.8 | 1.4 | 2.2 | 0.1 | 0.8 | 1.2 | 2.3 | 2.1 |
| C2 | 543 (7.7%) | 5.3 | 13.3 | 6.3 | 1.3 | 0.3 | 7.0 | 2.1 | 9.2 | 2.3 | 2.7 | 6.0 | 2.0 | 3.1 | 22.0 | 0.9 | 2.9 | 1.3 | 1.8 | 0.1 | 3.9 | 1.5 | 1.5 | 3.2 |
| C3 | 336 (4.8%) | 5.2 | 12.7 | 6.1 | 1.1 | 0.4 | 6.5 | 4.3 | 9.3 | 1.7 | 3.8 | 5.2 | 2.5 | 4.9 | 14.2 | 1.3 | 3.3 | 2.6 | 4.5 | 0.3 | 3.7 | 1.8 | 1.4 | 3.2 |
| C4 | 2141 (30.3%) | 11.5 | 17.4 | 10.9 | 3.1 | 0.2 | 12.3 | 2.3 | 10.9 | 0.9 | 3.4 | 11.0 | 2.5 | 1.9 | 0.7 | 1.7 | 1.6 | 0.9 | 1.8 | 0.1 | 0.5 | 0.8 | 2.4 | 1.3 |
| C5 | 728 (10.3%) | 9.6 | 14.2 | 9.0 | 2.7 | 0.2 | 10.5 | 4.3 | 7.0 | 10.7 | 3.9 | 8.2 | 2.1 | 2.5 | 1.3 | 2.4 | 2.0 | 1.4 | 1.7 | 0.2 | 0.6 | 1.3 | 2.4 | 1.9 |
| C6 | 155 (2.2%) | 7.1 | 12.6 | 4.8 | 1.5 | 0.3 | 7.4 | 1.9 | 16.1 | 4.6 | 1.8 | 14.1 | 1.6 | 5.9 | 3.0 | 1.3 | 2.4 | 1.8 | 2.9 | 0.0 | 2.4 | 1.5 | 1.7 | 3.3 |
| C7 | 1176 (16.7%) | 9.4 | 15.4 | 7.6 | 1.8 | 0.2 | 9.1 | 1.6 | 14.5 | 2.4 | 2.0 | 11.5 | 1.7 | 6.7 | 0.6 | 1.9 | 2.3 | 1.1 | 1.9 | 0.1 | 1.1 | 1.8 | 2.8 | 2.5 |

#### Profils numeriques complets - gamma_1_2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1593 (22.6%) | 8.8 | 16.4 | 9.1 | 1.9 | 0.3 | 9.3 | 4.4 | 10.9 | 1.1 | 4.0 | 8.2 | 2.9 | 7.6 | 0.8 | 2.3 | 2.9 | 1.4 | 2.5 | 0.1 | 0.9 | 1.2 | 0.9 | 2.1 |
| C2 | 835 (11.8%) | 5.2 | 13.0 | 6.2 | 1.2 | 0.3 | 6.7 | 2.9 | 9.2 | 2.3 | 3.2 | 5.6 | 2.1 | 3.7 | 19.2 | 1.1 | 3.1 | 1.8 | 2.8 | 0.2 | 4.0 | 1.7 | 1.3 | 3.3 |
| C3 | 1168 (16.5%) | 9.2 | 15.2 | 7.4 | 1.7 | 0.2 | 8.7 | 1.6 | 14.4 | 3.2 | 2.0 | 11.3 | 1.7 | 6.8 | 1.0 | 1.8 | 2.4 | 1.2 | 2.0 | 0.1 | 1.2 | 1.9 | 2.4 | 2.6 |
| C4 | 1862 (26.4%) | 11.9 | 17.8 | 11.1 | 3.2 | 0.2 | 12.5 | 2.1 | 10.8 | 1.4 | 3.4 | 11.3 | 2.3 | 2.1 | 0.7 | 1.5 | 1.5 | 0.9 | 1.8 | 0.0 | 0.5 | 0.8 | 0.9 | 1.3 |
| C5 | 160 (2.3%) | 6.9 | 12.4 | 4.9 | 1.5 | 0.3 | 7.4 | 1.8 | 16.3 | 4.6 | 1.8 | 14.1 | 1.5 | 6.0 | 3.7 | 1.3 | 2.3 | 1.5 | 2.8 | 0.0 | 2.4 | 1.4 | 1.7 | 3.1 |
| C6 | 864 (12.2%) | 9.5 | 15.0 | 9.3 | 2.5 | 0.2 | 11.5 | 4.0 | 9.8 | 1.1 | 3.3 | 8.7 | 2.9 | 2.2 | 0.9 | 2.1 | 1.7 | 1.1 | 1.5 | 0.1 | 0.5 | 1.0 | 9.5 | 1.5 |
| C7 | 580 (8.2%) | 9.0 | 14.5 | 8.8 | 2.5 | 0.2 | 10.4 | 4.4 | 7.2 | 9.2 | 4.3 | 7.7 | 2.3 | 3.2 | 1.0 | 4.0 | 2.3 | 1.6 | 1.7 | 0.2 | 0.6 | 1.2 | 1.4 | 2.2 |

#### Profils numeriques complets - gamma_0p5_2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2070 (29.3%) | 8.8 | 16.1 | 9.0 | 2.0 | 0.3 | 9.6 | 4.4 | 10.5 | 1.9 | 4.0 | 8.1 | 2.8 | 6.7 | 0.8 | 2.4 | 2.8 | 1.5 | 2.3 | 0.1 | 0.8 | 1.2 | 1.7 | 2.1 |
| C2 | 747 (10.6%) | 5.1 | 12.9 | 6.0 | 1.2 | 0.3 | 6.4 | 2.8 | 9.3 | 2.6 | 3.2 | 5.6 | 2.1 | 3.6 | 20.0 | 1.0 | 3.0 | 1.8 | 2.7 | 0.2 | 4.1 | 1.8 | 1.0 | 3.3 |
| C3 | 2404 (34.0%) | 11.4 | 17.1 | 10.8 | 3.1 | 0.2 | 12.3 | 2.6 | 10.3 | 1.8 | 3.5 | 10.9 | 2.4 | 1.9 | 0.8 | 1.7 | 1.5 | 0.9 | 1.8 | 0.1 | 0.5 | 0.9 | 2.2 | 1.4 |
| C4 | 1194 (16.9%) | 9.5 | 15.5 | 7.6 | 1.8 | 0.2 | 8.9 | 1.5 | 14.6 | 3.3 | 1.9 | 11.4 | 1.6 | 6.4 | 0.9 | 1.7 | 2.3 | 1.1 | 1.9 | 0.1 | 1.1 | 1.7 | 2.6 | 2.4 |
| C5 | 186 (2.6%) | 6.3 | 12.8 | 5.3 | 1.7 | 0.3 | 7.6 | 1.8 | 15.8 | 4.5 | 1.9 | 13.3 | 1.6 | 6.7 | 3.1 | 1.5 | 2.4 | 1.8 | 2.5 | 0.0 | 2.4 | 1.3 | 1.7 | 3.4 |
| C6 | 128 (1.8%) | 7.0 | 13.5 | 7.4 | 1.4 | 0.3 | 8.6 | 3.8 | 8.9 | 1.3 | 3.3 | 6.0 | 2.9 | 4.7 | 10.5 | 1.6 | 2.9 | 1.6 | 2.8 | 0.1 | 2.8 | 1.0 | 5.4 | 2.1 |
| C7 | 333 (4.7%) | 8.7 | 14.0 | 8.6 | 2.4 | 0.2 | 10.9 | 4.0 | 7.3 | 6.0 | 3.8 | 7.3 | 2.5 | 3.3 | 0.9 | 3.8 | 2.1 | 1.3 | 1.5 | 0.2 | 0.5 | 0.9 | 7.9 | 1.8 |

#### Profils numeriques complets - gamma_0p25_2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1899 (26.9%) | 8.9 | 16.3 | 9.2 | 2.0 | 0.3 | 9.5 | 4.4 | 10.5 | 2.1 | 4.0 | 8.2 | 2.8 | 6.8 | 0.7 | 2.2 | 2.8 | 1.5 | 2.3 | 0.1 | 0.8 | 1.3 | 1.2 | 2.1 |
| C2 | 310 (4.4%) | 6.6 | 14.7 | 7.2 | 1.5 | 0.3 | 7.5 | 1.4 | 9.9 | 2.0 | 2.8 | 6.7 | 2.3 | 1.7 | 18.8 | 0.7 | 3.0 | 1.2 | 2.1 | 0.1 | 4.1 | 1.2 | 1.5 | 2.7 |
| C3 | 1159 (16.4%) | 9.4 | 15.4 | 7.5 | 1.7 | 0.2 | 8.7 | 1.5 | 14.7 | 3.7 | 1.9 | 11.3 | 1.7 | 6.6 | 0.8 | 1.7 | 2.3 | 1.0 | 1.9 | 0.1 | 1.1 | 1.8 | 2.5 | 2.4 |
| C4 | 2257 (32.0%) | 11.6 | 17.2 | 10.9 | 3.2 | 0.2 | 12.5 | 2.4 | 10.3 | 1.9 | 3.4 | 11.0 | 2.4 | 2.0 | 0.8 | 1.6 | 1.5 | 0.9 | 1.8 | 0.1 | 0.5 | 0.8 | 1.7 | 1.4 |
| C5 | 194 (2.7%) | 6.0 | 12.5 | 5.3 | 1.7 | 0.3 | 7.4 | 1.9 | 15.5 | 4.4 | 1.9 | 13.0 | 1.6 | 6.6 | 3.9 | 1.6 | 2.7 | 1.8 | 2.8 | 0.0 | 2.3 | 1.5 | 1.5 | 3.6 |
| C6 | 689 (9.8%) | 9.0 | 14.3 | 8.6 | 2.3 | 0.2 | 11.1 | 4.2 | 8.8 | 2.1 | 3.7 | 7.8 | 2.9 | 3.0 | 0.8 | 4.0 | 2.0 | 1.4 | 1.6 | 0.2 | 0.6 | 1.0 | 8.6 | 1.9 |
| C7 | 554 (7.8%) | 4.5 | 12.3 | 5.8 | 1.1 | 0.3 | 6.2 | 3.8 | 9.0 | 2.6 | 3.4 | 5.2 | 2.1 | 5.1 | 18.8 | 1.2 | 3.1 | 2.1 | 3.1 | 0.3 | 3.8 | 1.8 | 1.2 | 3.5 |


## ENCDM 2014 - resultats DPMM 23 postes

### Structure moyenne de reference

| Famille | Part moyenne |
| --- | --- |
| Alimentaire | 42.1% |
| Logement-energie | 25.5% |
| Sante | 8.2% |
| Autres depenses | 7.6% |
| Transport-communication | 6.8% |
| Culture-enseignement | 3.9% |
| Ameublement-equipement | 3.0% |
| Habillement | 2.9% |

| Poste | Libelle | Codes source | Part moyenne |
| --- | --- | --- | --- |
| S1 | S1 alimentaire 01 | DAM_G01 | 7.2% |
| S2 | S2 alimentaire 02/04/05 | DAM_G02, DAM_G04, DAM_G05 | 14.5% |
| S3 | S3 alimentaire 06/07/08 | DAM_G06, DAM_G07, DAM_G08 | 8.0% |
| S4 | S4 alimentaire 09/10 | DAM_G09, DAM_G10 | 1.5% |
| S5 | S5 alimentaire 13/14 | DAM_G13, DAM_G14 | 0.3% |
| S6 | S6 alimentaire mixte | DAM_G03, DAM_G11, DAM_G12, DAM_G15, DAM_G17, DAM_G18 | 10.5% |
| S7 | S7 habillement-chaussures | DAM_G21 a DAM_G28 | 2.9% |
| S8 | S8 logement poste 31 | DAM_G31 | 15.6% |
| S9 | S9 logement/energie 32/34 | DAM_G32, DAM_G34 | 1.8% |
| S10 | S10 ameublement-equipement | DAM_G41 a DAM_G47 | 3.0% |
| S11 | S11 logement poste 33 | DAM_G33 | 8.1% |
| S12 | S12 sante 51 | DAM_G51 | 2.7% |
| S13 | S13 sante 52/53 | DAM_G52, DAM_G53 | 5.6% |
| S14 | S14 transport 61 | DAM_G61 | 2.8% |
| S15 | S15 transport 62 | DAM_G62 | 2.0% |
| S16 | S16 transport/communication 63 | DAM_G63 | 1.9% |
| S17 | S17 loisirs/culture 71/74 | DAM_G71 a DAM_G74 | 1.2% |
| S18 | S18 culture/enseignement 75/76/77 | DAM_G75, DAM_G76; + DAM_G77 dans ENCDM | 2.7% |
| S19 | S19 autres 81/84 | DAM_G81 a DAM_G84 | 0.1% |
| S20 | S20 autres 87/88 | DAM_G87, DAM_G88 | 1.5% |
| S21 | S21 autres 85/86 | DAM_G85, DAM_G86 | 1.7% |
| S22 | S22 autres 89 | DAM_G89 | 1.7% |
| S23 | S23 autres 91/94 | DAM_G91 a DAM_G94 | 2.5% |

### Comparaison des priors et nombre effectif de clusters

| Prior | K_MAX | alpha_DP moy. | K eff >1% | K eff >2% | K eff >3% | Plus petit cluster | n min | Prob. max moy. | Ambigus | Divergences | ESS min |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 7 | 1.581 | 7 | 7 | 7 | 4.1% | 651 | 0.840 | 12.9% | 0 | 233.9 |
| gamma_1_2 | 7 | 1.386 | 7 | 7 | 7 | 3.7% | 593 | 0.855 | 11.3% | 0 | 156.6 |
| gamma_0p5_2 | 7 | 1.304 | 7 | 7 | 7 | 6.5% | 1044 | 0.827 | 14.2% | 0 | 325.6 |
| gamma_0p25_2 | 7 | 1.369 | 7 | 7 | 7 | 6.0% | 959 | 0.838 | 13.5% | 0 | 318.5 |

Lecture : en 2014, les 7 composantes sont toutes substantielles quel que soit le prior. gamma_1_1 est retenu comme lecture principale parce qu'il maximise la discrimination socio-economique et garde des tailles confortables. gamma_1_2 est tres proche et donne meme une probabilite maximale moyenne legerement superieure ; il sert donc de verification de robustesse plutot que de contradiction.

### Diagnostic socio-economique global par prior

| Prior | Prob. max | Ambigus | Part min | n min | Small <1% | n<100 | eta2 DAM | eta2 log_DAM | Associations dominantes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 0.840 | 12.9% | 4.1% | 651 | 0 | 0 | 0.319 | 0.349 | quintile_DAM=0.326 ; Diplôme_agregé_CM=0.254 ; Quintiles=0.238 ; Quintileurbain=0.210 ; Milieu=0.210 |
| gamma_1_2 | 0.855 | 11.3% | 3.7% | 593 | 0 | 0 | 0.309 | 0.328 | quintile_DAM=0.311 ; Diplôme_agregé_CM=0.229 ; Quintiles=0.214 ; Milieu=0.197 ; Quintileurbain=0.190 |
| gamma_0p5_2 | 0.827 | 14.2% | 6.5% | 1044 | 0 | 0 | 0.266 | 0.315 | quintile_DAM=0.309 ; Milieu=0.253 ; Diplôme_agregé_CM=0.222 ; Quintiles=0.213 ; Quintileurbain=0.210 |
| gamma_0p25_2 | 0.838 | 13.5% | 6.0% | 959 | 0 | 0 | 0.264 | 0.304 | quintile_DAM=0.306 ; Milieu=0.221 ; Diplôme_agregé_CM=0.219 ; Quintiles=0.210 ; Quintileurbain=0.196 |

### Lecture principale des profils : gamma_1_1

#### Tailles, poids et concentration

| Cluster | Poids posteriori | Affectes | phi | S1 theorique | >1% |
| --- | --- | --- | --- | --- | --- |
| C1 | 28.6% | 4854 (30.4%) | 23.9 | 9.0% | oui |
| C2 | 23.0% | 3502 (21.9%) | 18.0 | 9.0% | oui |
| C3 | 17.2% | 2629 (16.5%) | 26.0 | 9.0% | oui |
| C4 | 11.8% | 1986 (12.4%) | 20.7 | 6.3% | oui |
| C5 | 4.0% | 651 (4.1%) | 30.0 | 6.2% | oui |
| C6 | 6.0% | 997 (6.2%) | 27.5 | 6.2% | oui |
| C7 | 9.4% | 1351 (8.5%) | 8.8 | 6.2% | oui |

#### Lecture par grandes familles budgetaires

| Cluster | Taille | Lecture comportementale | Familles dominantes |
| --- | --- | --- | --- |
| C1 | 4854 (30.4%) | Profil intermediaire | Alimentaire 43.0%, Logement-energie 24.0%, Sante 12.1%, Autres depenses 6.1% |
| C2 | 3502 (21.9%) | Logement S8 dominant | Alimentaire 49.4%, Logement-energie 30.7%, Sante 5.7%, Autres depenses 5.0% |
| C3 | 2629 (16.5%) | Alimentaire contraint | Alimentaire 50.4%, Logement-energie 23.9%, Autres depenses 5.8%, Transport-communication 4.9% |
| C4 | 1986 (12.4%) | Transport-communication tres eleve | Alimentaire 33.0%, Logement-energie 20.5%, Transport-communication 18.5%, Autres depenses 10.8% |
| C5 | 651 (4.1%) | Transport-communication tres eleve | Alimentaire 29.3%, Logement-energie 17.7%, Autres depenses 14.3%, Transport-communication 13.6% |
| C6 | 997 (6.2%) | Autres depenses elevees | Alimentaire 36.4%, Logement-energie 20.4%, Autres depenses 11.3%, Sante 9.2% |
| C7 | 1351 (8.5%) | Logement-energie eleve | Logement-energie 35.1%, Alimentaire 27.5%, Autres depenses 12.3%, Sante 11.0% |

#### Signatures fines S1-S23

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 4854 (30.4%) | Profil intermediaire | S2 14.8%, S8 14.3%, S6 10.5%, S13 9.2%, S3 8.5% | S13 +3.6 pp, S7 +0.7 pp, S3 +0.4 pp | S14 -2.3 pp, S8 -1.2 pp, S20 -0.8 pp |
| C2 | 3502 (21.9%) | Logement S8 dominant | S8 18.5%, S2 15.9%, S6 12.7%, S11 10.9%, S3 9.3% | S8 +3.0 pp, S11 +2.8 pp, S6 +2.2 pp, S1 +1.9 pp | S14 -2.3 pp, S7 -2.2 pp, S13 -2.0 pp |
| C3 | 2629 (16.5%) | Alimentaire contraint | S2 17.0%, S8 14.5%, S6 12.7%, S3 10.0%, S1 8.5% | S2 +2.4 pp, S6 +2.2 pp, S3 +2.0 pp, S7 +1.4 pp | S13 -5.2 pp, S14 -2.3 pp, S8 -1.1 pp |
| C4 | 1986 (12.4%) | Transport-communication tres eleve | S14 15.1%, S8 13.1%, S2 12.3%, S6 7.9%, S3 6.3% | S14 +12.3 pp, S20 +2.5 pp, S23 +1.1 pp, S16 +0.5 pp | S11 -2.7 pp, S6 -2.6 pp, S8 -2.4 pp |
| C5 | 651 (4.1%) | Transport-communication tres eleve | S8 11.8%, S2 11.4%, S14 9.9%, S18 7.0%, S6 6.8% | S14 +7.1 pp, S18 +4.3 pp, S21 +2.7 pp, S23 +2.4 pp | S11 -4.0 pp, S8 -3.8 pp, S6 -3.7 pp |
| C6 | 997 (6.2%) | Autres depenses elevees | S2 13.9%, S8 13.3%, S6 8.5%, S3 7.0%, S13 5.7% | S17 +2.3 pp, S15 +2.0 pp, S23 +1.8 pp, S20 +1.8 pp | S11 -2.7 pp, S8 -2.2 pp, S14 -2.1 pp |
| C7 | 1351 (8.5%) | Logement-energie eleve | S8 21.6%, S2 10.4%, S13 9.1%, S11 8.9%, S6 7.6% | S8 +6.0 pp, S13 +3.5 pp, S9 +2.8 pp, S23 +2.3 pp | S3 -4.4 pp, S2 -4.1 pp, S6 -2.9 pp |

#### Tableau numerique des postes structurants

| Cluster | Taille | S1 | S2 | S3 | S6 | S7 | S8 | S9 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4854 (30.4%) | 7.4 | 14.8 | 8.5 | 10.5 | 3.7 | 14.3 | 1.7 | 8.0 | 2.9 | 9.2 | 0.6 | 2.3 | 1.9 | 0.9 | 2.3 |
| C2 | 3502 (21.9%) | 9.1 | 15.9 | 9.3 | 12.7 | 0.8 | 18.5 | 1.3 | 10.9 | 2.2 | 3.5 | 0.6 | 1.8 | 1.2 | 0.5 | 1.9 |
| C3 | 2629 (16.5%) | 8.5 | 17.0 | 10.0 | 12.7 | 4.3 | 14.5 | 1.2 | 8.3 | 3.1 | 0.4 | 0.6 | 2.3 | 2.0 | 0.9 | 2.5 |
| C4 | 1986 (12.4%) | 5.0 | 12.3 | 6.3 | 7.9 | 2.7 | 13.1 | 2.0 | 5.4 | 2.4 | 4.9 | 15.1 | 1.0 | 2.4 | 1.4 | 3.0 |
| C5 | 651 (4.1%) | 4.2 | 11.4 | 5.5 | 6.8 | 3.9 | 11.8 | 1.8 | 4.1 | 2.7 | 5.1 | 9.9 | 0.9 | 2.7 | 3.1 | 7.0 |
| C6 | 997 (6.2%) | 5.3 | 13.9 | 7.0 | 8.5 | 4.7 | 13.3 | 1.6 | 5.5 | 3.5 | 5.7 | 0.7 | 4.0 | 2.8 | 3.5 | 3.1 |
| C7 | 1351 (8.5%) | 4.8 | 10.4 | 3.6 | 7.6 | 1.8 | 21.6 | 4.6 | 8.9 | 1.9 | 9.1 | 1.4 | 1.8 | 2.0 | 1.8 | 3.4 |

#### Caracterisation socio-economique

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4854 | 65798 | 59117 | -12.3% | 62.7% | 37.3% | Q3 (26.9%) |
| C2 | 3502 | 43340 | 38884 | -42.3% | 55.3% | 44.7% | Q1 (44.5%) |
| C3 | 2629 | 56085 | 50790 | -25.3% | 57.4% | 42.6% | Q2 (29.7%) |
| C4 | 1986 | 124117 | 103626 | +65.3% | 72.2% | 27.8% | Q5 (53.0%) |
| C5 | 651 | 194565 | 164245 | +159.2% | 87.9% | 12.1% | Q5 (81.3%) |
| C6 | 997 | 103684 | 94416 | +38.1% | 87.7% | 12.3% | Q5 (45.5%) |
| C7 | 1351 | 76757 | 55538 | +2.2% | 74.9% | 25.1% | Q1 (30.4%) |

### Sensibilite des profils aux priors

#### gamma_1_1

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 4854 (30.4%) | Profil intermediaire | S2 14.8%, S8 14.3%, S6 10.5%, S13 9.2%, S3 8.5% | S13 +3.6 pp, S7 +0.7 pp, S3 +0.4 pp | S14 -2.3 pp, S8 -1.2 pp, S20 -0.8 pp |
| C2 | 3502 (21.9%) | Logement S8 dominant | S8 18.5%, S2 15.9%, S6 12.7%, S11 10.9%, S3 9.3% | S8 +3.0 pp, S11 +2.8 pp, S6 +2.2 pp, S1 +1.9 pp | S14 -2.3 pp, S7 -2.2 pp, S13 -2.0 pp |
| C3 | 2629 (16.5%) | Alimentaire contraint | S2 17.0%, S8 14.5%, S6 12.7%, S3 10.0%, S1 8.5% | S2 +2.4 pp, S6 +2.2 pp, S3 +2.0 pp, S7 +1.4 pp | S13 -5.2 pp, S14 -2.3 pp, S8 -1.1 pp |
| C4 | 1986 (12.4%) | Transport-communication tres eleve | S14 15.1%, S8 13.1%, S2 12.3%, S6 7.9%, S3 6.3% | S14 +12.3 pp, S20 +2.5 pp, S23 +1.1 pp, S16 +0.5 pp | S11 -2.7 pp, S6 -2.6 pp, S8 -2.4 pp |
| C5 | 651 (4.1%) | Transport-communication tres eleve | S8 11.8%, S2 11.4%, S14 9.9%, S18 7.0%, S6 6.8% | S14 +7.1 pp, S18 +4.3 pp, S21 +2.7 pp, S23 +2.4 pp | S11 -4.0 pp, S8 -3.8 pp, S6 -3.7 pp |
| C6 | 997 (6.2%) | Autres depenses elevees | S2 13.9%, S8 13.3%, S6 8.5%, S3 7.0%, S13 5.7% | S17 +2.3 pp, S15 +2.0 pp, S23 +1.8 pp, S20 +1.8 pp | S11 -2.7 pp, S8 -2.2 pp, S14 -2.1 pp |
| C7 | 1351 (8.5%) | Logement-energie eleve | S8 21.6%, S2 10.4%, S13 9.1%, S11 8.9%, S6 7.6% | S8 +6.0 pp, S13 +3.5 pp, S9 +2.8 pp, S23 +2.3 pp | S3 -4.4 pp, S2 -4.1 pp, S6 -2.9 pp |

#### gamma_1_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 5123 (32.1%) | Logement S8 dominant | S2 15.2%, S8 15.1%, S6 10.5%, S3 8.6%, S13 8.0% | S13 +2.4 pp, S7 +1.0 pp, S2 +0.7 pp, S3 +0.6 pp | S14 -2.5 pp, S21 -1.0 pp, S20 -0.5 pp |
| C2 | 805 (5.0%) | Transport-communication tres eleve | S14 16.3%, S8 14.9%, S2 12.0%, S6 7.7%, S3 6.1% | S14 +13.5 pp, S20 +2.7 pp, S23 +1.4 pp, S18 +1.1 pp | S13 -2.8 pp, S6 -2.8 pp, S2 -2.5 pp |
| C3 | 4476 (28.0%) | Alimentaire contraint | S2 16.8%, S8 15.8%, S6 13.4%, S3 10.1%, S11 9.7% | S6 +2.9 pp, S2 +2.2 pp, S3 +2.1 pp, S1 +1.9 pp | S13 -3.8 pp, S14 -2.3 pp, S23 -1.0 pp |
| C4 | 2261 (14.2%) | Logement-energie eleve | S8 22.1%, S2 12.0%, S11 10.3%, S6 8.8%, S13 8.3% | S8 +6.5 pp, S13 +2.7 pp, S11 +2.2 pp, S9 +1.5 pp | S3 -2.9 pp, S2 -2.6 pp, S14 -2.1 pp |
| C5 | 593 (3.7%) | Transport-communication tres eleve | S8 12.1%, S2 10.9%, S14 10.6%, S18 7.2%, S6 6.5% | S14 +7.7 pp, S18 +4.5 pp, S23 +2.9 pp, S21 +2.6 pp | S11 -4.2 pp, S6 -4.0 pp, S2 -3.6 pp |
| C6 | 1214 (7.6%) | Autres depenses elevees | S2 13.8%, S8 11.5%, S6 9.1%, S3 7.5%, S21 7.4% | S21 +5.7 pp, S7 +1.7 pp, S15 +1.6 pp, S10 +1.2 pp | S8 -4.1 pp, S14 -2.2 pp, S11 -2.2 pp |
| C7 | 1498 (9.4%) | Transport-communication tres eleve | S14 12.8%, S2 12.8%, S8 12.0%, S6 8.4%, S13 6.8% | S14 +10.0 pp, S20 +2.2 pp, S13 +1.2 pp, S23 +0.7 pp | S8 -3.6 pp, S11 -2.8 pp, S6 -2.1 pp |

#### gamma_0p5_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 3970 (24.9%) | Profil intermediaire | S2 14.8%, S8 13.1%, S6 10.6%, S3 8.5%, S11 7.4% | S15 +1.8 pp, S7 +1.3 pp, S13 +1.3 pp, S10 +0.6 pp | S8 -2.5 pp, S14 -2.3 pp, S18 -0.8 pp |
| C2 | 2568 (16.1%) | Transport-communication tres eleve | S14 13.5%, S8 12.4%, S2 12.0%, S6 7.7%, S3 6.1% | S14 +10.7 pp, S20 +2.4 pp, S23 +1.5 pp, S18 +1.2 pp | S11 -3.1 pp, S8 -3.1 pp, S6 -2.8 pp |
| C3 | 2300 (14.4%) | Logement S8 dominant | S8 16.9%, S2 16.0%, S6 10.6%, S3 8.9%, S11 8.0% | S18 +2.5 pp, S2 +1.5 pp, S7 +1.3 pp, S8 +1.3 pp | S13 -4.1 pp, S14 -2.3 pp, S15 -0.7 pp |
| C4 | 2318 (14.5%) | Alimentaire contraint | S2 17.8%, S6 15.3%, S8 12.7%, S3 11.2%, S11 9.7% | S6 +4.8 pp, S3 +3.2 pp, S2 +3.2 pp, S1 +2.3 pp | S13 -5.0 pp, S8 -2.9 pp, S14 -2.0 pp |
| C5 | 2614 (16.4%) | Sante specialisee | S8 17.4%, S2 14.2%, S13 13.7%, S6 9.8%, S11 9.0% | S13 +8.2 pp, S8 +1.8 pp, S11 +0.9 pp | S14 -2.2 pp, S7 -1.5 pp, S23 -0.8 pp |
| C6 | 1156 (7.2%) | Logement-energie eleve | S8 18.8%, S2 10.0%, S11 8.7%, S6 8.0%, S23 6.0% | S9 +3.7 pp, S23 +3.5 pp, S8 +3.3 pp, S21 +2.6 pp | S2 -4.6 pp, S3 -4.5 pp, S1 -2.5 pp |
| C7 | 1044 (6.5%) | Logement-energie eleve | S8 28.3%, S2 15.1%, S11 12.6%, S6 10.7%, S1 8.8% | S8 +12.8 pp, S11 +4.5 pp, S1 +1.6 pp, S2 +0.6 pp | S13 -4.6 pp, S14 -2.1 pp, S7 -2.0 pp |

#### gamma_0p25_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 3473 (21.7%) | Profil intermediaire | S2 15.1%, S8 13.3%, S6 11.1%, S3 8.7%, S11 7.6% | S15 +1.9 pp, S7 +1.3 pp, S13 +1.2 pp, S3 +0.7 pp | S8 -2.3 pp, S14 -2.3 pp, S18 -1.1 pp |
| C2 | 2094 (13.1%) | Logement S8 dominant | S8 17.0%, S2 16.3%, S6 11.0%, S3 9.1%, S1 8.3% | S18 +2.1 pp, S2 +1.8 pp, S8 +1.4 pp, S7 +1.3 pp | S13 -4.4 pp, S14 -2.3 pp, S9 -1.1 pp |
| C3 | 3009 (18.8%) | Alimentaire contraint | S2 17.2%, S8 15.6%, S6 14.3%, S3 10.4%, S11 10.3% | S6 +3.8 pp, S2 +2.6 pp, S3 +2.4 pp, S1 +2.3 pp | S13 -4.8 pp, S14 -2.0 pp, S18 -1.4 pp |
| C4 | 2493 (15.6%) | Transport-communication tres eleve | S14 13.8%, S8 12.5%, S2 12.0%, S6 7.7%, S3 6.1% | S14 +10.9 pp, S20 +2.5 pp, S23 +1.6 pp, S18 +1.2 pp | S11 -3.2 pp, S8 -3.1 pp, S6 -2.8 pp |
| C5 | 959 (6.0%) | Profil intermediaire | S2 13.7%, S8 11.0%, S6 8.8%, S9 8.4%, S3 7.8% | S9 +6.6 pp, S18 +2.0 pp, S7 +1.1 pp, S10 +1.0 pp | S8 -4.6 pp, S14 -2.0 pp, S11 -1.8 pp |
| C6 | 2518 (15.8%) | Sante specialisee | S8 18.4%, S13 14.2%, S2 13.9%, S6 9.4%, S11 9.0% | S13 +8.6 pp, S8 +2.9 pp, S11 +0.9 pp | S14 -2.2 pp, S7 -1.5 pp, S6 -1.1 pp |
| C7 | 1424 (8.9%) | Logement-energie eleve | S8 22.5%, S2 11.1%, S11 10.0%, S6 8.4%, S1 5.6% | S8 +6.9 pp, S23 +2.3 pp, S9 +1.9 pp, S11 +1.9 pp | S3 -4.0 pp, S2 -3.4 pp, S6 -2.1 pp |

### Annexe numerique : profils complets S1-S23 par prior

#### Profils numeriques complets - gamma_1_1

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4854 (30.4%) | 7.4 | 14.8 | 8.5 | 1.5 | 0.3 | 10.5 | 3.7 | 14.3 | 1.7 | 3.3 | 8.0 | 2.9 | 9.2 | 0.6 | 2.3 | 1.9 | 0.9 | 2.3 | 0.1 | 0.8 | 1.6 | 1.7 | 1.8 |
| C2 | 3502 (21.9%) | 9.1 | 15.9 | 9.3 | 2.1 | 0.2 | 12.7 | 0.8 | 18.5 | 1.3 | 2.4 | 10.9 | 2.2 | 3.5 | 0.6 | 1.8 | 1.2 | 0.5 | 1.9 | 0.0 | 0.8 | 0.9 | 1.8 | 1.5 |
| C3 | 2629 (16.5%) | 8.5 | 17.0 | 10.0 | 1.9 | 0.4 | 12.7 | 4.3 | 14.5 | 1.2 | 3.6 | 8.3 | 3.1 | 0.4 | 0.6 | 2.3 | 2.0 | 0.9 | 2.5 | 0.1 | 0.8 | 1.2 | 1.9 | 1.8 |
| C4 | 1986 (12.4%) | 5.0 | 12.3 | 6.3 | 1.1 | 0.3 | 7.9 | 2.7 | 13.1 | 2.0 | 2.8 | 5.4 | 2.4 | 4.9 | 15.1 | 1.0 | 2.4 | 1.4 | 3.0 | 0.2 | 4.1 | 1.7 | 1.2 | 3.6 |
| C5 | 651 (4.1%) | 4.2 | 11.4 | 5.5 | 0.9 | 0.4 | 6.8 | 3.9 | 11.8 | 1.8 | 3.3 | 4.1 | 2.7 | 5.1 | 9.9 | 0.9 | 2.7 | 3.1 | 7.0 | 0.3 | 3.8 | 4.4 | 0.8 | 4.9 |
| C6 | 997 (6.2%) | 5.3 | 13.9 | 7.0 | 1.1 | 0.5 | 8.5 | 4.7 | 13.3 | 1.6 | 4.0 | 5.5 | 3.5 | 5.7 | 0.7 | 4.0 | 2.8 | 3.5 | 3.1 | 0.4 | 3.4 | 2.0 | 1.2 | 4.4 |
| C7 | 1351 (8.5%) | 4.8 | 10.4 | 3.6 | 0.8 | 0.3 | 7.6 | 1.8 | 21.6 | 4.6 | 1.9 | 8.9 | 1.9 | 9.1 | 1.4 | 1.8 | 2.0 | 1.8 | 3.4 | 0.1 | 1.8 | 3.4 | 2.1 | 4.8 |

#### Profils numeriques complets - gamma_1_2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 5123 (32.1%) | 7.5 | 15.2 | 8.6 | 1.5 | 0.3 | 10.5 | 3.9 | 15.1 | 1.5 | 3.3 | 7.9 | 3.0 | 8.0 | 0.4 | 2.2 | 2.0 | 1.0 | 2.5 | 0.1 | 1.0 | 0.7 | 1.6 | 2.0 |
| C2 | 805 (5.0%) | 5.4 | 12.0 | 6.1 | 1.0 | 0.3 | 7.7 | 1.7 | 14.9 | 2.0 | 2.4 | 5.9 | 2.1 | 2.8 | 16.3 | 0.9 | 2.2 | 1.4 | 3.7 | 0.1 | 4.2 | 2.0 | 1.0 | 3.9 |
| C3 | 4476 (28.0%) | 9.1 | 16.8 | 10.1 | 2.1 | 0.3 | 13.4 | 2.1 | 15.8 | 1.2 | 3.0 | 9.7 | 2.7 | 1.7 | 0.5 | 2.1 | 1.5 | 0.7 | 2.0 | 0.1 | 0.8 | 0.9 | 1.9 | 1.5 |
| C4 | 2261 (14.2%) | 6.3 | 12.0 | 5.1 | 1.2 | 0.3 | 8.8 | 1.5 | 22.1 | 3.3 | 1.8 | 10.3 | 1.8 | 8.3 | 0.8 | 1.7 | 1.6 | 1.4 | 2.8 | 0.1 | 1.4 | 2.1 | 1.9 | 3.6 |
| C5 | 593 (3.7%) | 3.9 | 10.9 | 5.2 | 0.9 | 0.4 | 6.5 | 4.0 | 12.1 | 1.9 | 3.3 | 3.9 | 2.7 | 4.6 | 10.6 | 0.9 | 2.8 | 3.6 | 7.2 | 0.3 | 3.9 | 4.3 | 0.8 | 5.4 |
| C6 | 1214 (7.6%) | 5.7 | 13.8 | 7.5 | 1.2 | 0.4 | 9.1 | 4.6 | 11.5 | 2.2 | 4.2 | 6.0 | 3.1 | 5.4 | 0.7 | 3.7 | 2.3 | 2.2 | 2.7 | 0.4 | 1.3 | 7.4 | 1.7 | 3.0 |
| C7 | 1498 (9.4%) | 5.1 | 12.8 | 6.7 | 1.2 | 0.4 | 8.4 | 3.4 | 12.0 | 1.8 | 3.0 | 5.3 | 2.7 | 6.8 | 12.8 | 1.3 | 2.4 | 1.4 | 2.7 | 0.2 | 3.8 | 1.3 | 1.2 | 3.2 |

#### Profils numeriques complets - gamma_0p5_2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 3970 (24.9%) | 7.1 | 14.8 | 8.5 | 1.5 | 0.4 | 10.6 | 4.3 | 13.1 | 1.7 | 3.7 | 7.4 | 3.1 | 6.9 | 0.6 | 3.8 | 2.2 | 1.4 | 1.9 | 0.2 | 1.1 | 1.8 | 1.8 | 2.3 |
| C2 | 2568 (16.1%) | 4.8 | 12.0 | 6.1 | 1.1 | 0.4 | 7.7 | 3.2 | 12.4 | 2.0 | 3.0 | 5.0 | 2.5 | 5.1 | 13.5 | 1.1 | 2.5 | 1.9 | 3.9 | 0.2 | 3.9 | 2.4 | 1.1 | 4.0 |
| C3 | 2300 (14.4%) | 8.0 | 16.0 | 8.9 | 1.5 | 0.4 | 10.6 | 4.2 | 16.9 | 1.2 | 3.4 | 8.0 | 3.2 | 1.5 | 0.5 | 1.4 | 2.2 | 1.1 | 5.2 | 0.1 | 1.1 | 1.3 | 1.5 | 1.9 |
| C4 | 2318 (14.5%) | 9.5 | 17.8 | 11.2 | 2.4 | 0.3 | 15.3 | 2.0 | 12.7 | 1.3 | 3.4 | 9.7 | 2.5 | 0.6 | 0.8 | 2.0 | 1.4 | 0.7 | 1.0 | 0.1 | 0.7 | 1.1 | 2.1 | 1.5 |
| C5 | 2614 (16.4%) | 7.5 | 14.2 | 7.7 | 1.5 | 0.3 | 9.8 | 1.4 | 17.4 | 1.4 | 2.5 | 9.0 | 2.3 | 13.7 | 0.6 | 1.2 | 1.5 | 0.6 | 1.8 | 0.1 | 1.0 | 1.1 | 1.5 | 1.7 |
| C6 | 1156 (7.2%) | 4.7 | 10.0 | 3.5 | 0.9 | 0.3 | 8.0 | 2.1 | 18.8 | 5.5 | 2.2 | 8.7 | 2.0 | 5.9 | 2.7 | 1.8 | 2.1 | 2.3 | 3.5 | 0.2 | 2.2 | 4.3 | 2.4 | 6.0 |
| C7 | 1044 (6.5%) | 8.8 | 15.1 | 7.4 | 1.7 | 0.3 | 10.7 | 0.9 | 28.3 | 0.7 | 1.3 | 12.6 | 1.8 | 1.0 | 0.7 | 1.4 | 1.2 | 0.4 | 1.8 | 0.0 | 0.8 | 0.5 | 1.4 | 1.3 |

#### Profils numeriques complets - gamma_0p25_2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 3473 (21.7%) | 7.4 | 15.1 | 8.7 | 1.5 | 0.3 | 11.1 | 4.2 | 13.3 | 0.9 | 3.6 | 7.6 | 3.2 | 6.8 | 0.6 | 3.9 | 2.1 | 1.3 | 1.6 | 0.2 | 1.1 | 1.6 | 1.8 | 2.2 |
| C2 | 2094 (13.1%) | 8.3 | 16.3 | 9.1 | 1.6 | 0.4 | 11.0 | 4.2 | 17.0 | 0.7 | 3.3 | 8.1 | 3.2 | 1.2 | 0.5 | 1.5 | 2.2 | 1.0 | 4.8 | 0.1 | 1.0 | 1.2 | 1.5 | 1.8 |
| C3 | 3009 (18.8%) | 9.5 | 17.2 | 10.4 | 2.3 | 0.3 | 14.3 | 1.7 | 15.6 | 1.2 | 3.0 | 10.3 | 2.4 | 0.7 | 0.8 | 1.9 | 1.3 | 0.6 | 1.2 | 0.1 | 0.7 | 1.1 | 2.0 | 1.5 |
| C4 | 2493 (15.6%) | 4.7 | 12.0 | 6.1 | 1.1 | 0.4 | 7.7 | 3.2 | 12.5 | 1.7 | 3.0 | 4.9 | 2.5 | 5.1 | 13.8 | 1.1 | 2.5 | 2.0 | 3.9 | 0.2 | 4.0 | 2.5 | 1.1 | 4.1 |
| C5 | 959 (6.0%) | 6.0 | 13.7 | 7.8 | 1.4 | 0.4 | 8.8 | 4.1 | 11.0 | 8.4 | 4.0 | 6.3 | 2.7 | 6.2 | 0.8 | 1.9 | 2.0 | 1.5 | 4.7 | 0.2 | 1.3 | 2.3 | 1.7 | 2.8 |
| C6 | 2518 (15.8%) | 7.1 | 13.9 | 7.5 | 1.5 | 0.3 | 9.4 | 1.4 | 18.4 | 1.1 | 2.4 | 9.0 | 2.3 | 14.2 | 0.6 | 1.3 | 1.6 | 0.7 | 1.9 | 0.1 | 1.1 | 1.2 | 1.4 | 1.7 |
| C7 | 1424 (8.9%) | 5.6 | 11.1 | 4.0 | 1.0 | 0.3 | 8.4 | 1.8 | 22.5 | 3.7 | 1.9 | 10.0 | 1.9 | 4.6 | 2.2 | 1.7 | 1.9 | 1.8 | 3.1 | 0.2 | 1.9 | 3.3 | 2.2 | 4.8 |


## Synthese comparative 2007-2014

Le passage de 9 a 23 postes rend les profils plus riches : les composantes ne sont plus seulement alimentaires, logement, sante ou transport ; elles distinguent aussi des sous-types alimentaires, les differents blocs du logement, la sante detaillee, la culture/enseignement et les postes residuels. En 2007, la segmentation reste fortement liee au niveau de vie et au milieu, avec des profils alimentaires/logement opposes a des profils sante, transport ou depenses diversifiees. En 2014, la separation par niveau de vie demeure forte mais les profils sont plus differencies, ce qui traduit une diversification de la structure de consommation et une meilleure identification des comportements non alimentaires.