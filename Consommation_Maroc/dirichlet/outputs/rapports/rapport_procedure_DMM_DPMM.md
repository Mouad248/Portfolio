# Rapport technique sur la procedure d'estimation DMM et DPMM

## 1. Objet du rapport

Ce rapport decrit la procedure technique mise en place pour construire, estimer et exploiter des modeles de melange de Dirichlet appliques aux structures de depenses des menages. Il couvre uniquement la chaine methodologique allant de la creation des matrices de parts budgetaires jusqu'a l'obtention des clusters et des fichiers de sortie. Il ne traite pas de l'interpretation economique finale des groupes, ni de la discussion substantielle du meilleur nombre de classes.

Le projet travaille sur deux enquetes de consommation des menages :

- ENNVM 2007 ;
- ENCDM 2014.

Pour chaque enquete, deux niveaux de representation des depenses ont ete construits :

- une representation agregee en 9 grands postes, notee `G1` a `G9` ;
- une representation plus fine en 23 postes, notee `S1` a `S23`.

Deux familles de modeles ont ensuite ete utilisees :

- le DMM, ou Dirichlet Mixture Model fini, estime pour plusieurs valeurs de `K` ;
- le DPMM, ou Dirichlet Process Mixture Model tronque, estime par approche bayesienne avec NUTS.

L'objectif technique est d'obtenir, pour chaque menage, une affectation probabiliste a des groupes de comportement budgetaire, ainsi que des profils moyens de clusters exploitables pour l'analyse.

## 2. Organisation generale du projet

La procedure est repartie en plusieurs familles de scripts.

Les scripts de creation de matrices sont places dans `matrix_creation/`. Ils lisent les bases brutes, nettoient les variables de depenses, construisent les parts budgetaires et exportent des matrices pretes pour les modeles.

Les scripts DMM sont places dans `DMM/`. Ils estiment des melanges finis de Dirichlet pour `K = 2, ..., 9`, produisent les responsabilites posteriori, les affectations de clusters, les profils moyens et les parametres de Dirichlet estimes.

Les scripts DPMM sont places dans `DPMM/`. Ils estiment des melanges de Dirichlet bayesiens tronques avec `K_MAX = 7`, en utilisant NUTS, une representation stick-breaking et plusieurs priors sur le parametre de concentration du processus de Dirichlet.

Les scripts de diagnostic sont places dans `Diagnostics/`. Ils n'ont pas pour role de re-estimer les modeles. Ils lisent les fichiers produits par les modeles et construisent des tableaux de controle : qualite d'affectation, tailles des clusters, profils, tests statistiques et croisements avec les variables socio-economiques.

## 3. Creation des matrices de parts budgetaires

### 3.1 Principe statistique

Les modeles de Dirichlet s'appliquent a des vecteurs de proportions strictement positives et dont la somme vaut 1. Pour chaque menage `i`, on construit donc un vecteur :

```text
W_i = (w_i1, w_i2, ..., w_iJ)
```

avec :

```text
w_ij > 0
sum_j w_ij = 1
```

Dans les scripts, `J = 9` pour les matrices en 9 postes et `J = 23` pour les matrices fines.

La part budgetaire brute d'un poste est calculee comme :

```text
w_ij = depense_ij / DAM_i
```

ou `DAM_i` represente la depense annuelle totale du menage.

### 3.2 Matrices en 9 postes

Les scripts concernes sont :

- `matrix_creation/matrice_ennvm_9.py` ;
- `matrix_creation/matrice_encdm_9.py`.

Ces scripts utilisent les colonnes :

```text
DAM_G1, DAM_G2, ..., DAM_G9
```

et construisent :

```text
w_G1, w_G2, ..., w_G9
```

La procedure technique est la suivante :

1. lecture de la base brute Excel ;
2. verification de l'existence de `DAM` et des colonnes `DAM_G1` a `DAM_G9` ;
3. conversion numerique des colonnes de depenses ;
4. exclusion des menages avec `DAM` manquant ou non positif ;
5. exclusion des depenses de postes manquantes ou negatives ;
6. calcul des parts `w_Gj = DAM_Gj / DAM` ;
7. calcul de `sum_w` pour controler si les parts couvrent la totalite de la depense ;
8. normalisation ligne par ligne pour obtenir une somme exactement egale a 1 ;
9. remplacement des zeros par un petit epsilon ;
10. renormalisation apres epsilon.

