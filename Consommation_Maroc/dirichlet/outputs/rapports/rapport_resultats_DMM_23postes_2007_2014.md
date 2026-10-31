# Rapport detaille des resultats DMM - 23 postes, ENNVM 2007 et ENCDM 2014

Ce rapport analyse les resultats du DMM applique aux matrices fines en 23 postes. Par rapport au rapport 9 postes, l'objectif est de decrire les sous-profils de consommation : sous-composantes alimentaires, logement-energie, sante detaillee, transport, culture et autres depenses. La lecture economique est faite a deux niveaux : les postes fins S1-S23 et des familles agregees reconstruites a partir du mapping des matrices.

## Mapping S1-S23 utilise dans le rapport

| Poste | Codes sources | Libelle court |
| --- | --- | --- |
| S1 | DAM_G01 | S1 alimentaire 01 |
| S2 | DAM_G02, DAM_G04, DAM_G05 | S2 alimentaire 02/04/05 |
| S3 | DAM_G06, DAM_G07, DAM_G08 | S3 alimentaire 06/07/08 |
| S4 | DAM_G09, DAM_G10 | S4 alimentaire 09/10 |
| S5 | DAM_G13, DAM_G14 | S5 alimentaire 13/14 |
| S6 | DAM_G03, DAM_G11, DAM_G12, DAM_G15, DAM_G17, DAM_G18 | S6 alimentaire mixte |
| S7 | DAM_G21 a DAM_G28 | S7 habillement-chaussures |
| S8 | DAM_G31 | S8 logement poste 31 |
| S9 | DAM_G32, DAM_G34 | S9 logement/energie 32/34 |
| S10 | DAM_G41 a DAM_G47 | S10 ameublement-equipement |
| S11 | DAM_G33 | S11 logement poste 33 |
| S12 | DAM_G51 | S12 sante 51 |
| S13 | DAM_G52, DAM_G53 | S13 sante 52/53 |
| S14 | DAM_G61 | S14 transport 61 |
| S15 | DAM_G62 | S15 transport 62 |
| S16 | DAM_G63 | S16 transport/communication 63 |
| S17 | DAM_G71 a DAM_G74 | S17 loisirs/culture 71/74 |
| S18 | DAM_G75, DAM_G76; + DAM_G77 dans ENCDM | S18 culture/enseignement 75/76/77 |
| S19 | DAM_G81 a DAM_G84 | S19 autres 81/84 |
| S20 | DAM_G87, DAM_G88 | S20 autres 87/88 |
| S21 | DAM_G85, DAM_G86 | S21 autres 85/86 |
| S22 | DAM_G89 | S22 autres 89 |
| S23 | DAM_G91 a DAM_G94 | S23 autres 91/94 |

## Conclusion generale sur K

Pour les deux enquetes, AIC/BIC favorisent les solutions les plus fines, mais la lecture comportementale ne doit pas suivre automatiquement K=9. Les solutions fines augmentent l'ambiguite et multiplient des sous-profils parfois proches. K=6 ressort comme solution centrale : il donne une segmentation riche, beaucoup plus informative que K=2-K4, tout en restant lisible. K=7 peut etre considere comme variante raffinee, surtout pour ENNVM 2007, mais K=6 reste le meilleur choix de presentation.

## ENNVM 2007 - resultats DMM 23 postes

### Structure moyenne de reference

#### Parts S1-S23

| Poste | Libelle court | Part moyenne |
| --- | --- | --- |
| S1 | S1 alimentaire 01 | 9.3% |
| S2 | S2 alimentaire 02/04/05 | 15.8% |
| S3 | S3 alimentaire 06/07/08 | 8.9% |
| S4 | S4 alimentaire 09/10 | 2.3% |
| S5 | S5 alimentaire 13/14 | 0.2% |
| S6 | S6 alimentaire mixte | 10.1% |
| S7 | S7 habillement-chaussures | 3.0% |
| S8 | S8 logement poste 31 | 10.9% |
| S9 | S9 logement/energie 32/34 | 2.4% |
| S10 | S10 ameublement-equipement | 3.3% |
| S11 | S11 logement poste 33 | 9.4% |
| S12 | S12 sante 51 | 2.4% |
| S13 | S13 sante 52/53 | 4.5% |
| S14 | S14 transport 61 | 3.1% |
| S15 | S15 transport 62 | 1.9% |
| S16 | S16 transport/communication 63 | 2.3% |
| S17 | S17 loisirs/culture 71/74 | 1.3% |
| S18 | S18 culture/enseignement 75/76/77 | 2.1% |
| S19 | S19 autres 81/84 | 0.1% |
| S20 | S20 autres 87/88 | 1.2% |
| S21 | S21 autres 85/86 | 1.2% |
| S22 | S22 autres 89 | 2.3% |
| S23 | S23 autres 91/94 | 2.1% |

#### Regroupement par familles

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

### Comparaison statistique de K=2 a K=9

| K | BIC | AIC | Entropie | Prob. max moy. | Ambigus <0.60 | Taille min | Taille max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | -1409090 | -1409412 | 0.948 | 0.985 | 0.9% | 911 | 6151 |
| 3 | -1416471 | -1416958 | 0.826 | 0.922 | 4.6% | 842 | 3669 |
| 4 | -1418460 | -1419112 | 0.843 | 0.913 | 4.9% | 859 | 4081 |
| 5 | -1421767 | -1422584 | 0.809 | 0.877 | 9.3% | 762 | 2053 |
| 6 | -1424749 | -1425730 | 0.798 | 0.853 | 11.8% | 708 | 1789 |
| 7 | -1426429 | -1427575 | 0.810 | 0.851 | 12.3% | 567 | 1559 |
| 8 | -1427035 | -1428346 | 0.800 | 0.836 | 13.6% | 239 | 1476 |
| 9 | -1429120 | -1430595 | 0.810 | 0.838 | 13.8% | 533 | 1304 |

Lecture : les criteres AIC/BIC continuent de favoriser K=9, mais la solution devient progressivement plus fragmentee. K=6 donne deja une decomposition fine avec des groupes interpretablement distincts : alimentaire contraint, sante detaillee, transport tres eleve, logement-energie et profils intermediaires. K=7 apporte une nuance supplementaire sans perte forte, mais K=8 introduit un groupe plus petit et K=9 fragmente davantage la lecture. Le choix central defendable est donc K=6, avec K=7 comme extension analytique possible.

### Propagation comportementale des profils

A K=2, le modele oppose un grand bloc alimentaire-logement a un bloc plus aise/diversifie. K=3 separe deja une composante a forte sante et une composante alimentaire. K=4 clarifie le transport tres eleve. K=5 et K=6 distinguent mieux logement, sante detaillee et alimentation. Au-dela, les nouvelles classes deviennent surtout des sous-profils : variations de S8/S11 dans le logement, de S13 dans la sante ou de S14 dans le transport.

### Profils K=6 : lecture par familles

| Cluster | Taille | Libelle | Alimentaire | Habillement | Logement-energie | Ameublement-equipement | Sante | Transport-communication | Culture-enseignement | Autres depenses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1660 (23.5%) | Alimentaire contraint | 57.1 | 2.2 | 23.8 | 3.2 | 2.7 | 3.6 | 2.2 | 5.2 |
| C2 | 708 (10.0%) | Profil intermediaire | 44.2 | 4.7 | 22.6 | 4.3 | 6.3 | 7.6 | 3.3 | 7.0 |
| C3 | 1295 (18.3%) | Alimentaire S2 dominant | 50.1 | 4.8 | 20.6 | 3.9 | 4.9 | 5.2 | 5.0 | 5.6 |
| C4 | 827 (11.7%) | Transport tres eleve | 32.5 | 3.1 | 17.0 | 3.2 | 5.9 | 23.4 | 4.5 | 10.5 |
| C5 | 1789 (25.3%) | Sante detaillee elevee | 45.1 | 2.3 | 22.0 | 3.2 | 13.1 | 5.1 | 2.6 | 6.5 |
| C6 | 783 (11.1%) | Logement-energie tres eleve | 38.6 | 1.9 | 31.9 | 1.9 | 6.1 | 6.3 | 3.5 | 9.8 |

### Profils K=6 : signatures fines S1-S23

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1660 (23.5%) | Alimentaire contraint | S2 16.8%, S6 13.1%, S1 12.7%, S11 11.7%, S3 10.8% | S1 +3.4 pp, S6 +3.1 pp, S11 +2.3 pp, S3 +1.9 pp | S13 -3.8 pp, S14 -2.2 pp, S16 -1.1 pp |
| C2 | 708 (10.0%) | Profil intermediaire | S2 14.7%, S6 10.0%, S3 8.5%, S1 8.5%, S8 7.7% | S9 +5.2 pp, S15 +2.0 pp, S7 +1.6 pp, S10 +1.0 pp | S8 -3.2 pp, S11 -2.1 pp, S14 -2.1 pp |
| C3 | 1295 (18.3%) | Alimentaire S2 dominant | S2 17.8%, S8 11.1%, S6 10.2%, S3 10.1%, S1 9.5% | S2 +2.1 pp, S7 +1.8 pp, S18 +1.6 pp, S3 +1.2 pp | S13 -2.7 pp, S14 -2.4 pp, S9 -1.5 pp |
| C4 | 827 (11.7%) | Transport tres eleve | S14 19.2%, S2 13.0%, S8 9.3%, S6 6.7%, S3 6.2% | S14 +16.1 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.3 pp, S11 -3.8 pp, S6 -3.3 pp |
| C5 | 1789 (25.3%) | Sante detaillee elevee | S2 15.5%, S8 11.3%, S13 10.7%, S6 9.6%, S11 9.1% | S13 +6.2 pp | S14 -2.4 pp, S9 -0.9 pp, S7 -0.7 pp |
| C6 | 783 (11.1%) | Logement-energie tres eleve | S8 15.9%, S2 14.6%, S11 12.1%, S6 7.9%, S1 7.8% | S8 +4.9 pp, S11 +2.7 pp, S9 +1.5 pp, S23 +1.1 pp | S3 -2.3 pp, S6 -2.1 pp, S1 -1.5 pp |

### Caracterisation socio-economique K=6

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1660 | 33147 | 29198 | -41.7% | 39.0% | 61.0% | Q1 (39.6%) |
| C2 | 708 | 62908 | 54336 | +10.6% | 50.7% | 49.3% | Q4 (30.8%) |
| C3 | 1295 | 53955 | 46553 | -5.2% | 75.1% | 24.9% | Q4 (28.3%) |
| C4 | 827 | 128391 | 97095 | +125.7% | 74.4% | 25.6% | Q5 (67.7%) |
| C5 | 1789 | 49286 | 43325 | -13.4% | 64.3% | 35.7% | Q4 (24.4%) |
| C6 | 783 | 48471 | 31369 | -14.8% | 66.4% | 33.6% | Q1 (40.6%) |

### Parametres de Dirichlet K=6

`pi` donne le poids du cluster dans le melange. `alpha_sum` indique la concentration du profil : plus elle est elevee, plus la composante est homogene autour de son profil moyen theorique.

