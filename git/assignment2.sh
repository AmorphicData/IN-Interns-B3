#./bin/bash
#Author Name: Nayan Sachan
#Publish Date: 14 Feb 2024
#Last Updated: 16 Feb 2024

backup_dir=bkdir
source_dir=test
source_main=main
backup_main=main
#check for source dir
if [ ! -d "$source_dir" ];then
    echo "Source Direcotry does not exists"
    exit 1
else:
    echo "Source Directory Exists"
fi
#check for backup dir
if [ ! -d "$backup_dir" ]; then
    mkdir -p "$backup_dir"
    cd "$backup_dir"
    git clone "$backup_git"
    echo "Backup directory does n't exists but created"
    cd ..
else
    echo "Backup Directory exisits"
fi

#check for changed files
cd "$source_dir"
git pull origin "$source_main"
# now i have to check for changed files
changed_files=($(git diff --name-only main origin/main))
if [ ${#changed_files[@]} -eq 0 ];then
    echo "No files Changed"
else
    #pull changes from source
    git pull -X theirs origin "$source_main"
    cd ..
    #copy the changes from src_dir to backup_dir
    for file in "${changed_files[@]}";do
        cp "$source_dir/$file" "$backup_dir/backup_git"
    done
    cd "$backup_dir"/backup_git
    for file in "${changed_files[@]}"; do
        git add "$file"
    done
    git commit -m "Cloned from Source dir"
    git push origin "$backup_main"
    cd ..
    cd ..
fi
cd ..



#crontab command 

# */5 * * * * assignment2.sh
