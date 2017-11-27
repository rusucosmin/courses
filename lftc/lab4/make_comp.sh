flex lab4.lx
yacc -d --verbose --debug grammar.y
gcc lex.yy.c y.tab.c -o comp
