#!/bin/bash

for i in "$@";
do
    if [ $(($i % 2)) -eq 0 ];
    then
        echo $i
    fi
done
