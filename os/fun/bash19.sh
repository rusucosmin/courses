#!/bin/bash

#Find recursively in a directory all ".c" files having more than 500 lines. 
#Stop after finding 10 such files.

find /home/cosmin/work/cplusplus/ -type f -name "*.cpp" | while read SF; do
    lines=`wc -l "$SF" | awk '{print $1}'`
    if [ $lines -ge 500 ]; then
        echo "$lines $SF"
        CNT=$((CNT + 1))
        if [ $CNT -eq 10 ]; then
            break
        fi
    fi
done
