#!/bin/bash
#Author Name: Ananya Paliwal
#Publish Date: Feb 11, 2024
#Last Updated: Feb 14, 2024
#Master branch name hardcoded.
main="main"
git checkout $main
git pull origin $main
prefix="origin/"
file="$2"
if [ -s "$file" ];
then
        echo "List of branches:"
        while read -r line;
        do
                echo "$line"
        done < "$file"
else
        git branch -r
fi
#Creation of a array for valid branches only!
branches_array=()
echo "Validating from remote branches...."
for i in $(git branch -r);
do
        branch="${i#$prefix}"
        if grep -q -e "$branch" "$file";
        then
                echo "Branch $branch found in remote"
                branches_array+=("$branch")
        fi
done
if [ ${#branches_array[@]} -eq 0 ]; then
    echo "Array is empty."
else
    echo "Array is not empty."
fi
read -p "Want to continue updation with the $main(yes/no):" chk
case $chk in
        "yes")
                for branch in "${branches_array[@]}";
                do
                        echo "Merging main in branch $branch"
                        git checkout $branch
                        #git pull origin $branch
                        git merge -X ours -m "Merging main in $branch" $main
                        git push origin $branch
                        sleep 5
                done
                ;;
        "no")
                echo "!"
                exit
                ;;
        *)
                echo "Wrong Input"
                exit
                ;;
esac
