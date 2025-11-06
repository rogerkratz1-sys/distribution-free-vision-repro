import pandas as pd
import numpy as np
import math

df = pd.read_csv("per_k_summary_with_hedges.csv", encoding="utf-8")
# compute subject-level n = floor(1000/k)
df["k"] = df["k"].astype(int)
df["n_subj"] = (1000 // df["k"]).astype(int)

# compute J vectorized: J = 1 - 3/(4*N - 9), where N = n1 + n2 = 2 * n_subj
N = 2 * df["n_subj"]
J = 1.0 - 3.0 / (4.0 * N - 9.0)

# ensure numeric cohens_d and handle non-numeric safely
df["cohens_d"] = pd.to_numeric(df["cohens_d"], errors="coerce")
df["hedges_g"] = df["cohens_d"] * J

out = "per_k_summary_with_hedges_subjectN.csv"
df.to_csv(out, index=False, encoding="utf-8")
print("Wrote", out)
print("Rows:", len(df))
print("Sample rows (first 5):")
print(df[["metric","k","cohens_d","n_subj","hedges_g"]].head().to_string(index=False))
