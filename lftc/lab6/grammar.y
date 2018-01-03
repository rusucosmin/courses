%{
#include <stdio.h>
#include <string.h>
#include <math.h>

char vars[250][250];
int cntvar;
int vals[250];

void add_var(char *var) {
  for(int i = 0; i < cntvar; ++ i) {
    if(strcmp(vars[i], var) == 0) {
      fprintf(stderr, "Error: identifier %s redeclared\n", var);
      exit(0);
    }
  }
  fprintf(stderr, "Adding variable %s\n", var);
  strcpy(vars[cntvar], var);
  vals[cntvar] = 0;
  ++ cntvar;
}

void assign(char *var, int val) {
  for(int i = 0; i < cntvar; ++ i) {
    if(strcmp(vars[i], var) == 0) {
      vals[i] = val;
      return ;
    }
  }
  fprintf(stderr, "Error: identifier %s not declared\n", var);
}

int var_val(char *var) {
  for(int i = 0; i < cntvar; ++ i) {
    if(strcmp(vars[i], var) == 0) {
      return vals[i];
    }
  }
  fprintf(stderr, "Error: Use of undeclared indentifier %s\n", var);
}

void yyerror(const char *str) {
  fprintf(stderr,"> Error: %s.\n",str);
  exit(0);
}

int yywrap() {
  return 1;
}

int yydebug = 1;

int main(argc, argv)
int argc;
char **argv;
{
  main_lex(argc, argv);
  yyparse();
  fprintf(stdout, "> Finished: No syntax errors\n");
}

%}


%token ID INT CHAR FLOAT CIN COUT IF ELSE WHILE MAIN OBRACE EBRACE
%token SEMICOLON OPAR EPAR PLUS MINUS MULT DIV MOD GT LT GE LE EQ NOTEQ
%token ASSIGN RETURN

%union
{
  int integer;
  float real;
  char *text;
}

%token <integer> INTEGER
%token <float> REAL
%token <text> TEXT

%type <text> ID
%type <integer> constant
%type <integer> expr
%type <integer> condition
%type <integer> return

%start program

%%
program:
        | INT MAIN OPAR EPAR compound_stmt
        ;

type: INT
    | FLOAT
    ;

compound_stmt:
        | OBRACE stmt_list EBRACE
        ;

stmt_list:
        | stmt_list stmt ;

stmt: decl SEMICOLON {
    }
    | assign SEMICOLON {
    }
    | return SEMICOLON {
    }
    | iostmt SEMICOLON {
    }
    | loop {
    }
    | if_stmt {
    }
    ;

decl:
    type ID {
      if(strlen(yylval.text) > 250) {
        fprintf(stderr, "Error: identifier %s is too long (more than 250 character limit)\n", yylval.text);
        exit(0);
      }
      add_var($2);
    }
    ;

assign: ID ASSIGN expr {
      assign($1, $3);
    }
    ;

constant: INTEGER {
      $$ = $1;
    }
    ;

expr: ID {
      $$ = var_val($1);
    }
    | constant {
      $$ = $1;
    }
    | expr PLUS ID {
      $$ = $1 + var_val($3);
    }
    | expr MINUS ID {
      $$ = $1 - var_val($3);
    }
    | expr MULT ID {
      $$ = $1 * var_val($3);
    }
    | expr DIV ID {
      $$ = $1 / var_val($3);
    }
    | expr MOD ID {
      $$ = $1 % var_val($3);
    }
    | expr PLUS constant {
      $$ = $1 + $3;
    }
    | expr MINUS constant {
      $$ = $1 - $3;
    }
    | expr MULT constant {
      $$ = $1 * $3;
    }
    | expr DIV constant {
      $$ = $1 / $3;
    }
    | expr MOD constant {
      $$ = $1 % $3;
    }
    | OPAR expr EPAR {
      $$ = $2;
    }
    ;

return: RETURN expr {
      $$ = $2;
    }
    ;

iostmt: input
    | output
    ;

input: CIN ID {
      int x;
      scanf("%d", &x);
      assign($2, x);
    }
    ;
output:
    COUT expr {
      printf("%d", $2);
    }
    ;

loop: WHILE OPAR condition EPAR compound_stmt
    ;

condition: expr EQ expr {
      $$ = ($1 == $3);
    }
    | expr NOTEQ expr {
      $$ = ($1 != $3);
    }
    | expr LT expr {
      $$ = ($1 < $3);
    }
    | expr LE expr {
      $$ = ($1 <= $3);
    }
    | expr GT expr {
      $$ = ($1 > $3);
    }
    | expr GE expr {
      $$ = ($1 >= $3);
    }
    ;

if_stmt: IF OPAR condition EPAR compound_stmt {
      if($3) {
      }
    }
    | IF OPAR condition EPAR compound_stmt ELSE compound_stmt {
      if($3) {
      }
    }
    ;
%%
