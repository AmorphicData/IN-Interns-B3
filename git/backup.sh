#!/bin/bash
#Author Name: Tarun Adhikari
#Publish Date: Feb 14, 2024
#Last Updated: Feb 15, 2024

src="https://github.com/TarunAdhikari1212/dummy.git"
back_up="https://github.com/TarunAdhikari1212/backup.git"
sdir="src_dir"
bdir="bacup"

if [ -d "$sdir" ]; then
    echo "Source found."
    git clone "$src" "$sdir"
else
    exit 1
fi
#Creating a backup directory
if [ ! -d "$bdir" ]; then
    echo "No backup folder found. Creating....."
    mkdir "$bdir"
fi

cd "$bdir" || exit 1
git clone "$back_up" "$bdir"
echo "Backup folder created"

cd "../$sdir"
git pull origin main

#Checking for changes in source dir & create a backup in backup dir
change_arr=($( git diff --name-only main origin/main ))
if [[ ${#change_arr[@]} -ne 0 ]]; then
    git pull -X theirs origin main
    cd ..
    for f in "${change_arr[@]}"; do
        cp "$sdir/$f" "$bdir"
    done 
else
    echo "No changes found"
fi

#Added and committed changes in backup directory to remote
cd "$bdir" || exit 1
git add .
git commit -m "Backed up on: `date +'%Y-%m-%d %H:%M:%S'`"
git push origin main

# Every 5 mins run this script
# systemctl start crond
# */5 * * * * backup.sh