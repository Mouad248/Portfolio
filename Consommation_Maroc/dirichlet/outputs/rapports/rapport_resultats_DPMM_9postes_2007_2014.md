# Rapport detaille des resultats DPMM - 9 postes, ENNVM 2007 et ENCDM 2014

Ce rapport analyse les resultats du Dirichlet Process Mixture Model tronque applique aux matrices de parts budgetaires en 9 postes. Contrairement au DMM fini, le DPMM ne choisit pas directement un K fixe : il utilise une troncature K_MAX=7, puis le nombre effectif de groupes est lu a partir des poids posteriori, des tailles affectees et de la stabilite comportementale des profils.

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

## Conclusion generale

Les resultats DPMM sont coherents avec les resultats DMM : les grands comportements recurrents sont les profils alimentaires, logement, sante, communication, transport et loisirs/culture. La difference principale est que le DPMM exprime cette segmentation comme une solution tronquee a K_MAX=7, avec parfois des composantes rares. Pour les deux bases, le K effectif comportemental est plutot compris entre 6 et 7. Une presentation conservatrice peut retenir 6 groupes substantiels ; une presentation plus fine peut garder 7 groupes en precisant que certains clusters sont rares.

## ENNVM 2007 - resultats DPMM 9 postes

### Structure moyenne de reference

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

### Comparaison des priors et nombre effectif de clusters

| Prior | K_MAX | alpha_DP moy. | K eff >1% | K eff >2% | K eff >3% | Plus petit cluster | n min | Prob. max moy. | Ambigus | Divergences |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 7 | 1.057 | 7 | 6 | 6 | 1.0% | 73 | 0.844 | 14.7% | 0 |
| gamma_1_2 | 7 | 1.138 | 7 | 7 | 6 | 2.0% | 138 | 0.829 | 16.8% | 0 |
| gamma_0p5_2 | 7 | 1.271 | 7 | 7 | 7 | 3.7% | 264 | 0.817 | 18.2% | 0 |
| gamma_0p25_2 | 7 | 0.908 | 7 | 6 | 6 | 1.0% | 72 | 0.825 | 16.6% | 0 |

Lecture : tous les priors utilisent formellement les 7 composantes de la troncature au seuil de 1%, mais certains produisent un petit cluster autour de 1% a 2%. La solution est donc mieux interpretee comme un K effectif de 6 a 7. Le prior gamma_1_1 donne la classification la plus nette, mais avec un petit groupe de 73 menages ; gamma_0p5_2 donne des groupes plus equilibres mais une ambiguite plus elevee. Pour la presentation, gamma_1_1 est retenu comme lecture principale, avec la reserve que son cluster C7 est un profil rare.

### Diagnostic socio-economique global par prior

| Prior | Prob. max | Ambigus | Part min | n min | Small <1% | n<100 | eta2 DAM | eta2 log_DAM | Associations dominantes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 0.844 | 14.7% | 1.0% | 73 | 0 | 1 | 0.227 | 0.270 | quintile_DAM=0.278 ; Quintiles=0.191 ; Niveau_scolaire_CM=0.185 ; Sexe_CM=0.174 ; Profession_CM=0.164 |
| gamma_1_2 | 0.829 | 16.8% | 2.0% | 138 | 0 | 0 | 0.282 | 0.324 | quintile_DAM=0.306 ; Quintiles=0.213 ; Milieu=0.195 ; Niveau_scolaire_CM=0.191 ; Sexe_CM=0.173 |
| gamma_0p5_2 | 0.817 | 18.2% | 3.7% | 264 | 0 | 0 | 0.255 | 0.326 | quintile_DAM=0.305 ; Quintiles=0.221 ; Milieu=0.211 ; Niveau_scolaire_CM=0.188 ; Sexe_CM=0.184 |
| gamma_0p25_2 | 0.825 | 16.6% | 1.0% | 72 | 0 | 1 | 0.240 | 0.293 | quintile_DAM=0.294 ; Quintiles=0.208 ; Niveau_scolaire_CM=0.188 ; Sexe_CM=0.179 ; Milieu=0.176 |

### Lecture principale des profils : gamma_1_1

#### Tailles, poids et concentration

| Cluster | Poids posteriori | Affectes | phi | G1 theorique | >1% |
| --- | --- | --- | --- | --- | --- |
| C1 | 20.6% | 1447 (20.5%) | 29.4 | 51.9% | oui |
| C2 | 19.7% | 1689 (23.9%) | 28.6 | 46.1% | oui |
| C3 | 7.3% | 399 (5.6%) | 21.3 | 46.1% | oui |
| C4 | 9.3% | 584 (8.3%) | 20.0 | 46.0% | oui |
| C5 | 33.8% | 2270 (32.1%) | 7.5 | 46.0% | oui |
| C6 | 8.2% | 600 (8.5%) | 20.7 | 28.9% | oui |
| C7 | 1.0% | 73 (1.0%) | 22.4 | 28.1% | oui |

