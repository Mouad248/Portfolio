import numpy as np
import pandas as pd
from pathlib import Path
from scipy.special import gammaln, logsumexp
from scipy.optimize import minimize
from sklearn.cluster import KMeans

# =====================================================
# 1. Paramètres à modifier selon la base
# =====================================================

INPUT_FILE = Path("data/processed/ennvm_2007_parts_budgetaires.xlsx")
PREFIX = "ennvm_2007"

OUTPUT_DIR = Path("outputs/tables")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SHARE_COLS = [f"w_G{i}" for i in range(1, 10)]

K_VALUES = range(2, 10)   # K = 2 à 9
MAX_ITER = 200
TOL = 1e-6
RANDOM_STATE = 123

# =====================================================
# 2. Fonctions DMM
# =====================================================

def log_dirichlet_pdf(W, alpha):
    alpha = np.asarray(alpha)
    log_coef = gammaln(alpha.sum()) - gammaln(alpha).sum()
    return log_coef + ((alpha - 1) * np.log(W)).sum(axis=1)


def estimate_alpha_weighted(W, weights, alpha_init):
    weights = np.asarray(weights)

    if weights.sum() <= 0:
        return alpha_init

    weights = weights / weights.sum()

    def objective(log_alpha):
        alpha = np.exp(log_alpha)
        logpdf = log_dirichlet_pdf(W, alpha)
        return -np.sum(weights * logpdf)

    res = minimize(
        objective,
        np.log(alpha_init),
        method="L-BFGS-B",
        options={"maxiter": 500}
    )

    if not res.success:
        return alpha_init

    return np.exp(res.x)


def initialize_parameters(W, K, random_state=123):
    n, J = W.shape

    kmeans = KMeans(
        n_clusters=K,
        random_state=random_state,
        n_init=20
    )

    labels = kmeans.fit_predict(W)

    pi = np.zeros(K)
    alpha = np.zeros((K, J))

    for k in range(K):
        idx = labels == k
        pi[k] = idx.mean()

        if idx.sum() < 5:
            alpha[k] = np.ones(J)
        else:
            mean_k = W[idx].mean(axis=0)
            mean_k = mean_k / mean_k.sum()

            phi = 50
            alpha[k] = mean_k * phi

    pi = pi / pi.sum()
    return pi, alpha


def fit_dirichlet_mixture(W, K, max_iter=200, tol=1e-6, random_state=123):
    n, J = W.shape

    pi, alpha = initialize_parameters(W, K, random_state)
    previous_loglik = -np.inf

    for iteration in range(max_iter):

        # E-step
        log_resp = np.zeros((n, K))

        for k in range(K):
            log_resp[:, k] = np.log(pi[k] + 1e-15) + log_dirichlet_pdf(W, alpha[k])

        log_norm = logsumexp(log_resp, axis=1)
        loglik = log_norm.sum()

        tau = np.exp(log_resp - log_norm[:, None])

        # convergence
        if np.abs(loglik - previous_loglik) < tol:
            break

        previous_loglik = loglik

        # M-step
        Nk = tau.sum(axis=0)
        pi = Nk / n

        for k in range(K):
            if Nk[k] < 5:
                alpha[k] = np.ones(J)
            else:
                alpha[k] = estimate_alpha_weighted(W, tau[:, k], alpha[k])

    n_params = (K - 1) + K * J

    bic = -2 * loglik + n_params * np.log(n)
    aic = -2 * loglik + 2 * n_params

    entropy = -np.sum(tau * np.log(tau + 1e-15))
    entropy_norm = 1 - entropy / (n * np.log(K))

    labels = tau.argmax(axis=1) + 1
    max_prob = tau.max(axis=1)

    return {
        "K": K,
        "pi": pi,
        "alpha": alpha,
        "tau": tau,
        "labels": labels,
        "max_prob": max_prob,
        "loglik": loglik,
        "bic": bic,
        "aic": aic,
        "entropy_norm": entropy_norm,
        "iterations": iteration + 1
    }


def make_profile_table(W_df, labels):
    temp = W_df.copy()
    temp["cluster"] = labels

    profile = temp.groupby("cluster")[SHARE_COLS].mean()
    profile.insert(0, "cluster_size", temp.groupby("cluster").size())

    return profile