L'epsilon utilise est :

```text
EPSILON = 1e-6
```

Cette correction est indispensable car la loi de Dirichlet n'est pas definie sur des composantes nulles. Sans cette correction, le terme `log(W)` dans la vraisemblance produirait des valeurs infinies ou non definies.

Les sorties principales sont :

- `data/processed/ennvm_2007_parts_budgetaires.xlsx` ;
- `data/processed/encdm_2014_parts_budgetaires.xlsx`.

### 3.3 Matrices en 23 postes

Les scripts concernes sont :

- `matrix_creation/matrice_ennvm_23.py` ;
- `matrix_creation/matrice_encdm_23.py`.

La matrice en 23 postes n'est pas directement lue depuis 23 variables brutes finales. Elle est reconstruite a partir de sous-postes de depenses `DAM_Gxx`.

Le mapping principal est :

```text
S1  = DAM_G01
S2  = DAM_G02 + DAM_G04 + DAM_G05
S3  = DAM_G06 + DAM_G07 + DAM_G08
S4  = DAM_G09 + DAM_G10
S5  = DAM_G13 + DAM_G14
S6  = DAM_G03 + DAM_G11 + DAM_G12 + DAM_G15 + DAM_G17 + DAM_G18
S7  = DAM_G21 + ... + DAM_G28
S8  = DAM_G31
S9  = DAM_G32 + DAM_G34
S10 = DAM_G41 + ... + DAM_G47
S11 = DAM_G33
S12 = DAM_G51
S13 = DAM_G52 + DAM_G53
S14 = DAM_G61
S15 = DAM_G62
S16 = DAM_G63
S17 = DAM_G71 + DAM_G72 + DAM_G73 + DAM_G74
S18 = DAM_G75 + DAM_G76, avec DAM_G77 ajoute dans ENCDM 2014
S19 = DAM_G81 + DAM_G82 + DAM_G83 + DAM_G84
S20 = DAM_G87 + DAM_G88
S21 = DAM_G85 + DAM_G86
S22 = DAM_G89
S23 = DAM_G91 + DAM_G92 + DAM_G93 + DAM_G94
```

Apres construction des montants `S1` a `S23`, les parts sont creees sous la forme :

```text
w_S1, w_S2, ..., w_S23
```

La procedure est analogue au cas 9 postes, avec une difference importante : les valeurs manquantes des sous-postes sont remplacees par zero apres verification de `DAM`, puis les postes agreges `S` sont construits. Les parts sont ensuite normalisees et corrigees par epsilon.

Les sorties principales sont :

- `data/processed/ennvm_2007_parts_budgetaires_23.xlsx` ;
- `data/processed/encdm_2014_parts_budgetaires_23.xlsx`.

## 4. Modele DMM : melange fini de Dirichlet

### 4.1 Idee generale

Le DMM suppose que la population observee est composee de `K` sous-populations latentes. Chaque sous-population possede son propre profil de parts budgetaires. Conditionnellement au cluster latent `z_i`, le vecteur de parts du menage suit une loi de Dirichlet :

```text
W_i | z_i = k ~ Dirichlet(alpha_k)
```

avec :

```text
P(z_i = k) = pi_k
sum_k pi_k = 1
```

Le modele melange donc plusieurs densites de Dirichlet :

```text
f(W_i) = sum_k pi_k Dirichlet(W_i ; alpha_k)
```

Chaque composante `k` represente un type de structure budgetaire. Le vecteur `alpha_k` controle a la fois le centre du profil et sa concentration. Le profil moyen theorique d'une composante est :

```text
E[W_j | k] = alpha_kj / sum_j alpha_kj
```

La somme `alpha_sum = sum_j alpha_kj` mesure la concentration autour de ce profil moyen : plus elle est elevee, plus les menages du cluster sont homogenes autour de leur profil moyen.

### 4.2 Scripts DMM

Les scripts DMM sont :

