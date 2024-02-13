#!/bin/bash
#Author Name: Kaustubh Pandey
#Publish Date: Feb 11, 2024
#Last Updated: Feb 13, 2024

# Function to check if branches file exists and read branches from it
read_branches_from_file() {
    if [ -f "$branches_file" ]; then
        while IFS= read -r line; do
            branches+=("$line")
        done < "$branches_file"
    else
        echo "$branches_file not found."
        exit 1
    fi
}

# Function to compare branches
compare_branches() {
    local arr=("$@")
    for branch in "${arr[@]}"; do
        if git show-ref --verify --quiet "refs/heads/$branch"; then
            matched_branches+=("$branch")
        else
            other_branches+=("$branch")
        fi
    done
}

# Function to update branches
update_branches() {
    for branch in "${matched_branches[@]}"; do
        read -p "Do you want to update branch $branch? (yes/no): " choice
        case "$choice" in
            yes)
                git checkout "$branch"
                git merge -X ours -m "Merging branch $branch" $branch
                git push origin "$branch"
                ;;
            no)
                echo "Skipping branch $branch."
                ;;
            *)
                echo "Invalid choice. Skipping branch $branch."
                ;;
        esac
    done
}

# Main script starts here
if [ "$#" -eq 2 ] && [ "$1" == "--file" ]; then
    branches_file="$2"
    read_branches_from_file
else
    echo "Usage: ./file.sh --file <branches_file>"
    exit 1
fi

# Check if branches array is empty
if [ "${#branches[@]}" -eq 0 ]; then
    echo "No valid branches found."
    exit 1
fi

compare_branches "${branches[@]}"

# Print matched and unmatched branches
echo "Branches in the remote:"
echo "Matched branches: ${matched_branches[@]}"
echo "Unmatched branches: ${other_branches[@]}"

# Check if there are matched branches
if [ "${#matched_branches[@]}" -eq 0 ]; then
    echo "No matching branches found."
    exit 0
fi

update_branches



