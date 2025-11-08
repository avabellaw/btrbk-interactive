import os
import sys
import re

snapshots_dir=sys.argv[1]
SNAPSHOT_REGEX="^@([a-zA-Z-]*).([0-9]{4})([0-9]{2})([0-9]{2})T([0-9]{2})([0-9]{2})$"

class Snapshot():
    def __init__(self, snapshot_name):
        self.data = re.search(SNAPSHOT_REGEX, snapshot_name).groups()

        self.subvol, self.year, self.month, self.day, self.hr, self.min = \
            self.data
        
        self.snapshot_name = snapshot_name
        self.path = f"{snapshots_dir}/{snapshot_name}"

def init():
    if not os.path.isdir(snapshots_dir):
        sys.exit(f'Directory "{snapshots_dir}" doesnt exist.')

def get_snapshot_arr():
    return [Snapshot(snapshot) for snapshot in os.listdir(snapshots_dir)]


init()

snapshots = get_snapshot_arr()

for snapshot in snapshots:
    print(snapshot.data)
