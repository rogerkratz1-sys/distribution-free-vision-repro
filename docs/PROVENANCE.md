Commands run:
python scripts/rerun_perms_targeted.py --input data/trials_davg_k3_for_rerun.csv --rows "davg:3" --nperm 500000 --seed 20251030 --nproc 8 --plot --plot-nperm 20000
python scripts/regenerate_table_D.py --input data/trials_davg_k3_for_rerun.csv --out outputs/table_D_regenerated.csv --seed 20251030 --fast --group-col "label"
Outputs produced: outputs/table_D_regenerated.csv; outputs/davg_3_n500000_hist.png; outputs/davg_k3_500k_out.txt
Seed: 20251030
Date: 2025-11-05
