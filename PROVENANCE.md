# PROVENANCE.md
# Format: FILE  |  COMMAND_USED_TO_GENERATE  |  COMMIT_HASH
per_k_summary.csv  |  python make_per_k_table_from_simple_npz.py --npz g_test_outputs.npz --out per_k_summary.csv  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
per_k_summary_extended.csv  |  python aggregate_per_k_summaries.py --pattern gtest_per_k_summary_*.csv --out per_k_summary_extended.csv  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
plot_delta_vs_k.png  |  python plot_delta_vs_k.py --input per_k_summary_extended.csv --output plot_delta_vs_k.png  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
g_test_outputs.npz  |  original full NPZ used to generate per_k CSVs; source: Downloads 11/2/2025 11:52 AM  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
g_test_outputs_forced.npz  |  alternative NPZ with forced settings; source: Downloads 10/31/2025 2:14 PM  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
gtest_per_k_summary.csv  |  per-run aggregated CSV example moved from Downloads 11/2/2025 11:52 AM  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
per_k_summary_from_downloads.csv  |  per_k CSV copied from Downloads (rename preserved)  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
combined_metrics_k3_k10_final.csv  |  combined metrics used for sanity checks  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
mutual_davg_summary.csv  |  alternative summary for mutual/d_avg  |  f3754fb955749f050fda09cc4fd5d2c1cfd76eae
2025-11-03T13:12:43.1676175-08:00  Zenodo DOI: 10.5281/zenodo.17517439  Release tag: v1.0-appendixE.2  Commit: 7546a07
