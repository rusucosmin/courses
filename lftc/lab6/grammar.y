%{
  #include <string.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include "decl.h"
  extern int yylex();
  extern int yyparse();
  extern FILE *yyin;
  extern int line;
  extern void printAll();
  void yyerror(const char *s);
  int t = 1;
  int lbl = 1;
  char * NewTempName() {
    char temp[10];
    sprintf(temp,"%d",t++);
    char tc[10];
    tc[0] = 't';
    return strdup(strcat(tc,temp));
  }
  char * NewLabelName() {
    char temp[10];
    char l[10];
    sprintf(l,"label");
    sprintf(temp,"%d",lbl++);
    return strdup(strcat(l,temp));
  }
  char* result;
  char* display_function = "\ndisp proc\nMOV BX, 10\nMOV DX, 0000H\nMOV CX, 0000H\n.Dloop1:\nMOV DX, 0000H\ndiv BX\nPUSH DX\nINC CX\nCMP AX, 0\nJNE .Dloop1\n.Dloop2:\nPOP DX\nADD DX, 30H\nMOV AH, 02H\nINT 21H\nLOOP .Dloop2\nmov dx,offset newl\nmov ah,09h\nint 21h\nRET\n disp ENDP"
                            "\nreadInput proc"
                            "\nmov  ah, 0Ah"
                            "\nmov  dx, offset string"
                            "\nint  21H"
                            "\ncall string2number"
                            "\nret"
                            "\nreadInput endp"

                            "\nstring2number proc"
                            "\n;MAKE SI TO POINT TO THE LEAST SIGNIFICANT DIGIT."
                              "\nmov  si, offset string + 1 ;NUMBER OF CHARACTERS ENTERED."
                              "\nmov  cl, [ si ] ;NUMBER OF CHARACTERS ENTERED.\nmov  ch, 0 ;CLEAR CH, NOW CX==CL."
                              "\nadd  si, cx ;NOW SI POINTS TO LEAST SIGNIFICANT DIGIT."
                            "\n;CONVERT STRING."
                              "\nmov  bx, 0"
                              "\nmov  bp, 1 ;MULTIPLE OF 10 TO MULTIPLY EVERY DIGIT."
                            "\nrepeat:"
                            "\n;CONVERT CHARACTER."
                              "\nmov  al, [ si ] ;CHARACTER TO PROCESS."
                              "\nsub  al, 48 ;CONVERT ASCII CHARACTER TO DIGIT."
                              "\nmov  ah, 0 ;CLEAR AH, NOW AX==AL."
                              "\nmul  bp ;AX*BP = DX:AX."
                              "\nadd  bx,ax ;ADD RESULT TO BX"
                            "\n;INCREASE MULTIPLE OF 10 (1, 10, 100...)."
                              "\nmov  ax, bp"
                              "\nmov  bp, 10"
                              "\nmul  bp ;AX*10 = DX:AX."
                              "\nmov  bp, ax ;NEW MULTIPLE OF 10."
                            "\n;CHECK IF WE HAVE FINISHED"
                              "\ndec  si ;NEXT DIGIT TO PROCESS."
                              "\nloop repeat ;COUNTER CX-1, IF NOT ZERO, REPEAT."
                              "\nret"
                            "\nstring2number endp";
    char* vars= "\t\nnewl db "  ",13,10,\"$\""
                "\n\t\tstring db 5"
                    "\n\t\tdb ?"
                    "\n\t\tdb 5 dup (?)";
%}

