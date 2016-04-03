#!/bin/bash

# Display a report showing the full name of all the users currently 
# connected, and the number of processes belonging to each of them.

for i in `ps aux | tail -n +2 | awk '{print $1}'`
do
    name=`cat /etc/passwd | grep "^$i\>" | awk -F':' '{print $5}'`
    echo $name
done | sort | uniq -c | sort -n -r
