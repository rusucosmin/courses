#!/bin/bash

while true
do
	read -p "username: " U
	if [ "$U" == "exit" ]
	then
		echo "Bye bye"
		break
	fi
	if [ `cat /etc/passwd | awk -F':' '{print $1}' | grep -c "\<$U\>"` -ne 1 ]
	then
		echo "$U is not user"
		continue
	else
		echo "Last logins for $U"
		last | grep "$U" | head -3
	fi
done
