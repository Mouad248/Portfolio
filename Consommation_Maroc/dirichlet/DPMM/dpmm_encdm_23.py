from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from scipy.special import gammaln, logsumexp

import arviz as az
import pymc as pm
import pytensor.tensor as pt


# =====================================================
# 1. Parameters
# =====================================================

INPUT_FILE = Path("data/processed/encdm_2014_parts_budgetaires_23.xlsx")
PREFIX = "encdm_2014_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"

OUTPUT_TABLES = Path("outputs/tables")
OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)

SHARE_COLS = [f"w_S{i}" for i in range(1, 24)]

K_MAX = 7
RANDOM_SEED = 123

CHAINS = 1
CORES = 1
DRAWS = 1000
TUNE = 1000
TARGET_ACCEPT = 0.9

# Priors requested by the user: Gamma(alpha, beta).
ALPHA_DP_PRIORS = [
    ("gamma_1_1", 1.0, 2.0),
    ("gamma_1_2", 0.25, 2.0),
    ("gamma_0p5_2", 0.1, 2.0),
    ("gamma_0p25_2", 0.05, 2.0),
]

USE_JAX = True
ORDERED_S1_IDENTIFICATION = True

# Relabeling controls.
RELABEL_ITER = 8
RELABEL_WEIGHT_PENALTY = 0.25
OCCUPIED_WEIGHT_THRESHOLD = 0.01
OCCUPIED_SIZE_THRESHOLD = 20


# =====================================================
# 2. Data and likelihood helpers
# =====================================================

def load_w():
    df = pd.read_excel(INPUT_FILE)
    w = df[SHARE_COLS].to_numpy(dtype=float)
    if np.any(w <= 0):
        raise ValueError("Some budget shares are <= 0. Check epsilon preprocessing.")
    w = w / w.sum(axis=1, keepdims=True)
    return df, w


def make_estimation_sample(w):
    idx = np.arange(w.shape[0])
    return idx, w


def g1_order_init(k_max):
    # Descending target food shares. The ordered transform is ascending, so the
    # model uses g1 = sigmoid(-g1_ordered).
    target_g1_desc = np.linspace(0.58, 0.18, k_max)
    return -np.log(target_g1_desc / (1 - target_g1_desc))


def build_model(log_w_sub, prior_alpha, prior_beta):
    n, j = log_w_sub.shape
    with pm.Model() as model:
        alpha_dp = pm.Gamma("alpha_dp", alpha=prior_alpha, beta=prior_beta)

        v = pm.Beta("v", alpha=1.0, beta=alpha_dp, shape=K_MAX - 1)
        remaining = pt.concatenate([pt.ones(1), pt.cumprod(1 - v)])
        weights_first = v * remaining[:-1]
        weights_last = remaining[-1:]
        weights = pt.concatenate([weights_first, weights_last])
        weights = weights / weights.sum()
        pm.Deterministic("weights", weights)

        if ORDERED_S1_IDENTIFICATION:
            # Identification constraint for mixture labels:
            # components are ordered by their theoretical food share S1.
            #
            # This is stronger than post-hoc relabeling. It breaks the label
            # symmetry inside the posterior sampled by NUTS. The remaining eight
            # budget shares are still flexible through a Dirichlet distribution
            # and are scaled to sum to 1 - S1.
            g1_ordered = pm.Normal(
                "g1_ordered",
                mu=0.0,
                sigma=2.0,
                shape=K_MAX,
                transform=pm.distributions.transforms.ordered,
                initval=g1_order_init(K_MAX),
            )
            g1 = pm.Deterministic("g1_ordered_desc", pm.math.sigmoid(-g1_ordered))
            r_rest = pm.Dirichlet("r_rest", a=np.ones(j - 1), shape=(K_MAX, j - 1))
            m = pm.Deterministic(
                "m",
                pt.concatenate([g1[:, None], (1 - g1)[:, None] * r_rest], axis=1),
            )
        else:
            m = pm.Dirichlet("m", a=np.ones(j), shape=(K_MAX, j))

        phi = pm.Gamma("phi", alpha=2.0, beta=0.1, shape=K_MAX)
        alpha_comp = pm.Deterministic("alpha_comp", m * phi[:, None])

        alpha_sum = alpha_comp.sum(axis=1)
        log_coef = pt.gammaln(alpha_sum) - pt.gammaln(alpha_comp).sum(axis=1)
        logp_components = log_coef[None, :] + pt.dot(log_w_sub, (alpha_comp - 1).T)
        logp_mix = pm.math.logsumexp(
            pt.log(weights + 1e-15)[None, :] + logp_components,
            axis=1,
        )

        # The latent allocations are marginalized. This is much more stable than
        # sampling one categorical cluster indicator per household.
        pm.Potential("likelihood", logp_mix.sum())

    return model


