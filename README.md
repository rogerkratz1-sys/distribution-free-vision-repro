# README

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17517439.svg)](https://doi.org/10.5281/zenodo.17517439)

**Distribution-free vision reproducibility repository**

Short summary of the project, goals, and intended audience.

## Quick start

1. Clone the repo
   - `git clone https://github.com/rogerkratz1-sys/distribution-free-vision-repro.git`
2. Create environment
   - Python: `python -m venv .venv`
   - Activate (PowerShell): `.\.venv\Scripts\Activate.ps1`
   - Install dependencies: `pip install -r requirements.txt`
3. Run smoke test
   - PowerShell (recommended on Windows): `.\verify-environment.ps1`
   - Expected result: prints PowerShell and Python versions, runs the sample script, and exits with code 0 when checks pass.

## Structure

- `scripts/` — analysis and utility scripts
- `data/` — raw and processed data (large files are stored externally; see ARTIFACTS.md or PROVENANCE.md for pointers)
- `results/` — generated artifacts
- `docs/` — manuscript and supplementary material
- `PROVENANCE.md` — provenance and archival record
- `ARTIFACTS.md` — artifact index and verification

## Contributing

See CONTRIBUTING.md for guidelines on branching, tests, and release process (create this file if missing).

## License

See LICENSE for full terms; add a LICENSE file (e.g., MIT) to make the project re-usable.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17517439.svg)](https://doi.org/10.5281/zenodo.17517439)
## Appendix E canonical NPZs
Canonical NPZ path: reproducibility/appendix_E_delta_vs_k/g_test_outputs_canonical.npz
Per-metric NPZs: reproducibility/appendix_E_delta_vs_k/g_test_outputs_d_avg.npz, reproducibility/appendix_E_delta_vs_k/g_test_outputs_mutual.npz
Use these paths for downstream aggregation and table regeneration.
## Appendix E canonical NPZs

Canonical NPZ (all-resampling arrays):
- reproducibility/appendix_E_delta_vs_k/g_test_outputs_canonical.npz

Per-metric extracted NPZs:
- reproducibility/appendix_E_delta_vs_k/g_test_outputs_d_avg.npz
- reproducibility/appendix_E_delta_vs_k/g_test_outputs_mutual.npz

Per-k NPZs (examples):
- reproducibility/appendix_E_delta_vs_k/g_test_outputs_davg_k3.npz

These files include delta_obs, delta_perms (n_perm + 1), delta_boots (n_boot + 1), and canonical d_null / d_cluster arrays. See PROVENANCE.md for extraction details and SHA256 digests.
