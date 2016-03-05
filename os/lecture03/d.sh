#!/bin/bash

D=""
while true; do
    read -p "Directory: " D
    if [ -z "$D" ]; then
        continue
    fi
    if [ ! -d "$D" ]; then
        echo "ERROR: \"$D\" is not a directory" >&2
        continue
    fi
    break
done

E=""
while [ -z "$E" ]; do
    read -p "Extension: " E
done






SUM=0
for F in `find $D -name "*.$E"`; do
    LC=`wc -l $F | cut -d\  -f 1`
    SUM=`expr $LC + $SUM`
done
echo $SUM
