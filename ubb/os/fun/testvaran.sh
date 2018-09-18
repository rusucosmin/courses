#!/bin/bash

while [ $# -ge 2 ]
do
    if [ ! -f $2 ]
    then
        echo "$2 - not a file"
        break
    fi
    if [ `grep -o "$1" "$2" | wc -l` -ge 2 ]
    then
        echo $2
    fi
    shift
    shift
done
