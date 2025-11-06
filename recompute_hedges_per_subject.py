import pandas as pd, math
def hedges_from_d(d,n1,n2):
    N = int(n1) + int(n2)
    J = 1.0 - (3.0 / (4.0 * N - 9.0))
    return d * J
df = pd.read_csv("per_k_summary_with_hedges.csv", encoding="utf-8")
df["n_subj"] = df["k"].astype(int).apply(lambda k: math.floor(1000.0/float(k)))
df["hedges_g"] = df.apply(lambda r: hedges_from_d(r["cohens_d"], r["n_subj"], r["n_subj"]), axis=1)
df.to_csv("per_k_summary_with_hedges_subjectN.csv", index=False, encoding="utf-8")
print("Wrote per_k_summary_with_hedges_subjectN.csv")