- `DMM/dmm_ennvm_9.py` ;
- `DMM/dmm_encdm_9.py` ;
- `DMM/dmm_ennvm_23.py` ;
- `DMM/dmm_encdm_23.py`.

Ils utilisent les matrices traitees dans `data/processed/`.

Pour les matrices 9 postes, les colonnes de modelisation sont :

```text
w_G1, ..., w_G9
```

Pour les matrices 23 postes, les colonnes sont :

```text
w_S1, ..., w_S23
```

### 4.3 Evaluation de la densite de Dirichlet

La log-densite de Dirichlet est calculee directement dans les scripts avec :

```text
log Dir(W ; alpha)
= log Gamma(sum_j alpha_j)
  - sum_j log Gamma(alpha_j)
  + sum_j (alpha_j - 1) log(w_j)
```

Techniquement, la fonction utilise :

- `scipy.special.gammaln` pour calculer `log Gamma(.)` de maniere stable ;
- `numpy.log` pour les logarithmes des parts ;
- une evaluation vectorisee par lignes de la matrice `W`.

L'utilisation de `gammaln` est importante car les fonctions Gamma peuvent devenir numeriquement tres grandes. Travailler en log evite les debordements.

### 4.4 Initialisation par KMeans

Avant l'algorithme EM, les parametres sont initialises avec `KMeans` de `scikit-learn`.

La procedure est :

1. appliquer `KMeans` aux vecteurs de parts `W` ;
2. utiliser les groupes initiaux pour estimer des proportions initiales `pi_k` ;
3. calculer la moyenne empirique des parts dans chaque groupe ;
4. initialiser `alpha_k` comme :

```text
alpha_k = mean_k * phi
```

avec `phi = 50`.

Si un cluster initial contient trop peu d'observations, le script initialise `alpha_k` par un vecteur de uns.

Cette initialisation donne un point de depart economiquement raisonnable : les clusters initiaux se differencient deja par leurs profils de consommation.

### 4.5 Estimation par algorithme EM

Le DMM est estime par un algorithme EM.

Dans l'etape E, les responsabilites posteriori sont calculees :

```text
tau_ik = P(z_i = k | W_i)
```

La formule utilisee est :

```text
tau_ik =
pi_k Dir(W_i ; alpha_k)
/
sum_l pi_l Dir(W_i ; alpha_l)
```

Pour eviter les problemes de sous-flux numerique, les calculs sont faits en log avec :

- `scipy.special.logsumexp` pour normaliser les log-probabilites ;
- `numpy.exp` pour revenir aux probabilites posteriori.

Dans l'etape M, les poids du melange sont mis a jour par :

```text
pi_k = Nk / n
Nk = sum_i tau_ik
```

Les parametres `alpha_k` sont re-estimes par maximum de vraisemblance ponderee. Pour chaque composante, le script minimise l'oppose de la log-vraisemblance ponderee :

```text
- sum_i tau_ik log Dir(W_i ; alpha_k)
```

L'optimisation est faite avec :

- `scipy.optimize.minimize` ;
- methode `L-BFGS-B` ;
- parametrisation en `log(alpha)` afin de garantir `alpha > 0`.

La convergence EM est arretee lorsque la variation de log-vraisemblance devient inferieure a :

```text
TOL = 1e-6
```

ou lorsque le nombre maximal d'iterations est atteint :

```text
MAX_ITER = 200
```

### 4.6 Choix de K dans le DMM

Les scripts DMM estiment systematiquement :

```text
K = 2, 3, ..., 9
```

Pour chaque valeur de `K`, ils calculent :

- la log-vraisemblance finale ;
- l'AIC ;
- le BIC ;
- l'entropie normalisee ;
- le nombre d'iterations ;
- la taille minimale et maximale des clusters ;
- la probabilite maximale moyenne d'appartenance ;
- la probabilite maximale mediane ;
- la part des menages ambigus, definis par `max_prob < 0.60`.

Le BIC et l'AIC servent de criteres statistiques, mais ils ne suffisent pas a eux seuls pour retenir une structure de clusters. L'entropie et la part de menages ambigus renseignent sur la nettete de la classification. Les profils budgetaires moyens servent ensuite a verifier si les groupes sont interpretablement distincts.

