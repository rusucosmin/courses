#!/bin/bash

if [ `expr $# % 2` -eq 1 ]
then
    echo "Even arguments expected"
    exit 1
fi

while [ $# -ge 2 ]
do
    if [ ! -f $2 ]
    then
        echo "$2 - Not a file"
    else
        if [ `cat "$2" | grep $1 | wc -l` -ge 5 ]
        then
            echo "$2 is good"
        fi
    fi
    shift
    shift
done
