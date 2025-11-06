import pandas as pd
import numpy as np

df = pd.read_csv("per_k_summary.csv")
# If df contains per-k per-group sample sizes n1 and n2, use them; otherwise use n_subj inferred from other columns.
# Here we apply the standard correction using total sample size per row if columns n1,n2 exist; otherwise infer N = n1+n2.
if {'n1','n2'}.issubset(df.columns):
    N = df['n1'] + df['n2']
else:
    # fallback: try to infer per-subject n from context or set N to NaN so we only apply approximate correction
    N = None

def hedges_from_d(d, n1=None, n2=None):
    if n1 is None or n2 is None:
        # approximate J using large-N formula with N->inf gives J~1; here we return d unchanged if sizes unknown
        return d
    J = 1.0 - (3.0 / (4.0*(n1 + n2) - 9.0))
    return d * J

if N is not None:
    df['hedges_g'] = df.apply(lambda r: hedges_from_d(r['cohens_d'], int(r['n1']), int(r['n2'])), axis=1)
else:
    df['hedges_g'] = df['cohens_d']  # placeholder if sample sizes unavailable

df.to_csv("per_k_summary_with_hedges.csv", index=False)
print("Wrote per_k_summary_with_hedges.csv (hedges_g column added).")