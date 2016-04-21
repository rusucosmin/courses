#!/bin/bash

for V in asdf qwer 1234 zxvc rtyu; do
    echo $V
done
echo =====
for V in $*; do
    echo $V
done
echo =====
for V in *; do
    echo $V
done
echo =====
for V in blah blah ../03/*t* ./* ../*; do
    echo $V
done
