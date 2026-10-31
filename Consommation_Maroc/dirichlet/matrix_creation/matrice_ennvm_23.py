import pandas as pd
from pathlib import Path

# =====================================================
# 1. Paramètres à modifier selon la base
# =====================================================

INPUT_FILE = Path("data/raw/menage_ennvm_propre.xlsx")
OUTPUT_FILE = Path("data/processed/ennvm_2007_parts_budgetaires_23.xlsx")

DAM_COL = "DAM"
EPSILON = 1e-6

# =====================================================
# 2. Mapping S1 à S23
# =====================================================

S_MAPPING = {
    "S1":  ["DAM_G01"],
    "S2":  ["DAM_G02", "DAM_G04", "DAM_G05"],
    "S3":  ["DAM_G06", "DAM_G07", "DAM_G08"],
    "S4":  ["DAM_G09", "DAM_G10"],
    "S5":  ["DAM_G13", "DAM_G14"],
    "S6":  ["DAM_G03", "DAM_G11", "DAM_G12", "DAM_G15", "DAM_G17", "DAM_G18"],
    "S7":  ["DAM_G21", "DAM_G22", "DAM_G23", "DAM_G24", "DAM_G25", "DAM_G26", "DAM_G27", "DAM_G28"],
    "S8":  ["DAM_G31"],
    "S9":  ["DAM_G32", "DAM_G34"],
    "S10": ["DAM_G41", "DAM_G42", "DAM_G43", "DAM_G44", "DAM_G45", "DAM_G46", "DAM_G47"],
    "S11": ["DAM_G33"],
    "S12": ["DAM_G51"],
    "S13": ["DAM_G52", "DAM_G53"],
    "S14": ["DAM_G61"],
    "S15": ["DAM_G62"],
    "S16": ["DAM_G63"],
    "S17": ["DAM_G71", "DAM_G72", "DAM_G73", "DAM_G74"],
    "S18": ["DAM_G75", "DAM_G76"],
    "S19": ["DAM_G81", "DAM_G82", "DAM_G83", "DAM_G84"],
    "S20": ["DAM_G87", "DAM_G88"],
    "S21": ["DAM_G85", "DAM_G86"],
    "S22": ["DAM_G89"],
    "S23": ["DAM_G91", "DAM_G92", "DAM_G93", "DAM_G94"],
}

# =====================================================
# 3. Charger la base
# =====================================================

df = pd.read_excel(INPUT_FILE)

print("Dimensions initiales :", df.shape)

# =====================================================
# 4. Vérification des colonnes
# =====================================================

all_needed_cols = [DAM_COL]

for cols in S_MAPPING.values():
    all_needed_cols.extend(cols)

all_needed_cols = list(dict.fromkeys(all_needed_cols))

missing = [col for col in all_needed_cols if col not in df.columns]

if missing:
    raise ValueError(f"Colonnes manquantes : {missing}")

# conversion numérique
for col in all_needed_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nValeurs manquantes après conversion :")
print(df[all_needed_cols].isna().sum())

# =====================================================
# 5. Nettoyage minimal
# =====================================================

df = df[df[DAM_COL].notna()]
df = df[df[DAM_COL] > 0]

for col in all_needed_cols:
    if col != DAM_COL:
        df[col] = df[col].fillna(0)
        df[col] = df[col].clip(lower=0)

print("\nDimensions après nettoyage :", df.shape)

# =====================================================
# 6. Construction des S1 à S23
# =====================================================

S_COLS = []

for s_name, cols in S_MAPPING.items():
    df[s_name] = df[cols].sum(axis=1)
    S_COLS.append(s_name)

# =====================================================
# 7. Construction des parts budgétaires
# =====================================================

W_COLS = []

for s_name in S_COLS:
    w_name = f"w_{s_name}"
    df[w_name] = df[s_name] / df[DAM_COL]
    W_COLS.append(w_name)

df["sum_w_23"] = df[W_COLS].sum(axis=1)

print("\nRésumé somme des parts 23 avant normalisation :")
print(df["sum_w_23"].describe())

problem = df[(df["sum_w_23"] < 0.99) | (df["sum_w_23"] > 1.01)]
print("\nNombre de ménages avec somme hors [0.99 ; 1.01] :", len(problem))

# =====================================================
# 8. Normalisation + epsilon
# =====================================================

df = df[df["sum_w_23"] > 0]

# première normalisation
df[W_COLS] = df[W_COLS].div(df["sum_w_23"], axis=0)

n_zeros_before = (df[W_COLS] == 0).sum().sum()
print("\nNombre total de parts nulles avant epsilon :", n_zeros_before)

# correction epsilon
df[W_COLS] = df[W_COLS].clip(lower=EPSILON)

# renormalisation
df[W_COLS] = df[W_COLS].div(df[W_COLS].sum(axis=1), axis=0)

df["sum_w_23_normalized"] = df[W_COLS].sum(axis=1)

print("Nombre total de parts nulles après epsilon :", (df[W_COLS] == 0).sum().sum())

print("\nRésumé somme après epsilon et normalisation :")
print(df["sum_w_23_normalized"].describe())

print("\nPart minimale après correction :")
print(df[W_COLS].min().min())

# =====================================================
# 9. Export
# =====================================================

keep_cols = []

possible_cols = [
    "N_menage", "n_menage", "id_menage",
    "Milieu", "milieu",
    "Region", "Région", "region",
    "coef_menage", "coef_ménage",
    DAM_COL
]

for col in possible_cols:
    if col in df.columns:
        keep_cols.append(col)

final_df = df[keep_cols + S_COLS + W_COLS + ["sum_w_23", "sum_w_23_normalized"]]

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
final_df.to_excel(OUTPUT_FILE, index=False)

print(f"\nFichier exporté : {OUTPUT_FILE}")
print("\nColonnes parts exportées :")
print(W_COLS)