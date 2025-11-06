# ARTIFACTS.md

**Repository artifacts index**

This file maps produced artifacts to the scripts and CI jobs that generate them. Each artifact entry lists: path, generator script, verification command, expected format, and checksum.

- **artifact: results/aggregate.csv**  
  **generator:** scripts/run_analysis.py  
  **verify:** `python -m scripts.verify results/aggregate.csv`  
  **format:** CSV (UTF-8, comma)  
  **checksum:** sha256:...

- **artifact: figures/figure1.png**  
  **generator:** scripts/plot_figure1.py  
  **verify:** `python scripts/verify_figure1.py`  
  **format:** PNG (300 dpi)  
  **checksum:** sha256:...

- **artifact: environment/requirements.txt**  
  **generator:** `pip freeze > environment/requirements.txt`  
  **verify:** `pip check`  
  **format:** plain text

- **CI smoke tests:** list of CI jobs that validate artifact generation and exit codes.

- **Notes on reproducibility:** how to re-run long jobs (e.g., estimated runtime, HPC hints, checkpointing), and where large raw data is stored (external links or access instructions).
