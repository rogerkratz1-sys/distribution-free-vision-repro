#!/usr/bin/env python3
r"""
rerun_perms_targeted.py

Usage (PowerShell):
python .\rerun_perms_targeted.py --input .\trials.csv --rows "davg:3" --nperm 500000 --seed 20251030 --nproc 8 --plot --plot-nperm 20000 | Out-File .\out.txt -Encoding utf8

Requirements:
- CSV must include columns: metric, k, value, group
  where group has values like 'null'/'cluster' or '0'/'1'.
"""

from __future__ import annotations
import argparse
import csv
import sys
from typing import List, Tuple
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

def read_values_from_csv(path: str, metric: str, k: str, group_col: str = "group") -> Tuple[List[float], List[float]]:
    with open(path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row; expected header with metric,k,value,group")
        headers = [h.strip() for h in reader.fieldnames]
        # require explicit columns
        if not any(h.lower() == "metric" for h in headers):
            raise ValueError("CSV must have a 'metric' column")
        if not any(h.lower() == "k" for h in headers):
            raise ValueError("CSV must have a 'k' column")
        if not any(h.lower() in ("value","val","score","measurement") for h in headers):
            raise ValueError("CSV must have a numeric 'value' column")
        if group_col not in reader.fieldnames and not any(h.lower() == group_col.lower() for h in reader.fieldnames):
            raise ValueError(f"CSV must contain an explicit group column named '{group_col}' (case-sensitive or state exact header)")

        # find canonical header names used in file
        metric_col = next(h for h in reader.fieldnames if h.lower() == "metric")
        k_col = next(h for h in reader.fieldnames if h.lower() == "k")
        value_col = next(h for h in reader.fieldnames if h.lower() in ("value","val","score","measurement"))
        # find exact group header name (case-insensitive)
        group_name = next(h for h in reader.fieldnames if h.lower() == group_col.lower())

        null_vals = []
        cluster_vals = []
        fh.seek(0)
        reader = csv.DictReader(fh)
        for row in reader:
            try:
                if row[metric_col].strip() != metric or row[k_col].strip() != k:
                    continue
            except KeyError:
                continue
            raw_val = row.get(value_col, "")
            try:
                v = float(raw_val)
            except Exception:
                continue
            grp = row.get(group_name, "").strip().lower()
            if grp in ("null", "background", "0", "none", "n"):
                null_vals.append(v)
            elif grp in ("cluster", "target", "1", "t", "y", "yes"):
                cluster_vals.append(v)
            else:
                # unknown label: skip
                continue

    if not null_vals or not cluster_vals:
        raise ValueError(f"After filtering metric={metric}, k={k} found n_null={len(null_vals)}, n_cluster={len(cluster_vals)}; both must be >0")
    return null_vals, cluster_vals

def observed_delta(null_vals: List[float], cluster_vals: List[float]) -> float:
    return float(np.mean(null_vals) - np.mean(cluster_vals))

def _worker_count_chunk(args):
    chunk_size, combined, n_null, n_cluster, obs_delta, seed_offset = args
    rng = np.random.default_rng(seed_offset)
    count = 0
    total_n = n_null + n_cluster
    comb = np.asarray(combined, dtype=float)
    for _ in range(chunk_size):
        idx = rng.permutation(total_n)
        perm_null = comb[idx[:n_null]]
        perm_cluster = comb[idx[n_null:]]
        delta = float(np.mean(perm_null) - np.mean(perm_cluster))
        if delta >= obs_delta:
            count += 1
    return count

def _worker_sample_deltas(args):
    """
    Worker that returns a list (or numpy array) of sampled deltas for plotting.
    args: (sample_count, combined_array, n_null, n_cluster, seed_offset)
    """
    sample_count, combined, n_null, n_cluster, seed_offset = args
    rng = np.random.default_rng(seed_offset)
    total_n = n_null + n_cluster
    comb = np.asarray(combined, dtype=float)
    out = []
    for _ in range(sample_count):
        idx = rng.permutation(total_n)
        perm_null = comb[idx[:n_null]]
        perm_cluster = comb[idx[n_null:]]
        out.append(float(np.mean(perm_null) - np.mean(perm_cluster)))
    return out

def run_permutation_test_parallel(null_vals: List[float], cluster_vals: List[float],
                                  nperm: int, seed: int, nproc: int,
                                  plot_nperm: int = 10000, make_plot: bool = False,
                                  metric: str = "metric", k: str = "k"):
    n_null = len(null_vals)
    n_cluster = len(cluster_vals)
    obs_delta = observed_delta(null_vals, cluster_vals)
    combined = np.concatenate([np.array(null_vals, dtype=float), np.array(cluster_vals, dtype=float)])
    total_perm = int(nperm)

    workers = max(1, min(int(nproc), cpu_count()))
    base, rem = divmod(total_perm, workers)
    chunk_sizes = [base + (1 if i < rem else 0) for i in range(workers)]
    args_count = []
    seed_base = int(seed)
    for i, cs in enumerate(chunk_sizes):
        args_count.append((cs, combined, n_null, n_cluster, obs_delta, seed_base + 1000 + i))

    # run counting
    with Pool(processes=workers) as pool:
        results = pool.map(_worker_count_chunk, args_count)
    total_count = sum(results)

    # optionally build a sampled distribution for plotting (not used for inference)
    sampled_deltas = None
    if make_plot:
        sample_total = min(int(plot_nperm), total_perm)
        # distribute sample_total across workers
        base_s, rem_s = divmod(sample_total, workers)
        sample_sizes = [base_s + (1 if i < rem_s else 0) for i in range(workers)]
        args_sample = []
        for i, ss in enumerate(sample_sizes):
            args_sample.append((ss, combined, n_null, n_cluster, seed_base + 5000 + i))
        with Pool(processes=workers) as pool:
            lists = pool.map(_worker_sample_deltas, args_sample)
        # flatten
        sampled_deltas = [x for sub in lists for x in sub]

        # make histogram and save PNG
        png_name = f"{metric}_{k}_n{nperm}_hist.png"
        fig, ax = plt.subplots(figsize=(6,4))
        ax.hist(sampled_deltas, bins=100, color="#2c7bb6", alpha=0.8, density=True)
        ax.axvline(obs_delta, color="red", linestyle="--", label=f"obs delta = {obs_delta:.6f}")
        ax.set_xlabel("Permutation delta (mean_null - mean_cluster)")
        ax.set_ylabel("Density")
        ax.set_title(f"Null permutation distribution: {metric}, k={k}, nperm_sample={len(sampled_deltas)}")
        ax.legend()
        fig.tight_layout()
        plt.savefig(png_name, dpi=150)
        plt.close(fig)
    return obs_delta, total_count, sampled_deltas, (n_null, n_cluster)

def parse_rows_arg(rows_arg: str) -> Tuple[str, str]:
    if ':' not in rows_arg:
        raise argparse.ArgumentTypeError("rows argument must be of form metric:k (e.g. davg:3)")
    metric, k = rows_arg.split(':', 1)
    return metric, k

def main(argv):
    p = argparse.ArgumentParser(description="Run targeted permutation tests in parallel.")
    p.add_argument('--input', '-i', required=True, help="Input CSV file (must include metric,k,value,group columns)")
    p.add_argument('--rows', '-r', required=True, help="Rows selector in form metric:k (e.g. davg:3)")
    p.add_argument('--nperm', type=int, default=100000, help="Number of permutations")
    p.add_argument('--seed', type=int, default=20250101, help="Base RNG seed")
    p.add_argument('--batch', type=int, default=1, help="(unused) legacy")
    p.add_argument('--nproc', type=int, default=1, help="Number of processes to use")
    p.add_argument('--plot', action='store_true', help="Save PNG histogram (uses sampling)")
    p.add_argument('--plot-nperm', type=int, default=10000, help="Number of sampled permutations for histogram (default 10000)")
    p.add_argument('--group-col', type=str, default="group", help="Name of group column in CSV (default 'group')")
    args = p.parse_args(argv)

    metric, k = parse_rows_arg(args.rows)
    try:
        null_vals, cluster_vals = read_values_from_csv(args.input, metric, k, group_col=args.group_col)
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(3)

    print(f"Available metric,k pairs and counts: {{('{metric}', '{k}'): {len(null_vals) + len(cluster_vals)}}}")
    print(f"n_null = {len(null_vals)}; n_cluster = {len(cluster_vals)}")

    try:
        obs_delta, count_ge, sampled_deltas, (n_null, n_cluster) = run_permutation_test_parallel(
            null_vals, cluster_vals, args.nperm, args.seed, args.nproc,
            plot_nperm=args.plot_nperm, make_plot=args.plot, metric=metric, k=k)
    except Exception as e:
        print(f"Error during permutation run: {e}", file=sys.stderr)
        sys.exit(4)

    # Two-sided p-value using permutation distribution for one-sided tail count
    # one-sided p = (count_ge + 1) / (nperm + 1). For two-sided, double the smaller tail.
    one_sided = (count_ge + 1) / (args.nperm + 1)
    two_sided = min(1.0, 2.0 * min(one_sided, 1.0 - one_sided))
    print(f"Observed delta (mean_null - mean_cluster): {obs_delta}")
    print(f"Permutations tested: {args.nperm}")
    print(f"Permutations with delta >= observed (one-sided upper tail): {count_ge}")
    print(f"One-sided p-value (with +1 correction): {one_sided}")
    print(f"Two-sided p-value (approx, doubled tail): {two_sided}")
    if args.plot:
        png_name = f"{metric}_{k}_n{args.nperm}_hist.png"
        if os.path.exists(png_name):
            print(f"Histogram PNG saved: {png_name}")
        else:
            print("Plot option requested but PNG not found (unexpected)", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1:])