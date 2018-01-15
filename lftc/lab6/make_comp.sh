#!/bin/bash
echo "Running 'flex flex.l'"
flex flex.l
echo "Running 'bison -d grammar.y'"
bison -d grammar.y
echo "Compiling and linking both"
gcc  -w -o comp grammar.tab.c lex.yy.c
