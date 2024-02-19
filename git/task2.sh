#!/bin/bash
## Backup script
# Author Name: Harshini
# Publish Date: Feb 14, 2024
# Last Updated: Feb 15, 2024
## define variables
SOURCE_DIR=“/Users/harshini/documents/work”
BACKUP_DIR=“/Users/harshini/documents/backup_dir”
REMOTE_REPO=“https://github.com/HarshiniBollineni1/work.git”
BRANCH_NAME=“harshini”
## check if source directory exists, exit otherwise
if [ ! -d “$SOURCE_DIR” ]; then
  echo “Error: Source directory does not exist.”
  exit 1
fi
## check if backup directory exists, create one otherwise
if [ ! -d “$BACKUP_DIR” ]; then
  mkdir -p “$BACKUP_DIR”
fi
## check if changes are available in source directory, exit if no changes
if [[ $(git -C “$SOURCE_DIR” status --porcelain) ]]; then
  echo “Changes found in source directory.”
else
  echo “No changes found in source directory. Exiting.”
  exit 0
fi
## copy changes to backup directory
cp -r “$SOURCE_DIR/” “$BACKUP_DIR/”
## initialize git on backup directory if not already initialized
if [ ! -d “$BACKUP_DIR/.git” ]; then
  git -C “$BACKUP_DIR” init
  git -C “$BACKUP_DIR” remote add origin “$REMOTE_REPO”
fi
## commit and push to remote_repo (to your branch)
git -C “$BACKUP_DIR” add .
git -C “$BACKUP_DIR” commit -m “Automated backup changes”
git -C “$BACKUP_DIR” push -u origin “$BRANCH_NAME”