#### Profils budgetaires detailles

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1447 (20.5%) | Alimentation dominante, communication faible | 52.5 | 4.1 | 22.2 | 3.9 | 6.3 | 5.5 | 3.9 | 0.2 | 1.4 |
| C2 | 1689 (23.9%) | Profil intermediaire | 45.9 | 4.5 | 19.1 | 4.0 | 7.0 | 5.6 | 3.9 | 8.0 | 2.0 |
| C3 | 399 (5.6%) | Communication elevee | 45.2 | 3.7 | 21.9 | 3.2 | 7.4 | 7.3 | 0.0 | 9.7 | 1.5 |
| C4 | 584 (8.3%) | Communication elevee | 44.1 | 0.1 | 23.4 | 2.7 | 6.7 | 8.1 | 4.3 | 9.0 | 1.6 |
| C5 | 2270 (32.1%) | Profil intermediaire | 49.5 | 1.6 | 27.9 | 2.5 | 7.2 | 4.6 | 2.2 | 2.7 | 1.9 |
| C6 | 600 (8.5%) | Sante tres elevee | 28.3 | 3.8 | 15.8 | 3.4 | 6.9 | 25.6 | 5.8 | 7.6 | 2.8 |
| C7 | 73 (1.0%) | Loisirs/culture extreme | 28.4 | 4.4 | 15.4 | 3.7 | 4.2 | 7.9 | 5.4 | 7.5 | 23.2 |

#### Caracterisation socio-economique

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1447 | 45231 | 40315 | -20.5% | 56.8% | 43.2% | Q2 (26.2%) |
| C2 | 1689 | 62347 | 52798 | +9.6% | 64.9% | 35.1% | Q4 (28.8%) |
| C3 | 399 | 50404 | 43070 | -11.4% | 58.4% | 41.6% | Q4 (25.3%) |
| C4 | 584 | 56773 | 45706 | -0.2% | 68.0% | 32.0% | Q3 (23.5%) |
| C5 | 2270 | 39183 | 29860 | -31.1% | 52.7% | 47.3% | Q1 (40.4%) |
| C6 | 600 | 133759 | 100648 | +135.1% | 77.2% | 22.8% | Q5 (68.2%) |
| C7 | 73 | 116679 | 94722 | +105.1% | 79.5% | 20.5% | Q5 (65.8%) |

### Sensibilite des profils aux priors

#### gamma_1_1

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1447 (20.5%) | Alimentation dominante, communication faible | G1 52.5%, G3 22.2%, G5 6.3% | G1 +6.0 pp, G2 +1.1 pp, G4 +0.6 pp | G8 -4.6 pp, G6 -1.8 pp |
| C2 | 1689 (23.9%) | Profil intermediaire | G1 45.9%, G3 19.1%, G8 8.0% | G8 +3.1 pp, G2 +1.5 pp, G4 +0.7 pp | G3 -3.7 pp, G6 -1.7 pp |
| C3 | 399 (5.6%) | Communication elevee | G1 45.2%, G3 21.9%, G8 9.7% | G8 +4.9 pp, G2 +0.7 pp, G5 +0.5 pp | G7 -3.3 pp, G1 -1.3 pp |
| C4 | 584 (8.3%) | Communication elevee | G1 44.1%, G3 23.4%, G8 9.0% | G8 +4.1 pp, G7 +0.9 pp, G6 +0.8 pp | G2 -2.9 pp, G1 -2.5 pp |
| C5 | 2270 (32.1%) | Profil intermediaire | G1 49.5%, G3 27.9%, G5 7.2% | G3 +5.2 pp, G1 +3.0 pp | G6 -2.7 pp, G8 -2.1 pp |
| C6 | 600 (8.5%) | Sante tres elevee | G1 28.3%, G6 25.6%, G3 15.8% | G6 +18.3 pp, G8 +2.8 pp, G7 +2.5 pp | G1 -18.2 pp, G3 -6.9 pp |
| C7 | 73 (1.0%) | Loisirs/culture extreme | G1 28.4%, G9 23.2%, G3 15.4% | G9 +21.1 pp, G8 +2.6 pp, G7 +2.1 pp | G1 -18.2 pp, G3 -7.3 pp |

#### gamma_1_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 2048 (29.0%) | Profil intermediaire | G1 50.9%, G3 28.2%, G5 7.0% | G3 +5.4 pp, G1 +4.3 pp | G6 -3.9 pp, G8 -2.9 pp |
| C2 | 1084 (15.3%) | Profil intermediaire | G1 49.9%, G3 19.0%, G8 8.5% | G8 +3.7 pp, G1 +3.4 pp, G2 +1.2 pp | G3 -3.8 pp, G6 -3.2 pp |
| C3 | 138 (2.0%) | Profil intermediaire | G1 49.6%, G6 17.2%, G3 13.2% | G6 +9.9 pp, G1 +3.0 pp, G2 +1.2 pp | G3 -9.5 pp, G5 -2.7 pp |
| C4 | 1063 (15.1%) | Communication elevee | G1 45.8%, G3 22.6%, G8 9.7% | G8 +4.9 pp | G7 -1.7 pp, G2 -1.6 pp |
| C5 | 1544 (21.9%) | Profil intermediaire | G1 51.2%, G3 22.8%, G5 6.6% | G1 +4.6 pp, G2 +1.2 pp, G4 +0.6 pp | G8 -4.5 pp, G6 -1.7 pp |
| C6 | 963 (13.6%) | Diversifie hors alimentaire | G1 31.8%, G3 19.0%, G6 12.7% | G6 +5.4 pp, G8 +3.8 pp, G7 +3.2 pp | G1 -14.8 pp, G3 -3.7 pp |
| C7 | 222 (3.1%) | Sante tres elevee | G6 41.7%, G1 23.7%, G3 13.2% | G6 +34.4 pp, G9 +1.4 pp, G8 +1.2 pp | G1 -22.9 pp, G3 -9.6 pp |

