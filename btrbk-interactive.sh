snapshot_path=$1

if [ ! -d $snapshot_path ]; then
    echo "Directory doesn't exist";
    exit 1
fi

