#!/bin/bash

#secelean.sh: Sa citesc nume de fisiere de la tastatura pana doua
#citite consecutiv ocupa acelasi size in bytes si au aceleasi drepturi

lastb=0
while true
do
	read -p "File: " F
	if [ ! -f "$F" ]
	then
		echo ""$F" - not a file"
	else
		actb=`du -b "$F" | awk '{print $1}'`
		if [ $actb -eq $lastb ] && [ `stat $F == 
		then
			echo "bye bye"
			break
		fi
		lastb=$actb
	fi
done
