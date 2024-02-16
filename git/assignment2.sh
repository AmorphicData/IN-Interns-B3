#!/bin/bash

# Author Name: Kaustubh Pandey
# Publish Date: 14 Feb 2024
# Last Updated: 16 Feb 2024

backup_git="your_backup_repo_link"
source_main=main
source_dir=test
backup_main=main
backup_dir=bkp_dir

# Function to check if directory exists
check_Source_directory() {
    if [ ! -d "$1" ]; then
        echo "$2 Directory does not exist."
        exit 1
    else
        echo "$2 Directory exists."
    fi
}

check_Backup_directory(){
   if [ ! -d "$1" ]; then
      mkdir -p "$1"
      cd "$1"
      git clone "$backup_git"
      echo "Created $2 directory as it doesn't exist"
      cd ..
   else
      echo "$2 Directory exists"
   fi
}

# Function to perform backup
perform_backup() {
    cd "$source_dir"
    git pull origin "$source_main"

    # Checking for changed files
    changed_files=($(git diff --name-only main origin/main))
    if [ ${#changed_files[@]} -eq 0 ]; then
        echo "No files changed."
    else
        # Pull changes from source
        git pull -X theirs origin "$source_main"
        cd ..
        # Copy the changes from source directory to backup directory
        for file in "${changed_files[@]}"; do
            cp "$source_dir/$file" "$backup_dir/$backup_git"
        done
        cd "$backup_dir"/$backup_git
        for file in "${changed_files[@]}"; do
            git add "$file"
        done
        git commit -m "Cloned from Source directory"
        git push origin "$backup_main"
        cd ..
        cd ..
    fi
    cd ..
}

check_Source_directory "$source_dir" "Source"
check_Backup_directory "$backup_dir" "Backup"

perform_backup

# crontab command
# */5 * * * * assignment2.sh
