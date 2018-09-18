#!/bin/bash

for file in "$@";
do
    if [ -f "$file" ];
    then
        cp "$file" "$file.file"
    fi
done
