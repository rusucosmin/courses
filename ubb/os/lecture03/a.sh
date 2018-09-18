#!/bin/bash

for A in cat dog piggy; do
    echo Hello $A
done

#for E in a@a.c b@b.c; do
#    mail ... $E ...
#done

#for F in ../02/*.txt; do
#    ls -l $F
#done

N=0
for W in `cat grades.txt`; do
    N=`expr $N + 1`
done
echo $N

SUM=0
for F in `find ~ -name "*.txt"`; do
    LC=`wc -l $F | cut -d\  -f 1`
    SUM=`expr $LC + $SUM`
done
echo $SUM









