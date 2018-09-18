#!/bin/bash


for file in "$@";
do
    if [ -x $file ] && [ -r $file ];
    then
        echo $file
    fi
done
