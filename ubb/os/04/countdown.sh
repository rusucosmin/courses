#!/bin/bash

N=$1
if ! expr $N + 0 > /dev/null 2>&1; then
    echo "ERROR: I want a number!" >&2
    exit 1
fi

# Alternative way of checking
if ! echo $N | grep -q '^[0-9]\+$'; then
    echo "ERROR: I want a number!" >&2
    exit 1
fi

while [ $N -gt 0 ]; do
    echo $N
    N=`expr $N - 1`
    sleep 1
done
echo "START!"
