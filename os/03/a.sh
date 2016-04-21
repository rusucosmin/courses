#!/bin/bash

R=`./p 17 17 | sed 's/\..*//'`

if test $R -gt 5; then
    echo Great
else
    echo Not so great
fi

if [ $R -gt 5 ] || [ $R -lt 10 ]; then
    echo Great
else
    echo Not so great
fi

A=1
B=1
while [ `./p $A $B | sed 's/\..*//'` -lt 5 ]; do
    A=`expr $A + 1`
    B=$A
    echo $A $B
done
