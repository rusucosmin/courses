#!/bin/bash

SUM=0
for F in `find $1 -name "*.txt"`; do
    LC=`wc -l $F | cut -d\  -f 1`
    SUM=`expr $LC + $SUM`
done
echo $SUM
