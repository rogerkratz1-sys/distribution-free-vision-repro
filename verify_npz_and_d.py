import numpy as np
npz = np.load("g_test_outputs.npz", allow_pickle=True)
print("keys:", npz.files)
print({k: npz[k].shape for k in npz.files})
for name,(a_k,b_k) in (("davg",("d_null","d_cluster")),("mutual",("m_null","m_cluster"))):
    a,b = npz[a_k], npz[b_k]
    sp = ((a.var(ddof=1)+b.var(ddof=1))/2.0)**0.5
    d = (a.mean()-b.mean())/sp if sp!=0 else float("inf")
    print(f"{name}: mean_null={a.mean():.6g}, mean_cluster={b.mean():.6g}, pooled_sd={sp:.6g}, cohens_d={d:.6g}")
print("equality checks:", np.allclose(npz["d_null"],npz["m_null"]), np.allclose(npz["d_cluster"],npz["m_cluster"]))
