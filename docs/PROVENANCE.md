# PROVENANCE

Repository snapshot
- Commit: f5a736089f4059592ce543bdaaef5dab14df266e
- Date: 2025-11-05
- Local path when recorded: C:\Users\ctint\Downloads\appendix_E_delta_vs_k

Environment
- Python: (see env/python_version.txt)
- Pip packages: (see env/requirements.txt)
- Notes: reproduce environment with the above Python and pip freeze output

Key commands used to produce archived outputs
- python scripts/rerun_perms_targeted.py --input data/trials_davg_k3_for_rerun.csv --rows "davg:3" --nperm 500000 --seed 20251030 --nproc 8 --plot --plot-nperm 20000
- python scripts/regenerate_table_D.py --input data/trials_davg_k3_for_rerun.csv --out outputs/table_D_regenerated.csv --seed 20251030 --fast --group-col "label"
- python scripts/regenerate_table_D.py --input data/trials_davg_k3_for_rerun.csv --out outputs/table_D_regenerated.csv --seed 20251030 --fast --group-col "label"  # quick-verify/run repeated for checks

RNG seeds and deterministic notes
- Seed used for headline permutation runs: 20251030
- Notes: Use the same seed and command-line flags to reproduce the exact outputs listed below. If using different hardware or Python builds, numerical differences at floating-point rounding may occur.

Primary outputs produced (recorded in repository)
- outputs/table_D_regenerated.csv  (regenerated Table D; seed 20251030; --fast used for quick runs)
- outputs/davg_3_n500000_hist.png  (histogram from 500k permutations; plot_nperm 20000)
- outputs/davg_k3_500k_out.txt

Checksums and manifest
- All tracked file checksums are recorded in checksums/checksums.sha256
- To verify locally: Get-FileHash -Algorithm SHA256 <file>

Repository provenance notes
- Git remote: origin -> https://github.com/rogerkratz1-sys/distribution-free-vision-repro.git
- Branch at time of snapshot: main
- Local commit log (most recent): git log -1 --pretty=format:"%H %cI %an %s"

Contact / maintainer
- Repository maintainer: Roger (local user account: ctint)
- Local machine: record or paste machine/OS details here if desired

