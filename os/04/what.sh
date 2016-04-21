#!/bin/bash

if echo $1 | grep -q '^[a-z]$'; then
    echo Letter
elif echo $1 | grep -q '^[0-9]$'; then
    echo Digit
else
    echo Something else
fi

case $1 in
    [0-9] ) echo Digit ;;
    [a-z] ) echo Letter ;;
    * ) echo Something else ;;
esac