#### gamma_0p5_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1505 (21.3%) | Alimentation dominante, communication faible | G1 52.7%, G3 22.1%, G5 6.2% | G1 +6.1 pp, G2 +1.1 pp, G4 +0.6 pp | G8 -4.5 pp, G6 -1.8 pp |
| C2 | 794 (11.2%) | Communication elevee | G1 52.0%, G3 18.6%, G8 9.1% | G1 +5.4 pp, G8 +4.3 pp, G2 +1.0 pp | G3 -4.2 pp, G6 -3.5 pp |
| C3 | 847 (12.0%) | Communication elevee | G1 47.9%, G3 22.5%, G8 9.0% | G8 +4.2 pp, G1 +1.4 pp | G7 -2.0 pp, G2 -1.7 pp |
| C4 | 2019 (28.6%) | Profil intermediaire | G1 51.3%, G3 28.5%, G5 6.8% | G3 +5.8 pp, G1 +4.8 pp | G6 -3.9 pp, G8 -3.1 pp |
| C5 | 1273 (18.0%) | Profil intermediaire | G1 36.5%, G3 19.6%, G6 9.7% | G8 +2.7 pp, G6 +2.4 pp, G7 +2.2 pp | G1 -10.0 pp, G3 -3.2 pp |
| C6 | 264 (3.7%) | Sante tres elevee | G6 35.1%, G1 27.8%, G3 13.1% | G6 +27.8 pp, G8 +1.6 pp, G7 +0.8 pp | G1 -18.8 pp, G3 -9.7 pp |
| C7 | 360 (5.1%) | Communication elevee | G1 28.2%, G3 21.2%, G6 17.9% | G6 +10.6 pp, G8 +6.4 pp, G9 +3.4 pp | G1 -18.4 pp, G2 -1.6 pp |

#### gamma_0p25_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 1404 (19.9%) | Alimentation dominante, communication faible | G1 52.8%, G3 22.2%, G5 6.1% | G1 +6.3 pp, G2 +1.1 pp, G4 +0.6 pp | G8 -4.7 pp, G6 -1.9 pp |
| C2 | 340 (4.8%) | Communication elevee | G1 49.5%, G3 19.2%, G8 14.4% | G8 +9.5 pp, G1 +2.9 pp | G6 -4.0 pp, G5 -3.6 pp |
| C3 | 1166 (16.5%) | Communication elevee | G1 44.2%, G3 23.0%, G8 9.8% | G8 +4.9 pp, G6 +0.9 pp | G1 -2.4 pp, G2 -1.6 pp |
| C4 | 1446 (20.5%) | Profil intermediaire | G1 45.0%, G3 19.1%, G5 8.1% | G2 +1.7 pp, G5 +1.2 pp, G8 +1.2 pp | G3 -3.7 pp, G1 -1.6 pp |
| C5 | 2064 (29.2%) | Profil intermediaire | G1 50.0%, G3 28.3%, G5 7.1% | G3 +5.6 pp, G1 +3.4 pp | G6 -3.2 pp, G8 -2.9 pp |
| C6 | 570 (8.1%) | Sante tres elevee | G1 28.0%, G6 26.1%, G3 15.8% | G6 +18.8 pp, G8 +2.9 pp, G7 +2.6 pp | G1 -18.6 pp, G3 -7.0 pp |
| C7 | 72 (1.0%) | Loisirs/culture extreme | G1 28.4%, G9 23.3%, G3 15.3% | G9 +21.3 pp, G8 +2.7 pp, G7 +2.1 pp | G1 -18.1 pp, G3 -7.4 pp |

### Annexe numerique : profils complets par prior

