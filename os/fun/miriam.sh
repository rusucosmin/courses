#!/bin/bash

while true
do
	clear
	echo "Checking"
	for usr in `cat cosmin.txt`
	do
		cnt=`ps aux | grep "^$usr\>" | grep -c "vim"`
		ps aux | grep "^$usr\>" | grep "vim"
		if [ $cnt -gt 0 ]
		then
			echo $cnt
			echo $usr is using man or vim
		fi
	done
	sleep 1
done