### 4.7 Affectation des clusters DMM

Apres estimation, chaque menage recoit :

- un vecteur de probabilites `prob_cluster_1`, ..., `prob_cluster_K` ;
- un cluster final `cluster_dmm`, obtenu par `argmax(tau_ik)` ;
- une probabilite maximale `max_prob` ;
- un indicateur `ambiguous_060`, egal a vrai si `max_prob < 0.60`.

Les profils moyens de clusters sont calcules comme les moyennes empiriques des parts budgetaires des menages affectes a chaque cluster.

### 4.8 Sorties DMM

Pour chaque enquete, chaque niveau de postes et chaque valeur de `K`, les scripts exportent :

- un fichier `membership`, contenant les menages, leur cluster et leurs probabilites d'appartenance ;
- un fichier `profiles`, contenant les profils moyens des clusters ;
- un fichier `alpha`, contenant les parametres de Dirichlet estimes ;
- un fichier global `summary`, comparant les valeurs de `K = 2` a `K = 9`.

Ces fichiers constituent la base de l'analyse des clusters DMM.

## 5. Modele DPMM : melange de Dirichlet avec processus de Dirichlet tronque

### 5.1 Motivation

Le DPMM introduit une approche bayesienne ou le nombre effectif de groupes n'est pas fixe au meme sens que dans le DMM. On fixe une borne superieure `K_MAX`, mais le modele peut attribuer un poids faible a certaines composantes. Ainsi, `K_MAX` represente une capacite maximale, alors que le nombre de clusters substantiels est lu a travers les poids posteriori et les tailles affectees.

Dans le projet, les scripts utilisent :

```text
K_MAX = 7
```

Le DPMM est estime pour les quatre cas :

- ENNVM 2007, 9 postes ;
- ENCDM 2014, 9 postes ;
- ENNVM 2007, 23 postes ;
- ENCDM 2014, 23 postes.

Les scripts sont :

- `DPMM/dpmm_ennvm_9.py` ;
- `DPMM/dpmm_encdm_9.py` ;
- `DPMM/dpmm_ennvm_23.py` ;
- `DPMM/dpmm_encdm_23.py`.

### 5.2 Representation stick-breaking

Le DPMM est implemente sous forme de melange tronque. Les poids de melange sont generes par une construction de type stick-breaking :

```text
v_k ~ Beta(1, alpha_DP)
```

puis :

```text
pi_k = v_k prod_l<k (1 - v_l)
```

La derniere composante recupere le reste de la masse. Les poids sont ensuite renormalises pour sommer a 1.

Le parametre `alpha_DP` controle la tendance du modele a utiliser davantage de composantes. Une valeur plus elevee favorise potentiellement plus de groupes occupes ; une valeur plus faible concentre davantage la masse sur quelques composantes.

### 5.3 Sensibilite aux priors de alpha_DP

Chaque script DPMM teste plusieurs priors Gamma sur `alpha_DP`. Les scripts actuels contiennent une liste `ALPHA_DP_PRIORS`, chaque element ayant la forme :

```text
(nom_du_prior, alpha, beta)
```

Dans les scripts, la loi est specifiee par :

```text
alpha_DP ~ Gamma(alpha, beta)
```

Cette sensibilite permet de verifier si les conclusions sur le nombre effectif de clusters dependent fortement ou non du prior choisi. Les sorties sont ensuite comparees par prior.

### 5.4 Parametrisation des composantes de Dirichlet

Chaque composante du melange possede un parametre de Dirichlet :

```text
alpha_comp_k = m_k * phi_k
```

ou :

- `m_k` est le profil moyen theorique de la composante ;
- `phi_k` est un parametre de concentration ;
- `alpha_comp_k` est le vecteur de parametres de Dirichlet.

Le parametre de concentration est modelise par :

```text
phi_k ~ Gamma(2.0, 0.1)
```

Cette decomposition est utile car elle separe :

- la position du cluster dans le simplexe, via `m_k` ;
- le degre d'homogeneite autour de cette position, via `phi_k`.

### 5.5 Contrainte d'ordre contre le label switching

