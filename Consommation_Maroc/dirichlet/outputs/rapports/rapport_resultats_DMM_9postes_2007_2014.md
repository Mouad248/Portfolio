# Rapport detaille des resultats DMM - 9 postes, ENNVM 2007 et ENCDM 2014

## Objet et angle de lecture

Ce rapport presente les resultats du Dirichlet Mixture Model fini applique aux matrices de parts budgetaires en 9 postes. Il couvre uniquement les cas ENNVM 2007 et ENCDM 2014. L'accent est mis sur les profils comportementaux issus des clusters : ce que chaque groupe consomme relativement plus ou moins, comment les profils se divisent lorsque K augmente, et quelles solutions sont les plus defendables pour une interpretation economique.

Les profils sont lus a partir des parts budgetaires moyennes des menages affectes a chaque cluster. Les diagnostics socio-economiques utilisent les fichiers de diagnostic deja generes et servent a qualifier les groupes par niveau de depense, milieu et quintiles de DAM. Les resultats de modelisation DMM eux-memes sont construits sur les matrices de parts normalisees.

## Libelles des 9 postes

| Poste | Libelle |
| --- | --- |
| G1 | Alimentation & boissons |
| G2 | Habillement & chaussures |
| G3 | Logement, eau, energie |
| G4 | Boissons alcool. & tabac |
| G5 | Ameublement & equipement |
| G6 | Sante |
| G7 | Transport |
| G8 | Communication |
| G9 | Loisirs, culture & enseignement |

## Conclusion generale sur le choix de K

Dans les deux enquetes, les criteres AIC/BIC continuent d'avantager les solutions plus fines, surtout K=9. Cette amelioration statistique ne doit pas etre confondue avec une meilleure interpretabilite. Les solutions elevees reduisent la nettete des affectations, augmentent la part de menages ambigus et finissent par creer des groupes tres petits. Pour l'analyse comportementale, K=6 ressort comme le meilleur compromis commun : il conserve des tailles suffisantes, fait apparaitre les grands profils economiques et reste lisible. Pour ENNVM 2007, K=5 peut etre defendu comme version plus sobre ; pour ENCDM 2014, K=7 ou K=8 peuvent etre exploites comme raffinement, mais K=6 reste la base de lecture la plus robuste.

## ENNVM 2007 - resultats DMM 9 postes

### Profil moyen global de l'echantillon

| Poste | Libelle | Part moyenne |
| --- | --- | --- |
| G1 | Alimentation & boissons | 46.5% |
| G2 | Habillement & chaussures | 3.0% |
| G3 | Logement, eau, energie | 22.7% |
| G4 | Boissons alcool. & tabac | 3.3% |
| G5 | Ameublement & equipement | 6.9% |
| G6 | Sante | 7.3% |
| G7 | Transport | 3.3% |
| G8 | Communication | 4.8% |
| G9 | Loisirs, culture & enseignement | 2.1% |

### Comparaison statistique des valeurs de K

| K | BIC | AIC | Entropie | Prob. max moy. | Ambigus < 0.60 | Taille min | Taille max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | -299235 | -299365 | 0.820 | 0.952 | 2.4% | 2783 | 4279 |
| 3 | -302144 | -302343 | 0.722 | 0.881 | 7.2% | 1558 | 2809 |
| 4 | -305050 | -305318 | 0.753 | 0.865 | 9.7% | 1430 | 2188 |
| 5 | -306053 | -306389 | 0.773 | 0.860 | 11.2% | 504 | 1944 |
| 6 | -307076 | -307481 | 0.739 | 0.824 | 14.0% | 492 | 1928 |
| 7 | -307332 | -307805 | 0.732 | 0.803 | 17.5% | 161 | 1411 |
| 8 | -307525 | -308067 | 0.715 | 0.782 | 21.1% | 164 | 1436 |
| 9 | -307863 | -308474 | 0.710 | 0.771 | 23.9% | 166 | 1473 |

Lecture synthetique : les criteres de vraisemblance, AIC et BIC continuent de s'ameliorer jusqu'a K=9, ce qui est attendu dans un melange fini flexible. Cependant, la qualite classificatoire se degrade apres K=6 : la probabilite maximale moyenne descend de 0,824 a K=6 a 0,771 a K=9, et la part des menages ambigus passe de 14,0% a 23,9%. Les solutions K=7 a K=9 introduisent aussi des groupes tres petits, autour de 160 menages. Pour une lecture comportementale, K=6 est donc le compromis le plus defendable ; K=5 reste une solution plus conservatrice.

### Propagation des profils de K=2 a K=9

La partition commence a K=2 par une opposition entre un profil plus diversifie, moins alimentaire et plus urbain, et un profil plus alimentaire-logement. A K=3, le bloc essentiel se separe entre un profil fortement alimentaire et un profil alimentaire-logement. A K=4, apparait plus clairement un groupe a sante et communication elevees. A K=5, le modele isole un petit groupe a tres forte part de sante. A K=6, les principaux comportements sont lisibles sans tomber encore dans une fragmentation excessive. A partir de K=7, ce groupe sante se divise en un noyau extreme et un groupe plus modere ; K=8 et K=9 ajoutent surtout des sous-profils de logement, equipement et communication.

### Profils detailles pour K=6

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1347 (19.1%) | Alimentation dominante | 53.0 | 4.3 | 21.8 | 4.0 | 6.0 | 5.3 | 4.0 | 0.2 | 1.4 |
| C2 | 492 (7.0%) | Sante tres elevee | 27.6 | 3.9 | 14.9 | 3.4 | 6.3 | 27.7 | 5.8 | 6.9 | 3.6 |
| C3 | 1100 (15.6%) | Alimentation-logement | 52.4 | 2.1 | 29.0 | 2.3 | 5.4 | 1.9 | 2.5 | 2.6 | 1.7 |
| C4 | 1260 (17.8%) | Communication elevee | 40.2 | 1.5 | 23.5 | 2.6 | 7.9 | 9.1 | 2.4 | 10.1 | 2.8 |
| C5 | 935 (13.2%) | Logement renforce | 51.6 | 1.1 | 26.8 | 3.0 | 8.4 | 5.8 | 1.9 | 0.2 | 1.3 |
| C6 | 1928 (27.3%) | Profil intermediaire | 45.2 | 4.4 | 19.4 | 4.0 | 7.0 | 6.1 | 4.0 | 7.7 | 2.2 |

### Caracterisation socio-economique des profils K=6

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1347 | 44393 | 39728 | -22.0% | 56.2% | 43.8% | Q2 (26.8%) |
| C2 | 492 | 143296 | 108828 | +151.9% | 74.6% | 25.4% | Q5 (72.0%) |
| C3 | 1100 | 29934 | 23142 | -47.4% | 44.2% | 55.8% | Q1 (56.8%) |
| C4 | 1260 | 63796 | 46213 | +12.1% | 67.5% | 32.5% | Q5 (24.9%) |
| C5 | 935 | 38585 | 33970 | -32.2% | 56.3% | 43.7% | Q1 (28.2%) |
| C6 | 1928 | 63306 | 53318 | +11.3% | 66.4% | 33.6% | Q4 (28.5%) |

### Parametres de Dirichlet pour K=6

Le parametre `pi` represente le poids estime de la composante dans le melange. `alpha_sum` mesure la concentration : plus elle est elevee, plus le profil theorique du cluster est homogene autour de sa moyenne.

