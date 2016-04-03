#!/bin/bash

#neamtu.sh: Se dădeau ca argumente niste useri, sa se afișeze de cate ori
#s-au logat in zilele de luni si sa se sorteze in ordinea inversa a logarilor

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
