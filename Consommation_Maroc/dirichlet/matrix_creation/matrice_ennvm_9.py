import pandas as pd
from pathlib import Path

# =========================
# 1. Chemins
# =========================

INPUT_FILE = Path("data/raw/menage_ennvm_propre.xlsx")
OUTPUT_FILE = Path("data/processed/ennvm_2007_parts_budgetaires.xlsx")

# =========================
# 2. Charger la base
# =========================

df = pd.read_excel(INPUT_FILE)

print("Dimensions initiales :", df.shape)

# =========================
# 3. Colonnes à vérifier
# =========================

dam_col = "DAM"
post_cols = [f"DAM_G{i}" for i in range(1, 10)]

needed_cols = [dam_col] + post_cols

missing = [col for col in needed_cols if col not in df.columns]

if missing:
    raise ValueError(f"Colonnes manquantes : {missing}")

# =========================
# 4. Vérifier et convertir en numérique
# =========================

for col in needed_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nTypes après conversion :")
print(df[needed_cols].dtypes)

print("\nValeurs manquantes après conversion :")
print(df[needed_cols].isna().sum())

# =========================
# 5. Garder ménages valides
# =========================

df = df[df[dam_col].notna()]
df = df[df[dam_col] > 0]

for col in post_cols:
    df = df[df[col].notna()]
    df = df[df[col] >= 0]

print("\nDimensions après nettoyage :", df.shape)

# =========================
# 6. Créer les parts budgétaires
# =========================

share_cols = []

for i in range(1, 10):
    dep_col = f"DAM_G{i}"
    share_col = f"w_G{i}"
    df[share_col] = df[dep_col] / df[dam_col]
    share_cols.append(share_col)

# =========================
# 7. Vérifier somme des parts
# =========================

df["sum_w"] = df[share_cols].sum(axis=1)

print("\nRésumé somme des parts :")
print(df["sum_w"].describe())

# tolérance car parfois arrondis ou postes non exhaustifs
problem = df[(df["sum_w"] < 0.99) | (df["sum_w"] > 1.01)]

print("\nNombre de ménages avec somme des parts hors [0.99 ; 1.01] :", len(problem))
# =========================
# 8. Normalisation + correction des zéros pour Dirichlet
# =========================

EPSILON = 1e-6

# garder seulement les ménages avec somme positive
df = df[df["sum_w"] > 0]

# première normalisation : somme = 1
for col in share_cols:
    df[col] = df[col] / df["sum_w"]

# compter les zéros avant correction
n_zeros_before = (df[share_cols] == 0).sum().sum()
print("\nNombre total de parts nulles avant epsilon :", n_zeros_before)

# ajouter epsilon aux parts nulles ou très faibles
df[share_cols] = df[share_cols].clip(lower=EPSILON)

# renormaliser après epsilon
df[share_cols] = df[share_cols].div(df[share_cols].sum(axis=1), axis=0)

df["sum_w_normalized"] = df[share_cols].sum(axis=1)

# vérifier
n_zeros_after = (df[share_cols] == 0).sum().sum()
print("Nombre total de parts nulles après epsilon :", n_zeros_after)

print("\nRésumé somme après epsilon et normalisation :")
print(df["sum_w_normalized"].describe())

print("\nValeur minimale des parts après correction :")
print(df[share_cols].min().min())
# =========================
# 9. Exporter matrice W + variables utiles
# =========================

keep_cols = []

for col in ["N_menage", "Milieu", "Region", "Région", "coef_menage", "coef_ménage", dam_col]:
    if col in df.columns:
        keep_cols.append(col)

final_df = df[keep_cols + share_cols + ["sum_w", "sum_w_normalized"]]

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
final_df.to_excel(OUTPUT_FILE, index=False)

print(f"\nFichier exporté : {OUTPUT_FILE}")
print("\nColonnes exportées :")
print(final_df.columns.tolist())