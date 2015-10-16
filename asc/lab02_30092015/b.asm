ASSUME cs:code, ds:data

data SEGMENT
	a dw 10
	b db 2
	x dw ?
data ENDS

code SEGMENT
start:
	mov ax,data
	mov ds,ax
	; in signed nu trebuie pus 0 in high, ci trebuie sa apelez
	; cbw
	mov ax,a
	mov bx,0
	mov bl,b
	add ax,bx
	mov x,ax

	mov ax,4C00h
	int 21h
code ENDS
End start
