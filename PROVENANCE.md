# Provenance for release v1.0.0

- Release: v1.0.0 — Restore provenance and release outputs
- Release URL: https://github.com/rogerkratz1-sys/distribution-free-vision-repro/releases/tag/v1.0.0
- Tag: v1.0.0
- Commit (tag target): 9595cfda228e0bb52490cb408b26e65c18cafb3d
- Published: 2025-11-06 (UTC timestamp as recorded in release)
- Included artifacts:
  - release-outputs-v1.0-perms-repro.zip (asset on the release page)
  - CHECKSUMS.txt (included in release assets)
- Notes:
  - Release body and text assets were normalized to UTF-8 (BOM-free) before publishing.
  - Recommended next step for archival citation: create a Zenodo snapshot of this repository at the published tag to mint a DOI.

Zenodo DOI: https://doi.org/10.5281/zenodo.17517439
per_k_summary_with_hedges.csv — generated from per_k_summary.csv (UTF-16LE) on 2025-11-06 using the one-liner recorded in Supplementary_Data_S1_README.md; hedges_g computed with trial-level ensemble sizes n1 = n2 = 1000 and small-sample correction J = 1 - 3/(4N - 9); output encoded UTF-8.
per_k_summary_with_hedges_subjectN.csv — generated from per_k_summary_with_hedges.csv on 2025-11-06 using recompute_hedges_per_subject_fixed.py; hedges_g computed with subject counts n = floor(1000/k) per row and small-sample correction J = 1 - 3/(4N - 9); output encoded UTF-8.
Release v1.0-hedges.1 — commit 67ca1c2; recorded on 2025-11-06T15:36:24; see Supplementary_Data_S1_README.md for regeneration commands.
Release v1.0-hedges.1 — commit 7ef8a51; recorded on 2025-11-06T15:42:29; see Supplementary_Data_S1_README.md for regeneration commands.
Release v1.0-hedges.1 — commit 401af9d; recorded on 2025-11-06T15:44:15; see Supplementary_Data_S1_README.md for regeneration commands.
2025-11-06: Replaced release CHECKSUMS.txt to match canonical local CHECKSUMS.txt (SHA256: 3A9833BE94D85E557AE3555CC849481ACD7D3300D952325ED9C612D122DBE759).
2025-11-06: Added SHA256 for plot_delta_vs_k_from_npz.png (047CCE40E93BB6D0CEBED2CF52CE1A9ADA77168FEC0639FAE1BF53E7F0550EC9).
2025-11-06: Added CHECKSUMS.txt entries for release-outputs-v1.0-perms-repro.zip (51831867B3EE7632D5ED871971C4700712F9E752B7660F405C4E5776CEDA9D6E) and plot_delta_vs_k_from_npz.png (047CCE40E93BB6D0CEBED2CF52CE1A9ADA77168FEC0639FAE1BF53E7F0550EC9).
2025-11-06: Added placeholder scripts for Appendix E and documented canonical originals in release-outputs-v1.0-perms-repro.zip.
2025-11-06: Converted per_k_summary.csv and per_k_summary_extended.csv from UTF-16 LE to UTF-8 for cross-platform reproducibility.
2025-11-06: ARCHIVE created at ..\release-outputs-v1.0-perms-repro_20251106-205208.zip; SHA256: 46C5BB2E1E94330B3191E3AA20E3B8ECDF6179CBCFC9A9393D6F648C6317D9A1; contents: aggregate_per_k_summaries.py; make_per_k_table_from_simple_npz.py; run_g_tests.py; PROVENANCE.md; per_k_summary_agg.csv; per_k_table_from_npz.csv; g_test_outputs.npz (if present).
2025-11-07 10:44:17 UTC — Added canonical NPZ: reproducibility\\appendix_E_delta_vs_k\\g_test_outputs_canonical.npz
- Source: existing g_test_outputs.npz found in repo root
- Action: copied into repository canonical folder for archival
- SHA256: 16B99D75298F89D701DEBF8A16788D366EDA63EDE96D8BD22591008827FB4328
- Repo commit: 09b0a08
- Keys expected: d_null, d_cluster, m_null, m_cluster, delta_perms, delta_boots, delta_obs
- Notes: delta_perms length should be 50001 and delta_boots length should be 2001; verify mapping of delta_obs to metrics before automated aggregation.
2025-11-07 10:47:21 UTC — Canonical NPZ mapping note
- File: reproducibility/appendix_E_delta_vs_k/g_test_outputs_canonical.npz
- delta_obs mapping: index 0 => d_avg; index 1 => mutual
- delta_perms: length 50001 (n_perm + 1); delta_boots: length 2001 (n_boot + 1)
- Repo commit: 6e9c84f
2025-11-07 10:48:56 UTC — Added per-metric NPZ: reproducibility/appendix_E_delta_vs_k/g_test_outputs_d_avg.npz
- Source: reproducibility/appendix_E_delta_vs_k/g_test_outputs_canonical.npz
- SHA256: AF8B5A6EF699A4F56FE17242F3A0DD14609AFB91932A1F45346CCD0B890C916F
- Repo commit: 6e9c84f
- Keys included: {per-metric arrays plus delta_obs (single element), delta_perms, delta_boots, meta}
- Note: delta_obs mapping assumed index 0 => d_avg, index 1 => mutual (see PROVENANCE.md mapping note)
2025-11-07 10:48:56 UTC — Added per-metric NPZ: reproducibility/appendix_E_delta_vs_k/g_test_outputs_mutual.npz
- Source: reproducibility/appendix_E_delta_vs_k/g_test_outputs_canonical.npz
- SHA256: 16149435749B240F1282FDE72A32F0B487F417197CF31F55D2C0A4224B436287
- Repo commit: 6e9c84f
- Keys included: {per-metric arrays plus delta_obs (single element), delta_perms, delta_boots, meta}
- Note: delta_obs mapping assumed index 0 => d_avg, index 1 => mutual (see PROVENANCE.md mapping note)