| Cluster | pi | alpha_sum | Profil theorique dominant |
| --- | --- | --- | --- |
| C1 | 0.188 | 30.1 | G1=52.2%, G3=21.3%, G5=5.6% |
| C2 | 0.070 | 21.7 | G1=28.3%, G6=25.2%, G3=15.3% |
| C3 | 0.180 | 7.9 | G1=51.9%, G3=29.4%, G5=3.9% |
| C4 | 0.173 | 12.1 | G1=40.0%, G3=23.2%, G8=10.3% |
| C5 | 0.149 | 17.4 | G1=50.7%, G3=25.9%, G5=7.7% |
| C6 | 0.240 | 26.8 | G1=44.8%, G3=19.2%, G8=7.7% |

### Diagnostics socio-economiques globaux par K

| K | Cramer Milieu | Cramer quintile_DAM | eta2 DAM | eta2 log_DAM | Associations qualitatives dominantes |
| --- | --- | --- | --- | --- | --- |
| 2 | 0.130 | 0.401 | 0.074 | 0.154 | quintile_DAM=0.401 ; Profession_CM=0.254 ; Niveau_scolaire_CM=0.236 ; Quintiles=0.227 ; Taille_ménage_agreg=0.217 |
| 3 | 0.134 | 0.335 | 0.090 | 0.179 | quintile_DAM=0.335 ; Taille_ménage_agreg=0.204 ; Profession_CM=0.199 ; Quintiles=0.192 ; Niveau_scolaire_CM=0.185 |
| 4 | 0.170 | 0.294 | 0.124 | 0.237 | quintile_DAM=0.294 ; Quintiles=0.196 ; Taille_ménage_agreg=0.176 ; Sexe_CM=0.174 ; Milieu=0.170 |
| 5 | 0.173 | 0.289 | 0.247 | 0.301 | quintile_DAM=0.289 ; Quintiles=0.195 ; Profession_CM=0.195 ; Sexe_CM=0.178 ; Niveau_scolaire_CM=0.176 |
| 6 | 0.182 | 0.301 | 0.244 | 0.315 | quintile_DAM=0.301 ; Quintiles=0.205 ; Sexe_CM=0.186 ; Milieu=0.182 ; Profession_CM=0.176 |
| 7 | 0.201 | 0.317 | 0.277 | 0.339 | quintile_DAM=0.317 ; Quintiles=0.218 ; Milieu=0.201 ; Niveau_scolaire_CM=0.185 ; Sexe_CM=0.181 |
| 8 | 0.226 | 0.320 | 0.278 | 0.344 | quintile_DAM=0.320 ; Milieu=0.226 ; Quintiles=0.223 ; Niveau_scolaire_CM=0.188 ; Sexe_CM=0.176 |
| 9 | 0.228 | 0.319 | 0.276 | 0.343 | quintile_DAM=0.319 ; Milieu=0.228 ; Quintiles=0.227 ; Niveau_scolaire_CM=0.189 ; Sexe_CM=0.179 |

### Annexe : signatures de profils pour tous les K

#### K=2

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 2783 (39.4%) | Profil intermediaire | Alimentation & boissons 42.2%, Logement, eau, energie 19.1%, Sante 9.6% | Communication +2.5 pp, Sante +2.3 pp, Habillement & chaussures +1.2 pp |
| C2 | 4279 (60.6%) | Profil intermediaire | Alimentation & boissons 49.4%, Logement, eau, energie 25.1%, Ameublement & equipement 6.9% | Alimentation & boissons +2.8 pp, Logement, eau, energie +2.4 pp |

#### K=3

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1558 (22.1%) | Logement renforce | Alimentation & boissons 46.8%, Logement, eau, energie 27.8%, Ameublement & equipement 6.5% | Logement, eau, energie +5.0 pp |
| C2 | 2809 (39.8%) | Profil intermediaire | Alimentation & boissons 51.3%, Logement, eau, energie 23.5%, Ameublement & equipement 7.1% | Alimentation & boissons +4.8 pp, Logement, eau, energie +0.8 pp |
| C3 | 2695 (38.2%) | Profil intermediaire | Alimentation & boissons 41.4%, Logement, eau, energie 19.0%, Sante 9.8% | Communication +2.9 pp, Sante +2.5 pp, Habillement & chaussures +1.2 pp |

#### K=4

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 2188 (31.0%) | Profil intermediaire | Alimentation & boissons 43.1%, Logement, eau, energie 18.9%, Sante 8.0% | Communication +2.9 pp, Habillement & chaussures +1.4 pp, Transport +1.0 pp |
| C2 | 1430 (20.2%) | Alimentation dominante | Alimentation & boissons 52.8%, Logement, eau, energie 22.1%, Ameublement & equipement 6.2% | Alimentation & boissons +6.2 pp, Habillement & chaussures +1.1 pp, Boissons alcool. & tabac +0.6 pp |
| C3 | 1962 (27.8%) | Alimentation-logement | Alimentation & boissons 52.4%, Logement, eau, energie 28.1%, Ameublement & equipement 6.6% | Alimentation & boissons +5.8 pp, Logement, eau, energie +5.4 pp |
| C4 | 1482 (21.0%) | Communication elevee | Alimentation & boissons 37.8%, Logement, eau, energie 21.8%, Sante 13.4% | Sante +6.1 pp, Communication +4.3 pp, Loisirs, culture & enseignement +0.9 pp |

#### K=5

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1944 (27.5%) | Logement renforce | Alimentation & boissons 51.9%, Logement, eau, energie 28.1%, Ameublement & equipement 6.7% | Alimentation & boissons +5.4 pp, Logement, eau, energie +5.4 pp |
| C2 | 1873 (26.5%) | Profil intermediaire | Alimentation & boissons 45.2%, Logement, eau, energie 19.2%, Communication 7.8% | Communication +3.0 pp, Habillement & chaussures +1.4 pp, Boissons alcool. & tabac +0.7 pp |
| C3 | 504 (7.1%) | Sante tres elevee | Sante 27.4%, Alimentation & boissons 27.4%, Logement, eau, energie 15.0% | Sante +20.1 pp, Transport +2.6 pp, Communication +2.1 pp |
| C4 | 1306 (18.5%) | Communication elevee | Alimentation & boissons 41.3%, Logement, eau, energie 23.4%, Communication 9.6% | Communication +4.8 pp, Sante +1.7 pp, Ameublement & equipement +1.0 pp |
| C5 | 1435 (20.3%) | Alimentation dominante | Alimentation & boissons 52.5%, Logement, eau, energie 22.2%, Ameublement & equipement 6.3% | Alimentation & boissons +5.9 pp, Habillement & chaussures +1.1 pp, Boissons alcool. & tabac +0.6 pp |

#### K=6

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1347 (19.1%) | Alimentation dominante | Alimentation & boissons 53.0%, Logement, eau, energie 21.8%, Ameublement & equipement 6.0% | Alimentation & boissons +6.4 pp, Habillement & chaussures +1.3 pp, Boissons alcool. & tabac +0.7 pp |
| C2 | 492 (7.0%) | Sante tres elevee | Sante 27.7%, Alimentation & boissons 27.6%, Logement, eau, energie 14.9% | Sante +20.4 pp, Transport +2.5 pp, Communication +2.0 pp |
| C3 | 1100 (15.6%) | Alimentation-logement | Alimentation & boissons 52.4%, Logement, eau, energie 29.0%, Ameublement & equipement 5.4% | Logement, eau, energie +6.3 pp, Alimentation & boissons +5.9 pp |
| C4 | 1260 (17.8%) | Communication elevee | Alimentation & boissons 40.2%, Logement, eau, energie 23.5%, Communication 10.1% | Communication +5.2 pp, Sante +1.8 pp, Ameublement & equipement +1.1 pp |
| C5 | 935 (13.2%) | Logement renforce | Alimentation & boissons 51.6%, Logement, eau, energie 26.8%, Ameublement & equipement 8.4% | Alimentation & boissons +5.1 pp, Logement, eau, energie +4.0 pp, Ameublement & equipement +1.6 pp |
| C6 | 1928 (27.3%) | Profil intermediaire | Alimentation & boissons 45.2%, Logement, eau, energie 19.4%, Communication 7.7% | Communication +2.9 pp, Habillement & chaussures +1.4 pp, Boissons alcool. & tabac +0.7 pp |

