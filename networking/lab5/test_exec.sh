#!/bin/bash
cmds=("ls -l" "pwd" "time" "man yes" "uptime")

i=0
for cmd in "${cmds[@]}"
do
	echo "python exec_server $cmd"
	python exec_client.py $cmd > $i.out &
	i=$((i+1))
done
