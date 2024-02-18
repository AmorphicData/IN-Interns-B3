#!/bin/bash
#Author Name: Tarun Adhikari
#Publish Date: Feb 16, 2024
#Last Updated: Feb 18, 2024

exec < /dev/tty             ## helps in forcing the script to take keyboard input
msg_file="$1"
msg=$(cat "$msg_file")
pref=("add" "update" "remove" "refactor" "bug-fix" "document" "Test" "bug-Fix")

# Validate the prefix from the list of allowed prefixes
valid_prefix=false
for prefix in "${pref[@]}"; do
    if [[ "$msg" =~ ^"$prefix":.+ ]]; then
        valid_prefix=true
        break
    fi
done

# Exit at validation failure
if [ "$valid_prefix" = false ]; then
    echo "Error: Commit message prefix is not one of the allowed prefixes:"
    printf '%s\n' "${pref[@]}"
    exit 1
fi
# Prompt user for confirmation to continue the commit
echo "Commit message: $msg"
read -p "Do you want to continue with this commit? (yes/no): " answer
if [ "$answer" != "yes" ]; then
    echo "Commit aborted."
    exit 1
fi

#Place the file under .git/hooks folder for functioning