#### K=7

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1411 (20.0%) | Alimentation dominante | Alimentation & boissons 52.8%, Logement, eau, energie 21.9%, Ameublement & equipement 6.1% | Alimentation & boissons +6.2 pp, Habillement & chaussures +1.3 pp, Boissons alcool. & tabac +0.7 pp |
| C2 | 161 (2.3%) | Sante tres elevee | Sante 46.2%, Alimentation & boissons 22.2%, Logement, eau, energie 11.7% | Sante +38.9 pp, Loisirs, culture & enseignement +1.0 pp, Communication +0.8 pp |
| C3 | 1121 (15.9%) | Logement renforce | Alimentation & boissons 52.0%, Logement, eau, energie 29.1%, Ameublement & equipement 5.6% | Logement, eau, energie +6.3 pp, Alimentation & boissons +5.5 pp |
| C4 | 934 (13.2%) | Logement renforce | Alimentation & boissons 51.5%, Logement, eau, energie 26.8%, Ameublement & equipement 8.5% | Alimentation & boissons +4.9 pp, Logement, eau, energie +4.1 pp, Ameublement & equipement +1.6 pp |
| C5 | 1215 (17.2%) | Communication elevee | Alimentation & boissons 41.5%, Logement, eau, energie 23.8%, Communication 10.3% | Communication +5.5 pp, Logement, eau, energie +1.0 pp, Ameublement & equipement +0.9 pp |
| C6 | 1293 (18.3%) | Profil intermediaire | Alimentation & boissons 48.9%, Logement, eau, energie 19.2%, Communication 8.3% | Communication +3.5 pp, Alimentation & boissons +2.4 pp, Habillement & chaussures +1.1 pp |
| C7 | 927 (13.1%) | Diversifie hors alimentaire | Alimentation & boissons 33.0%, Logement, eau, energie 17.8%, Sante 14.8% | Sante +7.5 pp, Transport +3.0 pp, Communication +2.2 pp |

#### K=8

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1436 (20.3%) | Alimentation dominante | Alimentation & boissons 52.6%, Logement, eau, energie 22.0%, Ameublement & equipement 6.2% | Alimentation & boissons +6.0 pp, Habillement & chaussures +1.3 pp, Boissons alcool. & tabac +0.6 pp |
| C2 | 1213 (17.2%) | Profil intermediaire | Alimentation & boissons 49.4%, Logement, eau, energie 19.2%, Communication 8.3% | Communication +3.4 pp, Alimentation & boissons +2.8 pp, Habillement & chaussures +1.2 pp |
| C3 | 164 (2.3%) | Sante tres elevee | Sante 44.7%, Alimentation & boissons 23.0%, Logement, eau, energie 11.7% | Sante +37.5 pp, Communication +1.0 pp, Loisirs, culture & enseignement +0.8 pp |
| C4 | 992 (14.0%) | Diversifie hors alimentaire | Alimentation & boissons 33.3%, Logement, eau, energie 18.2%, Sante 14.0% | Sante +6.7 pp, Transport +3.0 pp, Communication +2.4 pp |
| C5 | 486 (6.9%) | Equipement/logement | Alimentation & boissons 35.1%, Logement, eau, energie 29.0%, Ameublement & equipement 12.4% | Logement, eau, energie +6.2 pp, Ameublement & equipement +5.5 pp, Loisirs, culture & enseignement +2.6 pp |
| C6 | 1055 (14.9%) | Communication elevee | Alimentation & boissons 43.3%, Logement, eau, energie 23.4%, Communication 10.7% | Communication +5.8 pp, Logement, eau, energie +0.6 pp |
| C7 | 936 (13.3%) | Alimentation-logement | Alimentation & boissons 54.7%, Logement, eau, energie 28.5%, Ameublement & equipement 4.4% | Alimentation & boissons +8.1 pp, Logement, eau, energie +5.7 pp |
| C8 | 780 (11.0%) | Alimentation-logement | Alimentation & boissons 54.4%, Logement, eau, energie 26.1%, Ameublement & equipement 7.3% | Alimentation & boissons +7.9 pp, Logement, eau, energie +3.4 pp |

#### K=9

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 940 (13.3%) | Alimentation-logement | Alimentation & boissons 54.6%, Logement, eau, energie 28.4%, Ameublement & equipement 4.4% | Alimentation & boissons +8.1 pp, Logement, eau, energie +5.7 pp |
| C2 | 1036 (14.7%) | Diversifie hors alimentaire | Alimentation & boissons 33.6%, Logement, eau, energie 18.0%, Sante 13.7% | Sante +6.4 pp, Communication +2.8 pp, Transport +2.7 pp |
| C3 | 1473 (20.9%) | Alimentation dominante | Alimentation & boissons 52.4%, Logement, eau, energie 22.2%, Ameublement & equipement 6.2% | Alimentation & boissons +5.8 pp, Habillement & chaussures +1.3 pp, Boissons alcool. & tabac +0.6 pp |
| C4 | 409 (5.8%) | Communication elevee | Alimentation & boissons 43.8%, Logement, eau, energie 22.0%, Communication 11.2% | Communication +6.4 pp, Habillement & chaussures +0.9 pp |
| C5 | 588 (8.3%) | Equipement/logement | Alimentation & boissons 35.7%, Logement, eau, energie 27.4%, Ameublement & equipement 12.4% | Ameublement & equipement +5.5 pp, Logement, eau, energie +4.6 pp, Loisirs, culture & enseignement +2.4 pp |
| C6 | 166 (2.4%) | Sante tres elevee | Sante 44.6%, Alimentation & boissons 23.3%, Logement, eau, energie 11.7% | Sante +37.3 pp, Communication +0.9 pp, Loisirs, culture & enseignement +0.7 pp |
| C7 | 823 (11.7%) | Alimentation-logement | Alimentation & boissons 54.7%, Logement, eau, energie 26.0%, Ameublement & equipement 7.2% | Alimentation & boissons +8.2 pp, Logement, eau, energie +3.2 pp |
| C8 | 1069 (15.1%) | Profil intermediaire | Alimentation & boissons 50.4%, Logement, eau, energie 18.7%, Communication 8.2% | Alimentation & boissons +3.8 pp, Communication +3.4 pp, Habillement & chaussures +1.3 pp |
| C9 | 558 (7.9%) | Communication elevee | Alimentation & boissons 42.5%, Logement, eau, energie 25.4%, Communication 9.4% | Communication +4.5 pp, Logement, eau, energie +2.7 pp, Transport +1.1 pp |

### Annexe : profils numeriques complets pour tous les K

Les valeurs ci-dessous sont exprimees en pourcentage de la depense totale du menage dans chaque cluster. Elles permettent de retrouver precisement la contribution de chaque poste G1-G9.

#### Profils numeriques K=2

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2783 (39.4%) | Profil intermediaire | 42.2 | 4.2 | 19.1 | 3.9 | 6.8 | 9.6 | 4.3 | 7.4 | 2.4 |
| C2 | 4279 (60.6%) | Profil intermediaire | 49.4 | 2.3 | 25.1 | 2.9 | 6.9 | 5.8 | 2.7 | 3.2 | 1.8 |

