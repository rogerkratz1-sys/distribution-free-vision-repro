# Appendix E Reproduction instructions

This Appendix README explains how reviewers can reproduce per-k NPZs and verify provenance.

1) Purpose
- The repository includes a canonical NPZ with full resampling arrays and example per-metric / per-k NPZs.
- Reviewers can generate per-k NPZs on demand using run_k_test.py and record SHA256 into PROVENANCE.md.

2) How to run
- Auto-discover trials CSV by metric and k:
  `
  python run_k_test.py --metric davg --k 3\n  `
- Explicit trials CSV:
  `
  python run_k_test.py --metric davg --k 3 --trials path/to/trials_davg_k3_for_rerun.csv\n  ``n
3) What to expect
- Output NPZ path: reproducibility/appendix_E_delta_vs_k/g_test_outputs_<metric>_k<k>.npz
- NPZ contents: per_trial; d_null; d_cluster; delta_obs; delta_perms; delta_boots; meta
- Example stdout after successful run:
  `
  WROTE reproducibility/appendix_E_delta_vs_k/g_test_outputs_davg_k3.npz\n  SHA256 C156E67A7DFF56B280E300913AA15AE82ED23FC6E32C765223F4DE685C6512D8\n  ``n
4) Provenance workflow for reviewers
- Compute SHA256 (PowerShell):
  `
  Get-FileHash -Path reproducibility\\appendix_E_delta_vs_k\\g_test_outputs_<metric>_k<k>.npz -Algorithm SHA256\n  ``n- Append SHA, command used, trials CSV, and repo commit to PROVENANCE.md (a template entry was added earlier).

5) Notes and troubleshooting
- If run_k_test.py cannot auto-find trials CSV, pass --trials with the CSV path.
- NPZ files are tracked in git; if you prefer LFS for future large binaries, contact the maintainers.
