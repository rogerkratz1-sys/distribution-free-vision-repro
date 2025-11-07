#!/usr/bin/env python3
import numpy as np, pandas as pd
from pathlib import Path
p = Path("g_test_outputs.npz")
if not p.exists():
    raise SystemExit("g_test_outputs.npz not found")
d = np.load(str(p), allow_pickle=True)
keys = set(d.files)
if "delta_obs" not in keys:
    raise SystemExit("delta_obs not found in NPZ")
obs = np.asarray(d["delta_obs"])
k_len = obs.shape[0]
perm_mean = None
if "delta_perms" in keys:
    perms = np.asarray(d["delta_perms"])
    if perms.ndim == 2:
        perm_mean = perms.mean(axis=0)
    else:
        try:
            perm_mean = np.vstack(perms).mean(axis=0)
        except Exception:
            perm_mean = None
boot_med = None
if "delta_boots" in keys:
    boots = np.asarray(d["delta_boots"])
    if boots.ndim == 2:
        boot_med = np.median(boots, axis=0)
rows = []
for i in range(k_len):
    row = {"k": int(i+1), "delta_obs": float(obs[i])}
    if perm_mean is not None and len(perm_mean) > i:
        row["delta_perm_mean"] = float(perm_mean[i])
    if boot_med is not None and len(boot_med) > i:
        row["delta_boot_median"] = float(boot_med[i])
    rows.append(row)
pd.DataFrame(rows).to_csv("per_k_table_from_npz.csv", index=False)
print("Wrote per_k_table_from_npz.csv (k_count={})".format(len(rows)))
