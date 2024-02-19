#!/bin/bash
## automated backup script
# Author Name: Saksham Dhillon
# Publish Date: Feb 14, 2024
# Last Updated: Feb 14, 2024
backup_dir=bkdir
source_dir=test
source_main=main
backup_main=main
backup_link="https://github.com/RounakChauhan123/backup_git"
#Check if Source Dir exists
if [ ! -d "$source_dir" ]; then
       
        echo "Source directory does n't exists"
        exit 1
else
        echo "Source Directory exists"
fi
#Check if backup dir exists else create one and initialise backup git repo in it
if [ ! -d "$backup_dir" ]; then
         mkdir -p "$backup_dir"
         cd "$backup_dir"
         git clone "$backup_link" 
         echo "Backup directory does n't exists but created"
         cd ..
         
else
         
         echo "Backup Directory exisits"
fi
#ls

start_time=$(date +%s)
cd "$source_dir"

git pull origin "$source_main"
 #git clone "$backup_link"
#store all changed files names in changed_files array
changed_files=($(git diff --name-only main origin/main ))
 #git config pull.rebase false 
if [ ${#changed_files[@]} -eq 0 ]; then
    echo "No changed files found."
else
 #git pull -X theirs --no-edit origin "$source_main" -m "Your default merge message here"
#PULL command to fetch changes from source remote to our source local
 git pull -X theirs origin "$source_main"
 #git commit -m "Updated local source repo with remote source repo"


 
 cd ..
 #Copying all changed files in backup_dir
 for file in "${changed_files[@]}"; do
     cp "$source_dir/$file" "$backup_dir/backup_git"
 done
 cd "$backup_dir"
 cd backup_git
 for file in "${changed_files[@]}"; do
     git add "$file"
 done
#git add backup_git
#Pushing the changed files on backup repo
 git commit -m "Cloned from source repo"
 git push origin "$backup_main"
 cd ..
 cd ..
fi
cd ..
end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "Execution Time: $execution_time seconds"
     


# crontab -e */5 * * * *




