#!/bin/bash

#bogdan.sh Se primeste ca parametrii un n Si mai multe foldere 
#Sa se afiseze folderele care au dimensiunea peste n

if [ $# -lt 2 ]
then
	echo "Not enough args"
	exit 1
fi

N=$1

if [ `echo "$1" | grep "[^0-9]\+"` ]
then
	echo "$N - Not a number"
	exit 1
fi

while [ $# -gt 1 ]
do
	D=$2	
	if [ ! -d $D ]
	then
		echo ""$D" : Not a directory"
	else
		if [ `du "$D" | awk '{print $1}'` -ge $N ]
		then
			du "$D"
		fi
	fi
	shift
done
