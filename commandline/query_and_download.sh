#!/bin/bash

# Download a set of files matching some attributes or annotations using synapse query
# For example, get all files in a particular directory (may need to change parentId)
# Then use xargs to download them all to the current directory

synapse query "select id from file where parentId=='syn2512369'" | tail -n +2 | xargs -n 1 -I{} synapse get {}