| Cluster | pi | alpha_sum | Profil theorique dominant |
| --- | --- | --- | --- |
| C1 | 0.248 | 19.6 | S2=17.2%, S6=13.6%, S1=13.0%, S11=12.1%, S3=11.6% |
| C2 | 0.096 | 24.5 | S2=15.0%, S6=10.6%, S3=9.4%, S1=9.0%, S11=8.2% |
| C3 | 0.177 | 28.7 | S2=17.9%, S8=10.6%, S3=10.6%, S6=10.6%, S1=9.7% |
| C4 | 0.114 | 20.9 | S14=17.3%, S2=13.8%, S8=9.2%, S6=7.3%, S3=7.2% |
| C5 | 0.247 | 19.7 | S2=16.2%, S8=10.9%, S6=10.4%, S11=10.2%, S3=9.8% |
| C6 | 0.119 | 8.2 | S8=16.5%, S2=15.3%, S11=13.9%, S1=7.7%, S6=7.5% |

### Diagnostics socio-economiques globaux

| K | Cramer Milieu | Cramer quintile_DAM | eta2 DAM | eta2 log_DAM | Associations qualitatives dominantes |
| --- | --- | --- | --- | --- | --- |
| 2 | 0.119 | 0.466 | 0.244 | 0.218 | quintile_DAM=0.466 ; Quintiles=0.351 ; Profession_CM=0.310 ; Niveau_scolaire_CM=0.296 ; Strate_habitat=0.175 |
| 3 | 0.115 | 0.375 | 0.243 | 0.256 | quintile_DAM=0.375 ; Quintiles=0.262 ; Profession_CM=0.240 ; Niveau_scolaire_CM=0.213 ; Taille_ménage_agreg=0.196 |
| 4 | 0.129 | 0.312 | 0.250 | 0.258 | quintile_DAM=0.312 ; Quintiles=0.231 ; Profession_CM=0.197 ; Taille_ménage_agreg=0.172 ; Niveau_scolaire_CM=0.171 |
| 5 | 0.267 | 0.289 | 0.263 | 0.296 | quintile_DAM=0.289 ; Milieu=0.267 ; Quintiles=0.210 ; Profession_CM=0.195 ; Niveau_scolaire_CM=0.160 |
| 6 | 0.280 | 0.300 | 0.255 | 0.300 | quintile_DAM=0.300 ; Milieu=0.280 ; Quintiles=0.219 ; Profession_CM=0.184 ; Niveau_scolaire_CM=0.165 |
| 7 | 0.279 | 0.299 | 0.254 | 0.300 | quintile_DAM=0.299 ; Milieu=0.279 ; Quintiles=0.216 ; Profession_CM=0.170 ; Niveau_scolaire_CM=0.167 |
| 8 | 0.305 | 0.300 | 0.260 | 0.305 | Milieu=0.305 ; quintile_DAM=0.300 ; Quintiles=0.219 ; Niveau_scolaire_CM=0.171 ; Profession_CM=0.162 |
| 9 | 0.353 | 0.311 | 0.263 | 0.317 | Milieu=0.353 ; quintile_DAM=0.311 ; Quintiles=0.224 ; Niveau_scolaire_CM=0.183 ; Strate_habitat=0.177 |

### Annexe : signatures des profils pour tous les K

#### K=2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 6151 (87.1%) | Alimentaire S2 dominant | S2 16.2%, S8 11.2%, S6 10.5%, S11 9.9%, S1 9.9% | S1 +0.6 pp, S11 +0.6 pp, S6 +0.5 pp, S2 +0.4 pp | S14 -2.3 pp |
| C2 | 911 (12.9%) | Transport tres eleve | S14 18.5%, S2 13.0%, S8 9.4%, S6 6.8%, S3 6.2% | S14 +15.4 pp, S20 +2.7 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.2 pp, S11 -3.8 pp, S6 -3.3 pp |

#### K=3

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 2551 (36.1%) | Profil intermediaire | S2 15.7%, S8 13.3%, S11 11.7%, S6 10.1%, S1 9.9% | S8 +2.3 pp, S11 +2.3 pp, S13 +0.8 pp, S9 +0.6 pp | S14 -2.1 pp, S7 -1.9 pp, S10 -0.9 pp |
| C2 | 3669 (52.0%) | Alimentaire S2 dominant | S2 16.5%, S6 10.8%, S1 9.9%, S3 9.8%, S8 9.7% | S7 +1.3 pp, S3 +0.9 pp, S6 +0.8 pp, S2 +0.7 pp | S14 -2.3 pp, S8 -1.2 pp, S11 -0.7 pp |
| C3 | 842 (11.9%) | Transport tres eleve | S14 19.4%, S2 12.8%, S8 9.2%, S6 6.6%, S3 6.1% | S14 +16.3 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.3 pp, S11 -3.9 pp, S6 -3.5 pp |

#### K=4

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 959 (13.6%) | Profil intermediaire | S2 15.2%, S6 9.6%, S3 8.7%, S1 8.4%, S8 8.2% | S9 +3.6 pp, S13 +2.1 pp, S7 +1.6 pp, S10 +0.9 pp | S8 -2.8 pp, S14 -2.2 pp, S11 -2.1 pp |
| C2 | 1163 (16.5%) | Logement-energie tres eleve | S8 14.9%, S2 14.9%, S11 11.8%, S1 8.5%, S6 8.4% | S8 +4.0 pp, S11 +2.4 pp, S13 +2.1 pp, S9 +1.1 pp | S3 -1.9 pp, S6 -1.7 pp, S14 -1.6 pp |
| C3 | 859 (12.2%) | Transport tres eleve | S14 18.6%, S2 13.1%, S8 9.3%, S6 6.7%, S3 6.2% | S14 +15.5 pp, S20 +2.7 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.2 pp, S11 -3.8 pp, S6 -3.3 pp |
| C4 | 4081 (57.8%) | Alimentaire S2 dominant | S2 16.7%, S6 11.3%, S8 10.8%, S1 10.6%, S3 10.1% | S1 +1.3 pp, S6 +1.3 pp, S3 +1.2 pp, S2 +1.0 pp | S14 -2.3 pp, S9 -1.1 pp, S13 -1.0 pp |

#### K=5

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 806 (11.4%) | Transport tres eleve | S14 19.9%, S2 12.9%, S8 9.2%, S6 6.6%, S3 6.1% | S14 +16.8 pp, S20 +2.9 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.4 pp, S11 -3.8 pp, S6 -3.5 pp |
| C2 | 1981 (28.1%) | Profil intermediaire | S2 15.9%, S8 14.4%, S11 11.9%, S6 9.8%, S1 9.8% | S8 +3.4 pp, S11 +2.5 pp, S13 +0.8 pp, S1 +0.5 pp | S14 -2.1 pp, S7 -1.8 pp, S9 -1.1 pp |
| C3 | 1460 (20.7%) | Alimentaire contraint | S2 17.1%, S6 12.7%, S1 12.0%, S3 11.1%, S11 10.1% | S6 +2.7 pp, S1 +2.6 pp, S3 +2.2 pp, S7 +1.4 pp | S13 -3.3 pp, S14 -2.2 pp, S9 -1.8 pp |
| C4 | 762 (10.8%) | Profil intermediaire | S2 14.9%, S9 11.6%, S6 10.7%, S1 9.8%, S11 9.3% | S9 +9.2 pp, S6 +0.6 pp, S1 +0.5 pp, S4 +0.5 pp | S8 -3.0 pp, S14 -1.9 pp, S13 -1.3 pp |
| C5 | 2053 (29.1%) | Alimentaire S2 dominant | S2 16.1%, S8 10.5%, S6 9.5%, S3 8.9%, S1 8.5% | S13 +2.4 pp, S7 +1.3 pp, S15 +0.7 pp, S10 +0.7 pp | S14 -2.3 pp, S11 -1.4 pp, S9 -0.9 pp |

#### K=6

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1660 (23.5%) | Alimentaire contraint | S2 16.8%, S6 13.1%, S1 12.7%, S11 11.7%, S3 10.8% | S1 +3.4 pp, S6 +3.1 pp, S11 +2.3 pp, S3 +1.9 pp | S13 -3.8 pp, S14 -2.2 pp, S16 -1.1 pp |
| C2 | 708 (10.0%) | Profil intermediaire | S2 14.7%, S6 10.0%, S3 8.5%, S1 8.5%, S8 7.7% | S9 +5.2 pp, S15 +2.0 pp, S7 +1.6 pp, S10 +1.0 pp | S8 -3.2 pp, S11 -2.1 pp, S14 -2.1 pp |
| C3 | 1295 (18.3%) | Alimentaire S2 dominant | S2 17.8%, S8 11.1%, S6 10.2%, S3 10.1%, S1 9.5% | S2 +2.1 pp, S7 +1.8 pp, S18 +1.6 pp, S3 +1.2 pp | S13 -2.7 pp, S14 -2.4 pp, S9 -1.5 pp |
| C4 | 827 (11.7%) | Transport tres eleve | S14 19.2%, S2 13.0%, S8 9.3%, S6 6.7%, S3 6.2% | S14 +16.1 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.3 pp, S11 -3.8 pp, S6 -3.3 pp |
| C5 | 1789 (25.3%) | Sante detaillee elevee | S2 15.5%, S8 11.3%, S13 10.7%, S6 9.6%, S11 9.1% | S13 +6.2 pp | S14 -2.4 pp, S9 -0.9 pp, S7 -0.7 pp |
| C6 | 783 (11.1%) | Logement-energie tres eleve | S8 15.9%, S2 14.6%, S11 12.1%, S6 7.9%, S1 7.8% | S8 +4.9 pp, S11 +2.7 pp, S9 +1.5 pp, S23 +1.1 pp | S3 -2.3 pp, S6 -2.1 pp, S1 -1.5 pp |

#### K=7

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 567 (8.0%) | Autres/culture diversifies | S2 14.1%, S6 10.7%, S1 8.8%, S8 8.7%, S3 8.3% | S22 +5.5 pp, S15 +2.1 pp, S13 +0.8 pp, S7 +0.8 pp | S8 -2.2 pp, S14 -2.1 pp, S11 -1.9 pp |
| C2 | 733 (10.4%) | Logement-energie tres eleve | S8 16.1%, S2 14.6%, S11 12.4%, S6 7.8%, S1 7.7% | S8 +5.2 pp, S11 +3.0 pp, S23 +1.3 pp, S21 +1.0 pp | S3 -2.4 pp, S6 -2.3 pp, S1 -1.7 pp |
| C3 | 823 (11.7%) | Transport tres eleve | S14 19.4%, S2 13.0%, S8 9.2%, S6 6.7%, S3 6.2% | S14 +16.4 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.3 pp, S11 -3.8 pp, S6 -3.3 pp |
| C4 | 702 (9.9%) | Profil intermediaire | S2 14.5%, S9 10.6%, S6 10.1%, S1 9.1%, S3 9.0% | S9 +8.2 pp, S7 +1.5 pp, S10 +0.9 pp, S15 +0.5 pp | S8 -3.6 pp, S14 -1.8 pp, S13 -1.7 pp |
| C5 | 1189 (16.8%) | Alimentaire S2 dominant | S2 18.1%, S8 11.3%, S3 10.2%, S6 10.2%, S1 9.5% | S2 +2.3 pp, S7 +1.8 pp, S18 +1.7 pp, S3 +1.3 pp | S13 -2.5 pp, S14 -2.4 pp, S9 -1.8 pp |
| C6 | 1559 (22.1%) | Alimentaire contraint | S2 17.0%, S6 13.1%, S1 12.8%, S11 11.9%, S3 10.8% | S1 +3.5 pp, S6 +3.1 pp, S11 +2.5 pp, S3 +1.9 pp | S13 -3.9 pp, S14 -2.2 pp, S9 -1.2 pp |
| C7 | 1489 (21.1%) | Sante detaillee elevee | S2 15.8%, S8 11.9%, S13 11.6%, S6 9.4%, S11 9.4% | S13 +7.1 pp, S8 +1.0 pp | S14 -2.5 pp, S9 -1.0 pp, S7 -1.0 pp |