%union {
  struct{
    char* code;
    char* varn;
  } attributes;
  struct {
    char* code;
    char* lbl_Else;
    char* lbl_After;
  } ifAttr;
  struct {
    char* code;
    char* varn;
    char* op;
  } exprAttr;
  int intval;
}
%token <intval> CONST
%token <attributes> ID
%token IF
%token THEN
%token ELSE
%token LT
%token CIN
%token COUT
%token GG
%token LL
%token INCLUDE
%token USING
%token RETURN
%token NAMESPACE
%token GT
%token INT
%token EE
%token NE
%type <attributes> stmt
%type <attributes> assign_stmt
%type <attributes> iostmt
%type <attributes> program
%type <attributes> antet
%type <attributes> expression
%type <exprAttr> expression1
%type <attributes> term
%type <exprAttr> term1
%type <attributes> factor
%type <attributes> stmt_list
%type <attributes> stmt_list1
%type <attributes> declstmt
%type <attributes> ifstmt
%type <attributes> boolOp
%type <attributes> cond
%%
program: antet '{' stmt_list RETURN CONST ';' '}'
            {
                char temp[10000];
                char ids[500];
                for(int i = 1;i<t;i++)
                {
                    strcat(ids,"\tt");
                    char no[10];
                    sprintf(no,"%d",i);
                    strcat(ids,no);
                    strcat(ids," dw ?\n");
                }

                strcat(ids,vars);
                sprintf(temp,"assume cs:code,ds:data\ndata segment\n%s\ndata ends\ncode segment\nstart:\nmov ax,data\nmov ds,ax\n%s\nmov ah,4ch\nint 21h\n%s\ncode ends\nend start\n",ids,$3.code,display_function);
                $$.code = strdup(temp);
                printf("Assembly code:\n\n%s\n",$$.code);
                result = strdup($$.code);
            }

antet: INCLUDE LT ID GT USING NAMESPACE ID ';' INT ID '('')'
            {
                $$.code="";
                $$.varn="";
            }

stmt_list:stmt stmt_list1
            {
                char temp[10000];
                sprintf(temp,"%s\n%s\n",$1.code,$2.code);
                $$.code=strdup(temp);
                $$.varn="";
            }
stmt_list1:stmt_list
            {
                $$.code=strdup($1.code);
                $$.varn="";
            }
stmt_list1:
            {
                $$.code="";
                $$.varn="";
            }
stmt:ifstmt
            {
                $$.code=strdup($1.code);
                $$.varn="";
            }
    |
    assign_stmt
            {
                $$.code=strdup($1.code);
            }
    |
    iostmt
            {
                $$.code=strdup($1.code);
            }
    |
    declstmt
            {
                $$.code ="";
                $$.varn="";
            }

expression:term expression1
            {
                char temp[5000];
                if(strcmp($2.op,"-")==0)
                {
                    $$.varn = $1.varn;
                    sprintf(temp,"%s\n",$1.code);
                    //sprintf(temp,"%s\n%s\nmov ax,%s\nmov %s,ax\n",$1.code,$2.code,$1.varn,$$.varn);
                }
                else
                {
                    $$.varn = NewTempName();
                    sprintf(temp,"%s\n%s\nmov ax,%s\nmov bx,%s\n%s ax,bx\nmov %s,ax",$1.code,$2.code,$1.varn,$2.varn,$2.op,$$.varn);
                }
                $$.code=strdup(temp);
            }
expression1:'+' expression
            {
                $$.op="add";
                $$.varn=NewTempName();
                char temp[5000];
                sprintf(temp,"%s\nmov ax,%s\nmov %s,ax\n",$2.code,$2.varn,$$.varn);
                $$.code=strdup(temp);
            }
expression1:'-' expression
            {
                $$.op="sub";
                $$.varn=NewTempName();
                char temp[1000];
                sprintf(temp,"%s\nmov ax,%s\nmov %s,ax\n",$2.code,$2.varn,$$.varn);
                $$.code=strdup(temp);
            }
expression1:
            {
                $$.varn="",$$.code="";$$.op="-";
            }

term:factor term1
            {
                char temp[5000];
                if(strcmp($2.op,"-")==0)
                {
                    sprintf(temp,"%s\n",$1.code);
                    $$.varn = $1.varn;
                }
                else
                {
                    $$.varn=NewTempName();
                    sprintf(temp,"%s\n%s\nmov ax,%s\nmov bx,%s\n%s bx\nmov %s,ax\n",$1.code,$2.code,$1.varn,$2.varn,$2.op,$$.varn);
                }
                $$.code=strdup(temp);
            }
