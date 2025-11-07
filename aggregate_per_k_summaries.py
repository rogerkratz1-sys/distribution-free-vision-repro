#!/usr/bin/env python3
import glob, pandas as pd, sys
files = sorted(glob.glob("per_k_summary*.csv"))
frames = []
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            lines = fh.read().splitlines()
    except Exception:
        with open(f, 'r', encoding='latin-1') as fh:
            lines = fh.read().splitlines()
    if len(lines) <= 1:
        continue
    frames.append(pd.read_csv(f, encoding='utf-8', engine='python'))
if not frames:
    sys.exit("No per_k_summary CSVs with data found")
out = pd.concat(frames, ignore_index=True).drop_duplicates()
if 'metric' in out.columns and 'k' in out.columns:
    out = out.sort_values(['metric','k'])
out.to_csv("per_k_summary_agg.csv", index=False)
print("Wrote per_k_summary_agg.csv (rows={})".format(len(out)))