#### K=8

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 568 (8.0%) | Autres/culture diversifies | S2 14.0%, S6 10.7%, S1 8.8%, S8 8.7%, S3 8.3% | S22 +5.6 pp, S15 +2.1 pp, S7 +0.8 pp, S13 +0.8 pp | S8 -2.3 pp, S14 -2.1 pp, S11 -1.9 pp |
| C2 | 1173 (16.6%) | Alimentaire S2 dominant | S2 18.1%, S8 11.2%, S3 10.2%, S6 10.2%, S1 9.5% | S2 +2.3 pp, S7 +1.8 pp, S18 +1.7 pp, S3 +1.3 pp | S13 -2.6 pp, S14 -2.5 pp, S9 -1.8 pp |
| C3 | 1333 (18.9%) | Alimentaire contraint | S2 17.1%, S6 13.6%, S1 13.4%, S11 11.9%, S3 11.3% | S1 +4.1 pp, S6 +3.6 pp, S11 +2.5 pp, S3 +2.4 pp | S13 -3.8 pp, S14 -2.2 pp, S8 -1.5 pp |
| C4 | 690 (9.8%) | Profil intermediaire | S2 14.4%, S9 11.0%, S6 9.8%, S3 8.9%, S1 8.9% | S9 +8.6 pp, S7 +1.5 pp, S10 +0.9 pp, S15 +0.5 pp | S8 -3.6 pp, S14 -1.8 pp, S13 -1.8 pp |
| C5 | 828 (11.7%) | Transport tres eleve | S14 19.5%, S2 13.0%, S8 9.3%, S6 6.7%, S3 6.2% | S14 +16.4 pp, S20 +2.8 pp, S23 +1.2 pp, S16 +0.8 pp | S1 -4.3 pp, S11 -3.8 pp, S6 -3.4 pp |
| C6 | 239 (3.4%) | Logement-energie tres eleve | S8 14.5%, S11 12.2%, S2 12.2%, S6 7.2%, S13 6.7% | S8 +3.6 pp, S9 +3.2 pp, S11 +2.8 pp, S13 +2.2 pp | S3 -3.9 pp, S1 -3.7 pp, S2 -3.5 pp |
| C7 | 1476 (20.9%) | Sante detaillee elevee | S2 15.7%, S8 11.7%, S13 11.6%, S6 9.4%, S11 9.4% | S13 +7.1 pp, S8 +0.8 pp | S14 -2.5 pp, S9 -1.0 pp, S7 -0.9 pp |
| C8 | 755 (10.7%) | Logement-energie tres eleve | S8 17.3%, S2 16.5%, S11 12.3%, S1 9.3%, S6 9.1% | S8 +6.3 pp, S11 +2.9 pp, S22 +0.8 pp, S2 +0.7 pp | S14 -2.1 pp, S13 -1.9 pp, S10 -1.7 pp |

#### K=9

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 533 (7.5%) | Logement-energie tres eleve | S8 15.2%, S2 13.5%, S11 13.3%, S6 8.0%, S1 7.6% | S8 +4.2 pp, S11 +3.9 pp, S9 +1.7 pp, S21 +1.5 pp | S3 -2.9 pp, S2 -2.2 pp, S6 -2.0 pp |
| C2 | 559 (7.9%) | Logement-energie tres eleve | S8 18.8%, S2 17.6%, S11 11.0%, S1 8.5%, S6 8.4% | S8 +7.8 pp, S2 +1.9 pp, S11 +1.6 pp, S16 +1.6 pp | S13 -3.1 pp, S14 -2.4 pp, S6 -1.7 pp |
| C3 | 800 (11.3%) | Profil intermediaire | S2 15.5%, S8 10.0%, S6 9.2%, S3 8.6%, S1 7.9% | S13 +2.2 pp, S15 +2.1 pp, S18 +1.7 pp, S7 +1.6 pp | S14 -2.2 pp, S11 -2.0 pp, S1 -1.4 pp |
| C4 | 612 (8.7%) | Profil intermediaire | S2 14.7%, S9 11.6%, S6 9.8%, S1 9.0%, S3 8.9% | S9 +9.2 pp, S7 +1.3 pp, S10 +1.0 pp, S15 +0.4 pp | S8 -3.7 pp, S13 -1.7 pp, S14 -1.7 pp |
| C5 | 816 (11.6%) | Autres/culture diversifies | S2 14.9%, S6 11.4%, S8 9.9%, S22 9.9%, S1 9.5% | S22 +7.6 pp, S6 +1.4 pp, S7 +1.1 pp, S12 +0.5 pp | S13 -2.4 pp, S14 -2.2 pp, S9 -1.4 pp |
| C6 | 801 (11.3%) | Transport tres eleve | S14 19.7%, S2 13.0%, S8 9.2%, S6 6.7%, S3 6.2% | S14 +16.7 pp, S20 +2.8 pp, S23 +1.3 pp, S16 +0.8 pp | S1 -4.3 pp, S11 -3.8 pp, S6 -3.3 pp |
| C7 | 606 (8.6%) | Alimentaire S2 dominant | S2 19.0%, S8 11.5%, S3 11.0%, S6 10.6%, S1 10.2% | S2 +3.3 pp, S3 +2.1 pp, S7 +1.7 pp, S18 +1.6 pp | S13 -3.3 pp, S14 -2.5 pp, S22 -2.0 pp |
| C8 | 1031 (14.6%) | Alimentaire contraint | S2 17.4%, S6 14.2%, S1 14.2%, S11 12.2%, S3 11.4% | S1 +4.8 pp, S6 +4.1 pp, S11 +2.8 pp, S3 +2.4 pp | S13 -4.1 pp, S14 -2.2 pp, S8 -1.6 pp |
| C9 | 1304 (18.5%) | Sante detaillee elevee | S2 15.9%, S13 11.8%, S8 10.9%, S6 9.9%, S1 9.7% | S13 +7.3 pp | S14 -2.4 pp, S7 -1.1 pp, S9 -0.9 pp |

### Annexe : profils numeriques complets pour tous les K

Les valeurs sont exprimees en pourcentage de la depense totale du menage dans le cluster.

#### Profils numeriques K=2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 6151 (87.1%) | 9.9 | 16.2 | 9.3 | 2.4 | 0.2 | 10.5 | 3.0 | 11.2 | 2.4 | 3.3 | 9.9 | 2.4 | 4.6 | 0.8 | 2.1 | 2.1 | 1.2 | 2.0 | 0.1 | 0.8 | 1.2 | 2.5 | 1.9 |
| C2 | 911 (12.9%) | 5.1 | 13.0 | 6.2 | 1.2 | 0.3 | 6.8 | 3.1 | 9.4 | 2.2 | 3.2 | 5.6 | 2.2 | 4.0 | 18.5 | 1.2 | 3.1 | 1.8 | 2.8 | 0.2 | 3.9 | 1.6 | 1.3 | 3.3 |

#### Profils numeriques K=3

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2551 (36.1%) | 9.9 | 15.7 | 8.6 | 2.3 | 0.2 | 10.1 | 1.2 | 13.3 | 3.0 | 2.4 | 11.7 | 1.9 | 5.3 | 0.9 | 1.7 | 2.0 | 1.1 | 1.9 | 0.0 | 1.0 | 1.4 | 2.5 | 1.9 |
| C2 | 3669 (52.0%) | 9.9 | 16.5 | 9.8 | 2.5 | 0.2 | 10.8 | 4.3 | 9.7 | 2.0 | 3.9 | 8.7 | 2.7 | 4.1 | 0.8 | 2.3 | 2.3 | 1.3 | 2.1 | 0.1 | 0.7 | 1.1 | 2.4 | 1.9 |
| C3 | 842 (11.9%) | 5.0 | 12.8 | 6.1 | 1.2 | 0.3 | 6.6 | 3.0 | 9.2 | 2.4 | 3.2 | 5.5 | 2.2 | 4.0 | 19.4 | 1.1 | 3.1 | 1.8 | 2.8 | 0.2 | 4.0 | 1.6 | 1.4 | 3.3 |

#### Profils numeriques K=4

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 959 (13.6%) | 8.4 | 15.2 | 8.7 | 2.1 | 0.3 | 9.6 | 4.6 | 8.2 | 6.0 | 4.1 | 7.3 | 2.6 | 6.6 | 0.9 | 2.7 | 2.7 | 1.5 | 2.2 | 0.2 | 0.8 | 1.2 | 2.2 | 2.1 |
| C2 | 1163 (16.5%) | 8.5 | 14.9 | 7.0 | 1.6 | 0.2 | 8.4 | 1.8 | 14.9 | 3.5 | 1.9 | 11.8 | 1.7 | 6.6 | 1.5 | 1.7 | 2.4 | 1.2 | 2.0 | 0.1 | 1.5 | 1.8 | 2.4 | 2.6 |
| C3 | 859 (12.2%) | 5.1 | 13.1 | 6.2 | 1.2 | 0.3 | 6.7 | 3.1 | 9.3 | 2.1 | 3.3 | 5.5 | 2.2 | 4.0 | 18.6 | 1.1 | 3.1 | 1.8 | 2.7 | 0.2 | 3.9 | 1.7 | 1.5 | 3.2 |
| C4 | 4081 (57.8%) | 10.6 | 16.7 | 10.1 | 2.7 | 0.2 | 11.3 | 3.0 | 10.8 | 1.3 | 3.5 | 10.0 | 2.5 | 3.5 | 0.8 | 2.0 | 2.0 | 1.1 | 1.9 | 0.1 | 0.6 | 1.0 | 2.5 | 1.6 |

#### Profils numeriques K=5

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 806 (11.4%) | 4.9 | 12.9 | 6.1 | 1.2 | 0.3 | 6.6 | 3.0 | 9.2 | 2.1 | 3.1 | 5.5 | 2.2 | 3.7 | 19.9 | 1.0 | 3.1 | 1.8 | 2.8 | 0.2 | 4.0 | 1.6 | 1.4 | 3.3 |
| C2 | 1981 (28.1%) | 9.8 | 15.9 | 8.4 | 2.2 | 0.2 | 9.8 | 1.2 | 14.4 | 1.3 | 2.3 | 11.9 | 2.0 | 5.2 | 1.0 | 1.7 | 2.1 | 1.0 | 2.0 | 0.0 | 1.2 | 1.5 | 2.7 | 2.2 |
| C3 | 1460 (20.7%) | 12.0 | 17.1 | 11.1 | 3.2 | 0.2 | 12.7 | 4.4 | 9.4 | 0.6 | 3.7 | 10.1 | 2.4 | 1.2 | 0.9 | 1.7 | 1.4 | 0.9 | 1.8 | 0.1 | 0.5 | 0.8 | 2.4 | 1.4 |
| C4 | 762 (10.8%) | 9.8 | 14.9 | 9.2 | 2.7 | 0.2 | 10.7 | 1.8 | 7.9 | 11.6 | 3.4 | 9.3 | 2.0 | 3.2 | 1.1 | 2.1 | 1.9 | 1.3 | 1.6 | 0.1 | 0.5 | 1.1 | 2.1 | 1.4 |
| C5 | 2053 (29.1%) | 8.5 | 16.1 | 8.9 | 1.9 | 0.3 | 9.5 | 4.3 | 10.5 | 1.5 | 4.0 | 8.0 | 2.9 | 6.9 | 0.8 | 2.7 | 2.9 | 1.5 | 2.3 | 0.1 | 0.8 | 1.2 | 2.3 | 2.2 |

