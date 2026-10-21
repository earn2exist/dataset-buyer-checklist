"""Fictional fixture: manually assigned origins, not automatic verification."""
import csv
from pathlib import Path
rows = list(csv.DictReader(Path(__file__).with_name("source-origins.csv").open()))
known = {r["origin_id"] for r in rows if r["origin_id"] not in ("", "unknown")}
assert len(rows) == 4
assert len(known) == 2
assert sum(r["independent_test"] == "yes" for r in rows) == 1
print("4 pages; 2 known origins; 1 independent test. Fictional, manually classified example.")
