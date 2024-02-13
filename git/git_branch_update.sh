#!/bin/bash
# Author Name: praneeth miryanam
# Publish Date: May 30, 2023
# Last Updated: Feb 13, 2024

echo "Welcome to the Git Branch Updater Script"

# Define master branch 
master_branch="main"

# checkout master branch, pull latest changes
git checkout $master_branch
git pull origin $master_branch


# Function to trim whitespaces from start and end of branch names
trim() {
    echo "$1" | awk '{$1=$1;print}'
}

# Function to get list of all remote branches except master branch
get_remote_branches() {
    git branch -r | grep -v "$master_branch" | awk -F'origin/' '{print $2}'
}

# Read list of branch names (from console csv input or file input)
# If neither passed, get all remote branches
if [ "$#" -eq 0 ]; then
    branches=$(get_remote_branches)
elif [ "$1" == "-f" ]; then
    if [ -f "$2" ]; then
        branches=$(cat $2)
    else
        echo "File not found!"
        exit 1
    fi
else
    branches=$1
fi

# Verify the remote has all the branches exist from the branches list
valid_branches=()
for branch in $branches; do
    branch=$(trim "$branch")
    if git show-ref "refs/remotes/origin/$branch" >/dev/null; then
        valid_branches+=("$branch")
    else
        echo "Branch $branch does not exist in remote repository."
    fi
done
 

# Show user the valid branches going to be updated
echo "The following branches will be updated:"
echo "$valid_branches"

# If no valid branches, exit the script
if [ -z "$valid_branches" ]; then
    echo "No valid branches to update."
    exit 1
fi

# Ask user input to confirm the update
read -p "Do you want to proceed with updating these branches? (yes/no): " confirm

# If yes, update each branch with the master branch
if [ "$confirm" == "yes" ]; then
    for branch in $valid_branches; do
        echo "Updating branch $branch..."
        git checkout $branch
        git pull origin $master_branch
        git merge -X ours origin $master_branch
        sleep 5
        
        if [ $? -ne 0 ]; then
            echo "Failed to update branch $branch. Exiting..."
            exit 1
        fi
    done
    echo "All branches updated successfully."
else
    echo "Exiting without updating branches."
    exit 0
fi

