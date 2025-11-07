# Reproducibility checklist for Appendix E k = 3

This short file explains how reviewers can verify the k=3 results quickly and reliably.

**Canonical file**
- Path: reproducibility/appendix_E_delta_vs_k/g_test_outputs_davg_k3.npz  
- Expected SHA256: **b0a00a8c4ba358eee58ad9b795e28cefaa29c513c90adf89ca31a32a7d64b5fb**

**Correctness invariant**
- The NPZ is correct for Exhibit E if and only if **delta_obs == mean(per_trial)** inside the NPZ.

**Quick verification (recommended)**
1. From the repo root run the included verifier:

   python verify_k3.py

   Exit codes:
   - 0 = SHA matches expected and delta_obs == mean(per_trial)  
   - 1 = file missing  
   - 2 = SHA mismatch  
   - 3 = internal inconsistency (delta_obs != mean(per_trial))

2. Alternatively, the same check can be performed manually:

   - Print SHA:
     Get-FileHash reproducibility\appendix_E_delta_vs_k\g_test_outputs_davg_k3.npz -Algorithm SHA256
   - Confirm delta_obs equals mean(per_trial):
     `python
     import numpy as np
     d = np.load("reproducibility/appendix_E_delta_vs_k/g_test_outputs_davg_k3.npz", allow_pickle=True)
     print(float(np.asarray(d["delta_obs"]).ravel()[0]), float(np.asarray(d["per_trial"]).mean()))
     `

**Regenerating the NPZ**
- If reviewers want to regenerate the NPZ from source, run the patched runner included in this repository:

  python run_k_test.py --metric davg --k 3

- The patched runner recomputes delta_obs := mean(per_trial) (when per_trial is present) and writes the NPZ. If Windows file locking prevents atomic replace, the repository also contains a fixed NPZ and provenance entry that reviewers can use instead.

**If you regenerate**
- Record the resulting SHA in PROVENANCE.md with a brief rationale. The repository already contains the canonical corrected SHA for k=3 above; if you produce an alternate file, document why and supply the new SHA.

**Notes for reviewers**
- If you encounter WinError 5 or other file-lock issues when the generator attempts an atomic replace, use the canonical NPZ above for verification and record your regeneration attempt and SHA in PROVENANCE.md.

Thank you for verifying our work.
