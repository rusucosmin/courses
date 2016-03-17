#!/bin/bash

while [ "$1" != "" ]; do
    if [ ! `echo $1 | grep '[0-9]\+'` ]; then
        echo "Not a number. I can't take the primality test on non-numbers...";
    else
        echo "Parmeter: $1";
        prime = 1;
        if [ $1 -lt 2 ]; then
            prime = 0;
        fi
    fi
    shift

done;