#### Profils numeriques K=3

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1558 (22.1%) | Logement renforce | 46.8 | 1.9 | 27.8 | 2.0 | 6.5 | 5.2 | 2.4 | 5.3 | 2.2 |
| C2 | 2809 (39.8%) | Profil intermediaire | 51.3 | 2.5 | 23.5 | 3.4 | 7.1 | 6.0 | 2.8 | 1.8 | 1.5 |
| C3 | 2695 (38.2%) | Profil intermediaire | 41.4 | 4.2 | 19.0 | 3.9 | 6.8 | 9.8 | 4.4 | 7.7 | 2.6 |

#### Profils numeriques K=4

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2188 (31.0%) | Profil intermediaire | 43.1 | 4.5 | 18.9 | 4.0 | 7.0 | 8.0 | 4.4 | 7.7 | 2.4 |
| C2 | 1430 (20.2%) | Alimentation dominante | 52.8 | 4.1 | 22.1 | 3.9 | 6.2 | 5.4 | 3.8 | 0.2 | 1.4 |
| C3 | 1962 (27.8%) | Alimentation-logement | 52.4 | 1.7 | 28.1 | 2.5 | 6.6 | 3.2 | 2.2 | 1.7 | 1.5 |
| C4 | 1482 (21.0%) | Communication elevee | 37.8 | 1.6 | 21.8 | 2.7 | 7.7 | 13.4 | 2.8 | 9.2 | 3.0 |

#### Profils numeriques K=5

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1944 (27.5%) | Logement renforce | 51.9 | 1.7 | 28.1 | 2.5 | 6.7 | 3.4 | 2.3 | 1.6 | 1.6 |
| C2 | 1873 (26.5%) | Profil intermediaire | 45.2 | 4.4 | 19.2 | 4.0 | 6.9 | 6.1 | 4.0 | 7.8 | 2.2 |
| C3 | 504 (7.1%) | Sante tres elevee | 27.4 | 3.9 | 15.0 | 3.3 | 6.4 | 27.4 | 5.9 | 7.0 | 3.7 |
| C4 | 1306 (18.5%) | Communication elevee | 41.3 | 1.4 | 23.4 | 2.7 | 7.8 | 9.0 | 2.3 | 9.6 | 2.5 |
| C5 | 1435 (20.3%) | Alimentation dominante | 52.5 | 4.1 | 22.2 | 3.9 | 6.3 | 5.5 | 3.9 | 0.2 | 1.4 |

#### Profils numeriques K=6

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1347 (19.1%) | Alimentation dominante | 53.0 | 4.3 | 21.8 | 4.0 | 6.0 | 5.3 | 4.0 | 0.2 | 1.4 |
| C2 | 492 (7.0%) | Sante tres elevee | 27.6 | 3.9 | 14.9 | 3.4 | 6.3 | 27.7 | 5.8 | 6.9 | 3.6 |
| C3 | 1100 (15.6%) | Alimentation-logement | 52.4 | 2.1 | 29.0 | 2.3 | 5.4 | 1.9 | 2.5 | 2.6 | 1.7 |
| C4 | 1260 (17.8%) | Communication elevee | 40.2 | 1.5 | 23.5 | 2.6 | 7.9 | 9.1 | 2.4 | 10.1 | 2.8 |
| C5 | 935 (13.2%) | Logement renforce | 51.6 | 1.1 | 26.8 | 3.0 | 8.4 | 5.8 | 1.9 | 0.2 | 1.3 |
| C6 | 1928 (27.3%) | Profil intermediaire | 45.2 | 4.4 | 19.4 | 4.0 | 7.0 | 6.1 | 4.0 | 7.7 | 2.2 |

#### Profils numeriques K=7

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1411 (20.0%) | Alimentation dominante | 52.8 | 4.4 | 21.9 | 4.0 | 6.1 | 5.3 | 4.0 | 0.2 | 1.5 |
| C2 | 161 (2.3%) | Sante tres elevee | 22.2 | 1.9 | 11.7 | 2.2 | 4.2 | 46.2 | 2.8 | 5.7 | 3.1 |
| C3 | 1121 (15.9%) | Logement renforce | 52.0 | 2.1 | 29.1 | 2.3 | 5.6 | 2.0 | 2.6 | 2.6 | 1.8 |
| C4 | 934 (13.2%) | Logement renforce | 51.5 | 1.1 | 26.8 | 2.9 | 8.5 | 5.8 | 1.9 | 0.2 | 1.3 |
| C5 | 1215 (17.2%) | Communication elevee | 41.5 | 1.6 | 23.8 | 2.6 | 7.7 | 7.8 | 2.2 | 10.3 | 2.6 |
| C6 | 1293 (18.3%) | Profil intermediaire | 48.9 | 4.2 | 19.2 | 3.7 | 6.2 | 4.5 | 3.3 | 8.3 | 1.7 |
| C7 | 927 (13.1%) | Diversifie hors alimentaire | 33.0 | 4.7 | 17.8 | 4.3 | 8.1 | 14.8 | 6.4 | 7.1 | 3.8 |

#### Profils numeriques K=8

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1436 (20.3%) | Alimentation dominante | 52.6 | 4.3 | 22.0 | 3.9 | 6.2 | 5.4 | 4.0 | 0.2 | 1.5 |
| C2 | 1213 (17.2%) | Profil intermediaire | 49.4 | 4.2 | 19.2 | 3.7 | 6.1 | 4.4 | 3.2 | 8.3 | 1.6 |
| C3 | 164 (2.3%) | Sante tres elevee | 23.0 | 2.2 | 11.7 | 2.4 | 4.3 | 44.7 | 3.0 | 5.8 | 2.8 |
| C4 | 992 (14.0%) | Diversifie hors alimentaire | 33.3 | 4.6 | 18.2 | 4.3 | 8.2 | 14.0 | 6.3 | 7.2 | 3.8 |
| C5 | 486 (6.9%) | Equipement/logement | 35.1 | 1.7 | 29.0 | 1.1 | 12.4 | 9.2 | 3.9 | 2.9 | 4.6 |
| C6 | 1055 (14.9%) | Communication elevee | 43.3 | 1.5 | 23.4 | 3.1 | 7.2 | 7.3 | 1.7 | 10.7 | 1.8 |
| C7 | 936 (13.3%) | Alimentation-logement | 54.7 | 2.2 | 28.5 | 2.6 | 4.4 | 1.1 | 2.2 | 3.0 | 1.4 |
| C8 | 780 (11.0%) | Alimentation-logement | 54.4 | 0.9 | 26.1 | 3.0 | 7.3 | 5.3 | 1.8 | 0.2 | 1.0 |

#### Profils numeriques K=9

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 940 (13.3%) | Alimentation-logement | 54.6 | 2.1 | 28.4 | 2.5 | 4.4 | 1.1 | 2.2 | 3.2 | 1.4 |
| C2 | 1036 (14.7%) | Diversifie hors alimentaire | 33.6 | 4.7 | 18.0 | 4.3 | 8.2 | 13.7 | 6.1 | 7.6 | 3.8 |
| C3 | 1473 (20.9%) | Alimentation dominante | 52.4 | 4.3 | 22.2 | 3.9 | 6.2 | 5.4 | 3.9 | 0.3 | 1.5 |
| C4 | 409 (5.8%) | Communication elevee | 43.8 | 4.0 | 22.0 | 3.4 | 7.3 | 6.6 | 0.1 | 11.2 | 1.6 |
| C5 | 588 (8.3%) | Equipement/logement | 35.7 | 1.6 | 27.4 | 1.2 | 12.4 | 9.5 | 3.0 | 4.7 | 4.5 |
| C6 | 166 (2.4%) | Sante tres elevee | 23.3 | 2.1 | 11.7 | 2.4 | 4.3 | 44.6 | 2.9 | 5.8 | 2.8 |
| C7 | 823 (11.7%) | Alimentation-logement | 54.7 | 0.8 | 26.0 | 2.9 | 7.2 | 5.2 | 1.5 | 0.6 | 1.0 |
| C8 | 1069 (15.1%) | Profil intermediaire | 50.4 | 4.3 | 18.7 | 3.7 | 5.8 | 4.2 | 3.1 | 8.2 | 1.6 |
| C9 | 558 (7.9%) | Communication elevee | 42.5 | 0.2 | 25.4 | 3.1 | 6.4 | 7.0 | 4.4 | 9.4 | 1.6 |


