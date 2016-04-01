#!/bin/bash

D=$1
if [ ! -d $d ]
then
    D=.
fi
find $D -type f | while read F; do
    if file $F | grep -q "\<ASCII\>"
    then
        cat $F
    fi
done | grep -o ["a-zA-Z"] | sort | uniq -c | sort -n -r
