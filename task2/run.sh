#!/bin/bash

mkdir -p $3 || exit 1 > /dev/null 2>&1
find $1  -name  "*.$2" -exec cp '{}' $3 \; > /dev/null 2>&1
tar -czf $4 $3 > /dev/null 2>&1
echo  "done"
