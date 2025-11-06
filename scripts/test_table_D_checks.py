#!/usr/bin/env python3
"""
test_table_D_checks.py

Run quick verification checks on outputs/table_D_regenerated.csv and compare
basic invariants (counts, numeric columns present, no NaN deltas).
Exit with non-zero code if checks fail.
"""
import csv
import sys
import os
import math

OUT = 'outputs/table_D_regenerated.csv'

def fail(msg):
    print("FAIL:", msg)
    sys.exit(2)

if not os.path.exists(OUT):
    fail(f"{OUT} not found. Run regenerate_table_D.py first.")

with open(OUT, newline='', encoding='utf-8') as fh:
    reader = csv.DictReader(fh)
    rows = list(reader)

if not rows:
    fail("Regenerated table is empty")

# basic checks
for i,r in enumerate(rows[:10]):
    try:
        n_null = int(r['n_null'])
        n_cluster = int(r['n_cluster'])
    except Exception:
        fail(f"Row {i} missing integer counts")
    try:
        delta = float(r['delta'])
    except Exception:
        fail(f"Row {i} delta is not numeric")
    if math.isnan(delta):
        fail(f"Row {i} delta is NaN")

print("All quick checks passed.")
sys.exit(0)

