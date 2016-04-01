#!/bin/bash

#Write a shell script that will show on the screen every s seconds, a top of the 
#first n users on the linux system, sorted by the number their running 
#processes (n will be read from keyboard and s from command line).

S=$1

if [ "$S" == "" ] || [ `echo "$S" | grep "[^0-9]\+"` ]; then
    echo "Not a number!"
    exit 1
fi

while true; do
    read -p "n = " N
    if [ ! `echo $N | grep "[^0-9]\+"` ]; then
        break
    fi
    echo "Not a number!";
done


while true; do
    clear
    ps aux | tail -n +2 | awk '{print $1}' | sort | uniq -c | sort -n -r | head -n $N
    sleep $S
done
