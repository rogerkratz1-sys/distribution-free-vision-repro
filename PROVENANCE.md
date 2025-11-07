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
