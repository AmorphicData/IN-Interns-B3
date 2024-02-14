#!/bin/bash
#Author Name: Kaustubh Pandey
#Publish Date: Feb 11, 2024
#Last Updated: Feb 13, 2024
#Master branch name hardcoded.
main="main"
git checkout $main
git pull origin $main
prefix="origin/"
file="$1"
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

