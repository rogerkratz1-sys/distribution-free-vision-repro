# README

**Project title**

Short summary of the project, goals, and intended audience.

## Quick start

1. Clone the repo
2. Create environment
   - Python: `python -m venv .venv` ; `.\.venv\Scripts\Activate.ps1` ; `pip install -r environment/requirements.txt`
3. Run smoke test
   - `.\verify-environment.ps1` (PowerShell) or `bash scripts/run_smoke.sh`

## Structure

- `scripts/` — analysis and utility scripts
- `data/` — raw and processed data (large files external; include pointers)
- `results/` — generated artifacts
- `docs/` — manuscript and supplementary material
- `PROVENANCE.md` — provenance and archival record
- `ARTIFACTS.md` — artifact index and verification

## Contributing

See CONTRIBUTING.md for guidelines on branching, tests, and release process.

## License

Specify license and copyright.