def sample_model(model):
    with model:
        if USE_JAX:
            try:
                idata = pm.sample(
                    draws=DRAWS,
                    tune=TUNE,
                    chains=CHAINS,
                    cores=CORES,
                    target_accept=TARGET_ACCEPT,
                    random_seed=RANDOM_SEED,
                    nuts_sampler="numpyro",
                    progressbar=True,
                )
            except Exception as exc:
                print("JAX/Numpyro NUTS failed, falling back to PyMC NUTS.")
                print("Reason:", repr(exc))
                idata = pm.sample(
                    draws=DRAWS,
                    tune=TUNE,
                    chains=CHAINS,
                    cores=CORES,
                    target_accept=TARGET_ACCEPT,
                    random_seed=RANDOM_SEED,
                    progressbar=True,
                )
        else:
            idata = pm.sample(
                draws=DRAWS,
                tune=TUNE,
                chains=CHAINS,
                cores=CORES,
                target_accept=TARGET_ACCEPT,
                random_seed=RANDOM_SEED,
                progressbar=True,
            )

    return idata


def log_dirichlet_pdf_matrix(w, alpha):
    out = np.zeros((w.shape[0], alpha.shape[0]))
    log_w = np.log(w)
    for k in range(alpha.shape[0]):
        a = alpha[k]
        log_coef = gammaln(a.sum()) - gammaln(a).sum()
        out[:, k] = log_coef + ((a - 1) * log_w).sum(axis=1)
    return out


def responsibilities(w, weights, alpha):
    logpdf = log_dirichlet_pdf_matrix(w, alpha)
    log_resp = np.log(weights + 1e-15)[None, :] + logpdf
    log_norm = logsumexp(log_resp, axis=1)
    return np.exp(log_resp - log_norm[:, None])


# =====================================================
# 3. Relabeling
# =====================================================

def flatten_posterior(idata):
    posterior = idata.posterior
    weights = posterior["weights"].values.reshape(-1, K_MAX)
    alpha = posterior["alpha_comp"].values.reshape(-1, K_MAX, len(SHARE_COLS))
    phi = posterior["phi"].values.reshape(-1, K_MAX)
    m = alpha / alpha.sum(axis=2, keepdims=True)
    return weights, alpha, phi, m


def relabel_draws(weights, alpha, phi, m):
    # Initialize by a deterministic economic ordering. Then improve it by
    # iterative reference matching. This is more stable than using raw MCMC labels.
    order0 = np.argsort(-m[:, :, 0], axis=1)
    weights_r = np.take_along_axis(weights, order0, axis=1)
    phi_r = np.take_along_axis(phi, order0, axis=1)
    alpha_r = np.take_along_axis(alpha, order0[:, :, None], axis=1)
    m_r = np.take_along_axis(m, order0[:, :, None], axis=1)

    ref_m = m_r.mean(axis=0)
    ref_w = weights_r.mean(axis=0)

    for _ in range(RELABEL_ITER):
        new_weights = np.empty_like(weights_r)
        new_phi = np.empty_like(phi_r)
        new_alpha = np.empty_like(alpha_r)
        new_m = np.empty_like(m_r)

        for d in range(weights.shape[0]):
            cost = np.zeros((K_MAX, K_MAX))
            for i in range(K_MAX):
                for j in range(K_MAX):
                    profile_dist = np.linalg.norm(m[d, i] - ref_m[j])
                    weight_dist = abs(weights[d, i] - ref_w[j])
                    cost[i, j] = profile_dist + RELABEL_WEIGHT_PENALTY * weight_dist

            row_ind, col_ind = linear_sum_assignment(cost)
            perm = row_ind[np.argsort(col_ind)]
            new_weights[d] = weights[d, perm]
            new_phi[d] = phi[d, perm]
            new_alpha[d] = alpha[d, perm]
            new_m[d] = m[d, perm]

        weights_r, phi_r, alpha_r, m_r = new_weights, new_phi, new_alpha, new_m
        ref_m = m_r.mean(axis=0)
        ref_w = weights_r.mean(axis=0)

    # Final human-readable ordering: high-food-share components first.
    final_order = np.argsort(-ref_m[:, 0])
    return (
        weights_r[:, final_order],
        alpha_r[:, final_order],
        phi_r[:, final_order],
        m_r[:, final_order],
    )


