#!/bin/bash

#neagos.sh 
#Sa se scrie un script care tot citeste de la utilizator (nu neaparat numere) 
#pana se introduce de trei ori consecuvtiv un numar par mai mare decat 10.

#tananana SO

cnt=0

while true
do
	read -p "Input: " U
	if [ ! `echo "$U" | grep "[^0-9]\+"` ] && [ `expr "$U" % 2` -eq 0 ] && [ "$U" -ge 10 ]
	then
		cnt=$((cnt+1))
	else
		cnt=0
	fi
	if [ $cnt -eq 3 ]
	then
		echo "Bye bye bye"
		break
	fi
done
