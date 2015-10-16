ASSUME cs:code, ds:data

data SEGMENT
	a db 10 
	b dw 20 
	c db 7
	x dw ?
data ENDS

code SEGMENT
start:
	mov ax,data
	mov ds,ax

	mov ax,0 ;; ax = 0
	mov al,a ; ax = ah(0) + al(a) al = a
	mov bx,b ; bx = b
	add ax,bx ; ax = ax + bx = a + b
	mov bx,0 ; bx = 0
	mov bl,c ; bl = c

	sub ax,bx ; ax = ax - c

	mov x,ax

	mov ax,4C00h
	int 21h
code ENDS
end start

