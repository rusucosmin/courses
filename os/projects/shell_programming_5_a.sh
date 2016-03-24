#!/bin/bash
S=$1

if [ ! `echo "$S" | grep '[0-9]\+'` ]; then
    echo "Not a number!"
    exit 1
fi

while true; do
    read -p "n = " N
    if [ `echo $N | grep "[0-9]\+"` ]; then
        break
    fi
    echo "Not a number!";
done


while true; do
    clear
    ps aux | tail -n +2 | awk '{print $1}' | sort | uniq -c | sort -n -r | head -n $N
    sleep $S
done