Les modeles de melange bayesiens souffrent naturellement du label switching. Les composantes sont echangeables : appeler une composante cluster 1 ou cluster 4 ne change pas la vraisemblance. Si l'echantillonneur explore ces permutations, les moyennes posteriori des parametres deviennent difficiles a interpreter.

Pour stabiliser les labels, les scripts DPMM utilisent une contrainte d'ordre economique.

Dans les modeles en 9 postes, les composantes sont ordonnees selon la part theorique du premier poste :

```text
G1
```

Dans les modeles en 23 postes, elles sont ordonnees selon :

```text
S1
```

Techniquement, le modele definit une variable latente ordonnee `g1_ordered`, transformee ensuite par une fonction logistique. L'ordre impose une hierarchie descendante de la part alimentaire theorique. Les autres parts sont modelisees par une loi de Dirichlet conditionnelle et sont redimensionnees pour sommer a `1 - G1` ou `1 - S1`.

Cette contrainte reduit le label switching directement pendant l'echantillonnage. Elle est ensuite completee par un relabeling posteriori.

### 5.6 Relabeling posteriori

Apres echantillonnage, les tirages posteriori sont reorganises par une procedure de relabeling.

La procedure commence par trier chaque tirage selon la part theorique du premier poste. Ensuite, elle applique une procedure iterative de matching avec une reference moyenne. Pour chaque tirage et chaque composante, une matrice de cout est construite a partir :

- de la distance entre profils moyens `m_k` ;
- de la difference de poids de melange ;
- d'une penalisation de poids controlee par `RELABEL_WEIGHT_PENALTY = 0.25`.

Le probleme d'appariement est resolu par :

```text
scipy.optimize.linear_sum_assignment
```

Il s'agit de l'algorithme hongrois, utilise ici pour aligner les composantes des tirages MCMC sur une reference commune. La procedure est repetee :

```text
RELABEL_ITER = 8
```

Enfin, les composantes sont remises dans un ordre lisible, avec les groupes a forte part du premier poste en premier.

### 5.7 Vraisemblance marginalisee

Les scripts DPMM ne tirent pas explicitement un indicateur categoriel de cluster pour chaque menage pendant NUTS. Les allocations latentes sont marginalisees dans la vraisemblance :

```text
log p(W_i) = log sum_k pi_k Dirichlet(W_i ; alpha_k)
```

Cette strategie est plus stable que l'echantillonnage direct des labels discrets, car NUTS ne gere pas naturellement les variables discretes. Elle evite aussi une partie des problemes numeriques lies a l'exploration combinatoire des allocations.

La vraisemblance est ajoutee au modele par :

```text
pm.Potential("likelihood", logp_mix.sum())
```

### 5.8 Echantillonnage NUTS

Les modeles DPMM sont estimes avec PyMC :

```text
pm.sample(...)
```

Les parametres principaux sont :

```text
DRAWS = 1000
TUNE = 1000
CHAINS = 1
CORES = 1
TARGET_ACCEPT = 0.9
```

Le choix d'une seule chaine a ete retenu dans les scripts actuels pour eviter les difficultes pratiques de parallelisation et de label switching multi-chain. En contrepartie, `R-hat` n'est pas interpretable comme dans une estimation multi-chain classique. Les diagnostics se concentrent donc surtout sur :

- le nombre de divergences ;
- l'ESS disponible ;
- la coherence des poids posteriori ;
- la stabilite selon les priors ;
- la qualite des affectations posteriori.

Les scripts activent :

```text
USE_JAX = True
```

Lorsque possible, PyMC utilise le backend NUTS de NumPyro, qui s'appuie sur JAX. Si cette execution echoue, le script retombe automatiquement sur le NUTS standard de PyMC.

### 5.9 Passage de l'estimation aux clusters

Apres estimation, les scripts calculent les moyennes posteriori :

- des poids du melange ;
- des parametres `alpha_comp` ;
- des concentrations `phi` ;
- des profils moyens theoriques `m`.

Avec ces parametres posteriori moyens, les responsabilites sont recalculees pour tous les menages :

```text
tau_ik = P(z_i = k | W_i, parametres posteriori moyens)
```

Chaque menage recoit ensuite :

