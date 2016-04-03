#!/bin/bash

#miriam.sh: sa monitorizez procesele si daca un utilizator folosea vim 
#sau man sa se afiseze un mesaj ca este o operatie ilegala,ceva de genul:))

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
