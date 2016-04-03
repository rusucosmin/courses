#!/bin/bash

# last3.sh: Se dau nume de utilizatori in linia de comanda pe care 
#eu trebuie sa le citesc , si pt fiecare, trebuie sa afisez ultimele 3 logari

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
