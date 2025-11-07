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
#### Sentinel handling for per-sample arrays

Some per-sample arrays in g_test_outputs.npz (d_null, d_cluster, m_null, m_cluster) contain a non-data sentinel at index 0 (value 0.0). Downstream scripts that compute per-sample statistics should follow one of these conventions:

- Trim for per-sample analyses (recommended for plots, effect-size computation, CSV regeneration): drop index 0 so arrays contain only true samples. Use this when producing publication tables, figures, or CSV outputs.
- Ignore for archive-preserving checks: keep the NPZ unchanged but explicitly skip index 0 when computing summary statistics.
- Document which approach you used in PROVENANCE.md so reviewers can audit the decision.

#### Sentinel handling for per-sample arrays

Some per-sample arrays in g_test_outputs.npz (d_null, d_cluster, m_null, m_cluster) contain a non-data sentinel at index 0 (value 0.0). Downstream scripts that compute per-sample statistics should follow one of these conventions:

- Trim for per-sample analyses (recommended for plots, effect-size computation, CSV regeneration): drop index 0 so arrays contain only true samples. Use this when producing publication tables, figures, or CSV outputs.
- Ignore for archive-preserving checks: keep the NPZ unchanged but explicitly skip index 0 when computing summary statistics.
- Document which approach you used in PROVENANCE.md so reviewers can audit the decision.


Note: verify_npz_and_d.py now trims a leading sentinel (index 0) from per-sample arrays when computing summaries; see PROVENANCE.md for the patch record.
