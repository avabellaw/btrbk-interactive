#!/bin/bash

snapshot_path=$1
SNAPSHOT_REGEX="^@([a-zA-Z]*)\.([0-9]{4})([0-9]{2})([0-9]{2})T([0-9]{2})([0-9]{2})$"

if [ ! -d $snapshot_path ]; then
    echo "Directory doesn't exist";
    exit 1
fi

snapshots=$(ls $snapshot_path)

for snapshot in $snapshots; do
    if [[ "$snapshot" =~ $SNAPSHOT_REGEX ]]; then
        subvolume=${BASH_REMATCH[1]}
        year=${BASH_REMATCH[2]}
        month=${BASH_REMATCH[3]}
        day=${BASH_REMATCH[4]}
        hour=${BASH_REMATCH[5]}
        min=${BASH_REMATCH[6]}

        echo "Folder: $subvolume"
        echo "Year: $year"
        echo "Month: $month"
        echo "Day: $day"
        echo "Hour: $hour"
        echo "Min: $min"
    else
        echo "Invalid snapshot name format"
    fi
done