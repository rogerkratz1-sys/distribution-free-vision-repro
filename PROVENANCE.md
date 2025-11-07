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
Fixed g_test_outputs.npz: copied m_* from d_* to repair sentinel mismatch; backup: g_test_outputs.npz.bak; verified with verify_npz_and_d.py; commit 67ca1c2; recorded on 2025-11-06T15:56:54.
Trimmed leading sentinel from d_*/m_* in g_test_outputs.npz; backup saved as g_test_outputs.npz.pretrim.bak; updated d_null_clean.csv and d_cluster_clean.csv; verified with verify_npz_and_d.py; recorded on 2025-11-06T16:01:16
Note: g_test_outputs.npz contains a leading sentinel value (index 0 == 0.0) for d_*/m_* arrays; verification scripts explicitly ignore index-0 when computing per-sample statistics. Recorded on 2025-11-06T16:01:38

2025-11-06 16:23 UTC  |  verify_npz_and_d.py  |  Trimmed leading sentinel at index 0 from per-sample arrays (d_null, d_cluster, m_null, m_cluster) so downstream summaries and CSV regeneration use only true samples. Backup saved as verify_npz_and_d.py.pretrim.bak and verify_npz_and_d.py.backup.pretrim.
2025-11-06: Regenerated CHECKSUMS.txt to fix malformed line endings; reconstructed verify_npz_and_d.py.pretrim.bak from verify_npz_and_d.py.backup.pretrim; uploaded corrected CHECKSUMS.txt to release v1.0.2.