#### Profils numeriques - gamma_1_1

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1447 (20.5%) | Alimentation dominante, communication faible | 52.5 | 4.1 | 22.2 | 3.9 | 6.3 | 5.5 | 3.9 | 0.2 | 1.4 |
| C2 | 1689 (23.9%) | Profil intermediaire | 45.9 | 4.5 | 19.1 | 4.0 | 7.0 | 5.6 | 3.9 | 8.0 | 2.0 |
| C3 | 399 (5.6%) | Communication elevee | 45.2 | 3.7 | 21.9 | 3.2 | 7.4 | 7.3 | 0.0 | 9.7 | 1.5 |
| C4 | 584 (8.3%) | Communication elevee | 44.1 | 0.1 | 23.4 | 2.7 | 6.7 | 8.1 | 4.3 | 9.0 | 1.6 |
| C5 | 2270 (32.1%) | Profil intermediaire | 49.5 | 1.6 | 27.9 | 2.5 | 7.2 | 4.6 | 2.2 | 2.7 | 1.9 |
| C6 | 600 (8.5%) | Sante tres elevee | 28.3 | 3.8 | 15.8 | 3.4 | 6.9 | 25.6 | 5.8 | 7.6 | 2.8 |
| C7 | 73 (1.0%) | Loisirs/culture extreme | 28.4 | 4.4 | 15.4 | 3.7 | 4.2 | 7.9 | 5.4 | 7.5 | 23.2 |

#### Profils numeriques - gamma_1_2

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2048 (29.0%) | Profil intermediaire | 50.9 | 1.7 | 28.2 | 2.5 | 7.0 | 3.4 | 2.4 | 1.9 | 1.9 |
| C2 | 1084 (15.3%) | Profil intermediaire | 49.9 | 4.2 | 19.0 | 3.7 | 5.9 | 4.1 | 3.2 | 8.5 | 1.5 |
| C3 | 138 (2.0%) | Profil intermediaire | 49.6 | 4.3 | 13.2 | 3.9 | 4.1 | 17.2 | 2.6 | 3.9 | 1.3 |
| C4 | 1063 (15.1%) | Communication elevee | 45.8 | 1.4 | 22.6 | 2.8 | 7.3 | 7.1 | 1.7 | 9.7 | 1.6 |
| C5 | 1544 (21.9%) | Profil intermediaire | 51.2 | 4.2 | 22.8 | 3.9 | 6.6 | 5.5 | 3.9 | 0.3 | 1.5 |
| C6 | 963 (13.6%) | Diversifie hors alimentaire | 31.8 | 4.5 | 19.0 | 4.3 | 8.4 | 12.7 | 6.5 | 8.6 | 4.3 |
| C7 | 222 (3.1%) | Sante tres elevee | 23.7 | 1.9 | 13.2 | 2.1 | 4.8 | 41.7 | 3.2 | 6.0 | 3.5 |

#### Profils numeriques - gamma_0p5_2

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1505 (21.3%) | Alimentation dominante, communication faible | 52.7 | 4.1 | 22.1 | 3.9 | 6.2 | 5.4 | 3.8 | 0.3 | 1.4 |
| C2 | 794 (11.2%) | Communication elevee | 52.0 | 4.0 | 18.6 | 3.6 | 4.9 | 3.8 | 2.8 | 9.1 | 1.3 |
| C3 | 847 (12.0%) | Communication elevee | 47.9 | 1.4 | 22.5 | 3.0 | 7.1 | 6.4 | 1.3 | 9.0 | 1.4 |
| C4 | 2019 (28.6%) | Profil intermediaire | 51.3 | 1.7 | 28.5 | 2.6 | 6.8 | 3.4 | 2.3 | 1.7 | 1.7 |
| C5 | 1273 (18.0%) | Profil intermediaire | 36.5 | 4.8 | 19.6 | 4.3 | 8.7 | 9.7 | 5.6 | 7.6 | 3.3 |
| C6 | 264 (3.7%) | Sante tres elevee | 27.8 | 3.1 | 13.1 | 2.9 | 4.8 | 35.1 | 4.1 | 6.4 | 2.7 |
| C7 | 360 (5.1%) | Communication elevee | 28.2 | 1.4 | 21.2 | 1.7 | 8.6 | 17.9 | 4.4 | 11.2 | 5.4 |

#### Profils numeriques - gamma_0p25_2

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1404 (19.9%) | Alimentation dominante, communication faible | 52.8 | 4.1 | 22.2 | 3.9 | 6.1 | 5.4 | 3.8 | 0.2 | 1.4 |
| C2 | 340 (4.8%) | Communication elevee | 49.5 | 3.4 | 19.2 | 3.3 | 3.3 | 3.3 | 2.6 | 14.4 | 1.1 |
| C3 | 1166 (16.5%) | Communication elevee | 44.2 | 1.4 | 23.0 | 2.7 | 7.2 | 8.2 | 1.9 | 9.8 | 1.6 |
| C4 | 1446 (20.5%) | Profil intermediaire | 45.0 | 4.7 | 19.1 | 4.2 | 8.1 | 6.5 | 4.3 | 6.0 | 2.2 |
| C5 | 2064 (29.2%) | Profil intermediaire | 50.0 | 1.7 | 28.3 | 2.6 | 7.1 | 4.1 | 2.5 | 1.9 | 1.9 |
| C6 | 570 (8.1%) | Sante tres elevee | 28.0 | 3.8 | 15.8 | 3.4 | 6.5 | 26.1 | 5.9 | 7.8 | 2.8 |
| C7 | 72 (1.0%) | Loisirs/culture extreme | 28.4 | 4.4 | 15.3 | 3.7 | 4.0 | 7.8 | 5.5 | 7.5 | 23.3 |