def posterior_diagnostics(idata):
    rows = {}
    if "diverging" in idata.sample_stats:
        rows["n_divergences"] = int(idata.sample_stats["diverging"].sum().values)
    else:
        rows["n_divergences"] = np.nan

    try:
        summ = az.summary(idata, var_names=["alpha_dp", "weights", "phi"], round_to=4)
        rows["max_rhat"] = float(summ["r_hat"].max()) if "r_hat" in summ else np.nan
        rows["min_ess_bulk"] = float(summ["ess_bulk"].min())
    except Exception:
        rows["max_rhat"] = np.nan
        rows["min_ess_bulk"] = np.nan
    return rows


# =====================================================
# 4. Prior run and exports
# =====================================================

def summarize_prior(prior_name, idata, w_sub, w_full, df_full):
    weights, alpha, phi, m = flatten_posterior(idata)
    weights_r, alpha_r, phi_r, m_r = relabel_draws(weights, alpha, phi, m)

    weights_post = weights_r.mean(axis=0)
    alpha_post = alpha_r.mean(axis=0)
    phi_post = phi_r.mean(axis=0)
    m_post = m_r.mean(axis=0)

    tau_sub = responsibilities(w_sub, weights_post, alpha_post)
    labels_sub = tau_sub.argmax(axis=1) + 1
    max_prob_sub = tau_sub.max(axis=1)

    tau_full = responsibilities(w_full, weights_post, alpha_post)
    labels_full = tau_full.argmax(axis=1) + 1
    max_prob_full = tau_full.max(axis=1)

    size_sub = pd.Series(labels_sub).value_counts().reindex(range(1, K_MAX + 1), fill_value=0)
    size_full = pd.Series(labels_full).value_counts().reindex(range(1, K_MAX + 1), fill_value=0)

    diag = posterior_diagnostics(idata)
    occupied_weight = int((weights_post > OCCUPIED_WEIGHT_THRESHOLD).sum())
    occupied_sub = int((size_sub > OCCUPIED_SIZE_THRESHOLD).sum())
    occupied_full = int((size_full > OCCUPIED_SIZE_THRESHOLD).sum())

    cluster_summary = pd.DataFrame({
        "prior": prior_name,
        "cluster": range(1, K_MAX + 1),
        "posterior_weight_mean": weights_post,
        "assigned_size_estimation": size_sub.values,
        "assigned_share_estimation": size_sub.values / len(w_sub),
        "assigned_size_full": size_full.values,
        "assigned_share_full": size_full.values / len(w_full),
        "phi_mean": phi_post,
        "alpha_sum_mean": alpha_post.sum(axis=1),
        "mean_S1_theoretical": m_post[:, 0],
        "weight_gt_1pct": weights_post > OCCUPIED_WEIGHT_THRESHOLD,
        "size_full_gt_20": size_full.values > OCCUPIED_SIZE_THRESHOLD,
    })

    alpha_df = pd.DataFrame(alpha_post, columns=[f"alpha_S{i}" for i in range(1, len(SHARE_COLS) + 1)])
    alpha_df.insert(0, "prior", prior_name)
    alpha_df.insert(1, "cluster", range(1, K_MAX + 1))
    alpha_df["alpha_sum_mean"] = alpha_post.sum(axis=1)
    alpha_df["posterior_weight_mean"] = weights_post
    alpha_df["phi_mean"] = phi_post
    for j in range(1, len(SHARE_COLS) + 1):
        alpha_df[f"m_S{j}_theoretical"] = m_post[:, j - 1]

    membership = df_full.copy()
    membership["cluster_dpmm_nuts"] = labels_full
    membership["max_prob_dpmm_nuts"] = max_prob_full
    membership["ambiguous_060_dpmm_nuts"] = max_prob_full < 0.60
    tau_df = pd.DataFrame(tau_full, columns=[f"prob_cluster_{k}" for k in range(1, K_MAX + 1)])
    membership = pd.concat([membership, tau_df], axis=1)

    profile_df = df_full[SHARE_COLS].copy()
    profile_df["cluster_dpmm_nuts"] = labels_full
    profiles = profile_df.groupby("cluster_dpmm_nuts")[SHARE_COLS].mean()
    profiles.insert(0, "cluster_size", profile_df.groupby("cluster_dpmm_nuts").size())

    global_row = {
        "prior": prior_name,
        "K_MAX": K_MAX,
        "estimation_n": len(w_sub),
        "full_n": len(w_full),
        "alpha_dp_mean": float(idata.posterior["alpha_dp"].mean().values),
        "alpha_dp_sd": float(idata.posterior["alpha_dp"].std().values),
        "occupied_weight_gt_1pct": occupied_weight,
        "occupied_size_sub_gt20": occupied_sub,
        "occupied_size_full_gt20": occupied_full,
        "mean_max_prob_estimation": float(max_prob_sub.mean()),
        "median_max_prob_estimation": float(np.median(max_prob_sub)),
        "share_ambiguous_estimation_lt_0_60": float((max_prob_sub < 0.60).mean()),
        "mean_max_prob_full": float(max_prob_full.mean()),
        "median_max_prob_full": float(np.median(max_prob_full)),
        "share_ambiguous_full_lt_0_60": float((max_prob_full < 0.60).mean()),
        **diag,
    }

    base = OUTPUT_TABLES / f"{PREFIX}_{prior_name}"
    cluster_summary.to_excel(base.with_name(base.name + "_cluster_summary.xlsx"), index=False)
    alpha_df.to_excel(base.with_name(base.name + "_alpha.xlsx"), index=False)
    membership.to_excel(base.with_name(base.name + "_membership_full.xlsx"), index=False)
    profiles.to_excel(base.with_name(base.name + "_profiles_full.xlsx"))

    return global_row, cluster_summary