#### Profils numeriques K=6

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1660 (23.5%) | 12.7 | 16.8 | 10.8 | 3.5 | 0.2 | 13.1 | 2.2 | 10.4 | 1.8 | 3.2 | 11.7 | 2.0 | 0.7 | 0.9 | 1.5 | 1.2 | 0.9 | 1.3 | 0.0 | 0.4 | 0.9 | 2.5 | 1.2 |
| C2 | 708 (10.0%) | 8.5 | 14.7 | 8.5 | 2.2 | 0.3 | 10.0 | 4.7 | 7.7 | 7.6 | 4.3 | 7.3 | 2.5 | 3.8 | 1.0 | 4.0 | 2.7 | 1.7 | 1.5 | 0.2 | 0.7 | 1.2 | 2.5 | 2.3 |
| C3 | 1295 (18.3%) | 9.5 | 17.8 | 10.1 | 2.1 | 0.3 | 10.2 | 4.8 | 11.1 | 0.9 | 3.9 | 8.6 | 3.1 | 1.8 | 0.7 | 1.8 | 2.8 | 1.3 | 3.7 | 0.1 | 0.9 | 0.9 | 2.0 | 1.8 |
| C4 | 827 (11.7%) | 5.0 | 13.0 | 6.2 | 1.2 | 0.3 | 6.7 | 3.1 | 9.3 | 2.1 | 3.2 | 5.6 | 2.2 | 3.7 | 19.2 | 1.1 | 3.1 | 1.8 | 2.7 | 0.2 | 3.9 | 1.6 | 1.4 | 3.3 |
| C5 | 1789 (25.3%) | 9.0 | 15.5 | 8.7 | 2.1 | 0.2 | 9.6 | 2.3 | 11.3 | 1.6 | 3.2 | 9.1 | 2.5 | 10.7 | 0.7 | 2.2 | 2.2 | 1.1 | 1.5 | 0.1 | 0.7 | 1.3 | 2.6 | 1.9 |
| C6 | 783 (11.1%) | 7.8 | 14.6 | 6.6 | 1.4 | 0.3 | 7.9 | 1.9 | 15.9 | 3.9 | 1.9 | 12.1 | 1.7 | 4.4 | 2.0 | 1.7 | 2.7 | 1.3 | 2.2 | 0.1 | 1.9 | 2.1 | 2.6 | 3.2 |

#### Profils numeriques K=7

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 567 (8.0%) | 8.8 | 14.1 | 8.3 | 2.1 | 0.3 | 10.7 | 3.8 | 8.7 | 1.5 | 3.8 | 7.5 | 2.9 | 5.3 | 1.0 | 4.0 | 2.3 | 1.4 | 1.6 | 0.2 | 0.6 | 1.1 | 7.8 | 2.1 |
| C2 | 733 (10.4%) | 7.7 | 14.6 | 6.5 | 1.3 | 0.3 | 7.8 | 2.0 | 16.1 | 3.3 | 2.0 | 12.4 | 1.7 | 4.2 | 1.9 | 1.8 | 2.7 | 1.3 | 2.2 | 0.1 | 2.0 | 2.2 | 2.5 | 3.4 |
| C3 | 823 (11.7%) | 5.0 | 13.0 | 6.2 | 1.2 | 0.3 | 6.7 | 3.0 | 9.2 | 2.0 | 3.2 | 5.6 | 2.2 | 3.7 | 19.4 | 1.1 | 3.1 | 1.8 | 2.7 | 0.2 | 3.9 | 1.6 | 1.3 | 3.3 |
| C4 | 702 (9.9%) | 9.1 | 14.5 | 9.0 | 2.5 | 0.2 | 10.1 | 4.5 | 7.4 | 10.6 | 4.2 | 7.8 | 2.2 | 2.8 | 1.3 | 2.5 | 2.3 | 1.5 | 1.5 | 0.2 | 0.8 | 1.5 | 1.6 | 2.2 |
| C5 | 1189 (16.8%) | 9.5 | 18.1 | 10.2 | 2.1 | 0.3 | 10.2 | 4.9 | 11.3 | 0.6 | 3.9 | 8.7 | 3.1 | 1.9 | 0.6 | 1.8 | 2.8 | 1.3 | 3.8 | 0.1 | 0.9 | 0.8 | 1.4 | 1.7 |
| C6 | 1559 (22.1%) | 12.8 | 17.0 | 10.8 | 3.5 | 0.1 | 13.1 | 2.0 | 10.7 | 1.2 | 3.1 | 11.9 | 2.1 | 0.6 | 0.8 | 1.5 | 1.2 | 0.9 | 1.3 | 0.0 | 0.4 | 0.8 | 2.4 | 1.2 |
| C7 | 1489 (21.1%) | 9.0 | 15.8 | 8.7 | 2.0 | 0.2 | 9.4 | 2.1 | 11.9 | 1.4 | 3.1 | 9.4 | 2.4 | 11.6 | 0.6 | 2.0 | 2.2 | 1.1 | 1.5 | 0.1 | 0.7 | 1.3 | 1.6 | 1.8 |

#### Profils numeriques K=8

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 568 (8.0%) | 8.8 | 14.0 | 8.3 | 2.1 | 0.3 | 10.7 | 3.9 | 8.7 | 1.5 | 3.8 | 7.5 | 2.9 | 5.3 | 1.0 | 4.0 | 2.3 | 1.5 | 1.7 | 0.2 | 0.6 | 1.1 | 7.9 | 2.1 |
| C2 | 1173 (16.6%) | 9.5 | 18.1 | 10.2 | 2.2 | 0.3 | 10.2 | 4.9 | 11.2 | 0.6 | 3.9 | 8.7 | 3.1 | 1.9 | 0.6 | 1.8 | 2.9 | 1.3 | 3.8 | 0.1 | 0.8 | 0.8 | 1.4 | 1.7 |
| C3 | 1333 (18.9%) | 13.4 | 17.1 | 11.3 | 3.7 | 0.2 | 13.6 | 2.2 | 9.5 | 1.1 | 3.4 | 11.9 | 2.0 | 0.7 | 0.9 | 1.6 | 1.1 | 0.9 | 1.2 | 0.0 | 0.4 | 0.7 | 2.2 | 1.2 |
| C4 | 690 (9.8%) | 8.9 | 14.4 | 8.9 | 2.4 | 0.3 | 9.8 | 4.5 | 7.4 | 11.0 | 4.2 | 7.8 | 2.2 | 2.7 | 1.3 | 2.5 | 2.3 | 1.5 | 1.5 | 0.2 | 0.8 | 1.6 | 1.6 | 2.2 |
| C5 | 828 (11.7%) | 5.0 | 13.0 | 6.2 | 1.2 | 0.3 | 6.7 | 3.0 | 9.3 | 2.0 | 3.1 | 5.6 | 2.2 | 3.7 | 19.5 | 1.1 | 3.1 | 1.8 | 2.7 | 0.2 | 4.0 | 1.7 | 1.3 | 3.3 |
| C6 | 239 (3.4%) | 5.6 | 12.2 | 5.0 | 1.5 | 0.3 | 7.2 | 2.1 | 14.5 | 5.6 | 2.0 | 12.2 | 1.6 | 6.7 | 2.8 | 1.8 | 3.1 | 1.9 | 2.6 | 0.1 | 2.5 | 2.7 | 1.6 | 4.2 |
| C7 | 1476 (20.9%) | 8.9 | 15.7 | 8.7 | 2.0 | 0.2 | 9.4 | 2.1 | 11.7 | 1.4 | 3.2 | 9.4 | 2.4 | 11.6 | 0.6 | 2.0 | 2.2 | 1.1 | 1.6 | 0.1 | 0.7 | 1.4 | 1.6 | 1.9 |
| C8 | 755 (10.7%) | 9.3 | 16.5 | 7.8 | 1.7 | 0.2 | 9.1 | 1.8 | 17.3 | 1.8 | 1.6 | 12.3 | 2.1 | 2.6 | 0.9 | 1.7 | 2.4 | 0.9 | 2.0 | 0.1 | 1.3 | 1.5 | 3.1 | 2.3 |

#### Profils numeriques K=9

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 533 (7.5%) | 7.6 | 13.5 | 6.0 | 1.5 | 0.2 | 8.0 | 2.0 | 15.2 | 4.1 | 2.2 | 13.3 | 1.3 | 5.1 | 2.1 | 1.6 | 2.3 | 1.3 | 2.0 | 0.1 | 2.0 | 2.7 | 2.2 | 3.5 |
| C2 | 559 (7.9%) | 8.5 | 17.6 | 8.3 | 1.3 | 0.3 | 8.4 | 1.6 | 18.8 | 1.1 | 2.0 | 11.0 | 3.4 | 1.4 | 0.7 | 2.1 | 3.9 | 1.2 | 2.4 | 0.1 | 1.5 | 0.8 | 2.0 | 1.9 |
| C3 | 800 (11.3%) | 7.9 | 15.5 | 8.6 | 1.8 | 0.3 | 9.2 | 4.6 | 10.0 | 1.3 | 4.3 | 7.4 | 3.0 | 6.7 | 0.9 | 4.1 | 3.1 | 1.8 | 3.7 | 0.2 | 0.9 | 1.0 | 1.3 | 2.5 |
| C4 | 612 (8.7%) | 9.0 | 14.7 | 8.9 | 2.5 | 0.3 | 9.8 | 4.4 | 7.2 | 11.6 | 4.3 | 7.9 | 2.1 | 2.7 | 1.4 | 2.4 | 2.4 | 1.5 | 1.4 | 0.2 | 0.7 | 1.5 | 1.1 | 2.1 |
| C5 | 816 (11.6%) | 9.5 | 14.9 | 9.3 | 2.4 | 0.2 | 11.4 | 4.1 | 9.9 | 1.0 | 3.4 | 8.7 | 2.8 | 2.1 | 0.8 | 2.0 | 1.7 | 1.1 | 1.3 | 0.1 | 0.5 | 1.1 | 9.9 | 1.6 |
| C6 | 801 (11.3%) | 5.0 | 13.0 | 6.2 | 1.2 | 0.3 | 6.7 | 3.0 | 9.2 | 2.0 | 3.1 | 5.6 | 2.2 | 3.7 | 19.7 | 1.0 | 3.1 | 1.8 | 2.8 | 0.2 | 4.0 | 1.6 | 1.3 | 3.3 |
| C7 | 606 (8.6%) | 10.2 | 19.0 | 11.0 | 2.4 | 0.3 | 10.6 | 4.7 | 11.5 | 0.5 | 3.9 | 9.2 | 3.1 | 1.2 | 0.6 | 1.2 | 2.7 | 1.0 | 3.7 | 0.1 | 0.9 | 0.7 | 0.3 | 1.4 |
| C8 | 1031 (14.6%) | 14.2 | 17.4 | 11.4 | 3.9 | 0.1 | 14.2 | 1.9 | 9.3 | 1.3 | 3.2 | 12.2 | 1.6 | 0.4 | 0.9 | 1.5 | 0.9 | 0.9 | 1.2 | 0.0 | 0.3 | 0.7 | 1.1 | 1.3 |
| C9 | 1304 (18.5%) | 9.7 | 15.9 | 9.1 | 2.4 | 0.2 | 9.9 | 1.9 | 10.9 | 1.5 | 3.0 | 9.6 | 2.1 | 11.8 | 0.7 | 1.8 | 1.8 | 1.0 | 1.3 | 0.0 | 0.6 | 1.4 | 1.5 | 1.8 |