## ENCDM 2014 - resultats DMM 9 postes

### Profil moyen global de l'echantillon

| Poste | Libelle | Part moyenne |
| --- | --- | --- |
| G1 | Alimentation & boissons | 42.1% |
| G2 | Habillement & chaussures | 2.9% |
| G3 | Logement, eau, energie | 25.5% |
| G4 | Boissons alcool. & tabac | 3.0% |
| G5 | Ameublement & equipement | 8.2% |
| G6 | Sante | 6.8% |
| G7 | Transport | 3.9% |
| G8 | Communication | 5.1% |
| G9 | Loisirs, culture & enseignement | 2.5% |

### Comparaison statistique des valeurs de K

| K | BIC | AIC | Entropie | Prob. max moy. | Ambigus < 0.60 | Taille min | Taille max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | -639172 | -639318 | 0.803 | 0.947 | 2.4% | 7345 | 8625 |
| 3 | -644126 | -644348 | 0.743 | 0.890 | 6.9% | 3625 | 7081 |
| 4 | -648213 | -648513 | 0.711 | 0.845 | 10.9% | 2790 | 6536 |
| 5 | -650114 | -650490 | 0.695 | 0.811 | 15.7% | 1994 | 4810 |
| 6 | -650997 | -651450 | 0.686 | 0.787 | 19.9% | 1095 | 4639 |
| 7 | -652908 | -653438 | 0.664 | 0.755 | 23.6% | 1076 | 4652 |
| 8 | -653372 | -653979 | 0.652 | 0.738 | 27.3% | 1205 | 4109 |
| 9 | -653543 | -654226 | 0.670 | 0.737 | 27.5% | 162 | 4151 |

Lecture synthetique : comme pour 2007, AIC et BIC favorisent mecaniquement les solutions les plus fines. Mais K=9 introduit un cluster minuscule de 162 menages et une ambiguite proche de 27,5%. K=6 conserve des tailles de clusters raisonnables, avec un minimum de 1095 menages, tout en isolant les grands comportements budgetaires. K=7 ou K=8 peuvent servir a une analyse plus fine, mais K=6 reste la solution centrale pour l'interpretation.

### Propagation des profils de K=2 a K=9

La partition de 2014 commence egalement par une opposition entre depenses essentielles et depenses plus diversifiees. A K=3, les profils alimentaire, logement et diversifie se separent. A K=4, le logement tres eleve devient un comportement distinct. A K=5, le modele isole un groupe aise marque par la sante, le transport et la communication. A K=6, la structure devient economiquement tres claire : alimentaire populaire, logement contraint, centre urbain, communication/equipement et profil aise. Les valeurs K=7 et K=8 raffinent surtout les profils logement et communication. K=9 ajoute un petit groupe loisirs-culture, mais sa taille de 1% le rend fragile comme classe generale.

### Profils detailles pour K=6

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2293 (14.4%) | Alimentation dominante | 49.5 | 3.8 | 25.8 | 3.5 | 7.5 | 4.5 | 4.0 | 0.2 | 1.3 |
| C2 | 2434 (15.2%) | Communication elevee | 35.9 | 0.9 | 26.9 | 2.1 | 9.9 | 8.7 | 2.7 | 9.6 | 3.3 |
| C3 | 1095 (6.9%) | Profil intermediaire | 47.2 | 3.8 | 23.0 | 3.2 | 8.2 | 6.6 | 0.0 | 6.4 | 1.5 |
| C4 | 4639 (29.0%) | Profil intermediaire | 43.1 | 4.1 | 22.5 | 3.6 | 8.0 | 6.0 | 4.2 | 6.6 | 2.0 |
| C5 | 3646 (22.8%) | Logement renforce | 47.0 | 1.5 | 32.6 | 2.4 | 8.1 | 3.2 | 2.2 | 1.0 | 2.0 |
| C6 | 1863 (11.7%) | Sante-transport aise | 26.2 | 3.8 | 18.2 | 3.1 | 8.0 | 16.4 | 9.8 | 8.5 | 5.9 |

### Caracterisation socio-economique des profils K=6

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2293 | 52574 | 48220 | -30.0% | 56.7% | 43.3% | Q2 (30.8%) |
| C2 | 2434 | 78492 | 61698 | +4.6% | 71.0% | 29.0% | Q5 (22.9%) |
| C3 | 1095 | 64036 | 57551 | -14.7% | 54.7% | 45.3% | Q3 (26.9%) |
| C4 | 4639 | 76886 | 67506 | +2.4% | 68.2% | 31.8% | Q4 (29.6%) |
| C5 | 3646 | 43828 | 37762 | -41.6% | 55.6% | 44.4% | Q1 (47.1%) |
| C6 | 1863 | 161376 | 137236 | +115.0% | 84.1% | 15.9% | Q5 (70.7%) |

### Parametres de Dirichlet pour K=6

Le parametre `pi` represente le poids estime de la composante dans le melange. `alpha_sum` mesure la concentration : plus elle est elevee, plus le profil theorique du cluster est homogene autour de sa moyenne.

| Cluster | pi | alpha_sum | Profil theorique dominant |
| --- | --- | --- | --- |
| C1 | 0.147 | 28.4 | G1=48.7%, G3=25.1%, G5=6.8% |
| C2 | 0.160 | 12.0 | G1=36.3%, G3=26.4%, G5=9.3% |
| C3 | 0.084 | 26.0 | G1=46.3%, G3=22.7%, G5=7.6% |
| C4 | 0.235 | 27.7 | G1=42.4%, G3=22.0%, G5=7.6% |
| C5 | 0.254 | 9.2 | G1=46.3%, G3=32.2%, G5=6.4% |
| C6 | 0.120 | 17.9 | G1=28.3%, G3=19.0%, G6=14.0% |

### Diagnostics socio-economiques globaux par K

| K | Cramer Milieu | Cramer quintile_DAM | eta2 DAM | eta2 log_DAM | Associations qualitatives dominantes |
| --- | --- | --- | --- | --- | --- |
| 2 | 0.125 | 0.431 | 0.107 | 0.183 | quintile_DAM=0.431 ; Niveau_scolaire_agreg_CM=0.239 ; Taille_agregée=0.236 ; Profession_agreg_CM=0.225 ; Deciles=0.224 |
| 3 | 0.165 | 0.326 | 0.117 | 0.192 | quintile_DAM=0.326 ; Decileurbain=0.183 ; Niveau_scolaire_agreg_CM=0.181 ; Deciles=0.180 ; Profession_agreg_CM=0.179 |
| 4 | 0.172 | 0.299 | 0.129 | 0.239 | quintile_DAM=0.299 ; Sexe_CM=0.187 ; Deciles=0.177 ; Diplôme_agregé_CM=0.174 ; Milieu=0.172 |
| 5 | 0.192 | 0.318 | 0.300 | 0.342 | quintile_DAM=0.318 ; Diplôme_agregé_CM=0.269 ; Deciles=0.232 ; Decileurbain=0.228 ; Quintileurbain=0.218 |
| 6 | 0.197 | 0.320 | 0.303 | 0.349 | quintile_DAM=0.320 ; Diplôme_agregé_CM=0.275 ; Quintiles=0.214 ; Deciles=0.210 ; Decileurbain=0.208 |
| 7 | 0.202 | 0.325 | 0.298 | 0.350 | quintile_DAM=0.325 ; Diplôme_agregé_CM=0.274 ; Quintiles=0.218 ; Sexe_CM=0.202 ; Milieu=0.202 |
| 8 | 0.219 | 0.329 | 0.296 | 0.361 | quintile_DAM=0.329 ; Diplôme_agregé_CM=0.268 ; Quintiles=0.231 ; Milieu=0.219 ; Quintileurbain=0.208 |
| 9 | 0.221 | 0.331 | 0.298 | 0.362 | quintile_DAM=0.331 ; Diplôme_agregé_CM=0.273 ; Quintiles=0.232 ; Milieu=0.221 ; Quintileurbain=0.211 |

