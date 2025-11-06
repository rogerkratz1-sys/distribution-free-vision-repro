#!/usr/bin/env python3
"""
recompute_cohens_d.py
Recompute Cohen's d from recorded per-trial arrays (preferred) or from per_k_summary.csv (fallback).
Usage: python recompute_cohens_d.py [--npz g_test_outputs.npz] [--csv per_k_summary.csv]
"""
import argparse, numpy as np, pandas as pd, sys, os

def cohens_d_from_arrays(a, b):
    s_pooled = np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2.0)
    return (a.mean() - b.mean()) / s_pooled if s_pooled != 0 else float('inf')

def from_npz(npz_path):
    npz = np.load(npz_path, allow_pickle=True)
    out = []
    # Heuristic keys used in this repository; edit if your NPZ uses different names.
    key_map = {
        'davg': ('d_null','d_cluster'),
        'mutual': ('m_null','m_cluster'),
    }
    for metric, (k_null, k_cluster) in key_map.items():
        if k_null in npz and k_cluster in npz:
            null = npz[k_null]
            cluster = npz[k_cluster]
            # If arrays are 2D (multiple ks), caller should run with --csv or edit index mapping.
            if null.ndim == 2 or cluster.ndim == 2:
                raise RuntimeError("Found 2D arrays for metric; run with CSV or edit script to select k index.")
            d = cohens_d_from_arrays(null, cluster)
            out.append((metric, d, null.mean(), cluster.mean()))
    return out

def from_csv(csv_path):
    df = pd.read_csv(csv_path)
    rows = []
    for _, r in df.iterrows():
        mean_null = r.get('mean_null')
        mean_cluster = r.get('mean_cluster')
        sp = r.get('pooled_sd') or r.get('s_pooled') or r.get('pooled_sd_est')
        try:
            if pd.notna(sp):
                d = (float(mean_null) - float(mean_cluster)) / float(sp)
                rows.append((r['metric'], int(r['k']), d))
            else:
                rows.append((r['metric'], int(r['k']), float('nan')))
        except Exception:
            rows.append((r.get('metric','?'), r.get('k','?'), float('nan')))
    return rows

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--npz', default='g_test_outputs.npz')
    p.add_argument('--csv', default='per_k_summary.csv')
    args = p.parse_args()
    if os.path.exists(args.npz):
        try:
            out = from_npz(args.npz)
            if out:
                for metric, d, mu1, mu2 in out:
                    print(f"{metric}: mean_null={mu1:.6g}, mean_cluster={mu2:.6g}, recomputed Cohen's d = {d:.6g}")
                return
        except Exception as e:
            print("NPZ approach failed:", e, file=sys.stderr)
    if os.path.exists(args.csv):
        rows = from_csv(args.csv)
        for metric, k, d in rows:
            if pd.isna(d):
                print(f"{metric}, k={k}: cannot recompute (missing pooled_sd in CSV)")
            else:
                print(f"{metric}, k={k}: recomputed Cohen's d = {d:.6g}")
    else:
        print("Neither NPZ nor CSV found. Place g_test_outputs.npz or per_k_summary.csv in this directory.", file=sys.stderr)

if __name__ == '__main__':
    main()
