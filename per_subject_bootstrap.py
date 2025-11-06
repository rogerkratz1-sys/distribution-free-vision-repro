#!/usr/bin/env python3
# usage: python per_subject_bootstrap.py k
import sys, numpy as np

def pooled_sd(x, y):
    sd1, sd2 = x.std(ddof=1), y.std(ddof=1)
    return (((len(x) - 1) * sd1 * sd1 + (len(y) - 1) * sd2 * sd2) / (len(x) + len(y) - 2)) ** 0.5

def hedges_from_samples(x, y):
    psd = pooled_sd(x, y)
    d = (x.mean() - y.mean()) / psd
    J = 1.0 - (3.0 / (4.0 * (len(x) + len(y)) - 9.0))
    return d, d * J, psd

def block_means(arr, k):
    m = len(arr) // k
    return arr[:m * k].reshape(m, k).mean(axis=1)

def bootstrap_g(x_sub, y_sub, n_boot=5000, rng=None):
    if rng is None:
        rng = np.random.default_rng()
    n1, n2 = len(x_sub), len(y_sub)
    boots = []
    for _ in range(n_boot):
        bx = rng.choice(x_sub, size=n1, replace=True)
        by = rng.choice(y_sub, size=n2, replace=True)
        d, g, _ = hedges_from_samples(bx, by)
        boots.append(g)
    return np.array(boots)

def main():
    if len(sys.argv) != 2:
        print("Usage: python per_subject_bootstrap.py k")
        sys.exit(1)
    k = int(sys.argv[1])
    c = np.loadtxt("d_cluster_clean.csv", ndmin=1)
    n = np.loadtxt("d_null_clean.csv", ndmin=1)
    csub = block_means(c, k)
    nsub = block_means(n, k)
    if len(csub) != len(nsub):
        m = min(len(csub), len(nsub))
        csub = csub[:m]; nsub = nsub[:m]
    d, g, psd = hedges_from_samples(csub, nsub)
    boots = bootstrap_g(csub, nsub, n_boot=5000)
    ci = np.percentile(boots, [2.5, 97.5])
    print(f"block k={k} per-subj n={len(csub)} mean1={csub.mean():.6g} mean2={nsub.mean():.6g}")
    print(f" pooled_sd={psd:.6g} Cohen_d={d:.6g} Hedges_g={g:.6g}")
    print(f" bootstrap mean_g={np.nanmean(boots):.6g} 95% CI=[{ci[0]:.6g}, {ci[1]:.6g}]")
    print("NOTE: ensure k matches trials-per-subject; if unknown, try plausible k values")

if __name__ == '__main__':
    main()