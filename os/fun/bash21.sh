#!/bin/bash

#Write the script that monitors the content of a given file. 
#Whenever the file changes, it should display the changed content.

if [ $# -ne 1 ]
then
    echo "One argument expected"
    exit 1
fi

if [ ! -f $1 ]
then
    echo "Not a file"
    exit 1
fi

last=`cat $1`
while true
do
    act=`cat $1`
    #echo `diff <(echo $last) <(echo $act)`
    DIFF=`diff <(echo "$last") <(echo "$act")`
    if [ "$DIFF" != "" ]
    then
        echo "File has changed"
    fi
    last=$act
    sleep 1
done
