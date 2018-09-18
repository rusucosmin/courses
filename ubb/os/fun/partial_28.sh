#!/bin/bash

if [ $# -lt 3 ]
then
    echo "No files to process"
    exit 1
fi

if [ `echo "$2" | grep "[^0-9]\+"` ]
then
    echo "Not a number"
    exit 1
fi

W=$1
N=$2

while [ "$#" -ge 3 ]
do
    if [ ! -f $3 ]
    then
        echo "$3 - Not a file"
    else
        if [ `cat "$3" | grep -o "$W" | wc -l` -eq $N ]
        then
            echo $3
        fi
    fi
    shift
done
