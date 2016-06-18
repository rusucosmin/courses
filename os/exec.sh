#!/bin/bash

for i in "$@";
do
    if [ -f $i ] && [ -x "$i" ];
    then
        echo $i is executable
    fi
done