### Annexe : signatures de profils pour tous les K

#### K=2

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 7345 (46.0%) | Profil intermediaire | Alimentation & boissons 38.8%, Logement, eau, energie 21.6%, Sante 8.7% | Communication +2.1 pp, Sante +1.9 pp, Transport +1.5 pp |
| C2 | 8625 (54.0%) | Logement renforce | Alimentation & boissons 45.0%, Logement, eau, energie 28.8%, Ameublement & equipement 8.3% | Logement, eau, energie +3.3 pp, Alimentation & boissons +2.8 pp |

#### K=3

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 3625 (22.7%) | Alimentation dominante | Alimentation & boissons 50.3%, Logement, eau, energie 25.5%, Ameublement & equipement 7.7% | Alimentation & boissons +8.2 pp, Habillement & chaussures +0.9 pp |
| C2 | 5264 (33.0%) | Logement renforce | Alimentation & boissons 42.0%, Logement, eau, energie 30.7%, Ameublement & equipement 8.7% | Logement, eau, energie +5.2 pp |
| C3 | 7081 (44.3%) | Profil intermediaire | Alimentation & boissons 38.0%, Logement, eau, energie 21.6%, Sante 8.9% | Communication +2.4 pp, Sante +2.1 pp, Transport +1.6 pp |

#### K=4

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 2790 (17.5%) | Logement tres eleve | Alimentation & boissons 45.9%, Logement, eau, energie 34.1%, Ameublement & equipement 8.0% | Logement, eau, energie +8.6 pp, Alimentation & boissons +3.8 pp |
| C2 | 3309 (20.7%) | Alimentation dominante | Alimentation & boissons 50.6%, Logement, eau, energie 26.0%, Ameublement & equipement 7.7% | Alimentation & boissons +8.5 pp, Habillement & chaussures +0.9 pp |
| C3 | 6536 (40.9%) | Profil intermediaire | Alimentation & boissons 38.8%, Logement, eau, energie 21.5%, Sante 8.4% | Communication +1.9 pp, Transport +1.8 pp, Sante +1.6 pp |
| C4 | 3335 (20.9%) | Communication elevee | Alimentation & boissons 37.0%, Logement, eau, energie 25.6%, Sante 9.3% | Communication +4.1 pp, Sante +2.5 pp, Ameublement & equipement +1.0 pp |

#### K=5

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 3066 (19.2%) | Alimentation dominante | Alimentation & boissons 50.1%, Logement, eau, energie 26.2%, Ameublement & equipement 7.8% | Alimentation & boissons +8.0 pp, Habillement & chaussures +0.9 pp, Logement, eau, energie +0.7 pp |
| C2 | 1994 (12.5%) | Sante-transport aise | Alimentation & boissons 26.2%, Logement, eau, energie 18.5%, Sante 15.8% | Sante +9.1 pp, Transport +5.9 pp, Communication +3.5 pp |
| C3 | 3272 (20.5%) | Communication elevee | Alimentation & boissons 39.0%, Logement, eau, energie 26.0%, Ameublement & equipement 9.4% | Communication +4.2 pp, Sante +1.3 pp, Ameublement & equipement +1.1 pp |
| C4 | 4810 (30.1%) | Profil intermediaire | Alimentation & boissons 43.9%, Logement, eau, energie 22.6%, Ameublement & equipement 7.8% | Alimentation & boissons +1.7 pp, Habillement & chaussures +1.2 pp, Communication +1.0 pp |
| C5 | 2828 (17.7%) | Logement tres eleve | Alimentation & boissons 45.4%, Logement, eau, energie 34.0%, Ameublement & equipement 8.1% | Logement, eau, energie +8.5 pp, Alimentation & boissons +3.3 pp |

#### K=6

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 2293 (14.4%) | Alimentation dominante | Alimentation & boissons 49.5%, Logement, eau, energie 25.8%, Ameublement & equipement 7.5% | Alimentation & boissons +7.3 pp, Habillement & chaussures +0.9 pp |
| C2 | 2434 (15.2%) | Communication elevee | Alimentation & boissons 35.9%, Logement, eau, energie 26.9%, Ameublement & equipement 9.9% | Communication +4.6 pp, Sante +1.9 pp, Ameublement & equipement +1.7 pp |
| C3 | 1095 (6.9%) | Profil intermediaire | Alimentation & boissons 47.2%, Logement, eau, energie 23.0%, Ameublement & equipement 8.2% | Alimentation & boissons +5.1 pp, Communication +1.4 pp, Habillement & chaussures +0.9 pp |
| C4 | 4639 (29.0%) | Profil intermediaire | Alimentation & boissons 43.1%, Logement, eau, energie 22.5%, Ameublement & equipement 8.0% | Communication +1.5 pp, Habillement & chaussures +1.2 pp, Alimentation & boissons +1.0 pp |
| C5 | 3646 (22.8%) | Logement renforce | Alimentation & boissons 47.0%, Logement, eau, energie 32.6%, Ameublement & equipement 8.1% | Logement, eau, energie +7.1 pp, Alimentation & boissons +4.9 pp |
| C6 | 1863 (11.7%) | Sante-transport aise | Alimentation & boissons 26.2%, Logement, eau, energie 18.2%, Sante 16.4% | Sante +9.6 pp, Transport +5.9 pp, Communication +3.4 pp |

#### K=7

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1896 (11.9%) | Sante-transport aise | Alimentation & boissons 26.5%, Logement, eau, energie 18.3%, Sante 16.4% | Sante +9.6 pp, Transport +5.8 pp, Communication +3.3 pp |
| C2 | 1076 (6.7%) | Profil intermediaire | Alimentation & boissons 46.9%, Logement, eau, energie 22.5%, Ameublement & equipement 7.8% | Alimentation & boissons +4.8 pp, Communication +2.3 pp, Habillement & chaussures +0.9 pp |
| C3 | 1532 (9.6%) | Logement tres eleve | Alimentation & boissons 44.3%, Logement, eau, energie 35.6%, Ameublement & equipement 7.5% | Logement, eau, energie +10.1 pp, Alimentation & boissons +2.2 pp |
| C4 | 4652 (29.1%) | Profil intermediaire | Alimentation & boissons 43.2%, Logement, eau, energie 22.7%, Ameublement & equipement 8.0% | Communication +1.4 pp, Habillement & chaussures +1.2 pp, Alimentation & boissons +1.1 pp |
| C5 | 2338 (14.6%) | Communication elevee | Alimentation & boissons 35.0%, Logement, eau, energie 27.2%, Communication 9.9% | Communication +4.8 pp, Sante +1.9 pp, Logement, eau, energie +1.7 pp |
| C6 | 2207 (13.8%) | Alimentation dominante | Alimentation & boissons 49.5%, Logement, eau, energie 25.6%, Ameublement & equipement 7.1% | Alimentation & boissons +7.4 pp, Habillement & chaussures +1.1 pp, Transport +0.6 pp |
| C7 | 2269 (14.2%) | Alimentation-logement | Alimentation & boissons 49.3%, Logement, eau, energie 30.1%, Ameublement & equipement 9.1% | Alimentation & boissons +7.2 pp, Logement, eau, energie +4.6 pp, Ameublement & equipement +0.8 pp |