- `cluster_dpmm_nuts`, par maximum de probabilite ;
- `max_prob_dpmm_nuts` ;
- `ambiguous_060_dpmm_nuts`, si la probabilite maximale est inferieure a 0.60 ;
- `prob_cluster_1`, ..., `prob_cluster_K_MAX`.

### 5.10 Nombre de clusters occupes et K effectif

Dans le DPMM, le nombre `K_MAX = 7` n'est pas forcement le nombre final de groupes interpretablement actifs. Les scripts calculent des indicateurs d'occupation :

```text
OCCUPIED_WEIGHT_THRESHOLD = 0.01
OCCUPIED_SIZE_THRESHOLD = 20
```

Un cluster peut donc etre techniquement present mais tres peu occupe. L'analyse distingue :

- `K_MAX`, borne superieure de la troncature ;
- le nombre de composantes avec poids posteriori superieur a 1 % ;
- le nombre de composantes affectant plus de 20 menages ;
- le nombre de groupes economiquement substantiels apres lecture des profils.

Cette distinction est essentielle pour eviter de dire que le modele choisit automatiquement `K = 7`. En pratique, le DPMM peut proposer une solution technique a 7 composantes, tout en indiquant un nombre effectif plus proche de 5 ou 6 si certaines composantes sont tres petites ou redondantes.

### 5.11 Sorties DPMM

Pour chaque prior de `alpha_DP`, les scripts exportent :

- un fichier `cluster_summary`, avec poids posteriori, tailles affectees, concentration et indicateurs d'occupation ;
- un fichier `alpha`, avec les parametres de Dirichlet posteriori moyens ;
- un fichier `membership_full`, avec affectations et probabilites par menage ;
- un fichier `profiles_full`, avec profils moyens empiriques par cluster.

Un fichier global `prior_comparison` est aussi produit. Il contient :

- une feuille `prior_global_summary` ;
- une feuille `cluster_summary`.

Ces sorties servent ensuite aux diagnostics DPMM.

## 6. Diagnostics apres estimation

Les diagnostics sont separes de l'estimation afin de ne pas melanger deux taches differentes :

- estimer les modeles ;
- analyser les resultats produits.

Les scripts de diagnostic lisent les sorties DMM ou DPMM et fusionnent les affectations avec les variables socio-economiques disponibles dans les bases brutes. Ils construisent ensuite des tableaux d'analyse :

- distributions globales ;
- tableaux croises cluster x variables qualitatives ;
- pourcentages par ligne ;
- ecarts aux proportions globales ;
- tests du khi-deux ;
- V de Cramer ;
- statistiques quantitatives par cluster ;
- ANOVA ;
- test de Kruskal-Wallis ;
- vue synthetique par `K` ou par prior.

Ces diagnostics permettent de juger si les groupes sont statistiquement differencies et interpretables en termes de comportement des menages.

## 7. Bibliotheques Python utilisees

### 7.1 pandas

`pandas` est utilise pour :

- lire et ecrire les fichiers Excel ;
- nettoyer les bases ;
- selectionner les colonnes de depenses ;
- construire les matrices de parts ;
- fusionner les memberships avec les variables brutes ;
- agreger les profils par cluster ;
- exporter les tableaux de resultats.

### 7.2 numpy

`numpy` est utilise pour :

- manipuler les matrices de parts budgetaires ;
- calculer les logarithmes, exponentielles et normalisations ;
- vectoriser les calculs de densite ;
- calculer les responsabilites ;
- manipuler les tenseurs posteriori du DPMM apres extraction depuis ArviZ/PyMC.

### 7.3 scipy.special

`scipy.special.gammaln` est utilise pour calculer la log-fonction Gamma dans la densite de Dirichlet. `scipy.special.logsumexp` est utilise pour stabiliser les sommes de probabilites en echelle logarithmique dans les melanges.

Ces deux fonctions sont centrales mathematiquement : elles rendent possible une evaluation numeriquement stable de la vraisemblance des modeles de Dirichlet.

### 7.4 scipy.optimize

`scipy.optimize.minimize` est utilise dans le DMM pour estimer les parametres `alpha_k` par maximum de vraisemblance ponderee. La methode employee est `L-BFGS-B`, appliquee a `log(alpha)` pour respecter la contrainte de positivite.

