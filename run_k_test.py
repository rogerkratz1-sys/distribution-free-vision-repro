#!/usr/bin/env python3
# run_k_test.py (patched)
import argparse, os, sys, json, glob, hashlib
import numpy as np
import pandas as pd

def sha256(path):
    h = hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def find_trials_csv(metric, k, root="."):
    pattern = f"**/trials_{metric}_k{k}*.csv"
    results = glob.glob(os.path.join(root, pattern), recursive=True)
    if results: return results[0]
    for p in glob.glob(os.path.join(root,"**","trials_*.csv"), recursive=True):
        name = os.path.basename(p).lower()
        if metric.lower() in name and f"k{k}" in name:
            return p
    return None

def load_canonical_npz(outdir):
    p = os.path.join(outdir, "g_test_outputs_canonical.npz")
    if os.path.exists(p):
        return np.load(p, allow_pickle=True)
    return {}

def select_delta_obs_from_canonical(canon, metric_token):
    if "delta_obs" not in canon:
        return np.array([np.nan]), None
    dobs = np.asarray(canon["delta_obs"])
    metric_low = metric_token.lower()
    if dobs.size == 1:
        return np.array([float(dobs[0])]), 0
    if metric_low.startswith("d") or "avg" in metric_low:
        idx = 0
    elif "mutual" in metric_low:
        idx = 1 if dobs.size > 1 else 0
    else:
        idx = 0
    return np.array([float(dobs[idx])]), idx

def main():
    p = argparse.ArgumentParser(description="Produce per-k NPZ for reviewer from trials CSV or metric+k")
    p.add_argument("--metric", required=True, help="metric token (e.g., davg or mutual or d_avg)")
    p.add_argument("--k", required=True, help="k value (e.g., 3)")
    p.add_argument("--trials", help="explicit path to trials CSV (optional)")
    p.add_argument("--outdir", default=os.path.join("reproducibility","appendix_E_delta_vs_k"), help="output directory")
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    trials_path = args.trials or find_trials_csv(args.metric, args.k, root=".")
    if not trials_path:
        print("ERROR: trials CSV not found for metric/k; provide --trials", file=sys.stderr); sys.exit(2)

    df = pd.read_csv(trials_path)
    numeric = df.select_dtypes(include=[float,int])
    if numeric.shape[1] == 0:
        print("ERROR: trials CSV contains no numeric columns", file=sys.stderr); sys.exit(3)
    per_trial = numeric.iloc[:,0].to_numpy(dtype=float)

    canon = load_canonical_npz(args.outdir)
    delta_obs, used_idx = select_delta_obs_from_canonical(canon, args.metric)
    if used_idx is not None:
        try:
            print(f"Selected delta_obs index {used_idx} from canonical delta_obs (shape {np.asarray(canon[\\"delta_obs\\"]).shape}); value {float(delta_obs[0])}")
        except Exception:
            print(f"Selected delta_obs index {used_idx} from canonical delta_obs")
    else:
        print("Warning: canonical delta_obs not found; delta_obs set to NaN")

    outfn = os.path.join(args.outdir, f"g_test_outputs_{args.metric}_k{args.k}.npz")
    np.savez(outfn,
             per_trial = per_trial,
             d_null = canon.get("d_null", np.empty((0,))),
             d_cluster = canon.get("d_cluster", np.empty((0,))),
             delta_obs = delta_obs,
             delta_perms = canon.get("delta_perms", np.empty((0,))),
             delta_boots = canon.get("delta_boots", np.empty((0,))),
             meta = np.array(json.dumps({
                 "source_trial_csv": os.path.abspath(trials_path),
                 "derived_from": os.path.abspath(os.path.join(args.outdir,"g_test_outputs_canonical.npz")) if os.path.exists(os.path.join(args.outdir,"g_test_outputs_canonical.npz")) else None
             }))
    )
    print("WROTE", outfn)
    print("SHA256", sha256(outfn))

if __name__ == "__main__":
    main()
