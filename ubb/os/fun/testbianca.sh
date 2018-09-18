#!/bin/bash

while [ $# -gt 0 ]
do
    if [ `echo "$1" | grep '[0-9]\+'` ]
    then
        echo $1 is a number
    else
        echo $1
    fi
    shift
done
