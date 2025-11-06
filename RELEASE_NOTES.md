## v1.0.0 — Restore provenance and release outputs

Summary
- Restored PROVENANCE.md, ARTIFACTS.md, and README.md templates.
- Added release artifact `release-outputs-v1.0-perms-repro.zip`.

Contents
- PROVENANCE.md — repository provenance and archival record.
- ARTIFACTS.md — artifact index and verification commands.
- README.md — quick-start and repo layout.
- release-outputs-v1.0-perms-repro.zip — packaged outputs for reviewer convenience.

Verification
- Commit: 9595cfd (pushed to origin/main).
- Smoke test: run `.\verify-environment.ps1` locally to confirm runtime behaviour.

Notes for archivists
- Consider creating a Zenodo snapshot after publishing this release to mint a DOI.
- Include checksums of all artifacts in ARTIFACTS.md for a deterministic snapshot.

Contact
- Maintainer: Roger Kratz <maintainer@example.org>

DOI: https://doi.org/10.5281/zenodo.17517439
