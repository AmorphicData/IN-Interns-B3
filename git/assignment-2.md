## Automated Backup Script

Write a shell script to create backup of a specified directory, commit changes, and push them to a remote Git repository.

### Instructions

- Clone a git repo (source)
- Create an empty directory (if not exist) (backup)
- Make changes in source directory then run the script
- Script should copy the changed files to backup directory
- Initialize the backup directory with git using the remote_repository address
- Commit and push the changes in backup directory to remote_repo
- Using Cron, set schedule of 5mins to run this script

### Shell Script

```sh

#!/bin/bash
## automated backup script
# Author Name: Susheel Pogaku
# Publish Date: Feb 14, 2024
# Last Updated: Feb 14, 2024

## define variables
## check source directory exist, exit otherwise
## check remote directory exist, create one otherwise
## check if changes are available in source directory, exit if no changes
## copy changes to remote directory
## initialize git on remote directory if not already initialized
## commit and push to remote_repo (to your branch only)

```