def main():
    print("Loading data:", INPUT_FILE)
    df_full, w_full = load_w()
    idx, w_sub = make_estimation_sample(w_full)
    log_w_sub = np.log(w_sub)

    print("Full W:", w_full.shape)
    print("Estimation W:", w_sub.shape)
    print("K_MAX:", K_MAX)

    global_rows = []
    all_cluster_summaries = []

    for prior_name, prior_alpha, prior_beta in ALPHA_DP_PRIORS:
        print("\n==============================")
        print(f"Prior alpha_dp ~ Gamma({prior_alpha}, {prior_beta}) [{prior_name}]")
        print("==============================")

        model = build_model(log_w_sub, prior_alpha, prior_beta)
        idata = sample_model(model)

        global_row, cluster_summary = summarize_prior(
            prior_name=prior_name,
            idata=idata,
            w_sub=w_sub,
            w_full=w_full,
            df_full=df_full,
        )
        global_rows.append(global_row)
        all_cluster_summaries.append(cluster_summary)

    global_summary = pd.DataFrame(global_rows)
    cluster_summary_all = pd.concat(all_cluster_summaries, ignore_index=True)

    overview_file = OUTPUT_TABLES / f"{PREFIX}_prior_comparison.xlsx"
    with pd.ExcelWriter(overview_file, engine="openpyxl") as writer:
        global_summary.to_excel(writer, sheet_name="prior_global_summary", index=False)
        cluster_summary_all.to_excel(writer, sheet_name="cluster_summary", index=False)

    print("\nPrior comparison saved:", overview_file)
    print(global_summary.to_string(index=False))


if __name__ == "__main__":
    main()

