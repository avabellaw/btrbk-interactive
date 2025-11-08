import os
import sys
import re
import calendar

snapshots_dir = sys.argv[1]
SNAPSHOT_REGEX = "^@([a-zA-Z-]*).([0-9]{4})([0-9]{2})([0-9]{2})T([0-9]{2})([0-9]{2})$"


class Snapshot():
    def __init__(self, snapshot_name):
        self.data = re.search(SNAPSHOT_REGEX, snapshot_name).groups()

        self.subvol, self.year, self.month, self.day, self.hr, self.min = \
            self.data

        self.snapshot_name = snapshot_name
        self.path = f"{snapshots_dir}/{snapshot_name}"

    def __str__(self):
        return f"@{self.subvol} {self.day} {calendar.month_name[int(self.month)][:3]}"


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
        self.parent_dir = ""
        self.subvol = ""

    def list(self):
        for s in self.snapshots:
            print(s)


init()

snapshots = get_snapshot_arr()

manage = ManageSnapshots(snapshots)

manage.list()
