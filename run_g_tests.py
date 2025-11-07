#!/usr/bin/env python3
import argparse, subprocess
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument("--npz", default="g_test_outputs.npz")
p.add_argument("--do-aggregate", action="store_true")
args = p.parse_args()
if not Path(args.npz).exists():
    raise SystemExit(f"{args.npz} not found")
subprocess.check_call(["python","make_per_k_table_from_simple_npz.py","--npz",args.npz] if False else ["python","make_per_k_table_from_simple_npz.py"])
if args.do_aggregate:
    subprocess.check_call(["python","aggregate_per_k_summaries.py"])
print("run_g_tests: done")
