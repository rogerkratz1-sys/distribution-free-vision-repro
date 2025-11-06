import pandas as pd
def hedges_from_d(d,n1,n2):
    N = int(n1) + int(n2)
    J = 1.0 - (3.0 / (4.0 * N - 9.0))
    return d * J
df = pd.read_csv("per_k_summary.csv", encoding="utf-16")
df["hedges_g"] = df["cohens_d"].apply(lambda d: hedges_from_d(d,1000,1000))
out = "per_k_summary_with_hedges.csv"
df.to_csv(out, index=False, encoding="utf-8")
print("Wrote", out)
