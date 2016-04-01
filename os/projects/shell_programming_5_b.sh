#!/bin/bash

while [ "$1" != "" ]; do
    if [ `echo $1 | grep '[^0-9]\+'` ]; then
        echo "$1 Not a number. I can't take the primality test on non-numbers...";
    else
        prime=1;
        if [ $1 -lt 2 ]; then
            prime=0;
        fi
        d=2;
        while [[ $prime -eq 1 && `expr $d \* $d` -le $1 ]]; do
            if [ `expr $1 % $d` -eq 0 ]; then
                prime=0;
            fi
            d=`expr $d + 1`;
        done
        if [ $prime -eq 1 ]; then
            echo "$1 is prime";
        else
            echo "$1 is NOT prime";
        fi
    fi
    shift
done;