## ENCDM 2014 - resultats DPMM 9 postes

### Structure moyenne de reference

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

### Comparaison des priors et nombre effectif de clusters

| Prior | K_MAX | alpha_DP moy. | K eff >1% | K eff >2% | K eff >3% | Plus petit cluster | n min | Prob. max moy. | Ambigus | Divergences |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 7 | 1.511 | 7 | 6 | 6 | 1.0% | 165 | 0.801 | 20.0% | 0 |
| gamma_1_2 | 7 | 1.340 | 7 | 6 | 6 | 1.5% | 242 | 0.805 | 19.3% | 0 |
| gamma_0p5_2 | 7 | 1.469 | 6 | 6 | 6 | 0.9% | 146 | 0.774 | 22.6% | 0 |
| gamma_0p25_2 | 7 | 1.058 | 7 | 7 | 6 | 2.6% | 411 | 0.827 | 17.1% | 0 |

Lecture : le cas 2014 montre plus clairement le debat entre K=6 et K=7 effectifs. gamma_0p5_2 indique seulement 6 clusters au seuil de poids posteriori de 1%, tandis que gamma_1_1 et gamma_1_2 gardent un petit groupe proche de 1%. gamma_0p25_2 offre le meilleur compromis de qualite d'affectation et de tailles non minuscules. Il est donc retenu comme lecture principale, avec K effectif proche de 7 mais une lecture conservatrice possible a 6.

### Diagnostic socio-economique global par prior

| Prior | Prob. max | Ambigus | Part min | n min | Small <1% | n<100 | eta2 DAM | eta2 log_DAM | Associations dominantes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gamma_1_1 | 0.801 | 20.0% | 1.0% | 165 | 0 | 0 | 0.286 | 0.341 | quintile_DAM=0.311 ; Diplôme_agregé_CM=0.264 ; Quintiles=0.225 ; Quintileurbain=0.203 ; Milieu=0.199 |
| gamma_1_2 | 0.805 | 19.3% | 1.5% | 242 | 0 | 0 | 0.289 | 0.342 | quintile_DAM=0.312 ; Diplôme_agregé_CM=0.264 ; Quintiles=0.225 ; Quintileurbain=0.205 ; Milieu=0.205 |
| gamma_0p5_2 | 0.774 | 22.6% | 0.9% | 146 | 1 | 0 | 0.243 | 0.316 | quintile_DAM=0.309 ; Diplôme_agregé_CM=0.252 ; Milieu=0.208 ; Quintiles=0.202 ; Sexe_CM=0.195 |
| gamma_0p25_2 | 0.827 | 17.1% | 2.6% | 411 | 0 | 0 | 0.287 | 0.326 | quintile_DAM=0.301 ; Diplôme_agregé_CM=0.281 ; Quintiles=0.206 ; Milieu=0.202 ; Quintileurbain=0.191 |

### Lecture principale des profils : gamma_0p25_2

#### Tailles, poids et concentration

| Cluster | Poids posteriori | Affectes | phi | G1 theorique | >1% |
| --- | --- | --- | --- | --- | --- |
| C1 | 38.8% | 5872 (36.8%) | 10.6 | 47.0% | oui |
| C2 | 28.9% | 5289 (33.1%) | 28.0 | 43.6% | oui |
| C3 | 15.8% | 2364 (14.8%) | 15.8 | 40.5% | oui |
| C4 | 3.7% | 619 (3.9%) | 30.7 | 28.9% | oui |
| C5 | 3.9% | 578 (3.6%) | 24.8 | 28.6% | oui |
| C6 | 6.4% | 837 (5.2%) | 11.8 | 28.4% | oui |
| C7 | 2.6% | 411 (2.6%) | 27.8 | 26.7% | oui |

#### Profils budgetaires detailles

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 5872 (36.8%) | Alimentation dominante, communication faible | 47.5 | 2.2 | 30.2 | 2.7 | 8.1 | 3.6 | 2.7 | 0.9 | 1.9 |
| C2 | 5289 (33.1%) | Profil intermediaire | 43.8 | 4.1 | 22.7 | 3.6 | 8.1 | 6.1 | 4.0 | 5.7 | 1.9 |
| C3 | 2364 (14.8%) | Communication elevee | 40.9 | 2.0 | 24.8 | 2.7 | 9.0 | 7.9 | 0.5 | 10.1 | 2.2 |
| C4 | 619 (3.9%) | Sante tres elevee | 28.2 | 3.3 | 16.3 | 2.7 | 6.1 | 29.0 | 4.5 | 6.8 | 3.1 |
| C5 | 578 (3.6%) | Communication elevee | 26.9 | 4.6 | 16.7 | 3.8 | 7.6 | 9.8 | 7.2 | 11.3 | 12.1 |
| C6 | 837 (5.2%) | Communication elevee | 26.1 | 1.0 | 28.0 | 1.7 | 10.3 | 10.5 | 8.1 | 9.7 | 4.5 |
| C7 | 411 (2.6%) | Transport tres eleve | 25.6 | 3.5 | 18.4 | 3.1 | 7.4 | 9.4 | 23.6 | 6.2 | 2.9 |

