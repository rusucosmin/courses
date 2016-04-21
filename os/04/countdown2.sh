#!/bin/bash

N=$1
if ! echo $N | grep -q '^[0-9]\+$'; then
    echo "ERROR: I want a number!" >&2
    exit 1
fi

if [ $N -eq 0 ]; then
    echo "START!"
else
    echo $N
    sleep 5
    ./countdown2.sh `expr $N - 1`
fi