## ENCDM 2014 - resultats DMM 23 postes

### Structure moyenne de reference

#### Parts S1-S23

| Poste | Libelle court | Part moyenne |
| --- | --- | --- |
| S1 | S1 alimentaire 01 | 7.2% |
| S2 | S2 alimentaire 02/04/05 | 14.5% |
| S3 | S3 alimentaire 06/07/08 | 8.0% |
| S4 | S4 alimentaire 09/10 | 1.5% |
| S5 | S5 alimentaire 13/14 | 0.3% |
| S6 | S6 alimentaire mixte | 10.5% |
| S7 | S7 habillement-chaussures | 2.9% |
| S8 | S8 logement poste 31 | 15.6% |
| S9 | S9 logement/energie 32/34 | 1.8% |
| S10 | S10 ameublement-equipement | 3.0% |
| S11 | S11 logement poste 33 | 8.1% |
| S12 | S12 sante 51 | 2.7% |
| S13 | S13 sante 52/53 | 5.6% |
| S14 | S14 transport 61 | 2.8% |
| S15 | S15 transport 62 | 2.0% |
| S16 | S16 transport/communication 63 | 1.9% |
| S17 | S17 loisirs/culture 71/74 | 1.2% |
| S18 | S18 culture/enseignement 75/76/77 | 2.7% |
| S19 | S19 autres 81/84 | 0.1% |
| S20 | S20 autres 87/88 | 1.5% |
| S21 | S21 autres 85/86 | 1.7% |
| S22 | S22 autres 89 | 1.7% |
| S23 | S23 autres 91/94 | 2.5% |

#### Regroupement par familles

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

### Comparaison statistique de K=2 a K=9

| K | BIC | AIC | Entropie | Prob. max moy. | Ambigus <0.60 | Taille min | Taille max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | -3102041 | -3102402 | 0.927 | 0.979 | 1.1% | 2712 | 13258 |
| 3 | -3119511 | -3120056 | 0.832 | 0.924 | 4.5% | 2615 | 6773 |
| 4 | -3125814 | -3126543 | 0.790 | 0.884 | 8.5% | 2578 | 5652 |
| 5 | -3129060 | -3129974 | 0.791 | 0.863 | 10.1% | 1182 | 5198 |
| 6 | -3134552 | -3135650 | 0.802 | 0.860 | 10.2% | 704 | 4162 |
| 7 | -3135898 | -3137180 | 0.795 | 0.840 | 12.7% | 691 | 3636 |
| 8 | -3138433 | -3139900 | 0.790 | 0.825 | 15.2% | 623 | 3068 |
| 9 | -3141329 | -3142980 | 0.792 | 0.819 | 16.1% | 1020 | 2665 |

Lecture : ENCDM 2014 conserve des tailles de clusters relativement solides meme pour K eleve, mais l'ambiguite augmente de 10,2% a K=6 a 16,1% a K=9. K=6 isole clairement les grands comportements : alimentaire populaire, logement-energie, sante, transport tres eleve et profils diversifies. K=7 ou K=8 sont utiles pour raffiner, mais K=6 reste la meilleure base de lecture comportementale.

### Propagation comportementale des profils

En 2014, K=2 resume encore une opposition alimentaire/logement contre profils diversifies. K=3 et K=4 font ressortir logement et sante. K=5 introduit nettement le transport tres eleve. K=6 est le premier niveau ou les six profils principaux deviennent lisibles ensemble. K=7-K9 ajoutent des sous-profils culture-autres, logement S8 et sante S13, mais au prix d'une classification moins nette.

### Profils K=6 : lecture par familles

| Cluster | Taille | Libelle | Alimentaire | Habillement | Logement-energie | Ameublement-equipement | Sante | Transport-communication | Culture-enseignement | Autres depenses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4162 (26.1%) | Profil intermediaire | 43.5 | 4.3 | 22.8 | 3.6 | 9.4 | 6.4 | 3.4 | 6.6 |
| C2 | 1687 (10.6%) | Logement-energie tres eleve | 33.2 | 1.7 | 36.6 | 1.8 | 6.2 | 5.1 | 4.6 | 10.8 |
| C3 | 3069 (19.2%) | Sante detaillee elevee | 41.3 | 1.6 | 28.1 | 2.5 | 14.9 | 3.3 | 2.9 | 5.3 |
| C4 | 4041 (25.3%) | Alimentaire contraint | 52.4 | 2.7 | 26.1 | 3.2 | 3.3 | 4.0 | 2.9 | 5.5 |
| C5 | 704 (4.4%) | Autres/culture diversifies | 33.2 | 4.6 | 18.2 | 4.0 | 8.6 | 7.2 | 9.7 | 14.6 |
| C6 | 2307 (14.4%) | Transport tres eleve | 32.0 | 3.0 | 19.9 | 2.8 | 7.4 | 18.2 | 5.3 | 11.4 |

### Profils K=6 : signatures fines S1-S23

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 4162 (26.1%) | Profil intermediaire | S2 15.0%, S8 13.6%, S6 10.8%, S3 8.6%, S11 7.5% | S15 +1.6 pp, S7 +1.4 pp, S3 +0.6 pp, S13 +0.6 pp | S14 -2.2 pp, S8 -1.9 pp, S11 -0.6 pp |
| C2 | 1687 (10.6%) | Logement-energie tres eleve | S8 22.2%, S2 11.9%, S11 10.5%, S6 9.1%, S1 6.1% | S8 +6.7 pp, S11 +2.4 pp, S9 +2.1 pp, S23 +1.7 pp | S3 -3.4 pp, S2 -2.7 pp, S6 -1.4 pp |
| C3 | 3069 (19.2%) | Sante detaillee elevee | S8 17.6%, S2 14.3%, S13 12.5%, S6 9.8%, S11 9.0% | S13 +7.0 pp, S8 +2.0 pp, S11 +0.9 pp | S14 -2.3 pp, S7 -1.3 pp, S23 -0.9 pp |
| C4 | 4041 (25.3%) | Alimentaire contraint | S2 17.0%, S8 15.5%, S6 13.5%, S3 10.2%, S11 9.4% | S6 +3.0 pp, S2 +2.5 pp, S3 +2.2 pp, S1 +2.0 pp | S13 -5.1 pp, S14 -2.2 pp, S23 -0.9 pp |
| C5 | 704 (4.4%) | Autres/culture diversifies | S2 13.1%, S8 11.7%, S6 7.4%, S3 6.5%, S18 6.3% | S18 +3.6 pp, S21 +3.5 pp, S17 +2.2 pp, S23 +2.1 pp | S8 -3.9 pp, S11 -3.4 pp, S6 -3.1 pp |
| C6 | 2307 (14.4%) | Transport tres eleve | S14 14.6%, S8 12.9%, S2 12.0%, S6 7.7%, S3 6.1% | S14 +11.8 pp, S20 +2.5 pp, S23 +1.5 pp, S18 +0.9 pp | S11 -3.1 pp, S6 -2.8 pp, S8 -2.7 pp |

### Caracterisation socio-economique K=6

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4162 | 69845 | 62364 | -7.0% | 62.4% | 37.6% | Q4 (27.2%) |
| C2 | 1687 | 63565 | 42184 | -15.3% | 69.7% | 30.3% | Q1 (43.4%) |
| C3 | 3069 | 58296 | 50735 | -22.3% | 68.5% | 31.5% | Q2 (25.6%) |
| C4 | 4041 | 49410 | 44908 | -34.2% | 53.0% | 47.0% | Q1 (31.9%) |
| C5 | 704 | 150204 | 124537 | +100.1% | 88.6% | 11.4% | Q5 (65.2%) |
| C6 | 2307 | 137230 | 114822 | +82.8% | 75.3% | 24.7% | Q5 (59.4%) |

### Parametres de Dirichlet K=6

`pi` donne le poids du cluster dans le melange. `alpha_sum` indique la concentration du profil : plus elle est elevee, plus la composante est homogene autour de son profil moyen theorique.

| Cluster | pi | alpha_sum | Profil theorique dominant |
| --- | --- | --- | --- |
| C1 | 0.243 | 27.0 | S2=15.4%, S8=12.8%, S6=11.1%, S3=9.2%, S11=8.3% |
| C2 | 0.116 | 9.3 | S8=21.2%, S2=13.6%, S11=12.2%, S6=8.8%, S1=8.6% |
| C3 | 0.195 | 20.4 | S8=16.4%, S2=15.1%, S13=11.0%, S6=10.5%, S11=9.9% |
| C4 | 0.264 | 21.8 | S2=17.4%, S8=14.6%, S6=13.7%, S3=10.9%, S11=10.2% |
| C5 | 0.043 | 27.6 | S2=13.5%, S8=11.6%, S6=8.0%, S3=7.1%, S11=5.7% |
| C6 | 0.139 | 21.0 | S14=13.5%, S2=12.8%, S8=12.3%, S6=8.3%, S3=7.0% |

### Diagnostics socio-economiques globaux

| K | Cramer Milieu | Cramer quintile_DAM | eta2 DAM | eta2 log_DAM | Associations qualitatives dominantes |
| --- | --- | --- | --- | --- | --- |
| 2 | 0.115 | 0.497 | 0.247 | 0.239 | quintile_DAM=0.497 ; Deciles=0.367 ; Decileurbain=0.358 ; Quintileurbain=0.341 ; Quintiles=0.339 |
| 3 | 0.132 | 0.410 | 0.270 | 0.298 | quintile_DAM=0.410 ; Deciles=0.293 ; Decileurbain=0.279 ; Quintiles=0.271 ; Quintileurbain=0.262 |
| 4 | 0.168 | 0.342 | 0.265 | 0.299 | quintile_DAM=0.342 ; Deciles=0.249 ; Decileurbain=0.239 ; Quintiles=0.231 ; Quintileurbain=0.226 |
| 5 | 0.155 | 0.297 | 0.263 | 0.296 | quintile_DAM=0.297 ; Deciles=0.209 ; Diplôme_agregé_CM=0.209 ; Decileurbain=0.200 ; Quintiles=0.191 |
| 6 | 0.190 | 0.304 | 0.270 | 0.305 | quintile_DAM=0.304 ; Diplôme_agregé_CM=0.228 ; Quintiles=0.209 ; Deciles=0.201 ; Decileurbain=0.193 |
| 7 | 0.211 | 0.312 | 0.270 | 0.320 | quintile_DAM=0.312 ; Diplôme_agregé_CM=0.229 ; Quintiles=0.217 ; Milieu=0.211 ; Quintileurbain=0.193 |
| 8 | 0.230 | 0.313 | 0.304 | 0.323 | quintile_DAM=0.313 ; Diplôme_agregé_CM=0.233 ; Milieu=0.230 ; Quintiles=0.208 ; Quintileurbain=0.199 |
| 9 | 0.236 | 0.318 | 0.288 | 0.334 | quintile_DAM=0.318 ; Milieu=0.236 ; Diplôme_agregé_CM=0.232 ; Quintiles=0.210 ; Quintileurbain=0.201 |

