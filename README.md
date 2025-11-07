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
#### Reproducing Appendix E per-k NPZs
Run python run_k_test.py --metric davg --k 3 to generate a per-k NPZ (or pass --trials path/to/trials.csv). The script writes reproducibility/appendix_E_delta_vs_k/g_test_outputs_<metric>_k<k>.npz and prints SHA256 to stdout; copy the SHA into PROVENANCE.md with the repo commit.

Verification note for Appendix E k=3: the canonical NPZ is reproducibility/appendix_E_delta_vs_k/g_test_outputs_davg_k3.npz (expected SHA256 b0a00a8c4ba358eee58ad9b795e28cefaa29c513c90adf89ca31a32a7d64b5fb). Confirm correctness by running the included verifier: python verify_k3.py (it checks the SHA and that delta_obs == mean(per_trial)). To regenerate from source, run the patched runner: python run_k_test.py --metric davg --k 3. If you regenerate, record the new SHA and brief rationale in PROVENANCE.md.

