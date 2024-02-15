## Git pre-commit hook Script

Write a shell script to create a pre-commit hook, that checks the commit message to meet certain conditions before committing.

### Instructions

- define list of allowed prefixes ( add, update, remove, refactor, bug-fix, document  )
- once user commits, capture the commit message and validated if the message has one of the defined prefixes
- commit message format should be `prefix:` followed by some text
- move the script file to `.git/hook/pre-commit`
- test the pre-commit hook with provided samples


### sample commit message

**valid list**
- add: new feature
- update: file1 with changes
- remove: file2 and file3
- refactor: file1 for performance


**valid list**
- updated: all files
- remove file1 and remove: file2
- Added: extra features
- Test: test1 file
- bug-Fix: file-x

### Shell Script

```sh

#!/bin/bash
## Pre-commit hook script for checking commit message
# Author Name: Susheel Pogaku
# Publish Date: Feb 14, 2024
# Last Updated: Feb 14, 2024

## define the list of allowed commit message prefixes
## get the commit message
## validate the prefix from list of allowed prefixes
## exit with warning if validation fails ( show allowed list of prefixes )
## prompt user for confirmation to continue the commit ( show commit message and ask for yes/no prompt )
## commit the message, exit otherwise
```
