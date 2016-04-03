#!/bin/bash

# count.sh ceva de genu sa verifici daca argumentele sunt fisiere sau numere
# si sa numeri cate sunt fisiere

files=0
numbers=0
for arg in $@
do
	if [ -f "$arg" ]
	then
		files=$((files+1))	
	else
		if [ ! `echo "$arg" | grep "[^0-9]\+"` ]
		then
			numbers=$((numbers+1))
		fi
	fi
done
echo "$files Files"
echo "$numbers Numbers"
