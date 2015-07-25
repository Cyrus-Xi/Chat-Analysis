#!/usr/bin/env bash

# For every directory in current directory, move the child *log.html file up one 
# level and name it after its parent directory.
for i in *; do
    mv -i "$i/[multi-way]log.html" "$i.html"
done