#### Caracterisation socio-economique

| Cluster | n | DAM moy. | DAM med. | Ecart DAM | Urbain | Rural | Quintile surrep. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 5872 | 47378 | 41643 | -36.9% | 56.2% | 43.8% | Q1 (38.4%) |
| C2 | 5289 | 76018 | 66541 | +1.3% | 67.2% | 32.8% | Q4 (28.9%) |
| C3 | 2364 | 68593 | 58023 | -8.6% | 62.0% | 38.0% | Q3 (22.7%) |
| C4 | 619 | 149291 | 127845 | +98.9% | 75.3% | 24.7% | Q5 (66.2%) |
| C5 | 578 | 160180 | 134728 | +113.4% | 87.7% | 12.3% | Q5 (70.6%) |
| C6 | 837 | 120094 | 88965 | +60.0% | 84.9% | 15.1% | Q5 (44.6%) |
| C7 | 411 | 172514 | 147326 | +129.8% | 91.5% | 8.5% | Q5 (73.7%) |

### Sensibilite des profils aux priors

#### gamma_1_1

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 5810 (36.4%) | Alimentation dominante, communication faible | G1 47.6%, G3 30.3%, G5 8.1% | G1 +5.5 pp, G3 +4.9 pp | G8 -4.1 pp, G6 -3.2 pp |
| C2 | 4279 (26.8%) | Profil intermediaire | G1 45.7%, G3 22.9%, G5 7.8% | G1 +3.6 pp, G2 +1.2 pp, G4 +0.7 pp | G3 -2.6 pp, G6 -1.5 pp |
| C3 | 837 (5.2%) | Profil intermediaire | G1 43.6%, G3 27.6%, G5 7.4% | G3 +2.1 pp, G8 +1.8 pp, G1 +1.5 pp | G2 -2.9 pp, G9 -1.1 pp |
| C4 | 1360 (8.5%) | Communication elevee | G1 43.5%, G3 23.1%, G8 9.2% | G8 +4.1 pp, G1 +1.4 pp, G2 +0.7 pp | G7 -3.8 pp, G3 -2.4 pp |
| C5 | 2469 (15.5%) | Sante-transport aise | G1 28.6%, G3 19.4%, G6 14.9% | G6 +8.1 pp, G7 +4.6 pp, G8 +3.8 pp | G1 -13.6 pp, G3 -6.1 pp |
| C6 | 165 (1.0%) | Loisirs/culture extreme | G1 29.1%, G9 25.7%, G3 15.7% | G9 +23.2 pp, G8 +2.4 pp, G2 +0.7 pp | G1 -13.0 pp, G3 -9.8 pp |
| C7 | 1050 (6.6%) | Communication elevee | G1 27.9%, G3 26.5%, G8 12.3% | G8 +7.2 pp, G6 +5.0 pp, G5 +2.8 pp | G1 -14.2 pp, G2 -1.8 pp |

#### gamma_1_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 5829 (36.5%) | Alimentation dominante, communication faible | G1 47.6%, G3 30.3%, G5 8.0% | G1 +5.5 pp, G3 +4.8 pp | G8 -4.1 pp, G6 -3.2 pp |
| C2 | 4328 (27.1%) | Profil intermediaire | G1 45.6%, G3 22.8%, G5 7.8% | G1 +3.5 pp, G2 +1.2 pp, G4 +0.7 pp | G3 -2.6 pp, G6 -1.5 pp |
| C3 | 829 (5.2%) | Profil intermediaire | G1 43.9%, G3 27.6%, G5 7.4% | G3 +2.1 pp, G1 +1.8 pp, G8 +1.7 pp | G2 -2.9 pp, G9 -1.2 pp |
| C4 | 1244 (7.8%) | Profil intermediaire | G1 43.9%, G3 23.6%, G5 8.9% | G8 +2.8 pp, G1 +1.8 pp, G2 +0.7 pp | G7 -3.8 pp, G3 -1.9 pp |
| C5 | 2494 (15.6%) | Sante-transport aise | G1 28.5%, G3 19.2%, G6 14.8% | G6 +8.0 pp, G7 +4.7 pp, G8 +3.1 pp | G1 -13.6 pp, G3 -6.2 pp |
| C6 | 242 (1.5%) | Communication extreme | G1 31.8%, G8 31.7%, G3 16.9% | G8 +26.6 pp | G1 -10.3 pp, G3 -8.6 pp |
| C7 | 1004 (6.3%) | Communication elevee | G1 28.0%, G3 27.0%, G6 12.4% | G6 +5.6 pp, G8 +5.0 pp, G5 +3.1 pp | G1 -14.1 pp, G2 -1.9 pp |