### Annexe : signatures des profils pour tous les K

#### K=2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 13258 (83.0%) | Logement poste S8 eleve | S8 16.2%, S2 15.1%, S6 11.1%, S11 8.8%, S3 8.4% | S11 +0.6 pp, S8 +0.6 pp, S6 +0.6 pp, S2 +0.5 pp | S14 -2.0 pp, S20 -0.5 pp |
| C2 | 2712 (17.0%) | Transport tres eleve | S14 12.7%, S8 12.5%, S2 12.0%, S6 7.6%, S13 6.1% | S14 +9.9 pp, S20 +2.3 pp, S23 +1.6 pp, S18 +1.3 pp | S11 -3.1 pp, S8 -3.1 pp, S6 -2.9 pp |

#### K=3

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 2615 (16.4%) | Transport tres eleve | S14 13.5%, S8 12.8%, S2 11.8%, S6 7.5%, S3 5.9% | S14 +10.7 pp, S20 +2.4 pp, S23 +1.7 pp, S18 +1.4 pp | S11 -3.2 pp, S6 -3.0 pp, S8 -2.8 pp |
| C2 | 6773 (42.4%) | Logement poste S8 eleve | S8 18.1%, S2 14.9%, S6 11.6%, S11 9.8%, S3 8.2% | S8 +2.5 pp, S11 +1.7 pp, S6 +1.1 pp, S1 +0.9 pp | S14 -1.9 pp, S13 -1.5 pp, S7 -1.1 pp |
| C3 | 6582 (41.2%) | Profil intermediaire | S2 15.3%, S8 14.1%, S6 10.6%, S3 8.7%, S11 7.6% | S13 +1.6 pp, S7 +1.1 pp, S2 +0.7 pp, S3 +0.7 pp | S14 -2.3 pp, S8 -1.5 pp, S20 -0.5 pp |

#### K=4

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 4855 (30.4%) | Logement poste S8 eleve | S8 19.6%, S2 14.0%, S6 10.7%, S11 10.1%, S1 7.7% | S8 +4.1 pp, S11 +2.0 pp, S9 +0.5 pp, S1 +0.5 pp | S7 -1.9 pp, S14 -1.7 pp, S10 -0.9 pp |
| C2 | 5652 (35.4%) | Profil intermediaire | S2 14.7%, S8 14.1%, S6 10.1%, S13 8.3%, S3 8.3% | S13 +2.8 pp, S7 +1.0 pp, S15 +0.7 pp, S10 +0.5 pp | S14 -2.3 pp, S8 -1.4 pp, S11 -0.6 pp |
| C3 | 2578 (16.1%) | Transport tres eleve | S14 13.5%, S8 12.6%, S2 11.9%, S6 7.5%, S3 6.0% | S14 +10.7 pp, S20 +2.4 pp, S23 +1.6 pp, S18 +1.4 pp | S11 -3.2 pp, S6 -3.0 pp, S8 -2.9 pp |
| C4 | 2885 (18.1%) | Alimentaire contraint | S2 17.4%, S8 14.2%, S6 13.7%, S3 10.6%, S1 9.2% | S6 +3.2 pp, S2 +2.8 pp, S3 +2.6 pp, S1 +2.0 pp | S13 -5.0 pp, S14 -2.2 pp, S8 -1.4 pp |

#### K=5

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 3224 (20.2%) | Logement-energie tres eleve | S8 20.6%, S2 13.7%, S6 10.8%, S11 10.5%, S1 7.6% | S8 +5.0 pp, S11 +2.4 pp, S9 +0.9 pp, S23 +0.5 pp | S13 -2.0 pp, S7 -1.7 pp, S14 -1.3 pp |
| C2 | 5198 (32.5%) | Sante detaillee elevee | S8 15.6%, S2 14.6%, S13 10.6%, S6 10.1%, S11 8.3% | S13 +5.0 pp | S14 -2.3 pp, S21 -0.6 pp, S23 -0.6 pp |
| C3 | 1182 (7.4%) | Profil intermediaire | S2 14.1%, S8 12.2%, S6 9.2%, S3 7.9%, S1 6.2% | S21 +3.2 pp, S7 +1.8 pp, S18 +1.5 pp, S15 +1.3 pp | S8 -3.4 pp, S14 -2.1 pp, S11 -1.9 pp |
| C4 | 3851 (24.1%) | Alimentaire contraint | S2 17.0%, S8 14.2%, S6 13.1%, S3 10.1%, S1 8.7% | S6 +2.6 pp, S2 +2.4 pp, S3 +2.1 pp, S1 +1.5 pp | S13 -4.7 pp, S14 -2.2 pp, S8 -1.3 pp |
| C5 | 2515 (15.7%) | Transport tres eleve | S14 13.7%, S8 12.6%, S2 11.9%, S6 7.6%, S3 6.0% | S14 +10.8 pp, S20 +2.4 pp, S23 +1.6 pp, S18 +1.3 pp | S11 -3.2 pp, S8 -2.9 pp, S6 -2.9 pp |

#### K=6

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 4162 (26.1%) | Profil intermediaire | S2 15.0%, S8 13.6%, S6 10.8%, S3 8.6%, S11 7.5% | S15 +1.6 pp, S7 +1.4 pp, S3 +0.6 pp, S13 +0.6 pp | S14 -2.2 pp, S8 -1.9 pp, S11 -0.6 pp |
| C2 | 1687 (10.6%) | Logement-energie tres eleve | S8 22.2%, S2 11.9%, S11 10.5%, S6 9.1%, S1 6.1% | S8 +6.7 pp, S11 +2.4 pp, S9 +2.1 pp, S23 +1.7 pp | S3 -3.4 pp, S2 -2.7 pp, S6 -1.4 pp |
| C3 | 3069 (19.2%) | Sante detaillee elevee | S8 17.6%, S2 14.3%, S13 12.5%, S6 9.8%, S11 9.0% | S13 +7.0 pp, S8 +2.0 pp, S11 +0.9 pp | S14 -2.3 pp, S7 -1.3 pp, S23 -0.9 pp |
| C4 | 4041 (25.3%) | Alimentaire contraint | S2 17.0%, S8 15.5%, S6 13.5%, S3 10.2%, S11 9.4% | S6 +3.0 pp, S2 +2.5 pp, S3 +2.2 pp, S1 +2.0 pp | S13 -5.1 pp, S14 -2.2 pp, S23 -0.9 pp |
| C5 | 704 (4.4%) | Autres/culture diversifies | S2 13.1%, S8 11.7%, S6 7.4%, S3 6.5%, S18 6.3% | S18 +3.6 pp, S21 +3.5 pp, S17 +2.2 pp, S23 +2.1 pp | S8 -3.9 pp, S11 -3.4 pp, S6 -3.1 pp |
| C6 | 2307 (14.4%) | Transport tres eleve | S14 14.6%, S8 12.9%, S2 12.0%, S6 7.7%, S3 6.1% | S14 +11.8 pp, S20 +2.5 pp, S23 +1.5 pp, S18 +0.9 pp | S11 -3.1 pp, S6 -2.8 pp, S8 -2.7 pp |

#### K=7

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 691 (4.3%) | Autres/culture diversifies | S2 13.2%, S8 11.9%, S6 7.6%, S3 6.5%, S18 6.1% | S18 +3.5 pp, S21 +3.2 pp, S17 +2.2 pp, S23 +1.9 pp | S8 -3.6 pp, S11 -3.3 pp, S6 -2.9 pp |
| C2 | 2267 (14.2%) | Transport tres eleve | S14 14.9%, S8 13.0%, S2 12.0%, S6 7.7%, S3 6.1% | S14 +12.0 pp, S20 +2.5 pp, S23 +1.5 pp, S18 +0.9 pp | S11 -3.1 pp, S6 -2.8 pp, S8 -2.6 pp |
| C3 | 3636 (22.8%) | Sante detaillee elevee | S8 17.3%, S2 14.2%, S13 12.8%, S6 9.7%, S11 8.6% | S13 +7.2 pp, S8 +1.7 pp, S11 +0.5 pp | S14 -2.3 pp, S9 -1.2 pp, S7 -0.8 pp |
| C4 | 1469 (9.2%) | Profil intermediaire | S2 14.5%, S8 10.9%, S6 9.8%, S9 8.4%, S3 8.3% | S9 +6.6 pp, S7 +1.2 pp, S10 +0.9 pp, S13 +0.9 pp | S8 -4.7 pp, S14 -2.0 pp, S11 -1.3 pp |
| C5 | 2978 (18.6%) | Alimentaire contraint | S2 17.4%, S8 16.4%, S6 14.0%, S3 10.5%, S11 10.2% | S6 +3.5 pp, S2 +2.8 pp, S1 +2.6 pp, S3 +2.5 pp | S13 -4.8 pp, S14 -2.1 pp, S23 -1.1 pp |
| C6 | 3321 (20.8%) | Profil intermediaire | S2 15.8%, S8 14.1%, S6 12.0%, S3 9.4%, S11 8.0% | S15 +1.9 pp, S7 +1.6 pp, S6 +1.5 pp, S3 +1.4 pp | S13 -3.3 pp, S14 -2.3 pp, S8 -1.5 pp |
| C7 | 1608 (10.1%) | Logement-energie tres eleve | S8 22.8%, S2 11.5%, S11 10.3%, S6 8.8%, S1 5.8% | S8 +7.2 pp, S11 +2.2 pp, S23 +1.9 pp, S9 +1.3 pp | S3 -3.7 pp, S2 -3.0 pp, S6 -1.7 pp |

