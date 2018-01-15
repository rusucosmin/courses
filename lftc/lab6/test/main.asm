assume cs:code,ds:data
data segment
	t1 dw ?
	t2 dw ?
	t3 dw ?
	t4 dw ?
	t5 dw ?
	t6 dw ?
	t7 dw ?
	t8 dw ?
	t9 dw ?
	t10 dw ?
	c dw ?
	b dw ?
	a dw ?
	
newl db ,13,10,"$"
		string db 5
		db ?
		db 5 dup (?)
data ends
code segment
start:
mov ax,data
mov ds,ax



call readInput
mov a,bx

call readInput
mov b,bx






mov ax,1
mov t1,ax

mov ax,a
mov bx,t1
add ax,bx
mov t2,ax



mov ax,t2
mov bx,5
cmp ax,bx
jle label1
mov ax,a
call disp
mov ax,b
call disp



label1:









mov ax,1
mov t3,ax

mov ax,b
mov bx,t3
sub ax,bx
mov t4,ax
mov ax,t4
mov t5,ax

mov ax,t5
mov t6,ax

mov ax,a
mov bx,t6
mul bx
mov t7,ax


mov ax,t7
mov t8,ax


mov ax,t8
mov t9,ax

mov ax,1
mov bx,t9
add ax,bx
mov t10,ax
mov ax,t10
mov c,ax

mov ax,c
call disp









mov ah,4ch
int 21h

disp proc
MOV BX, 10
MOV DX, 0000H
MOV CX, 0000H
.Dloop1:
MOV DX, 0000H
div BX
PUSH DX
INC CX
CMP AX, 0
JNE .Dloop1
.Dloop2:
POP DX
ADD DX, 30H
MOV AH, 02H
INT 21H
LOOP .Dloop2
mov dx,offset newl
mov ah,09h
int 21h
RET
 disp ENDP
readInput proc
mov  ah, 0Ah
mov  dx, offset string
int  21H
call string2number
ret
readInput endp
string2number proc
;MAKE SI TO POINT TO THE LEAST SIGNIFICANT DIGIT.
mov  si, offset string + 1 ;NUMBER OF CHARACTERS ENTERED.
mov  cl, [ si ] ;NUMBER OF CHARACTERS ENTERED.
mov  ch, 0 ;CLEAR CH, NOW CX==CL.
add  si, cx ;NOW SI POINTS TO LEAST SIGNIFICANT DIGIT.
;CONVERT STRING.
mov  bx, 0
mov  bp, 1 ;MULTIPLE OF 10 TO MULTIPLY EVERY DIGIT.
repeat:
;CONVERT CHARACTER.
mov  al, [ si ] ;CHARACTER TO PROCESS.
sub  al, 48 ;CONVERT ASCII CHARACTER TO DIGIT.
mov  ah, 0 ;CLEAR AH, NOW AX==AL.
mul  bp ;AX*BP = DX:AX.
add  bx,ax ;ADD RESULT TO BX
;INCREASE MULTIPLE OF 10 (1, 10, 100...).
mov  ax, bp
mov  bp, 10
mul  bp ;AX*10 = DX:AX.
mov  bp, ax ;NEW MULTIPLE OF 10.
;CHECK IF WE HAVE FINISHED
dec  si ;NEXT DIGIT TO PROCESS.
loop repeat ;COUNTER CX-1, IF NOT ZERO, REPEAT.
ret
string2number endp
code ends
end start
