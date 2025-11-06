import numpy as np
for f in ("./d_cluster.csv","./d_null.csv"):
    a = np.loadtxt(f, delimiter=",", ndmin=1)
    print(f"{f} n={len(a)} min={a.min():.6g} q1={np.percentile(a,25):.6g} med={np.median(a):.6g} q3={np.percentile(a,75):.6g} max={a.max():.6g} std(ddof=1)={np.std(a,ddof=1):.6g}")