#### gamma_0p5_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 4230 (26.5%) | Alimentation dominante, communication faible | G1 49.9%, G3 27.4%, G5 8.0% | G1 +7.8 pp, G3 +1.9 pp | G8 -4.8 pp, G6 -2.3 pp |
| C2 | 3840 (24.0%) | Profil intermediaire | G1 46.0%, G3 23.1%, G5 7.5% | G1 +3.9 pp, G2 +1.3 pp, G4 +0.7 pp | G3 -2.4 pp, G6 -1.9 pp |
| C3 | 2162 (13.5%) | Communication elevee | G1 41.1%, G3 24.9%, G8 10.4% | G8 +5.3 pp, G6 +0.7 pp, G5 +0.6 pp | G7 -3.6 pp, G1 -1.0 pp |
| C4 | 2795 (17.5%) | Sante-transport aise | G1 30.2%, G3 18.7%, G6 14.4% | G6 +7.7 pp, G7 +3.8 pp, G8 +3.6 pp | G1 -11.9 pp, G3 -6.8 pp |
| C5 | 146 (0.9%) | Loisirs/culture extreme | G1 29.8%, G9 27.7%, G3 14.8% | G9 +25.2 pp, G8 +2.0 pp, G2 +0.7 pp | G1 -12.3 pp, G3 -10.7 pp |
| C6 | 1098 (6.9%) | Profil intermediaire | G1 33.4%, G3 29.7%, G5 9.0% | G3 +4.2 pp, G7 +4.1 pp, G8 +1.8 pp | G1 -8.7 pp, G2 -2.4 pp |
| C7 | 1699 (10.6%) | Profil intermediaire | G1 41.4%, G3 36.2%, G5 8.7% | G3 +10.7 pp | G6 -4.2 pp, G8 -2.6 pp |

#### gamma_0p25_2

| Cluster | Taille | Libelle | Postes dominants | Sur-representations | Sous-representations |
| --- | --- | --- | --- | --- | --- |
| C1 | 5872 (36.8%) | Alimentation dominante, communication faible | G1 47.5%, G3 30.2%, G5 8.1% | G1 +5.4 pp, G3 +4.8 pp | G8 -4.2 pp, G6 -3.1 pp |
| C2 | 5289 (33.1%) | Profil intermediaire | G1 43.8%, G3 22.7%, G5 8.1% | G1 +1.6 pp, G2 +1.2 pp, G8 +0.7 pp | G3 -2.8 pp, G6 -0.7 pp |
| C3 | 2364 (14.8%) | Communication elevee | G1 40.9%, G3 24.8%, G8 10.1% | G8 +5.1 pp, G6 +1.1 pp, G5 +0.8 pp | G7 -3.4 pp, G1 -1.2 pp |
| C4 | 619 (3.9%) | Sante tres elevee | G6 29.0%, G1 28.2%, G3 16.3% | G6 +22.2 pp, G8 +1.8 pp, G9 +0.6 pp | G1 -13.9 pp, G3 -9.2 pp |
| C5 | 578 (3.6%) | Communication elevee | G1 26.9%, G3 16.7%, G9 12.1% | G9 +9.6 pp, G8 +6.3 pp, G7 +3.3 pp | G1 -15.2 pp, G3 -8.8 pp |
| C6 | 837 (5.2%) | Communication elevee | G3 28.0%, G1 26.1%, G6 10.5% | G8 +4.7 pp, G7 +4.3 pp, G6 +3.7 pp | G1 -16.1 pp, G2 -1.9 pp |
| C7 | 411 (2.6%) | Transport tres eleve | G1 25.6%, G7 23.6%, G3 18.4% | G7 +19.7 pp, G6 +2.6 pp, G8 +1.1 pp | G1 -16.5 pp, G3 -7.1 pp |

### Annexe numerique : profils complets par prior

#### Profils numeriques - gamma_1_1

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 5810 (36.4%) | Alimentation dominante, communication faible | 47.6 | 2.2 | 30.3 | 2.7 | 8.1 | 3.6 | 2.7 | 0.9 | 1.8 |
| C2 | 4279 (26.8%) | Profil intermediaire | 45.7 | 4.2 | 22.9 | 3.7 | 7.8 | 5.2 | 4.0 | 4.9 | 1.7 |
| C3 | 837 (5.2%) | Profil intermediaire | 43.6 | 0.0 | 27.6 | 2.7 | 7.4 | 6.0 | 4.4 | 6.8 | 1.4 |
| C4 | 1360 (8.5%) | Communication elevee | 43.5 | 3.6 | 23.1 | 3.2 | 8.6 | 7.1 | 0.1 | 9.2 | 1.7 |
| C5 | 2469 (15.5%) | Sante-transport aise | 28.6 | 3.8 | 19.4 | 3.2 | 8.6 | 14.9 | 8.5 | 8.9 | 4.2 |
| C6 | 165 (1.0%) | Loisirs/culture extreme | 29.1 | 3.6 | 15.7 | 3.0 | 5.3 | 5.6 | 4.5 | 7.5 | 25.7 |
| C7 | 1050 (6.6%) | Communication elevee | 27.9 | 1.1 | 26.5 | 1.5 | 11.0 | 11.8 | 3.3 | 12.3 | 4.6 |

