#!/bin/bash

D=$1
S=$2

for F in `find $D -type f`; do
    K=`ls -l $F | awk '{print $5}'`
    if [ $K -ge $S ]; then
        echo $K $F
    fi
done