`scipy.optimize.linear_sum_assignment` est utilise dans le DPMM pour resoudre le probleme de relabeling posteriori. Il permet d'apparier les composantes des tirages MCMC a une reference commune en minimisant une matrice de cout.

### 7.5 scikit-learn

`sklearn.cluster.KMeans` est utilise pour initialiser les composantes du DMM. Cette initialisation donne des profils de depart plausibles avant l'algorithme EM.

### 7.6 PyMC

`pymc` est la bibliotheque centrale pour le DPMM bayesien. Elle sert a definir :

- les priors Gamma et Beta ;
- la construction stick-breaking ;
- les profils de composantes ;
- les concentrations `phi` ;
- la vraisemblance marginalisee via `pm.Potential` ;
- l'echantillonnage NUTS.

### 7.7 PyTensor

`pytensor.tensor` est utilise dans les scripts PyMC pour construire les operations symboliques du modele :

- concatenation ;
- produit cumule ;
- produit matriciel ;
- calcul de `gammaln` ;
- log-vraisemblance vectorisee.

### 7.8 ArviZ

`arviz` est utilise pour extraire des diagnostics posteriori, notamment :

- le nombre effectif d'echantillons ;
- les resumés de parametres ;
- `R-hat` lorsque disponible.

Dans les scripts actuels, comme l'estimation se fait avec une seule chaine, `R-hat` est souvent non disponible ou non interpretable.

### 7.9 JAX et NumPyro

Les scripts DPMM demandent a PyMC d'utiliser le backend NUTS `numpyro` lorsque cela est possible. NumPyro s'appuie sur JAX, qui compile et accelere certains calculs numeriques. L'objectif est d'ameliorer le temps d'execution sans modifier la specification statistique du modele.

Si le backend JAX/NumPyro echoue, le code retombe automatiquement sur le NUTS standard de PyMC.

### 7.10 openpyxl

`openpyxl` est utilise indirectement par `pandas` pour lire et ecrire les fichiers Excel `.xlsx`. Les resultats sont donc facilement inspectables dans Excel.

## 8. Resume de la chaine complete

La chaine technique peut etre resumee ainsi :

1. Lecture des bases brutes ENNVM 2007 et ENCDM 2014.
2. Verification des variables de depenses et de la depense totale `DAM`.
3. Construction des matrices en 9 postes `w_G1` a `w_G9`.
4. Construction des matrices en 23 postes `w_S1` a `w_S23`.
5. Normalisation des parts pour que chaque ligne somme a 1.
6. Correction epsilon pour rendre toutes les composantes strictement positives.
7. Estimation DMM pour `K = 2, ..., 9`.
8. Export des memberships, profils, parametres alpha et criteres AIC/BIC/entropie.
9. Estimation DPMM tronquee avec `K_MAX = 7`.
10. Test de plusieurs priors Gamma sur `alpha_DP`.
11. Echantillonnage NUTS avec tentative JAX/NumPyro.
12. Stabilisation des labels par contrainte d'ordre et relabeling posteriori.
13. Calcul des responsabilites posteriori pour tous les menages.
14. Export des clusters, probabilites, profils et diagnostics de prior.
15. Analyse separee des sorties par scripts de diagnostic.

## 9. Conclusion methodologique

La procedure mise en place combine une approche frequentiste et une approche bayesienne des melanges de Dirichlet. Le DMM fournit une grille comparative explicite pour plusieurs valeurs de `K`, tandis que le DPMM fournit une approche plus flexible ou le nombre effectif de composantes est interprete a partir des poids posteriori et des tailles de clusters.

Le point central de la procedure est la representation des menages par des vecteurs de parts budgetaires strictement positives et normalisees. Cette representation justifie l'utilisation de la loi de Dirichlet et permet de comparer les menages par structure de consommation plutot que par niveau absolu de depense.

Les sorties finales ne se limitent pas a une affectation dure des menages. Elles conservent les probabilites d'appartenance, les indicateurs d'ambiguite, les profils moyens et les parametres de concentration. Ces elements sont essentiels pour juger la robustesse, la lisibilite et l'interpretabilite des groupes obtenus.