#### K=8

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 623 (3.9%) | Diversifie transport/autres | S8 11.5%, S2 11.3%, S14 9.7%, S18 6.9%, S6 6.8% | S14 +6.9 pp, S18 +4.2 pp, S21 +2.7 pp, S23 +2.7 pp | S11 -4.1 pp, S8 -4.1 pp, S6 -3.7 pp |
| C2 | 1994 (12.5%) | Transport tres eleve | S14 15.1%, S8 13.2%, S2 12.2%, S6 7.8%, S3 6.3% | S14 +12.3 pp, S20 +2.6 pp, S23 +1.3 pp, S16 +0.5 pp | S11 -2.9 pp, S6 -2.7 pp, S8 -2.4 pp |
| C3 | 1834 (11.5%) | Alimentaire contraint | S2 18.0%, S6 14.5%, S8 13.3%, S3 11.2%, S1 9.6% | S6 +4.0 pp, S2 +3.4 pp, S3 +3.1 pp, S1 +2.4 pp | S13 -4.8 pp, S8 -2.2 pp, S14 -2.2 pp |
| C4 | 3068 (19.2%) | Logement poste S8 eleve | S8 15.5%, S2 15.1%, S6 9.7%, S3 8.4%, S11 7.5% | S18 +2.2 pp, S7 +1.4 pp, S12 +0.6 pp, S2 +0.6 pp | S14 -2.3 pp, S9 -1.1 pp, S6 -0.8 pp |
| C5 | 1217 (7.6%) | Profil intermediaire | S2 14.1%, S8 10.1%, S6 10.1%, S3 8.2%, S9 7.5% | S9 +5.7 pp, S15 +1.6 pp, S7 +1.4 pp, S10 +1.0 pp | S8 -5.4 pp, S14 -1.9 pp, S11 -1.4 pp |
| C6 | 1937 (12.1%) | Logement poste S8 eleve | S2 15.8%, S8 15.7%, S6 12.7%, S3 9.3%, S11 8.7% | S15 +2.8 pp, S6 +2.2 pp, S3 +1.3 pp, S2 +1.3 pp | S13 -4.5 pp, S14 -2.4 pp, S18 -1.3 pp |
| C7 | 2845 (17.8%) | Sante detaillee elevee | S8 16.8%, S2 14.4%, S13 13.7%, S6 10.2%, S11 8.9% | S13 +8.1 pp, S8 +1.2 pp, S11 +0.8 pp | S14 -2.3 pp, S18 -1.5 pp, S7 -1.3 pp |
| C8 | 2452 (15.4%) | Logement-energie tres eleve | S8 21.5%, S2 13.4%, S11 10.9%, S6 10.4%, S1 7.3% | S8 +5.9 pp, S11 +2.7 pp, S9 +1.0 pp, S23 +0.9 pp | S13 -2.3 pp, S3 -1.8 pp, S14 -1.7 pp |

#### K=9

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1264 (7.9%) | Diversifie transport/autres | S8 12.5%, S2 11.8%, S14 11.5%, S18 6.9%, S6 6.9% | S14 +8.7 pp, S18 +4.3 pp, S20 +2.5 pp, S23 +1.9 pp | S6 -3.6 pp, S11 -3.6 pp, S8 -3.1 pp |
| C2 | 1074 (6.7%) | Profil intermediaire | S2 14.4%, S6 10.5%, S8 10.3%, S3 8.4%, S9 7.8% | S9 +6.0 pp, S15 +1.6 pp, S7 +1.2 pp, S13 +0.9 pp | S8 -5.3 pp, S14 -1.8 pp, S18 -1.2 pp |
| C3 | 1830 (11.5%) | Alimentaire contraint | S2 17.9%, S6 14.6%, S8 13.1%, S3 11.2%, S1 9.6% | S6 +4.1 pp, S2 +3.4 pp, S3 +3.2 pp, S1 +2.4 pp | S13 -4.8 pp, S8 -2.4 pp, S14 -2.2 pp |
| C4 | 2665 (16.7%) | Sante detaillee elevee | S8 17.1%, S2 14.4%, S13 14.2%, S6 10.2%, S11 9.0% | S13 +8.6 pp, S8 +1.5 pp, S11 +0.9 pp | S14 -2.2 pp, S7 -1.4 pp, S18 -1.4 pp |
| C5 | 2650 (16.6%) | Logement poste S8 eleve | S8 16.1%, S2 15.4%, S6 9.9%, S3 8.6%, S11 7.7% | S18 +2.3 pp, S7 +1.3 pp, S2 +0.9 pp, S12 +0.6 pp | S14 -2.4 pp, S9 -1.2 pp, S21 -1.0 pp |
| C6 | 1340 (8.4%) | Transport tres eleve | S14 16.5%, S8 13.5%, S2 12.3%, S6 8.4%, S3 6.5% | S14 +13.7 pp, S20 +2.5 pp, S23 +1.2 pp, S16 +0.4 pp | S11 -2.5 pp, S2 -2.3 pp, S6 -2.1 pp |
| C7 | 1020 (6.4%) | Autres/culture diversifies | S2 13.4%, S21 11.4%, S8 11.1%, S6 8.7%, S3 7.1% | S21 +9.7 pp, S7 +1.4 pp, S10 +1.4 pp, S17 +1.0 pp | S8 -4.5 pp, S11 -2.2 pp, S14 -1.8 pp |
| C8 | 1808 (11.3%) | Logement poste S8 eleve | S8 16.1%, S2 15.8%, S6 12.8%, S3 9.3%, S11 8.9% | S15 +2.9 pp, S6 +2.3 pp, S2 +1.3 pp, S3 +1.3 pp | S13 -4.5 pp, S14 -2.5 pp, S18 -1.2 pp |
| C9 | 2319 (14.5%) | Logement-energie tres eleve | S8 22.0%, S2 13.5%, S11 11.1%, S6 10.5%, S1 7.4% | S8 +6.4 pp, S11 +3.0 pp, S9 +1.0 pp, S23 +0.9 pp | S13 -2.3 pp, S14 -2.0 pp, S3 -1.8 pp |

### Annexe : profils numeriques complets pour tous les K

Les valeurs sont exprimees en pourcentage de la depense totale du menage dans le cluster.

#### Profils numeriques K=2

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 13258 (83.0%) | 7.7 | 15.1 | 8.4 | 1.6 | 0.3 | 11.1 | 2.9 | 16.2 | 1.8 | 3.0 | 8.8 | 2.7 | 5.5 | 0.8 | 2.2 | 1.8 | 1.1 | 2.4 | 0.1 | 1.1 | 1.6 | 1.8 | 2.2 |
| C2 | 2712 (17.0%) | 4.7 | 12.0 | 6.1 | 1.1 | 0.4 | 7.6 | 3.3 | 12.5 | 1.9 | 2.9 | 5.0 | 2.6 | 6.1 | 12.7 | 1.2 | 2.5 | 1.9 | 4.0 | 0.2 | 3.8 | 2.4 | 1.0 | 4.1 |

#### Profils numeriques K=3

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2615 (16.4%) | 4.6 | 11.8 | 5.9 | 1.0 | 0.4 | 7.5 | 3.2 | 12.8 | 1.9 | 2.9 | 4.9 | 2.5 | 5.4 | 13.5 | 1.1 | 2.5 | 2.0 | 4.1 | 0.2 | 4.0 | 2.4 | 1.1 | 4.2 |
| C2 | 6773 (42.4%) | 8.1 | 14.9 | 8.2 | 1.7 | 0.3 | 11.6 | 1.8 | 18.1 | 2.0 | 2.5 | 9.8 | 2.3 | 4.1 | 1.0 | 1.9 | 1.6 | 0.9 | 2.3 | 0.1 | 1.1 | 1.5 | 1.9 | 2.3 |
| C3 | 6582 (41.2%) | 7.3 | 15.3 | 8.7 | 1.5 | 0.3 | 10.6 | 4.0 | 14.1 | 1.5 | 3.6 | 7.6 | 3.0 | 7.2 | 0.5 | 2.5 | 2.0 | 1.2 | 2.5 | 0.2 | 1.1 | 1.6 | 1.6 | 2.1 |

#### Profils numeriques K=4

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4855 (30.4%) | 7.7 | 14.0 | 7.3 | 1.6 | 0.3 | 10.7 | 1.0 | 19.6 | 2.3 | 2.2 | 10.1 | 2.2 | 5.6 | 1.2 | 1.8 | 1.6 | 0.9 | 2.4 | 0.1 | 1.2 | 1.7 | 2.0 | 2.6 |
| C2 | 5652 (35.4%) | 7.0 | 14.7 | 8.3 | 1.4 | 0.3 | 10.1 | 3.9 | 14.1 | 1.6 | 3.5 | 7.5 | 3.0 | 8.3 | 0.5 | 2.7 | 2.1 | 1.3 | 2.5 | 0.2 | 1.2 | 1.7 | 1.6 | 2.2 |
| C3 | 2578 (16.1%) | 4.6 | 11.9 | 6.0 | 1.1 | 0.4 | 7.5 | 3.2 | 12.6 | 1.9 | 3.0 | 4.9 | 2.5 | 5.2 | 13.5 | 1.1 | 2.5 | 2.0 | 4.1 | 0.2 | 4.0 | 2.4 | 1.1 | 4.1 |
| C4 | 2885 (18.1%) | 9.2 | 17.4 | 10.6 | 2.1 | 0.3 | 13.7 | 3.9 | 14.2 | 1.1 | 3.5 | 8.8 | 2.9 | 0.6 | 0.7 | 1.9 | 1.5 | 0.8 | 2.1 | 0.1 | 0.7 | 1.0 | 1.7 | 1.5 |

#### Profils numeriques K=5

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 3224 (20.2%) | 7.6 | 13.7 | 6.8 | 1.6 | 0.3 | 10.8 | 1.2 | 20.6 | 2.7 | 2.0 | 10.5 | 1.9 | 3.6 | 1.5 | 1.7 | 1.5 | 1.1 | 2.5 | 0.1 | 1.3 | 1.9 | 2.1 | 3.0 |
| C2 | 5198 (32.5%) | 7.3 | 14.6 | 8.2 | 1.5 | 0.3 | 10.1 | 2.5 | 15.6 | 1.6 | 3.0 | 8.3 | 2.8 | 10.6 | 0.5 | 2.2 | 1.9 | 1.0 | 2.1 | 0.1 | 1.1 | 1.1 | 1.6 | 2.0 |
| C3 | 1182 (7.4%) | 6.2 | 14.1 | 7.9 | 1.3 | 0.4 | 9.2 | 4.8 | 12.2 | 1.8 | 4.0 | 6.2 | 3.2 | 5.5 | 0.8 | 3.4 | 2.2 | 2.0 | 4.1 | 0.3 | 1.4 | 5.0 | 1.5 | 2.6 |
| C4 | 3851 (24.1%) | 8.7 | 17.0 | 10.1 | 1.9 | 0.3 | 13.1 | 4.2 | 14.2 | 1.2 | 3.6 | 8.5 | 3.0 | 0.8 | 0.6 | 2.2 | 1.8 | 0.9 | 2.2 | 0.1 | 0.8 | 1.0 | 1.8 | 1.8 |
| C5 | 2515 (15.7%) | 4.7 | 11.9 | 6.0 | 1.1 | 0.4 | 7.6 | 3.3 | 12.6 | 1.9 | 3.0 | 4.9 | 2.5 | 5.2 | 13.7 | 1.1 | 2.5 | 2.0 | 4.0 | 0.2 | 4.0 | 2.3 | 1.1 | 4.1 |