#### Profils numeriques - gamma_1_2

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 5829 (36.5%) | Alimentation dominante, communication faible | 47.6 | 2.2 | 30.3 | 2.7 | 8.0 | 3.6 | 2.7 | 1.0 | 1.8 |
| C2 | 4328 (27.1%) | Profil intermediaire | 45.6 | 4.2 | 22.8 | 3.7 | 7.8 | 5.3 | 3.9 | 5.0 | 1.7 |
| C3 | 829 (5.2%) | Profil intermediaire | 43.9 | 0.0 | 27.6 | 2.7 | 7.4 | 6.0 | 4.4 | 6.8 | 1.3 |
| C4 | 1244 (7.8%) | Profil intermediaire | 43.9 | 3.6 | 23.6 | 3.2 | 8.9 | 7.3 | 0.1 | 7.8 | 1.7 |
| C5 | 2494 (15.6%) | Sante-transport aise | 28.5 | 3.8 | 19.2 | 3.2 | 8.5 | 14.8 | 8.6 | 8.2 | 5.2 |
| C6 | 242 (1.5%) | Communication extreme | 31.8 | 3.3 | 16.9 | 3.4 | 5.3 | 4.3 | 1.8 | 31.7 | 1.5 |
| C7 | 1004 (6.3%) | Communication elevee | 28.0 | 1.0 | 27.0 | 1.4 | 11.4 | 12.4 | 3.3 | 10.1 | 5.5 |

#### Profils numeriques - gamma_0p5_2

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 4230 (26.5%) | Alimentation dominante, communication faible | 49.9 | 2.7 | 27.4 | 3.1 | 8.0 | 4.5 | 2.5 | 0.2 | 1.5 |
| C2 | 3840 (24.0%) | Profil intermediaire | 46.0 | 4.2 | 23.1 | 3.7 | 7.5 | 4.9 | 3.8 | 5.3 | 1.6 |
| C3 | 2162 (13.5%) | Communication elevee | 41.1 | 2.1 | 24.9 | 2.7 | 8.8 | 7.5 | 0.3 | 10.4 | 2.2 |
| C4 | 2795 (17.5%) | Sante-transport aise | 30.2 | 4.1 | 18.7 | 3.4 | 8.7 | 14.4 | 7.7 | 8.7 | 4.2 |
| C5 | 146 (0.9%) | Loisirs/culture extreme | 29.8 | 3.6 | 14.8 | 2.5 | 5.2 | 5.4 | 4.0 | 7.1 | 27.7 |
| C6 | 1098 (6.9%) | Profil intermediaire | 33.4 | 0.5 | 29.7 | 1.8 | 9.0 | 8.0 | 8.0 | 6.9 | 2.7 |
| C7 | 1699 (10.6%) | Profil intermediaire | 41.4 | 1.4 | 36.2 | 1.9 | 8.7 | 2.5 | 3.0 | 2.5 | 2.5 |

#### Profils numeriques - gamma_0p25_2

| Cluster | Taille | Libelle | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 5872 (36.8%) | Alimentation dominante, communication faible | 47.5 | 2.2 | 30.2 | 2.7 | 8.1 | 3.6 | 2.7 | 0.9 | 1.9 |
| C2 | 5289 (33.1%) | Profil intermediaire | 43.8 | 4.1 | 22.7 | 3.6 | 8.1 | 6.1 | 4.0 | 5.7 | 1.9 |
| C3 | 2364 (14.8%) | Communication elevee | 40.9 | 2.0 | 24.8 | 2.7 | 9.0 | 7.9 | 0.5 | 10.1 | 2.2 |
| C4 | 619 (3.9%) | Sante tres elevee | 28.2 | 3.3 | 16.3 | 2.7 | 6.1 | 29.0 | 4.5 | 6.8 | 3.1 |
| C5 | 578 (3.6%) | Communication elevee | 26.9 | 4.6 | 16.7 | 3.8 | 7.6 | 9.8 | 7.2 | 11.3 | 12.1 |
| C6 | 837 (5.2%) | Communication elevee | 26.1 | 1.0 | 28.0 | 1.7 | 10.3 | 10.5 | 8.1 | 9.7 | 4.5 |
| C7 | 411 (2.6%) | Transport tres eleve | 25.6 | 3.5 | 18.4 | 3.1 | 7.4 | 9.4 | 23.6 | 6.2 | 2.9 |


## Synthese comparative 2007-2014

En 2007, les profils DPMM font ressortir une forte opposition entre profils alimentaires/logement et profils a forte sante ou communication. Les petits clusters correspondent a des comportements rares mais economiquement lisibles, notamment loisirs/culture ou sante tres elevee. En 2014, la structure est plus diversifiee : le modele isole plus nettement les comportements de transport, communication et loisirs/culture, en plus des profils alimentaires et logement. Cela confirme une diversification de la structure budgetaire entre 2007 et 2014.