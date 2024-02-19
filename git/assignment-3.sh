# #!/bin/bash
# ## Pre-commit hook script for checking commit message
# # Author Name: Ananya Paliwal
# # Publish Date: Feb 14, 2024
# # Last Updated: Feb 19, 2024

exec < /dev/tty 
commit_message_file="$1"  
          
commit_message=$(cat "$commit_message_file")


allowed_prefixes=("add" "update" "remove" "refactor" "bug-fix" "document")
prefix_valid=false
for prefix in "${allowed_prefixes[@]}"; do
    if [[ "$commit_message" == "${prefix}"* ]]; then
        prefix_valid=true
        break
    fi
done

if [ "$prefix_valid" != true ]; then
    echo "Error: Invalid commit message. Allowed prefixes are: ${allowed_prefixes[@]}"
    exit 1
fi

echo "Commit message: $commit_message"
read -p "Do you want to continue with the commit? (yes/no): " choice

case "$choice" in
    yes)
        exit 0
        ;;
    *)
        echo "Commit aborted by user."
        exit 1
        ;;
esac


