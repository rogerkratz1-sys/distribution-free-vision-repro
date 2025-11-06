#!/usr/bin/env python3
"""
regenerate_table_D.py

Regenerate Table D from input CSVs and produce a CSV table_D_regenerated.csv
Usage:
python regenerate_table_D.py --input data/trials_davg_k3_for_rerun.csv --out outputs/table_D_regenerated.csv --seed 20251030 --fast

Notes:
- This script demonstrates a deterministic pipeline: grouping, summary statistics,
  and a small permutation-based check for each (metric,k) pair. It has a --fast
  mode that uses fewer permutations for quick verification.
"""
from __future__ import annotations
import argparse
import csv
import sys
from collections import defaultdict
import numpy as np
import os

def read_table_rows(path):
    with open(path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            yield row

def summarize_metric_k(rows, metric, k, group_col='label'):
    null_vals = []
    cluster_vals = []
    for r in rows:
        if r.get('metric') != metric or r.get('k') != k:
            continue
        try:
            v = float(r.get('value', ''))
        except Exception:
            continue
        grp = r.get(group_col, '').strip().lower()
        if grp in ('null','0','background','none'):
            null_vals.append(v)
        elif grp in ('cluster','1','target'):
            cluster_vals.append(v)
    return null_vals, cluster_vals

def compute_summary(null_vals, cluster_vals):
    mn_null = float(np.mean(null_vals)) if null_vals else float('nan')
    se_null = float(np.std(null_vals, ddof=1)/np.sqrt(len(null_vals))) if len(null_vals) > 1 else float('nan')
    mn_cluster = float(np.mean(cluster_vals)) if cluster_vals else float('nan')
    se_cluster = float(np.std(cluster_vals, ddof=1)/np.sqrt(len(cluster_vals))) if len(cluster_vals) > 1 else float('nan')
    delta = mn_null - mn_cluster
    return mn_null, se_null, mn_cluster, se_cluster, delta

def quick_perm_pvalue(null_vals, cluster_vals, nperm=10000, seed=20251030):
    rng = np.random.default_rng(seed)
    combined = np.array(list(null_vals) + list(cluster_vals), dtype=float)
    n_null = len(null_vals)
    count = 0
    total = int(nperm)
    for _ in range(total):
        idx = rng.permutation(len(combined))
        perm_null = combined[idx[:n_null]]
        perm_cluster = combined[idx[n_null:]]
        if np.mean(perm_null) - np.mean(perm_cluster) >= (np.mean(null_vals) - np.mean(cluster_vals)):
            count += 1
    p = (count + 1) / (total + 1)
    return p, count

def main(argv):
    p = argparse.ArgumentParser(description="Regenerate Table D summaries and quick checks.")
    p.add_argument('--input', '-i', required=True)
    p.add_argument('--out', '-o', default='outputs/table_D_regenerated.csv')
    p.add_argument('--seed', type=int, default=20251030)
    p.add_argument('--fast', action='store_true', help='Use fewer permutations for speed')
    p.add_argument('--group-col', type=str, default='label')
    args = p.parse_args(argv)

    # collect available metric,k pairs
    rows = list(read_table_rows(args.input))
    pairs = defaultdict(int)
    for r in rows:
        pairs[(r.get('metric'), r.get('k'))] += 1

    rows_by_pair = defaultdict(list)
    for r in rows:
        rows_by_pair[(r.get('metric'), r.get('k'))].append(r)

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    header = ['metric','k','n_null','n_cluster','mean_null','se_null','mean_cluster','se_cluster','delta','perm_p_fast','perm_count_ge_fast']
    with open(args.out, 'w', newline='', encoding='utf-8') as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        for (metric,k), cnt in sorted(pairs.items()):
            pair_rows = rows_by_pair[(metric,k)]
            null_vals, cluster_vals = summarize_metric_k(pair_rows, metric, k, group_col=args.group_col)
            if not null_vals or not cluster_vals:
                continue
            mn_null, se_null, mn_cluster, se_cluster, delta = compute_summary(null_vals, cluster_vals)
            nperm = 2000 if args.fast else 10000
            pval, count_ge = quick_perm_pvalue(null_vals, cluster_vals, nperm=nperm, seed=args.seed)
            writer.writerow([metric, k, len(null_vals), len(cluster_vals),
                             f"{mn_null:.12g}", f"{se_null:.12g}",
                             f"{mn_cluster:.12g}", f"{se_cluster:.12g}",
                             f"{delta:.12g}", f"{pval:.12g}", count_ge])
    print(f"Table regenerated to {args.out}")

if __name__ == "__main__":
    main(sys.argv[1:])

