#!/bin/bash

cnt=0
sum=0
for arg in "$@";
do
    cnt=$(($cnt+1))
    if [ $(($cnt % 3)) -eq 0 ];
    then
        sum=$(($sum+$arg))
    fi
done
echo $sum