#### K=8

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 1607 (10.1%) | Communication elevee | Alimentation & boissons 42.5%, Logement, eau, energie 23.6%, Communication 9.8% | Communication +4.7 pp, Habillement & chaussures +0.6 pp |
| C2 | 1279 (8.0%) | Logement tres eleve | Alimentation & boissons 47.7%, Logement, eau, energie 36.1%, Ameublement & equipement 5.1% | Logement, eau, energie +10.6 pp, Alimentation & boissons +5.6 pp |
| C3 | 2205 (13.8%) | Sante-transport aise | Alimentation & boissons 27.0%, Logement, eau, energie 18.7%, Sante 15.6% | Sante +8.8 pp, Transport +5.1 pp, Communication +3.8 pp |
| C4 | 1401 (8.8%) | Logement renforce | Alimentation & boissons 39.1%, Logement, eau, energie 28.7%, Communication 7.9% | Logement, eau, energie +3.2 pp, Communication +2.8 pp, Transport +1.3 pp |
| C5 | 2262 (14.2%) | Alimentation dominante | Alimentation & boissons 48.9%, Logement, eau, energie 26.1%, Ameublement & equipement 7.3% | Alimentation & boissons +6.8 pp, Habillement & chaussures +1.0 pp, Logement, eau, energie +0.7 pp |
| C6 | 1902 (11.9%) | Alimentation-logement | Alimentation & boissons 52.6%, Logement, eau, energie 29.3%, Ameublement & equipement 6.9% | Alimentation & boissons +10.5 pp, Logement, eau, energie +3.8 pp |
| C7 | 4109 (25.7%) | Profil intermediaire | Alimentation & boissons 44.4%, Logement, eau, energie 22.1%, Ameublement & equipement 8.0% | Alimentation & boissons +2.3 pp, Habillement & chaussures +1.3 pp, Communication +0.9 pp |
| C8 | 1205 (7.5%) | Equipement/logement | Alimentation & boissons 29.8%, Logement, eau, energie 29.7%, Ameublement & equipement 17.0% | Ameublement & equipement +8.8 pp, Logement, eau, energie +4.3 pp, Loisirs, culture & enseignement +2.6 pp |

#### K=9

| Cluster | Taille | Libelle comportemental | Postes dominants | Sur-representations |
| --- | --- | --- | --- | --- |
| C1 | 2007 (12.6%) | Sante-transport aise | Alimentation & boissons 27.1%, Logement, eau, energie 18.7%, Sante 16.6% | Sante +9.8 pp, Transport +5.2 pp, Communication +3.6 pp |
| C2 | 4151 (26.0%) | Profil intermediaire | Alimentation & boissons 44.3%, Logement, eau, energie 22.1%, Ameublement & equipement 8.0% | Alimentation & boissons +2.2 pp, Habillement & chaussures +1.3 pp, Communication +1.0 pp |
| C3 | 1138 (7.1%) | Equipement/logement | Logement, eau, energie 30.2%, Alimentation & boissons 29.8%, Ameublement & equipement 17.8% | Ameublement & equipement +9.6 pp, Logement, eau, energie +4.8 pp, Loisirs, culture & enseignement +1.7 pp |
| C4 | 2259 (14.1%) | Alimentation dominante | Alimentation & boissons 48.9%, Logement, eau, energie 26.1%, Ameublement & equipement 7.3% | Alimentation & boissons +6.8 pp, Habillement & chaussures +1.0 pp, Logement, eau, energie +0.6 pp |
| C5 | 162 (1.0%) | Profil intermediaire | Loisirs, culture & enseignement 28.4%, Alimentation & boissons 24.9%, Logement, eau, energie 15.8% | Loisirs, culture & enseignement +25.9 pp, Communication +2.9 pp, Transport +1.0 pp |
| C6 | 1906 (11.9%) | Alimentation-logement | Alimentation & boissons 52.8%, Logement, eau, energie 29.1%, Ameublement & equipement 6.8% | Alimentation & boissons +10.6 pp, Logement, eau, energie +3.7 pp |
| C7 | 1601 (10.0%) | Communication elevee | Alimentation & boissons 42.4%, Logement, eau, energie 23.6%, Communication 9.8% | Communication +4.8 pp, Sante +0.6 pp, Habillement & chaussures +0.5 pp |
| C8 | 1285 (8.0%) | Logement tres eleve | Alimentation & boissons 47.5%, Logement, eau, energie 36.1%, Ameublement & equipement 5.1% | Logement, eau, energie +10.7 pp, Alimentation & boissons +5.4 pp |
| C9 | 1461 (9.1%) | Logement renforce | Alimentation & boissons 38.5%, Logement, eau, energie 28.7%, Communication 8.1% | Logement, eau, energie +3.2 pp, Communication +3.0 pp, Transport +1.5 pp |

### Annexe : profils numeriques complets pour tous les K

Les valeurs ci-dessous sont exprimees en pourcentage de la depense totale du menage dans chaque cluster. Elles permettent de retrouver precisement la contribution de chaque poste G1-G9.

#### Profils numeriques K=2

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 7345 (46.0%) | Profil intermediaire | 38.8 | 4.0 | 21.6 | 3.4 | 8.1 | 8.7 | 5.3 | 7.2 | 2.9 |
| C2 | 8625 (54.0%) | Logement renforce | 45.0 | 2.1 | 28.8 | 2.6 | 8.3 | 5.2 | 2.6 | 3.3 | 2.2 |

#### Profils numeriques K=3

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 3625 (22.7%) | Alimentation dominante | 50.3 | 3.8 | 25.5 | 3.4 | 7.7 | 4.9 | 1.9 | 1.2 | 1.3 |
| C2 | 5264 (33.0%) | Logement renforce | 42.0 | 1.0 | 30.7 | 2.2 | 8.7 | 5.3 | 3.1 | 4.5 | 2.6 |
| C3 | 7081 (44.3%) | Profil intermediaire | 38.0 | 3.9 | 21.6 | 3.4 | 8.2 | 8.9 | 5.5 | 7.5 | 3.0 |

#### Profils numeriques K=4

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2790 (17.5%) | Logement tres eleve | 45.9 | 1.0 | 34.1 | 2.2 | 8.0 | 2.7 | 3.1 | 1.2 | 2.0 |
| C2 | 3309 (20.7%) | Alimentation dominante | 50.6 | 3.8 | 26.0 | 3.4 | 7.7 | 4.5 | 2.3 | 0.4 | 1.3 |
| C3 | 6536 (40.9%) | Profil intermediaire | 38.8 | 4.1 | 21.5 | 3.5 | 8.1 | 8.4 | 5.7 | 6.9 | 2.9 |
| C4 | 3335 (20.9%) | Communication elevee | 37.0 | 1.4 | 25.6 | 2.3 | 9.3 | 9.3 | 2.6 | 9.1 | 3.4 |