# =====================================================
# 3. Chargement
# =====================================================

df = pd.read_excel(INPUT_FILE)

print("Base chargée :", INPUT_FILE)
print("Dimensions :", df.shape)

missing = [col for col in SHARE_COLS if col not in df.columns]
if missing:
    raise ValueError(f"Colonnes manquantes : {missing}")

W_df = df[SHARE_COLS].copy()
W = W_df.to_numpy(dtype=float)

if np.any(W <= 0):
    raise ValueError("Certaines parts sont nulles ou négatives. Vérifiez epsilon.")

W = W / W.sum(axis=1, keepdims=True)

print("\nSomme des parts :")
print(pd.Series(W.sum(axis=1)).describe())

# =====================================================
# 4. Estimation pour tous les K
# =====================================================

summary_rows = []

for K in K_VALUES:
    print(f"\n==============================")
    print(f"Estimation DMM avec K = {K}")
    print(f"==============================")

    result = fit_dirichlet_mixture(
        W,
        K=K,
        max_iter=MAX_ITER,
        tol=TOL,
        random_state=RANDOM_STATE
    )

    labels = result["labels"]
    max_prob = result["max_prob"]

    cluster_sizes = pd.Series(labels).value_counts().sort_index()

    summary_rows.append({
        "K": K,
        "loglik": result["loglik"],
        "AIC": result["aic"],
        "BIC": result["bic"],
        "entropy_norm": result["entropy_norm"],
        "iterations": result["iterations"],
        "min_cluster_size": cluster_sizes.min(),
        "max_cluster_size": cluster_sizes.max(),
        "mean_max_prob": max_prob.mean(),
        "median_max_prob": np.median(max_prob),
        "share_ambiguous_prob_lt_0_60": np.mean(max_prob < 0.60)
    })

    print("LogLik :", round(result["loglik"], 2))
    print("AIC    :", round(result["aic"], 2))
    print("BIC    :", round(result["bic"], 2))
    print("Entropie normalisée :", round(result["entropy_norm"], 4))
    print("Probabilité max moyenne :", round(max_prob.mean(), 4))
    print("Ménages ambigus < 0.60 :", round(np.mean(max_prob < 0.60), 4))
    print("\nTailles des clusters :")
    print(cluster_sizes.to_string())

    # -------------------------
    # Export memberships pour chaque K
    # -------------------------

    tau_cols = [f"prob_cluster_{k}" for k in range(1, K + 1)]
    tau_df = pd.DataFrame(result["tau"], columns=tau_cols)

    membership_df = df.copy()
    membership_df["cluster_dmm"] = labels
    membership_df["max_prob"] = max_prob
    membership_df["ambiguous_060"] = max_prob < 0.60
    membership_df = pd.concat([membership_df, tau_df], axis=1)

    membership_file = OUTPUT_DIR / f"{PREFIX}_dmm_membership_K{K}.xlsx"
    membership_df.to_excel(membership_file, index=False)

    # -------------------------
    # Export profils moyens pour chaque K
    # -------------------------

    profile = make_profile_table(W_df, labels)

    profile_file = OUTPUT_DIR / f"{PREFIX}_dmm_profiles_K{K}.xlsx"
    profile.to_excel(profile_file)

    # -------------------------
    # Export alpha pour chaque K
    # -------------------------

    alpha_df = pd.DataFrame(
        result["alpha"],
        columns=[f"alpha_G{i}" for i in range(1, 10)]
    )

    alpha_df.insert(0, "cluster", range(1, K + 1))
    alpha_df["alpha_sum"] = result["alpha"].sum(axis=1)
    alpha_df["pi"] = result["pi"]

    alpha_file = OUTPUT_DIR / f"{PREFIX}_dmm_alpha_K{K}.xlsx"
    alpha_df.to_excel(alpha_file, index=False)

# =====================================================
# 5. Export tableau global de comparaison
# =====================================================

summary_df = pd.DataFrame(summary_rows)

summary_file = OUTPUT_DIR / f"{PREFIX}_dmm_k2_to_k9_summary.xlsx"
summary_df.to_excel(summary_file, index=False)

print("\n==============================")
print("Résumé global K=2 à K=9")
print("==============================")
print(summary_df)

print("\nFichier résumé exporté vers :")
print(summary_file)

print("\nTravail terminé.")