#### Profils numeriques K=6

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4162 (26.1%) | 7.2 | 15.0 | 8.6 | 1.5 | 0.3 | 10.8 | 4.3 | 13.6 | 1.6 | 3.6 | 7.5 | 3.1 | 6.2 | 0.6 | 3.7 | 2.2 | 1.2 | 2.2 | 0.2 | 1.0 | 1.5 | 1.8 | 2.2 |
| C2 | 1687 (10.6%) | 6.1 | 11.9 | 4.7 | 1.1 | 0.3 | 9.1 | 1.7 | 22.2 | 3.9 | 1.8 | 10.5 | 1.8 | 4.5 | 1.7 | 1.7 | 1.7 | 1.6 | 3.0 | 0.1 | 1.6 | 2.8 | 2.1 | 4.2 |
| C3 | 3069 (19.2%) | 7.5 | 14.3 | 7.9 | 1.5 | 0.3 | 9.8 | 1.6 | 17.6 | 1.5 | 2.5 | 9.0 | 2.4 | 12.5 | 0.6 | 1.2 | 1.5 | 0.7 | 2.3 | 0.1 | 1.0 | 1.2 | 1.5 | 1.7 |
| C4 | 4041 (25.3%) | 9.2 | 17.0 | 10.2 | 2.1 | 0.3 | 13.5 | 2.7 | 15.5 | 1.2 | 3.2 | 9.4 | 2.8 | 0.5 | 0.7 | 1.7 | 1.6 | 0.8 | 2.1 | 0.1 | 0.8 | 1.2 | 1.9 | 1.6 |
| C5 | 704 (4.4%) | 4.7 | 13.1 | 6.5 | 1.0 | 0.5 | 7.4 | 4.6 | 11.7 | 1.8 | 4.0 | 4.7 | 3.1 | 5.5 | 2.7 | 1.8 | 2.7 | 3.4 | 6.3 | 0.5 | 3.3 | 5.2 | 1.0 | 4.6 |
| C6 | 2307 (14.4%) | 4.8 | 12.0 | 6.1 | 1.1 | 0.4 | 7.7 | 3.0 | 12.9 | 2.0 | 2.8 | 5.0 | 2.5 | 4.9 | 14.6 | 1.1 | 2.5 | 1.8 | 3.5 | 0.2 | 4.0 | 2.0 | 1.1 | 4.0 |

#### Profils numeriques K=7

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 691 (4.3%) | 4.8 | 13.2 | 6.5 | 1.0 | 0.5 | 7.6 | 4.6 | 11.9 | 1.3 | 4.0 | 4.8 | 3.2 | 5.6 | 2.6 | 2.1 | 2.7 | 3.4 | 6.1 | 0.4 | 3.4 | 4.9 | 1.1 | 4.4 |
| C2 | 2267 (14.2%) | 4.8 | 12.0 | 6.1 | 1.1 | 0.4 | 7.7 | 3.0 | 13.0 | 1.6 | 2.8 | 5.0 | 2.5 | 4.8 | 14.9 | 1.0 | 2.5 | 1.8 | 3.6 | 0.2 | 4.1 | 2.1 | 1.1 | 4.1 |
| C3 | 3636 (22.8%) | 7.3 | 14.2 | 7.8 | 1.4 | 0.3 | 9.7 | 2.1 | 17.3 | 0.6 | 2.7 | 8.6 | 2.7 | 12.8 | 0.5 | 1.7 | 1.7 | 0.8 | 2.2 | 0.1 | 1.0 | 1.2 | 1.5 | 1.8 |
| C4 | 1469 (9.2%) | 6.5 | 14.5 | 8.3 | 1.5 | 0.4 | 9.8 | 4.1 | 10.9 | 8.4 | 3.9 | 6.9 | 2.7 | 6.5 | 0.8 | 2.1 | 1.9 | 1.2 | 2.2 | 0.2 | 0.9 | 2.1 | 1.8 | 2.5 |
| C5 | 2978 (18.6%) | 9.8 | 17.4 | 10.5 | 2.2 | 0.3 | 14.0 | 1.8 | 16.4 | 0.9 | 2.9 | 10.2 | 2.4 | 0.8 | 0.7 | 1.1 | 1.2 | 0.6 | 2.0 | 0.0 | 0.7 | 0.9 | 1.8 | 1.4 |
| C6 | 3321 (20.8%) | 7.9 | 15.8 | 9.4 | 1.7 | 0.4 | 12.0 | 4.5 | 14.1 | 0.6 | 3.6 | 8.0 | 3.3 | 2.2 | 0.6 | 4.0 | 2.2 | 1.1 | 2.3 | 0.2 | 1.0 | 1.3 | 1.9 | 1.9 |
| C7 | 1608 (10.1%) | 5.8 | 11.5 | 4.3 | 1.1 | 0.3 | 8.8 | 1.7 | 22.8 | 3.1 | 1.7 | 10.3 | 1.8 | 5.4 | 1.6 | 1.7 | 1.8 | 1.6 | 3.2 | 0.1 | 1.8 | 2.9 | 2.1 | 4.4 |

#### Profils numeriques K=8

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 623 (3.9%) | 4.0 | 11.3 | 5.4 | 0.9 | 0.4 | 6.8 | 4.1 | 11.5 | 1.7 | 3.4 | 4.0 | 2.7 | 5.2 | 9.7 | 1.0 | 2.8 | 3.4 | 6.9 | 0.4 | 3.8 | 4.5 | 0.9 | 5.2 |
| C2 | 1994 (12.5%) | 4.9 | 12.2 | 6.3 | 1.1 | 0.4 | 7.8 | 2.9 | 13.2 | 1.7 | 2.8 | 5.3 | 2.4 | 4.8 | 15.1 | 1.1 | 2.4 | 1.6 | 3.1 | 0.2 | 4.1 | 1.8 | 1.1 | 3.8 |
| C3 | 1834 (11.5%) | 9.6 | 18.0 | 11.2 | 2.2 | 0.3 | 14.5 | 4.1 | 13.3 | 1.0 | 3.7 | 9.1 | 2.6 | 0.8 | 0.6 | 0.8 | 1.2 | 0.6 | 1.6 | 0.1 | 0.6 | 1.0 | 1.6 | 1.5 |
| C4 | 3068 (19.2%) | 7.2 | 15.1 | 8.4 | 1.4 | 0.3 | 9.7 | 4.3 | 15.5 | 0.7 | 3.4 | 7.5 | 3.3 | 5.8 | 0.5 | 2.1 | 2.2 | 1.3 | 4.9 | 0.1 | 1.2 | 1.5 | 1.5 | 2.1 |
| C5 | 1217 (7.6%) | 6.3 | 14.1 | 8.2 | 1.5 | 0.4 | 10.1 | 4.3 | 10.1 | 7.5 | 4.0 | 6.7 | 2.8 | 6.5 | 0.9 | 3.6 | 2.1 | 1.5 | 1.4 | 0.2 | 1.0 | 2.3 | 1.9 | 2.5 |
| C6 | 1937 (12.1%) | 8.3 | 15.8 | 9.3 | 1.8 | 0.3 | 12.7 | 2.4 | 15.7 | 0.8 | 3.1 | 8.7 | 3.3 | 1.1 | 0.5 | 4.8 | 2.3 | 1.0 | 1.4 | 0.2 | 1.0 | 1.3 | 2.4 | 1.9 |
| C7 | 2845 (17.8%) | 7.5 | 14.4 | 8.0 | 1.6 | 0.3 | 10.2 | 1.6 | 16.8 | 1.0 | 2.6 | 8.9 | 2.4 | 13.7 | 0.6 | 1.6 | 1.6 | 0.7 | 1.2 | 0.1 | 1.0 | 1.2 | 1.4 | 1.7 |
| C8 | 2452 (15.4%) | 7.3 | 13.4 | 6.2 | 1.5 | 0.3 | 10.4 | 1.4 | 21.5 | 2.8 | 2.0 | 10.9 | 1.9 | 3.3 | 1.1 | 1.4 | 1.5 | 1.2 | 2.6 | 0.1 | 1.3 | 2.4 | 2.1 | 3.4 |

#### Profils numeriques K=9

| Cluster | Taille | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1264 (7.9%) | 4.4 | 11.8 | 5.7 | 1.0 | 0.4 | 6.9 | 3.7 | 12.5 | 1.6 | 2.9 | 4.5 | 2.6 | 5.9 | 11.5 | 1.1 | 2.6 | 2.4 | 6.9 | 0.2 | 4.0 | 2.1 | 0.8 | 4.4 |
| C2 | 1074 (6.7%) | 6.6 | 14.4 | 8.4 | 1.6 | 0.4 | 10.5 | 4.2 | 10.3 | 7.8 | 3.9 | 6.9 | 2.8 | 6.4 | 1.0 | 3.6 | 2.1 | 1.4 | 1.5 | 0.2 | 1.0 | 0.8 | 1.9 | 2.4 |
| C3 | 1830 (11.5%) | 9.6 | 17.9 | 11.2 | 2.3 | 0.3 | 14.6 | 4.1 | 13.1 | 1.1 | 3.7 | 9.1 | 2.5 | 0.7 | 0.6 | 0.9 | 1.2 | 0.6 | 1.6 | 0.1 | 0.6 | 0.8 | 1.6 | 1.6 |
| C4 | 2665 (16.7%) | 7.6 | 14.4 | 8.0 | 1.6 | 0.3 | 10.2 | 1.5 | 17.1 | 1.0 | 2.5 | 9.0 | 2.4 | 14.2 | 0.6 | 1.6 | 1.6 | 0.6 | 1.3 | 0.0 | 1.0 | 0.5 | 1.4 | 1.7 |
| C5 | 2650 (16.6%) | 7.5 | 15.4 | 8.6 | 1.4 | 0.3 | 9.9 | 4.2 | 16.1 | 0.6 | 3.3 | 7.7 | 3.3 | 5.6 | 0.4 | 2.0 | 2.2 | 1.1 | 4.9 | 0.1 | 1.1 | 0.7 | 1.5 | 1.9 |
| C6 | 1340 (8.4%) | 5.1 | 12.3 | 6.5 | 1.2 | 0.4 | 8.4 | 2.4 | 13.5 | 1.9 | 2.7 | 5.6 | 2.4 | 3.8 | 16.5 | 1.0 | 2.3 | 1.5 | 1.6 | 0.1 | 4.1 | 1.7 | 1.4 | 3.7 |
| C7 | 1020 (6.4%) | 5.5 | 13.4 | 7.1 | 1.1 | 0.4 | 8.7 | 4.4 | 11.1 | 1.6 | 4.4 | 5.9 | 2.8 | 6.1 | 1.0 | 2.4 | 2.2 | 2.2 | 1.7 | 0.5 | 1.4 | 11.4 | 1.6 | 3.1 |
| C8 | 1808 (11.3%) | 8.4 | 15.8 | 9.3 | 1.8 | 0.3 | 12.8 | 2.2 | 16.1 | 0.8 | 3.0 | 8.9 | 3.3 | 1.0 | 0.4 | 5.0 | 2.3 | 1.0 | 1.5 | 0.1 | 1.0 | 0.9 | 2.4 | 1.9 |
| C9 | 2319 (14.5%) | 7.4 | 13.5 | 6.3 | 1.5 | 0.3 | 10.5 | 1.4 | 22.0 | 2.7 | 2.0 | 11.1 | 1.9 | 3.3 | 0.9 | 1.3 | 1.5 | 1.2 | 2.7 | 0.1 | 1.2 | 1.6 | 2.1 | 3.4 |


## Synthese comparative 2007-2014

Les deux annees montrent une stratification forte des comportements budgetaires. Les profils modestes restent marques par l'alimentaire et certaines composantes de logement. Les profils plus aises ou plus urbains se signalent par la montee de la sante, du transport, de la communication, de la culture et des autres depenses. La matrice en 23 postes permet surtout de voir que les clusters ne se differencient pas seulement par le volume alimentaire total : ils se distinguent aussi par la composition interne de l'alimentaire, par le type de logement/energie, et par l'apparition de postes tres specifiques comme S13 ou S14.