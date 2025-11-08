import os
import sys
import re
import calendar
from itertools import groupby

snapshots_dir = sys.argv[1]
SNAPSHOT_REGEX = "^@([a-zA-Z-]*).([0-9]{4})([0-9]{2})([0-9]{2})T([0-9]{2})([0-9]{2})$"


class Snapshot():
    def __init__(self, snapshot_name):
        self.data = re.search(SNAPSHOT_REGEX, snapshot_name).groups()

        self.subvol, self.year, self.month, self.day, self.hr, self.min = \
            self.data

        self.month_name = calendar.month_name[int(self.month)]

        self.snapshot_name = snapshot_name
        self.path = f"{snapshots_dir}/{snapshot_name}"

    def __str__(self):
        return f"@{self.subvol}: {self.hr}:{self.min} {self.day} {self.month_name[:3]} {self.year}"


def init():
    if not os.path.isdir(snapshots_dir):
        sys.exit(f'Directory "{snapshots_dir}" doesnt exist.')


def get_snapshot_arr():
    snapshots = [Snapshot(snapshot) for snapshot in os.listdir(snapshots_dir)]

    return sorted(snapshots,
                  key=lambda s: (s.subvol,
                                 s.year,
                                 s.month,
                                 s.day,
                                 s.hr,
                                 s.min)
                  )


class ManageSnapshots():
    def __init__(self, snapshots):
        self.snapshots = snapshots
        self.snapshots_by_subvol = groupby(snapshots, key=lambda s: s.subvol)

    def list(self):
        for subvol, snapshots in self.snapshots_by_subvol:
            print(f"----\nSubvolume: @{subvol}\n----")

            for date, snapshots_by_date in groupby(snapshots, key=lambda s: f"{s.day} {s.month_name[:3]} {s.year}"):
                print(f"\n{date}")

                for s in snapshots_by_date:
                    print(f"- {s.hr}:{s.min}")


init()

snapshots = get_snapshot_arr()

manage = ManageSnapshots(snapshots)

manage.list()
