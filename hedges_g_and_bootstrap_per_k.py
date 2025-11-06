
#!/usr/bin/env python3
"""
pytho

Usage:
    python hedges_g_and_bootstrap_per_k.py group1.csv group2.csv

Each CSV should contain a single column of numeric observations (optionally a header).
Computes:
 - n1, n2, means, sample SDs (ddof=1)
 - pooled SD (correct formula)
 - Cohen's d
 - Hedges' g (small-sample correction)
 - bootstrap 95% CI for Hedges' g (percentile method)
"""
import sys
import numpy as np

def read_1col_csv(path):
    """Read a CSV with one numeric column (optionally header). Returns 1D numpy array."""
    try:
        data = np.loadtxt(path, delimiter=',', ndmin=1)
    except Exception:
        data = np.loadtxt(path, delimiter=',', ndmin=1, skiprows=1)
    return data.astype(float)

def pooled_sd_from_samples(x, y):
    """Compute pooled standard deviation from raw samples x and y (ddof=1)."""
    n1, n2 = len(x), len(y)
    sd1 = np.std(x, ddof=1)
    sd2 = np.std(y, ddof=1)
    pooled = np.sqrt(((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2))
    return pooled, sd1, sd2

def cohen_d(x, y, pooled_sd):
    """Cohen's d (difference in means divided by pooled SD)."""
    return (np.mean(x) - np.mean(y)) / pooled_sd

def hedges_g_from_d(d, n1, n2):
    """Apply Hedges' small-sample correction J to Cohen's d."""
    J = 1 - (3.0 / (4.0 * (n1 + n2) - 9.0))
    return d * J

def bootstrap_hedges_g(x, y, n_boot=5000, rng=None):
    """Bootstrap Hedges' g by resampling within each group. Returns bootstrap array."""
    if rng is None:
        rng = np.random.default_rng()
    n1, n2 = len(x), len(y)
    boots = np.empty(n_boot)
    for i in range(n_boot):
        bx = rng.choice(x, size=n1, replace=True)
        by = rng.choice(y, size=n2, replace=True)
        pooled, sd1, sd2 = pooled_sd_from_samples(bx, by)
        if pooled <= 0:
            boots[i] = np.nan
            continue
        d = cohen_d(bx, by, pooled)
        boots[i] = hedges_g_from_d(d, n1, n2)
    return boots

def percentile_ci(arr, lower=2.5, upper=97.5):
    """Percentile CI, ignoring NaNs."""
    clean = arr[~np.isnan(arr)]
    if clean.size == 0:
        return np.nan, np.nan
    return np.percentile(clean, [lower, upper])

def main(argv):
    if len(argv) != 3:
        print("Usage: python hedges_g_and_bootstrap_per_k.py group1.csv group2.csv")
        sys.exit(2)

    g1_path, g2_path = argv[1], argv[2]
    x = read_1col_csv(g1_path)
    y = read_1col_csv(g2_path)

    print(f"Loaded group1: {len(x)} observations from {g1_path}")
    print(f"Loaded group2: {len(y)} observations from {g2_path}")

    n1, n2 = len(x), len(y)
    m1, m2 = np.mean(x), np.mean(y)
    pooled, sd1, sd2 = pooled_sd_from_samples(x, y)

    print("\nDiagnostics:")
    print(f" n1 = {n1}  n2 = {n2}")
    print(f" mean1 = {m1:.6g}  mean2 = {m2:.6g}")
    print(f" sd1 (sample, ddof=1) = {sd1:.6g}  sd2 (sample, ddof=1) = {sd2:.6g}")
    print(f" pooled_sd = {pooled:.6g}")

    if pooled <= 0:
        print("\nERROR: pooled_sd is zero or negative. Check your inputs.")
        sys.exit(1)

    d = cohen_d(x, y, pooled)
    g = hedges_g_from_d(d, n1, n2)

    print("\nEffect sizes:")
    print(f" Cohen's d = {d:.6g}")
    print(f" Hedges' g (bias corrected) = {g:.6g}")

    if pooled < 1e-6:
        print("\nWARNING: pooled_sd is extremely small; effect sizes will be huge and unstable.")
    if abs(d) > 10:
        print("\nWARNING: Cohen's d magnitude > 10 — double-check that you are using raw observations")
    if np.isnan(d) or np.isnan(g):
        print("\nERROR: NaN encountered in effect size computation. Check inputs.")
        sys.exit(1)

    print("\nBootstrapping Hedges' g (5000 resamples)...")
    boots = bootstrap_hedges_g(x, y, n_boot=5000)
    ci_low, ci_high = percentile_ci(boots, 2.5, 97.5)
    mean_boot = np.nanmean(boots)

    print(f" Bootstrap mean (Hedges' g) = {mean_boot:.6g}")
    print(f" 95% percentile CI = [{ci_low:.6g}, {ci_high:.6g}]")

    print("\nSUMMARY:")
    print("n1, n2, mean1, mean2, sd1, sd2, pooled_sd, cohen_d, hedges_g, ci_low, ci_high")
    print(f"{n1}, {n2}, {m1:.8g}, {m2:.8g}, {sd1:.8g}, {sd2:.8g}, {pooled:.8g}, {d:.8g}, {g:.8g}, {ci_low:.8g}, {ci_high:.8g}")

if __name__ == "__main__":
    main(sys.argv)