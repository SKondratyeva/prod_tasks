#!/bin/bash

mkdir -p $3 || exit 1
find $1  -name  "*.$2" -exec cp '{}' $3 \;
tar -czvf "$3.tar.gz" $3
echo  "done"
