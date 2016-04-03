#!/bin/bash

lastb=0
while true
do
	read -p "File: " F
	if [ ! -f "$F" ]
	then
		echo ""$F" - not a file"
	else
		actb=`du -b "$F" | awk '{print $1}'`
		if [ $actb -eq $lastb ]
		then
			echo "bye bye"
			break
		fi
		lastb=$actb
	fi
done
