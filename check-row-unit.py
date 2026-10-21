"""Demonstrate why row unit matters. Python 3; fictional local fixture only."""
import csv
from pathlib import Path
with Path(__file__).with_name('duplicate-rows.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
keys = [(r['entity_id'], r['location_id']) for r in rows]
assert len(rows) == 3
assert len(set(r['entity_id'] for r in rows)) == 1
assert len(set(keys)) == 2
assert len(keys) - len(set(keys)) == 1
print('3 rows; 1 entity; 2 entity/location pairs; 1 repeated pair')
print('A repeated key is a review flag, not permission to delete a row.')
