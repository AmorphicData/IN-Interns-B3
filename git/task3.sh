#!/bin/bash
# Pre-commit hook script for checking commit message
# Author: Harshini
# Publish Date: Feb 14, 2024
# Last Updated: Feb 19, 2024
# Define the list of allowed commit message prefixes
file="$1"
file_msg=$(cat "$file")
allowed_prefixes=("add" "update" "remove" "refactor" "bug-fix" "document")
# Get the commit message
# Validate the prefix from the list of allowed prefixes
valid_prefix=false
for prefix in "${allowed_prefixes[@]}"; do
    if [[ "$commit_message" =~ ^$prefix:.*$ ]]; then
        valid_prefix=true
        break
    fi
done
# Exit with a warning if validation fails
if [ "$valid_prefix" == false ]; then
    echo "Error: Invalid commit message format."
    echo "Allowed prefixes: ${allowed_prefixes[@]}"
    exit 1
fi
# Prompt user for confirmation to continue the commit
echo "Commit message: $commit_message"
read -p "Do you want to continue with this commit? (yes/no):"  response
# Commit the message, exit otherwise
if [ "$response" != "yes" ]; then
    echo "Commit aborted."
    exit 1
fi


