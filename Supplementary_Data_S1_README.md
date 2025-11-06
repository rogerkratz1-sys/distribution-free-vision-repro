If present, per_k_summary.csv contains trial-level Cohen's d in the column cohens_d (computed as (mean_null - mean_cluster)/pooled SD with pooled SD = sqrt(((n1-1)s1^2 + (n2-1)s2^2)/(n1+n2-2)) using ddof=1). We provide two derived files for convenience: per_k_summary_with_hedges.csv, where hedges_g was computed using trial-level ensemble sizes n1 = n2 = 1000; and per_k_summary_with_hedges_subjectN.csv, where hedges_g was computed using subject counts n = floor(T/k) per row (T = 1000). Hedges' g was obtained by applying the small-sample correction J = 1 - 3/(4N - 9) with N = n1 + n2. Original per_k_summary.csv is encoded UTF-16LE; generated CSVs are encoded UTF-8 for portability. Exact regeneration commands are provided below.

Regeneration commands (PowerShell-safe)

- Inspect original header (UTF-16LE)
python -c "import pandas as pd; df=pd.read_csv('per_k_summary.csv',encoding='utf-16',nrows=1); print('Columns:',list(df.columns))"

- Recreate per_k_summary_with_hedges.csv (Hedges g using trial-level n1=n2=1000)
python -c "import pandas as pd; df=pd.read_csv('per_k_summary.csv',encoding='utf-16'); J=lambda N: 1.0-(3.0/(4.0*N-9.0)); df['hedges_g']=df['cohens_d'].apply(lambda d: d*J(2000)); df.to_csv('per_k_summary_with_hedges.csv',index=False,encoding='utf-8'); print('Wrote per_k_summary_with_hedges.csv')"

- Recreate per_k_summary_with_hedges_subjectN.csv (Hedges g using subject counts n = floor(1000/k))
python -c "import pandas as pd; df=pd.read_csv('per_k_summary_with_hedges.csv',encoding='utf-8'); df['k']=df['k'].astype(int); df['n_subj']=(1000//df['k']).astype(int); N=2*df['n_subj']; J=1.0-3.0/(4.0*N-9.0); df['cohens_d']=pd.to_numeric(df['cohens_d'],errors='coerce'); df['hedges_g']=df['cohens_d']*J; df.to_csv('per_k_summary_with_hedges_subjectN.csv',index=False,encoding='utf-8'); print('Wrote per_k_summary_with_hedges_subjectN.csv')"
