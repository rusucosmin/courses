#!/bin/bash

for usr in $@
do
	if [ `cat /etc/passwd | grep -o "^$usr:.*" | wc -l` -eq 0 ]
	then
		echo "$usr is not a user" 1>&2
	else
		logcnt=`last "$usr" | head -n -2 | grep "Mar" | wc -l`
		echo "$logcnt $usr "
	fi 
done | sort -n -r
