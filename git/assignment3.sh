#!/bin/bash
#Author Name: Nayan Sachan
#Publish Date: 14 feb 2024
#Last Updated: 18 feb 2024

exec < /dev/tty ## helps in forcing the script to take keyboard input
commit_msg_file="$1"
commit_msg=$(cat "$commit_msg_file")
allowed_prefixes=("add" "update" "remove" "refactor" "bug-fix" "document" "updated" "Added" "Test" "bug-Fix")
# Get the commit message
# echo $commit_msg
# Validate the prefix from the list of allowed prefixes
valid_prefix=false
for prefix in "${allowed_prefixes[@]}"; do
    if [[ "$commit_msg" =~ ^"$prefix":.+ ]]; then
        valid_prefix=true
        break
    fi
done
#echo $valid_prefix
# Exit with a warning if validation fails
if [ "$valid_prefix" = false ]; then
    echo "Error: Commit message prefix is not one of the allowed prefixes:"
    printf '%s:\n' "${allowed_prefixes[@]}"
    exit 1
fi
# Prompt user for confirmation to continue the commit
echo "Commit message: $commit_msg"
read -p "Do you want to continue with this commit? (yes/no): " answer
if [ "$answer" != "yes" ]; then
    echo "Commit aborted."
    exit 1
fi
