%{
  #include <stdlib.h>
  #include <string.h>
  #include <math.h>
  #include "decl.h"
  #include "grammar.tab.h"
  #define NSYMS   100

  int pifLen = 0;
  int idx = 0;
  int len = 0;
  int iCode = 0;
  int cCode = 1;
  PIF program[500];
  ST symtbl[50];
  ST stid[50];
  int stidlen = 0;
  int line = 1;

  void addPIF(int key, int value) {
    program[pifLen].key = key;
    program[pifLen].value = value;
    pifLen ++;
  }

  void printPIF() {
    printf("PIF\n");
    for(int t = 0; t < pifLen; t ++) {
      if(program[t].key != iCode && program[t].key != cCode) {
        printf(" %d   0 ", program[t].key);
        printf("\n");
      } else {
        printf(" %d   %d ", program[t].key, program[t].value);
        printf("\n");
      }
    }
  }

  void addConst(char* token) {
    int found = 0;
    int i = 0;
    while(i < len) {
      if (strcmp(symtbl[i].key, token) == 0) {
        found = 1;
        addPIF(cCode, i);
      }
      i ++;
    }
    if (found == 0) {
      strcpy(symtbl[len].key, token);
      addPIF(cCode, len);
      len ++;
    }
  }

  void addId(char* token) {
    int found = 0;
    int i = j0;
    while(i < stidlen) {
      if(strcmp(stid[i].key, token)==0) {
        found = 1;
        addPIF(iCode, i);
      }
      i ++;
    }
    if (found == 0) {
      strcpy(stid[stidlen].key, token);
      addPIF(iCode, stidlen);
      stidlen ++;
    }
  }

  void printST() {
    printf("ST const\n");
    for(int i = 0; i < len; i ++) {
      printf("%s   %d", symtbl[i].key, i);
      printf("\n");
    }
    printf("\n");
    printf("ST ID\n");
    for(int i = 0; i < stidlen; i ++) {
      printf("%s  %d", stid[i].key, i);
      printf("\n");
    }
    printf("\n");
  }

  void printAll() {
    printPIF();
    printST();
  }
%}

%option noyywrap
id                      [a-zA-Z][a-zA-Z0-9_]*
digit                   [0-9]
no                      [1-9][0-9]*
errI                    [0-9_]*[a-z]
errC                    [0]*[1-9]*

%%
{digit}                 {int i;sscanf(yytext,"%d",&i);yylval.intval = i; return CONST;}
{no}                    {int i;sscanf(yytext,"%d",&i);yylval.intval = i;return CONST;}
{digit}+"."{digit}{no}  {int i;sscanf(yytext,"%d",&i);yylval.intval = i; return CONST;}
\if                     {return IF;}
then                    {return THEN;}
else                    {return ELSE;}
cin                     {return CIN;}
cout                    {return COUT;}
int                     {return INT;}
\#include               {return INCLUDE;}
using                   {return USING;}
namespace               {return NAMESPACE;}
return                  {return RETURN;}
\>>                     {return GG;}
\!=                     {return NE;}
\<<                     {return LL;}
\<                      {return LT;}
\>                      {return GT;}
\=                      {return '=';}
\==                     {return EE;}
\id                     {addId(yytext);yylval.attributes.varn=strdup(yytext);return ID;}
\const                  {int i;sscanf(yytext,"%d",&i);yylval.intval = i;printf("i=%d",i);return CONST;}
\+                      {return '+';}
\-                      {return '-';}
\*                      {return '*';}
\/                      {return '/';}
\(                      {return '(';}
\)                      {return ')';}
\;                      {return ';';}
\{                      {return '{';}
\}                      {return '}';}
{id}                    {addId(yytext);yylval.attributes.varn=strdup(yytext);return ID;}
{errI}                  {printf("Error [%s]\n",yytext);}
{errC}                  {printf("Error [%s]\n",yytext);}
[ \t]+
[\n\r]                  ++line;
.                       {printf("Error [%s]\n",yytext);}

