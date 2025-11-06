import numpy as np
for f in ("d_cluster_clean.csv","d_null_clean.csv"):
    a = np.loadtxt(f, ndmin=1, delimiter=",")
    vals, counts = np.unique(a, return_counts=True)
    order = counts.argsort()[::-1]
    print(f)
    print(f" n={len(a)} unique={vals.size}")
    for v, c in zip(vals[order][:10], counts[order][:10]):
        print(f"  {v} count={c}")
