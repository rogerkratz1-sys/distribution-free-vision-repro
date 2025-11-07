#!/usr/bin/env python3
import hashlib, sys
from pathlib import Path
import numpy as np

def main():
    p = Path("reproducibility/appendix_E_delta_vs_k/g_test_outputs_davg_k3.npz")
    expected = "b0a00a8c4ba358eee58ad9b795e28cefaa29c513c90adf89ca31a32a7d64b5fb"
    if not p.exists():
        print("MISSING:", p)
        return 1
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != expected:
        print("SHA MISMATCH", h)
        return 2
    d = np.load(str(p), allow_pickle=True)
    stored = float(np.asarray(d["delta_obs"]).ravel()[0])
    mean = float(np.asarray(d["per_trial"]).mean())
    print("SHA OK; delta_obs", stored, "per_trial mean", mean)
    if abs(stored - mean) > 1e-12:
        print("INCONSISTENT: delta_obs != mean(per_trial)")
        return 3
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