term1:'*' term
            {
                $$.op="mul";
                $$.varn=NewTempName();
                char temp[5000];
                sprintf(temp,"%s\nmov ax,%s\nmov %s,ax\n",$2.code,$2.varn,$$.varn);
                $$.code=strdup(temp);
            }
term1:'/' term
            {
                $$.op="div";
                $$.varn=NewTempName();
                char temp[5000];
                sprintf(temp,"%s\nmov ax,%s\nmov %s,ax\n",$2.code,$2.varn,$$.varn);
                $$.code=strdup(temp);   
            }
term1:
            {
                $$.varn="";$$.code="";$$.op="-";
            }
factor:ID
            {
                $$.varn = strdup($1.varn);
                $$.code="";
            }
factor:CONST
            {
                char temp[10];
                sprintf(temp,"%d",$1);
                $$.varn = strdup(temp);
                $$.code="";
            }
factor:'(' expression ')'
            {
                char temp[1000];
                $$.varn=NewTempName();
                sprintf(temp,"%s\nmov ax,%s\nmov %s,ax",$2.code,$2.varn,$$.varn);
                $$.code=strdup(temp);

            }

ifstmt:IF '(' cond  ')' '{' stmt_list '}'
        {
            /*
                mov ax,expression1.varn
                mov bx,expression2.varn
                cmp ax,bx
                j.. labeli
                stmt_list.code
                labeli:
            */
                char* temp = malloc(1000*sizeof(char));
                char* lbl = NewLabelName();
                sprintf(temp,"%s%s\n%s\n%s:\n",$3.code,lbl,$6.code,lbl);
                $$.code=strdup(temp);
        };


assign_stmt:ID '=' expression ';'
        {
            char temp[500];
            sprintf(temp,"%s\nmov ax,%s\nmov %s,ax\n",$3.code,$3.varn,$1.varn);
            $$.code=strdup(temp);
        }

iostmt:COUT LL ID ';'
        {
            $$.varn="";
            char temp[100];
            sprintf(temp,"mov ax,%s\ncall disp",$3.varn);
            $$.code=strdup(temp);
        }
    |
        CIN GG ID ';'
        {
            $$.varn="";
            char temp[100];
            sprintf(temp,"call readInput\nmov %s,bx\n",$3.varn);
            $$.code=strdup(temp);
        }
declstmt: INT ID ';'
        {
            char* temp = malloc(1000*sizeof(char));

            sprintf(temp,"\t%s dw ?\n",$2.varn);

            strcat(temp,vars);

            vars = strdup(temp);
            $$.code="";
            $$.varn="";
            free(temp);
        }

cond:expression boolOp expression 
        {
            /*
                mov ax,expression1.varn
                mov bx,expression2.varn
                cmp ax,bx
                boolOp.code
            */
            char* temp =malloc(1000*sizeof(char));
            sprintf(temp,"%s\n%s\nmov ax,%s\nmov bx,%s\ncmp ax,bx\n%s ",$1.code,$3.code,$1.varn,$3.varn,$2.code);
            $$.code=strdup(temp);
            free(temp);
            $$.varn="";
        }

boolOp: GT
         {
            $$.code = "jle";
            $$.varn="";
         }
        | LT
        {
            $$.code = "jge";
            $$.varn="";
        }
        |
        EE
        {
            $$.code = "jne";
            $$.varn="";
        }
        |
        NE
        {
            $$.code = "je";
            $$.varn="";
        }
%%
int main(int argc, char *argv[]) {
    ++argv, --argc;

    if (argc > 0){
        yyin = fopen(argv[0], "r"); 
        int c;
        FILE *file;
        printf("Source code: \n");
        file = fopen(argv[0], "r");
        if (file) {
            while ((c = getc(file)) != EOF)
                putchar(c);
            fclose(file);
        }
    }
    else
        yyin = stdin;
    while (!feof(yyin)) {
        yyparse();
    }
    printf("The file is syntactically correct!\n");
    FILE *file = fopen("out.asm", "w");

    int results = fputs(result, file);
    if (results == EOF) {
        //error
    }
    fclose(file);
    return 0;
}

void yyerror(const char *s) {
    printf("Error: %s at line -> %d ! \n", s, line);
    exit(1);
}