#### Profils numeriques K=5

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 3066 (19.2%) | Alimentation dominante | 50.1 | 3.8 | 26.2 | 3.4 | 7.8 | 4.6 | 2.4 | 0.3 | 1.4 |
| C2 | 1994 (12.5%) | Sante-transport aise | 26.2 | 3.8 | 18.5 | 3.1 | 8.3 | 15.8 | 9.8 | 8.6 | 5.9 |
| C3 | 3272 (20.5%) | Communication elevee | 39.0 | 1.4 | 26.0 | 2.4 | 9.4 | 8.1 | 1.8 | 9.2 | 2.7 |
| C4 | 4810 (30.1%) | Profil intermediaire | 43.9 | 4.1 | 22.6 | 3.6 | 7.8 | 5.9 | 4.2 | 6.0 | 1.9 |
| C5 | 2828 (17.7%) | Logement tres eleve | 45.4 | 1.0 | 34.0 | 2.1 | 8.1 | 2.8 | 3.2 | 1.3 | 2.1 |

#### Profils numeriques K=6

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2293 (14.4%) | Alimentation dominante | 49.5 | 3.8 | 25.8 | 3.5 | 7.5 | 4.5 | 4.0 | 0.2 | 1.3 |
| C2 | 2434 (15.2%) | Communication elevee | 35.9 | 0.9 | 26.9 | 2.1 | 9.9 | 8.7 | 2.7 | 9.6 | 3.3 |
| C3 | 1095 (6.9%) | Profil intermediaire | 47.2 | 3.8 | 23.0 | 3.2 | 8.2 | 6.6 | 0.0 | 6.4 | 1.5 |
| C4 | 4639 (29.0%) | Profil intermediaire | 43.1 | 4.1 | 22.5 | 3.6 | 8.0 | 6.0 | 4.2 | 6.6 | 2.0 |
| C5 | 3646 (22.8%) | Logement renforce | 47.0 | 1.5 | 32.6 | 2.4 | 8.1 | 3.2 | 2.2 | 1.0 | 2.0 |
| C6 | 1863 (11.7%) | Sante-transport aise | 26.2 | 3.8 | 18.2 | 3.1 | 8.0 | 16.4 | 9.8 | 8.5 | 5.9 |

#### Profils numeriques K=7

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1896 (11.9%) | Sante-transport aise | 26.5 | 3.8 | 18.3 | 3.2 | 8.0 | 16.4 | 9.6 | 8.4 | 5.8 |
| C2 | 1076 (6.7%) | Profil intermediaire | 46.9 | 3.8 | 22.5 | 3.2 | 7.8 | 6.8 | 0.0 | 7.4 | 1.5 |
| C3 | 1532 (9.6%) | Logement tres eleve | 44.3 | 1.5 | 35.6 | 2.0 | 7.5 | 1.6 | 3.3 | 1.9 | 2.3 |
| C4 | 4652 (29.1%) | Profil intermediaire | 43.2 | 4.1 | 22.7 | 3.6 | 8.0 | 5.9 | 4.1 | 6.4 | 2.0 |
| C5 | 2338 (14.6%) | Communication elevee | 35.0 | 0.9 | 27.2 | 2.0 | 9.8 | 8.7 | 2.9 | 9.9 | 3.6 |
| C6 | 2207 (13.8%) | Alimentation dominante | 49.5 | 4.0 | 25.6 | 3.5 | 7.1 | 4.4 | 4.4 | 0.1 | 1.4 |
| C7 | 2269 (14.2%) | Alimentation-logement | 49.3 | 1.4 | 30.1 | 2.7 | 9.1 | 4.6 | 1.1 | 0.3 | 1.4 |

#### Profils numeriques K=8

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1607 (10.1%) | Communication elevee | 42.5 | 3.5 | 23.6 | 3.1 | 8.2 | 7.3 | 0.1 | 9.8 | 2.0 |
| C2 | 1279 (8.0%) | Logement tres eleve | 47.7 | 1.4 | 36.1 | 2.2 | 5.1 | 1.1 | 2.4 | 2.5 | 1.6 |
| C3 | 2205 (13.8%) | Sante-transport aise | 27.0 | 3.8 | 18.7 | 3.2 | 8.2 | 15.6 | 8.9 | 8.8 | 5.7 |
| C4 | 1401 (8.8%) | Logement renforce | 39.1 | 0.3 | 28.7 | 2.2 | 7.8 | 6.9 | 5.1 | 7.9 | 2.1 |
| C5 | 2262 (14.2%) | Alimentation dominante | 48.9 | 3.9 | 26.1 | 3.4 | 7.3 | 4.4 | 4.4 | 0.2 | 1.4 |
| C6 | 1902 (11.9%) | Alimentation-logement | 52.6 | 1.3 | 29.3 | 2.9 | 6.9 | 4.4 | 0.8 | 0.7 | 1.3 |
| C7 | 4109 (25.7%) | Profil intermediaire | 44.4 | 4.3 | 22.1 | 3.7 | 8.0 | 5.7 | 4.0 | 6.0 | 1.9 |
| C8 | 1205 (7.5%) | Equipement/logement | 29.8 | 1.6 | 29.7 | 1.5 | 17.0 | 7.9 | 3.2 | 4.1 | 5.1 |

#### Profils numeriques K=9

| Cluster | Taille | Libelle comportemental | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2007 (12.6%) | Sante-transport aise | 27.1 | 3.8 | 18.7 | 3.2 | 8.3 | 16.6 | 9.1 | 8.7 | 4.5 |
| C2 | 4151 (26.0%) | Profil intermediaire | 44.3 | 4.3 | 22.1 | 3.7 | 8.0 | 5.7 | 4.0 | 6.1 | 1.9 |
| C3 | 1138 (7.1%) | Equipement/logement | 29.8 | 1.6 | 30.2 | 1.5 | 17.8 | 7.8 | 3.0 | 3.9 | 4.3 |
| C4 | 2259 (14.1%) | Alimentation dominante | 48.9 | 3.9 | 26.1 | 3.4 | 7.3 | 4.4 | 4.4 | 0.2 | 1.4 |
| C5 | 162 (1.0%) | Profil intermediaire | 24.9 | 3.6 | 15.8 | 2.6 | 5.2 | 6.6 | 4.9 | 8.0 | 28.4 |
| C6 | 1906 (11.9%) | Alimentation-logement | 52.8 | 1.3 | 29.1 | 2.9 | 6.8 | 4.4 | 0.8 | 0.7 | 1.2 |
| C7 | 1601 (10.0%) | Communication elevee | 42.4 | 3.5 | 23.6 | 3.1 | 8.2 | 7.4 | 0.1 | 9.8 | 1.9 |
| C8 | 1285 (8.0%) | Logement tres eleve | 47.5 | 1.4 | 36.1 | 2.2 | 5.1 | 1.1 | 2.5 | 2.5 | 1.7 |
| C9 | 1461 (9.1%) | Logement renforce | 38.5 | 0.3 | 28.7 | 2.2 | 7.9 | 7.0 | 5.3 | 8.1 | 2.1 |


## Synthese comparative 2007-2014

Le passage de 2007 a 2014 fait ressortir une structure plus diversifiee en 2014. La part alimentaire moyenne baisse, tandis que le logement, l'equipement, la communication et les depenses liees a des comportements plus urbains prennent davantage de place. Les deux enquetes revelent un axe central oppose : d'un cote les profils alimentaires-logement, souvent plus modestes et plus ruraux ; de l'autre les profils plus aises, plus urbains et plus diversifies, avec davantage de sante, transport, communication et loisirs. Le DMM capte donc non seulement des differences de structure budgetaire, mais aussi une stratification economique sous-jacente.

La solution K=6 est particulierement utile parce qu'elle evite deux ecueils : elle n'ecrase pas les comportements dans une opposition trop generale comme K=2 ou K=3, et elle evite la multiplication de micro-profils des solutions K=8 ou K=9. Elle donne une segmentation suffisamment expressive pour decrire les comportements des menages, tout en restant defendable statistiquement et economiquement.