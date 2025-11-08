import os
import sys
import re

snapshots_dir=sys.argv[1]
SNAPSHOT_REGEX="^@([a-zA-Z\-]*)\.([0-9]{4})([0-9]{2})([0-9]{2})T([0-9]{2})([0-9]{2})$"

def init():
    if not os.path.isdir(snapshots_dir):
        sys.exit(f'Directory "{snapshots_dir}" doesnt exist.')

def get_snapshots():
    for snapshot in os.listdir(snapshots_dir):
        print("Snapshot name: ", snapshot)

        data = re.search(SNAPSHOT_REGEX, snapshot)
        subvol, year, month, day, hr, min = data.groups()

        print(subvol, year, month, day, hr, min)

init()

get_snapshots()
