#!/bin/bash

## Automated Backup Script
# Author Name: Ananya Paliwal
# Publish Date: Feb 14, 2024
# Last Updated: Feb 16, 2024

## Define variables
source_directory="/Users/ananyapaliwal/practice/Practice-purpose"
backup_directory="/Users/ananyapaliwal/practice/Backup"
remote_repository="https://github.com/ananyapaliwal/Practice-purpose.git"
branch="main"

## Check if source directory exists
if [ ! -d "$source_directory" ]; then
    echo "Error: Source directory not found."
    exit 1
fi

## Check if backup directory exists, create if not
if [ ! -d "$backup_directory" ]; then
    mkdir -p "$backup_directory"
fi

## Check if there are changes in the source directory
cd "$source_directory" || exit 1
if [ -n "$(git status --porcelain)" ]; then
    echo "There are changes in the source directory."
else
    echo "No changes in the source directory. Exiting."
    exit 0
fi

## Copy changes to the backup directory
rsync -av --delete "$source_directory/" "$backup_directory"

## Initialize Git in the backup directory (if not already done)
cd "$backup_directory" || exit 1
if [ ! -d ".git" ]; then
    git init
    git remote add origin "$remote_repository"
fi

## Commit and push changes to the remote repository
git checkout "$branch"
git add .
git commit -m "Automated backup on $(date)"
git push origin "$branch"

echo "Backup and push completed successfully."

## Add crontab entry to run the script every 5 minutes
echo "*/5 * * * * /Users/ananyapaliwal/practice/check.sh" | crontab -
