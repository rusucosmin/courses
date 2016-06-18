#!/bin/bash

for file in `ls *.txt`;
do
    if [ "`cat "$file" | grep "cat"`" != "" ];
    then
        echo $file
    fi
done
